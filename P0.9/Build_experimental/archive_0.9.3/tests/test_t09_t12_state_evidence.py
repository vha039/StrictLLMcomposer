"""Tier-1 items 9-12: state axes, staleness, evidence namespace, no partition."""

from __future__ import annotations

import json

import pytest

from jobbsok import artifacts as artifacts_module
from jobbsok import failure as failure_module
from jobbsok import status as status_module
from jobbsok import validate as validate_module
from jobbsok.atomicio import atomic_write_json, read_json
from jobbsok.evidence_index import build_index, check_index, evidence_ids, slugify


def _write_render_report(layout, run_id, job_id, *, overall, pdf_state="OK"):
    report = {
        "artifact_role": "RENDER_REPORT",
        "binding": {
            "run_id": run_id, "job_id": job_id,
            "final_package_sha256": "0" * 64, "document_date": "2026-08-23",
            "baseline_map_sha256": "0" * 64, "cv_master_sha256": "0" * 64,
            "letter_master_sha256": "0" * 64, "template_map_sha256": "0" * 64,
            "render_config": {"converter": "word_com",
                              "invocation_granularity": "per_document"},
        },
        "render_state": {
            "cv_docx": "OK", "cv_pdf": pdf_state,
            "letter_docx": "OK", "letter_pdf": pdf_state, "overall": overall,
        },
        "documents": [
            {"component": "cv", "format": "docx", "state": "OK", "checks": {}},
            {"component": "cv", "format": "pdf", "state": pdf_state, "checks": {},
             "limitation": None if pdf_state == "OK" else "PDF not verified.",
             "human_action": None if pdf_state == "OK" else "Export manually."},
        ],
        "rendered_at": "2026-08-23T06:00:00Z",
    }
    atomic_write_json(
        layout.job_dir(run_id, job_id) / "current" / "render_report.json", report
    )
    return report


# --------------------------------------------------------------------------
# T09 Three orthogonal state axes (DEC-42)
# --------------------------------------------------------------------------

def test_t09_axes_are_three_separate_fields(staged):
    layout, run_id, manifest, job_id, _ = staged
    job = status_module.derive(layout, manifest)["jobs"][0]
    assert "semantic_triage" in job
    assert "production_state" in job and "highest_valid_stage" in job
    assert "semantic_final_available" in job
    assert isinstance(job["render_state"], dict) and "overall" in job["render_state"]


@pytest.mark.parametrize("triage", ["READY", "CHECK", "RERUN"])
def test_t09_pdf_degradation_does_not_change_semantic_triage(staged, triage):
    """DEC-41 / ACC-06: a PDF problem is never a semantic status."""
    layout, run_id, manifest, job_id, fixture_dir = staged
    review = read_json(fixture_dir / "review.json")
    review["triage"] = triage
    atomic_write_json(
        layout.job_dir(run_id, job_id) / "current" / "review.json", review
    )

    _write_render_report(layout, run_id, job_id, overall="OK", pdf_state="OK")
    good = status_module.derive(layout, manifest)["jobs"][0]

    _write_render_report(layout, run_id, job_id, overall="DEGRADED", pdf_state="DEGRADED")
    degraded = status_module.derive(layout, manifest)["jobs"][0]

    assert good["semantic_triage"] == triage
    assert degraded["semantic_triage"] == triage, (
        "PDF degradation must not touch the semantic axis"
    )
    assert good["production_state"] == degraded["production_state"] == "VALID"
    assert good["semantic_final_available"] is degraded["semantic_final_available"] is True
    assert degraded["render_state"]["overall"] == "FAILED", (
        "an unverified synthetic receipt must not be presented as current"
    )
    assert degraded["render_state"]["human_action"]


