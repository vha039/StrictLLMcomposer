"""Child branch: the only way to change anything a run froze.

DEC-40 / Contract 6.3. To change any frozen-run element the system creates
a new run with a new `run_id` and a `parent_run_id` referencing the prior
run. The original stays untouched. There is no same-run amend, no manifest
version lineage, no event sourcing and no artifact-lineage graph.

Frozen inputs are re-collected from the current repository, because a
changed input is the reason to branch in the first place. Prior semantic
artifacts are offered as prior context and become current in the child only
after they are validated under the child manifest.

A deterministic child-local rebind is permitted only when every
content-governing hash is identical. The rebind updates identity and hash
metadata; it never authors or alters the semantic payload. Otherwise the
owning standard stage must regenerate the artifact -- no artifact becomes
current in the child solely because it existed in the parent (Spec 5.4).
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import SCHEMA_REVISION, SPEC_REVISION
from . import settings as settings_module
from .atomicio import atomic_write_json, read_json
from .baseline import check_baseline_map
from .errors import ConfigurationError, ValidationResult
from .evidence_index import check_index
from .hashing import sha256_file
from .manifest import (
    FROZEN_DIR,
    MANIFEST_NAME,
    FrozenRunAssets,
    _iso,
    _iter_frozen_records,
    _reconciliation,
    _verify_frozen_assets,
    collect_frozen_inputs,
    load_manifest,
    make_run_id,
    require_intact,
    utc_now,
    writing_policy_records,
)
from .paths import (
    BRANCHES_DIR,
    MAX_BRANCH_COMPONENT,
    Layout,
    split_run_reference,
)
from .schemas import validate_against_schema

#: Operator-asserted navigation label. It is never verified executor
#: provenance, and there is no configured-model fallback: the frozen role
#: mapping stays the declared execution setting, not proof of execution.
MODEL_TAG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,7}$")
DEFAULT_MODEL_TAG = "unknown"

#: Which frozen inputs govern each artifact's content. A child-local rebind
#: is allowed only when every one of these is identical (Contract 6.3.6).
CONTENT_GOVERNING: dict[str, tuple[tuple[str, ...], ...]] = {
    # Stage 1 now reads the mechanical baseline projection, so a
    # baseline-only change must regenerate the strategy: selection and
    # allocation were chosen against a specific inventory and default
    # bullet set (RP-08).
    "strategy": (
        ("authorities", "WORK"), ("authorities", "EDU"), ("authorities", "OTHER"),
        ("evidence_index",), ("baseline_map",), ("cv_baseline",),
        ("personality_profile",),
        ("personality_facet_index",), ("stage_instructions", "stage1"),
        ("writing_policy",), ("schemas", "strategy.schema.json"),
    ),
    "final_package": (
        ("authorities", "WORK"), ("authorities", "EDU"), ("authorities", "OTHER"),
        ("evidence_index",), ("baseline_map",), ("cv_baseline",),
        ("stage_instructions", "stage3"), ("writing_policy",),
        ("schemas", "package.schema.json"),
    ),
    "review": (
        ("stage_instructions", "stage3"), ("writing_policy",),
        ("schemas", "review.schema.json"),
    ),
}

#: The active child artifact set. Stage 2 is retired, so no child is ever
#: created with a draft; a legacy parent's draft is neither copied nor
#: rebound.
ARTIFACT_STAGE = {
    "strategy": 1, "final_package": 3, "review": 3,
}

DEPENDENCIES = {
    "strategy": (),
    "final_package": ("strategy",),
    "review": ("final_package",),
}

ARTIFACT_FILES = {
    "strategy": "strategy.json",
    "final_package": "final_package.json",
    "review": "review.json",
}

REUSED = "REUSED"
REGENERATE_REQUIRED = "REGENERATE_REQUIRED"
ABSENT = "ABSENT"


@dataclass
class BranchResult:
    run_id: str | None
    manifest: dict[str, Any] | None
    result: ValidationResult = field(default_factory=ValidationResult)
    #: job_id -> {artifact: REUSED | REGENERATE_REQUIRED | ABSENT}
    disposition: dict[str, dict[str, str]] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.result.ok and self.run_id is not None


def _input_value(inputs: dict[str, Any], keys: tuple[str, ...]) -> Any:
    if keys[0] == "schemas":
        filename = keys[1]
        return next(
            record for record in inputs["schemas"]
            if Path(record["path"]).name == filename
        )
    value: Any = inputs
    for key in keys:
        value = value[key]
    return value


def _fingerprint(value: Any) -> Any:
    if isinstance(value, list):
        return tuple((record["path"], record["sha256"]) for record in value)
    return value["sha256"]


def _same_governing_inputs(
    parent: dict[str, Any], child: dict[str, Any], artifact: str
) -> bool:
    stage = ARTIFACT_STAGE[artifact]
    for keys in CONTENT_GOVERNING[artifact]:
        if keys == ("writing_policy",):
            # §3.4: compare exactly the policy records this artifact's owning
            # stage consumes. Narrowing the bundle and the governing hash while
            # leaving the branch comparison broad would silently regenerate a
            # strategy for a voice-only change it never saw.
            a = writing_policy_records(parent, stage)
            b = writing_policy_records(child, stage)
        else:
            a = _input_value(parent["frozen_inputs"], keys)
            b = _input_value(child["frozen_inputs"], keys)
        if _fingerprint(a) != _fingerprint(b):
            return False
    parent_stages = parent["settings_snapshot"]["stages"]
    child_stages = child["settings_snapshot"]["stages"]
    parent_role = parent_stages[f"stage{stage}"]
    child_role = child_stages[f"stage{stage}"]
    if parent_role != child_role:
        return False
    if parent_stages.get("role_mapping", {}).get(parent_role) != \
            child_stages.get("role_mapping", {}).get(child_role):
        return False
    return True


def branch(
    layout: Layout,
    parent_run_id: str,
    *,
    reviewed_by: str,
    from_stage: int | None = None,
    model_tag: str = DEFAULT_MODEL_TAG,
    moment: datetime | None = None,
) -> BranchResult:
    """Create the one permitted child run under the root ancestor.

    `from_stage` is the first stage to execute again, not an 'after'
    label: 1 forces strategy, final and review absent; 3 forces final and
    review absent and reuses the current strategy only when its governing
    inputs still match. It can never override a stale or changed
    prerequisite or a revision migration. Omitting it preserves the
    ordinary policy-driven reuse.
    """
    moment = moment or utc_now()
    if from_stage is not None and from_stage not in (1, 3):
        raise ConfigurationError(
            f"--from-stage must be 1 or 3; Stage 2 is retired. Got {from_stage!r}."
        )
    if not MODEL_TAG_PATTERN.fullmatch(model_tag):
        raise ConfigurationError(
            "--model-tag must be a short lowercase ASCII label matching "
            f"[a-z0-9][a-z0-9-]{{0,7}}; got {model_tag!r}. A model identity "
            "is never silently truncated."
        )
    result = ValidationResult()
    parent = load_manifest(layout, parent_run_id)
    parent_dir = layout.run_dir(parent_run_id)
    require_intact(layout, parent)

    from . import artifacts as artifacts_module
    from . import validate as validate_module
    from .validate import RunContext

    parent_context = RunContext(layout, parent)
    parent_states = {
        job["job_id"]: artifacts_module.semantic_state(
            layout, parent_context, job["job_id"]
        )
        for job in parent["jobs"]
        if job["job_class"] == "CORE"
    }

    # ACC-03: snapshot the entire root ancestor, including every existing
    # sibling branch. No branches/ exemption: publishing the new child is
    # the only permitted addition inside that tree.
    ancestor_root = layout.run_dir(split_run_reference(parent_run_id)[0])
    ancestor_before = {
        path.relative_to(ancestor_root).as_posix(): sha256_file(path)
        for path in sorted(ancestor_root.rglob("*")) if path.is_file()
    }

    frozen_inputs, index, baseline_map = collect_frozen_inputs(layout)
    result.extend(check_index(index, layout.authorities).violations)
    result.extend(check_baseline_map(baseline_map).violations)

    reconciliation, conflicts = _reconciliation(layout, reviewed_by, moment)
    for conflict in conflicts:
        result.add("CTR-01", "authorities/CV_BASELINE.md", "baseline_reconciliation",
                   "no known baseline-versus-authority conflict", conflict)

    try:
        settings = settings_module.load(layout)
    except ConfigurationError as exc:
        result.add("CTR-01", "policy/settings.toml", "-", "readable settings", str(exc))
        return BranchResult(None, None, result)

    seed = "|".join(
        [_iso(moment), parent_run_id] + sorted(j["job_id"] for j in parent["jobs"])
    )
    #: A branch of a branch is physically a sibling under the same root
    #: ancestor. parent_run_id keeps the exact immediate lineage, so depth
    #: never grows (DEC-40/ACC-03).
    root_ancestor, _ = split_run_reference(parent_run_id)
    component = (
        f"stage{from_stage or 0}_{model_tag}_"
        f"{moment.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    )
    if len(component) > MAX_BRANCH_COMPONENT:
        raise ConfigurationError(
            f"Branch component {component!r} exceeds "
            f"{MAX_BRANCH_COMPONENT} characters."
        )
    run_id = f"{root_ancestor}/{BRANCHES_DIR}/{component}"
    ancestor_dir = layout.run_dir(root_ancestor)

    child: dict[str, Any] = {
        "artifact_role": "RUN_MANIFEST",
        "run_id": run_id,
        "parent_run_id": parent_run_id,
        "spec_revision": SPEC_REVISION,
        "schema_revision": SCHEMA_REVISION,
        "frozen_at": _iso(moment),
        "frozen_inputs": frozen_inputs,
        "settings_snapshot": settings_module.snapshot(settings),
        "baseline_reconciliation": reconciliation,
        "jobs": [dict(job) for job in parent["jobs"]],
    }
    validate_against_schema(
        child, layout.schemas, "manifest", file_label=MANIFEST_NAME, result=result
    )
    if not result.ok:
        return BranchResult(None, None, result)

    final = layout.run_dir(run_id)
    if final.exists():
        raise ConfigurationError(f"Run {run_id} already exists at {final}.")
    # Stage outside the root ancestor so the tree we are about to prove
    # unchanged never contains the work in progress. The staging token is
    # the existing short unique branch seed, never the slashed reference.
    staging = layout.runs / f".branching-{make_run_id(moment, seed)}"
    if staging.exists():
        shutil.rmtree(staging)

    revision_migrated = parent.get("spec_revision") != SPEC_REVISION

    disposition: dict[str, dict[str, str]] = {}
    try:
        staging.mkdir(parents=True)
        (staging / "audit").mkdir()
        for record in _iter_frozen_records(frozen_inputs):
            target = staging / FROZEN_DIR / record["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(layout.root / record["path"], target)

        atomic_write_json(staging / MANIFEST_NAME, child)
        child_context = RunContext(layout, child, run_dir=staging)

        for job in child["jobs"]:
            job_id = job["job_id"]
            job_dir = staging / "jobs" / job_id
            for sub in ("source", "derived", "current", "out", "history"):
                (job_dir / sub).mkdir(parents=True, exist_ok=True)

            parent_job = parent_dir / "jobs" / job_id
            source_name = Path(job["source"]["relpath"]).name
            if (parent_job / "source" / source_name).is_file():
                shutil.copy2(
                    parent_job / "source" / source_name,
                    job_dir / "source" / source_name,
                )
            derived = parent_job / "derived" / "vacancy_normalized.md"
            if derived.is_file():
                shutil.copy2(derived, job_dir / "derived" / "vacancy_normalized.md")

            states: dict[str, str] = {}
            rebound: dict[str, dict[str, Any]] = {}
            for artifact, filename in ARTIFACT_FILES.items():
                parent_artifact = parent_job / "current" / filename
                if not parent_artifact.is_file():
                    states[artifact] = ABSENT
                    continue
                if revision_migrated:
                    # A different revision changes the semantic contract;
                    # regenerate rather than rebind its artifacts.
                    states[artifact] = REGENERATE_REQUIRED
                    continue
                if job["job_class"] != "CORE":
                    states[artifact] = REGENERATE_REQUIRED
                    continue
                if from_stage is not None and ARTIFACT_STAGE[artifact] >= from_stage:
                    states[artifact] = REGENERATE_REQUIRED
                    continue
                if not parent_states[job_id].current(artifact):
                    states[artifact] = REGENERATE_REQUIRED
                    continue
                if not _same_governing_inputs(
                    parent, child, artifact
                ):
                    states[artifact] = REGENERATE_REQUIRED
                    continue
                if any(states.get(dependency) != REUSED
                       for dependency in DEPENDENCIES[artifact]):
                    states[artifact] = REGENERATE_REQUIRED
                    continue

                payload = read_json(parent_artifact)
                if artifact == "review":
                    binding = {
                        "run_id": run_id,
                        "job_id": job_id,
                        "final_package_sha256": artifacts_module.artifact_hash(
                            rebound["final_package"]
                        ),
                    }
                else:
                    binding = {
                        "run_id": run_id,
                        "job_id": job_id,
                        "employer": job["employer"],
                        "title": job["title"],
                        "manifest_sha256": child_context.manifest_sha256,
                        "vacancy_sha256": child_context.vacancy_sha256(job_id),
                        "evidence_index_sha256": child_context.index_sha256,
                        "stage_instruction_sha256": (
                            child_context.stage_instruction_sha256(artifact)
                        ),
                    }
                    if artifact == "final_package":
                        binding["baseline_map_sha256"] = (
                            child_context.assets.record("baseline_map")["sha256"]
                        )
                        binding["strategy_sha256"] = artifacts_module.artifact_hash(
                            rebound["strategy"]
                        )
                payload["binding"] = binding

                checked = validate_module.validate_artifact(
                    layout, child_context, job_id, artifact, payload
                )
                if not checked.ok:
                    states[artifact] = REGENERATE_REQUIRED
                    continue
                atomic_write_json(job_dir / "current" / filename, payload)
                rebound[artifact] = payload
                states[artifact] = REUSED
            disposition[job_id] = states

        ancestor_after = {
            path.relative_to(ancestor_root).as_posix(): sha256_file(path)
            for path in sorted(ancestor_root.rglob("*")) if path.is_file()
        }
        for path in sorted(set(ancestor_before) | set(ancestor_after)):
            before = ancestor_before.get(path)
            after = ancestor_after.get(path)
            if before != after:
                result.add(
                    "ACC-03", f"runs/{root_ancestor}/{path}", "-",
                    f"ancestor tree entry unchanged ({before or 'absent'})",
                    f"changed to {after or 'absent'} during branch",
                )
        result.extend(
            _verify_frozen_assets(
                FrozenRunAssets(layout, child, base_dir=staging)
            ).violations
        )
        if not result.ok:
            shutil.rmtree(staging, ignore_errors=True)
            return BranchResult(None, None, result, disposition)

        final.parent.mkdir(parents=True, exist_ok=True)
        staging.rename(final)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
        raise

    return BranchResult(run_id, child, result, disposition)
