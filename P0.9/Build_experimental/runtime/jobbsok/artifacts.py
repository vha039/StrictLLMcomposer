"""Current semantic artifacts: load, stamp, submit, staleness.

One generic core driven by `pipeline.ARTIFACTS`. Every artifact is a layer
written by exactly one stage (or, for the assembled final package, by the
tool at Stage-3 publish). At most one current copy per role per job; a
replacement is atomic and the superseded copy moves to `history/`.

Staleness compares declared input identities first, then the artifact's
evidence fingerprint against its frozen facts. Policy edits never mark
anything stale.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import pipeline
from .atomicio import atomic_write_json, read_json
from .errors import JobError, ValidationResult
from .hashing import sha256_canonical_json
from .paths import Layout

canonical_name = pipeline.canonical_name


def artifact_path(layout: Layout, run_id: str, job_id: str, artifact: str) -> Path:
    spec = pipeline.ARTIFACTS[canonical_name(artifact)]
    return layout.job_dir(run_id, job_id) / "current" / spec.filename


def load(layout: Layout, run_id: str, job_id: str, artifact: str) -> dict[str, Any] | None:
    path = artifact_path(layout, run_id, job_id, artifact)
    return read_json(path) if path.is_file() else None


#: Tool-owned provenance. A re-stamp alone must not change an artifact's
#: identity, so these never enter the semantic hash.
SEMANTIC_EXCLUDED = ("binding", "artifact_role")


def artifact_hash(payload: dict[str, Any]) -> str:
    """Semantic identity: what the owning stage actually wrote.

    `binding` and `artifact_role` are provenance, not content. `finalization`
    is excluded for the package as well: the document date becomes canonical
    after the review is already bound to it, and excluding it keeps `finalize`
    from marking that review stale.
    """
    skip = set(SEMANTIC_EXCLUDED)
    if payload.get("artifact_role") == "CURRENT_SEMANTIC_PACKAGE":
        skip.add("finalization")
    return sha256_canonical_json({k: v for k, v in payload.items() if k not in skip})


# --------------------------------------------------------------------------
# Currentness
# --------------------------------------------------------------------------


@dataclass
class SemanticState:
    loaded: dict[str, dict[str, Any] | None]
    valid: set[str]
    stale: set[str]
    invalid: set[str]
    stale_reason: dict[str, str] = field(default_factory=dict)

    def current(self, artifact: str) -> bool:
        name = canonical_name(artifact)
        return (
            self.loaded.get(name) is not None
            and name in self.valid
            and name not in self.stale
        )

    def digest(self, artifact: str) -> str | None:
        payload = self.loaded.get(canonical_name(artifact))
        return artifact_hash(payload) if payload is not None else None

    def payload(self, artifact: str) -> dict[str, Any] | None:
        return self.loaded.get(canonical_name(artifact))


def _stale_reason(
    context: Any, job_id: str, artifact: str, payload: dict[str, Any]
) -> str | None:
    """None when current; otherwise a one-line reason naming what moved."""
    binding = payload.get("binding") or {}
    stored_inputs = binding.get("inputs") or {}
    current_inputs = pipeline.upstream_hashes(context, job_id, artifact)
    keys = set(stored_inputs) | set(current_inputs)
    if artifact == "review" and "final_package" not in stored_inputs:
        keys.discard("final_package")
    moved = [
        name
        for name in sorted(keys)
        if stored_inputs.get(name) != current_inputs.get(name)
    ]
    if moved:
        evidence = []
        history = context.assets.run_dir / "jobs" / job_id / "history"
        for name in moved:
            copies = sorted(history.glob(f"*_{pipeline.ARTIFACTS[name].filename}"))
            for path in reversed(copies):
                if artifact_hash(read_json(path)) == stored_inputs.get(name):
                    evidence.append(f"history/{path.name}")
                    break
        suffix = " — previous copy in " + ", ".join(evidence) if evidence else ""
        return f"inputs changed: {', '.join(moved)}" + suffix
    if binding.get("evidence_fingerprint") != pipeline.artifact_fingerprint(
        context, job_id, artifact, upstream=stored_inputs
    ):
        return "frozen facts or the vacancy changed since this artifact was written"
    return None


def semantic_state(
    layout: Layout,
    context: Any,
    job_id: str,
    *,
    soft_thresholds: dict[str, int] | None = None,
) -> SemanticState:
    """One fixed currentness definition shared by every public action."""
    from . import validate as validate_module

    loaded = {
        name: load(layout, context.run_id, job_id, name)
        for name in pipeline.all_artifacts()
    }
    stale: set[str] = set()
    reasons: dict[str, str] = {}
    valid: set[str] = set()
    invalid: set[str] = set()
    for name, payload in loaded.items():
        if payload is None:
            continue
        reason = _stale_reason(context, job_id, name, payload)
        if reason:
            stale.add(name)
            reasons[name] = reason
        checked = validate_module.validate_artifact(
            layout, context, job_id, name, payload, soft_thresholds=soft_thresholds
        )
        (valid if checked.ok else invalid).add(name)
    return SemanticState(loaded, valid, stale, invalid, reasons)


# --------------------------------------------------------------------------
# Stamping
# --------------------------------------------------------------------------


def semantic_fields(context: Any, artifact: str) -> list[str]:
    name = canonical_name(artifact)
    schema = read_json(
        context.schemas_dir / f"{pipeline.ARTIFACTS[name].schema}.schema.json"
    )
    return sorted(set(schema.get("properties") or {}) - pipeline.TOOL_FIELDS)


def binding_for(
    context: Any,
    job_id: str,
    artifact: str,
    *,
    upstream: dict[str, str] | None = None,
) -> dict[str, Any]:
    name = canonical_name(artifact)
    spec = pipeline.ARTIFACTS[name]
    stage = spec.owner_stage if spec.owner_stage is not None else 3
    job = next(j for j in context.manifest["jobs"] if j["job_id"] == job_id)
    inputs = (
        dict(upstream)
        if upstream is not None
        else pipeline.upstream_hashes(context, job_id, name)
    )
    inputs = {
        key: value
        for key, value in inputs.items()
        if key in spec.inputs
    }
    return {
        "run_id": context.run_id,
        "job_id": job_id,
        "employer": job["employer"],
        "title": job["title"],
        "evidence_fingerprint": pipeline.artifact_fingerprint(
            context, job_id, name, upstream=inputs
        ),
        "policy_fingerprint": pipeline.policy_fingerprint(context, stage),
        "inputs": inputs,
    }


def stamp(
    context: Any,
    job_id: str,
    artifact: str,
    semantic_payload: dict[str, Any],
    *,
    upstream: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Reject tool-owned fields and insert the canonical values in memory."""
    name = canonical_name(artifact)
    spec = pipeline.ARTIFACTS[name]
    forbidden = sorted(pipeline.TOOL_FIELDS & set(semantic_payload))
    if forbidden:
        raise JobError(
            f"{name} contains tooling-owned fields {forbidden}. Return semantic "
            "fields only; the exact write set is in the context bundle."
        )
    payload: dict[str, Any] = {"artifact_role": spec.artifact_role}
    if name == "final_package":
        payload["source_stage"] = "ASSEMBLED"
    payload.update(semantic_payload)
    if name == "final_package":
        payload["finalization"] = {"state": "DRAFT"}
    payload["binding"] = binding_for(context, job_id, name, upstream=upstream)
    return payload


