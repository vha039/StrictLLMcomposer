# Jobbsøk_26 P0.9 — Updated Five-Lens Integrated Forensic Build Audit

**Audit date:** 2026-08-23  
**Audited artifact:** `Build.zip`  
**Build ZIP SHA-256:** `56a3afd0ff6d6e2771b47bc16ddb1bd4cdce1a609072254a5e0a0e22604d841a`  
**Architecture:** P0.9 / specification revision 0.9.0 / `FROZEN_NORMATIVE`  
**Basis:** previous independent forensic audit + additional five-direction control passes  
**Runtime source size:** ~6,082 Python LOC  
**Test source size:** ~2,701 Python LOC  
**Audit posture:** optimize the real framework, not ceremonial compliance. A deviation is not a defect merely because it differs from the frozen design.

---

## 0. Common review vocabulary

Every material finding uses the same disposition vocabulary requested for the independent review stack:

- **FIX** — current behavior is materially harmful or violates a trust boundary; change it.
- **IMPROVE** — a net-positive change is warranted, but the best remedy need not restore literal original design.
- **KEEP** — current implementation is benign or superior; a compliance-only “fix” would add no value or risk regression.
- **AMEND** — implementation evidence justifies changing/clarifying the frozen architecture itself.
- **DEFER** — do not pre-build a solution; pilot/experiment/surface evidence should decide.

