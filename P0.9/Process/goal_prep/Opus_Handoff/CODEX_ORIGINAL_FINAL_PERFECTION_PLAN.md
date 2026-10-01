# Jobbsøk_26 P0.9 final perfection plan

## 1. Verdict and pre-smoke blockers

**Verdict: NO-GO for real candidate data and the two-job semantic smoke.** The implementation is mechanically substantial, but current public commands can accept stale work, render from unfrozen inputs, certify unrelated bytes, strand valid work, and let one malformed job abort a batch.

Pre-smoke blockers, ordered by expected value:

1. **Closed-loop handoff and current-at-birth** — `MMR-006/035`. Stage 2/3 cannot reliably complete without manually constructing hashes, and wrong upstream bindings are accepted.
2. **Frozen render inputs and point-of-use template enforcement** — `MMR-002/022`. Live-root master edits can alter employer documents while the receipt claims frozen bytes.
3. **Target-machine rendering** — `MMR-023/024/030`. Long Norwegian paths lose PDFs; timeout cleanup is false; the forced CV page break contaminates visual evaluation.
4. **Job-scoped containment and deterministic finalization** — `MMR-017/018`, `RC-9`. A date typo or malformed JSON aborts commands and can leave only a CV promoted.
5. **Shared action eligibility and verified receipts** — `MMR-004/005/007/015/019–021/027`. Stale semantic work and stale output remain actionable/current-looking.
6. **Complete frozen-run resolution and policy binding** — `MMR-001/003`. Root schemas/settings still alter frozen-run behavior.
7. **Branch, failure and write-boundary integrity** — `MMR-008–013/016/026/028/029/043/044`.
8. **Operational handoff** — `MMR-036–038`: nonempty surface mapping, useful queue/context, and a human-owned pilot log.
9. **Public-path proof and reproducible evidence** — `MMR-045/046`, all gates, and the synthetic vertical slice.

Falsification result:

- Every Critical/High or meta-raised Critical/High finding survived: `MMR-001–008`, `010–011`, `013`, `015`, `017–020`, `022–023`, `030`, `035`, `038`, `046`, plus `RC-9`. `MMR-012/016` also survived.
- No Critical/High finding is accepted solely on inherited evidence. Findings were either reproduced through the current CLI or traced to an unambiguous current execution path.
- Claims that collapsed:
  - The reconciliation’s quoted `59b2…` final hash does not reproduce; `MMR-005` still survives because the current semantic hash is `ab1d…` while the receipt binds unrelated `74e8…`.
  - The current GATE-05 `PASS` collapses after visual inspection of the forced sparse-CV page break.
  - The base dismissal of nested packaging residue collapses: `P0.9/Build/Build.zip` exists and contains protected inputs.
  - `MMR-032` is downgraded to pilot evidence: the current Stage-2 policy explicitly requests the same three distilled fields the implementation supplies.
  - `MMR-039` does not justify an architecture amendment; GATE-10 already owns volatile privacy facts.
- Inherited but not independently repeated exactly: the measured 260-character Word threshold, visible-Word process isolation, timeout orphan counts, and the transient ownership-recovery sequence. The underlying path, timeout-message and ownership defects were independently confirmed.
- Current scratch suite result: **206 passed, 1 failed, 1 skipped**; the failure is the long-path Norwegian glyph/PDF case. All mutation tests ran outside canonical `Build/`.
- Planning made no canonical writes. Of the packaged snapshot entries readable in the sandbox, 175 matched byte-for-byte with zero mismatches; four protected output files and `.pytest_cache` were unreadable, so no stronger hash claim is made.

## 2. Disposition ledger by confirmed root cause

### RC-A — Frozen snapshots exist, but consumers bypass them

- **MMR-001 — FIX.** Editing live `schemas/package.schema.json` left `verify-integrity` green but changed `validate`.
- **MMR-002 — FIX.** Editing only the live CV master changed delivered DOCX bytes while the report recorded the untouched frozen-master hash.
- **MMR-003 — FIX.** Artifact bindings cover the stage instruction but not the shared writing policy; warning thresholds load live settings.
- **MMR-022 — FIX.** `render` reaches `write_filled_docx` without invoking the existing template-contract guard.
- **MMR-041 — DEFER.** Several settings are dead, but broad cleanup has no smoke value; the live-threshold escape is fixed under `MMR-003`.

