# Jobbsøk_26 P0.9.1 — Final Post-Implementation Acceptance Audit

**Audit date:** 2026-08-28  
**Scope:** exact `P0.9/Build` implementation, frozen P0.9 architecture, final P0.9.1 specification/instructions, implementation report, current repository state and independently rerun evidence  
**Verdict:** **GO_WITH_MINOR_FIXES**

## Executive conclusion

The implementation is close to the correct stopping point. The P0.9.1 patch is small, accurately scoped and materially improves the intended operating path. The frozen truth, submission and state-axis boundaries remain intact. The deterministic runtime still has no model, network, employer-contact or submission capability. A fresh public flow produced a frozen run, all four context modes, valid Stage 1/2/3 commits, triage-independent finalization, an idempotent repeat finalize, two valid DOCX files and truthful PDF degradation.

It is not yet a clean `GO` for three reasons:

1. Two higher-order interruption cases can make `next` say that nothing is outstanding even though current disk state still owes work.
2. The current post-patch suite has not been proven with Word COM in an unlocked interactive session: this audit reproduced **240 passed / 10 skipped / 0 failed**, not the required **250 / 0 / 0** target result.
3. The production role mapping and GATE-10 account posture are intentionally human-owned and are still blank/unrecorded in the checked-in defaults; they must be completed before the first real freeze.

The first two defects have small, local repairs. They require no command, schema, status field, state axis, dependency, retry engine or redesign. After those repairs and the target-Word gate, further speculative design has lower value than two real vacancies.

## Authority and audit method

Governing authority was applied in this order:

1. the current acceptance-audit request;
2. `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md`;
3. `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`;
4. the actual repository as implementation truth;
5. the final P0.9.1 specification/instructions for the retained patch and control-plane wording;
6. plans, reports and prior test claims as evidence only.

The final P0.9.1 specification and implementation instructions were read completely, as were both frozen architecture files and the repository-root `AGENTS.md`. No file under `P0.7/` was treated as authority. No architecture file was amended.

The architecture provenance is coherent in the implemented policy:

- frozen P0.9 mandates human approval before submission or irreversible external action;
- frozen P0.9 permits deterministic rendering and cluster-stage work without routine between-job confirmation;
- frozen P0.9 keeps semantic triage, production/mechanical state and render state separate;
- frozen P0.9 permits, but does not mandate, render-all-valid;
- P0.9.1 selects render-all-valid as operating policy.

The patch does not falsely present the selected policy as a frozen rule.

## Final finding register

| ID | Classification | Finding | Launch consequence |
|---|---|---|---|
| F-01 | `FIX_BEFORE_BATCH` | A current valid Stage-3 replacement can inherit an old render receipt that status calls `FAILED`; interrupted continuation only resumes `NOT_RENDERED`, while `next --stage 3` stops at the current final+review. | Repair locally before a real batch. |
| F-02 | `FIX_BEFORE_BATCH` | A failed semantic replacement over older valid downstream artifacts is visible as `FAILED`, but stage-specific `next` filters on the older highest-valid stage and can say “Nothing outstanding.” | Repair locally before relying on rerun/revision recovery. |
| F-03 | `FIX_BEFORE_BATCH` | Current target-machine Word evidence is incomplete: 10 COM-scoped tests skipped and public render degraded with Windows `0x80070520`. | Run the exact target gate after F-01/F-02; change code only if it fails there. |
| F-04 | `DEFER` | Dormant `converter = "auto"` support implements sequential Word→LibreOffice failover even though frozen P0.9 prohibits multi-converter failover infrastructure. Production settings use `word_com`, so the branch is unreachable in the exact run. | Record the deviation; do not delay two real jobs for a schema/config cleanup. |
| F-05 | `KEEP` | The ten-file P0.9.1 patch implements the eight retained changes without architecture, schema, dependency or state expansion. | Keep. |
| F-06 | `KEEP` | Truth, evidence, role ownership, immutable-run, no-clobber and human-only external-action boundaries are strongly enforced and adversarially tested. | Keep. |
| F-07 | `KEEP` | The three-stage writing design is decision-oriented, evidence-bound, reconstructive and plausibly capable of strong native Bokmål packages. | Keep the prompts unchanged for the first two jobs. |
| F-08 | `PILOT_FIX_ONLY_IF_OBSERVED` | Actual employer-facing excellence, `READY` calibration and cross-job semantic reset cannot be proven by fixtures or Python tests (`INV-08`). | Measure on two real vacancies; tune only on recurrent material misses. |
| F-09 | `PILOT_FIX_ONLY_IF_OBSERVED` | Soft page-target warning usefulness and the real human review burden are empirical. | Observe; do not add thresholds or workflow machinery now. |
| F-10 | `KEEP` | Blank `[stages.role_mapping]` is an explicit one-time human gate, not a missing runtime feature. | Populate it and record GATE-10 before the first production freeze; add no preflight code. |

