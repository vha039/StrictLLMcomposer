"""Tier-1 items 5-8: stage ownership, approved set/baseline, schema, failure."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from conftest import (
    BATCH_HEADER,
    BATCH_ROW,
    FIXED_MOMENT,
    make_fixtures,
    run_cli,
    set_role_mapping,
)
from jobbsok import artifacts as artifacts_module
from jobbsok import failure as failure_module
from jobbsok import status as status_module
from jobbsok import validate as validate_module
from jobbsok.atomicio import atomic_write_json, read_json
from jobbsok.errors import ValidationResult
from jobbsok.hashing import sha256_file
from jobbsok.manifest import freeze, load_manifest
from jobbsok import paths as paths_module
from jobbsok.paths import STAGE_WRITE_MAP


# --------------------------------------------------------------------------
# T05 Stage-scoped write ownership (INV-09)
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    "stage,artifact",
    [
        (3, "strategy"),        # Stage 3 may not touch the strategy
        (3, "draft_package"),   # nor the retired draft
        (1, "draft_package"),   # Stage 1 may not skip ahead
        (1, "final_package"),
        (1, "review"),
        (2, "draft_package"),   # Stage 2 is retired: it owns nothing now
    ],
)
def test_t05_upstream_mutation_by_a_downstream_stage_fails(stage, artifact):
    result = artifacts_module.check_stage_ownership(stage, artifact)
    assert not result.ok
    violation = result.errors[0]
    assert violation.contract_id == "INV-09"
    assert "owning standard stage" in violation.observed


@pytest.mark.parametrize(
    "stage,artifact",
    [(1, "strategy"), (3, "final_package"), (3, "review")],
)
def test_t05_owning_stage_may_write_its_own_artifact(stage, artifact):
    assert artifacts_module.check_stage_ownership(stage, artifact).ok


def test_t05_write_map_is_exactly_the_frozen_ownership():
    """INV-09 under the P0.9.3 amendment: Stage 2 is retired."""
    assert STAGE_WRITE_MAP == {
        1: ("strategy",),
        3: ("final_package", "review"),
    }
    # The retired draft keeps a read-only owner so historical bindings and
    # hash lookups still resolve, and no active stage may write it.
    assert paths_module.RETIRED_STAGE_OWNERSHIP == {"draft_package": 2}
    assert paths_module.owning_stage("draft_package") == 2
    assert not paths_module.stage_owns(2, "draft_package")


def test_t05_owning_stage_replacement_archives_the_previous_version(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["writer_guidance"] = "Revidert veiledning."
    result = artifacts_module.submit(
        layout, run_id, job_id, stage=1, artifact="strategy",
        payload=payload, timestamp="20260823T070000Z",
    )
    assert result.ok
    assert result.superseded is not None and result.superseded.is_file()
    history = layout.job_dir(run_id, job_id) / "history"
    assert list(history.glob("*strategy.json")), "the superseded copy goes to history"


def test_t05_replacing_the_strategy_produces_the_fixed_stale_scope(staged):
    """DEC-26 under the amendment: strategy replaced -> final, review, render."""
    layout, run_id, manifest, job_id, fixture_dir = staged
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["writer_guidance"] = "Helt ny veiledning."
    artifacts_module.submit(
        layout, run_id, job_id, stage=1, artifact="strategy",
        payload=payload, timestamp="20260823T070100Z",
    )
    stale, _ = artifacts_module.evaluate_staleness(
        layout, run_id, job_id, spec_revision=manifest["spec_revision"]
    )
    assert "final_package" in stale
    assert artifacts_module.STALE_SCOPE["strategy"] == (
        "final_package", "review", "render"
    )
    # The legacy table is preserved unchanged for historical runs.
    assert artifacts_module.LEGACY_STALE_SCOPE["strategy"] == (
        "draft_package", "final_package", "review", "render"
    )


def _public_context(layout, run_id, job_id, stage):
    completed = run_cli(
        layout, "context", "--run", run_id, "--job", job_id,
        "--stage", str(stage),
    )
    assert completed.returncode == 0, completed.stderr + completed.stdout
    return json.loads(completed.stdout)


def _assert_context_write_contract(layout, run_id, job_id, bundle):
    allowed = set(bundle["write"]["allowed"])
    schema_paths = bundle["write"]["schema_paths"]
    return_paths = bundle["write"]["return_paths"]
    assert set(schema_paths) == allowed
    assert set(return_paths) == allowed

    frozen_schemas = (layout.run_dir(run_id) / "frozen" / "schemas").resolve()
    returns_root = (
        layout.generated / "returns" / run_id / job_id
    ).resolve(strict=False)
    command = bundle["submission"]["command"]
    assert f'--handoff "{bundle["handoff"]["path"]}"' in command
    assert "<" not in command and ">" not in command

    resolved_returns = {}
    for artifact in allowed:
        schema_path = Path(schema_paths[artifact])
        assert schema_path.is_absolute() and schema_path.is_file()
        assert schema_path.resolve().is_relative_to(frozen_schemas)
        assert schema_path.name == (
            f"{artifacts_module.ARTIFACTS[artifact][1]}.schema.json"
        )

        return_path = Path(return_paths[artifact])
        assert return_path.is_absolute()
        assert return_path.resolve(strict=False).is_relative_to(returns_root)
        assert return_path.parent.name == Path(bundle["handoff"]["path"]).stem
        assert return_path.parent.is_dir()
        assert not return_path.exists()
        assert not artifacts_module.artifact_path(
            layout, run_id, job_id, artifact
        ).exists()
        assert f'"{return_path}"' in command
        resolved_returns[artifact] = return_path
    return resolved_returns


def _public_status(layout, run_id):
    completed = run_cli(layout, "status", "--run", run_id, "--json")
    assert completed.returncode == 0, completed.stderr + completed.stdout
    return json.loads(completed.stdout)


def _semantic_return(layout, fixture_dir, filename, artifact, suffix):
    payload = read_json(fixture_dir / filename)
    for field in artifacts_module.MECHANICAL_FIELDS[artifact]:
        payload.pop(field, None)
    path = layout.root / "returns" / f"{suffix}.json"
    atomic_write_json(path, payload)
    return path, payload


def _submit(layout, run_id, job_id, stage, handoff, file, review_file=None):
    args = [
        "stage-submit", "--run", run_id, "--job", job_id,
        "--stage", str(stage), "--handoff", handoff, "--file", str(file),
    ]
    if review_file is not None:
        args += ["--review-file", str(review_file)]
    return run_cli(layout, *args)


def test_t05_public_handoff_completes_all_stages_and_review_only(layout):
    set_role_mapping(layout, sol="synthetic-sol", terra="synthetic-terra")
    result = freeze(
        layout, layout.inbox / "batch_input.csv",
        reviewed_by="Test Reviewer", moment=FIXED_MOMENT,
    )
    assert result.ok, result.result.render()
    run_id, manifest = result.run_id, load_manifest(layout, result.run_id)
    job_id = manifest["jobs"][0]["job_id"]
    fixture_dir = make_fixtures(layout, run_id)

    stage1 = _public_context(layout, run_id, job_id, 1)
    assert stage1["handoff"]["mode"] == "STRATEGY"
    _assert_context_write_contract(layout, run_id, job_id, stage1)
    assert "binding" not in stage1["write"]["semantic_fields"]["strategy"]
    assert stage1["configured_model"] == "synthetic-sol"
    strategy_file, _ = _semantic_return(
        layout, fixture_dir, "strategy.valid.json", "strategy", "strategy"
    )
    submitted = _submit(
        layout, run_id, job_id, 1, stage1["handoff"]["path"], strategy_file
    )
    assert submitted.returncode == 0, submitted.stderr + submitted.stdout
    assert _public_status(layout, run_id)["jobs"][0]["highest_valid_stage"] == "STRATEGY"

    # next --stage 3 now selects the job on a current strategy, with no draft.
    queued = run_cli(layout, "next", "--run", run_id, "--stage", "3")
    assert queued.returncode == 0 and job_id in queued.stdout

    stage3 = _public_context(layout, run_id, job_id, 3)
    assert stage3["handoff"]["mode"] == "FINAL_AND_REVIEW"
    assert "draft_package" not in stage3["read"]
    assert (
        stage3["handoff"]["upstream"]["strategy_sha256"]
        == artifacts_module.artifact_hash(
            artifacts_module.load(layout, run_id, job_id, "strategy")
        )
    )
    stage3_returns = _assert_context_write_contract(
        layout, run_id, job_id, stage3
    )
    final_file, _ = _semantic_return(
        layout, fixture_dir, "final_package.json", "final_package", "final"
    )
    review_file, _ = _semantic_return(
        layout, fixture_dir, "review.json", "review", "review"
    )
    submitted = _submit(
        layout, run_id, job_id, 3, stage3["handoff"]["path"],
        final_file, review_file,
    )
    assert submitted.returncode == 0, submitted.stderr + submitted.stdout
    validated = run_cli(layout, "validate", "--run", run_id, "--job", job_id)
    assert validated.returncode == 0, validated.stderr + validated.stdout
    complete = _public_status(layout, run_id)["jobs"][0]
    assert complete["highest_valid_stage"] == "FINAL"
    assert complete["semantic_triage"] == "CHECK"
    assert "Utlysningen nevner prognosearbeid" in complete["recommended_action"]
    assert "Ingen dokumentert erfaring med prognosemodeller" in \
        complete["recommended_action"]

    final_path = artifacts_module.artifact_path(
        layout, run_id, job_id, "final_package"
    )
    review_path = artifacts_module.artifact_path(layout, run_id, job_id, "review")
    final_before = sha256_file(final_path)
    review_path.unlink()
    next_stage3 = run_cli(
        layout, "next", "--run", run_id, "--stage", "3"
    )
    assert next_stage3.returncode == 0 and job_id in next_stage3.stdout
    recovery = _public_context(layout, run_id, job_id, 3)
    assert recovery["handoff"]["mode"] == "REVIEW_ONLY"
    recovery_returns = _assert_context_write_contract(
        layout, run_id, job_id, recovery
    )
    assert recovery_returns["review"] != stage3_returns["review"]
    recovered = _submit(
        layout, run_id, job_id, 3, recovery["handoff"]["path"], review_file
    )
    assert recovered.returncode == 0, recovered.stderr + recovered.stdout
    assert sha256_file(final_path) == final_before


def test_t05_context_exposes_configured_capability_surface(layout):
    set_role_mapping(
        layout, sol="synthetic-sol-surface", terra="synthetic-terra-surface"
    )
    frozen = freeze(
        layout, layout.inbox / "batch_input.csv",
        reviewed_by="T", moment=FIXED_MOMENT,
    )
    assert frozen.ok, frozen.result.render()
    job_id = frozen.manifest["jobs"][0]["job_id"]

    context = _public_context(layout, frozen.run_id, job_id, 1)

    assert context["capability_role"] == "SOL_CLASS"
    assert context["configured_model"] == "synthetic-sol-surface"


def test_t05_stale_handoff_and_stale_actions_refuse_before_mutation(staged):
    from jobbsok import failure as failure_module

    layout, run_id, manifest, job_id, fixture_dir = staged
    stale_stage3 = _public_context(layout, run_id, job_id, 3)

    stage1 = _public_context(layout, run_id, job_id, 1)
    strategy_file, strategy = _semantic_return(
        layout, fixture_dir, "strategy.valid.json", "strategy", "strategy-new"
    )
    strategy["writer_guidance"] = "Ny, gyldig veiledning."
    atomic_write_json(strategy_file, strategy)
    replaced = _submit(
        layout, run_id, job_id, 1, stage1["handoff"]["path"], strategy_file
    )
    assert replaced.returncode == 0, replaced.stderr + replaced.stdout

    final_path = artifacts_module.artifact_path(layout, run_id, job_id, "final_package")
    history = layout.job_dir(run_id, job_id) / "history"
    before = sha256_file(final_path)
    history_before = sorted(p.name for p in history.glob("*final_package.json"))
    final_file, _ = _semantic_return(
        layout, fixture_dir, "final_package.json", "final_package", "stale-final"
    )
    review_file, _ = _semantic_return(
        layout, fixture_dir, "review.json", "review", "stale-review"
    )
    refused = _submit(
        layout, run_id, job_id, 3, stale_stage3["handoff"]["path"],
        final_file, review_file,
    )
    assert refused.returncode == 1
    assert "handoff is stale" in refused.stderr
    assert sha256_file(final_path) == before
    assert sorted(p.name for p in history.glob("*final_package.json")) == history_before
    assert failure_module.load(layout, run_id, job_id) is None

    # A replaced strategy stales the final and review, so Stage-3 context is
    # offered again as FINAL_AND_REVIEW; what must never work is the stale
    # handoff above. Production actions on the stale pair stay refused.
    reoffered = run_cli(
        layout, "context", "--run", run_id, "--job", job_id, "--stage", "3"
    )
    assert reoffered.returncode == 0, reoffered.stderr
    assert json.loads(reoffered.stdout)["handoff"]["mode"] == "FINAL_AND_REVIEW"
    assert run_cli(
        layout, "finalize", "--run", run_id, "--job", job_id
    ).returncode == 1
    assert run_cli(
        layout, "render", "--run", run_id, "--job", job_id
    ).returncode == 1
    continuation = run_cli(
        layout, "next", "--run", run_id, "--stage", "3"
    )
    assert continuation.returncode == 0 and job_id in continuation.stdout


def test_t05_model_provided_mechanical_fields_are_refused(frozen):
    layout, run_id, manifest = frozen
    job_id = manifest["jobs"][0]["job_id"]
    fixture_dir = make_fixtures(layout, run_id)
    context = _public_context(layout, run_id, job_id, 1)
    full_payload = fixture_dir / "strategy.valid.json"
    refused = _submit(
        layout, run_id, job_id, 1, context["handoff"]["path"], full_payload
    )
    assert refused.returncode == 1
    assert "tooling-owned fields" in refused.stderr
    assert not artifacts_module.artifact_path(
        layout, run_id, job_id, "strategy"
    ).exists()


def test_t05_invalid_stage3_half_never_displaces_current_pair(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = _public_context(layout, run_id, job_id, 3)
    final_path = artifacts_module.artifact_path(
        layout, run_id, job_id, "final_package"
    )
    review_path = artifacts_module.artifact_path(layout, run_id, job_id, "review")
    before = (sha256_file(final_path), sha256_file(review_path))
    history = layout.job_dir(run_id, job_id) / "history"
    history_before = sorted(p.name for p in history.glob("*"))

    final_file, final_semantic = _semantic_return(
        layout, fixture_dir, "final_package.json", "final_package", "pair-final"
    )
    review_file, review_semantic = _semantic_return(
        layout, fixture_dir, "review.json", "review", "pair-review"
    )
    review_semantic["triage"] = "INVALID"
    atomic_write_json(review_file, review_semantic)
    first = _submit(
        layout, run_id, job_id, 3, context["handoff"]["path"],
        final_file, review_file,
    )
    assert first.returncode == 1

    review_semantic["triage"] = "CHECK"
    atomic_write_json(review_file, review_semantic)
    final_semantic["used_evidence_refs"] = []
    atomic_write_json(final_file, final_semantic)
    second = _submit(
        layout, run_id, job_id, 3, context["handoff"]["path"],
        final_file, review_file,
    )
    assert second.returncode == 1
    assert (sha256_file(final_path), sha256_file(review_path)) == before
    assert sorted(p.name for p in history.glob("*")) == history_before


def test_t05_failed_stage_return_is_recorded_and_success_clears_it(frozen):
    from jobbsok import failure as failure_module

    layout, run_id, manifest = frozen
    job_id = manifest["jobs"][0]["job_id"]
    fixture_dir = make_fixtures(layout, run_id)
    context = _public_context(layout, run_id, job_id, 1)
    invalid, _ = _semantic_return(
        layout, fixture_dir, "strategy.invalid.json", "strategy", "invalid-strategy"
    )
    first = _submit(
        layout, run_id, job_id, 1, context["handoff"]["path"], invalid
    )
    assert first.returncode == 1
    failure = failure_module.load(layout, run_id, job_id)
    assert failure["classification"] == "FAILED"
    assert failure["mechanical_corrections_used"] == 0
    assert failure["attempts_used"] == 0
    assert "same session" in failure["recommended_next_action"]
    assert "Recovery:" in first.stdout
    assert "classification         : FAILED" in first.stdout
    assert "mechanical corrections : 0" in first.stdout
    assert "semantic attempts      : 0" in first.stdout
    assert failure["recommended_next_action"] in first.stdout

    valid, _ = _semantic_return(
        layout, fixture_dir, "strategy.valid.json", "strategy", "corrected-strategy"
    )
    corrected = _submit(
        layout, run_id, job_id, 1, context["handoff"]["path"], valid
    )
    assert corrected.returncode == 0, corrected.stderr + corrected.stdout
    assert failure_module.load(layout, run_id, job_id) is None


def test_t05_mechanical_correction_and_semantic_retry_are_separate(staged):
    from jobbsok import failure as failure_module

    layout, run_id, manifest, job_id, fixture_dir = staged
    context = _public_context(layout, run_id, job_id, 3)
    final_file, _ = _semantic_return(
        layout, fixture_dir, "final_package.json", "final_package", "retry-final"
    )
    review_file, review = _semantic_return(
        layout, fixture_dir, "review.json", "review", "retry-review"
    )
    review["triage"] = "INVALID"
    atomic_write_json(review_file, review)

    for _ in range(2):
        refused = _submit(
            layout, run_id, job_id, 3, context["handoff"]["path"],
            final_file, review_file,
        )
        assert refused.returncode == 1
    pending_retry = failure_module.load(layout, run_id, job_id)
    assert pending_retry["classification"] == "FAILED"
    assert pending_retry["mechanical_corrections_used"] == 1
    assert pending_retry["attempts_used"] == 0
    assert pending_retry["retry_position"] == 0
    assert "classification         : FAILED" in refused.stdout
    assert "mechanical corrections : 1" in refused.stdout
    assert "semantic attempts      : 0" in refused.stdout
    assert pending_retry["recommended_next_action"] in refused.stdout

    retry_context = _public_context(layout, run_id, job_id, 3)
    assert retry_context["handoff"]["semantic_retry_attempt"] == 1
    for _ in range(2):
        refused = _submit(
            layout, run_id, job_id, 3, retry_context["handoff"]["path"],
            final_file, review_file,
        )
        assert refused.returncode == 1
    blocked = failure_module.load(layout, run_id, job_id)
    assert blocked["classification"] == "BLOCKED_MANUAL"
    assert blocked["mechanical_corrections_used"] == 1
    assert blocked["attempts_used"] == 1
    assert "classification         : BLOCKED_MANUAL" in refused.stdout
    assert "mechanical corrections : 1" in refused.stdout
    assert "semantic attempts      : 1" in refused.stdout
    assert blocked["recommended_next_action"] in refused.stdout
    assert run_cli(
        layout, "context", "--run", run_id, "--job", job_id, "--stage", "3"
    ).returncode == 1


# --------------------------------------------------------------------------
# T06 Approved set and baseline reconciliation
# --------------------------------------------------------------------------

def test_t06_expected_set_comes_from_the_manifest_not_the_filesystem(staged):
    """DEC-08: a deleted job directory is still reported from the manifest."""
    import shutil

    layout, run_id, manifest, job_id, _ = staged
    shutil.rmtree(layout.job_dir(run_id, job_id))

    status = status_module.derive(layout, manifest)
    assert status["counts"]["approved_total"] == 1
    assert [j["job_id"] for j in status["jobs"]] == [job_id], (
        "the job must still be enumerated from the manifest after its "
        "directory is gone; directory discovery never defines completeness"
    )
    assert status["jobs"][0]["production_state"] == "FAILED"
    assert status["jobs"][0]["blocking"] == "RUN-INTEGRITY FAILURE"


def test_t06_exceptions_are_countable_and_never_block_a_core_job(layout):
    csv = layout.inbox / "mixed.csv"
    exception_row = (
        "engelsk_stilling,Global Corp,Senior Analyst,EXCEPTION,c1,2,LOW,"
        "vacancies/testetaten_radgiver.md,,,,Utlysningen er på engelsk\n"
    )
    # Distinct source per job (one vacancy cannot serve two jobs).
    other = layout.inbox / "vacancies" / "global_corp.md"
    other.write_text(
        (layout.inbox / "vacancies" / "testetaten_radgiver.md").read_text(
            encoding="utf-8"
        ),
        encoding="utf-8", newline="\n",
    )
    exception_row = exception_row.replace(
        "vacancies/testetaten_radgiver.md", "vacancies/global_corp.md"
    )
    csv.write_text(BATCH_HEADER + BATCH_ROW + exception_row,
                   encoding="utf-8", newline="\n")

    result = freeze(layout, csv, reviewed_by="T", moment=FIXED_MOMENT)
    assert result.ok, result.result.render()
    status = status_module.derive(layout, load_manifest(layout, result.run_id))
    assert status["counts"]["approved_total"] == 2
    assert status["counts"]["core"] == 1
    assert status["counts"]["exception"] == 1
    exception = next(j for j in status["jobs"] if j["job_id"] == "engelsk_stilling")
    assert exception["production_state"] == "EXCEPTION"
    assert exception["exception_note"] == "Utlysningen er på engelsk"


def test_t06_exception_job_is_inert_to_public_core_actions(layout):
    other = layout.inbox / "vacancies" / "global_corp.md"
    other.write_text(
        (layout.inbox / "vacancies" / "testetaten_radgiver.md").read_text(
            encoding="utf-8"
        ),
        encoding="utf-8", newline="\n",
    )
    exception = (
        "engelsk_stilling,Global Corp,Senior Analyst,EXCEPTION,c1,1,LOW,"
        "vacancies/global_corp.md,,,,Utlysningen er på engelsk\n"
    )
    csv = layout.inbox / "exception.csv"
    csv.write_text(BATCH_HEADER + exception, encoding="utf-8", newline="\n")
    result = freeze(layout, csv, reviewed_by="T", moment=FIXED_MOMENT)
    assert result.ok, result.result.render()

    for command in (
        ("context", "--run", result.run_id, "--job", "engelsk_stilling", "--stage", "1"),
        ("finalize", "--run", result.run_id, "--job", "engelsk_stilling"),
        ("render", "--run", result.run_id, "--job", "engelsk_stilling"),
        (
            "stage-submit", "--run", result.run_id, "--job", "engelsk_stilling",
            "--stage", "1", "--handoff", "missing", "--file", "missing",
        ),
    ):
        completed = run_cli(layout, *command)
        assert completed.returncode == 1
        assert "EXCEPTION" in completed.stderr
    assert list(
        (layout.job_dir(result.run_id, "engelsk_stilling") / "current").glob("*")
    ) == []


def test_t06_exception_without_a_reason_is_rejected(layout):
    from jobbsok.batchinput import read_batch_input

    csv = layout.inbox / "noreason.csv"
    csv.write_text(BATCH_HEADER + BATCH_ROW.replace("CORE", "EXCEPTION"),
                   encoding="utf-8", newline="\n")
    _, result = read_batch_input(csv)
    assert not result.ok
    assert any(v.contract_id == "DEC-03" for v in result.errors)


def test_t06_baseline_versus_authority_conflict_blocks_freeze(layout):
    """Contract 6.1: freeze fails on a known conflict."""
    authority = layout.authorities / "Education.md"
    authority.write_text(
        authority.read_text(encoding="utf-8") + "\nEndret uten ny baseline.\n",
        encoding="utf-8", newline="\n",
    )
    result = freeze(
        layout, layout.inbox / "batch_input.csv", reviewed_by="T",
        moment=FIXED_MOMENT,
    )
    assert not result.ok
    assert any("Re-review the baseline" in v.observed for v in result.result.errors)
    assert list(layout.runs.glob("r*")) == []


# --------------------------------------------------------------------------
# T07 Schema: valid and adversarial fixtures
# --------------------------------------------------------------------------

def test_t07_valid_fixtures_pass_every_validator(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    for artifact, filename in (
        ("strategy", "strategy.valid.json"),
        ("final_package", "final_package.json"),
        ("review", "review.json"),
    ):
        payload = read_json(fixture_dir / filename)
        result = validate_module.validate_artifact(
            layout, context, job_id, artifact, payload
        )
        assert result.ok, f"{filename}:\n{result.render()}"


def test_t07_adversarial_strategy_reports_every_violation_in_one_pass(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.invalid.json")
    result = validate_module.validate_strategy(payload, context, job_id)

    assert not result.ok
    contracts = {v.contract_id for v in result.errors}
    # One pass must surface the schema violation, the identity drift, the
    # unresolvable factual ref, the unresolvable baseline ref and the
    # unknown facet id -- not just the first of them.
    assert {"CTR-04", "ACC-10", "ACC-08", "DEC-34", "DEC-35"} <= contracts, contracts
    assert len(result.errors) >= 5
    for violation in result.errors:
        assert violation.file and violation.location
        assert violation.expected and violation.observed


def test_t07_unknown_top_level_field_is_rejected(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    payload["portal_answers"] = []
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok, "schemas are intentionally closed (Contract 22)"


def test_t07_letter_may_not_be_null(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    payload["letter"] = None
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL"
    )
    assert not result.ok, "DEC-01: every core job produces a complete letter"


def test_t07_semantic_density_over_historical_defaults_still_passes(staged):
    """DEC-33: counts are never hard failures."""
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "final_package.json")
    payload["cv"]["competencies"] = [f"Kompetanse nummer {n}" for n in range(1, 21)]
    payload["letter"]["body_paragraphs"] *= 4
    result = validate_module.validate_package(
        payload, context, job_id, expected_stage="STAGE3_FINAL",
        soft_thresholds={"competencies_expected_min": 4, "competencies_expected_max": 8},
    )
    assert result.ok, f"counts must not fail validation:\n{result.render()}"
    assert any(v.severity == "WARNING" for v in result.warnings)


def test_t07_strategy_requirements_have_no_upper_bound(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    template = payload["material_requirements"][0]
    payload["material_requirements"] = [
        {**template, "requirement_id": f"R{n:02d}"} for n in range(1, 41)
    ]
    result = validate_module.validate_strategy(payload, context, job_id)
    assert result.ok, "no hard cap may truncate a material employer requirement"


# --------------------------------------------------------------------------
# T08 Current failure record
# --------------------------------------------------------------------------

def test_t08_failed_differs_from_never_started_without_reading_history(frozen):
    layout, run_id, manifest = frozen
    job_id = manifest["jobs"][0]["job_id"]

    status = status_module.derive(layout, manifest)
    assert status["jobs"][0]["production_state"] == "NOT_STARTED"
    assert failure_module.load(layout, run_id, job_id) is None

    diagnostics = ValidationResult()
    diagnostics.add("CTR-05", "draft_package.json", "/cv/profile",
                    "a profile", "missing")
    failure_module.record(
        layout, run_id, job_id, operation="STAGE2",
        classification="FAILED", result=diagnostics,
        diagnostic_summary="Draft was mechanically invalid.",
        recommended_next_action="Repair the draft and resubmit Stage 2.",
        attempts_used=1, last_successful_stage="STRATEGY",
    )
    status = status_module.derive(layout, manifest)
    assert status["jobs"][0]["production_state"] == "FAILED"
    assert status["counts"]["failed"] == 1

    # History must not be needed, and must not decide anything.
    history = layout.job_dir(run_id, job_id) / "history"
    history.mkdir(parents=True, exist_ok=True)
    (history / "20260101T000000Z_failure.json").write_text("{}", encoding="utf-8")
    assert status_module.derive(layout, manifest)["jobs"][0]["production_state"] == "FAILED"


def test_t08_success_clears_the_current_failure(frozen):
    layout, run_id, manifest = frozen
    job_id = manifest["jobs"][0]["job_id"]
    failure_module.record(
        layout, run_id, job_id, operation="RENDER", classification="FAILED",
        recommended_next_action="Retry the render.",
    )
    assert failure_module.load(layout, run_id, job_id) is not None
    assert failure_module.clear(layout, run_id, job_id)
    assert failure_module.load(layout, run_id, job_id) is None
    assert list((layout.job_dir(run_id, job_id) / "history").glob("*failure.json"))


def test_t08_blocked_manual_wins_and_exposes_the_next_action(frozen):
    layout, run_id, manifest = frozen
    job_id = manifest["jobs"][0]["job_id"]
    failure_module.record(
        layout, run_id, job_id, operation="STAGE3",
        classification="BLOCKED_MANUAL",
        diagnostic_summary="Configured retry path exhausted.",
        recommended_next_action="Restart Stage 1 manually or drop the job.",
        attempts_used=1, last_successful_stage="DRAFT",
    )
    status = status_module.derive(layout, manifest)
    job = status["jobs"][0]
    assert job["production_state"] == "BLOCKED_MANUAL"
    assert job["blocking"] == "Configured retry path exhausted."
    assert job["recommended_action"] == "Restart Stage 1 manually or drop the job."
    assert job["highest_valid_stage"] == "DRAFT"
    assert status["counts"]["blocked_manual"] == 1


def test_t08_retry_scaffolding_is_bounded_and_then_blocks():
    """DEC-36 / GATE-11: the array only tells the operator what to run next."""
    assert failure_module.next_retry_stage([3], 0) == 3
    assert failure_module.next_retry_stage([3], 1) is None
    assert failure_module.next_retry_stage([3, 2, 1], 2) == 1
    assert failure_module.next_retry_stage([], 0) is None


def test_t08_a_planted_marker_file_has_no_status_authority(staged):
    layout, run_id, manifest, job_id, _ = staged
    before = status_module.derive(layout, manifest)["jobs"][0]
    job_dir = layout.job_dir(run_id, job_id)
    (job_dir / "_DONE.md").write_text("Status: COMPLETED\nStage: 3\n", encoding="utf-8")
    (job_dir / "BATCH_STATUS.md").write_text("alt ferdig", encoding="utf-8")
    after = status_module.derive(layout, manifest)["jobs"][0]
    assert after == before, "markers and status prose have no authority (DEC-07)"


def test_t08_failed_replacement_is_surfaced_by_its_own_stage_queue(staged):
    """A failed replacement must not hide behind an older valid downstream stage.

    Replacing an upstream artifact never displaces the current one, so after a
    refused Stage-1 return the job still reports `highest_valid_stage == FINAL`.
    The stage ladder alone would then report nothing outstanding for Stage 1,
    contradicting the recovery action the same run just recorded.
    """
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = _public_context(layout, run_id, job_id, 1)
    invalid_file, _ = _semantic_return(
        layout, fixture_dir, "strategy.invalid.json", "strategy", "failed-stage1"
    )
    refused = _submit(
        layout, run_id, job_id, 1, context["handoff"]["path"], invalid_file
    )
    assert refused.returncode == 1, refused.stdout + refused.stderr

    record = failure_module.load(layout, run_id, job_id)
    assert record["operation"] == "STAGE1"
    assert record["classification"] == "FAILED"

    status = json.loads(
        run_cli(layout, "status", "--run", run_id, "--json").stdout
    )["jobs"][0]
    assert status["production_state"] == "FAILED"
    assert status["highest_valid_stage"] == "FINAL"

    owning = run_cli(layout, "next", "--run", run_id, "--stage", "1")
    assert owning.returncode == 0, owning.stderr
    assert job_id in owning.stdout, owning.stdout

    for other in (3,):
        quiet = run_cli(layout, "next", "--run", run_id, "--stage", str(other))
        assert "Nothing outstanding" in quiet.stdout, (other, quiet.stdout)

    # Bounded recovery is unchanged: a successful replacement clears the record
    # and the stage queue falls silent again.
    context = _public_context(layout, run_id, job_id, 1)
    valid_file, _ = _semantic_return(
        layout, fixture_dir, "strategy.valid.json", "strategy", "repaired-stage1"
    )
    accepted = _submit(
        layout, run_id, job_id, 1, context["handoff"]["path"], valid_file
    )
    assert accepted.returncode == 0, accepted.stdout + accepted.stderr
    assert failure_module.load(layout, run_id, job_id) is None
    cleared = run_cli(layout, "next", "--run", run_id, "--stage", "1")
    assert "Nothing outstanding" in cleared.stdout, cleared.stdout
