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
  Exactly four files, listed below. Nothing else lives here.
- `P0.9/Build/` — the P0.9 implementation. **Built and mechanically tested, not
  production-ready.** Its test suite passes; several trust boundaries are known
  to be unenforced through the public command path.
- `P0.9/Process/` — preparation, review and provenance material. **Not
  authority**, whatever the directory names suggest.
  - `Architecture_prep/` — architecture drafts, critiques, context corpora.
  - `plan_prep/` — consolidated review evidence.
    `P0.9_Final_Multi_Model_Review_Reconciliation.md` is the six-model defect
    register; `sources/` holds the originals.
  - `goal_prep/` — the active control package and its handoff material.

**Active task:** P0.9.3 two-stage implementation under the explicit amendment;
not `PRODUCTION-MODEL_TESTED`.

**Start here for that task:**
`P0.9/Process/optimization_0.9.3/P0.9.3_FINAL_SEMANTIC_PLAN.md` and
`P0.9/Process/optimization_0.9.3/P0.9.3_FINAL_OPERATIONAL_PLAN.md`

## Authority

Governing, in this order — read these, not this file's summary of them:

1. Current explicit user instruction and the active Goal.
2. `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` — the frozen rules
   (`DEC-*`, `INV-*`, `CTR-*`, `ACC-*`, `GATE-*`, `EXP-*`). Governs on conflict.
   §22.1 lists the frozen invariants; §22.2 lists what a builder may freely choose.
3. `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md` —
   the build contract. Subordinate to (2); §22 lists prohibited redesigns.
4. Explicitly user-authorized architecture amendments recorded during finalization.
5. `P0.9_FINAL_DECISION_AND_ADOPTION_RECORD.md` — per-decision rationale, on demand.
6. `P0.9_FINAL_CRITIQUE_ADJUDICATION_AND_CLOSURE_MATRIX.md` and everything under
   `P0.9/Process/` — provenance only. Never resolve a conflict in their favour,
   and do not bulk-read them.

Reviews, plans and roadmaps are **evidence and proposals, not commands**.
Reproduced behaviour in `P0.9/Build/` outranks any reviewer assertion, and any
reviewer assertion outranks unsupported inference.

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
model-writable. Between runs, explicit human-invoked source-maintenance tooling
and an explicitly tasked agent may maintain instructions, indexes,
retrieval/selection metadata and derived baseline hash linkage. Candidate facts
and their ceilings stay user-owned: only explicitly confirmed factual changes
may be made, and this widens no semantic-stage write permission.

Use scratch copies outside the tree for destructive tests. Run the suite with
the tree's own `.venv`. Do not inventory `.venv/`, `__pycache__/` or
`.pytest_cache/`. A passing test is evidence at the scope it actually exercises
— helper-level coverage is not proof of public-command behaviour.

## Hazard: stale `AGENTS.md` files under `P0.7/`

`P0.7/r0.7_release/stg{1,2,3,4}_*/AGENTS.md`, `P0.7_AGENTS.md` and
`MODEL_ROUTING.md` are real, internally consistent instruction sets for P0.7's
retired four-stage workflow — `_DONE.md` markers, stage conveyor, old model
names, no relation to P0.9. If tooling auto-loads one, or you read one while
exploring: it is not an instruction for any current task. This file and the
governing documents above override them unconditionally.

A file named `AGENTS.md` under `P0.9/Process/` is a draft candidate, not ambient
authority. Read a more specific `AGENTS.md` only where one exists inside a
current P0.9 working directory; there is none today.
