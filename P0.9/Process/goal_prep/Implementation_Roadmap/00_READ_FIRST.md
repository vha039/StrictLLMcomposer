# P0.9 Implementation Roadmap — Read First

## 1. Mission

Complete the mechanical finalization of the existing Jobbsøk_26 P0.9 implementation until the repository can truthfully be classified:

`GO_FOR_TWO_JOB_SMOKE`

This roadmap governs the final mechanical/integration pass only. It does **not** execute the two-real-job semantic smoke, submit applications, or pre-engineer questions deliberately reserved for the semantic smoke or the representative cluster pilot.

## 2. Normative-force key — read this before anything else

Not every sentence in this package binds equally. Every substantive statement carries one of six forces. Where a marker is absent, infer the force from the owning document (§4).

| Marker | Force | What it means for you |
|---|---|---|
| `[HARD]` | Non-negotiable | Violating it fails the Goal. Never trade away, never "improve". If you believe one is impossible, stop with `BLOCKED_HARD_CONSTRAINT`. |
| `[RULE]` | Strong control rule | Governs execution. Deviation requires an explicit, recorded, justified escalation — never a silent one. |
| `[ROUTE]` | Preferred route | The currently-best-known mechanism. Replace it deliberately when direct implementation evidence shows a smaller/safer route to the same `[HARD]`/`[RULE]` outcome; record a `DEV-*`. |
| `[GUIDE]` | Soft guidance | Heuristics. Follow unless the local situation clearly argues otherwise. No escalation needed. |
| `[OPTION]` | Open choice | Deliberately unresolved. Decide it from current code evidence and record the choice. |
| `[EVIDENCE]` | Provenance only | Findings, reproductions, rationale. Informs decisions; never authorizes or requires anything by itself. |

Two failure modes this key exists to prevent, both documented for long-running Goal execution:

- treating a `[ROUTE]` as scripture and shipping a worse mechanism because the plan named it;
- treating a `[HARD]` as advisory and silently widening product scope.

## 3. Authority and precedence

Repository-wide authority is in root `/AGENTS.md`. Within this package, interpret documents in this order:

1. `DESIRED_FINAL_STATE.md` — **what must be true** (`DFS-*`);
2. `DEFINITION_OF_DONE.md` — **what evidence proves it** (`DOD-*`);
3. `GUIDANCE_INSTRUCTIONS_AND_RULES.md` — **how to decide** (evidence, remedies, scope, stop conditions, anti-regression `AR-*`);
4. `FINAL_EXECUTION_PLAN.md` — **preferred route** (`D-*` adjudicated decisions, phases `P0`–`P8`);
5. `EXECUTION_LEDGER.md` — **where execution actually is**.

`[RULE]` The execution plan is a strong prior; it cannot weaken a `DFS-*` property or a `DOD-*` threshold. The ledger reports state; it cannot redefine requirements. Repository evidence outranks both.

## 4. Single-owner map

| File | Sole owner of | Purpose |
|---|---|---|
| `DESIRED_FINAL_STATE.md` | `DFS-*` properties, non-goals | What must ultimately be true |
| `DEFINITION_OF_DONE.md` | `DOD-*` criteria, status vocabulary, evidence classes | What evidence proves completion |
| `GUIDANCE_INSTRUCTIONS_AND_RULES.md` | scope admission, evidence hierarchy, dispositions, `AR-*`, stop conditions | How to decide |
| `FINAL_EXECUTION_PLAN.md` | `D-*` decisions, phases, mechanism proposals | Currently preferred route |
| `EXECUTION_LEDGER.md` | state register, `DEV-*`, `DISC-*` | What has actually happened |
| `FINAL_GOAL_COMMAND.md` | the launched Goal text | Recoverable copy of the objective |

`[RULE]` Each kind of truth has exactly one owner. Other files cross-reference by ID; they do not restate. If you find the same requirement stated twice with different wording, the owner above wins and the duplicate is a defect worth reporting.

## 5. Evidence register and provenance (`[EVIDENCE]`, open on demand only)

