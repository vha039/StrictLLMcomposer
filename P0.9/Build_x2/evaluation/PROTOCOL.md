# Paired Build_x2 experiment

The stable arm is `stable_snapshot/` captured before x2 edits. Verify every
snapshot file against `provenance/stable_source_sha256.json`; verify x2 files
against `provenance/x2_implemented_sha256.json`. Never edit the snapshot.
The common, six-vacancy source is `corpus/batch_input.csv` and
`corpus/vacancies/`. The operational x2 inbox stays empty until a trial.

## Gate execution (human started)

1. Gate 1 is `x2_gate1` (Stortinget, Abacus). Gate 2 is `x2_holdout`
   (BearingPoint, Amesto). Gate 3 is `x2_regression` (Norwegian, EIE).
2. For each gate, copy `stable_snapshot/` to a new scratch root outside
   `Build_x2`; create a new `.venv` there and install `-e .[dev]`.
   Use a fresh x2 run with no artifacts from earlier gates. Copy the same
   batch and vacancy bytes into both arm inboxes; filter only the gate's
   two rows. Run each arm's `index build`, preflight, freeze, and
   verify-integrity. Record both manifests and compare authority, baseline,
   vacancy, model, effort, grouping and human task wording before Stage 1.
3. Open distinct fresh human-started chats for each arm and stage. Use the
   neutral prompts in this directory, replacing `<ARM_ROOT>`, `<RUN>` and
   `<CLUSTER>` only. Each chat reads its own arm's frozen stage instruction.
   No reasoning, package or output crosses arms. Counterbalance launch
   order: stable first in Gate 1, x2 first in Gate 2, stable first in Gate 3.
4. Record stage launches, interventions, review minutes, tokens, cost,
   resubmissions, stale incidents, preview use and render limitations in
   `session_log.csv`. Missing measurements stay `UNKNOWN`.
5. After each completed pair, run `make_pairs.py` with separate arm package
   directories and an arm key path outside the blinded output tree. The
   script copies bytes and never edits package content. Assess A/B blind.

## Evaluation and stop rules

Estimate interview probability for each package and judge the paired choice
(A, B or tie). Record these in `scorecard.csv`. Diagnostic dimensions are
truth and defensibility, material answers, contribution/delivery/adoption/
persistence, employer relevance and motivation, readability/tone/social
calibration, and CV/letter physical presentation. Diagnostics explain the
primary outcome and cannot override it.

An unsupported material claim, identity error, missing supported material
answer, lifecycle or attribution error, CV over two pages, or letter over one
page is a hard failure. Stop after Gate 1 if either x2 package has a hard
failure, both x2 packages lose on interview likelihood, or human intervention
or review load rises. Run Gate 2 only if Gate 1 passes. Run Gate 3 only if
x2 wins at least three of four first pairs, aggregate estimated interview
probability rises, at least one holdout pair favors x2, and human load does
not rise. Gate 3 fails if either historical vacancy acquires a hard failure
or material interview-likelihood decline. On a material failure, change only
the implicated mechanism and rerun the affected gate from fresh runs.

The implementation phase ends with mechanics and these materials. No semantic
session is initiated by the implementation worker. Promotion to `Build` is a
separate decision after the paired experiment.
