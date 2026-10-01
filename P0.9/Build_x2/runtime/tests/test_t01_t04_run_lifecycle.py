"""Tier-1 items 1-4: freeze/immutability, branch, idempotency, identity/path."""

from __future__ import annotations

import json
import pathlib
from datetime import datetime, timedelta, timezone

import pytest

from conftest import (
    BATCH_HEADER,
    BATCH_ROW,
    FIXED_MOMENT,
    make_fixtures,
    run_cli,
)
from jobbsok import branch as branch_module
from jobbsok.atomicio import read_json
from jobbsok.batchinput import read_batch_input
from jobbsok.errors import PathSafetyError, RunIntegrityError
from jobbsok.hashing import sha256_file
from jobbsok.manifest import (
    FROZEN_DIR,
    _iter_frozen_records,
    freeze,
    load_manifest,
    require_intact,
    verify_frozen,
)
from jobbsok.paths import require_safe_component, resolve_within


# --------------------------------------------------------------------------
# T01 Freeze / immutability
# --------------------------------------------------------------------------

def test_t01_manifest_hashes_the_actual_sources(frozen):
    layout, run_id, manifest = frozen
    records = list(_iter_frozen_records(manifest["frozen_inputs"]))
    assert len(records) >= 20, "every frozen input must be hashed"
    for record in records:
        frozen_copy = layout.run_dir(run_id) / FROZEN_DIR / record["path"]
        assert frozen_copy.is_file(), f"{record['path']} was not preserved in the run"
        assert sha256_file(frozen_copy) == record["sha256"]
        assert sha256_file(layout.root / record["path"]) == record["sha256"], (
            "the manifest must hash the actual repository source at freeze time"
        )


def test_t01_vacancy_original_is_preserved_byte_for_byte(frozen):
    layout, run_id, manifest = frozen
    job = manifest["jobs"][0]
    preserved = layout.run_dir(run_id) / job["source"]["relpath"]
    original = layout.inbox / "vacancies" / "testetaten_radgiver.md"
    assert preserved.read_bytes() == original.read_bytes()
    assert sha256_file(preserved) == job["source"]["sha256"]


def test_t01_mutating_a_frozen_input_makes_commands_fail(frozen):
    layout, run_id, manifest = frozen
    target = (
        layout.run_dir(run_id) / FROZEN_DIR / "authorities" / "Work_experience.md"
    )
    target.write_text(
        target.read_text(encoding="utf-8") + "\ntampered\n", encoding="utf-8"
    )

    result = verify_frozen(layout, manifest)
    assert not result.ok
    assert any("Work_experience" in v.file for v in result.errors)
    assert any("child run" in v.observed for v in result.errors), (
        "the remedy must be restoration or a child run, never an in-place update"
    )
    with pytest.raises(RunIntegrityError):
        require_intact(layout, manifest)


def test_t01_public_commands_ignore_all_maintained_root_changes(layout):
    from jobbsok import artifacts as artifacts_module

    settings = layout.policy / "settings.toml"
    settings.write_text(
        settings.read_text(encoding="utf-8").replace(
            'converter = "word_com"', 'converter = "none"'
        ),
        encoding="utf-8",
        newline="\n",
    )
    frozen_result = freeze(
        layout, layout.inbox / "batch_input.csv",
        reviewed_by="T", moment=FIXED_MOMENT,
    )
    assert frozen_result.ok, frozen_result.result.render()
    run_id = frozen_result.run_id
    manifest = frozen_result.manifest
    job_id = manifest["jobs"][0]["job_id"]
    fixture_dir = make_fixtures(layout, run_id)
    for stage, artifact, filename in (
        (1, "strategy", "strategy.valid.json"),
        (3, "final_package", "final_package.json"),
        (3, "review", "review.json"),
    ):
        result = artifacts_module.submit(
            layout, run_id, job_id, stage=stage, artifact=artifact,
            payload=read_json(fixture_dir / filename), timestamp="20260823T060000Z",
        )
        assert result.ok, result.result.render()
    finalized = run_cli(
        layout, "finalize", "--run", run_id, "--job", job_id,
        "--date", "2026-08-23", "--reviewed-by", "T",
    )
    assert finalized.returncode == 0, finalized.stderr + finalized.stdout

    for path in (
        layout.authorities / "Work_experience.md",
        layout.context / "PERSONALITY_PROFILE.md",
        layout.policy / "settings.toml",
    ):
        path.write_text(
            path.read_text(encoding="utf-8") + "\nmaintained after freeze\n",
            encoding="utf-8", newline="\n",
        )
    (layout.schemas / "final_package.schema.json").write_text(
        "not the frozen schema", encoding="utf-8"
    )
    (layout.templates / "CV_MASTER.docx").write_bytes(b"not the frozen master")

    integrity = run_cli(layout, "verify-integrity", "--run", run_id)
    validation = run_cli(layout, "validate", "--run", run_id)
    rendered = run_cli(layout, "render", "--run", run_id, "--job", job_id)
    assert integrity.returncode == 0, integrity.stderr + integrity.stdout
    assert validation.returncode == 0, validation.stderr + validation.stdout
    assert rendered.returncode == 0, rendered.stderr + rendered.stdout
    out = layout.job_dir(run_id, job_id) / "out"
    assert len(list(out.glob("*.docx"))) == 2