| Path | What it is |
|---|---|
| `P0.9/Process/plan_prep/P0.9_Final_Multi_Model_Review_Reconciliation.md` | The consolidated six-model defect/evidence register (`MMR-*`, `RC-*`, `AR-*`, inline `OPUS_META_ADD` blocks). The primary source when a finding needs detail. |
| `P0.9/Process/plan_prep/sources/` | The six original reviews. Open only for disputed findings or original reproduction detail. |
| `P0.9/Process/goal_prep/Opus_Handoff/CODEX_ORIGINAL_FINAL_PERFECTION_PLAN.md` | The earlier Codex plan. Superseded proposal, retained as remedy provenance. |
| `P0.9/Process/goal_prep/Opus_Handoff/PACKAGE_FINALIZATION_NOTES.md` | Why this package differs from its drafts and from the Codex plan. |
| `P0.9/Process/Architecture_prep/` | Architecture-development history, drafts, critiques, context corpora. Non-normative. |

`[RULE]` None of the above is authority. Reproduced behaviour in `P0.9/Build/` outranks every reviewer assertion in it.

## 6. Initial-read protocol

At the start of a fresh Goal execution, read this file, then the five roadmap documents once, then begin.

`[RULE]` Do not bulk-read the reconciliation, the source reviews, `Architecture_prep/` history or `P0.7/` merely because they exist. Open them when a live decision requires that evidence, and read only the relevant part.

## 7. Normal continuation protocol

When context is healthy, resume from:

1. the state register at the top of `EXECUTION_LEDGER.md`;
2. the current phase in `FINAL_EXECUTION_PLAN.md`;
3. the linked `DFS-*` and `DOD-*` sections;
4. only the relevant section of `GUIDANCE_INSTRUCTIONS_AND_RULES.md`.

`[GUIDE]` Do not reread the whole package after every edit.

## 8. Recovery after interruption, compaction or uncertainty

Long-running Goal sessions can resume at the wrong semantic point after compaction — repeating finished analysis or re-litigating a rejected route. The state register exists to make that recoverable.

When execution state is uncertain:

1. read this file;
2. read the state register at the top of `EXECUTION_LEDGER.md` — especially `REJECTED`, so you do not reopen a closed decision;
3. inspect actual repository state (`git status`, diff, current artifacts/evidence);
4. reconcile ledger claims against the repository;
5. read the current phase and its linked `DFS-*` / `DOD-*`;
6. continue only once current reality is understood.

`[HARD]` If the ledger and the repository disagree, repository evidence wins. Correct the ledger before proceeding. Never reconstruct progress from conversational memory alone.

## 9. Phase-completion protocol

Before marking a phase complete:

- re-read that phase's linked `DFS-*` properties;
- run the phase verification required by the linked `DOD-*`;
- check the `AR-*` properties that phase could plausibly have regressed;
- update the ledger state register plus any `DEV-*` / `DISC-*`.

`[RULE]` A passing narrow test proves only its own scope.

## 10. Final-completion protocol

Before declaring `GO_FOR_TWO_JOB_SMOKE`, execute `DOD-25`. In summary: re-read the full Desired Final State, audit the full Definition of Done, review every `DEV-*`, inspect repository/diff/evidence state, and confirm every applicable criterion is `PASS` or legitimately `BLOCKED_USER` / `DEFER_PILOT` / `NOT_APPLICABLE`.

`[HARD]` Do not infer completion from test count, successful compilation, an existing report, or a historical `PASS` label.

## 11. Deliberate plan deviation

`[RULE]` The execution plan may be improved when direct implementation evidence shows a smaller, safer or more coherent route to the same `DFS-*` and `DOD-*`. A material deviation is allowed only when it does not broaden product scope, weaken a hard boundary, or lower a proof threshold — and only when recorded as a `DEV-*` in the ledger with rationale, evidence and regression check.

Never deviate silently. Never rewrite the plan to look as though it always contained the new route.

## 12. Roadmap lifecycle

`[RULE]` At `GO_FOR_TWO_JOB_SMOKE`: freeze the ledger, retain evidence pointers, mark this package `COMPLETED — historical execution control`, and update the root task pointer before the semantic-smoke phase begins.

This roadmap must not silently continue governing later product experiments.