### RC-B — No closed-loop contract from context to acceptance and action

- **MMR-004 — FIX.** After replacing strategy, `context`, `finalize`, and `render` all succeeded against the stale downstream chain.
- **MMR-006 — FIX.** A draft with a zeroed strategy hash was accepted and displaced the valid current draft.
- **MMR-007 — FIX.** Stage context succeeded on stale input; Stage 3 does not distinguish normal pair production from review-only recovery.
- **MMR-015 — FIX.** Removing only review left `next --stage 3` directing the operator to finalize/render instead of complete review.
- **MMR-016 — FIX.** `next` returned a normal job from a parent whose frozen policy failed integrity.
- **MMR-018 — FIX.** `finalize` accepted `23.08.2026`; validation passed; render then raised and left only a CV DOCX.
- **MMR-031 — FIX.** Stage-2 policy literally says to preserve ceilings “the strategy recorded,” contrary to factual-authority precedence.
- **MMR-035 — FIX.** Public context omits required upstream hashes and a complete executable handoff.

### RC-C — Failure and exception containment is helper-only

- **MMR-008 — FIX.** `failure.record`, `clear`, and retry selection have no production callers.
- **MMR-009 — AMEND.** Current wording can assign arbitrary deterministic/render errors to the production-failure axis despite the independent render axis.
- **MMR-017 — FIX.** A malformed current strategy aborts `status`, `next`, and `validate` with a traceback.
- **MMR-044 — FIX.** `stage-submit` does not reject `EXCEPTION` jobs although later core validation/render omit them.

### RC-D — Branch publishes before proving a coherent child

- **MMR-010 — FIX.** A frozen-parent tamper produced a refused but visible canonical child directory.
- **MMR-011 — FIX.** A tampered vacancy produced an exit-0 child containing changed bytes under the old manifest hash.
- **MMR-012 — FIX.** Code publishes the child while reused artifacts still carry `manifest_sha256="PENDING"`.
- **MMR-013 — FIX.** An unchanged branch reported all four artifacts `REUSED`; child status was nevertheless stale at strategy.
- **MMR-014 — DEFER.** `branch` has no updated-batch/vacancy interface, but that UX is unnecessary for the two-job smoke or unchanged-input branch proof.

### RC-E — A render report is trusted data, not a verified receipt

- **MMR-005 — FIX.** The retained run’s report binds no existing final generation, yet status reports render `OK`.
- **MMR-019 — FIX.** Failed new PDF generation does not retire a safely identified pipeline-owned PDF from an older semantic generation.
- **MMR-020 — FIX.** DOCX no-clobber refusal does not prevent the corresponding newly generated PDF from promoting.
- **MMR-021 — FIX.** Ownership is inferred only from the latest report state, so a transient failure can make pipeline output appear foreign.
- **MMR-025 — IMPROVE.** Manual PDF fallback is documented but cannot become current; clarify that boundary and defer an adoption subsystem.
- **MMR-026 — AMEND.** Public `render --dest` accepted an arbitrary external directory; useful human export and authoritative output need distinct semantics.
- **MMR-027 — AMEND.** Report currentness is neither defined nor revalidated as a receipt.
- **MMR-028 — FIX.** Identity checks use substring containment rather than exact document-specific fields.
- **MMR-029 — FIX.** The scanner patterns omit hyphenated `EMP-…` and `EDU-…` forms.
- **MMR-043 — FIX.** Existing write/reparse guards are unwired; external destination bypass was reproduced.

### RC-F — The physical renderer is not yet target-environment reliable

