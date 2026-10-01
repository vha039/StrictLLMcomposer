"""Mechanical validation of current semantic artifacts.

INV-07 keeps three classes separate. This module implements exactly one of
them -- the mechanical boundary. It never judges truth, relevance,
naturalness, persuasive quality or semantic support, and no result it
produces may be presented as proof of any of those (Spec 14.1).

The complete permitted scope is Spec 14.2 / Contract 8.2:
schema and parse validity; exact run/job/employer/title identity;
expected-set membership; immutable source/input hashes; known factual
evidence IDs and allowed source namespace; known mechanical
employment/baseline IDs; path/root/type safety; template-map mechanics;
private/control-token leakage in employer-facing fields; output existence
and extraction; static staleness.

Reference validation proves only that the ID exists, belongs to an allowed
authority namespace, and matches the run's hashes. It does not prove that
every factual implication is covered or that the evidence supports the
wording (Spec 14.4).
"""

from __future__ import annotations

from datetime import date
from typing import Any

from . import X2B_REVISION
from . import artifacts as artifacts_module
from . import leakage as leakage_module
from . import retrieval
from .atomicio import read_json
from .baseline import employment_ids, mechanical_refs
from .errors import ValidationResult
from .evidence_index import evidence_ids
from .hashing import sha256_file
from .manifest import FrozenRunAssets, find_job, read_frozen
from .paths import Layout
from .schemas import validate_against_schema

STAGE_INSTRUCTION_KEY = {
    "strategy": "stage1",
    "draft_package": "stage2",
    "final_package": "stage3",
}


class RunContext:
    """Everything validation needs from one frozen run, loaded once."""

    def __init__(
        self, layout: Layout, manifest: dict[str, Any], *, run_dir: Any = None
    ) -> None:
        from .atomicio import read_json

        self.layout = layout
        self.manifest = manifest
        self.run_id = manifest["run_id"]
        self.assets = FrozenRunAssets(layout, manifest, run_dir)
        self.schemas_dir = self.assets.schemas_dir

        self.index = self.assets.json("evidence_index")
        self.baseline_map = self.assets.json("baseline_map")
        self.facets = self.assets.json("personality_facet_index")
        self.evidence_ids = evidence_ids(self.index)
        self.baseline_refs = mechanical_refs(self.baseline_map)
        self.employment_ids = employment_ids(self.baseline_map)
        self.facet_ids = {f["facet_id"] for f in self.facets["facets"]}
        self.typology_tokens = self.facets.get("private_typology_tokens", [])
        self.index_sha256 = read_frozen(layout, manifest, "evidence_index")["sha256"]
        self.manifest_sha256 = sha256_file(self.assets.run_dir / "manifest.json")

    def stage_instruction_sha256(self, artifact: str) -> str | None:
        key = STAGE_INSTRUCTION_KEY.get(artifact)
        if key is None:
            return None
        return read_frozen(self.layout, self.manifest, "stage_instructions", key)["sha256"]

    def vacancy_sha256(self, job_id: str) -> str:
        return find_job(self.manifest, job_id)["source"]["sha256"]


# --------------------------------------------------------------------------
# Shared checks
# --------------------------------------------------------------------------

def _check_identity(
    binding: dict[str, Any],
    job: dict[str, Any],
    run_id: str,
    *,
    label: str,
    result: ValidationResult,
) -> None:
    """ACC-10: exact run/job/employer/title identity, no drift."""
    for field, expected in (
        ("run_id", run_id),
        ("job_id", job["job_id"]),
        ("employer", job["employer"]),
        ("title", job["title"]),
    ):
        observed = binding.get(field)
        if observed != expected:
            result.add(
                "ACC-10", label, f"binding.{field}",
                f"{expected!r} (from the immutable manifest)",
                f"{observed!r}",
            )


def _check_frozen_hashes(
    binding: dict[str, Any],
    context: RunContext,
    job_id: str,
    artifact: str,
    *,
    label: str,
    result: ValidationResult,
) -> None:
    expectations = {
        "manifest_sha256": context.manifest_sha256,
        "vacancy_sha256": context.vacancy_sha256(job_id),
        "evidence_index_sha256": context.index_sha256,
    }
    instruction = context.stage_instruction_sha256(artifact)
    if instruction is not None:
        expectations["stage_instruction_sha256"] = instruction

    for field, expected in expectations.items():
        observed = binding.get(field)
        if observed is None:
            continue  # schema decides whether the field is required
        if observed != expected:
            result.add(
                "DEC-26", label, f"binding.{field}",
                f"{expected}",
                f"{observed} - this artifact was written against different "
                "frozen inputs than the run it claims to belong to.",
            )


