"""Traceability: every Tier-1 item and mechanical ACC id names a real test.

Contract 23 requires a traceability matrix. This registry prevents a coverage
mapping from quietly drifting away from its named test; it does not prove that
the named test exercises a public command or an available target machine.
`evidence/finalization/TRACEABILITY.md` records the strongest scope reached.

`ACC-20` is deliberately absent from the mechanical map: it covers the real
product pilot, which no deterministic test can satisfy (INV-08). It is
listed here as explicitly owed rather than silently skipped.

Under the explicit P0.9.3 amendment the active semantic route is Stage 1 then
Stage 3, so every Tier-1 item below is exercised against that route. The
draft contract `CTR-05` is historical: its coverage lives in the frozen 0.9.0
runs this suite still reads through the legacy interpretation, not in any
active-stage test. Nothing here claims coverage the named tests do not
actually exercise.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

TESTS = Path(__file__).resolve().parent
RUNTIME = TESTS.parent

#: Contract 17.1 Tier-1 items -> the test-name substring that proves each.
TIER1 = {
    1: "test_t01_",
    2: "test_t02_",
    3: "test_t03_",
    4: "test_t04_",
    5: "test_t05_",
    6: "test_t06_",
    7: "test_t07_",
    8: "test_t08_",
    9: "test_t09_",
    10: "test_t10_",
    11: "test_t11_",
    12: "test_t12_",
    13: "test_t13_",
    14: "test_t14_",
    15: "test_t15_",
    16: "test_t16_",
    17: "test_t17_",
    18: "test_t18_",
    19: "test_t19_",
    20: "test_t20_",
    21: "test_t21_",
    22: "test_t22_",
    23: "test_t23_",
}

TIER1_TITLES = {
    1: "freeze/immutability", 2: "branch", 3: "idempotency",
    4: "identity/path", 5: "stage ownership", 6: "approved set/baseline",
    7: "schema", 8: "current failure", 9: "state axes", 10: "static staleness",
    11: "evidence namespace", 12: "no byte partition", 13: "CV merge",
    14: "leakage", 15: "personality", 16: "partial success",
    17: "continuation", 18: "template preflight", 19: "target render",
    20: "date/rerender", 21: "human edit", 22: "security",
    23: "source inspection",
}

#: ACC ids with executable engineering evidence -> a test-name substring.
ACC_COVERAGE = {
    "ACC-01": "test_t07_letter_may_not_be_null",
    "ACC-02": "test_t06_exceptions_are_countable",
    "ACC-03": "test_t02_child_gets_new_id",
    "ACC-04": "test_t22_protected_inputs_reject_writes",
    "ACC-05": "test_t09_every_required_production_state_is_reachable",
    "ACC-06": "test_t09_pdf_degradation_does_not_change_semantic_triage",
    "ACC-07": "test_t07_strategy_requirements_have_no_upper_bound",
    "ACC-08": "test_t11_baseline_reference_is_rejected_as_factual_support",
    "ACC-09": "test_t15_three_facets_pass_and_four_fail",
    "ACC-10": "test_t04_identity_drift_in_an_artifact_is_rejected",
    "ACC-11": "test_t13_present_override_fully_replaces_the_baseline_bullets",
    "ACC-12": "test_t19_target_machine_produces_both_docx",
    "ACC-13": "test_t07_adversarial_strategy_reports_every_violation_in_one_pass",
    "ACC-14": "test_t08_blocked_manual_wins",
    "ACC-15": "test_t16_one_poisoned_job_leaves_other_outputs_untouched",
    "ACC-16": "test_t19_pdf_failure_degrades_without_touching_the_semantic_axis",
    "ACC-17": "test_t21_promotion_refuses_a_file_this_pipeline_did_not_write",
    "ACC-18": "test_t18_actual_masters_match_the_single_canonical_map",
    "ACC-19": "test_t22_no_network_or_model_client_is_imported",
}

#: Not mechanically testable. Owed to the real pilot, not to this suite.
ACC_NOT_MECHANICAL = {
    "ACC-20": "real-job pilot: quality, effort, tail and counts with human "
              "scoring. Engineering tests must never be cited as product "
              "quality evidence (INV-08).",
}


def _all_test_names() -> set[str]:
    names: set[str] = set()
    for path in TESTS.glob("test_*.py"):
        for match in re.finditer(r"^def (test_\w+)", path.read_text(encoding="utf-8"),
                                 re.M):
            names.add(match.group(1))
    return names


@pytest.fixture(scope="module")
def test_names() -> set[str]:
    return _all_test_names()


@pytest.mark.parametrize("item", sorted(TIER1))
def test_tier1_item_has_at_least_one_test(item, test_names):
    prefix = TIER1[item]
    matching = [name for name in test_names if name.startswith(prefix)]
    assert matching, (
        f"Tier-1 item {item} ({TIER1_TITLES[item]}) has no test named {prefix}*"
    )


@pytest.mark.parametrize("acc", sorted(ACC_COVERAGE))
def test_acceptance_criterion_has_a_named_test(acc, test_names):
    needle = ACC_COVERAGE[acc]
    matching = [name for name in test_names if name.startswith(needle)]
    assert matching, f"{acc} points at {needle}*, which does not exist"


def test_acc_20_is_explicitly_owed_not_silently_skipped():
    assert set(ACC_COVERAGE) | set(ACC_NOT_MECHANICAL) == {
        f"ACC-{n:02d}" for n in range(1, 21)
    }
    assert "ACC-20" in ACC_NOT_MECHANICAL


def test_every_tier1_item_is_accounted_for():
    assert set(TIER1) == set(range(1, 24))
    assert set(TIER1_TITLES) == set(TIER1)


def test_no_experiment_only_subsystem_exists():
    """EXP-01..EXP-08 must add no unused hooks to the baseline."""
    banned = (
        "convergence_detector", "similarity_gate", "ngram_gate",
        "cluster_planner", "priority_predictor", "quality_judge",
        "best_of_n", "prep_model", "luna", "advisory_preparation",
        "experiment_hook", "trait_score", "archetype_memory",
    )
    for path in sorted((RUNTIME / "jobbsok").glob("*.py")):
        text = path.read_text(encoding="utf-8").lower()
        for token in banned:
            assert token not in text, f"{path.name} contains {token!r}"


def test_no_prohibited_redesign_surface_in_the_active_tree():
    """Contract 22, checked against code identifiers rather than prose."""
    import ast

    banned_names = {
        "letter_required", "portal_answers", "portal_status", "required_components",
        "manifest_version", "event_log", "replay_history", "rerun_workflow",
        "quality_score", "confidence_score", "fit_score", "trait_score",
    }
    offenders: list[str] = []
    for path in sorted((RUNTIME / "jobbsok").glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if node.name in banned_names:
                    offenders.append(f"{path.name}:{node.name}")
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if node.id in banned_names:
                    offenders.append(f"{path.name}:{node.id}")
            elif isinstance(node, ast.arg) and node.arg in banned_names:
                offenders.append(f"{path.name}:{node.arg}")
    assert not offenders, offenders