def test_t01_public_commands_refuse_frozen_input_tampering(frozen):
    layout, run_id, _ = frozen
    target = layout.run_dir(run_id) / FROZEN_DIR / "policy" / "stages" / \
        "stage1_decision_architecture.md"
    target.write_text(
        target.read_text(encoding="utf-8") + "\ntampered\n", encoding="utf-8"
    )

    integrity = run_cli(layout, "verify-integrity", "--run", run_id)
    validation = run_cli(layout, "validate", "--run", run_id)
    assert integrity.returncode == 2
    assert validation.returncode == 2
    assert "stage1_decision_architecture.md" in integrity.stdout
    assert "restore" in integrity.stdout.casefold() or "child run" in integrity.stdout.casefold()


def test_t01_no_same_run_amend_path_exists():
    """DEC-40: there is no same-run amend, anywhere in the command surface."""
    from jobbsok.cli import build_parser

    parser = build_parser()
    actions = [
        a for a in parser._actions if hasattr(a, "choices") and a.choices
    ]
    commands: set[str] = set()
    for action in actions:
        if isinstance(action.choices, dict):
            commands |= set(action.choices)
    assert commands, "expected subcommands"
    assert not any("amend" in name for name in commands)
    assert "branch" in commands


def test_t01_freeze_fails_atomically_on_bad_input(layout):
    bad = layout.inbox / "bad.csv"
    bad.write_text(
        BATCH_HEADER + BATCH_ROW.replace("CORE", "SOMETHING_ELSE"),
        encoding="utf-8", newline="\n",
    )
    result = freeze(layout, bad, reviewed_by="T", moment=FIXED_MOMENT)
    assert not result.ok
    assert result.run_id is None
    assert list(layout.runs.glob("*")) == [], "no partial run may be left behind"


# --------------------------------------------------------------------------
# T02 Branch
# --------------------------------------------------------------------------

def test_t02_child_gets_new_id_and_parent_link_and_parent_is_untouched(staged):
    layout, run_id, manifest, job_id, _ = staged
    parent_dir = layout.run_dir(run_id)
    before = {
        path.relative_to(parent_dir).as_posix(): sha256_file(path)
        for path in sorted(parent_dir.rglob("*")) if path.is_file()
    }

    result = branch_module.branch(
        layout, run_id, reviewed_by="T",
        moment=FIXED_MOMENT + timedelta(hours=1),
    )
    assert result.ok, result.result.render()
    assert result.run_id != run_id
    assert result.manifest["parent_run_id"] == run_id
    # The child is published inside the root ancestor's branches
    # directory and nowhere deeper (DEC-40).
    assert result.run_id.startswith(f"{run_id}/branches/stage")
    assert layout.run_dir(result.run_id).is_dir()

    after = {
        path.relative_to(parent_dir).as_posix(): sha256_file(path)
        for path in sorted(parent_dir.rglob("*")) if path.is_file()
    }
    # ACC-03: every pre-existing entry is byte-identical, and the only
    # addition is the new child namespace.
    added = {path for path in after if path not in before}
    assert all(
        path.startswith(result.run_id[len(run_id) + 1:] + "/") for path in added
    ), f"only the new child may be added: {sorted(added)[:3]}"
    survivors = {path: digest for path, digest in after.items() if path in before}
    assert survivors == before, "every prior entry must survive untouched"


def test_t02_unchanged_payload_is_rebound_not_reauthored(staged):
    layout, run_id, manifest, job_id, _ = staged
    result = branch_module.branch(
        layout, run_id, reviewed_by="T", moment=FIXED_MOMENT + timedelta(hours=1)
    )
    assert set(result.disposition[job_id].values()) == {branch_module.REUSED}

    parent_payload = read_json(
        layout.job_dir(run_id, job_id) / "current" / "strategy.json"
    )
    child_payload = read_json(
        layout.job_dir(result.run_id, job_id) / "current" / "strategy.json"
    )
    # Identity/hash metadata is rebound; the semantic payload is identical.
    assert child_payload["binding"]["run_id"] == result.run_id
    assert child_payload["binding"]["manifest_sha256"] != \
        parent_payload["binding"]["manifest_sha256"]
    for key in child_payload:
        if key != "binding":
            assert child_payload[key] == parent_payload[key], (
                f"{key} was altered; a rebind must never author or change payload"
            )
    assert "PENDING" not in json.dumps(
        [read_json(path) for path in (
            layout.job_dir(result.run_id, job_id) / "current"
        ).glob("*.json")]
    )
    checked = run_cli(layout, "validate", "--run", result.run_id)
    assert checked.returncode == 0, checked.stdout + checked.stderr
    status = run_cli(layout, "status", "--run", result.run_id, "--json")
    assert status.returncode == 0, status.stdout + status.stderr
    job = json.loads(status.stdout)["jobs"][0]
    assert job["production_state"] == "VALID"
    assert job["semantic_final_available"] is True
    assert job["semantic_triage"] == "CHECK"