def test_t09_no_combined_status_enum_exists_anywhere(layout):
    """Spec 7.5: no READY_DOCX_ONLY-style variant may exist.

    Checked structurally against the schemas' enum and const values rather
    than by scanning prose, because documenting the exclusion requires
    naming it.
    """
    banned = {"READY_DOCX_ONLY", "DOCX_ONLY", "CHECK_DOCX", "READY_PDF",
              "VALID_DEGRADED", "READY_DEGRADED"}
    values: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in ("description", "$comment", "title", "note"):
                    continue
                if key == "const" and isinstance(value, str):
                    values.add(value)
                if key == "enum" and isinstance(value, list):
                    values.update(v for v in value if isinstance(v, str))
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for path in sorted((layout.schemas).glob("*.schema.json")):
        walk(json.loads(path.read_text(encoding="utf-8")))

    assert not (values & banned), values & banned

    status_schema = json.loads(
        (layout.schemas / "status.schema.json").read_text(encoding="utf-8")
    )
    job = status_schema["properties"]["jobs"]["items"]["properties"]
    assert set(job["semantic_triage"]["enum"]) == {"READY", "CHECK", "RERUN", None}
    assert set(job["production_state"]["enum"]) == {
        "NOT_STARTED", "VALID", "FAILED", "STALE", "BLOCKED_MANUAL", "EXCEPTION"
    }
    # The render axis is a separate object, not a value in either enum above.
    assert job["render_state"]["type"] == "object"


def test_t09_semantic_final_is_not_inferred_from_a_render_file(staged):
    layout, run_id, manifest, job_id, _ = staged
    (layout.job_dir(run_id, job_id) / "current" / "final_package.json").unlink()
    _write_render_report(layout, run_id, job_id, overall="OK")
    job = status_module.derive(layout, manifest)["jobs"][0]
    assert job["semantic_final_available"] is False, (
        "presence of a rendered file must never imply a semantic final"
    )
    assert job["render_state"]["overall"] == "FAILED", (
        "a receipt without its current semantic final cannot remain current"
    )


def test_t09_every_required_production_state_is_reachable(staged):
    import shutil

    layout, run_id, manifest, job_id, fixture_dir = staged
    seen = set()

    seen.add(status_module.derive(layout, manifest)["jobs"][0]["production_state"])

    failure_module.record(
        layout, run_id, job_id, operation="STAGE3",
        classification="BLOCKED_MANUAL", recommended_next_action="Manual restart.",
    )
    seen.add(status_module.derive(layout, manifest)["jobs"][0]["production_state"])
    failure_module.clear(layout, run_id, job_id, archive=False)

    # STALE: replacing the strategy invalidates everything downstream.
    strategy = read_json(fixture_dir / "strategy.valid.json")
    strategy["writer_guidance"] = "Endret."
    artifacts_module.submit(layout, run_id, job_id, stage=1, artifact="strategy",
                            payload=strategy, timestamp="20260823T080000Z")
    seen.add(status_module.derive(layout, manifest)["jobs"][0]["production_state"])

    # FAILED: an invalid artifact with nothing downstream of it, so the
    # staleness rule (which takes precedence) does not apply.
    current = layout.job_dir(run_id, job_id) / "current"
    for name in ("final_package.json", "review.json"):
        (current / name).unlink()
    broken = read_json(fixture_dir / "strategy.valid.json")
    broken["headline_hypothesis"] = ""
    atomic_write_json(current / "strategy.json", broken)
    seen.add(status_module.derive(layout, manifest)["jobs"][0]["production_state"])

    shutil.rmtree(current)
    current.mkdir()
    seen.add(status_module.derive(layout, manifest)["jobs"][0]["production_state"])

    assert {"VALID", "BLOCKED_MANUAL", "FAILED", "STALE", "NOT_STARTED"} <= seen, seen


# --------------------------------------------------------------------------
# T10 Static staleness (DEC-26)
# --------------------------------------------------------------------------

def test_t10_invalidation_table_is_exactly_the_frozen_one():
    """Two fixed tables, selected by the run's own manifest revision."""
    assert artifacts_module.STALE_SCOPE == {
        "strategy": ("final_package", "review", "render"),
        "final_package": ("review", "render"),
        "review": ("queue",),
        "document_date": ("render",),
    }
    assert artifacts_module.LEGACY_STALE_SCOPE == {
        "strategy": ("draft_package", "final_package", "review", "render"),
        "draft_package": ("final_package", "review", "render"),
        "final_package": ("review", "render"),
        "review": ("queue",),
        "document_date": ("render",),
    }
    assert artifacts_module.stale_scope_table("0.9.0") is artifacts_module.LEGACY_STALE_SCOPE
    assert artifacts_module.stale_scope_table("0.9.3") is artifacts_module.STALE_SCOPE
    assert artifacts_module.UPSTREAM_BINDING == {
        "final_package": ("strategy", "strategy_sha256"),
        "review": ("final_package", "final_package_sha256"),
    }
    assert artifacts_module.LEGACY_UPSTREAM_BINDING == {
        "draft_package": ("strategy", "strategy_sha256"),
        "final_package": ("draft_package", "draft_sha256"),
        "review": ("final_package", "final_package_sha256"),
    }