No `BLOCKER` requiring redesign, architecture amendment or a new subsystem was found.

## Adversarial audit of the P0.9.1 patch

The external pre-change registry contains 99 active Build files. A byte-level comparison against current state identified exactly the expected ten changed files and no source/schema/architecture expansion:

- `BUILDER_REPORT.md`
- `policy/RUNBOOK.md`
- `policy/stages/stage1_decision_architecture.md`
- `policy/stages/stage3_final_writer_review.md`
- `pyproject.toml`
- `runtime/jobbsok/cli.py`
- `runtime/jobbsok/render.py`
- `runtime/tests/test_t01_t04_run_lifecycle.py`
- `runtime/tests/test_t05_t08_ownership_schema_failure.py`
- `runtime/tests/test_t19_t23_render_security.py`

### Retained-change disposition

| Change | Verified implementation | Disposition |
|---|---|---|
| 1 — RUNBOOK operating flow | Stage×cluster loop, no routine between-job confirmation, immediate explicit finalize/render for all triage values, truthful attribution, end summary and relocated GATE-10 reminder are present. | `KEEP`, subject to F-01/F-02 continuation repair. |
| 2 — Stage 3 policy references | Stage 3 names both writing policies and applies `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten`. | `KEEP`. |
| 3 — Stage 3 loop/triage behavior | Explicit reset, reconstructive authority, calibrated `READY` and immediate deterministic finalize/render are present without treating render as approval. | `KEEP`. |
| 4 — Stage 1 decision density/reset | Reset, decision-dense fields, `Single Backbone og strategisk asymmetri` and `WRONG_ROUTE` are present without a new rubric. | `KEEP`. |
| 5 — implementation version | `pyproject.toml` and the three changed control-plane frontmatters are `0.9.1`; specification/schema revision remains `0.9.0`. | `KEEP`. |
| 6 — context I/O | All four modes emit real frozen schema paths, handoff-scoped return paths and quoted executable PowerShell commands. | `KEEP`. |
| 7 — refusal recovery output | The just-written failure payload is printed with classification, correction count, semantic attempt and next action. State/exit behavior is unchanged. | `KEEP`. |
| 8 — page warning | Warning is configuration-driven, per-document, soft, printed only after successful PDF page counting and stored in the existing warnings array. | `KEEP`. |

`cmd_finalize` correctly received no triage branch: the pre-patch behavior was already triage-independent. No change was manufactured.

### Scope/version gate

- no new command or parser branch;
- no schema or schema-file edit;
- no new dependency or runtime module;
- no new manifest/status field, state axis or authoritative artifact;
- no model/network client, automatic model retry, approval abstraction, numeric judge or hard page/count threshold;
- no edit under `P0.9/Architecture/`;
- no edit to `policy/settings.toml`, Stage 2 or `policy/writing/*`;
- `SPEC_REVISION`, `SCHEMA_REVISION`, manifest schema constants and `[spec].schema_revision` remain `0.9.0`;
- the version edits are exactly four lines.

## Architecture compatibility

### Compatible material behavior