def test_t02_changed_governing_input_forces_regeneration(staged):
    """A changed upstream instruction invalidates strategy and its descendants."""
    layout, run_id, manifest, job_id, _ = staged
    instruction = layout.policy / "stages" / "stage1_decision_architecture.md"
    instruction.write_text(
        instruction.read_text(encoding="utf-8") + "\n\n## Tillegg\n\nNy regel.\n",
        encoding="utf-8", newline="\n",
    )
    result = branch_module.branch(
        layout, run_id, reviewed_by="T", moment=FIXED_MOMENT + timedelta(hours=2)
    )
    assert result.ok, result.result.render()
    states = result.disposition[job_id]
    assert states["strategy"] == branch_module.REGENERATE_REQUIRED
    assert states["final_package"] == branch_module.REGENERATE_REQUIRED
    assert states["review"] == branch_module.REGENERATE_REQUIRED
    assert not (
        layout.job_dir(result.run_id, job_id) / "current" / "strategy.json"
    ).exists(), "no artifact becomes current in the child merely by existing in the parent"


@pytest.mark.parametrize("target_kind", ["frozen", "vacancy"])
def test_t02_public_branch_refuses_compromised_parent_without_child(
    staged, target_kind,
):
    layout, run_id, manifest, _, _ = staged
    if target_kind == "frozen":
        target = layout.run_dir(run_id) / FROZEN_DIR / "policy" / "settings.toml"
    else:
        target = layout.run_dir(run_id) / manifest["jobs"][0]["source"]["relpath"]
    target.write_bytes(target.read_bytes() + b"\ntampered\n")
    before = {path.name for path in layout.runs.iterdir()}

    completed = run_cli(
        layout, "branch", "--run", run_id, "--reviewed-by", "T",
        "--at", "2026-08-23T09:00:00",
    )

    assert completed.returncode == 2
    assert {path.name for path in layout.runs.iterdir()} == before
    assert not list(layout.runs.glob(".branching-*"))


def test_t02_public_branch_invalidates_changed_stage_and_descendants(staged):
    layout, run_id, _, job_id, _ = staged
    instruction = layout.policy / "stages" / "stage3_final_writer_review.md"
    instruction.write_text(
        instruction.read_text(encoding="utf-8") + "\n\n## Tillegg\n\nNy regel.\n",
        encoding="utf-8", newline="\n",
    )
    completed = run_cli(
        layout, "branch", "--run", run_id, "--reviewed-by", "T",
        "--at", "2026-08-23T10:00:00",
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    child_run = completed.stdout.split("Child run : ", 1)[1].splitlines()[0]
    assert "strategy=REUSED" in completed.stdout
    assert "draft_package" not in completed.stdout
    assert "final_package=REGENERATE_REQUIRED" in completed.stdout
    assert "review=REGENERATE_REQUIRED" in completed.stdout
    current = layout.job_dir(child_run, job_id) / "current"
    assert {path.name for path in current.glob("*.json")} == {"strategy.json"}
    checked = run_cli(layout, "validate", "--run", child_run)
    assert checked.returncode == 0, checked.stdout + checked.stderr


def test_t02_interrupted_branch_never_exposes_canonical_child(staged, monkeypatch):
    layout, run_id, _, _, _ = staged
    parent_dir = layout.run_dir(run_id)
    before = {
        path.relative_to(parent_dir).as_posix(): sha256_file(path)
        for path in parent_dir.rglob("*") if path.is_file()
    }
    original_rename = type(parent_dir).rename

    def interrupt_exposure(path, target):
        if path.name.startswith(".branching-"):
            raise OSError("simulated interruption before canonical exposure")
        return original_rename(path, target)

    monkeypatch.setattr(type(parent_dir), "rename", interrupt_exposure)
    with pytest.raises(OSError, match="simulated interruption"):
        branch_module.branch(
            layout, run_id, reviewed_by="T",
            moment=FIXED_MOMENT + timedelta(hours=5),
        )
    assert {path.name for path in layout.runs.iterdir()} == {run_id}
    after = {
        path.relative_to(parent_dir).as_posix(): sha256_file(path)
        for path in parent_dir.rglob("*") if path.is_file()
    }
    assert after == before


def test_t02_changed_authority_blocks_branch_until_reconciliation_is_redone(staged):
    """Contract 6.1: freeze and branch fail on a known baseline conflict.

    Editing a candidate authority without re-reviewing CV_BASELINE against it
    means the rendered static chronology may now disagree with the source.
    That is a human decision between runs, not something tooling resolves.
    """
    layout, run_id, manifest, job_id, _ = staged
    authority = layout.authorities / "Work_experience.md"
    authority.write_text(
        authority.read_text(encoding="utf-8") + "\n\n### Ny seksjon\n\nNy tekst.\n",
        encoding="utf-8", newline="\n",
    )
    result = branch_module.branch(
        layout, run_id, reviewed_by="T", moment=FIXED_MOMENT + timedelta(hours=3)
    )
    assert not result.ok
    assert result.run_id is None
    assert any(v.contract_id == "CTR-01" for v in result.result.errors)
    assert any("Re-review the baseline" in v.observed for v in result.result.errors)


# --------------------------------------------------------------------------
# T03 Idempotency
# --------------------------------------------------------------------------

def test_t03_repeated_validation_and_status_create_no_duplicate_state(staged):
    from jobbsok import status as status_module
    from jobbsok import validate as validate_module

    layout, run_id, manifest, job_id, _ = staged
    context = validate_module.RunContext(layout, manifest)
    current = layout.job_dir(run_id, job_id) / "current"
    before = sorted(p.name for p in current.iterdir())

    first = status_module.derive(layout, manifest, context=context)
    second = status_module.derive(layout, manifest, context=context)

    after = sorted(p.name for p in current.iterdir())
    assert after == before, "status derivation must not write authoritative state"
    first.pop("derived_at"), second.pop("derived_at")
    assert first == second, "derivation must be deterministic for identical inputs"


def test_t03_index_regenerates_identically(layout):
    from jobbsok.evidence_index import build_index

    first = build_index(layout.authorities)
    second = build_index(layout.authorities)
    assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)


