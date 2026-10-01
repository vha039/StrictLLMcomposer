"""Tier-1 items 13-15: CV merge, leakage, personality."""

from __future__ import annotations

import json

import pytest

from jobbsok import leakage as leakage_module
from jobbsok import merge as merge_module
from jobbsok import validate as validate_module
from jobbsok.atomicio import read_json
from jobbsok.baseline import build_baseline_map, read_baseline
from jobbsok.errors import ValidationResult


@pytest.fixture
def baseline_map(layout):
    path = layout.authorities / "CV_BASELINE.md"
    return build_baseline_map(read_baseline(path), path)


# --------------------------------------------------------------------------
# T13 Dynamic CV merge (DEC-23, ACC-11) -- exact before/after arrays
# --------------------------------------------------------------------------

def test_t13_present_override_fully_replaces_the_baseline_bullets(baseline_map):
    before = merge_module.baseline_bullets(baseline_map)["EMP_OUS_ANALYSE"]
    assert len(before) == 3, "fixture assumption about the real baseline"

    package = {
        "cv": {
            "headline": "H", "profile": "P", "competencies": ["A"],
            "employment_overrides": [
                {"employment_id": "EMP_OUS_ANALYSE",
                 "bullets": ["Erstattet punkt én.", "Erstattet punkt to."]},
            ],
        }
    }
    effective = merge_module.effective_cv(baseline_map, package)
    after = merge_module.employment(effective, "EMP_OUS_ANALYSE")["bullets"]

    assert after == ["Erstattet punkt én.", "Erstattet punkt to."]
    assert len(after) == 2 and len(before) == 3
    for bullet in before:
        assert bullet not in after, "no baseline bullet may survive a full replacement"
    assert merge_module.employment(effective, "EMP_OUS_ANALYSE")["bullet_source"] \
        == "OVERRIDE"


def test_t13_absent_override_uses_the_baseline_default(baseline_map):
    package = {"cv": {"headline": "H", "profile": "P", "competencies": ["A"],
                      "employment_overrides": []}}
    effective = merge_module.effective_cv(baseline_map, package)
    for entry in effective["employments"]:
        assert entry["bullets"] == entry["default_bullets"]
        assert entry["bullet_source"] == "BASELINE_DEFAULT"


def test_t13_present_empty_replacement_renders_no_bullets(baseline_map):
    """Spec 12.2: an explicit empty replacement never falls back."""
    package = {
        "cv": {
            "headline": "H", "profile": "P", "competencies": ["A"],
            "employment_overrides": [
                {"employment_id": "EMP_TKS_HEIS", "bullets": []},
            ],
        }
    }
    effective = merge_module.effective_cv(baseline_map, package)
    entry = merge_module.employment(effective, "EMP_TKS_HEIS")
    assert entry["bullets"] == []
    assert entry["default_bullets"], "the baseline still has defaults"
    assert entry["bullet_source"] == "OVERRIDE", "it is an override, not a default"


def test_t13_empty_replacement_raises_a_warning_not_a_failure(staged):
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, job_id, fixture_dir = staged
    package = read_json(fixture_dir / "final_package.json")
    package["cv"]["employment_overrides"].append(
        {"employment_id": "EMP_AHLSELL", "bullets": []}
    )
    warnings = artifacts_module.soft_quality_warnings(
        package, {}, file_label="final_package.json"
    )
    assert warnings.ok, "an explicit empty replacement is legal"
    assert any("EMPTY replacement" in v.observed for v in warnings.warnings)


def test_t13_no_append_or_positional_merge_happens(baseline_map):
    package = {
        "cv": {
            "headline": "H", "profile": "P", "competencies": ["A"],
            "employment_overrides": [
                {"employment_id": "EMP_OUS_BAR", "bullets": ["Kun dette punktet."]},
            ],
        }
    }
    effective = merge_module.effective_cv(baseline_map, package)
    bullets = merge_module.employment(effective, "EMP_OUS_BAR")["bullets"]
    assert bullets == ["Kun dette punktet."], "no append, no positional mixture"