The exact configured system preserves the frozen architecture’s load-bearing invariants:

- approved vacancy identity and frozen inputs are manifest-bound and integrity-checked;
- static candidate facts come from the three authorities through the reviewed baseline/evidence index;
- Stage 1 owns strategy, Stage 2 draft, Stage 3 final+review; downstream stages cannot rewrite upstream artifacts;
- semantic currentness, current failure and render receipt remain separate authorities;
- Stage 3 may reconstruct rather than merely polish;
- `READY`/`CHECK`/`RERUN` are repair-scope triage only and do not gate rendering;
- finalize remains explicit and separate from render;
- PDF failure degrades the render axis without invalidating the semantic package;
- external submission and irreversible action remain human-only;
- no automatic model execution or retry exists.

### Dormant deviation: multi-converter `auto`

Frozen specification line 160 prohibits “multi-converter failover infrastructure.” Actual code permits `auto` in `runtime/jobbsok/settings.py`, both render schemas and `policy/settings.toml`, and `runtime/jobbsok/pdf.py:286` sequentially tries Word COM then LibreOffice.

This is a real architectural deviation, not a P0.9.1 patch regression. It is dormant because the frozen production snapshot uses `converter = "word_com"`. It cannot affect the two-job run unless the human changes configuration. Removing it now would touch runtime, policy, schemas and tests without improving the exact pilot path. Classification: `DEFER`. Remove it only in a deliberate schema/config revision or if converter policy is otherwise changed.

## Whole-system and higher-order findings

### F-01 — stale receipt strands owed rendering (`FIX_BEFORE_BATCH`)

The final specification and RUNBOOK assume owed internal production appears as `render_state.overall == "NOT_RENDERED"`. Actual interaction:

1. Stage 3 stamps every replacement final with `finalization.state = "DRAFT"` (`runtime/jobbsok/artifacts.py:329`).
2. An older render receipt remains until the next render.
3. Status verifies that old receipt against the replacement final. Any mismatch becomes render `FAILED` (`runtime/jobbsok/status.py:235-260`).
4. `next --stage 3` stops once final+review are current (`runtime/jobbsok/status.py:423-451`).
5. Interrupted continuation only repairs `NOT_RENDERED` (`policy/RUNBOOK.md:104-118`).

Reproduced result after a valid Stage-3 resubmission over an already rendered job:

```text
production_state       VALID
highest_valid_stage    FINAL
semantic_final_available true
semantic_triage        CHECK
finalization.state     DRAFT
render_state.overall   FAILED (receipt final hash mismatch)
next --stage 3         Nothing outstanding for that selection.
```

The retained run `r20260823-050000-fea486` independently exhibits the same terminal shape: valid current final, `CHECK`, render receipt final-hash mismatch, and `next --stage 3` reports nothing outstanding.

**Smallest sufficient repair:** in `status._derive_job`, distinguish receipt staleness from a failed current render. If every receipt error is a current-input binding mismatch, report the current render as `NOT_RENDERED` and expose no old output paths. Keep malformed receipts, missing/corrupt outputs, hash mismatches, locks and other verification failures as `FAILED`. Extend the existing status/staleness test file with render-once → replace final+review → status assertions. Add no render-stale state and no schema field.

### F-02 — failed replacement hidden by older valid stage (`FIX_BEFORE_BATCH`)

The bounded recovery footer works while the operator remains in the refusal flow. After an interruption, however, stage-specific `next` uses only `highest_valid_stage`. An old valid final therefore masks a current failure from a Stage 1/2/3 replacement attempt.

Reproduced with a fully staged job plus a current `STAGE1` failure:

```text
production_state       FAILED
highest_valid_stage    FINAL
semantic_triage        CHECK
recommended_action     Correct and resubmit Stage 1.
next --stage 1         Nothing outstanding for that selection.
```

This contradicts the current failure record and the specification’s claim that a repeated job from `next` represents bounded recovery in progress.