def _check_factual_refs(
    refs: list[str],
    context: RunContext,
    *,
    label: str,
    location: str,
    result: ValidationResult,
) -> None:
    """DEC-34 / ACC-08: EV: namespace only, and the id must resolve."""
    for index, ref in enumerate(refs or []):
        where = f"{location}[{index}]"
        if ref in context.baseline_refs or ref.startswith("BL:"):
            result.add(
                "DEC-34", label, where,
                "a factual evidence reference resolving to one of the three "
                "candidate authorities through the evidence index",
                f"{ref!r} is a mechanical baseline reference. Baseline IDs use a "
                "separate namespace and never count as factual support; a "
                "baseline identifier does not become evidence merely by being "
                "addressable.",
            )
            continue
        if ref not in context.evidence_ids:
            result.add(
                "ACC-08", label, where,
                "an evidence ID present in the frozen evidence index",
                f"{ref!r} does not resolve. Reference existence proves "
                "resolvability only, never semantic support.",
            )


def _check_baseline_refs(
    refs: list[str], context: RunContext, *, label: str, location: str,
    result: ValidationResult,
) -> None:
    for index, ref in enumerate(refs or []):
        if ref not in context.baseline_refs:
            result.add(
                "DEC-34", label, f"{location}[{index}]",
                "a baseline reference present in the mechanical baseline map",
                f"{ref!r} does not resolve",
            )


# --------------------------------------------------------------------------
# Per-artifact validation
# --------------------------------------------------------------------------

def validate_strategy(
    payload: dict[str, Any], context: RunContext, job_id: str
) -> ValidationResult:
    result = ValidationResult()
    label = "strategy.json"
    job = find_job(context.manifest, job_id)

    validate_against_schema(
        payload, context.schemas_dir, "strategy", file_label=label, result=result
    )
    binding = payload.get("binding") or {}
    _check_identity(binding, job, context.run_id, label=label, result=result)
    _check_frozen_hashes(binding, context, job_id, "strategy", label=label, result=result)

    for index, requirement in enumerate(payload.get("material_requirements") or []):
        _check_factual_refs(
            requirement.get("evidence_refs") or [], context,
            label=label, location=f"material_requirements[{index}].evidence_refs",
            result=result,
        )
    for index, plan in enumerate(payload.get("evidence_plan") or []):
        _check_factual_refs(
            plan.get("evidence_refs") or [], context,
            label=label, location=f"evidence_plan[{index}].evidence_refs", result=result,
        )
        _check_baseline_refs(
            plan.get("baseline_refs") or [], context,
            label=label, location=f"evidence_plan[{index}].baseline_refs", result=result,
        )
    counterfactual = payload.get("counterfactual_route")
    if isinstance(counterfactual, dict):
        _check_factual_refs(
            counterfactual.get("evidence_refs") or [], context,
            label=label, location="counterfactual_route.evidence_refs", result=result,
        )
    if context.manifest.get("spec_revision") == X2B_REVISION:
        for ref in retrieval.selected_strategy_refs(context.index, payload):
            if ref.endswith("#file"):
                result.add(
                    "INV-06", label, "evidence_plan",
                    "granular evidence sections for the closed Stage-3 packet",
                    f"{ref!r} selects an entire authority file",
                )
        seen: set[str] = set()
        for index, override in enumerate(
            (payload.get("cv_draft") or {}).get("employment_overrides") or []
        ):
            employment_id = override.get("employment_id")
            if employment_id not in context.employment_ids or employment_id in seen:
                result.add(
                    "ACC-11", label, f"cv_draft.employment_overrides[{index}].employment_id",
                    "a known, unique baseline employment ID",
                    f"{employment_id!r} is unknown or repeated",
                )
            seen.add(employment_id)
    else:
        _check_baseline_refs(
            (payload.get("cv_direction") or {}).get("employment_focus") or [], context,
            label=label, location="cv_direction.employment_focus", result=result,
        )

    # Personality: the 0-3 bound and evidence binding are schema-enforced.
    # Here we check facet-id membership in the closed set (ACC-09).
    for index, facet in enumerate(payload.get("personality_facets") or []):
        facet_id = facet.get("facet_id")
        if facet_id not in context.facet_ids:
            result.add(
                "DEC-35", label, f"personality_facets[{index}].facet_id",
                "a facet ID present in policy/personality_facets.json",
                f"{facet_id!r} is not in the closed facet set",
            )
        _check_factual_refs(
            facet.get("evidence_refs") or [], context,
            label=label, location=f"personality_facets[{index}].evidence_refs",
            result=result,
        )
    return result


