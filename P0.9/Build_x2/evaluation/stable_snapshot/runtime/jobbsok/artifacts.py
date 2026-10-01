"""Current semantic artifacts: load, validate, replace, and staleness.

Four obligations meet here.

INV-09 / Contract 4.2 -- stage-scoped write ownership. Under the P0.9.3
amendment Stage 1 replaces only the strategy and Stage 3 only the final and
review; Stage 2 is retired and its draft survives read-only in historical
runs. A downstream stage may not edit an upstream artifact. `submit` is the
only write path and it consults `paths.STAGE_WRITE_MAP`.

Contract 4.2 -- at most one current artifact per semantic role per job.
Replacements are atomic; the superseded copy moves to bounded audit history,
and history is never required for validation or status.

DEC-26 -- staleness is a small fixed invalidation table, not a runtime
dependency graph. Each artifact records the hashes it was written from;
comparison is a dict lookup.

DEC-33 -- hard validation is mechanical only. Semantic-density choices
(requirement counts, competency counts, paragraph counts) emit WARNING and
never fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .atomicio import atomic_write_bytes, atomic_write_json, read_json
from .errors import ConfigurationError, JobError, ValidationResult
from .hashing import sha256_canonical_json, sha256_file
from .paths import (
    Layout,
    STAGE_WRITE_MAP,
    flatten_run_reference,
    owning_stage,
    resolve_within,
)
from .schemas import validate_against_schema

#: artifact name -> (filename, schema name)
ARTIFACTS: dict[str, tuple[str, str]] = {
    "strategy": ("strategy.json", "strategy"),
    "draft_package": ("draft_package.json", "package"),
    "final_package": ("final_package.json", "package"),
    "review": ("review.json", "review"),
}

#: Friendly aliases accepted on the command line.
ALIASES = {"draft": "draft_package", "final": "final_package"}
HANDOFF_DIGEST_CHARS = 16

#: Artifacts an active 0.9.3 run works with, and the four a legacy 0.9.0 run
#: still owns. ARTIFACTS above stays the read catalog for both.
ACTIVE_ARTIFACTS: tuple[str, ...] = ("strategy", "final_package", "review")
LEGACY_ARTIFACTS: tuple[str, ...] = (
    "strategy", "draft_package", "final_package", "review",
)

#: DEC-26 static invalidation table. Replacing the key marks the listed
#: downstream artifacts stale. This is the whole dependency model. Two fixed
#: tables exist, selected by the run's own manifest revision -- never merged,
#: never traversed.
STALE_SCOPE: dict[str, tuple[str, ...]] = {
    "strategy": ("final_package", "review", "render"),
    "final_package": ("review", "render"),
    "review": ("queue",),
    "document_date": ("render",),
}

LEGACY_STALE_SCOPE: dict[str, tuple[str, ...]] = {
    "strategy": ("draft_package", "final_package", "review", "render"),
    "draft_package": ("final_package", "review", "render"),
    "final_package": ("review", "render"),
    "review": ("queue",),
    "document_date": ("render",),
}

#: Which recorded binding hash each artifact checks against which upstream.
UPSTREAM_BINDING: dict[str, tuple[str, str]] = {
    "final_package": ("strategy", "strategy_sha256"),
    "review": ("final_package", "final_package_sha256"),
}

LEGACY_UPSTREAM_BINDING: dict[str, tuple[str, str]] = {
    "draft_package": ("strategy", "strategy_sha256"),
    "final_package": ("draft_package", "draft_sha256"),
    "review": ("final_package", "final_package_sha256"),
}


def _legacy(spec_revision: str | None) -> bool:
    from .manifest import LEGACY_SPEC_REVISION

    return str(spec_revision) == LEGACY_SPEC_REVISION


def active_artifacts(spec_revision: str | None) -> tuple[str, ...]:
    """The artifact names one run actually owns."""
    return LEGACY_ARTIFACTS if _legacy(spec_revision) else ACTIVE_ARTIFACTS


def upstream_binding(spec_revision: str | None) -> dict[str, tuple[str, str]]:
    return LEGACY_UPSTREAM_BINDING if _legacy(spec_revision) else UPSTREAM_BINDING


def stale_scope_table(spec_revision: str | None) -> dict[str, tuple[str, ...]]:
    return LEGACY_STALE_SCOPE if _legacy(spec_revision) else STALE_SCOPE


def canonical_name(artifact: str) -> str:
    name = ALIASES.get(artifact, artifact)
    if name not in ARTIFACTS:
        raise ConfigurationError(
            f"Unknown artifact {artifact!r}. Known: "
            f"{sorted(set(ARTIFACTS) | set(ALIASES))}"
        )
    return name


def artifact_path(layout: Layout, run_id: str, job_id: str, artifact: str) -> Path:
    filename, _ = ARTIFACTS[canonical_name(artifact)]
    return layout.job_dir(run_id, job_id) / "current" / filename


def load(layout: Layout, run_id: str, job_id: str, artifact: str) -> dict[str, Any] | None:
    path = artifact_path(layout, run_id, job_id, artifact)
    return read_json(path) if path.is_file() else None


def artifact_hash(payload: dict[str, Any]) -> str:
    """Semantic identity of an artifact.

    Canonical JSON, so reformatting is not a change, and **excluding the
    package `finalization` block**.

    That exclusion is required by the frozen staleness table, not a
    convenience. DEC-26 lists two separate rows:

        final replaced                      -> draft, final, review, render
        final document date assigned/changed -> render

    The document date is co-owned metadata that becomes canonical at
    semantic finalization (DEC-38). If the review bound to a hash that
    included it, running `jobbsok finalize` would mark the review stale and
    demand a pointless Stage-3 rerun. Binding to the semantic payload keeps
    date assignment invalidating exactly the render, as frozen.
    """
    if payload.get("artifact_role") == "CURRENT_SEMANTIC_PACKAGE":
        payload = {k: v for k, v in payload.items() if k != "finalization"}
    return sha256_canonical_json(payload)


@dataclass
class SemanticState:
    loaded: dict[str, dict[str, Any] | None]
    valid: set[str]
    stale: set[str]
    invalid: set[str]

    def current(self, artifact: str) -> bool:
        name = canonical_name(artifact)
        # An artifact this run's revision does not own is simply absent.
        return (
            self.loaded.get(name) is not None
            and name in self.valid
            and name not in self.stale
        )

    def digest(self, artifact: str) -> str | None:
        payload = self.loaded.get(canonical_name(artifact))
        return artifact_hash(payload) if payload is not None else None


def semantic_state(
    layout: Layout,
    context: Any,
    job_id: str,
    *,
    soft_thresholds: dict[str, int] | None = None,
) -> SemanticState:
    """One fixed currentness definition shared by every public action."""
    from . import validate as validate_module

    spec_revision = context.manifest.get("spec_revision")
    loaded = {
        name: load(layout, context.run_id, job_id, name)
        for name in active_artifacts(spec_revision)
    }
    stale, _ = evaluate_staleness(
        layout, context.run_id, job_id, spec_revision=spec_revision
    )
    valid: set[str] = set()
    invalid: set[str] = set()
    for name, payload in loaded.items():
        if payload is None:
            continue
        checked = validate_module.validate_artifact(
            layout, context, job_id, name, payload,
            soft_thresholds=soft_thresholds,
        )
        (valid if checked.ok else invalid).add(name)
    return SemanticState(loaded, valid, stale, invalid)


MECHANICAL_FIELDS: dict[str, set[str]] = {
    "strategy": {
        "artifact_role", "authority", "elasticity",
        "final_writer_may_reconstruct", "source_escape_permitted", "binding",
    },
    "draft_package": {"artifact_role", "source_stage", "binding", "finalization"},
    "final_package": {"artifact_role", "source_stage", "binding", "finalization"},
    "review": {"artifact_role", "binding"},
}


def handoff_for(
    layout: Layout,
    context: Any,
    job_id: str,
    stage: int,
    *,
    soft_thresholds: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Return the exact current, mechanically derived envelope for one stage."""
    state = semantic_state(
        layout, context, job_id, soft_thresholds=soft_thresholds
    )
    job = next(j for j in context.manifest["jobs"] if j["job_id"] == job_id)
    if job["job_class"] == "EXCEPTION":
        raise JobError(
            f"{job_id} is an EXCEPTION job and is inert to the core semantic workflow."
        )
    from . import failure as failure_module

    current_failure = failure_module.load(layout, context.run_id, job_id)
    legacy = _legacy(context.manifest.get("spec_revision"))
    if current_failure and current_failure.get("classification") == "BLOCKED_MANUAL":
        raise JobError(
            f"{job_id} is BLOCKED_MANUAL. Resolve the recorded human decision "
            "before initiating another semantic stage."
        )

    if stage == 1:
        mode = "STRATEGY"
        expected = ["strategy"]
        upstream: dict[str, str] = {}
        prior = {"strategy": state.digest("strategy")}
    elif stage == 2:
        if not legacy:
            raise ConfigurationError(
                "Stage 2 is retired for revision 0.9.3 runs. The active route is "
                "Stage 1 then Stage 3, each in its own instance and chat."
            )
        if not state.current("strategy"):
            raise JobError(
                f"Stage 2 context refused for {job_id}: strategy is not current and valid."
            )
        mode = "DRAFT"
        expected = ["draft_package"]
        upstream = {"strategy_sha256": state.digest("strategy")}
        prior = {"draft_package": state.digest("draft_package")}
    elif stage == 3:
        if state.current("final_package") and not state.current("review"):
            mode = "REVIEW_ONLY"
            expected = ["review"]
            upstream = {"final_package_sha256": state.digest("final_package")}
            prior = {"review": state.digest("review")}
        else:
            required = "draft_package" if legacy else "strategy"
            if not state.current(required):
                raise JobError(
                    f"Stage 3 context refused for {job_id}: {required} is not "
                    "current and valid."
                )
            mode = "FINAL_AND_REVIEW"
            expected = ["final_package", "review"]
            upstream = (
                {"draft_sha256": state.digest("draft_package")}
                if legacy
                else {"strategy_sha256": state.digest("strategy")}
            )
            prior = {
                "final_package": state.digest("final_package"),
                "review": state.digest("review"),
            }
    else:
        raise ConfigurationError(f"Unknown stage: {stage}")

    envelope = {
        "artifact_role": "SEMANTIC_HANDOFF",
        "run_id": context.run_id,
        "job_id": job_id,
        "employer": job["employer"],
        "title": job["title"],
        "stage": stage,
        "mode": mode,
        "expected_artifacts": expected,
        "stage_policy_sha256": context.assets.stage_policy_sha256(stage),
        "upstream": upstream,
        "prior_current": prior,
    }
    if (
        current_failure
        and current_failure.get("operation") == f"STAGE{stage}"
        and current_failure.get("retry_position") is not None
    ):
        envelope["semantic_retry_attempt"] = (
            current_failure.get("semantic_attempt")
            or current_failure.get("attempts_used", 0) + 1
        )
    return envelope


