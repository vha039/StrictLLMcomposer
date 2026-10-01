"""Tier-1 items 16-18: partial success, continuation, template preflight."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import BATCH_HEADER, BATCH_ROW, FIXED_MOMENT, run_cli
from jobbsok import artifacts as artifacts_module
from jobbsok import render as render_module
from jobbsok import status as status_module
from jobbsok.atomicio import atomic_write_json, read_json
from jobbsok.docxfill import (
    binding_report,
    control_inventory,
    read_document,
    require_template_contract,
)
from jobbsok.errors import ConfigurationError
from jobbsok.hashing import sha256_file
from jobbsok.manifest import freeze, load_manifest
from tools.make_fixtures import build as build_fixtures

RUNTIME = Path(__file__).resolve().parents[1]


def _two_job_run(layout, *, bad_first=False):
    """Freeze a run with two independent CORE jobs."""
    second_source = layout.inbox / "vacancies" / "annen_etat.md"
    second_source.write_text(
        (layout.inbox / "vacancies" / "testetaten_radgiver.md").read_text(
            encoding="utf-8"
        ),
        encoding="utf-8", newline="\n",
    )
    second = (
        "annen_etat_analytiker,Annen Etat,Analytiker,CORE,c1,2,NORMAL,"
        "vacancies/annen_etat.md,,,,\n"
    )
    csv = layout.inbox / "two.csv"
    rows = second + BATCH_ROW if bad_first else BATCH_ROW + second
    csv.write_text(BATCH_HEADER + rows, encoding="utf-8", newline="\n")
    result = freeze(layout, csv, reviewed_by="T", moment=FIXED_MOMENT)
    assert result.ok, result.result.render()
    return result.run_id, load_manifest(layout, result.run_id)


# --------------------------------------------------------------------------
# T16 Partial success and job-local containment (INV-05, Spec 15.4)
# --------------------------------------------------------------------------

def test_t16_one_poisoned_job_leaves_other_outputs_untouched(layout):
    run_id, manifest = _two_job_run(layout)
    fixtures = layout.root / "fixtures"
    build_fixtures(layout, run_id, fixtures)

    good_job = "testetaten_radgiver"
    bad_job = "annen_etat_analytiker"

    # The good job gets a complete, valid artifact set.
    for stage, artifact, filename in (
        (1, "strategy", "strategy.valid.json"),
        (2, "draft_package", "draft_package.json"),
        (3, "final_package", "final_package.json"),
        (3, "review", "review.json"),
    ):
        artifacts_module.submit(
            layout, run_id, good_job, stage=stage, artifact=artifact,
            payload=read_json(fixtures / filename), timestamp="20260823T100000Z",
        )
    good_hashes = {
        path.name: sha256_file(path)
        for path in sorted((layout.job_dir(run_id, good_job) / "current").iterdir())
    }

    # The bad job gets a deliberately broken strategy written straight to disk.
    poisoned = read_json(fixtures / "strategy.invalid.json")
    poisoned["binding"]["job_id"] = bad_job
    atomic_write_json(
        layout.job_dir(run_id, bad_job) / "current" / "strategy.json", poisoned
    )

    status = status_module.derive(layout, manifest)
    by_id = {job["job_id"]: job for job in status["jobs"]}
    assert by_id[bad_job]["production_state"] == "FAILED"
    assert by_id[good_job]["production_state"] == "VALID"
    assert by_id[good_job]["semantic_final_available"] is True

    after = {
        path.name: sha256_file(path)
        for path in sorted((layout.job_dir(run_id, good_job) / "current").iterdir())
    }
    assert after == good_hashes, "a failing job must not touch a valid job's outputs"


def test_t16_run_result_is_visibly_nonzero_while_valid_jobs_survive(layout):
    run_id, manifest = _two_job_run(layout)
    fixtures = layout.root / "fixtures"
    build_fixtures(layout, run_id, fixtures)
    poisoned = read_json(fixtures / "strategy.invalid.json")
    poisoned["binding"]["job_id"] = "annen_etat_analytiker"
    atomic_write_json(
        layout.job_dir(run_id, "annen_etat_analytiker") / "current" / "strategy.json",
        poisoned,
    )
    artifacts_module.submit(
        layout, run_id, "testetaten_radgiver", stage=1, artifact="strategy",
        payload=read_json(fixtures / "strategy.valid.json"),
        timestamp="20260823T100100Z",
    )

    completed = subprocess.run(
        [sys.executable, "-c",
         f"import sys; sys.path.insert(0, r'{RUNTIME}'); "
         "from jobbsok.cli import main; sys.exit(main())",
         "--root", str(layout.root), "validate", "--run", run_id],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert completed.returncode == 1, "partial failure is exit 1, not 0 and not 2"
    assert "[PASS] testetaten_radgiver/strategy.json" in completed.stdout
    assert "[FAIL] annen_etat_analytiker/strategy.json" in completed.stdout


def test_t16_targeted_validation_touches_only_the_named_job(layout):
    run_id, manifest = _two_job_run(layout)
    fixtures = layout.root / "fixtures"
    build_fixtures(layout, run_id, fixtures)
    artifacts_module.submit(
        layout, run_id, "testetaten_radgiver", stage=1, artifact="strategy",
        payload=read_json(fixtures / "strategy.valid.json"),
        timestamp="20260823T100200Z",
    )
    other_dir = layout.job_dir(run_id, "annen_etat_analytiker")
    before = sorted(p.name for p in other_dir.rglob("*"))

    completed = subprocess.run(
        [sys.executable, "-c",
         f"import sys; sys.path.insert(0, r'{RUNTIME}'); "
         "from jobbsok.cli import main; sys.exit(main())",
         "--root", str(layout.root), "validate", "--run", run_id,
         "--job", "testetaten_radgiver"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert "annen_etat_analytiker" not in completed.stdout
    assert sorted(p.name for p in other_dir.rglob("*")) == before


def test_t16_malformed_job_json_is_structured_and_other_job_survives(layout):
    from jobbsok import failure as failure_module

    run_id, manifest = _two_job_run(layout)
    fixtures = layout.root / "fixtures"
    build_fixtures(layout, run_id, fixtures)
    artifacts_module.submit(
        layout, run_id, "testetaten_radgiver", stage=1, artifact="strategy",
        payload=read_json(fixtures / "strategy.valid.json"),
        timestamp="20260823T100250Z",
    )
    broken = artifacts_module.artifact_path(
        layout, run_id, "annen_etat_analytiker", "strategy"
    )
    broken.write_text("{not json", encoding="utf-8")

    status = run_cli(layout, "status", "--run", run_id, "--json")
    assert status.returncode == 1
    assert "Traceback" not in status.stderr
    by_id = {job["job_id"]: job for job in json.loads(status.stdout)["jobs"]}
    assert by_id["annen_etat_analytiker"]["production_state"] == "FAILED"
    assert by_id["testetaten_radgiver"]["highest_valid_stage"] == "STRATEGY"

    validated = run_cli(layout, "validate", "--run", run_id)
    assert validated.returncode == 1
    assert "parseable job-local JSON" in validated.stdout
    assert "[PASS] testetaten_radgiver/strategy.json" in validated.stdout
    assert "Traceback" not in validated.stderr
    continued = run_cli(layout, "next", "--run", run_id)
    assert continued.returncode == 0
    assert "annen_etat_analytiker" in continued.stdout
    assert failure_module.load(
        layout, run_id, "annen_etat_analytiker"
    ) is None, "read-only diagnostics must not persist production failure"


def _complete_for_render(layout, manifest, job_id, fixtures):
    from jobbsok.validate import RunContext

    context = RunContext(layout, manifest)

    def semantic(filename, artifact):
        payload = read_json(fixtures / filename)
        for field in artifacts_module.MECHANICAL_FIELDS[artifact]:
            payload.pop(field, None)
        return payload

    state = artifacts_module.semantic_state(layout, context, job_id)
    strategy = artifacts_module.stamp_payload(
        context, job_id, "strategy", semantic("strategy.valid.json", "strategy"), state
    )
    artifacts_module.submit(
        layout, manifest["run_id"], job_id, stage=1, artifact="strategy",
        payload=strategy, timestamp="20260823T110000Z",
    )
    state = artifacts_module.semantic_state(layout, context, job_id)
    draft = artifacts_module.stamp_payload(
        context, job_id, "draft_package",
        semantic("draft_package.json", "draft_package"), state,
    )
    artifacts_module.submit(
        layout, manifest["run_id"], job_id, stage=2, artifact="draft_package",
        payload=draft, timestamp="20260823T110001Z",
    )
    state = artifacts_module.semantic_state(layout, context, job_id)
    final = artifacts_module.stamp_payload(
        context, job_id, "final_package",
        semantic("final_package.json", "final_package"), state,
    )
    review_state = artifacts_module.SemanticState(
        {**state.loaded, "final_package": final},
        state.valid | {"final_package"}, state.stale, state.invalid,
    )
    review = artifacts_module.stamp_payload(
        context, job_id, "review", semantic("review.json", "review"), review_state
    )
    artifacts_module.submit_stage3_pair(
        layout, manifest["run_id"], job_id,
        final_payload=final, review_payload=review, timestamp="20260823T110002Z",
    )
    final_path = artifacts_module.artifact_path(
        layout, manifest["run_id"], job_id, "final_package"
    )
    final = read_json(final_path)
    final["finalization"] = {
        "state": "FINALIZED", "document_date": "2026-08-23",
        "finalized_at": "2026-08-23T11:00:03Z", "finalized_by": "T",
    }
    atomic_write_json(final_path, final)


def test_t16_unmodelled_render_exception_is_job_local_and_preserves_prior_output(
    layout, monkeypatch, capsys
):
    from jobbsok import failure as failure_module
    from jobbsok.cli import main

    settings = layout.policy / "settings.toml"
    settings.write_text(
        settings.read_text(encoding="utf-8").replace(
            'converter = "word_com"', 'converter = "none"'
        ),
        encoding="utf-8", newline="\n",
    )
    run_id, manifest = _two_job_run(layout, bad_first=True)
    fixtures = layout.root / "fixtures"
    build_fixtures(layout, run_id, fixtures)
    for job_id in ("annen_etat_analytiker", "testetaten_radgiver"):
        _complete_for_render(layout, manifest, job_id, fixtures)

    initial = run_cli(layout, "render", "--run", run_id)
    assert initial.returncode == 0, initial.stderr + initial.stdout
    bad_out = layout.job_dir(run_id, "annen_etat_analytiker") / "out"
    prior_bad = {p.name: sha256_file(p) for p in bad_out.glob("*.docx")}
    assert len(prior_bad) == 2

    original = render_module._build_document

    def poisoned(*args, **kwargs):
        if kwargs["job"]["job_id"] == "annen_etat_analytiker":
            raise ValueError("synthetic unmodelled build fault")
        return original(*args, **kwargs)

    monkeypatch.setattr(render_module, "_build_document", poisoned)
    rc = main(["--root", str(layout.root), "render", "--run", run_id])
    output = capsys.readouterr()
    assert rc == 1
    assert "[FAILED] annen_etat_analytiker" in output.out
    assert "[DEGRADED] testetaten_radgiver" in output.out
    assert {p.name: sha256_file(p) for p in bad_out.glob("*.docx")} == prior_bad
    assert failure_module.load(layout, run_id, "annen_etat_analytiker") is None


def test_t16_run_global_frozen_failure_aborts_before_job_processing(layout):
    run_id, manifest = _two_job_run(layout)
    frozen_schema = (
        layout.run_dir(run_id) / "frozen" / "schemas" / "strategy.schema.json"
    )
    frozen_schema.write_text("{}", encoding="utf-8")
    completed = run_cli(layout, "validate", "--run", run_id)
    assert completed.returncode == 2
    assert "RUN-INTEGRITY ERROR" in completed.stderr
    assert "[PASS]" not in completed.stdout and "[FAIL]" not in completed.stdout


# --------------------------------------------------------------------------
# T17 Continuation (Contract 10.2)
# --------------------------------------------------------------------------

def test_t17_next_job_is_derived_from_current_disk_state(layout):
    run_id, manifest = _two_job_run(layout)
    fixtures = layout.root / "fixtures"
    build_fixtures(layout, run_id, fixtures)

    status = status_module.derive(layout, manifest)
    first = status_module.next_job(status, stage=1)
    assert first is not None and first["highest_valid_stage"] is None

    artifacts_module.submit(
        layout, run_id, first["job_id"], stage=1, artifact="strategy",
        payload=read_json(fixtures / "strategy.valid.json"),
        timestamp="20260823T100300Z",
    )
    status = status_module.derive(layout, manifest)
    second = status_module.next_job(status, stage=1)
    assert second is not None and second["job_id"] != first["job_id"], (
        "the finished job must no longer be offered for Stage 1"
    )
    ready_for_two = status_module.next_job(status, stage=2)
    assert ready_for_two["job_id"] == first["job_id"]


def test_t17_context_bundle_excludes_completed_job_history(staged):
    layout, run_id, manifest, job_id, _ = staged
    completed = subprocess.run(
        [sys.executable, "-c",
         f"import sys; sys.path.insert(0, r'{RUNTIME}'); "
         "from jobbsok.cli import main; sys.exit(main())",
         "--root", str(layout.root), "context",
         "--run", run_id, "--job", job_id, "--stage", "3"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert completed.returncode == 0, completed.stderr
    bundle = json.loads(completed.stdout)
    serialized = json.dumps(bundle)
    assert "history" not in serialized, (
        "a fresh chat needs current inputs only, never completed-job history"
    )
    assert set(bundle["write"]["allowed"]) == {"final_package", "review"}
    assert bundle["read"]["vacancy_original"]
    assert bundle["read"]["draft_package"]


def test_t17_continuation_needs_no_state_file_editing(staged):
    layout, run_id, manifest, job_id, _ = staged
    before = {
        path.relative_to(layout.root).as_posix(): sha256_file(path)
        for path in sorted(layout.run_dir(run_id).rglob("*")) if path.is_file()
    }
    for args in (
        ["status", "--run", run_id],
        ["next", "--run", run_id, "--stage", "3"],
        ["context", "--run", run_id, "--job", job_id, "--stage", "3"],
    ):
        subprocess.run(
            [sys.executable, "-c",
             f"import sys; sys.path.insert(0, r'{RUNTIME}'); "
             "from jobbsok.cli import main; sys.exit(main())",
             "--root", str(layout.root), *args],
            capture_output=True, text=True, encoding="utf-8",
        )
    after = {
        path.relative_to(layout.root).as_posix(): sha256_file(path)
        for path in sorted(layout.run_dir(run_id).rglob("*")) if path.is_file()
    }
    assert after == before, "reading status must never mutate the run"


# --------------------------------------------------------------------------
# T18 Template preflight (Spec 16.3)
# --------------------------------------------------------------------------

def test_t18_actual_masters_match_the_single_canonical_map(layout):
    template_map = json.loads(
        (layout.templates / "template_map.json").read_text(encoding="utf-8")
    )
    for name, spec in template_map["documents"].items():
        master = layout.root / spec["master"]
        expected = {tag: c["count"] for tag, c in spec["controls"].items()}
        require_template_contract(master, expected)
        assert dict(control_inventory(master)) == expected
    assert dict(control_inventory(layout.templates / "CV_MASTER.docx")).__len__() == 17
    letter = control_inventory(layout.templates / "APPLICATION_MASTER.docx")
    assert len(letter) == 6 and sum(letter.values()) == 7


def test_t18_masters_are_not_data_bound(layout):
    for name in ("CV_MASTER.docx", "APPLICATION_MASTER.docx"):
        report = binding_report(layout.templates / name)
        assert report["data_bindings"] == 0
        assert report["doc_part_obj"] == 0


def test_t18_an_unknown_control_fails_preflight(layout, tmp_path):
    from zipfile import ZIP_DEFLATED, ZipFile

    source = layout.templates / "CV_MASTER.docx"
    tampered = tmp_path / "tampered.docx"
    with ZipFile(source) as src:
        payload = {n: src.read(n) for n in src.namelist()}
        order = src.namelist()
    document = payload["word/document.xml"].decode("utf-8")
    document = document.replace('w:val="CV_PROFILE"', 'w:val="CV_UKJENT_KONTROLL"', 1)
    payload["word/document.xml"] = document.encode("utf-8")
    with ZipFile(tampered, "w", ZIP_DEFLATED) as out:
        for name in order:
            out.writestr(name, payload[name])

    template_map = json.loads(
        (layout.templates / "template_map.json").read_text(encoding="utf-8")
    )
    expected = {
        tag: c["count"]
        for tag, c in template_map["documents"]["cv"]["controls"].items()
    }
    with pytest.raises(ConfigurationError) as excinfo:
        require_template_contract(tampered, expected)
    assert "unknown controls" in str(excinfo.value)
    assert "CV_UKJENT_KONTROLL" in str(excinfo.value)


def test_t18_missing_master_fails_preflight(layout, tmp_path):
    with pytest.raises(ConfigurationError):
        require_template_contract(tmp_path / "nope.docx", {"X": 1})


def test_t18_static_baseline_conflict_fails_preflight(layout):
    """Spec 4.2: the master's static furniture must agree with the baseline."""
    from jobbsok.baseline import build_baseline_map, read_baseline

    path = layout.authorities / "CV_BASELINE.md"
    baseline_map = build_baseline_map(read_baseline(path), path)
    template_map = json.loads(
        (layout.templates / "template_map.json").read_text(encoding="utf-8")
    )
    effective = {
        "candidate": baseline_map["candidate"],
        "employments": [
            {**e, "bullets": e["default_bullets"]} for e in baseline_map["employments"]
        ],
        "educations": baseline_map["educations"],
    }
    assert render_module.preflight_templates(layout, template_map, effective).ok

    for entry in effective["employments"]:
        if entry["employment_id"] == "EMP_OUS_ANALYSE":
            entry["formal_title"] = "Seniorrådgiver med personalansvar"
    result = render_module.preflight_templates(layout, template_map, effective)
    assert not result.ok
    assert any(v.contract_id == "DEC-23" for v in result.errors)
    assert any("baseline-owned static fact" in v.observed for v in result.errors)


def test_t18_fill_then_unwrap_leaves_no_control_or_placeholder(layout, tmp_path):
    from jobbsok.docxfill import W, fill_block, visible_text, write_filled_docx

    template_map = json.loads(
        (layout.templates / "template_map.json").read_text(encoding="utf-8")
    )
    spec = template_map["documents"]["cv"]
    output = tmp_path / "filled.docx"

    def edit(root):
        for tag in spec["controls"]:
            fill_block(root, tag, [(0, f"Innhold for {tag.lower()} med æøå")])

    write_filled_docx(
        layout.templates / "CV_MASTER.docx", output, edit,
        title="t", subject="s", creator="Vegard Håland",
    )
    root, _ = read_document(output)
    assert not list(root.iter(f"{W}sdt")), "no w:sdt may survive the unwrap"
    text = visible_text(output)
    assert "{{" not in text and "}}" not in text
    assert "æøå" in text
