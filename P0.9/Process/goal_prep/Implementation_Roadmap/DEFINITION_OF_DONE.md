# P0.9 Definition of Done

## 0. Purpose

This document defines the evidence required to prove that the P0.9 mechanical-finalization Goal is complete.

`[HARD]` Every criterion here is a proof threshold. `FINAL_EXECUTION_PLAN.md` may change route; it may not lower a threshold in this file.

Most criteria map one-to-one onto a `DFS-*` property. `DOD-07`, `DOD-10`, `DOD-23` and `DOD-25` are cross-cutting and are audited at their owning phase and again at final completion.

It tests **observable properties**, not whether the implementation copied the preferred mechanism in `FINAL_EXECUTION_PLAN.md`.

A plan mechanism may change without failing DoD if the desired property is still proven.

No criterion passes because:
- compilation succeeds;
- a helper test exists;
- a prior report says PASS;
- the historical test count is high;
- the implementation “looks correct.”

Evidence scope must match claim scope.

---

## 1. Status vocabulary

Use exactly:

- `PASS` — current evidence directly satisfies the criterion;
- `FAIL` — current evidence contradicts the criterion;
- `IN_PROGRESS` — accepted implementation/verification remains;
- `BLOCKED_USER` — only a specific user-owned fact/action prevents resolution;
- `DEFER_PILOT` — explicitly outside mechanical finalization and intentionally reserved for semantic/pilot evidence;
- `NOT_APPLICABLE` — criterion genuinely does not apply under the finalized architecture/environment.

Do not use `SKIP`, `WAIVED` or `GOOD_ENOUGH`.

Every non-PASS terminal status must state why it is legitimate.

---

## 2. Evidence classes

Evidence may include:

- **PUBLIC_CLI** — behavior exercised through the actual public command/operator path;
- **TARGET_WINDOWS** — reproduced on the intended Windows/Word environment;
- **UNIT_HELPER** — narrow helper/unit evidence; useful but never overclaimed;
- **STATIC_CODE** — unambiguous implementation-path inspection;
- **ARTIFACT_HASH** — retained immutable artifact/hash relation;
- **VISUAL_HUMAN** — human inspection of rendered document evidence;
- **USER_ACCOUNT** — user/account/provider facts that tooling cannot infer safely.

Prefer the strongest evidence class appropriate to the property.

---

## 3. DOD-00 — Core architecture preserved

**Maps:** DFS-00

PASS requires evidence that the repaired baseline still has:
- invariant core CV + letter;
- Bokmål semantic core;
- exactly three manual semantic stages;
- Stage-3 elasticity;
- human factual/submission authority;
- no deterministic model call, employer contact or submission;
- no runtime semantic quality judge;
- no hidden semantic orchestration/retry engine;
- render/PDF failure orthogonal to semantic validity.

Evidence:
- architecture/runtime configuration inspection;
- public-path smoke with synthetic jobs;
- repository search for prohibited branches/subsystems where relevant.

---

## 4. DOD-01 — Frozen-run immutability

**Maps:** DFS-01

### DOD-01A — Root metamorphism
Freeze a fresh synthetic run.

In disposable copies, mutate each maintained/root input category that could otherwise affect a run:
- schemas;
- relevant policies/stage instructions;
- settings;
- authorities/context/index sources as applicable;
- template/map/master;
- inbox/source-maintenance inputs.

PASS:
- existing run integrity/currentness/validation/context/finalization/render behavior remains governed by its frozen bytes;
- employer-visible output does not silently change because maintained roots changed.

### DOD-01B — Frozen self-tamper
Mutate one governing byte inside the run’s own frozen state.

PASS:
- integrity/current-work commands refuse or diagnose the compromised run appropriately;
- no authoritative new output is produced from the compromised frozen state.

### DOD-01C — Future-run visibility
Create a new freeze/child after an intentional maintained-root change.

PASS:
- the new run can see the intended maintained-root change;
- old run remains unaffected.