def write_handoff(layout: Layout, envelope: dict[str, Any]) -> Path:
    digest = sha256_canonical_json(envelope)[:HANDOFF_DIGEST_CHARS]
    directory = (
        layout.generated / "handoffs"
        / flatten_run_reference(envelope["run_id"])
        / envelope["job_id"]
    )
    path = directory / f"stage{envelope['stage']}-{digest}.json"
    atomic_write_json(path, envelope)
    return path


def verify_handoff(
    layout: Layout,
    context: Any,
    job_id: str,
    stage: int,
    supplied: Path,
    *,
    soft_thresholds: dict[str, int] | None = None,
) -> dict[str, Any]:
    expected = handoff_for(
        layout, context, job_id, stage, soft_thresholds=soft_thresholds
    )
    digest = sha256_canonical_json(expected)[:HANDOFF_DIGEST_CHARS]
    directory = (
        layout.generated / "handoffs"
        / flatten_run_reference(context.run_id)
        / job_id
    )
    expected_path = directory / f"stage{stage}-{digest}.json"
    actual_path = resolve_within(directory, supplied, label="handoff path")
    if actual_path != expected_path.resolve(strict=False) or not actual_path.is_file():
        raise JobError(
            "Submission refused before persistence: the handoff is stale, wrong, "
            f"or missing. Regenerate it with 'jobbsok context --run {context.run_id} "
            f"--job {job_id} --stage {stage}'."
        )
    if read_json(actual_path) != expected:
        raise JobError(
            "Submission refused before persistence: handoff contents do not match "
            "the current mechanically derived context."
        )
    return expected