def validate_package(
    payload: dict[str, Any],
    context: RunContext,
    job_id: str,
    *,
    expected_stage: str,
    soft_thresholds: dict[str, int] | None = None,
) -> ValidationResult:
    result = ValidationResult()
    artifact = "draft_package" if expected_stage == "STAGE2_DRAFT" else "final_package"
    label = artifacts_module.ARTIFACTS[artifact][0]
    job = find_job(context.manifest, job_id)

    validate_against_schema(
        payload, context.schemas_dir, "package", file_label=label, result=result
    )
    if payload.get("source_stage") != expected_stage:
        result.add(
            "ACC-10", label, "source_stage",
            expected_stage, f"{payload.get('source_stage')!r}",
        )
    finalization = payload.get("finalization") or {}
    if finalization.get("state") == "FINALIZED":
        document_date = finalization.get("document_date")
        try:
            parsed = date.fromisoformat(document_date)
        except (TypeError, ValueError):
            parsed = None
        if parsed is None or parsed.isoformat() != document_date:
            result.add(
                "DEC-38", label, "finalization.document_date",
                "a real canonical ISO date in YYYY-MM-DD form",
                f"{document_date!r}",
            )

    binding = payload.get("binding") or {}
    _check_identity(binding, job, context.run_id, label=label, result=result)
    _check_frozen_hashes(binding, context, job_id, artifact, label=label, result=result)

    _check_factual_refs(
        payload.get("used_evidence_refs") or [], context,
        label=label, location="used_evidence_refs", result=result,
    )
    if (
        expected_stage == "STAGE3_FINAL"
        and context.manifest.get("spec_revision") == X2B_REVISION
    ):
        strategy_path = (
            context.assets.run_dir / "jobs" / job_id / "current" / "strategy.json"
        )
        strategy = read_json(strategy_path) if strategy_path.is_file() else None
        if strategy is None:
            result.add(
                "INV-06", label, "used_evidence_refs",
                "a current Stage-1 evidence packet",
                "strategy is missing; run Stage 1 before Stage 3",
            )
        else:
            selected = set(retrieval.selected_strategy_refs(context.index, strategy))
            for ref in payload.get("used_evidence_refs") or []:
                if ref not in selected:
                    result.add(
                        "INV-06", label, "used_evidence_refs",
                        "an EV reference supplied in the Stage-1 evidence packet",
                        f"{ref!r} was not selected; restart Stage 1 to expand the packet",
                    )

    # ACC-11: only known employment IDs, no duplicates.
    seen: list[str] = []
    for index, override in enumerate((payload.get("cv") or {}).get("employment_overrides") or []):
        employment_id = override.get("employment_id")
        if employment_id not in context.employment_ids:
            result.add(
                "ACC-11", label, f"cv.employment_overrides[{index}].employment_id",
                f"a known baseline employment ID from {sorted(context.employment_ids)}",
                f"{employment_id!r} is unknown. A model stage may not add or "
                "remove employment identities.",
            )
        if employment_id in seen:
            result.add(
                "ACC-11", label, f"cv.employment_overrides[{index}].employment_id",
                "each employment overridden at most once",
                f"{employment_id!r} is overridden more than once",
            )
        seen.append(employment_id)

    leakage_module.scan_package(
        payload, file_label=label,
        typology_tokens=context.typology_tokens, result=result,
    )

    if soft_thresholds:
        result.extend(
            artifacts_module.soft_quality_warnings(
                payload, soft_thresholds, file_label=label
            ).violations
        )
    return result


def validate_review(
    payload: dict[str, Any], context: RunContext, job_id: str
) -> ValidationResult:
    result = ValidationResult()
    label = "review.json"
    job = find_job(context.manifest, job_id)

    validate_against_schema(
        payload, context.schemas_dir, "review", file_label=label, result=result
    )
    binding = payload.get("binding") or {}
    for field, expected in (("run_id", context.run_id), ("job_id", job["job_id"])):
        if binding.get(field) != expected:
            result.add("ACC-10", label, f"binding.{field}", f"{expected!r}",
                       f"{binding.get(field)!r}")
    return result


def validate_artifact(
    layout: Layout,
    context: RunContext,
    job_id: str,
    artifact: str,
    payload: dict[str, Any],
    *,
    soft_thresholds: dict[str, int] | None = None,
) -> ValidationResult:
    name = artifacts_module.canonical_name(artifact)
    if name == "strategy":
        return validate_strategy(payload, context, job_id)
    if name == "draft_package":
        return validate_package(
            payload, context, job_id, expected_stage="STAGE2_DRAFT",
            soft_thresholds=soft_thresholds,
        )
    if name == "final_package":
        return validate_package(
            payload, context, job_id, expected_stage="STAGE3_FINAL",
            soft_thresholds=soft_thresholds,
        )
    return validate_review(payload, context, job_id)