def test_t03_finalize_is_idempotent_and_preserves_the_date(staged):
    from jobbsok import artifacts as artifacts_module
    from jobbsok.atomicio import atomic_write_json

    layout, run_id, manifest, job_id, _ = staged
    path = artifacts_module.artifact_path(layout, run_id, job_id, "final_package")
    payload = read_json(path)
    payload["finalization"] = {
        "state": "FINALIZED", "document_date": "2026-08-23",
        "finalized_at": "2026-08-23T06:00:00Z", "finalized_by": "T",
    }
    atomic_write_json(path, payload)
    first_hash = artifacts_module.artifact_hash(read_json(path))

    # Re-reading and rewriting the same payload must not change the semantic
    # hash, and the date must survive.
    atomic_write_json(path, read_json(path))
    assert artifacts_module.artifact_hash(read_json(path)) == first_hash
    assert read_json(path)["finalization"]["document_date"] == "2026-08-23"


def test_t03_document_date_is_outside_the_semantic_hash(staged):
    """DEC-26: assigning the date invalidates render only, not the review."""
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, job_id, fixture_dir = staged
    payload = read_json(fixture_dir / "final_package.json")
    without = artifacts_module.artifact_hash(payload)
    payload["finalization"] = {
        "state": "FINALIZED", "document_date": "2026-09-01",
        "finalized_at": "2026-09-01T00:00:00Z", "finalized_by": "T",
    }
    assert artifacts_module.artifact_hash(payload) == without


@pytest.mark.parametrize("triage", ["READY", "CHECK", "RERUN"])
def test_t03_public_finalize_is_not_gated_by_review_triage(staged, triage):
    from jobbsok import artifacts as artifacts_module
    from jobbsok.atomicio import atomic_write_json

    layout, run_id, manifest, job_id, _ = staged
    review_path = artifacts_module.artifact_path(
        layout, run_id, job_id, "review"
    )
    review = read_json(review_path)
    review["triage"] = triage
    atomic_write_json(review_path, review)

    completed = run_cli(
        layout, "finalize", "--run", run_id, "--job", job_id,
    )

    assert completed.returncode == 0, completed.stderr + completed.stdout
    final_path = artifacts_module.artifact_path(
        layout, run_id, job_id, "final_package"
    )
    assert read_json(final_path)["finalization"]["state"] == "FINALIZED"


@pytest.mark.parametrize("bad_date", ["23.08.2026", "2026-02-30", "2026-8-3"])
def test_t03_public_finalize_refuses_noncanonical_or_impossible_dates(staged, bad_date):
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, job_id, _ = staged
    path = artifacts_module.artifact_path(layout, run_id, job_id, "final_package")
    before = sha256_file(path)
    completed = run_cli(
        layout, "finalize", "--run", run_id, "--job", job_id,
        "--date", bad_date,
    )
    assert completed.returncode == 1
    assert "canonical YYYY-MM-DD" in completed.stderr
    assert sha256_file(path) == before


def test_t03_public_finalize_is_idempotent_and_semantic_hash_neutral(staged):
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, job_id, _ = staged
    path = artifacts_module.artifact_path(layout, run_id, job_id, "final_package")
    semantic_before = artifacts_module.artifact_hash(read_json(path))
    first = run_cli(
        layout, "finalize", "--run", run_id, "--job", job_id,
        "--date", "2026-08-23", "--reviewed-by", "T",
    )
    assert first.returncode == 0, first.stderr + first.stdout
    after_first = read_json(path)
    second = run_cli(layout, "finalize", "--run", run_id, "--job", job_id)
    assert second.returncode == 0, second.stderr + second.stdout
    after_second = read_json(path)
    assert after_second == after_first
    assert artifacts_module.artifact_hash(after_second) == semantic_before


# --------------------------------------------------------------------------
# T04 Identity and path safety
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    "component",
    ["..", "a/b", "a\\b", "NUL", "con.json", "trailing.", "  leading", "x" * 200, ""],
)
def test_t04_unsafe_path_components_are_rejected(component):
    with pytest.raises(PathSafetyError):
        require_safe_component(component)