- **MMR-023 — FIX.** The full suite’s sole substantive failure is loss of PDF at the deeper realistic path.
- **MMR-024 — IMPROVE.** The adapter claims Word was terminated although its timeout path only terminates PowerShell.
- **MMR-030 — FIX.** The CV master contains one forced break between support sections; rendered pages show visibly poor balance.
- **MMR-040 — IMPROVE.** `auto`/LibreOffice fallthrough remains despite Word COM being the selected and installed baseline.
- **MMR-042 — DEFER.** No OS read-only layer exists, but its value depends on the still-unknown chosen model surface.
- **MMR-047 — DEFER.** Filling only `document.xml` is real, but both masters’ header/footer parts contain zero SDTs; generalized OOXML support would be speculative.

### RC-G — Operator and product evidence loops are incomplete

- **MMR-032 — DEFER.** Current code passes the exact label/ceiling/guardrail trio required by Stage-2 policy; extra taxonomy has no observed package benefit yet.
- **MMR-033 — DEFER.** Source-inspection heuristics exist, but no real-job false-positive evidence exists.
- **MMR-034 — DEFER.** There is no real semantic evidence that strategy structure causes filler.
- **MMR-036 — IMPROVE.** The generated queue exposes one summary action but not the current review reasons/limitations needed to act.
- **MMR-037 — FIX.** `pilot/` is empty.
- **MMR-038 — FIX.** Both role mappings are empty; context therefore cannot tell the operator which actual surface/model to use.
- **MMR-039 — KEEP.** The architecture already assigns surface/privacy/retention facts to GATE-10.

### RC-H — Evidence asserts names or deleted runs instead of reproducible behavior

- **MMR-045 — IMPROVE.** Traceability tests prove test-name presence and helper behavior while production callers are absent.
- **MMR-046 — FIX.** The vertical-slice run named by evidence no longer exists; the surviving run has an orphan render receipt.
- **MMR-048 — IMPROVE.** A nested 2.5 MB `Build.zip` exists in the active tree and contains protected inputs.

### RC-I — Correct foundational behavior at cleanup risk

- **MMR-049 — KEEP.** Freeze-time baseline-to-authority reconciliation is implemented and blocks recorded hash conflicts.

## 3. KEEP register

The coding pass must preserve all of the following:

- **AR-01:** Word COM remains the default; do not add LibreOffice for parity.
- **AR-02:** Repair the existing masters through `prepare_masters.py`; do not replace their control capital.
- **AR-03:** Preserve the verified Calibri retarget and Norwegian glyph behavior.
- **AR-04:** Semantic final hash continues to exclude finalization/date; date invalidates render only.
- **AR-05:** Preserve the explicit Norwegian filename fold for `æ`, `ø`, and `å`.
- **AR-06:** Active runs consume run-local snapshots; live roots only govern a new freeze/child.
- **AR-07:** Keep factual `EV:` and mechanical `BL:` namespaces separate; add no claim graph.
- **AR-08:** Retain exactly three manually initiated semantic stages.
- **AR-09:** Stage 3 remains truth-bounded and elastic; no strategy-compliance gate.
- **AR-10:** PDF failure remains render degradation, never semantic failure.
- **AR-11:** Preserve hash-based no-clobber for human-edited outputs.
- **AR-12:** Deterministic code gains no truth judgment, model call, employer contact, publication, or submission ability.
- **AR-13:** Status remains job-local and partial-success; never make the run an all-or-nothing transaction.
- **AR-14:** Semantic density/page guidance remains soft; no P0.7 caps or auto-fit.
- **AR-15:** Retry remains visible, bounded, manual, and stage-owned; no orchestration engine or `RERUN` subsystem.
- **AR-16:** Preserve stdlib-only OOXML handling, byte-identical passthrough of untouched ZIP parts, `_merge_root_tag`, and per-document one-shot Word COM with `AutomationSecurity=3` and read-only open. No `lxml`, `python-docx`, or persistent Word instance.
- **AR-17:** Post-freeze inbox edits/deletion cannot affect active runs.
- **AR-18:** Warnings remain non-failing; action staleness is enforced directly, not disguised as an error-level semantic judgment.
- **AR-19:** Preserve the blocking human-reviewed baseline-to-authority reconciliation at freeze.
- **Additional KEEP:** GATE-10 remains operational rather than frozen provider policy; the manifest remains fact/config only; render does not become an `ARTIFACTS` peer; no completion markers, event sourcing, dependency graph, same-run amend, automatic submission, or second exception workflow.

