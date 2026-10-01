# P0.9 Final Execution Plan

## 0. Status, interpretation and strictness

This is the **preferred execution route**, not the highest authority in the finalization package.

Its role is to propose a coherent route from the current P0.9 Build to the state defined in `DESIRED_FINAL_STATE.md` and proven by `DEFINITION_OF_DONE.md`.

This plan uses the normative-force key defined in `00_READ_FIRST.md` §2. Section headings below use
their own long-form labels; they map onto the key exactly as follows:

| Heading in this plan | Force | Meaning |
|---|---|---|
| **REQUIRED OUTCOME** | `[HARD]` | The linked `DFS-*` / `DOD-*` property must be achieved. This plan neither owns nor may weaken it. |
| **PREFERRED MECHANISM** | `[ROUTE]` | The mechanism currently judged simplest and safest. Replace it deliberately when direct code evidence shows a smaller or safer route to the same outcome, and record a `DEV-*`. |
| **OPTION / ADJUDICATE** | `[OPTION]` | Genuinely unresolved. Decide it from current consumers and evidence, then record the decision. |
| **DEFER** | `[RULE]` | Outside this baseline unless new direct evidence satisfies the scope-admission rule. |
| unlabelled prose | `[GUIDE]` | Context and reasoning. Useful, not binding. |

`[HARD]` No implementation mechanism in this plan becomes architecture merely because it appears here.
Everything under **PREFERRED MECHANISM** is a starting point, and choosing better is the intended
behaviour — not a deviation to apologize for.

The execution target is `GO_FOR_TWO_JOB_SMOKE`. The real semantic smoke is a separate phase.

---

## 1. Starting-state capsule

The current P0.9 implementation is mechanically substantial and has a strong underlying product architecture, but multiple public-path integration boundaries do not yet enforce the guarantees implied by its individual helpers/tests.

The most important confirmed families are:

1. run snapshots exist but some consumers still read maintained/root schemas/templates/settings/policy-like inputs;
2. manual semantic handoff does not currently form a closed loop from `context` to valid acceptance;
3. stale/invalid semantic state can remain actionable;
4. render reports can look current while binding unrelated semantic/output bytes;
5. per-component DOCX/PDF ownership can split generations;
6. branch reuse/publication can create internally stale or partially rebound children;
7. production failure/continuation helpers are not consistently connected to the operator path;
8. exception containment is not reliably scoped by job vs run/environment;
9. Word staging/timeout/template/layout behavior still contains known target-machine defects;
10. evidence reports/tests overstate some public-path guarantees.

The evidence register is `P0.9/Process/plan_prep/P0.9_Final_Multi_Model_Review_Reconciliation.md` (`MMR-*` rows, `RC-*` root causes, inline `OPUS_META_ADD` blocks). This plan maps accepted work to `DFS-*`/`DOD-*` IDs rather than duplicating reproductions. `[RULE]` Open it per finding, not in bulk.

---

## 2. Execution disposition map

This table is execution-oriented. Evidence and reviewer provenance remain in the reconciliation.

| Finding group | Draft disposition | Primary DFS | Planned phase |
|---|---|---:|---|
| MMR-001/002/003 | FIX | DFS-01, DFS-17 | P1 |
| MMR-004/006/007/015/018/031/035 | FIX | DFS-02/03/04/05/16 | P2 |
| MMR-008/017/044 + RC-9 | FIX | DFS-06/07 | P3 |
| MMR-009 | AMEND/clarify if still needed after implementation review | DFS-07/19 | P0/P3 |
| MMR-005/019/020/021/022/028/029/043 | FIX | DFS-08/09/10/11/14 | P4 |
| MMR-025 | IMPROVE documentation; adoption subsystem DEFER | DFS-08/09 | P4 |
| MMR-026/027 | AMEND/clarify | DFS-08/11/19 | P0/P4 |
| MMR-010/011/012/013/016 | FIX | DFS-04/12 | P5 |
| MMR-014 | DEFER | DFS-12 | — |
| MMR-023/030 | FIX | DFS-13/15 | P6 |
| MMR-024/040 | IMPROVE | DFS-13 | P6 |
| MMR-032/033/034/042/047 | DEFER/PILOT | DFS-18/non-goals | — |
| MMR-036/037/038 | FIX/IMPROVE before smoke | DFS-16/18 | P7 |
| MMR-039/049 | KEEP | DFS-18/00 | throughout |
| MMR-041 | targeted fix only where current consumers matter; broad cleanup DEFER | DFS-01 | P1 |
| MMR-045/046/048 | FIX/IMPROVE | DFS-17 | P8 |