Evidence class: PUBLIC_CLI + ARTIFACT_HASH.

---

## 5. DOD-02 — Tool-owned mechanical binding

**Maps:** DFS-02

PASS requires:
- the context/submission workflow does not require human/model canonical-hash calculation;
- mechanically predetermined identity/binding fields are supplied/verified by tooling;
- semantic model output contract contains only fields the model can legitimately determine, except where an approved schema reason requires otherwise.

Audit representative Stage-1/2/3 schemas and context bundles.

Evidence: PUBLIC_CLI + STATIC_CODE.

---

## 6. DOD-03 — Current-at-birth semantic artifacts

**Maps:** DFS-03

### DOD-03A — stale handoff refusal
Prepare a downstream context/handoff, replace its current upstream, then submit work produced against the old context.

PASS:
- command refuses before archiving/replacing valid current work;
- prior current/history hashes remain unchanged.

### DOD-03B — wrong binding refusal
Return intentionally wrong mechanically predetermined identity/upstream information where the interface still accepts such fields.

PASS:
- refused before persistence, or ignored only through a design that still proves current context mechanically.

### DOD-03C — correct handoff succeeds
Submit the exact current documented handoff.

PASS:
- accepted artifact is immediately derived `VALID/current`, not stale-at-birth.

Evidence: PUBLIC_CLI + ARTIFACT_HASH.

---

## 7. DOD-04 — Closed-loop semantic handoff

**Maps:** DFS-16, DFS-02

Using synthetic jobs, prove Stage 1, Stage 2, Stage 3 and review-only recovery can each be completed from the context shown to the operator/model and the documented command.

PASS requires:
- exact relevant inputs identified;
- role/surface information displayed at the scope actually configured;
- output contract clear;
- exact submission action present;
- no manual internal hash derivation or hidden reverse-engineering step;
- stale return path rejected safely.

Evidence: PUBLIC_CLI.

---

## 8. DOD-05 — Action currentness

**Maps:** DFS-04

Create stale descendants by replacing upstream semantic artifacts.

PASS:
- `context` for a downstream stale stage does not prepare invalid work;
- `finalize` cannot finalize stale/non-current final;
- authoritative `render` cannot consume stale/non-current final;
- continuation/next reflects actual remaining work;
- diagnostics can still explain the state.

Triage labels must not become accidental currentness gates unless architecture explicitly requires them.

Evidence: PUBLIC_CLI.

---

## 9. DOD-06 — Stage-3 completion and review-only recovery

**Maps:** DFS-05

### Normal pair
Stage 3 returns required final/review result.

PASS:
- pair is validated coherently before new current state becomes visible.

### Invalid half
Make final valid/review invalid, then the reverse.

PASS:
- no half-new Stage-3 current state displaces a previously valid coherent state.

### Interrupted recovery
Leave a current valid final with missing/invalid review.

PASS:
- `next`/context routes the same job to review-only completion;
- no unnecessary final regeneration/finalization is required.

Evidence: PUBLIC_CLI.

---

## 10. DOD-07 — Deterministic finalization and date validity

**Maps:** DFS-03, DFS-04

PASS:
- model cannot assign canonical document date/finalization state through semantic payload;
- deterministic finalize accepts canonical ISO date only;
- invalid `dd.mm.yyyy` or malformed date is rejected cleanly before render/output mutation;
- finalize is idempotent under the approved rule;
- pure rerender preserves canonical date;
- semantic final hash remains unchanged by finalization/date where architecture requires.

Evidence: PUBLIC_CLI + ARTIFACT_HASH.

---

## 11. DOD-08 — Failure scope and batch containment

**Maps:** DFS-06

Use at least two synthetic CORE jobs.

### Job-local malformed artifact
Corrupt one job’s current semantic JSON.

PASS:
- status/validate/next produce structured information for the damaged job;
- healthy job remains diagnosable/actionable;
- command returns appropriate nonzero aggregate status without raw whole-run crash.

