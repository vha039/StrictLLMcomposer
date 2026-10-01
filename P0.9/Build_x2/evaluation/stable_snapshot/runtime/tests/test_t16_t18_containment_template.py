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
        context, job_id, "final_package",
        semantic("final_package.json", "final_package"), state,
    )
    artifacts_module.submit(
        layout, manifest["run_id"], job_id, stage=3, artifact="final_package",
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
    assert bundle["read"]["strategy"]


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
    assert len(letter) == 6 and sum(letter.values()) == 6


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


# --------------------------------------------------------------------------
# Master typography and punctuation (ISS-01 to ISS-04, ISS-08)
#
# These carry the test_t16_ prefix because MASTER_VERIFICATION_AND_ACCEPTANCE
# section 2.4 names them that way; the registry in test_traceability.py maps by
# prefix, so item 16 stays satisfied and item 18 keeps its own tests.
# --------------------------------------------------------------------------

def _document_and_styles(master):
    from zipfile import ZipFile
    import xml.etree.ElementTree as ET

    with ZipFile(master) as archive:
        return (
            ET.fromstring(archive.read("word/document.xml")),
            ET.fromstring(archive.read("word/styles.xml")),
        )


def _control_paragraph(root, tag, ordinal):
    """The ordinal-th paragraph inside the single control carrying `tag`."""
    from jobbsok.docxfill import W

    matches = [
        sdt for sdt in root.iter(f"{W}sdt")
        if (sdt.find(f"{W}sdtPr/{W}tag") is not None
            and sdt.find(f"{W}sdtPr/{W}tag").get(f"{W}val") == tag)
    ]
    assert len(matches) == 1, f"expected exactly one {tag}, found {len(matches)}"
    paragraphs = list(matches[0].iter(f"{W}p"))
    assert len(paragraphs) > ordinal, f"{tag} holds {len(paragraphs)} paragraph(s)"
    return paragraphs[ordinal]


def test_t16_master_typography_uses_the_discrete_scale(layout):
    """The readability floor is a contract, not a coincidence (ISS-01/02/03).

    Two assertions, because the two masters carry size through two different
    mechanisms: every CV paragraph has an inline w:sz, while the letter body and
    signature have none and inherit styles.xml. Changing only one would be
    silently inert for the other.
    """
    from jobbsok.docxfill import W

    scale = {16, 20, 24, 28, 48}  # 8, 10, 12, 14 and 24 pt in half-points

    # (a) inline sizes in the body of both masters
    for name in ("CV_MASTER.docx", "APPLICATION_MASTER.docx"):
        document, _ = _document_and_styles(layout.templates / name)
        sizes = {
            size.get(f"{W}val") for size in document.iter(f"{W}sz")
        }
        assert sizes, f"{name} carries no inline w:sz at all"
        off_scale = {value for value in sizes if int(value) not in scale}
        assert not off_scale, f"{name} inline w:sz off the scale: {sorted(off_scale)}"
        assert not list(document.iter(f"{W}szCs")), (
            f"{name} must not introduce w:szCs; both masters had zero"
        )

    # (b) every APPLIED styles.xml style, including the retained exception
    expected = {
        "CV_MASTER.docx": {"Normal": "24", "ListBullet": "24", "Heading1": "28"},
        # The letter's subject line keeps Title at 40 half-points (20 pt). It is
        # asserted here as a deliberate, named exception rather than ignored.
        "APPLICATION_MASTER.docx": {"Normal": "24", "Title": "40"},
    }
    for name, wanted in expected.items():
        document, styles = _document_and_styles(layout.templates / name)
        applied = {node.get(f"{W}val") for node in document.iter(f"{W}pStyle")}
        applied.add("Normal")  # the default paragraph style is always applied
        assert applied == set(wanted), (
            f"{name} applies {sorted(applied)}; the contract covers {sorted(wanted)}"
        )
        for style_id, value in wanted.items():
            matches = [
                style for style in styles.findall(f"{W}style")
                if style.get(f"{W}styleId") == style_id
            ]
            assert len(matches) == 1, f"{name}: {style_id} appears {len(matches)} times"
            size = matches[0].find(f"{W}rPr/{W}sz")
            assert size is not None, f"{name}: {style_id} carries no w:sz"
            assert size.get(f"{W}val") == value, (
                f"{name}: {style_id} is {size.get(f'{W}val')}, expected {value}"
            )


def test_t16_subordinate_zones_are_not_title_formatted(layout):
    """ISS-04: two content zones inherited record-title run properties.

    The record lines themselves -- employer, unit, education, period -- are
    correct design and keep their bold and colour. Only these two content zones
    lose them.
    """
    from jobbsok.docxfill import W

    document, _ = _document_and_styles(layout.templates / "CV_MASTER.docx")
    for tag, ordinal in (
        ("CV_RELEVANT_BACHELOR_SUBJECTS", 0),
        ("CV_OPTIONAL_PREVIOUS_EXPERIENCE", 1),
    ):
        paragraph = _control_paragraph(document, tag, ordinal)
        runs = list(paragraph.iter(f"{W}r"))
        assert runs, f"{tag} content paragraph has no run to check"
        for run in runs:
            properties = run.find(f"{W}rPr")
            if properties is None:
                continue
            assert properties.find(f"{W}b") is None, f"{tag} still carries w:b"
            assert properties.find(f"{W}color") is None, (
                f"{tag} still carries a w:color override"
            )


def test_t16_masters_and_baseline_contain_no_en_or_em_dash(layout):
    """ISS-08: the deterministic sources of employer-facing dashes.

    baseline_provenance is excluded on purpose: it is inert, never rendered,
    and two of its values are verbatim cross-references into Work_experience.md.
    """
    from jobbsok.baseline import build_baseline_map, read_baseline
    from jobbsok.docxfill import W

    for name in ("CV_MASTER.docx", "APPLICATION_MASTER.docx"):
        document, _ = _document_and_styles(layout.templates / name)
        text = "".join(node.text or "" for node in document.iter(f"{W}t"))
        assert text, f"{name} yielded no visible text to check"
        assert "–" not in text, f"{name} still contains an en dash"
        assert "—" not in text, f"{name} still contains an em dash"

    path = layout.authorities / "CV_BASELINE.md"
    baseline_map = build_baseline_map(read_baseline(path), path)
    offenders = []

    def walk(value, where):
        if isinstance(value, dict):
            for key, item in value.items():
                walk(item, f"{where}/{key}")
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, f"{where}[{index}]")
        elif isinstance(value, str) and ("–" in value or "—" in value):
            if not where.endswith("baseline_provenance"):
                offenders.append((where, value))

    walk(baseline_map, "")
    assert not offenders, offenders