Any change to this disposition set during implementation must be evidence-backed and recorded as a material `DEV-*`.

---

## 2.5 Adjudicated decisions (`D-*`)

These were open in earlier drafts and in the original Codex plan. They are resolved here against the
frozen architecture and the current Build, with the supporting evidence stated so you do not have to
re-derive it. Each carries its own force. `[OPTION]` items are deliberately still yours to decide.

### D-01 — Architecture revision strategy — `[RULE]`

**Resolved:** do **not** perform a blanket `0.9.0 → 0.9.1` bump.

Verified field inventory in the current Build:

| Field | Location | Kind |
|---|---|---|
| `SPEC_REVISION`, `SCHEMA_REVISION` | `runtime/jobbsok/__init__.py` → written into every manifest by `freeze` and `branch` | architecture revision |
| `spec_revision`, `schema_revision` | `schemas/manifest.schema.json`, both **`const: "0.9.0"`** | architecture revision, exactly pinned |
| `map_version` | `schemas/baseline_map.schema.json`, `const: "0.9.0"` | **artifact format**, unrelated |
| `index_version` | `schemas/evidence_index.schema.json`, `const: "0.9.0"` | **artifact format**, unrelated |
| `[spec] revision`, `schema_revision` | `policy/settings.toml` | present but **not** in `settings.snapshot()`; currently consumed by nothing |

`[HARD]` Never change `map_version` or `index_version` as a side effect of an architecture revision.
They version artifact formats, not normative semantics.

`[RULE]` Bump the architecture revision **only if** an amendment actually changes normative semantics.
If it does, the `const` pins in `manifest.schema.json` must accept the set of revisions the runtime
genuinely supports, the exact prior `0.9.0` architecture files must remain byte-preserved, and runtime
behaviour toward an older frozen revision must be explicit and tested — supported under its own frozen
semantics, or refused with a clear diagnostic. Silent reinterpretation is forbidden.

`[HARD]` **Sequencing:** any revision change must land **after** Phase 1. Until run-bound schema reads
resolve from the run's own frozen snapshot, a live `const` bump instantly invalidates every existing
frozen run. Do not reorder these.

### D-02 — Binding invariant, not a named token — `[RULE]` + `[OPTION]`

`[RULE]` The normative requirement is the property: tooling owns mechanically derivable binding
metadata, and a candidate is refused before it displaces valid work unless it was produced against the
exact current governing state. That is `DFS-02` + `DFS-03`.

`[OPTION]` Whether that is implemented as a token, a digest, a re-derived envelope compared field by
field, or context-supplied values verified at submit is yours. `[HARD]` Do not write a named token
format into architecture.

`[EVIDENCE]` The gap is closed-loop, not cosmetic: `context --stage 2` emits `binding` without
`strategy_sha256` while `schemas/package.schema.json` requires it for `STAGE2_DRAFT`; `P0.9/Build/policy/RUNBOOK.md` has
no step to obtain it; and `stage-submit` accepts a wrong value, archiving the previously valid draft.
The documented manual workflow therefore cannot currently produce a non-stale draft.

### D-03 — Review is a render precondition, not part of receipt identity — `[RULE]`

**Resolved from the frozen architecture; no amendment is required.**

`[EVIDENCE]` Spec §16.2 `DEC-21` step 1 requires the finalizer to *"validate current final
package/review and document date"*. Spec §7.2 lists the render report as binding *"the current final,
final document date, baseline, template and render configuration"* — review is absent. Current
`runtime/jobbsok/render.py` contains **zero** references to review, so the precondition is simply
unimplemented.

`[RULE]` Therefore: a current valid review **is** required to initiate an authoritative render, and
review content is **not** part of receipt identity. Replacing only review must not invalidate unchanged
employer-document bytes. Both halves are existing frozen semantics — implement them, do not amend them.

### D-04 — Failure scope, not exception class — `[RULE]`