## 4. Ordered implementation phases

### Public interface changes

- `context` emits a deterministic `handoff_token`, model-owned output contract, resolved capability surface, output mode, and exact `stage-submit` command.
- Model payloads no longer own `binding`, `artifact_role`, or `finalization`; `stage-submit` rejects those keys, verifies the current handoff token, inserts canonical metadata in memory, validates, and only then commits.
- Stage 3 normally submits `--final FILE --review FILE` as one validated pair. A review-only mode remains for an interrupted/current final with missing review.
- Stored artifact bindings add required `stage_policy_sha256`; draft binds current strategy, final binds current draft, and review binds current final.
- `render --dest` remains explicit human export but is non-authoritative and cannot update current status/receipt.
- Newly frozen runs use specification/schema revision `0.9.1`; no compatibility layer is added for the synthetic `0.9.0` residue.

### Phase 0 — Apply the four amendments

Apply the exact amendments in §5, update the adoption record, then make implementation and schemas conform. Do not otherwise edit architecture.

### Phase 1 — Frozen assets and closed-loop handoff

**P1-A — Frozen asset resolver (`MMR-001/002/003`).**  
Governing rules: `INV-02/03`, `CTR-01`, `DEC-40`, `ACC-10`. Add one `FrozenRunAssets` value object in existing `manifest.py`; validation, settings, context, and render receive frozen paths/parsed settings through it. Root assets remain valid only for preflight/index/freeze/new-child collection. Define a static per-stage policy digest: Stage 1 includes its instruction, both writing policies, personality profile/catalog and semantic settings; Stages 2/3 include their instruction and both writing policies. Branch governing-input sets use the same definitions. Risk: accidentally freezing future-child intake. Verify old-run root metamorphism and that a new child sees intentional root changes. Repeating path resolution in each caller was rejected because it recreates the exact divergence; no new module or dependency graph is introduced.

**P1-B — Handoff transaction (`MMR-006/035`).**  
Governing rules: `INV-09`, `CTR-04–06`, `ACC-10`. Add a canonical handoff/token helper in `artifacts.py`, consumed only by `context` and `stage-submit`. The token hashes current run/job/stage/mode, frozen policy digest and required current upstream. Submission with a stale token or wrong job/stage is refused before history/current mutation. Stage-3 pair validation completes before either candidate displaces good work. Target tests: verbatim context command succeeds; old token after upstream replacement fails; invalid final or review preserves the complete prior pair; review-only recovery succeeds. Manual hash construction and silent stamping without a current token are both rejected.

### Phase 2 — One currentness predicate for all actions

**P2-A — `assess_current_chain` (`MMR-004/007/015/016`).**  
Governing rules: `DEC-26/40/42`, `CTR-02`, `ACC-05/06/15`. Put a fixed strategy→draft→final→review table in `artifacts.py`; use it from status, next, context, submit, finalize, and render. Diagnostics may inspect invalid files, but no state-changing/action command may consume them. Stage 3 exposes `PAIR` or `REVIEW_ONLY`; `next` refuses compromised runs. Triage remains orthogonal and never gates render. Inline checks were rejected because six current callers already disagree; a generalized graph is also rejected.

**P2-B — Tool-owned finalization and factual ceilings (`MMR-018/031`).**  
Governing rules: `DEC-38`, `INV-03/07`, `ACC-10/17`. Stage-3 payload must omit finalization; tooling stores `UNFINALIZED/null`, and `finalize` alone accepts an ISO `YYYY-MM-DD` date, using JSON Schema `FormatChecker` plus explicit parsing. Preserve the semantic hash exclusion. Replace the Stage-2 sentence with: “Preserve the claim ceilings supported by the factual authorities. Treat strategy ceilings as advisory diagnostics; correct or source-escape them whenever the authorities require it.” Tests cover model-supplied dates, invalid dates, idempotent finalize and stable pure rerender.

### Phase 3 — Job containment and narrowly owned failure state