@pytest.mark.parametrize(
    "candidate", ["../../etc/passwd", "..\\..\\windows\\system32", "/etc/shadow"]
)
def test_t04_traversal_is_rejected(layout, candidate):
    with pytest.raises(PathSafetyError):
        resolve_within(layout.runs, candidate)


def test_t04_symlink_or_junction_escape_is_rejected(layout, tmp_path):
    """Spec 17.2: reparse points are handled deliberately, not followed.

    Symlink creation needs Developer Mode or admin on Windows; a directory
    junction does not, and is the same reparse-point class. Either one must
    be refused.
    """
    import subprocess

    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "file.json").write_text("{}", encoding="utf-8")
    link = layout.runs / "sneaky"

    made = False
    try:
        link.symlink_to(outside, target_is_directory=True)
        made = True
    except (OSError, NotImplementedError):
        completed = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(outside)],
            capture_output=True, text=True,
        )
        made = completed.returncode == 0 and link.exists()
    if not made:
        pytest.skip("neither a symlink nor a junction could be created here")

    from jobbsok.paths import is_reparse_point

    assert is_reparse_point(link), "the link must be detected as a reparse point"
    with pytest.raises(PathSafetyError):
        resolve_within(layout.runs, "sneaky/file.json")


def test_t04_duplicate_job_ids_fail_loudly(layout):
    duplicate = layout.inbox / "dupe.csv"
    duplicate.write_text(BATCH_HEADER + BATCH_ROW + BATCH_ROW,
                         encoding="utf-8", newline="\n")
    _, result = read_batch_input(duplicate)
    assert not result.ok
    assert any(v.contract_id == "ACC-02" for v in result.errors)


def test_t04_two_jobs_may_not_share_one_vacancy_source(layout):
    collision = layout.inbox / "collide.csv"
    second = BATCH_ROW.replace("testetaten_radgiver,", "annen_jobb,", 1)
    collision.write_text(BATCH_HEADER + BATCH_ROW + second,
                         encoding="utf-8", newline="\n")
    _, result = read_batch_input(collision)
    assert not result.ok
    assert any("already used by job" in v.observed for v in result.errors)


def test_t04_unsupported_and_oversized_sources_fail(layout):
    bad = layout.inbox / "vacancies" / "vacancy.exe"
    bad.write_bytes(b"MZ\x00\x00")
    csv = layout.inbox / "exe.csv"
    csv.write_text(
        BATCH_HEADER + BATCH_ROW.replace(
            "vacancies/testetaten_radgiver.md", "vacancies/vacancy.exe"
        ),
        encoding="utf-8", newline="\n",
    )
    result = freeze(layout, csv, reviewed_by="T", moment=FIXED_MOMENT)
    assert not result.ok
    assert any(v.contract_id == "ACC-19" for v in result.result.errors)


def test_t04_identity_drift_in_an_artifact_is_rejected(staged):
    from jobbsok import validate as validate_module

    layout, run_id, manifest, job_id, fixture_dir = staged
    context = validate_module.RunContext(layout, manifest)
    payload = read_json(fixture_dir / "strategy.valid.json")
    payload["binding"]["title"] = "En helt annen tittel"
    result = validate_module.validate_strategy(payload, context, job_id)
    assert not result.ok
    assert any(v.location == "binding.title" for v in result.errors)


# --------------------------------------------------------------------------
# P0.9.3: two-stage chain, ordinary redo, nested references, frozen fetch and
# policy/hash scoping. These are implementation checks of new mechanics, not
# semantic quality gates.
# --------------------------------------------------------------------------

def test_p093_from_stage_redo_removes_exactly_the_requested_stages(staged):
    """--from-stage is the first stage to execute again, not an 'after' label."""
    layout, run_id, manifest, job_id, _ = staged

    redo3 = branch_module.branch(
        layout, run_id, reviewed_by="T", from_stage=3,
        moment=FIXED_MOMENT + timedelta(hours=3),
    )
    assert redo3.ok, redo3.result.render()
    states = redo3.disposition[job_id]
    assert states["strategy"] == branch_module.REUSED
    assert states["final_package"] == branch_module.REGENERATE_REQUIRED
    assert states["review"] == branch_module.REGENERATE_REQUIRED
    current = layout.job_dir(redo3.run_id, job_id) / "current"
    assert {p.name for p in current.glob("*.json")} == {"strategy.json"}
    assert redo3.run_id.startswith(f"{run_id}/branches/stage3_unknown_")

    redo1 = branch_module.branch(
        layout, run_id, reviewed_by="T", from_stage=1, model_tag="opus5",
        moment=FIXED_MOMENT + timedelta(hours=4),
    )
    assert redo1.ok, redo1.result.render()
    assert set(redo1.disposition[job_id].values()) == {
        branch_module.REGENERATE_REQUIRED
    }
    assert not list((layout.job_dir(redo1.run_id, job_id) / "current").glob("*.json"))
    assert redo1.run_id.startswith(f"{run_id}/branches/stage1_opus5_")

    # Omitting it keeps the ordinary policy-driven reuse.
    kept = branch_module.branch(
        layout, run_id, reviewed_by="T",
        moment=FIXED_MOMENT + timedelta(hours=5),
    )
    assert kept.ok, kept.result.render()
    assert kept.disposition[job_id]["final_package"] == branch_module.REUSED
    assert kept.run_id.startswith(f"{run_id}/branches/stage0_unknown_")


