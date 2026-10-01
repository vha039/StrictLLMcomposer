"""Child branch: the only way to change anything a run froze.

A child is a new run under `runs/<root>/branches/<component>` with its own
manifest and a `parent_run_id`. The parent is never touched.

Two input classes, deliberately different:

* **Facts** - the three authorities, the CV baseline, the evidence index and
  the baseline map - are **inherited from the parent** by default, so a
  reused artifact still points at the evidence it was actually written
  against. `--refresh-inputs` re-collects them from the repository and then
  drops every artifact whose evidence fingerprint no longer matches.
* **Control plane** - settings, the stage playbooks, writing policy,
  personality files, templates and schemas - is always taken live, because
  editing those is the usual reason to branch. It never invalidates an
  artifact by identity; reused artifacts retain their original policy
  fingerprint, and must still validate against the child's schemas.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import SCHEMA_REVISION, SPEC_REVISION
from . import artifacts as artifacts_module
from . import pipeline
from . import settings as settings_module
from .atomicio import atomic_write_json
from .baseline import check_baseline_map
from .errors import ConfigurationError, ValidationResult
from .evidence_index import check_index
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
    require_intact,
    utc_now,
)
from .paths import BRANCHES_DIR, MAX_BRANCH_COMPONENT, Layout, split_run_reference
from .schemas import validate_against_schema

DEFAULT_LABEL = "child"

#: Inherited from the parent unless --refresh-inputs. Everything else in
#: frozen_inputs is control plane and always taken live.
FACT_KEYS: tuple[tuple[str, ...], ...] = (
    ("authorities",), ("cv_baseline",), ("evidence_index",), ("baseline_map",),
)

REUSED = "REUSED"
DROPPED = "DROPPED"


@dataclass
class BranchResult:
    run_id: str | None
    manifest: dict[str, Any] | None
    result: ValidationResult = field(default_factory=ValidationResult)
    #: job_id -> {artifact: REUSED | DROPPED}
    disposition: dict[str, dict[str, str]] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.result.ok and self.run_id is not None


def _label_component(from_stage: int | None, label: str, moment: datetime) -> str:
    stamp = moment.astimezone(timezone.utc).strftime("%Y%m%dt%H%M%S")
    stage = "s" + (str(from_stage) if from_stage is not None else "x")
    component = f"{stage}_{label}_{stamp}"[:MAX_BRANCH_COMPONENT]
    return component.rstrip("_-")


def branch(
    layout: Layout,
    parent_run_id: str,
    *,
    reviewed_by: str,
    from_stage: int | None = None,
    label: str = DEFAULT_LABEL,
    refresh_inputs: bool = False,
    moment: datetime | None = None,
) -> BranchResult:
    """Create one child run. `from_stage` is the first stage to execute again."""
    moment = moment or utc_now()
    if from_stage is not None and from_stage not in pipeline.STAGE_ORDER:
        raise ConfigurationError(
            f"--from-stage must be one of {list(pipeline.STAGE_ORDER)}; got {from_stage!r}."
        )
    result = ValidationResult()
    parent = load_manifest(layout, parent_run_id)
    parent_dir = layout.run_dir(parent_run_id)
    require_intact(layout, parent)

    from .validate import RunContext, validate_artifact
    parent_context = RunContext(layout, parent)

    try:
        settings = settings_module.load(layout)
    except ConfigurationError as exc:
        result.add("CTR-01", "policy/settings.toml", "-", "readable settings", str(exc))
        return BranchResult(None, None, result)

    live_inputs, index, baseline_map = collect_frozen_inputs(layout)
    if refresh_inputs:
        result.extend(check_index(index, layout.authorities).violations)
        result.extend(check_baseline_map(baseline_map).violations)

    frozen_inputs = dict(live_inputs)
    if not refresh_inputs:
        for keys in FACT_KEYS:
            frozen_inputs[keys[0]] = parent["frozen_inputs"][keys[0]]

    reconciliation, conflicts = _reconciliation(layout, reviewed_by, moment)
    if refresh_inputs:
        for conflict in conflicts:
            result.add("CTR-01", "authorities/CV_BASELINE.md",
                       "baseline_reconciliation",
                       "no known baseline-versus-authority conflict", conflict)
    else:
        reconciliation = parent["baseline_reconciliation"]

    root_ancestor, _ = split_run_reference(parent_run_id)
    run_id = f"{root_ancestor}/{BRANCHES_DIR}/{_label_component(from_stage, label, moment)}"

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
    staging = layout.runs / f".branching-{_label_component(from_stage, label, moment)}"
    if staging.exists():
        shutil.rmtree(staging)

    disposition: dict[str, dict[str, str]] = {}
    try:
        staging.mkdir(parents=True)
        (staging / "audit").mkdir()
        for record in _iter_frozen_records(frozen_inputs):
            target = staging / FROZEN_DIR / record["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            source = layout.root / record["path"]
            if not source.is_file() or record["sha256"] != _sha(source):
                source = parent_dir / FROZEN_DIR / record["path"]
            shutil.copy2(source, target)

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
                shutil.copy2(parent_job / "source" / source_name,
                             job_dir / "source" / source_name)
            derived = parent_job / "derived" / "vacancy_normalized.md"
            if derived.is_file():
                shutil.copy2(derived, job_dir / "derived" / "vacancy_normalized.md")

            states: dict[str, str] = {}
            accepted: dict[str, dict[str, Any]] = {}
            parent_hashes: dict[str, str] = {}
            drop_from = from_stage
            facts_match = (
                pipeline.factual_hashes(parent_context) == pipeline.factual_hashes(child_context)
                and parent_context.vacancy_sha256(job_id) == child_context.vacancy_sha256(job_id)
            )
            for stage in pipeline.STAGE_ORDER:
                candidates = {
                    name: artifacts_module.load(layout, parent_run_id, job_id, name)
                    for name, spec in pipeline.ARTIFACTS.items()
                    if (spec.owner_stage if spec.owner_stage is not None else 3) == stage
                }
                candidates = {name: payload for name, payload in candidates.items() if payload is not None}
                staged: dict[str, dict[str, Any]] = {}
                staged_parent_hashes: dict[str, str] = {}
                for name, original in candidates.items():
                    if drop_from is not None and stage >= drop_from:
                        break
                    binding = original.get("binding") or {}
                    recorded = binding.get("inputs") or {}
                    known_parent = {**parent_hashes, **staged_parent_hashes}
                    available = {**accepted, **staged}
                    declared = pipeline.ARTIFACTS[name].inputs
                    child_inputs = {
                        key: artifacts_module.artifact_hash(available[key])
                        for key in declared if key in available
                    }
                    if name == "review" and original.get("triage") == "RERUN":
                        child_inputs.pop("final_package", None)
                    reusable = (
                        facts_match
                        and artifacts_module._stale_reason(parent_context, job_id, name, original) is None
                        and set(recorded) == set(child_inputs)
                        and all(known_parent.get(key) == digest for key, digest in recorded.items())
                    )
                    if not reusable:
                        drop_from = stage
                        break
                    payload = dict(original)
                    payload["binding"] = artifacts_module.binding_for(
                        child_context, job_id, name, upstream=child_inputs
                    )
                    payload["binding"]["policy_fingerprint"] = binding["policy_fingerprint"]
                    checked = validate_artifact(
                        layout, child_context, job_id, name, payload, loaded=available
                    )
                    if not checked.ok:
                        drop_from = stage
                        break
                    staged[name] = payload
                    staged_parent_hashes[name] = artifacts_module.artifact_hash(original)
                if drop_from is not None and stage >= drop_from:
                    states.update({name: DROPPED for name in candidates})
                    continue
                for name, payload in staged.items():
                    atomic_write_json(job_dir / "current" / pipeline.ARTIFACTS[name].filename, payload)
                    states[name] = REUSED
                accepted.update(staged)
                parent_hashes.update(staged_parent_hashes)
            disposition[job_id] = states

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


def _sha(path: Path) -> str:
    from .hashing import sha256_file

    return sha256_file(path)