**P3-A — Per-job exception barrier (`MMR-017`, `RC-9`).**  
Governing rules: `INV-05`, `DEC-06/42`, `ACC-05/15`. Add a small `run_job_guarded` helper in `cli.py` around each job iteration in validate, status, next derivation, and render. Catch ordinary `Exception`, never `KeyboardInterrupt/SystemExit`; produce a job-local structured diagnostic, continue healthy jobs, and return nonzero after all jobs. Complete both staged DOCX builds before promotion so a build exception changes no current output. A broad top-level catch was rejected because it cannot continue the batch.

**P3-B — Current failure wiring (`MMR-008/009/044`).**  
Governing rules: `DEC-07/36/42`, `CTR-03`, `ACC-05/14`. Only a mechanically invalid semantic candidate submitted under a current token, or an unmodelled semantic-production exception, increments the stage’s frozen retry allowance when no valid current artifact still satisfies that stage. Wrong/stale-token preconditions and read-only diagnostics do not persist failure; render errors remain render-only. Successful owning-stage submission clears/supersedes failure; exhausted allowance becomes `BLOCKED_MANUAL`. Core commands fail early on `EXCEPTION` jobs without constructing a second workflow.

### Phase 4 — Verified receipts, coherent outputs and safe writes

**P4-A — Receipt verification (`MMR-005/027`).**  
Governing rules: `DEC-21/42`, `CTR-02`, `ACC-06/16`. In `render.py`, implement `verify_render_receipt` with component-level results. A current receipt must bind the current semantic final hash, current review eligibility hash, document date, render configuration, actual frozen baseline/map/master hashes read immediately before use, and every current output’s path/hash/size. Status lists only receipt-verified current files; mismatched/unreceipted files are `NOT_RENDERED` with a reason, not semantic failure. Keep render outside the semantic artifact registry. A multi-file transaction coordinator was rejected.

**P4-B — Promotion and ownership (`MMR-019/020/021/025`).**  
Governing rules: `DEC-21/41`, `ACC-16/17`. Build and verify both DOCX plus attempted PDFs before promotion. Promote a PDF only when its corresponding DOCX was accepted from the same staged generation. Use each prior receipt entry independently as ownership evidence even when the receipt is no longer current. Safely move a stale pipeline-owned sibling out of `out/` only when its actual hash matches that entry; never move a foreign/human-edited file. Keep an existing still-current receipt if a rerender attempt fails before changing output. Manual export remains non-current and is described truthfully in the runbook; no adoption/version-management command enters baseline.

**P4-C — Template, destination, identity and leakage (`MMR-022/026/028/029/043`).**  
Governing rules: `DEC-27/39`, `ACC-10/18/19`. Immediately before fill, verify the frozen master’s exact control inventory and map. Wire the existing path/reparse primitives into every public write surface. Canonical writes resolve only inside the named run/generated roots; an explicit external human destination is non-authoritative and cannot point back into protected repository roots. Verify candidate name and employer/title against their exact normalized document-specific fields, not substrings. Extend private-ID detection to underscore and hyphenated `EMP`/`EDU` forms while retaining ordinary-phrase false-positive fixtures.

### Phase 5 — Staged, immutable branch

**P5 — Branch transaction (`MMR-010–013`).**  
Governing rules: `DEC-40`, `INV-02/03`, `CTR-01/02`, `ACC-03/05/15`. Before allocating/publishing a child, verify every parent frozen record and every vacancy source. Construct the complete child manifest and all reuse decisions in staging; no `PENDING` value reaches the canonical tree. Change `artifact_hash` to exclude only `binding.run_id` and `binding.manifest_sha256`, in addition to existing finalization exclusion; all semantic, policy, source and upstream bindings remain hashed. Rebind identity fields and validate strategy→draft→final→review against child schemas before one final rename. If any content-governing input differs, omit the affected artifact and descendants from `current/`; do not create a lineage engine. An unchanged child must become `VALID/FINAL` with current review and require no semantic regeneration, while deterministic rerender remains child-local. Parent tree hash must remain identical.

### Phase 6 — Target-machine Word and visual quality