### Job-local render failure
Trigger one job-specific render/build exception.

PASS:
- healthy job completes where shared state remains safe;
- failed job does not leave misleading partial current presentation.

### Run/environment-global failure
Simulate or directly test a shared failure class where safe continuation cannot be established.

PASS:
- command aborts at broader scope rather than pretending the condition is job-local.

Evidence: PUBLIC_CLI.

---

## 12. DOD-09 — Failure-axis and retry ownership

**Maps:** DFS-07

PASS requires:
- read-only validation/preflight diagnostics do not persist semantic-production failure merely because they found bad state;
- render/DOCX/PDF failure remains render-only;
- real failed semantic-production attempts reach the intended failure/recovery mechanism;
- successful owning-stage replacement clears/supersedes relevant failure state;
- `BLOCKED_MANUAL` becomes reachable only under the approved bounded rule.

### Required retry distinction
Prove the implementation does not collapse:
1. the one same-session mechanical correction allowance for structurally invalid model output; and
2. semantic/manual retry/restart ownership after genuine production failure.

Evidence: PUBLIC_CLI + STATIC_CODE.

---

## 13. DOD-10 — EXCEPTION containment

**Maps:** DFS-00, DFS-06

PASS:
- normal core stage-submit/finalize/render workflow refuses EXCEPTION jobs clearly;
- EXCEPTION representation remains inert;
- no second automated exception workflow is introduced.

Evidence: PUBLIC_CLI.

---

## 14. DOD-11 — Verified render receipt

**Maps:** DFS-08

After a valid render, independently mutate one thing at a time:

- current semantic final;
- document date;
- consumed immutable template/map/master input;
- relevant render configuration;
- one output byte;
- delete one output;
- alter receipt binding.

PASS:
- status immediately stops surfacing mismatched output as current;
- semantic validity is not incorrectly changed by receipt failure;
- rerender can recover safely.

### Review orthogonality
Replace only review/triage content while leaving current final/date/render inputs/output bytes unchanged.

PASS:
- receipt/render currentness behaves according to the explicitly approved architecture;
- under the draft intended model, unchanged employer bytes remain current even though a current review is required before initiating a new render.

Evidence: PUBLIC_CLI + ARTIFACT_HASH.

---

## 15. DOD-12 — Output-generation coherence and no-clobber

**Maps:** DFS-09, DFS-10

### Degraded rerender
Start from valid DOCX+PDF, then force new PDF generation failure.

PASS:
- stale old pipeline PDF cannot remain presented as if current for a newer DOCX generation.

### Human DOCX edit
Modify current DOCX outside pipeline, then rerender.

PASS:
- human DOCX is preserved;
- corresponding newly generated pipeline PDF does not advance alone to another semantic generation;
- operator receives truthful no-clobber information.

### Ownership recovery
After a transient failed/degraded attempt, rerun.

PASS:
- pipeline does not misclassify its own unchanged prior output as foreign solely because the latest attempt lacked complete receipt state.

Evidence: PUBLIC_CLI + ARTIFACT_HASH.

---

## 16. DOD-13 — Safe write boundaries

**Maps:** DFS-11

Test:
- canonical run/generated destination;
- explicit outside-repository human export;
- `../` traversal;
- protected repository target such as authorities/templates;
- symlink/junction/reparse escape.

PASS:
- canonical writes remain in approved roots;
- protected/traversal/reparse destinations are refused;
- allowed external human export is non-authoritative and cannot alter current receipt/status;
- explicit source-maintenance tooling remains able to update its maintained source targets when deliberately invoked.

Evidence: PUBLIC_CLI + TARGET_WINDOWS where reparse behavior is platform-specific.

---

## 17. DOD-14 — Branch integrity and semantic reuse

**Maps:** DFS-12

### Parent compromise
Tamper parent frozen governing input or vacancy source.