def semantic_fields(context: Any, artifact: str) -> list[str]:
    name = canonical_name(artifact)
    _, schema_name = ARTIFACTS[name]
    schema = read_json(context.schemas_dir / f"{schema_name}.schema.json")
    return sorted(set(schema["properties"]) - MECHANICAL_FIELDS[name])


def stamp_payload(
    context: Any,
    job_id: str,
    artifact: str,
    semantic_payload: dict[str, Any],
    state: SemanticState,
) -> dict[str, Any]:
    """Reject model-owned mechanics and insert the canonical values in memory."""
    name = canonical_name(artifact)
    forbidden = sorted(MECHANICAL_FIELDS[name] & set(semantic_payload))
    if forbidden:
        raise JobError(
            f"{name} contains tooling-owned fields {forbidden}. Return semantic "
            "fields only; use the exact stage-submit action from jobbsok context."
        )
    job = next(j for j in context.manifest["jobs"] if j["job_id"] == job_id)
    payload = dict(semantic_payload)

    if name == "strategy":
        payload = {
            "artifact_role": "STRATEGY_HYPOTHESIS",
            "authority": "NON_FACTUAL_NON_FINAL",
            "elasticity": "ELASTIC",
            "final_writer_may_reconstruct": True,
            "source_escape_permitted": True,
            **payload,
        }
    elif name in ("draft_package", "final_package"):
        payload = {
            "artifact_role": "CURRENT_SEMANTIC_PACKAGE",
            "source_stage": (
                "STAGE2_DRAFT" if name == "draft_package" else "STAGE3_FINAL"
            ),
            **payload,
        }
        if name == "final_package":
            payload["finalization"] = {"state": "DRAFT"}
    else:
        payload = {"artifact_role": "OPERATOR_TRIAGE", **payload}

    if name == "review":
        final_digest = state.digest("final_package")
        if final_digest is None:
            raise JobError("Review submission requires a current final package.")
        binding = {
            "run_id": context.run_id,
            "job_id": job_id,
            "final_package_sha256": final_digest,
        }
    else:
        binding = {
            "run_id": context.run_id,
            "job_id": job_id,
            "employer": job["employer"],
            "title": job["title"],
            "manifest_sha256": context.manifest_sha256,
            "vacancy_sha256": context.vacancy_sha256(job_id),
            "evidence_index_sha256": context.index_sha256,
            "stage_instruction_sha256": context.stage_instruction_sha256(name),
        }
        if name in ("draft_package", "final_package"):
            binding["baseline_map_sha256"] = context.assets.record("baseline_map")["sha256"]
        if name == "draft_package":
            binding["strategy_sha256"] = state.digest("strategy")
        elif name == "final_package":
            binding["strategy_sha256"] = state.digest("strategy")
            if _legacy(context.manifest.get("spec_revision")):
                binding["draft_sha256"] = state.digest("draft_package")
    payload["binding"] = binding
    return payload