**P6-A — Short staging and truthful timeout (`MMR-023/024/040`).**  
Governing rules: `DEC-21/41`, `ACC-16/18`. Build/convert under a short system-temp transaction directory with fixed `cv.*`/`letter.*` names, then copy to destination-local temporary files for atomic promotion under readable final names. Retain per-document Word COM. The PowerShell adapter snapshots Word PIDs around COM creation and records the uniquely created PID plus creation time; on timeout it terminates only that unique recorded process. If unique ownership is not established, it kills nothing and reports the surviving PID/operator action truthfully. Remove `auto` and LibreOffice fallthrough; retain `word_com` and explicit `none` degradation.

**P6-B — Reproducible page-break repair (`MMR-030`).**  
Governing rules: `DEC-24/39`, `ACC-18`, GATE-05. Remove the single forced CV break through `runtime/tools/prepare_masters.py`; do not hand-edit the DOCX. Its before/after inventory must prove unchanged controls, untouched ZIP-part passthrough, root tag, core-property repair and font target. Render sparse, normal and dense fixtures through Word/PDF and visually verify order, clipping, glyphs, blank pages, orphan headings and page balance without imposing a page cap.

### Phase 7 — Operator readiness and evidence

**P7-A — Context, queue and GATE-10 (`MMR-036/038/039`).**  
Governing rules: `DEC-19/31`, `ACC-15/19`. Queue/status expose current review reasons, limitations and exact next action without becoming authoritative. Preflight and freeze reject an empty mapping for any capability role used by a real batch. Context displays the run-frozen surface/model mapping and exact handoff command. GATE-10 records current file-access, privacy, retention and account-setting facts; no volatile provider name enters architecture.

**P7-B — Pilot log (`MMR-037`).**  
Governing rules: `INV-08`, `ACC-20`. Create a UTF-8, human-owned semicolon-delimited pilot log containing job/run identity, cluster position, actual stage surfaces/models, human overall quality, submit-ready, factual corrections, total human minutes, Stage-3 triage and repair scope, retries/reruns, notable context/render failure and submitted/dropped outcome. Runtime never reads it.

**P7-C — Public proof and packaging (`MMR-045/046/048`).**  
Governing rules: `INV-02/08`, `ACC-01–20`. Replace name-only traceability with public-CLI behavior tests; label helper-only tests honestly. Do not add the proposed generic “every helper has a caller” assertion—delete or wire helpers and prove the actual boundary instead. Regenerate the retained synthetic slice and reports from the repaired build, retain the referenced run/artifacts, then remove the orphan run/evidence. Remove nested `Build.zip`, add it to ignore rules, and create any later distribution outside the source tree with an explicit allow-list.

## 5. Architecture amendments

Apply these as dated P0.9.1 amendments, mirrored in the normative specification, verification contract and adoption record.

**A-01 — Deterministic binding ownership**  
Affected: `INV-09`, `CTR-04`, `CTR-05`, `CTR-06`, `ACC-10`.

Append exactly:

> Mechanical binding metadata is deterministic-tooling-owned. A stage handoff token MUST bind the exact frozen run, job, stage, mode, policy and current-upstream inputs visible when context was prepared. Submission MUST reject a token that is no longer current before archiving or replacing any current artifact; only then MAY deterministic tooling insert the canonical binding envelope. Tooling MUST NOT silently rebind semantic content produced against stale inputs.

**A-02 — Render report as receipt**  
Affected: `DEC-21`, `DEC-42`, `CTR-02`, `ACC-06`, `ACC-16`.

Append exactly:

> A render report is a verifiable receipt, not a multi-file commit marker and not a semantic artifact. It is current only while its semantic-final hash, review eligibility, document date, actual consumed input hashes, render configuration and every reported output path and byte hash match current state. Unreceipted or mismatched files MUST NOT be surfaced as current deliverables. Receipt failure changes only the render axis.

**A-03 — Failure-axis ownership**  
Affected: `DEC-07`, `DEC-36`, `DEC-42`, `CTR-03`, `ACC-05`, `ACC-14`.

Append exactly:

