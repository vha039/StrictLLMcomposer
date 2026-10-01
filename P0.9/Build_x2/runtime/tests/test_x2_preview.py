import json
from pathlib import Path

import pytest
from conftest import run_cli

from jobbsok import artifacts, preview, validate
from jobbsok.atomicio import read_json
from jobbsok.errors import JobError
from jobbsok.hashing import sha256_file
from jobbsok.pdf import ConversionResult


def _ready(fixtures):
    layout, run_id, manifest, fixture_dir = fixtures
    job_id = manifest["jobs"][0]["job_id"]
    submitted = artifacts.submit(layout, run_id, job_id, stage=1, artifact="strategy",
                                 payload=read_json(fixture_dir / "strategy.valid.json"),
                                 timestamp="20260823T060000Z")
    assert submitted.ok
    context = validate.RunContext(layout, manifest)
    handoff = artifacts.write_handoff(layout, artifacts.handoff_for(layout, context, job_id, 3))
    final = read_json(fixture_dir / "final_package.json")
    semantic = {key: value for key, value in final.items()
                if key not in artifacts.MECHANICAL_FIELDS["final_package"]}
    semantic_path = fixture_dir / "final_package.semantic.json"
    semantic_path.write_text(json.dumps(semantic, ensure_ascii=False), encoding="utf-8")
    return layout, context, job_id, handoff, semantic_path


def _hash_tree(root: Path):
    return {str(p.relative_to(root)): sha256_file(p) for p in root.rglob("*") if p.is_file()}


def test_preview_is_ephemeral_and_pdf_failure_keeps_semantic_metrics(fixtures, monkeypatch):
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    monkeypatch.setattr("jobbsok.pdf.convert", lambda *args, **kwargs: ConversionResult(False, diagnostics=["converter unavailable"]))
    before = (_hash_tree(layout.runs), _hash_tree(layout.generated))
    first = preview.run(layout, context, job_id=job_id, handoff=handoff, semantic_file=semantic,
                        preview_date="2026-09-23")
    second = preview.run(layout, context, job_id=job_id, handoff=handoff, semantic_file=semantic,
                         preview_date="2026-09-23")
    assert first["valid"]
    assert first["measurement_id"] == second["measurement_id"]
    assert first["page_counts"] == {"cv": "UNKNOWN", "letter": "UNKNOWN"}
    assert first["employment"] and first["semantic_sections"]
    assert before == (_hash_tree(layout.runs), _hash_tree(layout.generated))
    assert first["measurement_id"] != preview.run(layout, context, job_id=job_id,
        handoff=handoff, semantic_file=semantic, preview_date="2026-09-24")["measurement_id"]


def test_preview_refuses_tool_owned_fields_and_wrong_stage(fixtures):
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    bad = semantic.with_name("bad.semantic.json")
    payload = read_json(semantic)
    payload["binding"] = {}
    bad.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(JobError, match="tooling-owned"):
        preview.run(layout, context, job_id=job_id, handoff=handoff, semantic_file=bad)
    stage1 = artifacts.write_handoff(layout, artifacts.handoff_for(layout, context, job_id, 1))
    with pytest.raises(JobError):
        preview.run(layout, context, job_id=job_id, handoff=stage1, semantic_file=semantic)


def test_preview_invalid_fields_return_diagnostics_without_writes(fixtures):
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    payload = read_json(semantic)
    payload["cv"]["headline"] = ""
    semantic.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    before = (_hash_tree(layout.runs), _hash_tree(layout.generated))
    result = preview.run(layout, context, job_id=job_id, handoff=handoff,
                         semantic_file=semantic, preview_date="2026-09-23")
    assert not result["valid"]
    assert result["validation_errors"]
    assert before == (_hash_tree(layout.runs), _hash_tree(layout.generated))