`[HARD]` Do not implement a blanket `except Exception: continue`. Never treat `KeyboardInterrupt` or
`SystemExit` as a job failure.

`[RULE]` Classify each multi-job boundary failure as artifact-local, job-local, run-global or
environment-global, and continue only while shared state is known-safe. Preserving trustworthy state
outranks maximizing continuation.

`[EVIDENCE]` The current barrier catches `JobbsokError` only. A `dd.mm.yyyy` document date — the
ordinary Norwegian format — passes `finalize` and `validate`, then aborts a whole multi-job render with
a raw `ValueError`, leaving one job with a CV, no letter and no receipt, and later jobs unrendered. A
malformed current artifact additionally disables `status` and `next` for the entire run, i.e. it
disables the recovery path itself.

### D-05 — Two bounded-correction concepts stay distinct — `[HARD]`

`[EVIDENCE]` They are separately frozen: Spec §15.1 (one visible same-session **mechanical correction**
of structurally invalid model output) and Spec §15.2 `DEC-36` (`retry_start_stages`, **semantic**
restart scaffolding). Both exist in `policy/settings.toml` as `mechanical_correction_attempts` and
`retry_start_stages`.

`[HARD]` Do not collapse them into one retry counter or one state object. A refused stale precondition
that left valid current work untouched consumes neither allowance.

### D-06 — Write safety must not break source maintenance — `[HARD]`

`[EVIDENCE]` `runtime/tools/prepare_masters.py` deliberately writes into `layout.templates`, a protected
root, and archives pristine originals under `evidence/gates/GATE-02/`. A naive protected-root guard
wired into a shared write path would break the only reproducible master-repair mechanism (`AR-02`).

`[RULE]` Distinguish **run-production/model-controlled writes** (confined to approved writable roots;
traversal, reparse and protected-root escape refused) from **explicit human-invoked source-maintenance
tooling** (may update its maintained targets between runs). An explicit human export may resolve outside
the repository and is non-authoritative; it may not point back into a protected repository root.

### D-07 — Word cleanup: truthful always, kill only on proven ownership — `[HARD]` + `[OPTION]`

`[HARD]` The diagnostic must state what actually happened. The current message claims the Word process
was terminated when only the PowerShell host was killed; measurably, one timed-out render leaves two
orphaned automation processes that a later successful conversion does not reap.

`[HARD]` Never terminate a process that is not provably owned by this run (`AR-20`).

`[OPTION]` Automatic cleanup is permitted only if you establish ownership by a mechanism that cannot
misattribute under concurrent Word activity. **Before/after PID differencing does not meet that bar** —
it is a plausible heuristic, not proof, and a concurrently launched instance would be misattributed.
This explicitly overrides an earlier meta-review suggestion that treated PID differencing as
ownership-proven. If you cannot establish ownership, kill nothing and report the surviving process and
the operator action truthfully. That is a fully acceptable outcome.

### D-08 — OOXML: protect the property, do not ban a library — `[RULE]`

`AR-16` is the governing statement. Preserve byte-safe untouched package parts, the master's own
namespace/root declarations, and target-Word openability. Any serialization change requires target-Word
evidence that the result still opens.

`[EVIDENCE]` The historical failure was a round-trip artifact in `docProps/core.xml` that left the
`dcterms` prefix unbound — Word rejected the package, LibreOffice tolerated it, and the P0.7
LibreOffice-only verification never saw it. The risk is the transformation, not the dependency list.

### D-09 — Semantic-hash neutrality for run identity — `[OPTION]`, strong prior to adopt

`[EVIDENCE]` Production consumers of `artifacts.artifact_hash` are exactly three, and all three are
**intra-run** comparisons:

1. `artifacts.evaluate_staleness` — compares a recorded upstream hash to the current upstream;
2. `render._build_report` — records `final_package_sha256` in the receipt;
3. `status._derive_job` — compares the review binding to the current final.

(`runtime/tools/make_fixtures.py` also calls it, but it *generates* the same values and stays consistent
either way.) None of the three depends on run identity being part of semantic content identity, and
`validate._check_identity` already rejects a wrong `run_id`/`job_id`/employer/title independently.

