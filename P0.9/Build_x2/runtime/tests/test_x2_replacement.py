import json

from conftest import run_cli
from jobbsok import artifacts
from jobbsok.atomicio import read_json
from jobbsok.validate import RunContext


def test_strategy_replacement_prints_fixed_impact_before_commit(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = RunContext(layout, manifest)
    handoff = artifacts.write_handoff(layout, artifacts.handoff_for(layout, context, job_id, 1))
    strategy = read_json(fixture_dir / "strategy.valid.json")
    semantic = {k: v for k, v in strategy.items() if k not in artifacts.MECHANICAL_FIELDS["strategy"]}
    semantic["headline_hypothesis"] = "Økonomi og analyse"
    path = fixture_dir / "replacement.semantic.json"
    path.write_text(json.dumps(semantic, ensure_ascii=False), encoding="utf-8")
    result = run_cli(layout, "stage-submit", "--run", run_id, "--job", job_id,
                     "--stage", "1", "--file", str(path), "--handoff", str(handoff))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "fixed stale scope): final_package, review, render" in result.stdout
    assert "Existing downstream artifacts becoming stale: final_package, review" in result.stdout
    assert result.stdout.index("Replacement impact") < result.stdout.index("[OK] wrote")