@pytest.mark.parametrize(
    "replaced,expected_stale",
    [("strategy", "final_package"), ("final_package", "review")],
)
def test_t10_replacing_an_artifact_marks_exactly_its_downstream(
    staged, replaced, expected_stale
):
    layout, run_id, manifest, job_id, fixture_dir = staged
    source = {
        "strategy": "strategy.valid.json",
        "final_package": "final_package.json",
    }[replaced]
    payload = read_json(fixture_dir / source)
    if replaced == "strategy":
        payload["writer_guidance"] = "Ny veiledning."
    else:
        payload["writer_note"] = "Ny notat."
    stage = {"strategy": 1, "final_package": 3}[replaced]
    artifacts_module.submit(layout, run_id, job_id, stage=stage, artifact=replaced,
                            payload=payload, timestamp="20260823T090000Z")

    stale, result = artifacts_module.evaluate_staleness(
        layout, run_id, job_id, spec_revision=manifest["spec_revision"]
    )
    assert expected_stale in stale, f"{replaced} replaced -> {expected_stale} stale"
    assert any(v.severity == "WARNING" for v in result.violations)


def test_t10_staleness_never_triggers_automatic_execution(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["writer_guidance"] = "Ny veiledning."
    artifacts_module.submit(layout, run_id, job_id, stage=1, artifact="strategy",
                            payload=payload, timestamp="20260823T091000Z")
    before = {
        p.name: p.read_bytes()
        for p in (layout.job_dir(run_id, job_id) / "current").iterdir()
    }
    status = status_module.derive(layout, manifest)
    after = {
        p.name: p.read_bytes()
        for p in (layout.job_dir(run_id, job_id) / "current").iterdir()
    }
    assert after == before, "deriving status must never regenerate an artifact"
    assert status["jobs"][0]["production_state"] == "STALE"


def test_t10_frozen_input_mismatch_is_not_normalized_to_stale(frozen):
    from jobbsok.manifest import FROZEN_DIR, verify_frozen

    layout, run_id, manifest = frozen
    target = layout.run_dir(run_id) / FROZEN_DIR / "policy" / "settings.toml"
    target.write_text(target.read_text(encoding="utf-8") + "\n# tampered\n",
                      encoding="utf-8")
    result = verify_frozen(layout, manifest)
    assert not result.ok
    observed = " ".join(v.observed for v in result.errors)
    assert "run-integrity failure" in observed
    assert "not staleness" in observed
    assert "child run" in observed


# --------------------------------------------------------------------------
# T11 Evidence namespace (DEC-34, ACC-08)
# --------------------------------------------------------------------------

def test_t11_fabricated_factual_id_fails(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    payload["used_evidence_refs"] = ["EV:WORK#900-oppdiktet-referanse"]
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok
    assert any(v.contract_id == "ACC-08" for v in result.errors)


def test_t11_baseline_reference_is_rejected_as_factual_support(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    payload["used_evidence_refs"] = ["BL:EMP_OUS_ANALYSE"]
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok, "a baseline ID must never count as factual evidence"


def test_t11_baseline_provenance_string_is_not_resolvable_as_evidence(staged):
    """The P0.7 authority_anchor values must stay inert."""
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    provenance = {
        e.get("baseline_provenance")
        for e in context.baseline_map["employments"]
    }
    assert "EMP-OUS-001" in provenance, "fixture assumption"
    payload = read_json(fixture_dir / "final_package.json")
    payload["used_evidence_refs"] = ["EMP-OUS-001"]
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok


def test_t11_valid_refs_resolve(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    for ref in payload["used_evidence_refs"]:
        assert ref in context.evidence_ids
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert result.ok, result.render()


def test_t11_tampered_index_fails_the_run_and_recommends_a_child_run(frozen):
    from jobbsok.manifest import FROZEN_DIR, verify_frozen

    layout, run_id, manifest = frozen
    index_path = (
        layout.run_dir(run_id) / FROZEN_DIR / "generated" / "evidence_index.json"
    )
    index = json.loads(index_path.read_text(encoding="utf-8"))
    index["entries"].append({
        "evidence_id": "EV:WORK#998-innsatt-referanse", "source_id": "WORK",
        "kind": "SECTION", "heading_path": ["falsk"], "line_start": 1,
        "line_end": 2, "content_sha256": "0" * 64,
    })
    index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")

    result = verify_frozen(layout, manifest)
    assert not result.ok
    assert any("evidence_index.json" in v.file for v in result.errors)
    assert any("child run" in v.observed for v in result.errors)


def test_t11_reference_resolution_is_documented_as_not_semantic_support(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    payload["used_evidence_refs"] = ["EV:WORK#900-finnes-ikke"]
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert any("never semantic support" in v.observed for v in result.errors)


# --------------------------------------------------------------------------
# T12 No byte-partition dependency (DEC-34)
# --------------------------------------------------------------------------

def test_t12_index_makes_no_partition_claim(layout):
    index = build_index(layout.authorities)
    assert index["partition_claim"] is False


def test_t12_preambles_are_indexed_without_a_partition(layout):
    """The real authorities each carry text before the first heading."""
    index = build_index(layout.authorities)
    preambles = [e for e in index["entries"] if e["kind"] == "PREAMBLE"]
    assert len(preambles) == 3, "all three authorities have a preamble"
    for entry in preambles:
        assert entry["line_start"] == 1 and entry["line_end"] > 1


def test_t12_file_root_entry_exists_for_every_authority(layout):
    index = build_index(layout.authorities)
    ids = evidence_ids(index)
    for source in ("WORK", "EDU", "OTHER"):
        assert f"EV:{source}#file" in ids


def test_t12_unusual_headings_and_preamble_still_index(layout, tmp_path):
    """A source with odd structure must still yield usable sections."""
    odd = layout.authorities / "Education.md"
    odd.write_text(
        "Fritekst uten overskrift, med æøå og en URL: https://example.org\n"
        "\n"
        "Mer preambel.\n"
        "\n"
        "# Utdanning\n\nInnhold.\n\n"
        "###### Dypt nivå seks\n\nInnhold.\n\n"
        "## 0. Runtime-kjerne\n\n"
        "```\n# ikke en overskrift, det er kode\n```\n\n"
        "## 0. Runtime-kjerne\n\nDuplisert overskriftstekst.\n",
        encoding="utf-8", newline="\n",
    )
    index = build_index(layout.authorities)
    edu = [e for e in index["entries"] if e["source_id"] == "EDU"]
    kinds = {e["kind"] for e in edu}
    assert kinds == {"FILE", "PREAMBLE", "SECTION"}
    ids = [e["evidence_id"] for e in edu]
    assert len(ids) == len(set(ids)), "duplicate headings must still get unique IDs"
    assert not any("ikke en overskrift" in " ".join(e["heading_path"]) for e in edu), (
        "a heading inside a fenced code block is not structure"
    )
    assert check_index(index, layout.authorities).ok


def test_t12_direct_source_access_remains_available(frozen):
    """Escape hatch: the whole authority file is always readable in the run."""
    from jobbsok.manifest import FROZEN_DIR

    layout, run_id, manifest = frozen
    for name in ("Work_experience.md", "Education.md", "Other_high_value_information.md"):
        path = layout.run_dir(run_id) / FROZEN_DIR / "authorities" / name
        assert path.is_file() and path.stat().st_size > 0


def test_t12_slug_folds_norwegian_deterministically():
    assert slugify("Nåværende rolle — forsvarlige ansvarsområder") == \
        "navaerende-rolle-forsvarlige-ansvarsomra"
    assert slugify("ÆØÅ æøå") == "aeoa-aeoa"
    assert slugify("###") == "section"
