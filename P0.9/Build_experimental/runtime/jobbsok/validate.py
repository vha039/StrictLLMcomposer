"""Mechanical validation of current semantic artifacts.

One generic path for every artifact in `pipeline.ARTIFACTS`:

* schema and parse validity;
* exact run/job/employer/title identity;
* every `EV:` string in the payload resolves through the frozen evidence
  index, and no `BL:` string is offered where evidence is expected;
* known baseline employment IDs, each overridden at most once;
* facet IDs inside the closed set;
* private/control-token leakage in employer-facing fields;
* for the assembled package, a real canonical document date.

It never judges truth, relevance, persuasive quality or semantic support.
Reference validation proves resolvability only.
"""

from __future__ import annotations

from datetime import date
from collections import Counter
from typing import Any

from . import artifacts as artifacts_module
from . import leakage as leakage_module
from . import pipeline
from . import assemble as assemble_module
from . import signals
from .baseline import employment_ids, mechanical_refs
from .errors import ValidationResult
from .evidence_index import evidence_ids
from .hashing import sha256_file
from .manifest import FrozenRunAssets, find_job, read_frozen
from .paths import Layout
from .schemas import validate_against_schema


class RunContext:
    """Everything validation and the bundles need from one frozen run."""

    def __init__(
        self, layout: Layout, manifest: dict[str, Any], *, run_dir: Any = None
    ) -> None:
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

    def vacancy_sha256(self, job_id: str) -> str:
        return find_job(self.manifest, job_id)["source"]["sha256"]

    @property
    def settings(self) -> dict[str, Any]:
        return self.assets.settings


# --------------------------------------------------------------------------
# Shared checks
# --------------------------------------------------------------------------