`[OPTION]` Excluding only `binding.run_id` and `binding.manifest_sha256` from `artifact_hash` would make
a child rebind hash-neutral and remove the need for a downstream re-stamping cascade. Adopt it only
after you confirm empirically that an artifact carrying the wrong run/job is still rejected. If that
proof fails, use a bounded topological rebind instead. `[HARD]` Either way, no lineage or dependency
engine.

### D-10 — Goal boundary stops at `GO_FOR_TWO_JOB_SMOKE` — `[HARD]`

`INV-08` keeps engineering conformance, product baseline and causal experiments in separate evidence
loops. Executing real semantic jobs inside this Goal would merge loop A with loop B and destroy the
clean baseline. This Goal prepares and authorizes the smoke; it does not run it.


---

## 3. Phase 0 — Governance, amendment and revision preparation

### Objective
Resolve only the normative ambiguities that must be settled before code changes depend on them.

**Primary DFS:** DFS-07, DFS-08, DFS-11, DFS-19  
**Primary DOD:** DOD-07, DOD-08, DOD-11, DOD-19

### REQUIRED OUTCOMES

1. Mechanical binding ownership must be clear enough that models are not responsible for mechanically predetermined lineage/currentness values.
2. Render-report semantics must be explicit enough that status cannot treat an unverified receipt as current.
3. Failure-axis ownership must preserve semantic-production vs render separation.
4. Human external export must not legalize writes into protected in-repository roots.
5. Any architecture revision/amendment must preserve exact prior normative authority and define what happens when runtime encounters older frozen revisions.

### PREFERRED MECHANISM

Use **narrow amendment wording that freezes semantics, not incidental mechanism**.

Recommended amendment concepts:

#### A-01 — Deterministic binding ownership
Architecture should require deterministic tooling to own/verify mechanically derivable binding metadata and reject stale mechanical context before replacing current work.

**Do not require a named “handoff token” in architecture.** A token/digest may be the implementation mechanism, but the normative rule is the closed-loop/current-at-birth property.

#### A-02 — Verified render receipt
A render record is current only when it verifies the current render-relevant semantic final/date, the actual consumed immutable render inputs/configuration and actual output bytes.

**Important:** current review/triage may be an authorization precondition to initiate render, but pure review replacement must not automatically make unchanged employer-document bytes stale unless the architecture deliberately decides review contents are render identity.

#### A-03 — Failure-axis ownership
`FAILED/BLOCKED_MANUAL` represents semantic-production attempt/recovery state; read-only diagnostics and render/conversion failure stay outside that axis.

#### A-04 — Canonical writes vs explicit human export
Canonical production writes stay inside approved writable roots and reject traversal/reparse/protected-root escape. Explicit human export outside the repository may be non-authoritative.

**Carve-out:** explicit human-invoked source-maintenance tooling (for example maintained template preparation) is not a run-production write and must not be accidentally prohibited.

### Revision strategy — resolved in `D-01`

The earlier Codex plan proposed a blanket move to `0.9.1`. `D-01` rejects that and fixes the field inventory and the Phase-1 sequencing constraint. The remaining work here is to execute `D-01`, not to re-open it.

Before choosing a revision strategy:

1. inventory all revision/version consumers;
2. distinguish architecture revision from unrelated format/schema-version fields;
3. preserve the exact prior 0.9.0 normative files if semantics are amended;
4. decide whether old synthetic 0.9.0 runs are:
   - supported under their frozen semantics,
   - explicitly unsupported/refused by the new runtime,
   - or deliberately migrated through a bounded mechanism;
5. ensure no old run is silently interpreted as if it were born under amended semantics.

Prefer the smallest coherent strategy. Do not add a compatibility framework merely because multiple revisions exist.

### Exit
Normative decisions required by later phases are explicit; prior authority remains reconstructable; no code is changed merely to satisfy a version label.

---

## 4. Phase 1 — Frozen assets and content-governing policy resolution

### Objective
Make frozen-run behavior genuinely independent of maintained/root inputs after freeze.

**Primary DFS:** DFS-01, DFS-17  
**Primary DOD:** DOD-01, DOD-17

### REQUIRED OUTCOME

Every content-affecting run-bound read used by validation, context, currentness and render resolves from frozen run state or an immutable derivative of it.

### PREFERRED MECHANISM

Introduce one small shared resolver/value object or equivalent boundary in existing runtime code rather than repeating path selection in every caller.