@dataclass
class SubmitResult:
    artifact: str
    path: Path
    result: ValidationResult
    superseded: Path | None = None

    @property
    def ok(self) -> bool:
        return self.result.ok


def check_stage_ownership(stage: int, artifact: str) -> ValidationResult:
    """INV-09: refuse a write the stage does not own."""
    result = ValidationResult()
    name = canonical_name(artifact)
    allowed = STAGE_WRITE_MAP.get(stage, ())
    if name not in allowed:
        owner = owning_stage(name)
        result.add(
            "INV-09",
            name,
            f"stage {stage}",
            f"stage {stage} may write only {list(allowed) or 'nothing'}",
            f"attempted to write {name!r}, which is owned by "
            + (f"stage {owner}" if owner else "deterministic tooling")
            + ". Replacing an upstream artifact requires a separately "
              "initiated execution of its owning standard stage.",
        )
    return result


def submit(
    layout: Layout,
    run_id: str,
    job_id: str,
    *,
    stage: int,
    artifact: str,
    payload: dict[str, Any],
    timestamp: str,
) -> SubmitResult:
    """Atomically replace one current artifact, archiving the previous copy.

    Callers must have validated `payload` first; this function enforces only
    write ownership, which is the one rule no caller may bypass.
    """
    name = canonical_name(artifact)
    result = check_stage_ownership(stage, name)
    path = artifact_path(layout, run_id, job_id, name)
    if not result.ok:
        return SubmitResult(name, path, result)

    superseded: Path | None = None
    if path.is_file():
        history = layout.job_dir(run_id, job_id) / "history"
        history.mkdir(parents=True, exist_ok=True)
        superseded = history / f"{timestamp}_{path.name}"
        superseded.write_bytes(path.read_bytes())

    atomic_write_json(path, payload)
    return SubmitResult(name, path, result, superseded)


