# P0.9 Finalization Guidance, Instructions and Rules

## 1. Purpose and freedom envelope — `[HARD]` boundary, `[RULE]` elsewhere

This document governs **how implementation decisions are made** during the P0.9 mechanical finalization pass.

The destination is defined by `DESIRED_FINAL_STATE.md`. Completion evidence is defined by `DEFINITION_OF_DONE.md`. `FINAL_EXECUTION_PLAN.md` is the preferred route.

Sol has meaningful freedom to optimize **local implementation mechanism**. Sol does not have freedom to silently change:
- product scope;
- hard truth/identity/human-authority boundaries;
- approved architecture semantics;
- Desired Final State;
- Definition-of-Done thresholds.

Constrain outcomes and proof strongly. Keep mechanism adaptive.

## 2. Evidence hierarchy — `[RULE]`

Use evidence by directness and scope.

Preferred classifications:

- `REPRODUCED` — directly reproduced through the current relevant public/target path;
- `STATICALLY_CONFIRMED` — current code/data makes the claim unambiguous without executing it;
- `INHERITED_UNVERIFIED` — accepted provisionally from prior review evidence but not independently confirmed in the current pass;
- `PARTIAL` — only part of the claimed behavior is confirmed;
- `FALSIFIED` — current evidence contradicts the claim.

Do not call inherited evidence “confirmed.”

For implementation behavior:
1. current public-path reproduction;
2. current target-environment reproduction;
3. unambiguous current code-path evidence;
4. independent review convergence;
5. design inference;
6. literal-compliance concern.

Evidence must match the scope of the claim.

## 3. Disposition vocabulary — `[RULE]`

Use:

- `FIX` — demonstrated harmful defect;
- `IMPROVE` — worthwhile change, but the best remedy may differ from an earlier proposal;
- `KEEP` — current behavior/deviation is benign or better and must not be regressed;
- `AMEND` — evidence justifies an explicit narrow architecture clarification/change;
- `DEFER` — do not implement in this mechanical baseline; learn later or leave outside scope.

A reviewer’s disposition is evidence, not authority.

## 4. Remedy-selection rule — `[RULE]`

For every material repair, answer:

1. **What invariant/property is actually broken?**
2. **What is the smallest change that makes that failure impossible or reliably detectable?**
3. **If the diagnosis is wrong, what useful behavior could this remedy damage?**
4. **What known-good behavior must remain intact?**
5. **Can existing machinery close the defect more simply than a new abstraction/configuration surface?**
6. **Is the proposed mechanism solving one defect or creating a general framework for hypothetical future use?**

Prefer one coherent root-cause repair over several local symptom patches.

Do not equate “more defensive,” “more generic,” “more configurable,” or “more architecturally elegant” with “better.”

## 5. Complexity-admission rule — `[RULE]`

Before adding a new module, abstraction, schema layer, configuration surface, compatibility layer, workflow mechanism or persistent state concept, identify the accepted `DFS-*` / `DOD-*` requirement that becomes materially safer, simpler or less duplicated because it exists.

If no concrete accepted requirement needs it, do not add it.

A single-caller abstraction is acceptable when it creates a real trust boundary, isolates platform complexity, materially improves testability or simplifies an invariant. It is not justified merely for hypothetical reuse.

Prefer mechanically boring solutions.

## 6. Scope-admission rule for newly discovered work — `[HARD]`

*(This section is the single owner of scope admission. Other files reference it; they do not restate it.)*

New work may enter this finalization scope only if it is:

- required to achieve an existing `DFS-*` property;
- required to satisfy an applicable `DOD-*` criterion;
- a material correctness/integrity/containment defect exposed by approved work;
- a regression introduced by this finalization;
- a direct blocker to completing an already approved phase safely.

Otherwise record:

`DEFER_DISCOVERED`

with a concise reason in the execution ledger.

Implementation freedom does **not** include freedom to invent product scope.

## 7. Deliberate deviation from the execution plan — `[RULE]`

`FINAL_EXECUTION_PLAN.md` is the approved preferred route, not immutable scripture.

A material deviation is allowed when direct implementation evidence shows a smaller, safer, simpler or more coherent route to the same Desired Final State and DoD.

Before deviating, verify:
- the destination is unchanged;
- the proof threshold is unchanged;
- no hard boundary is weakened;
- product scope is not broadened;
- the new route does not silently resurrect a previously rejected subsystem.

Record the deviation in `EXECUTION_LEDGER.md` with:
- original route;
- chosen route;
- evidence/rationale;
- affected `DFS-*` / `DOD-*`;
- regression check.

Do not rewrite history to make the plan appear as if it always contained the new route.