It should cover only assets that are actually run-governing, such as:
- schemas used for the run’s semantic artifacts;
- template/map/master bytes consumed by render;
- stage instructions/shared writing policy that materially governs semantic artifacts;
- consumed semantic settings/role mappings where run-frozen semantics require them.

Root sources remain valid for:
- preflight;
- source maintenance;
- new freeze;
- deliberate child intake.

### Stage-policy binding

Define a deterministic digest/envelope over **actual content-governing frozen inputs**, not every config file in the repository.

The digest should be reusable by:
- semantic handoff/current-at-birth verification;
- branch governing-input comparison;
- evidence/receipt provenance where appropriate.

Do not build a dependency graph.

### Soft-threshold handling

If a setting only drives non-failing warnings/presentation and does not govern semantic acceptance/currentness, do not inflate it into architecture-critical state merely to obtain perfect hashing symmetry.

### Exit evidence

- old-run root metamorphism proves maintained/root schema/template/policy/settings edits cannot change the existing frozen run;
- tampering with the run’s own frozen governing byte is detected;
- new freeze/child can still intentionally see maintained-root changes.

---

## 5. Phase 2 — Closed-loop semantic handoff and action currentness

### Objective
Make the documented manual Stage-1/2/3 path mechanically completable without manual canonical metadata construction and without stale-at-birth artifacts.

**Primary DFS:** DFS-02, DFS-03, DFS-04, DFS-05, DFS-16  
**Primary DOD:** DOD-02, DOD-03, DOD-04, DOD-05

### REQUIRED OUTCOMES

- context supplies every mechanically predetermined value needed for a valid return path;
- stale/wrong returned work is refused before current/history mutation;
- successful accepted work is immediately current;
- one currentness/eligibility definition governs downstream actions;
- interrupted Stage 3 can resume review-only where appropriate.

### PREFERRED MECHANISM — tool-owned semantic envelope

At context time, tooling prepares a mechanically bound handoff representation covering at least:
- run/job/stage/mode identity;
- applicable frozen policy digest;
- required current upstream identity/hash;
- any fixed mechanically predetermined artifact-role/source-stage values.

The model should author only the semantic payload it genuinely controls.

At submission:
1. resolve the current expected mechanical envelope from disk;
2. reject stale/wrong context before archiving/replacing anything;
3. reject model-provided mechanical keys that tooling owns, or ignore them only if doing so cannot conceal misuse;
4. insert/stamp canonical mechanical metadata in memory;
5. validate the complete artifact;
6. commit only after all required checks pass.

### Handoff token — see `D-02` (`[OPTION]`)

A cryptographic/canonical token is one possible compact stale-context proof.

Use it only if it materially simplifies safe current-context verification. The desired state does not require the token as a named public protocol.

### Tool-owned fixed fields

Audit all semantic schemas for fields whose values are predetermined rather than semantic.

Likely candidates include:
- `binding`;
- `artifact_role`;
- `source_stage`;
- finalization/date state;
- fixed protocol constants that the stage cannot legitimately choose.

Move such fields out of model ownership where doing so reduces invalid combinations without taking semantic judgment away from the model.

Do not mechanically move fields that actually encode semantic decisions.

### Shared action-currentness predicate

Use one fixed stage-chain/currentness implementation from all relevant public actions:
- status derivation;
- next/continuation;
- context;
- stage submission;
- finalization;
- render precondition.

This should be a small fixed P0.9 stage table, not a generalized workflow engine.

### Stage 3

Support:
- normal final+review completion coherently;
- review-only completion when a valid current final exists and review is missing/invalid.

Atomicity requirement:
an invalid final/review candidate must not leave half of the new pair current.

### Deterministic finalization

Final document date is tooling-owned.
Accept only valid canonical date input; semantic hash remains independent of finalization/date.

### Stage-2 factual ceiling wording

Correct the prompt/policy so factual authorities remain the claim ceiling; strategy-recorded ceilings are advisory and correctable, never elevated above source authority.

### Exit
All three semantic stages and review-only recovery can complete through documented public commands with no manual hash calculation and no stale-at-birth state.

---

## 6. Phase 3 — Failure scope, continuation and retry ownership

### Objective
Make failures diagnostically honest, correctly scoped and recoverable without collapsing distinct retry/failure concepts.