def submit_stage3_pair(
    layout: Layout,
    run_id: str,
    job_id: str,
    *,
    final_payload: dict[str, Any],
    review_payload: dict[str, Any],
    timestamp: str,
) -> tuple[SubmitResult, SubmitResult]:
    """Commit a prevalidated Stage-3 pair; no candidate is visible early."""
    paths = {
        name: artifact_path(layout, run_id, job_id, name)
        for name in ("final_package", "review")
    }
    superseded: dict[str, Path | None] = {name: None for name in paths}
    history = layout.job_dir(run_id, job_id) / "history"
    prior: dict[str, tuple[bool, str | None]] = {}
    try:
        for name, path in paths.items():
            if path.is_file():
                history.mkdir(parents=True, exist_ok=True)
                archived = history / f"{timestamp}_{path.name}"
                if archived.exists():
                    raise ConfigurationError(
                        f"Stage-3 history target already exists: {archived}"
                    )
                atomic_write_bytes(archived, path.read_bytes())
                prior[name] = (True, sha256_file(archived))
                superseded[name] = archived
            else:
                prior[name] = (False, None)
    except Exception:
        # No current artifact was replaced, so leave no archive behind either.
        for archived in superseded.values():
            if archived is not None:
                archived.unlink(missing_ok=True)
        raise

    try:
        atomic_write_json(paths["final_package"], final_payload)
        atomic_write_json(paths["review"], review_payload)
    except Exception as exc:
        try:
            for name, path in paths.items():
                existed, expected = prior[name]
                archived = superseded[name]
                if existed:
                    if archived is None or not archived.is_file():
                        raise ConfigurationError(
                            f"Stage-3 rollback copy is missing for {path.name}."
                        )
                    atomic_write_bytes(path, archived.read_bytes())
                    if sha256_file(path) != expected:
                        raise ConfigurationError(
                            f"Stage-3 rollback hash mismatch for {path.name}."
                        )
                else:
                    path.unlink(missing_ok=True)
                    if path.exists():
                        raise ConfigurationError(
                            f"Stage-3 rollback could not remove {path.name}."
                        )
            for archived in superseded.values():
                if archived is not None:
                    archived.unlink()
        except Exception as rollback_exc:
            raise ConfigurationError(
                "Stage-3 pair commit failed and exact rollback could not be proven: "
                f"{rollback_exc}"
            ) from rollback_exc
        raise JobError(
            f"Stage-3 pair commit failed; prior final and review were restored: "
            f"{type(exc).__name__}: {exc}"
        ) from exc
    return (
        SubmitResult(
            "final_package", paths["final_package"], ValidationResult(),
            superseded["final_package"],
        ),
        SubmitResult(
            "review", paths["review"], ValidationResult(), superseded["review"]
        ),
    )