PASS:
- branch refuses before visible canonical child side effects.

### Parent immutability
Hash parent tree before/after successful branch.

PASS:
- parent unchanged.

### Unchanged governing inputs
Branch valid complete parent without semantic governing changes.

PASS:
- child becomes internally current/valid without unnecessary semantic regeneration.

### Changed governing input
Change a content-governing stage/policy/schema input according to finalized branch semantics.

PASS:
- correct earliest affected stage and descendants become non-current;
- unaffected predecessors remain valid.

### Interrupted branch
Interrupt before canonical exposure.

PASS:
- no canonical partial child.

### If semantic hash excludes run identity
Prove explicitly:
- same semantic hash across runs is possible where intended;
- wrong `run_id/job_id` still fails identity validation.

Evidence: PUBLIC_CLI + ARTIFACT_HASH.

---

## 18. DOD-15 — Revision/amendment coherence

**Maps:** DFS-19

If amendments/revision changes were made, PASS requires:

- exact affected architecture IDs/files recorded;
- trigger/evidence and old/new rule recorded;
- user authority recorded;
- exact prior normative authority preserved;
- active revision declarations internally consistent;
- old frozen run behavior/support/refusal is explicit and tested;
- unrelated format-version identifiers were not blindly changed;
- no old run is silently interpreted under changed semantics.

Evidence: STATIC_CODE + PUBLIC_CLI + ARTIFACT_HASH/document hashes.

If no revision change was needed, classify only truly non-applicable subchecks `NOT_APPLICABLE`; architecture-amendment governance still must be coherent.

---

## 19. DOD-16 — Target-Windows Word/path reliability

**Maps:** DFS-13

On target Windows/Word environment:

### Realistic long names
Use a realistic worst-case employer/title/path depth.

PASS:
- DOCX and expected PDFs complete through the baseline Word path;
- human-facing final names remain readable.

### Forced timeout with human Word open
Open a real human Word session, then force converter timeout.

PASS:
- human session survives;
- diagnostic truthfully states cleanup outcome;
- automation process is killed only when exact ownership was safely established;
- otherwise no unsafe kill occurs and operator recovery information is truthful.

Evidence: TARGET_WINDOWS.

---

## 20. DOD-17 — Template/document integrity

**Maps:** DFS-14

### Point-of-use contract
Mutate a disposable frozen master to contain:
- unknown control;
- missing required control;
- duplicate unsafe control.

PASS:
- authoritative render refuses locally before employer document generation.

### Maintained repair reproducibility
Run template-preparation/check tooling.

PASS:
- expected control inventory preserved;
- Word-compatible repaired properties remain;
- untouched OOXML package parts retain required byte-safe behavior;
- font/glyph target remains correct.

Evidence: PUBLIC_CLI/STATIC_CODE + TARGET_WINDOWS.

---

## 21. DOD-18 — Visual document QA

**Maps:** DFS-15

Render sparse, normal and dense representative fixtures through target Word/PDF.

Human visual inspection must confirm:
- no known forced near-empty/blank page;
- no clipping;
- no unintended blank pages;
- no missing Norwegian glyphs;
- sensible heading/section flow;
- no obvious deterministic layout defect likely to contaminate semantic-quality measurement.

Text extraction/parseability checks must also pass.

This criterion requires `VISUAL_HUMAN` evidence. Codex may prepare evidence but must not self-certify a human-only visual judgment if the execution surface cannot genuinely provide it.

---

## 22. DOD-19 — Operator/context readiness and GATE-10

**Maps:** DFS-16, DFS-18

PASS requires:
- context surfaces exact current stage/inputs/output contract/submission action;
- queue/status surfaces actionable current reasons/limitations without becoming authoritative state;
- configured capability-role mapping is usable for the next real smoke;
- no invented product mode exists solely to distinguish test vs real mapping.