Severity is independent of disposition: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`.

---

# 1. Executive verdict

The updated audit strengthens — but also **narrows and corrects** — the previous verdict.

The implementation is still a **strong first P0.9 build**. Its product boundary, three-stage semantic topology, factual/evidence separation, dynamic-CV merge, Word-based rendering direction, job-local persistence, no-model/no-network deterministic runtime, and most of its KISS architecture are sound. Several implementation deviations from the original plan are positively valuable and should be protected from “compliance repair.”

The earlier audit was intentionally severity-heavy because it was a trust-boundary release audit. The five additional control passes show that some earlier yellow/orange findings should **not** be treated as mandatory defects:

- the personality PF catalogue is not proven harmful and should not be replaced pre-pilot merely for provenance purity;
- hash-based baseline reconciliation plus explicit human attestation is fundamentally the correct deterministic/human split;
- missing OS read-only attributes are conditional defense-in-depth, not automatically a framework defect;
- arbitrary-output `--dest`, multi-converter code and exact-PID Word cleanup are implementation-quality questions whose remedies should be judged by net value, not literalism;
- the Word COM choice, targeted master repair, Calibri retarget, semantic/date hash split, Unicode filename correction, and run-local snapshot ownership model are **positive implementation outcomes** and must not be regressed.

At the same time, the extra executable/negative-space/workflow passes found new integration defects that are more valuable than several of the earlier lower-severity findings:

1. `branch` does **not verify parent run integrity before acting**. A tampered parent can create a child before the command reports failure.
2. A tampered parent **vacancy source** can be copied into a child and `branch` can return success; the child is born integrity-invalid.
3. `branch` renames its staging directory into the canonical run tree **before** replacing `PENDING` manifest hashes in reused artifacts, creating an interruption window where a partially rebound child is visible.
4. `next --stage 3` skips a job where Stage 3 has produced a valid final package but `review.json` is missing/invalid — exactly the interruption case continuation is supposed to recover from.
5. `next` does not refuse a compromised run; unlike semantic context/validation commands, it can return success without enforcing run integrity.
6. Stage-2 wording incorrectly says to preserve claim ceilings “the strategy recorded,” which risks treating a non-factual hypothesis as the ceiling authority instead of the factual sources.
7. the PDF extraction signal currently marks even one short/weak page as `requires_source_inspection`, potentially turning a normal footer/appendix page into repeated semantic-stage friction.
8. frozen-run soft editorial warning behavior still reads current root settings rather than the run snapshot; this is low impact but a real reproducibility inconsistency.

**Current recommendation:** do one bounded perfection/repair pass before the two-real-job smoke. Fix the genuine currentness/frozen-run/branch/continuation defects, keep positive deviations, and let Codex independently adjudicate the lower-impact IMPROVE/DEFER items. There is still **no evidence requiring a wholesale architecture rewrite** and no current finding reaches a confident `AMEND` recommendation.

---

# 2. Evidence and additional controls executed

The updated audit re-used the complete evidence base from the first forensic review and added five explicit high-level control passes matching the planned independent-review stack.

## 2.1 Evidence re-opened

- full extracted `Build.zip` tree;
- final normative specification;
- final implementation and verification contract;
- final decision/adoption record;
- previous forensic audit;
- `BUILDER_REPORT.md`;
- `evidence/gates/GATE_REPORTS.md`;
- vertical-slice evidence;
- all active `runtime/jobbsok/*.py`;
- all active tests;
- stage instructions, writing doctrine, persuasion calibration and runbook;
- schemas, settings, personality profile/facet index;
- current synthetic run, frozen snapshot, current artifacts and generated views.

## 2.2 Independent test rerun

On the Linux audit host:

```text
200 passed
1 failed
7 skipped
```

The single failure is the already-known platform-specific Windows-backslash traversal fixture; the seven skips are Word COM tests unavailable on Linux. This does not invalidate the supplied Windows 208-pass evidence, but it reinforces that the suite is target-Windows oriented rather than fully portable.

## 2.3 New adversarial reproductions

### Parent frozen input tampered before branch

- tampered parent run-local `Work_experience.md`;
- invoked real `jobbsok branch`;
- command returned failure and printed `Branch refused`;
- **a child run directory nevertheless existed afterward**.

### Parent vacancy source tampered before branch

- tampered parent preserved vacancy file;
- invoked real `jobbsok branch`;
- command returned success and labelled semantic artifacts `REUSED`;
- child `verify-integrity` immediately failed because the copied vacancy hash did not match the child manifest.

### Stage-3 interrupted between final and review

- removed current `review.json` while keeping a valid final;
- status correctly showed `highest_valid_stage = FINAL`, `semantic_triage = null`;
- `jobbsok next --stage 3 --cluster c1` returned **“Nothing outstanding”**.

### Wrong semantic upstream hash

- submitted a Stage-2 draft carrying a syntactically valid but false `strategy_sha256`;
- `stage-submit` returned success and replaced the draft;
- status immediately derived the draft/final chain as `STALE`.

This confirms the existing finding that stage submission validates hash shape but not actual current upstream binding.

### Compromised run queried with `next`

- tampered a frozen run authority;
- `jobbsok next` still returned exit 0 instead of refusing the compromised run.

---

# 3. Five-direction control results

| Direction | High-level conclusion | Most important added value |
|---|---|---|
| **Architecture-intent adjudication** | Core frozen invariants remain well chosen. Several implementation deviations are better than literal historical choices and should be preserved. No current evidence demands architecture re-adjudication. | Downgraded multiple compliance-only findings; protected Word COM, master repair, font retarget, semantic/date hash split, Unicode filenames and run-local snapshots. |
| **KISS / regression resistance** | The runtime is not broadly overbuilt. The meaningful excess is concentrated in converter optionality/dead settings and a few unused schema/config surfaces. Most fixes should centralize existing invariants rather than add machinery. | Avoids wasting a top-tier repair run on PF-taxonomy replacement, semantic baseline validators, broad permission systems or new workflow engines. |
| **Executable trust-boundary forensics** | Previous core P0 findings remain valid. New branch-integrity and continuation defects were independently reproduced through public runtime paths. | Found child creation from compromised parents and Stage-3 continuation failure. |
| **Negative-space / state-transition red team** | The biggest remaining blind spots occur across transitions rather than within helpers: before/after branch promotion, after partial Stage-3 completion, after root maintenance, after render failure and under compromised-run reads. | Added branch atomicity/integrity, `next` integrity and soft-settings drift findings. |
| **Human/model workflow / pilot readiness** | Stage prompts are generally strong and faithful, but the handoff still exposes avoidable mechanical metadata burden and has two semantic/UX risks: Stage-2 claim-ceiling wording and over-eager source-inspection signalling. | Adds workflow fixes that reduce human/model friction rather than adding more validation machinery. |

---

# 4. Integrated finding register

| ID | Evidence / current state | Intended outcome | Disposition | Severity | Confidence | Best action | Regression risk |
|---|---|---|---|---|---|---|---|
| **SOL-A001** | `runtime/jobbsok/render.py` resolves masters from live root (`layout.root / spec["master"]`) although the run stores frozen master copies. Previous reproduction: corrupt root master after freeze; old run integrity remains green but historical render breaks. | A frozen run renders from the exact template bytes it froze. | **FIX** | CRITICAL | HIGH | Resolve masters from run-local frozen template records; report hashes of bytes actually consumed. Add root-mutation invariant test. | Low. Preserve the repaired master content and Word COM path; change only source resolution. |
| **SOL-A002** | `RunContext.schemas_dir = layout.schemas`; old runs validate against live root schemas. Reproduced previously by changing root package schema after freeze. | A frozen run remains governed by its frozen schema snapshot. | **FIX** | CRITICAL | HIGH | Point run validation to run-local frozen schemas. Root schemas remain maintenance input for future runs. | Low; ensure freeze/branch creation still validates new manifests against current intended schemas before snapshot. |
| **SOL-A003** | Status can derive `STALE`/`semantic_final_available=false`, yet `cmd_render` checks only mechanical final-package validity and renders anyway. Independently reproduced in first audit. | Employer documents can be produced only from a current, eligible final/review chain. | **FIX** | CRITICAL | HIGH | One central current-render eligibility guard used by `finalize` and `render`: intact run, current final, current required upstream/review, finalization state. | Medium if overimplemented. Do not create a new state machine; reuse current status/staleness primitives. |
| **SOL-A004** | `status.py` copies current `render_report.json` state/output paths without validating report schema, final/date/template/config bindings or actual output hashes. Date/report/output tampering was previously reproduced. | Current render state describes the current semantic package and actual current bytes. | **FIX** | CRITICAL | HIGH | Validate report schema + binding + exact output hashes before presenting it as current. Treat mismatch as non-current render evidence, not semantic failure. | Medium. Do not make render degradation contaminate semantic triage. |
| **SOL-A005** | `failure.record()`/`clear()` are well-designed helpers but no production stage-submit/render/finalization path calls them. Real invalid stage submission returns failure without creating current failure state. | Failed attempts differ from never-started and can progress visibly to bounded `BLOCKED_MANUAL`. | **FIX** | HIGH | HIGH | Wire existing minimal failure record into real command failure/success boundaries; validate the record schema. No workflow engine. | Medium if every benign validator warning becomes failure state. Record only actual failed attempts/blocks. |
| **SOL-A006** | Package/review schemas require upstream hashes conditionally, but validators do not compare `strategy_sha256`, `draft_sha256`, or `final_package_sha256` against actual current upstream. Reproduced: wrong strategy hash is accepted by `stage-submit`, then status immediately marks chain stale. `context` also omits these hashes. | A successful stage submission is current at birth and bound to the exact current upstream. | **FIX** | HIGH | HIGH | Emit exact current upstream hashes in Stage-2/3 handoffs and enforce them during submit/review validation. Consider deterministic stamping of non-semantic binding metadata if it materially reduces operator/model copy burden. | Medium. Do not let binding injection mutate semantic payload or obscure stage ownership. |
| **SOL-A007** | On new semantic content + failed PDF regeneration, previous pipeline-owned PDF can remain in current `out/` beside new DOCX. Reproduced previously. | Current output directory must not visually present stale PDF as current fallback. | **FIX** | HIGH | HIGH | Move/archive/mark prior pipeline-owned PDF stale when a current regeneration cannot replace it; preserve human-edited files under no-clobber rules. | Medium. Never destroy the only recoverable human-edited artifact. |
| **SOL-A008** | `branch()` does not call `require_intact(parent)` before acting. Reproduction: tampered parent frozen authority caused `Branch refused`/exit 2 **after a child run had already been created**. | No child is created from a compromised parent; every command verifies relevant frozen state before acting. | **FIX** | HIGH | HIGH | Verify complete parent integrity before collecting current child inputs or creating staging. If parent invalid, exit with zero child-side effects. | Low. `status`/diagnostic commands may still read compromised state for reporting; branch should not mutate. |
| **SOL-A009** | Parent vacancy sources are not included in branch’s pre/post parent-integrity guard. Reproduction: tampered parent vacancy was copied; branch returned success; child immediately failed `verify-integrity`. | Child branch cannot be born from corrupt parent job authority. | **FIX** | HIGH | HIGH | Same central parent `verify_frozen/require_intact` precondition must include job vacancy hashes. Add explicit adversarial test. | Low. |
| **SOL-A010** | Branch writes reused artifacts with `manifest_sha256="PENDING"`, renames staging to canonical child directory, then edits those files in place to replace `PENDING`. Interruption after rename can expose a partially rebound child. | Child creation is transactionally visible only once its manifest and current reused artifacts are internally consistent. | **FIX** | MEDIUM | HIGH | Compute child manifest file hash from deterministic serialized manifest bytes before promotion; complete all rebindings inside staging, then single rename. | Low and simplifies logic. |
| **SOL-A011** | Branch command cannot naturally reopen all frozen intake: jobs/classes/order/priority/vacancy changes require fresh freeze and lose `parent_run_id`. | Reopening a frozen element should create an ergonomic child run while parent remains untouched. | **IMPROVE** | MEDIUM | HIGH | Let branch optionally consume updated batch input/vacancies under child lineage. Keep one manifest; no amendment/version engine. | Medium. Do not turn this into generalized lineage/workflow machinery. |
| **SOL-A012** | Branch static governing-input comparison can label draft/final/review `REUSED` even when an upstream semantic artifact must regenerate. Status later catches staleness, but current directory/disposition is misleading. | Reused semantic artifacts are current only when their semantic upstream chain is also current and validated under the child. | **FIX** | MEDIUM | HIGH | Rebind only validated current chains; otherwise store descendants as prior context/history and label accordingly. | Medium. Preserve cheap reuse when all governing inputs/upstreams really match. |
| **SOL-A013** | `status.next_job()` uses `wanted = {3: ("DRAFT",)}`. Reproduced: valid final + missing review → `highest_valid_stage=FINAL`, triage null, but `next --stage 3` says nothing outstanding. | Stage-3 continuation must resume an interrupted job until **both** final and review are current/valid. | **FIX** | HIGH | HIGH | Stage-3 next-selection must treat missing/invalid/stale review as incomplete Stage 3; likewise surface explicitly requested Stage-3 RERUN work where appropriate. | Low. Avoid auto-starting RERUN; only select the job. |
| **SOL-A014** | `cmd_next` derives status without refusing run-integrity failure. Reproduced compromised run returned exit 0. | Continuation must not launch/route semantic work from a compromised run. | **FIX** | MEDIUM | HIGH | `next` should fail nonzero when `status.integrity.ok=false`; `status` itself may remain available diagnostically. | Low. |
| **SOL-A015** | `render --dest` accepts arbitrary paths outside `runs/generated` and bypasses `assert_writable`. | Deterministic runtime should not accidentally write arbitrary locations; human alternative-output needs remain simple. | **IMPROVE** | MEDIUM | HIGH | Final Codex should adjudicate net value: either constrain `--dest` to an approved export/alternate root or retain explicit human-only arbitrary destination with a documented architecture deviation. Do not add a permission framework. | Medium. Removing it without replacement can regress no-clobber usability. |
| **SOL-A016** | CV template retains an unconditional page break and actual fixture is visibly poorly balanced. GATE-05 says PASS while sparse/dense visual QA remains owed. | Representative sparse/normal/dense CVs should be visually usable without hard page-count proxy rules. | **IMPROVE** | HIGH | HIGH | Remove/condition the forced break and do target Word sparse/normal/dense visual QA. Tune layout, not semantic content or auto-fit. | Medium. Preserve chronology, readability and stable static furniture. |
| **SOL-A017** | Builder/Gate reports label several areas mechanically complete despite reproduced trust-boundary gaps; GATE-05 is PASS while explicitly incomplete. | Evidence labels must describe actual trust-boundary evidence, not helper/test-name coverage. | **FIX** | MEDIUM | HIGH | Regenerate reports after repair. Distinguish helper-tested, production-path-tested, gate-open and product-model-tested. | Low. |
| **SOL-A018** | `pdf.py` ships `word_com`, `libreoffice`, `none`, `auto`; `auto` is real failover although LO is absent. `pdf_required`, `invocation_granularity`, `mechanical_correction_attempts` are weak/dead consumers. | Baseline should carry only mechanisms with current expected value. | **IMPROVE** | LOW | HIGH | Likely delete `auto`/unused LO and dead settings unless final Codex finds a current operational consumer. Keep the adapter boundary if it naturally simplifies Word/no-PDF separation. | Medium if deletion removes useful diagnostic/future manual switch for negligible simplification. Judge net value, not purity. |
| **SOL-A019** | Word COM timeout kills/abandons the PowerShell host but does not prove cleanup of the exact spawned WINWORD instance; diagnostic claims “Word process was terminated.” | A hung conversion should not contaminate later renders or kill unrelated Word work. | **IMPROVE** | MEDIUM | MEDIUM-HIGH | Prefer exact spawned-instance/PID cleanup if it can be implemented simply and tested on target Windows. At minimum make diagnostics truthful. | High if process discovery risks killing unrelated Word. Never use global WINWORD termination. |
| **SOL-A020** | Runbook tells human to manually export PDF then rerun render “to re-verify”; current render path does not adopt that manual PDF into current render report when automation still fails. | Manual PDF fallback should be operationally clear; state should not lie. | **IMPROVE** | LOW-MEDIUM | HIGH | Either add a tiny explicit manual-PDF verify/adopt path, or correct runbook to say manual PDF remains outside automated current state. Choose the simpler real workflow after pilot surface is known. | Low. Avoid a generalized document-import subsystem. |
| **SOL-A021** | Current framework-adapted personality profile + closed PF catalogue is stronger provenance-wise than the minimum frozen wording, but the feature remains interpretive, 0–3, evidence-bound and Stage 3 may ignore it. No runtime truth elevation was found. | Personality should improve specificity without factual authority or typology leakage. | **KEEP** | INFO | MEDIUM-HIGH | Do **not** replace/re-architect pre-smoke solely for historical provenance purity. Observe real output for anchoring/formulaic trait injection; tune only on evidence. | High if a “fix” destabilizes a working 0–3 interface before any product evidence exists. |
| **SOL-A022** | Baseline reconciliation deterministically checks recorded authority hashes and requires explicit `--reviewed-by` human attestation. It cannot and should not semantically prove chronology correctness. | Human owns factual reconciliation; runtime proves version match and refuses known mismatch. | **KEEP** | INFO | HIGH | Keep the deterministic/human split. Improve wording/test identities if desired; do not build a semantic baseline judge. | High if automated semantic checking becomes false authority. |
| **SOL-A023** | OS read-only attributes promised in the original plan were not implemented; logical stage write map, path guards and run hash checks are present. | Protected inputs must not be silently mutated by semantic stages. | **DEFER** | LOW-MEDIUM | MEDIUM | Decide from GATE-01/10 surface. If semantic models get unrestricted local filesystem write access, add lightweight filesystem protection; if they only submit through controlled CLI/file handoff, existing barrier may be sufficient. | Medium: read-only attributes can complicate legitimate between-run maintenance. |
| **SOL-A024** | Date handling relies partly on schema format semantics; explicit CLI date parsing/post-write validation is weaker than ideal. | Finalization date should be valid, canonical and stable. | **IMPROVE** | LOW | HIGH | Add explicit ISO-date parsing and final-package revalidation before atomic write. | Very low. |
| **SOL-A025** | Build ZIP contains `.venv`, caches and egg-info; ~91 MB extracted for a much smaller source/evidence payload. | Handoff/release archive should be reproducible and uncluttered. | **IMPROVE** | LOW | HIGH | Clean package; reproduce environment from `pyproject.toml`/Python version. | Very low. |
| **SOL-A026** | Linux rerun: 200 pass / 1 Windows-backslash path test fail / 7 Word-COM skips. | Target-Windows tests should stay authoritative without pretending full cross-platform portability. | **KEEP** | INFO | HIGH | Mark Windows-specific fixture/platform conditions clearly if desired. Do not alter Windows behavior to make POSIX interpret backslashes as separators. | High if portability “fix” weakens target behavior. |
| **SOL-A027** | `_thresholds(layout)` reloads current root `policy/settings.toml`; soft editorial warnings are not included in manifest settings snapshot. Thus old-run warning output can drift after source maintenance. | Frozen run settings should be stable at their intended scope. | **IMPROVE** | LOW | HIGH | Either snapshot soft warning thresholds and read from manifest, or explicitly classify them as non-frozen operator display policy. Prefer the simpler consistent rule. | Low; these warnings do not affect validity. |
| **SOL-A028** | `vacancy.extract_pdf()` calls `Extraction.flag()` even for a single short/weak page; any flag becomes `requires_source_inspection=true`. Code comments acknowledge one weak footer/appendix page can be ordinary. | `requires_source_inspection` should signal actual extraction uncertainty worth repeated semantic-stage source inspection, not ordinary low-value warnings. | **DEFER** | LOW-MEDIUM | MEDIUM-HIGH | Test on real vacancy corpus. If over-triggering is common, separate nonblocking extraction warnings from the canonical inspection flag. Do not prematurely add a scoring system. | Low. |
| **SOL-A029** | Stage-2 instruction: “Preserve the claim ceilings the strategy recorded.” Frozen authority says model artifacts cannot create/raise claim ceilings; Stage 2 may reopen factual sources. | Claim ceilings come from factual authorities; strategy records a hypothesis/interpretation, not authority. | **IMPROVE** | MEDIUM | HIGH | Reword narrowly: respect factual claim ceilings; treat strategy-recorded ceilings as guidance and correct them when direct authorities establish otherwise. | Very low and likely improves Stage-2 strength without reducing truth safety. |
| **SOL-A030** | Stage bundles require models to echo multiple deterministic hashes; Stage-2/3 bundles do not currently give all required upstream hashes. This increases malformed/stale-at-birth risk and manual friction. | Semantic models should author semantics; deterministic runtime should own/derive mechanics wherever possible. | **IMPROVE** | MEDIUM-HIGH | HIGH | Minimum: expose exact current upstream hashes. Perfection option: have submission tooling stamp deterministic binding metadata around a semantic stage payload, if this can be done without weakening stage ownership/auditability. | Medium. Schema/wrapper changes can be invasive; prefer the smallest clean implementation. |
| **SOL-A031** | `context` lists writing policy for Stage 1 alongside factual inputs even though Stage-1 read-order aims to establish employer/factual grounding first. The stage instruction itself preserves the intended order. | Stage 1 should not be prematurely anchored by candidate/writing narratives. | **DEFER** | LOW | MEDIUM | No pre-smoke machinery. If selected model surface auto-loads all referenced files indiscriminately, consider stage-specific ordered bundle metadata or delaying writing-policy exposure. | Medium if removing useful writing context degrades strategy usefulness. |
| **SOL-A032** | Render promotes verified files before `cmd_render` atomically writes the new report. A process crash after promotion can leave new pipeline files with old/no current report; subsequent no-clobber logic may treat them as foreign. | Crash recovery should remain understandable without a transaction engine. | **DEFER** | LOW-MEDIUM | MEDIUM-HIGH | First see whether simple report reconciliation or write ordering can close the window. Do not build multi-file transactions/version management unless observed. Ensure fixed render-report validation at least prevents false currentness. | High if “fix” creates disproportionate transaction machinery. |
| **SOL-A033** | `failure.schema.json`, `render_report.schema.json` and `status.schema.json` exist, but current production paths do not consistently validate these generated/current records against their schemas. | Canonical current records should not become trusted state merely because a helper produced JSON. | **IMPROVE** | MEDIUM | HIGH | Wire failure/render-report schema validation into the same currentness boundaries already being fixed. Validate status before persistence if essentially free; do not add redundant schema layers. | Low. |
| **SOL-A034** | `pilot/` exists but no header-only pilot log is shipped. | First real smoke should capture human quality/effort evidence without relying on memory. | **IMPROVE** | LOW | HIGH | Ship a simple header-only `PILOT_LOG.csv` before smoke. | Very low. |
| **SOL-A035** | Target machine lacks LibreOffice; installed Word COM successfully produced PDFs. | Use the simplest proven converter on the actual machine. | **KEEP** | INFO | HIGH | Keep Word COM as default. Do not reinstall/reintroduce LibreOffice merely for P0.7 parity. | High if compliance repair restores an unneeded dependency. |
| **SOL-A036** | Original P0.7 masters were Word-corrupt; targeted `prepare_masters.py` repair preserves SDT contract/layout and archived originals. | Produce Word-openable masters while preserving proven template capital. | **KEEP** | INFO | HIGH | Keep targeted repair unless later visual evidence motivates template redesign. | High if replaced wholesale without need. |
| **SOL-A037** | Both original template fonts were unavailable; masters were retargeted to installed Calibri and resulting PDFs show correct Norwegian glyphs/subsets. | Deterministic target-machine layout without silent substitution. | **KEEP** | INFO | HIGH | Keep Calibri unless GATE-05 visual QA shows an actual quality reason to change. | Medium if typography is changed for theoretical preference before QA. |
| **SOL-A038** | `artifact_hash()` excludes `finalization` for semantic package identity so date assignment invalidates render only, not review. | Date finalization must not force pointless Stage-3 semantic rerun. | **KEEP** | INFO | HIGH | Preserve semantic-vs-finalization hash separation; fix render-currentness around it rather than folding date back into semantic hash. | CRITICAL if “fixed” by hashing date into review identity. |
| **SOL-A039** | P0.7 ASCII folding deleted Norwegian letters; P0.9 maps `ø/æ/å` deterministically before ASCII filename folding. | Employer-facing filenames remain intelligible and portable. | **KEEP** | INFO | HIGH | Preserve the Norwegian fold and collision/path tests. | High if reverted to P0.7 behavior. |
| **SOL-A040** | Freeze creates run-local copies of authorities, policies, schemas, templates, maps and context. This is stronger/cleaner than letting active source maintenance govern an in-flight run. | Historical reproducibility plus safe between-run source maintenance. | **KEEP** | INFO | HIGH | Keep snapshot ownership model; repair all consumers so they consistently read it. | CRITICAL if “simplified” back to live-root reads. |
| **SOL-A041** | Evidence index and `EV:`/`BL:` namespace separation are lean, deterministic and nonsemantic. | Source navigation/provenance without ranking or claim-graph machinery. | **KEEP** | INFO | HIGH | Preserve. | High if replaced by RAG/ranking/manual claim graph in baseline. |
| **SOL-A042** | Stage 1/2/3 instructions and writing doctrine broadly implement vacancy-first reasoning, native Bokmål, CV/letter complementarity, Stage-3 elasticity and factual boundaries. No hard semantic count gates found. | High-quality semantic system whose models remain truth-bound but not mechanically overconstrained. | **KEEP** | INFO | HIGH | Preserve core prompt architecture; apply only targeted wording/handoff improvements such as SOL-A029/A030. | High if a mechanical “cleanup” simplifies away semantic quality guidance. |

---

# 5. Adjudication changes from the previous forensic audit

This section is deliberately explicit so a final repair agent does **not** consume the earlier severity labels mechanically.

| Previous finding | Updated disposition | Why |
|---|---|---|
| multi-converter / LibreOffice adapter | **IMPROVE**, low severity | It is unnecessary baseline surface, but current default behavior is Word COM and there is no demonstrated correctness harm. Delete only if simplification is net-positive. |
| exact Word PID cleanup | **IMPROVE**, medium | Orphan-process risk is plausible, but exact-PID machinery is not itself a frozen architectural invariant. Fix only with a safe target-Windows design that cannot kill unrelated Word. |
| personality profile / PF closed catalogue | **KEEP** pre-pilot | No evidence it causes truth inflation or poor writing. Replacing it now for provenance purity would spend complexity before product evidence. |
| baseline reconciliation “insufficient” | **KEEP** core design | Deterministic hashes + explicit human reconciliation is the right authority split. Do not build a semantic truth checker. |
| OS read-only attributes absent | **DEFER** | Whether this matters depends on the actual GATE-01/10 model surface and its filesystem permissions. Logical stage/CLI restrictions may be sufficient. |
| arbitrary `--dest` | **IMPROVE**, not hard blocker | It is a literal write-root deviation but has real no-clobber utility. Final Codex should choose the cleanest explicit-human behavior, not remove it reflexively. |
| child branch cannot change full inventory | **IMPROVE** | It weakens reopen ergonomics but does not corrupt ordinary runs; improve without adding lineage machinery. |
| GATE-05/page balance | **IMPROVE**, high | The known forced-break layout weakness is real and should be addressed before quality measurement, but it is a product/layout issue rather than a broken state invariant. |
| pilot log absent | **IMPROVE**, low | Cheap and useful, but not evidence that runtime mechanics are broken. |
| Linux backslash traversal test | **KEEP** target behavior | Cross-platform test portability is not worth weakening Windows path semantics. |

The following earlier findings remain unequivocal **FIX** items: live schemas/templates, stale-final rendering, render-report currentness, real failure lifecycle, semantic upstream binding, stale old PDFs, misleading branch currentness, and report evidence overclaim.

---

# 6. Pre-live-smoke priority set

## 6.1 Must FIX before the two-real-job smoke

These can contaminate the smoke by making outputs/state untrustworthy or by breaking the documented continuation path:

1. `SOL-A001` — render from frozen templates.
2. `SOL-A002` — validate from frozen schemas.
3. `SOL-A003` — refuse render/finalize from stale/non-current semantic final.
4. `SOL-A004` — validate render-report currentness and actual output hashes.
5. `SOL-A005` — integrate current failure/BLOCKED lifecycle into real commands.
6. `SOL-A006` — enforce actual semantic upstream hashes at submission/review; expose them cleanly.
7. `SOL-A007` — remove stale old pipeline PDF from current-output presentation after degraded regeneration.
8. `SOL-A008` / `SOL-A009` — branch must require complete parent integrity before any child side effect.
9. `SOL-A010` — complete child rebind inside staging before child becomes visible.
10. `SOL-A012` — child semantic reuse must respect current upstream chain.
11. `SOL-A013` — Stage-3 continuation must recover final-without-review / invalid-review jobs.
12. `SOL-A014` — `next` must not route work from a compromised run.
13. `SOL-A017` — regenerate builder/gate claims after actual repairs.

## 6.2 Improve before smoke if cheap/high-value

These are not trust-boundary blockers, but known behavior could distort pilot quality or create avoidable operator friction:

- `SOL-A016` — fix forced page break / complete GATE-05 sparse-normal-dense QA.
- `SOL-A029` — correct Stage-2 claim-ceiling authority wording.
- `SOL-A030` — reduce hash-copy friction; at least put exact upstream hashes in bundles.
- `SOL-A034` — ship pilot-log header.
- `SOL-A024` — explicit date parsing.

## 6.3 Let Codex adjudicate dynamically

These should **not** be treated as mandatory compliance tasks:

- `SOL-A011` branch full-intake reopen UX;
- `SOL-A015` arbitrary `--dest` behavior;
- `SOL-A018` converter/setting cleanup;
- `SOL-A019` exact Word cleanup mechanism;
- `SOL-A020` manual PDF adoption UX;
- `SOL-A023` OS read-only layer;
- `SOL-A027` soft-warning snapshot semantics;
- `SOL-A028` source-inspection threshold;
- `SOL-A031` Stage-1 policy-loading order;
- `SOL-A032` render promotion/report crash window;
- `SOL-A033` whether all generated views merit schema validation.

The correct decision for each is whatever maximizes framework value with the least permanent machinery.

---

# 7. Positive deviations / invariants a final Codex pass must protect

The final perfection run should treat these as regression guards, not cleanup targets:

1. **Word COM as target converter** (`SOL-A035`).
2. **Targeted Word-master OOXML repair**, not wholesale template replacement (`SOL-A036`).
3. **Calibri retarget based on actual installed-font evidence** (`SOL-A037`), subject only to visual QA.
4. **Semantic package hash excludes finalization metadata** (`SOL-A038`).
5. **Norwegian filename folding explicitly preserves `ø/æ/å` semantics** (`SOL-A039`).
6. **Run-local frozen snapshot ownership model** (`SOL-A040`).
7. **Lean evidence index and strict EV/BL namespace separation** (`SOL-A041`).
8. **Three semantic stages with true Stage-3 elasticity** (`SOL-A042`).
9. **No portal/channel/language/output-mode product branching.**
10. **PDF degradation remains orthogonal to semantic state.**
11. **Human-edited output no-clobber principle.**
12. **Mechanical validators never become semantic truth/persuasion judges.**

---

# 8. Architecture amendment assessment

**Current recommendation: no architecture amendment is necessary before the repair/perfection pass.**

The newly discovered defects are implementation failures to enforce already-intended invariants, not evidence that those invariants are wrong.

The useful implementation deviations are already within existing builder freedom or can be retained as evidence-backed implementation choices.

Potential later amendments should require real pilot evidence. In particular:

- do not amend personality until actual package quality shows recurrent anchoring/formulaic expression;
- do not amend source-inspection semantics until real vacancies show the signal materially overfires;
- do not amend stage topology based on current handoff friction; deterministic metadata stamping can solve most of it without another semantic stage;
- do not amend converter policy unless target-machine Word behavior proves unreliable in real production.

---

# 9. High-value regression / adversarial tests for the repair pass

Prefer these integration tests over expanding helper-level unit counts.

1. **Root-template invariance:** freeze → mutate root master → historical render uses frozen master and remains logically identical.
2. **Root-schema invariance:** freeze → mutate root schema → historical validation unchanged.
3. **Root-settings scope:** mutate current soft-warning settings → old run behavior follows explicitly chosen snapshot/non-frozen policy.
4. **Stale final cannot render:** replace draft → final/review stale → `finalize` and `render` nonzero with no employer-output mutation.
5. **Render report final binding:** alter final/date/template binding → status must not show current render OK.
6. **Render output tamper:** change actual output bytes → render state no longer current.
7. **Real failed submit lifecycle:** invalid `stage-submit` → current failure appears; valid resubmit clears/archives it.
8. **Retry exhaustion path:** real operator path reaches `BLOCKED_MANUAL`; helper-only test is insufficient.
9. **Wrong strategy hash:** Stage-2 artifact carrying non-current strategy hash is rejected at submission, not accepted then marked stale.
10. **Wrong draft hash:** Stage-3 final carrying non-current draft hash is rejected.
11. **Wrong final hash in review:** review rejected immediately.
12. **Stale PDF removal:** new DOCX + failed new PDF cannot leave old pipeline PDF looking current.
13. **Compromised-parent branch:** tamper any frozen parent asset → `branch` creates no child directory.
14. **Tampered parent vacancy:** same, including job-source hashes.
15. **Branch interruption atomicity:** injected failure before final promotion leaves no canonical child; after promotion child is internally consistent.
16. **Branch changed Stage-1 policy:** descendants not labelled/current-reused unless upstream chain is valid in child.
17. **Stage-3 interrupted final/review:** valid final + missing/invalid review → `next --stage 3` selects that job.
18. **Compromised run continuation:** `next` returns nonzero and tells operator to restore/branch.
19. **Render destination policy:** test whichever explicit-human destination rule is adopted.
20. **Word timeout isolation:** target Windows proves no orphaned owned Word process and no unrelated Word process is killed.
21. **Sparse/normal/dense CV visual fixtures:** human-reviewed target Word/PDF output after page-break correction.
22. **Manual PDF fallback:** if an adoption path is built, prove exact final/date binding; if not, prove documentation does not imply automated adoption.
23. **Single weak PDF footer:** representative vacancy demonstrates whether inspection signal should remain hard or warning-only.
24. **Stage handoff ergonomics:** generated Stage-2/3 bundle contains every deterministic value required to create a valid current artifact without manual hashing.

The traceability test may remain useful as a coverage-index regression guard, but it must never be cited as proof that an ACC/GATE is behaviorally satisfied merely because a named test exists.

---

# 10. Human/model workflow assessment

## 10.1 What is already strong

The semantic control plane is better than the raw implementation defects might imply:

- Stage 1 is vacancy-first and explicit about not vetoing a human-approved job.
- factual authorities remain the only candidate-fact source.
- Stage 1 personality is sequenced after factual grounding.
- Stage 2 is explicitly native Bokmål and requires both CV and letter.
- dynamic CV ownership is narrow and clear.
- Stage 3 is genuinely told to form an independent view before reading upstream work.
- Stage 3 is allowed to discard/reconstruct strategy without compliance explanation.
- final evidence refs are explicitly synchronized after reconstruction.
- review triage is based on repair scope, not reason count.
- writing doctrine strongly protects restrained Norwegian style and CV/letter complementarity without converting subjective style into deterministic regex failure.

These should be preserved.

## 10.2 Main workflow risks before live use

### Mechanical binding burden

The model is asked to output hashes that deterministic code already knows. This is low-value model work and creates a class of preventable stale-at-birth failures. At minimum, the context bundle should give every required value and validators should compare it immediately. A clean deterministic wrapper/stamp could be superior if it stays small.

### Stage-3 two-artifact completion

Stage 3 completion is final + review, but the current `next` logic models “FINAL exists” as enough to skip the job in a stage-specific continuation. This is a genuine user-flow defect, not a theoretical state-machine nit.

### Strategy claim-ceiling wording

Stage 2 must not treat a strategy-recorded ceiling as higher authority than direct factual sources. The current wording is likely to bias the writer toward unnecessary conservatism if Stage 1 under-read evidence. The fix is one sentence, not a new mechanism.

### Source-inspection signalling

The current extraction code may turn an ordinary weak footer page into repeated “inspect original” work for every semantic stage. Real vacancy examples should determine whether this is a material burden.

### Surface portability remains unresolved

The current stage context bundle mostly provides local filesystem paths. That is excellent for directly integrated local agents, but a web-only semantic surface may require manual upload/export packaging. This is properly a GATE-01/GATE-10 question. Do not pre-build a context packaging subsystem until the actual pilot surface is chosen.

---

# 11. KISS / complexity assessment

The build is **not broadly overengineered** despite its ~6k runtime LOC.

Most permanent code supports real boundaries:

- immutable manifests/snapshots;
- document generation/OOXML;
- evidence indexing;
- state/currentness;
- validation;
- Word/PDF conversion and checking;
- filesystem safety;
- deterministic CV merging.

The main KISS opportunities are local:

- remove unused converter failover/settings if they do not earn their existence;
- centralize currentness/eligibility rather than duplicating checks;
- reuse schema validation for failure/render reports instead of inventing parallel checks;
- deterministically derive mechanical binding metadata where possible;
- fix branch atomicity with precomputed manifest bytes/hash rather than adding transaction machinery;
- do not add an event log, dependency graph, generalized retry engine, permissions framework, document version manager, RAG layer or semantic judge.

The correct repair style is **fewer stronger boundaries**, not more architecture.

---

# 12. Updated release recommendation

## Current state

- **Architecture:** sound; remain frozen.
- **Implementation foundation:** strong.
- **Mechanical trust boundaries:** not yet release-clean.
- **Semantic prompts/policies:** strong enough for pilot after targeted wording/handoff fixes.
- **Builder evidence report:** must be regenerated after repairs.
- **Two-real-job smoke:** **NO-GO until the §6.1 FIX set is closed.**

## Go condition

Proceed to the live two-job smoke when:

1. all current frozen-run consumers use correct run-local frozen inputs;
2. stale/non-current finals cannot finalize/render;
3. render-report state is bound to actual current bytes;
4. real command failures persist/clear current failure state correctly;
5. upstream semantic hashes are supplied and enforced;
6. stale prior PDFs cannot masquerade as current after degradation;
7. branch cannot act on a compromised parent and becomes transactionally consistent;
8. Stage-3 continuation correctly handles missing/invalid review;
9. known CV forced-page-break issue has been repaired or at minimum visually requalified before measuring product quality;
10. builder/gate evidence is regenerated honestly.

Then:

1. execute GATE-10 role/privacy mapping;
2. run two real jobs through all three stages;
3. score actual package quality and human effort;
4. run representative cluster pilot;
5. use pilot evidence — not architectural intuition — to decide personality/source-inspection/context-packaging/other deferred refinements.

---

# 13. Final handoff principle for the Codex perfection pass

The final repair agent should **not** interpret this document as a patch list whose rows must all be implemented.

For `FIX`, independently reproduce or inspect the claimed failure, then close it with the smallest robust change and an integration regression test.

For `IMPROVE`, compare current implementation, frozen design, user-value objective and proposed remedy; implement only when net positive.

For `KEEP`, actively protect the current behavior from compliance-driven regression.

For `DEFER`, do not build machinery before the relevant pilot/surface evidence exists.

For `AMEND`, none is currently required; any future amendment needs stronger evidence than “the implementation is different.”

The target is not a perfectly obedient implementation of P0.9. The target is the **best truthful, low-friction, mechanically trustworthy Jobbsøk_26 framework that preserves the architecture’s valuable intent while improving on it where empirical evidence justifies doing so.**