# --------------------------------------------------------------------------
# Staleness
# --------------------------------------------------------------------------

def stale_scope(changed: str, *, spec_revision: str | None = None) -> tuple[str, ...]:
    table = stale_scope_table(spec_revision)
    key = (
        canonical_name(changed)
        if changed in ARTIFACTS or changed in ALIASES
        else changed
    )
    return table.get(key, ())


def evaluate_staleness(
    layout: Layout, run_id: str, job_id: str, *, spec_revision: str | None = None
) -> tuple[set[str], ValidationResult]:
    """Which current artifacts no longer match their recorded upstream hash.

    Compares only the fixed relations in UPSTREAM_BINDING. No graph, no
    traversal, no engine.
    """
    result = ValidationResult()
    stale: set[str] = set()
    cache: dict[str, dict[str, Any] | None] = {}
    bindings = upstream_binding(spec_revision)
    propagation = stale_scope_table(spec_revision)

    def get(name: str) -> dict[str, Any] | None:
        if name not in cache:
            cache[name] = load(layout, run_id, job_id, name)
        return cache[name]

    for artifact, (upstream, field) in bindings.items():
        payload = get(artifact)
        if payload is None:
            continue
        upstream_payload = get(upstream)
        if upstream_payload is None:
            stale.add(artifact)
            result.add(
                "DEC-26", ARTIFACTS[artifact][0], field,
                f"a current {upstream} to bind to",
                f"{upstream} is absent, so {artifact} cannot be current",
                severity="ERROR",
            )
            continue
        recorded = (
            payload.get("binding", {}).get(field)
            if artifact != "review"
            else payload.get("binding", {}).get(field)
        )
        actual = artifact_hash(upstream_payload)
        if recorded != actual:
            stale.add(artifact)
            for downstream in propagation.get(upstream, ()):
                if downstream in ARTIFACTS and get(downstream) is not None:
                    stale.add(downstream)
            result.add(
                "DEC-26", ARTIFACTS[artifact][0], f"binding.{field}",
                f"{field} == {actual[:12]}... (hash of the current {upstream})",
                f"{recorded[:12] if recorded else 'absent'}... - the {upstream} "
                f"was replaced, so this artifact is STALE. Re-run its owning "
                f"stage; do not edit it in place.",
                severity="WARNING",
            )
    return stale, result


# --------------------------------------------------------------------------
# Soft editorial warnings (DEC-24, DEC-33)
# --------------------------------------------------------------------------

def soft_quality_warnings(
    package: dict[str, Any], thresholds: dict[str, int], *, file_label: str
) -> ValidationResult:
    """Editorial signals. These never fail a command."""
    result = ValidationResult()
    cv = package.get("cv") or {}

    competencies = cv.get("competencies") or []
    low = thresholds.get("competencies_expected_min")
    high = thresholds.get("competencies_expected_max")
    if low and high and not (low <= len(competencies) <= high):
        result.add(
            "DEC-33", file_label, "cv.competencies",
            f"about {low}-{high} competencies (soft editorial default)",
            f"{len(competencies)} - this is a warning only; the count is an "
            "editorial choice and never a mechanical failure",
            severity="WARNING",
        )

    for override in cv.get("employment_overrides") or []:
        if not override.get("bullets"):
            result.add(
                "DEC-23", file_label,
                f"cv.employment_overrides[{override.get('employment_id')}]",
                "either no override (use baseline bullets) or a non-empty "
                "replacement",
                "a present EMPTY replacement, which explicitly means 'render no "
                "bullets for this employment'. Legal and deliberate, but there "
                "is no fallback to the baseline defaults.",
                severity="WARNING",
            )
    return result
