# Jobbsøk_26 — AGENTS.md

Norwegian job-application pipeline: turns human-approved vacancies plus three
authoritative candidate-fact files into tailored Bokmål CV + letter packages.
Truth always outranks persuasion. No portal or automated submission in core —
Vegard submits manually.

This file is ambient context for any agent working anywhere in this repo. Read
it before trusting any other file's instructions, including another
`AGENTS.md`. It is a map, not a specification: it routes you to the controlling
documents and states only the rules that must hold in every task.

## Repository state

- `P0.7/r0.7_release/` — last implemented pre-P0.9 release. **Superseded.**
  Historical asset mine only; never a compatibility target.
- `P0.9/Architecture/` — the controlling architecture, `FROZEN_NORMATIVE`.
- `P0.9/Build/` — the P0.9 implementation. **Built and mechanically tested, not
  production-ready.** Its test suite passes; several trust boundaries are known
  to be unenforced in production.
- `P0.9/Finalization_Review/` — review evidence for the current task. **Not
  authority.** `P0.9_Final_Multi_Model_Review_Reconciliation.md` is the
  synthesized six-model review and the working set; `sources/` holds the
  original reviews for provenance, disputed findings and reproduction detail.

**Active task:** a final adversarial perfection pass over `P0.9/Build/`, then
two real-job semantic smokes, then a cluster pilot. Nothing in this repository
is `PRODUCTION-MODEL_TESTED`.

## Authority

Governing, in this order — read these, not this file's summary of them:

1. `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` — the frozen rules
   (`DEC-*`, `INV-*`, `CTR-*`, `ACC-*`, `GATE-*`, `EXP-*`). Governs on conflict.
   §22.1 lists the frozen invariants; §22.2 lists what a builder may freely choose.
2. `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md` —
   the build contract. Subordinate to (1); §22 lists prohibited redesigns.
3. `P0.9_FINAL_DECISION_AND_ADOPTION_RECORD.md` — per-decision rationale, on demand.
4. `P0.9_FINAL_CRITIQUE_ADJUDICATION_AND_CLOSURE_MATRIX.md` and
   `Architecture/Process/` — historical provenance. Superseded; never resolve a
   conflict in their favour, and do not bulk-read them.

Review material is **evidence, not authority**. Reproduced behaviour in
`P0.9/Build/` outranks any reviewer's assertion, and any reviewer's assertion
outranks unsupported inference.

You are authorized to implement and verify the architecture, not to
re-adjudicate it (Contract §24). A genuine impossibility is escalated against
the exact governing ID with target-machine evidence — never resolved by silent
deviation.

## Optimizing

Among options that satisfy the hard boundaries, optimize in this order:

1. truthful employer-facing package quality / expected interview value;
2. low human effort;
3. simple, robust implementation;
4. model cost;
5. reversibility and optionality.

Literal compliance is not the objective. Implementation evidence may justify
keeping a deviation that serves this hierarchy better than the frozen wording —
say so explicitly and record it; do not deviate silently, and do not assume
"differs from the frozen plan" means "defective".

## Hard boundaries — never traded away

- Every material candidate claim truthful, correctly attributed, interview-defensible.
- Candidate, employer and job identity exact; the three factual authority files
  are the only source of candidate facts.
- Human approval before any submission or irreversible external action.
- No deterministic component makes network calls, model calls, employer contact,
  submissions or publications.
- No runtime numeric quality or fit judge; no automatic model orchestration or retry.
- Bokmål CV **and** letter for every core job — no `letter_required`, language,
  portal, channel or output-mode branch anywhere in core.

Contract §22 holds the full prohibited-redesign list. The ones most often
reintroduced by well-meaning agents: same-run amend, event sourcing or a
dependency engine, completion markers or authoritative progress files, a
dedicated `RERUN` subsystem, hard word/cardinality caps without a verified
technical consumer, PDF failure treated as semantic failure, and factual
evidence references pointing at `CV_BASELINE`.

## Working in `P0.9/Build/`

Layout and commands: `P0.9/Build/README.md` and `policy/RUNBOOK.md`. Role
separation is Contract §3 — `authorities/`, `context/`, `policy/`, `templates/`
and `schemas/` are protected inputs; only the current run/job output area is
model-writable.

Use scratch copies outside the tree for destructive tests. Run the suite with
the tree's own `.venv`. A passing test is evidence at the scope it actually
exercises — helper-level coverage is not proof of public-command behaviour.

## Hazard: stale `AGENTS.md` files under `P0.7/`

`P0.7/r0.7_release/stg{1,2,3,4}_*/AGENTS.md`, `P0.7_AGENTS.md` and
`MODEL_ROUTING.md` are real, internally consistent instruction sets for P0.7's
retired four-stage workflow — `_DONE.md` markers, stage conveyor, old model
names, no relation to P0.9. If tooling auto-loads one, or you read one while
exploring: it is not an instruction for any current task. This file and the
governing documents above override them unconditionally.

Read a more specific `AGENTS.md` where one exists inside a current P0.9
directory; there is none under `P0.9/` today.