## 8. Architecture-amendment discipline — `[HARD]`

Do not silently change normative architecture.

If implementation evidence justifies `AMEND`:
- identify the exact affected governing IDs/files;
- state the trigger/evidence;
- state old vs new rule;
- state frozen-run/revision/migration consequences;
- ensure explicit human authority exists;
- synchronize all required architecture/adoption records.

Prefer implementation fixes under existing intent when architecture already supports the required outcome.

Do not create an amendment merely to document an incidental implementation choice.

## 9. Failure-scope reasoning — `[RULE]`

Do not use exception class as a substitute for failure scope.

Reason about at least:

- `artifact-local`;
- `job-local`;
- `run-global`;
- `environment-global`.

A job-local malformed artifact/operator mistake should not unnecessarily abort independent healthy jobs when shared state remains known-safe.

A disk-full condition, shared permission failure, corrupt common configuration or other global uncertainty may legitimately require broader abort.

Containment must preserve trustworthy state, not maximize continuation at any cost.

## 10. Anti-regression register (`AR-*`) — `[RULE]`

This section is the **single owner** of the anti-regression set. `DEFINITION_OF_DONE.md` audits these by ID; it does not restate them.

Protect the **property**, not the incidental mechanism that currently implements it — unless direct target evidence makes the mechanism itself safety-critical. Never turn a library or product name into permanent architecture when the property can be preserved another way.

| ID | Protected property | Regression to avoid |
|---|---|---|
| `AR-01` | A working target-machine PDF path exists and is the proven baseline | Replacing or supplementing the working converter without target evidence that the alternative is better |
| `AR-02` | Masters are repaired reproducibly through maintained tooling, preserving the control inventory | Hand-editing a master, or rebuilding from scratch and losing template capital |
| `AR-03` | Rendered fonts/glyphs are actually present on the target machine and embed correctly | Chasing historical font metrics with no visual evidence |
| `AR-04` | Semantic artifact identity is independent of document finalization/date | Folding date or finalization state back into semantic/review identity |
| `AR-05` | Norwegian `æ/ø/å` survive filename folding | Reverting to plain NFKD, which silently deletes them |
| `AR-06` | Runs read their own immutable frozen snapshot | "Simplifying" back to live-root reads instead of making consumers consistent |
| `AR-07` | Factual evidence and mechanical-baseline references occupy separate namespaces | Adding ranking, claim graphs or a vector store to the baseline |
| `AR-08` | Exactly three manually initiated semantic stages | Adding a preparation, judging or fourth stage as a repair mechanism |
| `AR-09` | Stage 3 is truth-bounded elastic | Adding a strategy-compliance comparator or gate |
| `AR-10` | PDF/render degradation is orthogonal to semantic validity | Making render failure a semantic production failure, or adding a DOCX-only mode |
| `AR-11` | Human-edited deliverables are protected by ownership-checked promotion | Restoring destructive directory replacement, or normalising routine `--force` use |
| `AR-12` | Humans hold factual and irreversible authority | Introducing semantic truth checks in code, or any automated submission/contact |
| `AR-13` | One poisoned job does not block, demote or hide healthy jobs | Turning a run into an all-or-nothing transaction |
| `AR-14` | Semantic-density limits are warnings, never mechanical failures | Reintroducing hard word/count/page caps as validators |
| `AR-15` | Recovery is bounded, visible and manual | Building an automatic model-retry or workflow orchestration engine |
| `AR-16` | Untouched OOXML package parts stay byte-safe and target-Word-compatible; the master's own namespace/root declarations survive the round trip | Introducing any transformation that reserializes or normalizes protected parts without target-Word evidence that the result still opens. This is a property, not a ban on a named library |
| `AR-17` | After freeze, a run has no live dependency on `inbox/` or any maintained root | Reintroducing a live maintained-root read for an existing run while adding child-intake convenience |
| `AR-18` | Editorial/soft findings are structurally incapable of failing a command | Promoting warnings to errors while tightening currentness gating. Gate on currentness directly instead |
| `AR-19` | Freeze blocks on a known baseline↔authority reconciliation conflict | Weakening or bypassing that gate while refactoring freeze |
| `AR-20` | One automation instance per document, macros disabled, opened read-only; the operator's own application session is never disturbed | Sharing or persisting an automation instance, or terminating processes not provably owned by this run |

`[RULE]` If a repair appears to require regressing an `AR-*`, that is an escalation, not an implementation detail.

## 11. Tool-owned versus model-owned information — `[RULE]`

A semantic model should author semantic judgment and semantic content.

If a field’s correct value is mechanically predetermined by current repository/run state, strongly prefer deterministic tooling to supply, insert or verify it.