def test_p093_next_stage3_selects_a_current_strategy_and_review_loss_is_review_only(staged):
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, job_id, _ = staged
    queued = run_cli(layout, "next", "--run", run_id, "--stage", "3")
    assert queued.returncode == 0

    artifacts_module.artifact_path(layout, run_id, job_id, "review").unlink()
    reoffered = run_cli(layout, "next", "--run", run_id, "--stage", "3")
    assert reoffered.returncode == 0 and job_id in reoffered.stdout
    bundle = json.loads(run_cli(
        layout, "context", "--run", run_id, "--job", job_id, "--stage", "3"
    ).stdout)
    assert bundle["handoff"]["mode"] == "REVIEW_ONLY"

    artifacts_module.artifact_path(layout, run_id, job_id, "final_package").unlink()
    awaiting = run_cli(layout, "next", "--run", run_id, "--stage", "3")
    assert awaiting.returncode == 0 and job_id in awaiting.stdout
    status = json.loads(run_cli(layout, "status", "--run", run_id, "--json").stdout)
    assert status["jobs"][0]["recommended_action"] == "Run Stage 3."


def test_p093_branch_of_a_branch_is_a_sibling_with_the_exact_parent(staged):
    layout, run_id, manifest, job_id, _ = staged
    child = branch_module.branch(
        layout, run_id, reviewed_by="T", from_stage=3,
        moment=FIXED_MOMENT + timedelta(hours=6),
    )
    assert child.ok, child.result.render()

    ancestor_dir = layout.run_dir(run_id)
    before = {
        path.relative_to(ancestor_dir).as_posix(): sha256_file(path)
        for path in sorted(ancestor_dir.rglob("*")) if path.is_file()
    }
    grandchild = branch_module.branch(
        layout, child.run_id, reviewed_by="T", from_stage=1,
        moment=FIXED_MOMENT + timedelta(hours=7),
    )
    assert grandchild.ok, grandchild.result.render()

    # One physical level: the grandchild is a sibling under the same ancestor.
    assert grandchild.run_id.startswith(f"{run_id}/branches/stage1_")
    assert grandchild.run_id.count("/branches/") == 1
    assert grandchild.manifest["parent_run_id"] == child.run_id

    after = {
        path.relative_to(ancestor_dir).as_posix(): sha256_file(path)
        for path in sorted(ancestor_dir.rglob("*")) if path.is_file()
    }
    added = {path for path in after if path not in before}
    component = grandchild.run_id.split("/branches/", 1)[1]
    assert added and all(path.startswith(f"branches/{component}/") for path in added)
    assert {p: d for p, d in after.items() if p in before} == before, (
        "ACC-03: every pre-existing byte, including the sibling branch, survives"
    )
    assert run_cli(
        layout, "verify-integrity", "--run", child.run_id
    ).returncode == 0