def test_preview_rejects_altered_and_stale_handoffs(fixtures):
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    original = handoff.read_text(encoding="utf-8")
    handoff.write_text(original.replace('"FINAL_AND_REVIEW"', '"REVIEW_ONLY"'), encoding="utf-8")
    with pytest.raises(JobError, match="handoff"):
        preview.run(layout, context, job_id=job_id, handoff=handoff, semantic_file=semantic)
    handoff.write_text(original, encoding="utf-8")
    strategy = artifacts.load(layout, context.run_id, job_id, "strategy")
    strategy["headline_hypothesis"] = "Økonomirådgiver"
    changed = artifacts.submit(layout, context.run_id, job_id, stage=1, artifact="strategy",
                               payload=strategy, timestamp="20260823T070000Z")
    assert changed.ok
    with pytest.raises(JobError, match="handoff"):
        preview.run(layout, context, job_id=job_id, handoff=handoff, semantic_file=semantic)


def test_stage3_context_exposes_exact_preview_command(fixtures):
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    result = run_cli(layout, "context", "--run", context.run_id,
                     "--job", job_id, "--stage", "3")
    assert result.returncode == 0, result.stderr
    bundle = json.loads(result.stdout)
    command = bundle["preview"]["command"]
    assert command.startswith(".\\.venv\\Scripts\\jobbsok.exe preview ")
    assert f'--handoff "{bundle["handoff"]["path"]}"' in command
    assert f'--file "{bundle["write"]["return_paths"]["final_package"]}"' in command


def test_preview_bullet_sources_respect_full_replacement(frozen):
    layout, run_id, manifest = frozen
    context = validate.RunContext(layout, manifest)
    employment = context.baseline_map["employments"][0]
    key = employment["employment_id"]
    package = {"cv": {"headline": "Analytiker", "profile": "Profil", "competencies": [],
                      "employment_overrides": []},
               "letter": {"opening": "Åpning", "body_paragraphs": [], "closing": "Avslutning"}}
    baseline = next(r for r in preview._semantic_metrics(package, context.baseline_map)["employment"]
                    if r["employment_id"] == key)
    assert baseline["source"] == "baseline"
    assert baseline["bullet_count"] == len(employment["default_bullets"])
    package["cv"]["employment_overrides"] = [{"employment_id": key, "bullets": []}]
    empty = next(r for r in preview._semantic_metrics(package, context.baseline_map)["employment"]
                 if r["employment_id"] == key)
    assert empty["source"] == "override" and empty["bullet_count"] == 0
    package["cv"]["employment_overrides"][0]["bullets"] = ["Erstattet punkt"]
    replaced = next(r for r in preview._semantic_metrics(package, context.baseline_map)["employment"]
                    if r["employment_id"] == key)
    assert replaced["source"] == "override" and replaced["bullet_count"] == 1
    assert replaced["word_count"] == 2


def test_public_preview_returns_json_diagnostics_without_commit(fixtures):
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    payload = read_json(semantic)
    payload["cv"]["headline"] = ""
    semantic.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    before = (_hash_tree(layout.runs), _hash_tree(layout.generated))
    result = run_cli(layout, "preview", "--run", context.run_id, "--job", job_id,
                     "--handoff", str(handoff), "--file", str(semantic))
    assert result.returncode == 1, result.stderr
    parsed = json.loads(result.stdout)
    assert parsed["valid"] is False and parsed["validation_errors"]
    assert before == (_hash_tree(layout.runs), _hash_tree(layout.generated))


def test_public_valid_preview_stdout_is_json(fixtures, monkeypatch, capsys):
    from jobbsok.cli import main
    layout, context, job_id, handoff, semantic = _ready(fixtures)
    monkeypatch.setattr("jobbsok.pdf.convert", lambda *args, **kwargs: ConversionResult(False, diagnostics=["converter unavailable"]))
    exit_code = main(["--root", str(layout.root), "preview", "--run", context.run_id,
                      "--job", job_id, "--handoff", str(handoff), "--file", str(semantic)])
    output = capsys.readouterr()
    assert exit_code == 0, output.err
    parsed = json.loads(output.out)
    assert parsed["valid"] is True
    assert parsed["page_counts"]["cv"] == "UNKNOWN"