**Primary DFS:** DFS-06, DFS-07  
**Primary DOD:** DOD-06, DOD-07

### REQUIRED OUTCOMES

- job-local failures do not unnecessarily kill healthy jobs;
- run/environment-global uncertainty aborts at the correct scope;
- malformed state yields structured diagnostics rather than disabling recovery commands;
- semantic-production failure records are actually reachable through normal production paths;
- render failure never becomes semantic production failure;
- EXCEPTION jobs remain inert to core semantic workflow.

### PREFERRED MECHANISM — explicit failure scope

Do **not** implement “catch every `Exception` and continue” as a universal rule.

At each multi-job boundary classify whether an error is safely:
- artifact-local;
- job-local;
- run-global;
- environment-global.

Known job-local failures should become structured per-job diagnostics and allow safe continuation.

Unexpected exceptions may continue only when shared/run state remains known-safe. Otherwise abort cleanly.

Never catch `KeyboardInterrupt`/`SystemExit` as job failures.

### Partial-output safety

A document-build exception must not leave one newly promoted component looking current while its paired output was never completed.

Stage/prepare work before promotion as needed to preserve coherent current presentation.

### Semantic failure wiring

Wire the existing failure/recovery mechanism to **actual semantic-production attempts** only.

A refused stale/wrong precondition that leaves current good work untouched should not consume semantic retry allowance.

### REQUIRED DISTINCTION — two bounded-correction concepts

Preserve the distinction between:
1. the architecture’s one same-session **mechanical correction** allowance for malformed/structurally invalid model output; and
2. semantic/manual retry/restart ownership after genuine production failure or user-approved retry.

Do not collapse these into one generic retry counter/state.

### EXCEPTION jobs

Core stage-submit/finalize paths should refuse EXCEPTION jobs early and clearly.
Do not create a second automated exception workflow.

### Exit
Malformed one-job state remains diagnosable; healthy jobs continue where safe; retry/failure semantics remain bounded and orthogonal.

---

## 7. Phase 4 — Verified render receipts, coherent outputs and safe writes

### Objective
Ensure current employer output corresponds to the current eligible semantic generation and actual bytes.

**Primary DFS:** DFS-08, DFS-09, DFS-10, DFS-11, DFS-14  
**Primary DOD:** DOD-08, DOD-09, DOD-10, DOD-11, DOD-14

### REQUIRED OUTCOMES

- render state derives from verifiable reality, not report presence;
- stale/unreceipted output cannot masquerade current;
- DOCX/PDF siblings cannot split semantic generations;
- human edits remain protected;
- exact frozen template contract is enforced at render use;
- protected/reparse/traversal write escapes are refused.

### PREFERRED MECHANISM — verified receipt

Keep render outside the semantic-artifact registry.

A receipt should record/verify only render-relevant identity, including:
- current semantic final identity/hash;
- document date;
- actual consumed frozen template/map/master/config hashes;
- output path/hash/size per current component;
- converter/render configuration necessary to explain bytes.

Current review may be required as an authorization precondition to start render, but **do not bind receipt identity to review contents unless current architecture is explicitly amended to make review changes render-affecting**.

### Output ownership/coherence

Prepare the complete staged generation first.

For each logical component:
- a new PDF may become current only with the corresponding accepted DOCX from the same staged semantic generation;
- if human DOCX no-clobber refuses promotion, its new automated PDF cannot advance alone;
- prior pipeline-owned stale siblings may be removed/archived only when ownership is safely proven from stored hashes/receipt evidence;
- human/foreign files are never silently removed.

Do not build a multi-file transaction coordinator. Verified currentness and safe idempotent recovery are sufficient.

### Manual PDF fallback

Document it truthfully.
Do not add a document-version/adoption subsystem unless direct use evidence shows it is necessary before smoke.

### Template point-of-use enforcement

Immediately before fill:
- verify the exact frozen master consumed;
- verify expected control inventory/map;
- refuse missing/duplicate/unknown unsafe controls before employer output is generated.

### Identity and leakage

Tighten identity verification to exact normalized document-specific fields where practical, rather than substring containment.

Extend high-precision private-ID detection to actual hyphenated/underscore EMP/EDU patterns while retaining false-positive fixtures.

### Write boundaries