def test_p093_nested_child_completes_the_public_path(staged):
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, job_id, fixture_dir = staged
    child = branch_module.branch(
        layout, run_id, reviewed_by="T", from_stage=3,
        moment=FIXED_MOMENT + timedelta(hours=8),
    )
    assert child.ok, child.result.render()
    reference = child.run_id

    bundle = json.loads(run_cli(
        layout, "context", "--run", reference, "--job", job_id, "--stage", "3"
    ).stdout)
    assert bundle["run_id"] == reference
    # Generated directories use the flattened key; the reference itself does not.
    for path_key in (bundle["handoff"]["path"], *bundle["write"]["return_paths"].values()):
        assert reference.replace("/", "__") in path_key

    returns = {}
    for artifact, filename in (
        ("final_package", "final_package.json"), ("review", "review.json"),
    ):
        payload = read_json(fixture_dir / filename)
        for field in artifacts_module.MECHANICAL_FIELDS[artifact]:
            payload.pop(field, None)
        target = pathlib.Path(bundle["write"]["return_paths"][artifact])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        returns[artifact] = target

    submitted = run_cli(
        layout, "stage-submit", "--run", reference, "--job", job_id,
        "--stage", "3", "--handoff", bundle["handoff"]["path"],
        "--file", str(returns["final_package"]),
        "--review-file", str(returns["review"]),
    )
    assert submitted.returncode == 0, submitted.stderr + submitted.stdout

    final = artifacts_module.load(layout, reference, job_id, "final_package")
    assert final["binding"]["run_id"] == reference
    assert final["binding"]["strategy_sha256"] == artifacts_module.artifact_hash(
        artifacts_module.load(layout, reference, job_id, "strategy")
    )
    assert "draft_sha256" not in final["binding"]

    finalized = run_cli(
        layout, "finalize", "--run", reference, "--job", job_id,
        "--date", "2026-08-24", "--reviewed-by", "T",
    )
    assert finalized.returncode == 0, finalized.stderr + finalized.stdout
    # The nested component lengthens the run path, and MAX_PATH_CHARS is
    # deliberately unchanged, so render into a short destination the way the
    # existing budgeter expects. The receipt, not a hardcoded long filename,
    # names the actual outputs.
    rendered = run_cli(layout, "render", "--run", reference, "--job", job_id)
    receipt_path = (
        layout.job_dir(reference, job_id) / "current" / "render_report.json"
    )
    if rendered.returncode == 0:
        receipt = read_json(receipt_path)
        assert receipt["binding"]["run_id"] == reference
        # Output names come from the receipt and the existing budgeter, never
        # from a hardcoded long filename.
        for document in receipt["documents"]:
            if document["format"] == "docx" or document["state"] == "OK":
                assert document["state"] == "OK"
                assert pathlib.Path(document["output_path"]).is_file()
            else:
                assert document["format"] == "pdf"
                assert document["state"] == "DEGRADED"
                assert document["output_path"] is None
    else:
        # MAX_PATH_CHARS is deliberately unchanged, and pytest's temporary root
        # is far deeper than runs/ on the real machine. The nested component
        # can therefore exhaust the budget here; that is the existing guard
        # firing, not a broken reference. The export path below still proves
        # the nested reference resolves through rendering.
        assert "too deep to hold a usable output name" in (
            rendered.stdout + rendered.stderr
        )
        assert not receipt_path.is_file()
        export = pathlib.Path(layout.evidence) / "o"
        export.mkdir(exist_ok=True)
        exported = run_cli(
            layout, "render", "--run", reference, "--job", job_id,
            "--dest", str(export),
        )
        assert exported.returncode == 0, exported.stderr + exported.stdout
        assert list(export.glob("*.docx")), "the nested child renders real output"

    status = json.loads(
        run_cli(layout, "status", "--run", reference, "--json").stdout
    )
    assert status["run_id"] == reference


def test_p093_frozen_fetch_and_stage_specific_context(staged):
    from jobbsok import evidence_index as index_module
    from jobbsok.manifest import FrozenRunAssets

    layout, run_id, manifest, job_id, _ = staged
    assets = FrozenRunAssets(layout, manifest)
    index = assets.json("evidence_index")
    work_path = assets.path("authorities", "WORK")
    work_text = work_path.read_bytes().decode("utf-8")

    entry = index_module.resolve_section(index, "WORK", "4.3")
    slice_text = index_module.slice_entry(work_text, entry)
    assert slice_text in work_text, "the slice must be a verbatim substring"
    assert "PRJ-03" in slice_text
    assert "ø" in work_text and slice_text == "".join(
        work_text.splitlines(keepends=True)[entry["line_start"] - 1: entry["line_end"]]
    )
    # Line endings and final-newline presence are preserved rather than rejoined.
    crlf = "a\r\nb\r\nc"
    assert index_module.slice_entry(
        crlf, {"line_start": 1, "line_end": 2}
    ) == "a\r\nb\r\n"

    # A live-source edit cannot change what the frozen run returns.
    live = layout.authorities / "Work_experience.md"
    live.write_text(
        live.read_text(encoding="utf-8") + "\n\n## Ny\n\nTekst.\n",
        encoding="utf-8", newline="\n",
    )
    assert index_module.slice_entry(
        assets.path("authorities", "WORK").read_bytes().decode("utf-8"), entry
    ) == slice_text

    # Unknown IDs simply do not resolve.
    assert index_module.resolve(index, "EV:WORK#does-not-exist") is None

    # 4.1 is not 4.10, and a range covers its interior headings.
    assert index_module.resolve_section(index, "WORK", "4.1")["evidence_id"] !=         index_module.resolve_section(index, "WORK", "4.10")["evidence_id"]
    ranged = index_module.ids_for_refs(index, "WORK", "§§4.1–4.4")
    assert index_module.resolve_section(index, "WORK", "4.2")["evidence_id"] in ranged
    assert index_module.resolve_section(index, "WORK", "4.10")["evidence_id"] not in ranged

    responsibilities = index_module.resolve_section(
        index, "WORK", "Nåværende rolle – forsvarlige ansvarsområder"
    )
    early_ous = index_module.resolve_section(
        index, "WORK", "Tidlig OUS-plassering – Barne- og ungdomsklinikken (BAR)"
    )
    ous_refs = index_module.ids_for_refs(index, "WORK", "1.1")
    assert responsibilities["evidence_id"] in ous_refs
    assert early_ous["evidence_id"] in ous_refs
    assert "SuperBruker" in index_module.slice_entry(work_text, responsibilities)

    # The §10 children resolve explicitly; the parent span does not include them.
    parent = index_module.resolve_section(index, "WORK", "10")
    child = index_module.resolve_section(index, "WORK", "10.1")
    assert parent is not None and child is not None
    assert parent["line_end"] < child["line_start"]

    stage1 = json.loads(run_cli(
        layout, "context", "--run", run_id, "--job", job_id, "--stage", "1"
    ).stdout)
    assert set(stage1["read"]["authorities"]) == {"WORK", "EDU", "OTHER"}
    assert "authority_digests" not in stage1["read"]
    assert stage1["read"]["evidence_ids"] == index_module.ordered_evidence_ids(index)
    assert stage1["read"]["mandatory_source_refs"]
    assert stage1["optional_source_access"]["authorities"]
    assert stage1["read"]["baseline_map"]["employments"][0]["ref"].startswith("BL:")
    assert stage1["read"]["baseline_map"]["employments"][0]["default_bullets"]
    assert set(stage1["write"]["allowed"]) == {"strategy"}
    assert stage1["write"]["semantic_fields"]["strategy"]

    stage3 = json.loads(run_cli(
        layout, "context", "--run", run_id, "--job", job_id, "--stage", "3"
    ).stdout)
    assert "authorities" not in stage3["read"]
    assert "authority_digests" not in stage3["read"]
    assert "evidence_fetch" not in stage3["read"]
    assert "evidence_ids" not in stage3["read"]
    assert "optional_source_access" not in stage3
    assert "GLOBAL BOUNDARY VERBATIM" in stage3["read"]["selected_evidence"]
    assert responsibilities["evidence_id"] in stage3["read"]["selected_evidence_refs"]
    assert index_module.slice_entry(work_text, responsibilities).strip() in stage3["read"]["selected_evidence"]
    assert early_ous["evidence_id"] in stage3["read"]["selected_evidence_refs"]
    assert str(layout.run_dir(run_id)) not in stage3["read"]["selected_evidence"]
    assert stage3["read"]["baseline_map"]["employments"][0]["default_bullets"]
    assert set(stage3["write"]["allowed"]) == {"final_package", "review"}
    assert set(stage3["write"]["semantic_fields"]) == {"final_package", "review"}