> `FAILED` and `BLOCKED_MANUAL` current records represent semantic-production attempt and recovery state only. Read-only diagnostics and render, DOCX or PDF failures MUST NOT persist production failure. A refused candidate that leaves a still-current valid artifact untouched MUST NOT demote or hide that artifact. Successful owning-stage replacement clears or supersedes the applicable failure record.

**A-04 — Canonical writes versus human export**  
Affected: `DEC-27`, `ACC-19`.

Append exactly:

> Canonical deterministic and model-controlled writes MUST resolve inside approved run or generated roots and MUST reject traversal and symlink or reparse-point escape. An explicitly human-requested export MAY target a resolved path outside the repository, but is non-authoritative unless separately verified and adopted. Export into any protected repository root MUST be refused.

## 6. DEFER list

- `MMR-014`: updated batch/vacancy intake on branch; reconsider only after unchanged-child behavior is proven and a real reopen needs it.
- `MMR-032`: personality catalogue or richer distilled metadata; evaluate actual smoke packages first.
- `MMR-033`: source-inspection heuristic tuning; collect real false positives.
- `MMR-034`: strategy schema/prompt simplification; inspect two jobs and the cluster.
- `MMR-041`: broad dead-settings cleanup beyond consumers touched by accepted fixes.
- `MMR-042`: OS read-only attributes until GATE-10 identifies a surface where they add containment.
- `MMR-047`: generalized header/footer/text-box SDT support; current masters have no such controls.
- Manual-PDF verified adoption; current fallback remains explicit and non-authoritative.
- Conditional typography/page auto-fit, hard page caps, event sourcing, dependency/lineage engines, multi-file rollback coordination, automatic model routing/retry, and generic caller-count tests.
- All semantic-quality hypotheses lacking implementation evidence; record them in the pilot rather than changing baseline behavior.

## 7. Final verification and evidence-regeneration sequence

1. Record a full pre-change hash inventory; perform destructive/adversarial work only in disposable copies. After every phase, confirm protected inputs and unrelated job hashes.
2. Run compile/import checks and the full suite with an explicitly short scratch `--basetemp`; require every non-documented test to pass.
3. Freeze a fresh synthetic two-core-job run and drive every workflow through the actual CLI entrypoint.
4. **Frozen-root metamorphism:** after freeze, mutate every maintained root input category—including all live schemas, policies, settings, authorities, maps, templates and inbox—inside one scratch copy. Prove run-bound integrity/status/validation/context/finalization/render behavior and employer-visible output remain derived solely from frozen bytes. Prove a newly frozen child does see intended maintained-root changes.
5. **Handoff/currentness:** replay exact context commands; reject old/wrong tokens before archive; reject stale upstream; atomically validate Stage-3 pair; recover review-only; prove current good hashes survive every refused submission.
6. **Receipt/output:** change final content, review, date, each receipt binding and each output byte independently. Status must hide every non-current component. Repeat live-master mutation, PDF failure, human DOCX edit, rerender recovery, protected destination, external export and reparse/junction cases.
7. **Job containment:** use two jobs and make one artifact malformed, one current path a directory, one render date invalid and one render operation raise an ordinary unexpected exception. Validate/status/next/render must diagnose it, finish the healthy job, preserve unrelated hashes and return nonzero without partial current presentation.
8. **Branch:** test compromised frozen input, compromised vacancy, unchanged parent, changed policy, changed schema and interrupted staging. No refused child may appear; parent hashes never change; unchanged child is `VALID/FINAL`; changed governing input invalidates only the correct stage and descendants.
9. **Manual handoff:** prove context supplies surface, role, inputs, output contract and exact command; Stage 1/2/3 plus review-only can complete without manual hash calculation. Core commands refuse `EXCEPTION`.
10. **Rendering:** rerun realistic longest employer/title paths, forced timeout with an already-open human Word session, converter degradation, exact identity/leakage checks and sparse/normal/dense visual QA. PDFs and DOCX must match the same semantic generation.
11. Run an explicit AR-01…AR-19 audit through public behavior, active-tree searches and target-machine render evidence.
12. Execute GATE-01…GATE-10 at their true scope. GATE-05 remains open until visual evidence exists; GATE-10 remains open until account-specific user facts exist.
13. Regenerate the synthetic vertical slice, gate reports, traceability matrix and builder report from commands run against the repaired tree. Retain the referenced synthetic run and hashes; distinguish helper, public-command, target-machine and human evidence. Remove superseded/orphan evidence only after replacement verifies.
14. Only then issue a conditional **GO for two real jobs**. Each job must complete all three manual stages, current review/finalization and render; a human must confirm submit-ready CV and letter, zero known material truth/attribution defects, and record effort/quality. PDF degradation remains explicit rather than semantic failure.
15. A representative cluster pilot may begin only after both real jobs pass. Pilot observations do not mutate baseline unless they expose a recurrent material defect within the stated scope. No submission occurs automatically.