**Smallest sufficient repair:** have `cmd_next` pass a transient `{job_id: failure.operation}` mapping into `next_job`. Before the highest-stage filter, return a `FAILED` job only when its current operation matches the selected stage and cluster. Do not expose or persist the mapping, add a status field, or start any retry automatically. Extend the existing recovery/status test file with a fully staged job, a matching failed replacement and a mismatched-stage control.

### F-03 — target Word proof remains open (`FIX_BEFORE_BATCH`)

This audit opened a visible Word window and retried both the adapter and a direct COM probe. COM activation still failed before an automation instance was created:

```text
HRESULT 0x80070520: A specified logon session does not exist.
```

The current suite result is **240 passed / 10 skipped / 0 failed**. All ten skips are Word-COM-scoped. A prior Process report claims **246 passed / 0 skipped** for the pre-P0.9.1 suite in an ordinary interactive session, but that is a historical claim, not current independent evidence. P0.9.1 adds four non-COM cases, so the current target total is **250 passed / 0 skipped / 0 failed**.

**Smallest sufficient repair:** no code by default. In an unlocked interactive Windows/PowerShell session with Word COM, run the exact full suite with external `--basetemp`, then one current public finalize/render. Record the exact count and confirm both verified PDFs, page counts, Norwegian glyphs, rerender/date behavior and ownership tests. If the target run fails, fix only the reproduced failure.

## Freeze, authority and currentness

`KEEP`:

- Freeze is atomic and snapshots authorities, baseline map, evidence index, masters, template map, policy, settings and schemas.
- Manifest/schema revisions are pinned at `0.9.0`; the package release is independently `0.9.1`.
- Baseline reconciliation records the real human reviewer only at freeze/branch.
- A frozen-input mismatch is a run-integrity error; the operator branches rather than amending in place.
- Approved-set completeness comes from the manifest, not directory discovery.
- Exception jobs remain visible and do not block independent core jobs.

The checked-in `[stages.role_mapping]` is blank. That is an intentional human pre-production gate selected by the final P0.9.1 specification. Before the first real freeze, the operator must populate the mapping and record the account retention/training posture. A freeze-time code warning or a configuration-dependent test should not be added.

## Queue, continuation, failure and stale-state behavior

Outside F-01/F-02, the mechanics are strong:

- one current failure record per job, with bounded mechanical correction and at most the configured semantic retry;
- `BLOCKED_MANUAL` is job-local and skipped by `next`;
- strategy/draft/final replacement produces the frozen downstream stale scope;
- current review triage is exposed only when bound to the current final;
- status is regenerated from manifest/current artifacts/failure/receipt rather than history replay;
- a mixed run preserves valid peer outputs and reports poisoned jobs independently;
- rerender/date/edited-output protections are explicit and tested.

No event log, completion marker, dependency engine, fourth stage or autonomous recovery mechanism is needed.

## Evidence and truth boundaries

`KEEP`:

- only `Work_experience.md`, `Education.md` and `Other_high_value_information.md` can raise candidate claim ceilings;
- baseline, vacancy, personality and writing policy cannot create candidate facts;
- evidence references are validated against the frozen index and correct namespace;
- baseline-mechanical references cannot masquerade as factual evidence;
- Stage 1 consults personality only after factual grounding and selects zero to three evidence-bound facets;
- Stage 2/3 receive distilled personality guidance; Stage 3 may suppress or replace it;
- unknown employment/education IDs and prohibited merge expansion fail mechanically;
- leakage checks protect private tokens/placeholders and employer/job identity.

The evidence model is conservative enough for real use. Employer-facing truth still requires the final human rendered-package review; the system correctly does not claim otherwise.

## Rendering, output containment and document evidence

The fresh public render produced:

- CV DOCX: `OK`, openable, non-empty, no residual content controls, no private token/placeholder, identity/chronology/headline/override checks passed;
- letter DOCX: `OK`, openable, non-empty, no residual content controls, no private token/placeholder, employer addressing present;
- both PDFs: `DEGRADED` because COM activation failed;
- both failed PDF rows: `page_count = null`, `warnings = []`;
- overall render: `DEGRADED`, while semantic triage remained `RERUN` and production remained `VALID`.