def test_p093_policy_hash_scope_and_preserved_raw_instruction_sha(staged):
    from jobbsok import manifest as manifest_module
    from jobbsok.hashing import sha256_file
    from jobbsok.manifest import FrozenRunAssets
    from jobbsok.validate import RunContext

    layout, run_id, manifest, job_id, _ = staged
    assets = FrozenRunAssets(layout, manifest)
    context = RunContext(layout, manifest)

    # RP-06: the artifact binding hash is the raw frozen instruction file SHA.
    raw = context.stage_instruction_sha256("strategy")
    assert raw == sha256_file(assets.path("stage_instructions", "stage1"))
    combined = assets.stage_policy_sha256(1)
    assert combined != raw, "the handoff policy hash is a different quantity"

    # Stage 1 sees doctrine and persuasion only; Stage 3 sees all three.
    names1 = [
        pathlib.Path(record["path"]).name
        for record in manifest_module.writing_policy_records(manifest, 1)
    ]
    names3 = [
        pathlib.Path(record["path"]).name
        for record in manifest_module.writing_policy_records(manifest, 3)
    ]
    assert names1 == ["PERSUASION_CALIBRATION.md", "WRITING_DOCTRINE.md"]
    assert "FORFATTERSTEMME.md" in names3 and len(names3) == 3

    # A voice-only change leaves the strategy reusable but regenerates the final.
    voice = layout.policy / "writing" / "FORFATTERSTEMME.md"
    voice.write_text(
        voice.read_text(encoding="utf-8")
        + "\n\n## Tillegg\n\nNy regel.\n",
        encoding="utf-8",
        newline="\n",
    )
    voice_child = branch_module.branch(
        layout, run_id, reviewed_by="T", moment=FIXED_MOMENT + timedelta(hours=9)
    )
    assert voice_child.ok, voice_child.result.render()
    assert voice_child.disposition[job_id]["strategy"] == branch_module.REUSED
    assert voice_child.disposition[job_id]["final_package"] ==         branch_module.REGENERATE_REQUIRED

    # A baseline-only change regenerates the strategy (RP-08).
    baseline = layout.authorities / "CV_BASELINE.md"
    baseline.write_text(
        baseline.read_text(encoding="utf-8").replace(
            "Oppgis ved forespørsel.", "Oppgis på forespørsel."
        ),
        encoding="utf-8", newline="\n",
    )
    baseline_child = branch_module.branch(
        layout, run_id, reviewed_by="T", moment=FIXED_MOMENT + timedelta(hours=10)
    )
    assert baseline_child.ok, baseline_child.result.render()
    assert baseline_child.disposition[job_id]["strategy"] ==         branch_module.REGENERATE_REQUIRED

    # A doctrine change also regenerates the strategy.
    doctrine = layout.policy / "writing" / "WRITING_DOCTRINE.md"
    doctrine.write_text(
        doctrine.read_text(encoding="utf-8")
        + "\n\n## Tillegg\n\nNy regel.\n",
        encoding="utf-8",
        newline="\n",
    )
    doctrine_child = branch_module.branch(
        layout, run_id, reviewed_by="T", moment=FIXED_MOMENT + timedelta(hours=11)
    )
    assert doctrine_child.ok, doctrine_child.result.render()
    assert doctrine_child.disposition[job_id]["strategy"] ==         branch_module.REGENERATE_REQUIRED