def _walk(node: Any, path: str = ""):
    """Yield (location, value) for every scalar in a payload."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield from _walk(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _walk(value, f"{path}[{index}]")
    else:
        yield path, node


def _check_identity(
    binding: dict[str, Any], job: dict[str, Any], run_id: str,
    *, label: str, result: ValidationResult,
) -> None:
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
                f"{expected!r} (from the immutable manifest)", f"{observed!r}",
            )


def _check_references(
    payload: dict[str, Any], context: RunContext, *, label: str, result: ValidationResult
) -> None:
    """Every EV: string resolves; BL: never passes as evidence."""
    for location, value in _walk(payload):
        if not isinstance(value, str):
            continue
        if value.startswith("EV:") and value not in context.evidence_ids:
            result.add(
                "ACC-08", label, location,
                "an evidence ID present in the frozen evidence index",
                f"{value!r} does not resolve. Reference existence proves "
                "resolvability only, never semantic support.",
            )
        elif value.startswith("BL:"):
            if value not in context.baseline_refs:
                result.add(
                    "DEC-34", label, location,
                    "a baseline reference present in the mechanical baseline map",
                    f"{value!r} does not resolve",
                )
            elif location.endswith("refs") or "evidence" in location:
                result.add(
                    "DEC-34", label, location,
                    "a factual evidence reference (EV:) resolving through the "
                    "evidence index",
                    f"{value!r} is a mechanical baseline reference; a baseline "
                    "identifier never counts as factual support.",
                )
        elif (
            value.startswith("PF-")
            and "facet" in location
            and value not in context.facet_ids
        ):
            result.add(
                "DEC-35", label, location,
                "a facet ID present in policy/personality_facets.json",
                f"{value!r} is not in the closed facet set",
            )


def _check_cv_block(
    cv: dict[str, Any], context: RunContext, *, label: str, result: ValidationResult
) -> None:
    seen: list[str] = []
    for index, override in enumerate(cv.get("employment_overrides") or []):
        employment_id = override.get("employment_id")
        if employment_id not in context.employment_ids:
            result.add(
                "ACC-11", label, f"cv.employment_overrides[{index}].employment_id",
                f"a known baseline employment ID from {sorted(context.employment_ids)}",
                f"{employment_id!r} is unknown. A stage may not add or remove "
                "employment identities.",
            )
        if employment_id in seen:
            result.add(
                "ACC-11", label, f"cv.employment_overrides[{index}].employment_id",
                "each employment overridden at most once",
                f"{employment_id!r} is overridden more than once",
            )
        seen.append(employment_id)


# --------------------------------------------------------------------------
# Public entry point
# --------------------------------------------------------------------------


def _check_declarations(context, job_id, name, payload, loaded, result):
    label = pipeline.ARTIFACTS[name].filename

    def error(field, expected, observed):
        result.add("CTR-07", label, field, expected, str(observed))

    cv = loaded.get("cv_draft") or {}
    advocacy = payload if name == "advocacy_draft" else loaded.get("advocacy_draft") or {}
    if name == "final_package":
        package, summary = payload, {}
    else:
        package, summary = assemble_module.assemble(
            cv, advocacy, payload if name == "polish" else None
        )

    def text_for(keystone):
        if keystone.get("document") == "LETTER":
            return signals.letter_text(package.get("letter"))
        from .merge import effective_cv
        effective = effective_cv(context.baseline_map, package)
        rendered_cv = {**(package.get("cv") or {}), "employment_overrides": [
            {"bullets": item["bullets"]} for item in effective["employments"]
        ]}
        return signals.cv_text(rendered_cv)

    keystones = advocacy.get("keystones") or []
    if name == "advocacy_draft":
        ids = [item["id"] for item in keystones]
        if len(set(ids)) != len(ids):
            error("keystones", "unique keystone ids", ids)
        for item in keystones:
            if item["text"] not in text_for(item):
                error(f"keystones.{item['id']}.text", "verbatim text in " + item["document"], "absent")
    if name == "polish":
        dispositions = payload.get("keystone_disposition") or []
        wanted = Counter(item["id"] for item in keystones)
        actual = Counter(item["id"] for item in dispositions)
        if actual != wanted or any(count != 1 for count in actual.values()):
            error("keystone_disposition", "every upstream keystone id exactly once", list(actual.elements()))
        kept = {item["id"] for item in dispositions if item["disposition"] == "KEPT"}
        for item in keystones:
            if item["id"] in kept and item["text"] not in text_for(item):
                error(f"keystone_disposition.{item['id']}", "KEPT text still verbatim in " + item["document"], "absent")
        declared = {item["field"] for item in payload.get("changes") or [] if item.get("reason")}
        for field in sorted(set(summary["changed"].get("polish", [])) - declared):
            error("changes", "changed field declared with a reason", field)

    if name in ("advocacy_draft", "final_package"):
        delivery = (loaded.get("brief") or {}).get("delivery")
        letter = package.get("letter")
        if delivery == "LETTER_AND_CV":
            if not letter or not all(letter.get(k) for k in ("opening", "body_paragraphs", "closing")):
                error("letter", "LETTER_AND_CV: opening, at least one body paragraph, closing", letter)
        elif delivery in ("CV_ONLY", "CV_PLUS_FORM_ANSWERS"):
            if letter is not None:
                error("letter", delivery + ": letter null", "letter present")
            if delivery == "CV_PLUS_FORM_ANSWERS":
                questions = ((loaded.get("scout") or {}).get("submission") or {}).get("screening_questions") or []
                if not questions:
                    error("form_answers", "source screening questions", "no source questions recorded")
                elif Counter(item["question"] for item in package.get("form_answers") or []) != Counter(questions):
                    error("form_answers", "one entry per source screening question", "questions differ")


def validate_artifact(
    layout: Layout,
    context: RunContext,
    job_id: str,
    artifact: str,
    payload: dict[str, Any],
    *,
    soft_thresholds: dict[str, int] | None = None,
    loaded: dict[str, Any] | None = None,
) -> ValidationResult:
    name = pipeline.canonical_name(artifact)
    spec = pipeline.ARTIFACTS[name]
    label = spec.filename
    result = ValidationResult()
    job = find_job(context.manifest, job_id)

    validate_against_schema(
        payload, context.schemas_dir, spec.schema, file_label=label, result=result
    )
    binding = payload.get("binding") or {}
    _check_identity(binding, job, context.run_id, label=label, result=result)
    _check_references(payload, context, label=label, result=result)

    if result.ok and name in ("advocacy_draft", "polish", "final_package"):
        if loaded is None:
            loaded = {
                key: artifacts_module.load(layout, context.run_id, job_id, key)
                for key in ("scout", "brief", "cv_draft", "advocacy_draft")
            }
        _check_declarations(context, job_id, name, payload, loaded, result)

    cv = payload.get("cv")
    if isinstance(cv, dict):
        _check_cv_block(cv, context, label=label, result=result)

    if payload.get("cv") is not None or payload.get("letter") is not None:
        leakage_module.scan_package(
            payload, file_label=label,
            typology_tokens=context.typology_tokens, result=result,
        )

    if name == "final_package":
        if payload.get("source_stage") != "ASSEMBLED":
            result.add(
                "ACC-10", label, "source_stage", "ASSEMBLED",
                f"{payload.get('source_stage')!r}",
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
        if soft_thresholds:
            result.extend(
                artifacts_module.soft_quality_warnings(
                    payload, soft_thresholds, file_label=label
                ).violations
            )

    if name == "review":
        triage = payload.get("triage")
        inputs = binding.get("inputs") or {}
        if triage == "RERUN":
            if "final_package" in inputs:
                result.add("CTR-07", label, "binding.inputs", "RERUN binds no final_package", "final_package present")
            if payload.get("rerun_stage") not in (1, 2):
                result.add(
                    "CTR-07", label, "rerun_stage",
                    "1 or 2 when triage is RERUN",
                    f"{payload.get('rerun_stage')!r}",
                )
        elif payload.get("rerun_stage") is not None:
            result.add("CTR-07", label, "rerun_stage", "absent or null for publication", repr(payload["rerun_stage"]))
        if triage != "RERUN" and "final_package" not in inputs:
            result.add(
                "CTR-07", label, "binding.inputs.final_package",
                "the assembled final package hash for a READY/CHECK review",
                "absent",
            )
    return result