def test_t18_cleared_control_in_a_table_cell_leaves_a_valid_cell(layout, tmp_path):
    """A vacancy with no reference must still produce a letter Word will open.

    APP_REFERENCE_OPTIONAL is the sole content of one cell in the letter's
    address table. Clearing it empties the control, and unwrapping then leaves a
    w:tc holding only w:tcPr -- which ECMA-376 forbids and Word rejects with
    "The file appears to be corrupted", while ElementTree parses it happily.

    Both real pilot vacancies carry no reference, so this is the ordinary case,
    not an edge case. The existing fixtures all set one, which is why the suite
    was green while every no-reference letter was unopenable.
    """
    from jobbsok.docxfill import (
        W, fill_block, fill_inline, visible_text, write_filled_docx,
    )

    template_map = json.loads(
        (layout.templates / "template_map.json").read_text(encoding="utf-8")
    )
    spec = template_map["documents"]["letter"]
    output = tmp_path / "no_reference.docx"

    def edit(root):
        for tag, control in spec["controls"].items():
            if tag == "APP_REFERENCE_OPTIONAL":
                fill_block(root, tag, [])  # the vacancy has no reference
            elif control["kind"] == "inline":
                fill_inline(root, tag, f"Innhold {tag.lower()}")
            else:
                fill_block(root, tag, [(0, f"Innhold {tag.lower()} med æøå")])

    write_filled_docx(
        layout.templates / "APPLICATION_MASTER.docx", output, edit,
        title="t", subject="s", creator="Vegard Håland",
    )

    root, _ = read_document(output)
    cells = list(root.iter(f"{W}tc"))
    assert cells, "the letter master's address table must survive the fill"
    for cell in cells:
        blocks = [child for child in cell if child.tag in (f"{W}p", f"{W}tbl")]
        assert blocks, (
            "a table cell was left with no block-level child: "
            f"{[child.tag.rsplit('}', 1)[-1] for child in cell]}"
        )
    assert "Innhold app_reference_optional" not in visible_text(output), (
        "the cleared control must still render as absent, not as filler text"
    )


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