## 8. Genuine user-owned inputs

No user choice is needed for the mechanical implementation or synthetic proof. Work must stop before real candidate data until the user supplies:

- Two human-approved real vacancies with exact employer/title/source, `CORE` classification, priority, cluster and sequence, plus confirmation that the three factual authorities and baseline reconciliation are current.
- The actual Stage-1/2/3 model surfaces mapped to `SOL_CLASS` and `TERRA_CLASS`, confirmation of file access, and account-specific privacy/retention/training settings required by GATE-10.
- Human submit-ready judgment, factual-correction review, quality score, elapsed minutes and final submission/dropped outcome for each smoke job. Actual submission remains manual and outside core.

No unresolved conflict between hard constraints was found.

## GOAL CONTRACT

```text
Bring Jobbsøk_26 P0.9 to a truthfully evidenced state where a two-real-job semantic smoke can be run without known mechanical contamination. Detail and adjudication authority are in P0.9/Architecture/, P0.9/Finalization_Review/P0.9_Final_Multi_Model_Review_Reconciliation.md, and this final plan.

Observable end state:
- Every run-bound public command derives behavior from the immutable run snapshot; editing any maintained root input after freeze cannot alter that run’s behavior, eligibility or employer-visible output.
- Context produces a current, copy-ready handoff and exact command; stale/wrong handoffs are refused before good current work is archived or replaced.
- Finalization, context and render consume only a complete current semantic chain. Date is deterministic-tooling-owned and ISO-valid.
- Status lists an output only when a verified receipt binds the current semantic final, review eligibility, date, actual consumed frozen inputs and the bytes present.
- DOCX/PDF pairs cannot split generations; human edits are not clobbered; stale pipeline output cannot masquerade as current.
- Malformed data, operator mistakes and unmodelled exceptions remain job-local; healthy jobs complete and remain visible.
- Branch never mutates the parent or exposes a partial child; unchanged governing inputs yield a current child requiring no semantic regeneration.
- Core writes stay within approved roots; explicit external export is non-authoritative; traversal/reparse escape and core processing of EXCEPTION jobs are refused.
- Long realistic Windows paths render through one-shot Word COM; timeout diagnostics/cleanup are truthful; sparse/normal/dense documents pass target visual and parseability checks.
- Public-command tests, gates, vertical-slice artifacts and builder evidence are regenerated from the repaired tree and claim only their actual scope.
- Two approved real jobs finish with current Bokmål CV and letter, human submit-ready approval, zero known material truth/attribution defects and complete human-owned pilot entries.

Non-negotiable: preserve AR-01…AR-19; three manual semantic stages; Stage-3 elasticity; EV/BL separation; immutable runs; independent semantic/production/render axes; warning-only semantic guidance; PDF degradation orthogonality; no model/network/submission automation, runtime quality judge, same-run amend, event sourcing, dependency engine, P0.7 compatibility, or speculative subsystem.

Scope: accept only material correctness, integrity, containment, operator-blocking, smoke-contaminating or directly consequent work. Defer pilot-only semantic hypotheses and the explicit DEFER list.

Legitimate stops: all properties and evidence above pass; or stop before real data for missing approved vacancies/GATE-10 facts; or report BLOCKED only for a demonstrated hard-constraint conflict or unavailable target capability after two substantively different bounded approaches. Never infer PASS from helper tests, compilation, existing artifacts or a responsive Word process.
```