No page warning was produced for failed conversion. That is expected and correct.

Output filenames are sanitized; run/job paths reject traversal and reparse-point escape; canonical outputs use receipt hashes and per-file atomic promotion; a human-edited/locked destination is preserved unless the operator uses explicit `--force` or an alternate non-authoritative `--dest`.

The fresh DOCX files were structurally opened and their complete paragraph/table text extracted. The dynamic CV merge, complete letter and Norwegian characters were present in the package. Visual page inspection could not be completed: the packaged renderer has no LibreOffice binary, Word app control was not approved, and current COM failed. Therefore this audit does **not** claim a current visual/PDF pass.

## Stage 1/2/3 production-quality assessment

### Stage 1 — decision architecture

Likely strong. It forces vacancy-first decision analysis, separates material requirements from generic fit, establishes a single shortlist thesis, identifies objections and counterfactual routes, and consults personality only after evidence. The new reset and decision-density wording reduces generic BI/AI defaulting and cross-job carryover.

Classification: `KEEP`. Pilot question: does it choose a decisive, vacancy-specific route on both an obvious-fit and a higher-objection vacancy? Change only if a recurrent wrong route is observed.

### Stage 2 — native package writer

Likely strong. It explicitly requires native, restrained Bokmål; a complete tailored CV and complementary letter; narrow CV overrides; evidence references; no translated-American rhetoric; and a per-job reset. The writing doctrine’s single-backbone and CV/letter asymmetry are unusually concrete.

Classification: `KEEP`. Pilot question: does the actual configured writer produce a materially tailored CV rather than merely a tailored profile, and does the letter synthesize rather than repeat? Do not add a new English rubric.

### Stage 3 — reconstructive final writer/reviewer

Likely strong and appropriately elastic. It may reorder, suppress, replace and source-escape; it is not constrained to polishing the draft. It receives factual sources and current strategy/draft, may reject personality-conditioned expression, applies the two named quality gates, repairs unsupported upstream claims before save and returns actionable triage.

Classification: `KEEP` plus `PILOT_FIX_ONLY_IF_OBSERVED`. The unproven points are actual `READY` calibration, native voice, employer specificity, strategic reconstruction frequency and cross-job reset under real cluster length. Those are human/model evidence questions under `INV-08`, not Python gates.

## Independent verification evidence

All commands below were run from the real Build root containing `ø`, except where an external scratch path is explicit.

| Proof | Independent result |
|---|---|
| `jobbsok preflight` | `Preflight PASS`; Python 3.14.3, 17 CV controls, 7 letter controls, 144 evidence entries, 6 employments, 4 educations. |
| Full suite with external `--basetemp` | **240 passed / 10 skipped / 0 failed**, 97.82 s. Skips are not passes. |
| Adversarial T09–T18 plus traceability | **130 passed / 0 skipped / 0 failed**, 26.66 s. |
| `python -m tools.prepare_masters --check` | PASS; masters canonical, 17/7 controls, no reorder/font/page-break correction. |
| `python -m tools.vertical_slice --out <external> --workdir <external>` | **21 expected / 0 unexpected**; two DOCX outputs; truthful `DEGRADED`; poisoned peer isolated. |
| Public `context` | Actual JSON inspected for `STRATEGY`, `DRAFT`, `FINAL_AND_REVIEW`, `REVIEW_ONLY`; frozen schemas and distinct handoff-scoped return paths existed. |
| Verbatim public submission | Emitted PowerShell commands executed verbatim. A deliberately stamped input was first refused for tool-owned fields; the semantic-only correction succeeded and cleared recovery state. |
| Public finalize | Real finalize succeeded for `READY`, `CHECK`, `RERUN`; repeat without `--date` returned the existing-date idempotent path. |
| Public render/status | Both DOCX `OK`, both PDF `DEGRADED`, render exit 0; status retained `RERUN`/`VALID`/`DEGRADED`. |
| Direct Word COM probe | Failed with `0x80070520`; ten COM tests remained skipped. |
| Higher-order stale-receipt probe | Reproduced valid final+review + `DRAFT` + render `FAILED` + Stage-3 next “Nothing outstanding.” |
| Higher-order failed-rerun probe | Reproduced current `STAGE1` failure + older highest `FINAL` + Stage-1 next “Nothing outstanding.” |
| Final active-file hash check | After moving scratch runs/evidence outside Build and restoring the prior evidence mirror, exactly the expected ten baseline files differ. |