Centralize safe destination resolution for public write surfaces.

Canonical writes:
- approved writable roots only;
- no protected-root/traversal/reparse escape.

Human external export:
- may be outside repository when explicitly invoked;
- non-authoritative;
- cannot point back into protected repository roots.

Do not let this protection block explicit maintained-source tooling such as template preparation.

### Exit
Status exposes only receipt-verified current outputs; degradation/human edits/reparse/export cases behave coherently.

---

## 8. Phase 5 — Staged immutable branch

### Objective
Make child creation parent-safe, internally coherent before exposure and semantically reusable when governing content is truly unchanged.

**Primary DFS:** DFS-12, DFS-19  
**Primary DOD:** DOD-12, DOD-19

### REQUIRED OUTCOMES

- verify parent/frozen/vacancy integrity before canonical child side effects;
- parent tree unchanged;
- no canonical child containing placeholder rebinding state;
- unchanged governing semantic content can remain current in child;
- changed governing content invalidates the correct earliest stage and descendants.

### PREFERRED MECHANISM

Construct the entire child in staging.

Compute final child manifest identity before exposing the directory.
Finish all artifact reuse/rebinding/validation in staging.
Expose only after the child derives internally coherent current state.

### Semantic hash neutrality for run identity — see `D-09` (`[OPTION]`, consumer inventory already done)

A promising simplification is to exclude only mechanically run-specific identity fields such as:
- `binding.run_id`;
- `binding.manifest_sha256`;

from semantic `artifact_hash`, while preserving all semantic/policy/source/upstream content in the hash.

This may make a child identity rebind hash-neutral and avoid an unnecessary downstream re-stamping cascade.

**Before adopting it:**
1. inventory every `artifact_hash` consumer;
2. prove no legitimate consumer relies on run identity being part of semantic identity;
3. prove direct run/job identity validation still rejects an artifact from the wrong run/job even when semantic hashes match.

If that proof fails, use a bounded topological rebind instead.
Do not add a lineage/dependency engine.

### Exit
Unchanged branch → current valid child with no semantic regeneration.
Changed governing input → correct stage/descendant invalidation only.
Refused/interrupted branch → no visible partial child.

---

## 9. Phase 6 — Target-Windows Word, template and visual reliability

### Objective
Remove known deterministic document/render defects that would contaminate the semantic smoke.

**Primary DFS:** DFS-13, DFS-14, DFS-15  
**Primary DOD:** DOD-13, DOD-14, DOD-15

### Long-path staging

Use a short transaction/staging location independent of long employer-facing final names.
Retain readable final output names.

Do not shorten employer-visible names merely to work around internal staging depth.

### Word timeout truthfulness

The mandatory invariant is:
- diagnostics say what actually happened;
- unrelated user Word work is never killed.

### Process cleanup — see `D-07` (`[OPTION]`, bounded by `[HARD]` truthfulness)

Use the safest exact-ownership technique supported by target evidence.

Possible implementations include:
- direct association from the automation instance/window handle to PID;
- another reliable process relation;
- unambiguous before/after PID detection with sufficient ownership checks.

If exact ownership is not established, kill nothing automatically and report the likely surviving automation process/operator action truthfully.

Do not treat simple PID differencing as inherently “ownership-proven.”

### Converter surface

Word COM remains the baseline.
Remove `auto`/LibreOffice fallthrough only if no current required consumer depends on it and removal simplifies the baseline.
Keep explicit “no PDF converter/degraded” semantics where useful.

### Reproducible page-break/template tuning

Route the current forced-break repair through maintained template-preparation tooling, not opaque manual DOCX surgery.

Preserve:
- control inventory;
- repaired Word-compatible OOXML properties;
- font/glyph behavior;
- byte-safe untouched parts.

Do not ban libraries by name as architecture. Ban unsafe serialization behavior unless target evidence proves it safe.

### Visual QA

Render sparse, normal and dense fixtures through target Word/PDF.
Inspect:
- clipping;
- unintended blank pages;
- heading/section flow;
- glyphs;
- page balance;
- parseability.

No hard page cap or automatic semantic truncation.

### Exit
Known long-path, timeout-diagnostic and forced-break defects are closed; target document evidence is retained honestly.

---

## 10. Phase 7 — Operator readiness and pilot instrumentation