# --------------------------------------------------------------------------
# Submission
# --------------------------------------------------------------------------


@dataclass
class SubmitResult:
    artifact: str
    path: Path
    superseded: Path | None = None


def submit_many(
    layout: Layout,
    run_id: str,
    job_id: str,
    payloads: dict[str, dict[str, Any]],
    *,
    timestamp: str,
) -> list[SubmitResult]:
    """Write a stage's artifacts, archiving any superseded copies."""
    written: list[SubmitResult] = []
    history = layout.job_dir(run_id, job_id) / "history"
    for name, payload in payloads.items():
        path = artifact_path(layout, run_id, job_id, name)
        superseded = None
        if path.is_file():
            history.mkdir(parents=True, exist_ok=True)
            superseded = history / f"{timestamp}_{path.name}"
            superseded.write_bytes(path.read_bytes())
        atomic_write_json(path, payload)
        written.append(SubmitResult(name, path, superseded))
    return written


def discard(layout: Layout, run_id: str, job_id: str, artifact: str, *, timestamp: str) -> None:
    """Move a current artifact into history (used when a stage rejects)."""
    path = artifact_path(layout, run_id, job_id, artifact)
    if not path.is_file():
        return
    history = layout.job_dir(run_id, job_id) / "history"
    history.mkdir(parents=True, exist_ok=True)
    (history / f"{timestamp}_{path.name}").write_bytes(path.read_bytes())
    path.unlink()


# --------------------------------------------------------------------------
# Soft editorial warnings (counts are signals, never failures)
# --------------------------------------------------------------------------


def soft_quality_warnings(
    package: dict[str, Any], thresholds: dict[str, int], *, file_label: str
) -> ValidationResult:
    result = ValidationResult()
    cv = package.get("cv") or {}

    competencies = cv.get("competencies") or []
    low = thresholds.get("competencies_expected_min")
    high = thresholds.get("competencies_expected_max")
    if low and high and competencies and not (low <= len(competencies) <= high):
        result.add(
            "DEC-33", file_label, "cv.competencies",
            f"about {low}-{high} competencies (soft editorial default)",
            f"{len(competencies)} - warning only",
            severity="WARNING",
        )
    for override in cv.get("employment_overrides") or []:
        if not override.get("bullets"):
            result.add(
                "DEC-23", file_label,
                f"cv.employment_overrides[{override.get('employment_id')}]",
                "either no override (baseline bullets) or a non-empty replacement",
                "a present EMPTY replacement: renders no bullets for this "
                "employment. Legal and deliberate.",
                severity="WARNING",
            )
    return result