def test_t13_unknown_employment_id_is_rejected(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    package = read_json(fixture_dir / "final_package.json")
    package["cv"]["employment_overrides"].append(
        {"employment_id": "EMP_FINNES_IKKE", "bullets": ["Punkt."]}
    )
    result = validate_module.validate_package(
        package, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok
    assert any(v.contract_id == "ACC-11" for v in result.errors)
    assert any("may not add or remove employment identities" in v.observed
               for v in result.errors)


def test_t13_duplicate_override_for_one_employment_is_rejected(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    package = read_json(fixture_dir / "final_package.json")
    package["cv"]["employment_overrides"].append(
        {"employment_id": "EMP_OUS_ANALYSE", "bullets": ["Duplikat."]}
    )
    result = validate_module.validate_package(
        package, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok


def test_t13_static_chronology_is_preserved_and_ordered(baseline_map):
    package = {
        "cv": {
            "headline": "H", "profile": "P", "competencies": ["A"],
            "employment_overrides": [
                {"employment_id": "EMP_OUS_ANALYSE", "bullets": ["X."]}
            ],
        }
    }
    effective = merge_module.effective_cv(baseline_map, package)
    orders = [e["sort_order"] for e in effective["employments"]]
    assert orders == sorted(orders)
    original = {e["employment_id"]: e for e in baseline_map["employments"]}
    for entry in effective["employments"]:
        source = original[entry["employment_id"]]
        for field in ("employer", "formal_title", "period", "unit"):
            assert entry[field] == source[field], (
                f"{field} is baseline-owned and must survive the merge unchanged"
            )
    assert [e["education_id"] for e in effective["educations"]] == \
        [e["education_id"] for e in baseline_map["educations"]]


# --------------------------------------------------------------------------
# T14 Leakage, with false-positive fixtures
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    "text",
    [
        "Se EV:WORK#011-navaerende-rolle for detaljer.",
        "Basert på BL:EMP_OUS_ANALYSE.",
        "Jf. EMP_OUS_ANALYSE i baselinen.",
        "Intern rolle EMP-OUS-ANALYSE må ikke synes.",
        "Utdanningsnøkkel EDU-NTNU_ECON er privat.",
        "Fasett PF-07 er valgt.",
        "Kilde CLM-BAR-001 bekrefter dette.",
        "Fyll inn {{CV_PROFILE}} her.",
        "Se C:\\Users\\veggi\\runs\\r20260823-050000-fea486\\manifest.json",
        "Kontrollen CV_FUNCTIONAL_IDENTITY mangler.",
        "Kandidaten er INTP-A og scorer høyt på DISC.",
        "Profilen er tydelig MBTI-basert.",
    ],
)
def test_t14_private_material_fails(text):
    result = leakage_module.scan(text, file_label="f", location="l")
    assert not result.ok, f"should have been rejected: {text!r}"


@pytest.mark.parametrize("phrase", leakage_module.KNOWN_GOOD_PHRASES)
def test_t14_ordinary_phrases_pass(phrase):
    """Spec 10.3 / 14.2: stock phrases are semantic guidance, never failures."""
    result = leakage_module.scan(phrase, file_label="f", location="l")
    assert result.ok, f"false positive on {phrase!r}:\n{result.render()}"


def test_t14_brenner_for_passes_mechanical_validation_explicitly():
    result = leakage_module.scan(
        "Jeg brenner for arbeidet med beslutningsstøtte i helsesektoren.",
        file_label="f", location="l",
    )
    assert result.ok, (
        "Spec 10.3 names 'brenner for' as a semantic guidance issue that must "
        "not fail deterministic validation"
    )


def test_t14_realistic_norwegian_cv_text_has_no_false_positives(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    package = read_json(fixture_dir / "final_package.json")
    result = leakage_module.scan_package(package, file_label="final_package.json")
    assert result.ok, result.render()


def test_t14_leakage_is_scanned_only_in_employer_facing_fields(staged):
    """writer_note is private by design and never rendered."""
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    package = read_json(fixture_dir / "final_package.json")
    package["writer_note"] = "Brukte EV:WORK#004-0-2-ous-kjerne og fasett PF-01."
    result = validate_module.validate_package(
        package, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert result.ok, result.render()

    fields = dict(leakage_module.employer_facing_text(package))
    assert "writer_note" not in fields


def test_t14_leakage_in_a_cv_bullet_is_caught(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    package = read_json(fixture_dir / "final_package.json")
    package["cv"]["employment_overrides"][0]["bullets"][0] = (
        "Utviklet beslutningsstøtte, jf. EV:WORK#004-0-2-ous-kjerne."
    )
    result = validate_module.validate_package(
        package, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok
    assert any(v.contract_id == "DEC-27" for v in result.errors)


# --------------------------------------------------------------------------
# T15 Personality (DEC-35, ACC-09)
# --------------------------------------------------------------------------

def test_t15_zero_facets_is_valid(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["personality_facets"] = []
    result = validate_module.validate_strategy(payload, context, job_id)
    assert result.ok, f"zero facets is the valid null outcome:\n{result.render()}"


def test_t15_three_facets_pass_and_four_fail(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    template = payload["personality_facets"][0]

    payload["personality_facets"] = [
        {**template, "facet_id": fid} for fid in ("PF-01", "PF-02", "PF-12")
    ]
    assert validate_module.validate_strategy(payload, context, job_id).ok

    payload["personality_facets"].append({**template, "facet_id": "PF-03"})
    result = validate_module.validate_strategy(payload, context, job_id)
    assert not result.ok
    assert any("maxItems" in v.expected for v in result.errors)


def test_t15_facet_without_evidence_reference_fails(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["personality_facets"][0]["evidence_refs"] = []
    result = validate_module.validate_strategy(payload, context, job_id)
    assert not result.ok, "every selected facet must be evidence-bound"


def test_t15_facet_with_unresolvable_evidence_reference_fails(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["personality_facets"][0]["evidence_refs"] = ["EV:WORK#990-finnes-ikke"]
    result = validate_module.validate_strategy(payload, context, job_id)
    assert not result.ok


def test_t15_unknown_facet_id_fails(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["personality_facets"][0]["facet_id"] = "PF-99"
    result = validate_module.validate_strategy(payload, context, job_id)
    assert not result.ok
    assert any(v.contract_id == "DEC-35" for v in result.errors)


def test_t15_expression_ceiling_is_required_per_facet(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    del payload["personality_facets"][0]["expression_ceiling"]
    result = validate_module.validate_strategy(payload, context, job_id)
    assert not result.ok


def test_t15_personality_is_on_by_default_with_no_off_switch(layout):
    from jobbsok import settings as settings_module

    settings = settings_module.load(layout)
    assert settings["personality"]["max_selected_facets"] == 3
    assert "enabled" not in settings["personality"], (
        "DEC-35 forbids an OFF default; a dead toggle would be an "
        "optionality-only hook (Contract 21)"
    )
    profile = layout.context / "PERSONALITY_PROFILE.md"
    text = profile.read_text(encoding="utf-8")
    assert 'runtime_status: "ACTIVE"' in text
    assert 'default_toggle_state: "ON"' in text
    assert "states: [OFF, ON]" not in text


def test_t15_facet_index_is_the_closed_set(layout):
    facets = json.loads(
        (layout.policy / "personality_facets.json").read_text(encoding="utf-8")
    )
    ids = [f["facet_id"] for f in facets["facets"]]
    assert len(ids) == len(set(ids)) == 20
    assert facets["max_selected_facets"] == 3
    internal = [f["facet_id"] for f in facets["facets"]
                if not f["employer_expressible"]]
    assert internal, "risk/internal facets must be marked non-expressible"


def test_t15_stage3_receives_distilled_guidance_only(staged):
    """Contract 12.5: only the distilled selection, never the full profile.

    Under the P0.9.3 amendment the distilled packet is a Stage-3 input; the
    public Stage-3 context is therefore where it is asserted.
    """
    import subprocess
    import sys
    from pathlib import Path

    layout, run_id, manifest, job_id, _ = staged
    runtime = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "-c",
         f"import sys; sys.path.insert(0, r'{runtime}'); "
         "from jobbsok.cli import main; sys.exit(main())",
         "--root", str(layout.root), "context",
         "--run", run_id, "--job", job_id, "--stage", "3"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert completed.returncode == 0, completed.stderr
    bundle = json.loads(completed.stdout)

    assert "personality_distilled" in bundle
    assert bundle["personality_distilled"], "the selected facets are passed on"
    for facet in bundle["personality_distilled"]:
        assert set(facet) == {
            "plain_language_label", "expression_ceiling", "expression_guardrail",
            "vacancy_relevance", "intended_employer_interpretation",
            "misread_risk",
        }
        assert "facet_id" not in facet, "private facet codes are not handed over"
        assert "evidence_refs" not in facet, (
            "personality never becomes a second evidence authority"
        )
    assert any(f["intended_employer_interpretation"]
               for f in bundle["personality_distilled"]), (
        "the intended employer inference reaches the writer"
    )
    assert any(f["misread_risk"] for f in bundle["personality_distilled"]), (
        "the misread risk reaches the writer"
    )
    assert "personality_profile" not in bundle["read"], (
        "the full profile is not supplied to Stage 3"
    )
    # Stage 1, by contrast, does get the profile.
    completed1 = subprocess.run(
        [sys.executable, "-c",
         f"import sys; sys.path.insert(0, r'{runtime}'); "
         "from jobbsok.cli import main; sys.exit(main())",
         "--root", str(layout.root), "context",
         "--run", run_id, "--job", job_id, "--stage", "1"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert "personality_profile" in json.loads(completed1.stdout)["read"]


def test_t15_stage3_is_told_it_may_ignore_personality(staged):
    import subprocess
    import sys
    from pathlib import Path

    layout, run_id, manifest, job_id, _ = staged
    runtime = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "-c",
         f"import sys; sys.path.insert(0, r'{runtime}'); "
         "from jobbsok.cli import main; sys.exit(main())",
         "--root", str(layout.root), "context",
         "--run", run_id, "--job", job_id, "--stage", "3"],
        capture_output=True, text=True, encoding="utf-8",
    )
    bundle = json.loads(completed.stdout)
    assert "suppress" in bundle["personality_note"]
    assert "personality_profile" not in bundle["read"]