Account-specific GATE-10 facts require `USER_ACCOUNT` evidence:
- chosen SOL_CLASS/TERRA_CLASS surfaces;
- file-access behavior;
- relevant privacy/retention/training/account settings.

If those facts are not supplied, status is `BLOCKED_USER`, not inferred PASS.

---

## 23. DOD-20 — Pilot log scaffold

**Maps:** DFS-18

PASS:
- human-owned UTF-8 semicolon-delimited pilot log/template exists;
- fields cover the approved measurement set;
- runtime does not consume it as control state;
- documentation explains human ownership.

Evidence: STATIC_CODE/file inspection.

---

## 24. DOD-21 — Public-path assurance

**Maps:** DFS-17

For every Critical/High material boundary accepted in the final plan, confirm at least one test/evidence path exercises the actual public production path where that is the claimed scope.

PASS:
- helper-only tests are labeled helper-only;
- traceability does not equate test-name existence with production behavior;
- no generic caller-count test substitutes for proving the boundary itself.

Evidence: test mapping + PUBLIC_CLI.

---

## 25. DOD-22 — Evidence re-derivability and report truthfulness

**Maps:** DFS-17

PASS requires:
- fresh synthetic vertical slice generated from repaired tree;
- evidence references a retained run/artifacts or an equally reproducible immutable evidence set;
- relevant gate reports regenerated at their true scope;
- builder/finalization report claims only evidence actually present;
- stale/orphan report claims are removed or explicitly superseded after replacement evidence verifies;
- artifact/hash links can be independently recomputed.

Evidence: ARTIFACT_HASH + PUBLIC_CLI + retained reports.

---

## 26. DOD-23 — Anti-regression audit — `[HARD]`

**Maps:** `AR-01` … `AR-20` in `GUIDANCE_INSTRUCTIONS_AND_RULES.md` §10

That register is the single owner of the protected set. This criterion audits it by ID and deliberately
does not restate it; if the two ever disagree, §10 wins.

PASS requires, for every `AR-*`:
- a statement of how the finalized implementation still satisfies the **property**;
- evidence at the scope the property claims (target-Windows evidence where the property is environmental);
- for any `AR-*` whose implementing mechanism changed during finalization, explicit evidence that the
  property survived the change.

Do not require a specific implementation technology merely because an `AR-*` description once named one.
`AR-16` and `AR-20` are properties about serialization safety and process ownership respectively, not
about a dependency list or a cleanup technique.

Evidence: targeted public-path tests + active-tree inspection + TARGET_WINDOWS where relevant.

---

## 27. DOD-24 — Repository/distribution hygiene

**Maps:** DFS-17

PASS:
- nested `Build.zip` or equivalent distribution residue removed from active source tree;
- ignore rules exclude appropriate local environment/cache artifacts;
- distribution archive, if created, is generated outside source tree from explicit intended contents;
- protected candidate inputs are not duplicated into accidental packaging residue.

Evidence: file inventory/hash inspection.

---

## 28. DOD-25 — Final mechanical completion audit

Before `GO_FOR_TWO_JOB_SMOKE`:

1. run full deterministic suite on the intended target environment;
2. run all applicable DOD criteria above;
3. run final `/review`;
4. inspect repository diff/state;
5. inspect final execution ledger and all `DEV-*` / `DISC-*`;
6. confirm every applicable criterion is `PASS`;
7. resolve every `FAIL` and `IN_PROGRESS`;
8. classify only genuinely user-owned facts as `BLOCKED_USER`;
9. classify only approved semantic/pilot questions `DEFER_PILOT`;
10. confirm no known material mechanical defect remains inside roadmap scope.

### Terminal decision

`GO_FOR_TWO_JOB_SMOKE` is allowed only when:
- all mechanically resolvable criteria are PASS;
- any required user/account evidence for actually starting the smoke is present;
- remaining uncertainties are deliberately pilot-semantic, not known mechanics.

Otherwise stop at the exact legitimate blocking status.

The real two-job smoke is not part of this DoD.