Do not make the human/model repeatedly reproduce canonical hashes, run identities or fixed protocol constants that tooling already knows.

Conversely, do not let deterministic tooling decide:
- factual truth beyond mechanical authority checks;
- persuasion/positioning;
- requirement interpretation;
- writing quality;
- semantic triage beyond mechanically defined fields.

## 12. Verification cadence — `[GUIDE]`

Use layered verification.

### After a local edit
Run the smallest relevant unit/integration test.

### After a coherent root-cause repair
Run the targeted public-path/adversarial tests that exercise the repaired boundary.

### At phase exit
Run the relevant regression neighborhood plus linked `DOD-*` checks.

### At major checkpoints
Run the full deterministic suite appropriate to the target environment.

### At finalization
Run the full suite, full applicable DoD audit, gate/evidence regeneration and final `/review`.

Do not rerun the entire suite after every trivial edit.

Do not treat test count as confidence.

## 13. Public-path proof over helper confidence — `[RULE]`

A helper can be correct while the production path never calls it.

Where the claimed invariant concerns user/operator-visible behavior, include evidence through the public production command/path.

Helper-level tests remain useful but must not be presented as broader proof.

Do not add generic “every helper must have a caller” requirements merely to satisfy coverage aesthetics. Prove the specific contract-critical wiring instead.

## 14. Context and tool-output hygiene — `[GUIDE]`

Context is a scarce execution resource.

Prefer:
- targeted file/range inspection;
- focused search;
- targeted test selection;
- concise diff/status summaries;
- redirecting large logs to files and inspecting relevant excerpts.

Avoid:
- dumping entire large logs;
- repeatedly rereading the full reconciliation;
- rereading all roadmap files after every step;
- producing verbose narrative progress when a compact ledger update is sufficient.

If context becomes uncertain, follow `00_READ_FIRST.md` recovery protocol instead of relying on conversational memory.

## 15. Repository-change hygiene — `[RULE]`

Before destructive/adversarial reproduction:
- use disposable scratch copies outside canonical protected state where appropriate;
- preserve/record relevant pre-change hashes;
- avoid treating historical residue as a reference implementation unless provenance is trustworthy.

Do not mutate factual candidate authorities as part of implementation testing.

Do not silently rewrite prior evidence to make new results appear continuous. Supersede or regenerate evidence explicitly.

## 16. Plan and roadmap mutability — `[RULE]`

After user approval:
- `00_READ_FIRST.md`, `DESIRED_FINAL_STATE.md`, `GUIDANCE_INSTRUCTIONS_AND_RULES.md`, `DEFINITION_OF_DONE.md` and `FINAL_GOAL_COMMAND.md` are treated as stable control documents;
- `FINAL_EXECUTION_PLAN.md` is the approved preferred route;
- material route changes are normally recorded as `DEV-*` entries in the ledger rather than silently rewriting the plan;
- `EXECUTION_LEDGER.md` is expected to change continuously.

If a stable control document is actually wrong, stop treating that as an ordinary implementation decision and surface the required correction explicitly.

## 17. Execution-ledger discipline — `[RULE]`

The ledger is a compact state checkpoint, not a diary.

Keep:
- current phase/task;
- last verified checkpoint;
- linked DFS/DOD status;
- deliberate plan deviations;
- newly discovered issues and scope decision;
- exact current blockers;
- next action.

Do not copy:
- long tool logs;
- entire review findings;
- repeated architecture text;
- speculative future work.

Repository state outranks ledger state when they disagree.

## 18. Stop and escalation rules — `[HARD]`

*(This section is the single owner of terminal conditions. `FINAL_GOAL_COMMAND.md` restates them in compressed form because the Goal runtime may continue autonomously with no operator present; the two must stay consistent.)*

Legal terminal conditions for the implementation Goal are:

### `GO_FOR_TWO_JOB_SMOKE`
All mechanically applicable completion criteria are proven; remaining unknowns are genuinely user-owned or pilot-semantic.

### `BLOCKED_USER`
Progress requires a specific user-owned fact/action that cannot safely be inferred. Record the exact missing input.

### `BLOCKED_HARD_CONSTRAINT`
A demonstrated conflict between hard constraints or unavailable required target capability remains after at least two substantively different bounded approaches.

Do not stop merely because:
- compilation succeeds;
- existing tests pass;
- a report says PASS;
- a responsive Word process exists;
- further improvements are imaginable.

Do not continue merely because:
- an unrelated cleanup is available;
- a reviewer once suggested something;
- a metric/test count can be improved;
- a future hypothetical use case might benefit.

The goal is a finite mechanically trustworthy baseline, not endless perfection.