### Objective
Ensure the next human/model phase can actually run without plumbing ambiguity.

**Primary DFS:** DFS-16, DFS-18  
**Primary DOD:** DOD-16, DOD-18

### Context and queue

Expose:
- capability role;
- resolved configured surface/model identifier where available;
- exact stage;
- current inputs;
- output contract;
- exact submission action;
- current review reasons/limitations/next action.

Do not turn queue/status into authoritative progress state.

### GATE-10

GATE-10 remains operational evidence, not architecture.

Synthetic tests may use explicit fixture mappings.

Do **not** invent a new `real_batch` vs `synthetic_batch` product mode merely to validate nonempty mappings.

Before real data, actual user/account facts must be supplied or recorded as `BLOCKED_USER`:
- intended SOL_CLASS/TERRA_CLASS surfaces;
- file-access behavior;
- relevant privacy/retention/training/account settings.

### Pilot log scaffold

Create a simple human-owned UTF-8 semicolon-delimited template covering at least:
- run/job identity;
- cluster/sequence;
- actual stage surfaces;
- quality/submit-ready judgment;
- factual corrections;
- human minutes;
- Stage-3 triage/repair;
- retries/reruns;
- notable mechanical/render context;
- submitted/dropped outcome.

Runtime must never require/read this file as control state.

### Exit
All mechanically preparable handoff/pilot infrastructure exists; remaining GATE-10 facts are either truthfully recorded or explicitly `BLOCKED_USER`.

---

## 11. Phase 8 — Public-path proof, evidence regeneration and hygiene

### Objective
Replace overclaimed/historical assurance with evidence generated from the repaired tree.

**Primary DFS:** DFS-17, DFS-19, DFS-00  
**Primary DOD:** DOD-17, DOD-19, DOD-20, DOD-21, DOD-22

### Public-path assurance

Retain helper tests, but add/repair public-command tests for contract-critical boundaries.

Do not add a generic “all helpers require callers” metric.
Delete dead helpers or wire the specific required boundary and prove behavior.

### Synthetic vertical slice

Regenerate from the repaired implementation.
Retain the referenced synthetic run/artifacts/evidence needed to re-derive the claims.

Do not cosmetically edit old reports into PASS.

### Gate/report regeneration

Regenerate:
- relevant gate reports;
- traceability;
- builder/finalization report;
- evidence hashes.

Every claim must distinguish its evidence scope:
- helper/unit;
- public command;
- target Windows/Word;
- visual human;
- user/account.

### Packaging/repository hygiene

Remove nested `Build.zip` and similar source-tree distribution residue.
Exclude local caches/environment artifacts from final distribution.
If a distribution archive is needed, generate it outside the source tree from an allow-list.

### Final audit

Run the complete `DEFINITION_OF_DONE.md`.

Only after the DoD passes may the ledger record:

`GO_FOR_TWO_JOB_SMOKE`

---

## 12. Explicit DEFER set

Keep outside this mechanical baseline unless new direct evidence satisfies scope admission:

- branch UX for supplying updated inventory/vacancy merely for convenience;
- personality catalogue redesign;
- source-inspection heuristic tuning;
- Stage-1 strategy-schema simplification for possible filler;
- broad dead-settings cleanup unrelated to accepted fixes;
- OS read-only layer absent surface evidence;
- generalized header/footer/text-box OOXML support not required by current masters;
- manual-PDF adoption/version-management subsystem;
- hard page caps/semantic auto-fit;
- event sourcing;
- dependency/lineage framework;
- generic multi-file rollback coordinator;
- automated semantic-model routing/retry;
- runtime semantic quality judge;
- semantic/pilot hypotheses requiring real packages.

Newly discovered out-of-scope work is recorded as `DEFER_DISCOVERED`.

---

## 13. Execution-completion handoff

When all phases that remain applicable are complete:

1. stop implementing;
2. execute the full DoD audit;
3. resolve every `FAIL`/`IN_PROGRESS`;
4. identify exact `BLOCKED_USER` items rather than guessing;
5. run final `/review`;
6. finalize the ledger/evidence pointers;
7. classify the roadmap `GO_FOR_TWO_JOB_SMOKE` only if its terminal criteria are met.

Do **not** execute the real two-job semantic smoke inside this Goal.