The vertical-slice tool refreshed its in-Build evidence mirror during this audit. The entire audit-produced mirror was moved to external scratch and all pre-audit tracked evidence bytes were restored and hash-checked. The fresh synthetic run and run-specific generated handoffs/returns/views were likewise moved intact to external scratch. The retained historical run was not modified.

## Exact pre-batch repair and verification sequence

1. Add the F-01 binding-stale receipt distinction in `status._derive_job`; extend an existing status/staleness test.
2. Add the F-02 transient matching-failure operation to stage-specific `next`; extend an existing recovery/status test.
3. Run the two focused assertions first and observe their current failure, then implement; no new test file.
4. Run from the real Build root:

   ```powershell
   .\.venv\Scripts\python.exe -m pytest runtime/tests -q -p no:cacheprovider --basetemp C:\<external-scratch>
   .\.venv\Scripts\python.exe -m tools.prepare_masters --check
   .\.venv\Scripts\python.exe -m tools.vertical_slice --out C:\<external-evidence> --workdir C:\<external-workdir>
   ```

5. In an unlocked interactive Word-COM session, require exactly **250 passed / 0 skipped / 0 failed** and one successful public render with verified CV+letter PDFs. Confirm page counts/warnings and Norwegian glyphs by inspection.
6. Re-run both higher-order probes: replacement-final receipt must become `NOT_RENDERED`; matching failed replacement must be selected by the corresponding stage-specific `next`.
7. Re-run the final scope gate: no new dependency, schema, command, parser surface, module, state field, authority, client, retry mechanism, approval abstraction, hard threshold or architecture edit.
8. Populate `[stages.role_mapping]` with the actual roles and record GATE-10 account posture before the first production freeze.

## Residual risks after the minor fixes

| Risk | Treatment |
|---|---|
| Actual model-role quality and native voice | `PILOT_FIX_ONLY_IF_OBSERVED`; two real vacancies own the evidence. |
| Cross-job semantic bleed | Use the existing reset protocol and human spot-check; alter cluster shape only if observed. |
| `READY`/`CHECK`/`RERUN` calibration | Compare Stage-3 triage with actual human repair scope; tune only on recurrent material misclassification. |
| Page-target warning usefulness | Observe alongside actual rendered pages; keep advisory and configuration-driven. |
| Human time through review/submission | Record in the existing pilot evidence process; do not create runtime state or telemetry. |
| Dormant `auto` converter deviation | `DEFER`; exact production config never enters it. |
| PDF automation availability | DOCX remains conforming and manual export remains the architecture-approved fallback; target Word proof is still required for acceptance evidence. |

## Launch recommendation

**GO_WITH_MINOR_FIXES.** Implement only F-01 and F-02, pass the current 250/0 target-Word gate, complete the one-time role/account provenance gate, and then run the two deliberately selected real CORE vacancies through:

```text
freeze
→ Stage 1 × cluster
→ Stage 2 × cluster
→ Stage 3 × cluster
→ valid final+review
→ explicit finalize
→ render/verify
→ cluster summary
→ human reviews actual rendered package
→ human submits/revises/reruns/drops
```

No routine human checkpoint belongs between successful Stage 3 and rendering. Triage does not gate rendering. External irreversible action remains human-only.

After the local continuation fixes and target proof, the correct next action is two real vacancies—not another design pass.
