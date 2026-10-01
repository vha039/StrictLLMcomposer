I'll start by orienting myself in the repository structure.

Canonical build verified untouched; all destructive work ran on scratch copies at a short path. Here is the audit.

---

# P0.9 `Build/` — Forensic Audit (independent, executable)

**Baseline read:** `/AGENTS.md`, `P0.9_FINAL_NORMATIVE_SPECIFICATION.md` (rev 0.9.0, `FROZEN_NORMATIVE`), `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`.
**Method:** static read of all 23 runtime modules, then falsification through the public CLI (`jobbsok …`) against scratch copies at `…\Temp\claude\jb\A` (short path chosen because `paths.MAX_PATH_CHARS=240` and Word's 260-char limit are themselves under test). Canonical `P0.9/Build/` was read-only throughout; re-verified at the end: `verify-integrity` intact, 4/4 artifacts valid, `templates/CV_MASTER.docx = a8f90a50f3c0801d` unchanged.
**Baseline claim reproduced:** `208 passed in 138.55s`.
**No prior external forensic audit exists in the repo** (searched `**/*audit*`, `*review*.md`, `*critique*`). The only prior self-assessment is `BUILDER_REPORT.md`, read *after* the findings below were established; comparison in §6.

---

## 1. The invariants the architecture actually needs

Stripped to what must hold or the product breaks:

| ID | Invariant | Source |
|---|---|---|
| **I1** | After freeze, no maintained repo file may change any command's behaviour or output *for that run*. | DEC-40, Spec 7.3, Contract 6.2 |
| **I2** | A command that produces or blesses employer-facing output must **refuse** when the state axes say the artifact is not current. | Spec 7.6, Contract 7 |
| **I3** | Every derived artifact (render report, delivered DOCX/PDF) is "current" only if provably bound to the current final. | DEC-26, DEC-42 |
| **I4** | Every state the spec requires must be reachable through a **public** command, not only a helper. | DEC-07, CTR-03, ACC-05/14 |
| **I5** | Every write lands under a writable root, through no reparse point. | Spec 17.2, Contract 15, ACC-19 |
| **I6** | Every hash or diagnostic a report asserts must describe what actually happened. | INV-02, Spec 14.3 |
| **I7** | A child run whose governing hashes are identical is immediately usable without regeneration. | Spec 5.4, Contract 6.3.6 |
| **I8** | The employer-facing document date and approval are operator acts, never model-authored fields. | DEC-38, INV-09, Contract 22 |

**I1, I2, I3, I4, I5, I6, I7 and I8 are all falsifiable through public commands today.** Details follow.

---

## 2. Material findings

### F-01 — A frozen run validates against **live** schemas

| | |
|---|---|
| **Invariant** | I1 · `DEC-40`, Spec 7.3, Contract 6.2 |
| **Path** | [validate.py:44](P0.9/Build/runtime/jobbsok/validate.py:44) `RunContext.__init__` → `self.schemas_dir = layout.schemas`; consumed by `validate_against_schema(..., context.schemas_dir, ...)` in `validate_strategy` / `validate_package` / `validate_review`. Reached by `validate`, `status`, `stage-submit`, `finalize`, `render`. |
| **Evidence** | Appended `"ZZZ_INJECTED_BY_AUDIT"` to `required` in the **live** `schemas/package.schema.json`. `verify-integrity` → `all frozen inputs intact` (exit 0). `validate --run r20260823-050000-fea486` → `2 failed`, `CTR-05 … 'ZZZ_INJECTED_BY_AUDIT' is a required property`. |
| **Consequence** | Editing `schemas/` between runs retroactively changes what a frozen run accepts. Loosening a schema silently re-blesses artifacts a frozen run rejected; tightening it red-lights in-flight runs. `runs/<id>/frozen/schemas/*.json` **exist and are hash-verified but are never read.** The build's own stated model ("a run reads its inputs from its own `frozen/` copies") does not hold here. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | `RunContext.schemas_dir = layout.run_dir(run_id) / "frozen" / "schemas"`. The frozen copies already exist, already hash-verify, and `schemas._load` is keyed on the directory. One line. |
| **Regression test** | Freeze; loosen a live schema so a deliberately invalid package would pass; assert `validate` still fails and `verify-integrity` still passes. |

---

### F-02 — `render` builds employer documents from the **live** Word masters, and the render report asserts the frozen hash it did not use

| | |
|---|---|
| **Invariant** | I1 + I6 · `DEC-40`, `DEC-30`, `ACC-04`, Spec 14.3 |
| **Path** | [render.py:_build_document](P0.9/Build/runtime/jobbsok/render.py) → `write_filled_docx(layout.root / spec["master"], …)`. `spec["master"]` is `"templates/CV_MASTER.docx"` (from the *frozen* template map), resolved against the **live** root. `_build_report` then writes `binding.cv_master_sha256 = manifest["frozen_inputs"]["templates"]["cv_master"]["sha256"]` — copied from the manifest, never measured. |
| **Evidence** | Injected `AUDITMARKER_` into the first `w:t` of the live `templates/CV_MASTER.docx` (the candidate name line). `verify-integrity` → intact, exit 0. `render --force` → `[OK] CV: OK/OK`. Extracted DOCX text: first line `AUDITMARKER_VEGARD HØLAND`. Render report: `cv_master_sha256 = a8f90a50f3c0801d`; **actual file used = `83113ac91b6cc211`**. Every DOCX check passed, including `identity_present: True`. |
| **Consequence** | The one plane that reaches the employer is not frozen. Any edit to `templates/` — including a well-intentioned styling fix between runs — silently rewrites already-delivered runs' output, and the render report **certifies a hash that was not used**. That is a false provenance record under `INV-02`, worse than the read itself. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | **Critical** / Certain (reproduced end-to-end) |
| **Smallest remedy** | Resolve `spec["master"]` through `frozen_path(layout, run_id, read_frozen(manifest, "templates", …))`, and populate the report's `*_master_sha256` from `sha256_file()` of the file actually opened, not from the manifest. |
| **Regression test** | Render; mutate the live master; re-render with `--force`; assert the output text is unchanged **and** `render_report.binding.cv_master_sha256 == sha256_file(master actually read)`. |

---

### F-03 — `validate`, `finalize` and `render` all ignore `STALE`

| | |
|---|---|
| **Invariant** | I2 · Spec 7.6 ("`STALE` … prevents an artifact from being treated as current completion"), Contract 7 ("a stale … final MUST NOT be presented as current ready output") |
| **Path** | `cmd_render` ([cli.py:365-424](P0.9/Build/runtime/jobbsok/cli.py:365)) loads the final and calls `validate_artifact` only — `evaluate_staleness` is never consulted. `cmd_finalize` likewise. `cmd_validate` prints staleness but `failures` counts only validation errors; `artifacts.evaluate_staleness` emits `severity="WARNING"`, and `ValidationResult.ok` ignores warnings. |
| **Evidence** | Replaced the strategy via `stage-submit --stage 1`. `status` → `production: STALE`, `semantic final available: 0`. Then: `validate` → `Checked 4 artifact(s); 0 failed`, **exit 0**. `finalize --date 2026-09-01` → `Finalized … with document date 2026-09-01`, exit 0. `render --force` → `[OK] … CV: OK/OK letter: OK/OK`, exit 0, four employer-facing files replaced. |
| **Consequence** | Status reports the state correctly and every command that *acts* on it ignores it. The operator gets a canonical employer document date and a full CV+letter set generated from a package the system simultaneously reports as not current. This is the single clearest instance of "commands respect state" failing while "status reports it" succeeds. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | In `cmd_render` and `cmd_finalize`, call `evaluate_staleness` and refuse (`EXIT_JOB_FAILURE`) when `final_package` ∈ stale, unless an explicit `--allow-stale`. In `cmd_validate`, count stale artifacts toward the exit code (or raise the staleness violation to `ERROR` and let `ok` do the work). |
| **Regression test** | Replace the strategy; assert `render`, `finalize` exit non-zero and write nothing; assert `validate` exits non-zero. |

---

### F-04 — Render currentness is never derived; `DEC-26`'s `final replaced → render` row is unimplemented

| | |
|---|---|
| **Invariant** | I3 · `DEC-26`, `DEC-42`, `ACC-05`, `ACC-06` |
| **Path** | [status.py:_derive_job](P0.9/Build/runtime/jobbsok/status.py) copies `report["render_state"]` verbatim and never compares `report["binding"]["final_package_sha256"]` with `artifact_hash(current final)`. `artifacts.evaluate_staleness` iterates only `UPSTREAM_BINDING` (`draft`, `final`, `review`); `"render"` appears in `STALE_SCOPE` but is filtered out by `if downstream in ARTIFACTS`. `STALE_SCOPE["document_date"]` has no consumer at all. |
| **Evidence** | Rendered cleanly, then submitted a new final via `stage-submit --stage 3` (headline changed). `status --json`: `render_state.overall = "OK"`, `counts.render = {OK: 1}`, four `output_paths` listed in the queue. Report binds `final_package_sha256 = 74e87c0e65ea7475`; hash of the current final `= ba242bf5e3f30a73`. Delivered CV on disk still carries the **old** headline (`"Beslutningsstøtte…"`, new headline absent). |
| **Consequence** | The run reports a fully rendered job whose employer-facing documents do not match its current semantic final, and the queue lists those files as `output:`. In a 40-job batch this is precisely the state that gets submitted. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | In `_derive_job`, when a report exists, compare its `final_package_sha256` and `document_date` against the current final; on mismatch set `render_state.overall = "STALE"` and drop `output_paths` (or label them superseded). Also add `render` to what `render`/`status` treat as invalidated. |
| **Regression test** | Render → replace the final → assert `render_state.overall != "OK"` and `counts.render.OK == 0`. (Note: `_write_render_report` in the test suite hard-codes `final_package_sha256 = "0"*64` — an impossible hash — and status accepts it. Delete that shortcut.) |

---

### F-05 — A Stage-3 model artifact can assign the canonical employer-facing document date

| | |
|---|---|
| **Invariant** | I8 · `DEC-38` ("becomes canonical when the final semantic package is **explicitly finalized/approved**"), `INV-09`, Contract 14.4, Contract 22 ("document date at run freeze or render-time drift") |
| **Path** | `schemas/package.schema.json` **requires** `finalization` on `source_stage == "STAGE3_FINAL"` and permits `state: "FINALIZED"` with any `document_date`. `render_job` accepts it (`if finalization.get("state") != "FINALIZED" …`). `cmd_finalize` then refuses to touch it (`Already finalized on …`). No stage instruction tells the model what to put in `finalization` — `grep -i "finalization\|document_date\|FINALIZED" policy/stages/*.md` returns **nothing**. |
| **Evidence** | Submitted a final with `finalization = {state: FINALIZED, document_date: "2019-01-02", finalized_by: "stage-3 model"}` via `stage-submit --stage 3`. `render --force` with **no** `finalize` step → `[OK]`. Extracted letter text: `Oslo, 2. januar 2019`. `finalize` → `Already finalized on 2019-01-02.` |
| **Consequence** | A required field the Stage-3 instruction never specifies, whose most natural model guess (`FINALIZED` + today) bypasses the operator's approval act entirely, and whose wrong value ships visibly on the letter. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | Reject `finalization.state == "FINALIZED"` in `validate_package` when the payload arrives through `stage-submit` (model-authored finals must be `{"state": "DRAFT"}`); `finalize` remains the only writer of `FINALIZED`/`document_date`. Add one paragraph to `stage3_final_writer_review.md`. |
| **Regression test** | `stage-submit` a final with `state: FINALIZED` → refused; `render` on a `DRAFT` final → `JobError` naming `DEC-38`. |

---

### F-06 — Promotion ownership amnesia: one transient failure makes the pipeline call its own output "edited outside this pipeline", permanently

| | |
|---|---|
| **Invariant** | I6 + Spec 16.6 / `ACC-17` |
| **Path** | `render._previous_output_hashes` reads only the **latest** report. Any per-document failure or PDF degradation writes a report with `output_path: null` / `output_sha256: null`, erasing the hash the pipeline recorded. The next healthy render sees `expected_sha256=None` and `atomicio.promote_file` returns `REFUSED_FOREIGN`. |
| **Evidence** | (1) healthy render → `docx/cv: f56934f2`, file on disk `f56934f2`. (2) renamed the `CV_PROFILE` control in the master → `[FAILED] cv.docx: Expected exactly one block content control CV_PROFILE; found 0`, exit 1. (3) restored the master, nothing human-edited → `[FAILED] cv.docx: existing file preserved because no prior render recorded a hash for this file` / `action: The existing file was edited outside this pipeline and has been preserved.` Recovery impossible without `--force`. |
| **Consequence** | A **false** claim of human authorship, and it trains the operator to run `--force` habitually — which destroys the genuine `ACC-17` protection the mechanism exists for. It also fires on every PDF after any degradation (see F-14). |
| **Disposition** | **FIX** |
| **Severity / Confidence** | Medium-High / Certain |
| **Smallest remedy** | Carry forward the previous report's `output_sha256` for any document the current render did not successfully promote (merge, don't overwrite), so a failed attempt never erases ownership. Reword the note to distinguish "unknown provenance" from "edited outside this pipeline". |
| **Regression test** | render OK → force a per-document failure → restore → render; assert `promotion == "REPLACED"`, not `REFUSED_FOREIGN`. |

---

### F-07 — `render` never enforces the template control contract; an unknown control ships its content to the employer

| | |
|---|---|
| **Invariant** | Spec 16.3 ("Unknown, duplicate or missing required template controls MUST fail preflight rather than be ignored"), Contract 13.3 |
| **Path** | `docxfill.require_template_contract` is called **only** from `cmd_preflight`. The render transaction (`_build_document`) fills known tags, then `unwrap_content_controls` unwraps **every** `w:sdt` including unknown ones, and `assert_no_controls` passes because they were unwrapped. |
| **Evidence** | Cloned an existing SDT in the live CV master, retagged it `CV_UNKNOWN_LEFTOVER`, set its text to `INTERN NOTAT: ikke send til arbeidsgiver`. `preflight` → `[ERROR] DEC-30 templates/CV_MASTER.docx:controls`. `render --force` → `[OK] CV: OK/OK`. Extracted DOCX text: **`INTERN NOTAT` present**. |
| **Consequence** | The only defense against a stray control is a separate optional command reading the *live* master. Combined with F-02, a single master edit between preflight and render puts internal text into a delivered CV. The leakage scanner correctly does not catch this (it is narrow by design, per Spec 14.2) — the control contract is the intended defense and it is out of the path. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | Call `require_template_contract(frozen_master, expected)` inside `render_job` before `_build_document`, per document. |
| **Regression test** | Add an unknown control to the master; assert `render` fails that document and produces no output. |

---

### F-08 — Branch is functionally broken: an identical-input child is always `STALE`

| | |
|---|---|
| **Invariant** | I7 · Spec 5.4, Contract 6.3.6, Contract 17.1-T2, `ACC-03` |
| **Path** | `branch.branch` rebinds `binding.run_id` and `binding.manifest_sha256` on each `REUSED` artifact. `artifacts.artifact_hash` hashes the whole payload except `finalization` — so rebinding changes each artifact's canonical hash. The downstream pointers `binding.strategy_sha256`, `draft_sha256`, `final_package_sha256` are **not** rebound. |
| **Evidence** | Clean branch, every governing hash identical: `strategy=REUSED, draft_package=REUSED, final_package=REUSED, review=REUSED`. Child `status`: `production_state: STALE`, `highest_valid_stage: STRATEGY`, `stale_scope: [draft, final, review]`, `semantic_final_available: False`. Child `validate` emits three DEC-26 warnings, each falsely stating *"the strategy was replaced"* / *"the draft_package was replaced"* — nothing was replaced. |
| **Consequence** | Branching is the **only** legal way to change any frozen input (`DEC-40`), and every branch throws away the whole batch's semantic work, forcing Stage 1→2→3 for every job. The contract explicitly permits the rebind so that this does *not* happen. The diagnostics are also factually wrong. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | Exclude `binding.run_id` and `binding.manifest_sha256` from `artifact_hash` — the same treatment already correctly applied to `finalization`, and for the same reason (identity/provenance metadata is not the semantic payload). Alternative: rebind downstream pointers in the same pass. Prefer the former; it also makes the child's `binding` rebind hash-neutral by construction. |
| **Regression test** | Branch with identical inputs → assert child `production_state == "VALID"`, `highest_valid_stage == "FINAL"`, `semantic_final_available is True`. **The existing `test_t02_*` never derives the child's status** — that is why this passes today. |

---

### F-09 — `render --dest` is completely unvalidated: writes into protected roots, outside the build root, and accepts traversal

| | |
|---|---|
| **Invariant** | I5 · Spec 17.2, Contract 15, `ACC-19`, `ACC-04`, Contract 3 |
| **Path** | `cmd_render` passes `Path(args.dest)` straight to `render_job(destination=…)`, which does `out_dir.mkdir(parents=True)`. `paths.assert_writable` and `paths.assert_protected` exist, are correct, and are **called by no production code** — `grep` finds callers only in `runtime/tests/`. `resolve_within` has exactly one production caller (`manifest.freeze`, for the vacancy source). |
| **Evidence** | `render --dest "$R/authorities"` → exit 0; `ls authorities/` now shows `CV_…docx`, `CV_…pdf`, `Soknad_…docx`, `Soknad_…pdf` beside `Work_experience.md`, `Education.md`, `Other_high_value_information.md`, `CV_BASELINE.md`. `--dest C:/…/ESCAPED` (outside the build root) → exit 0, files written. `--dest "$R/runs/<id>/jobs/../../../templates"` → exit 0, files written into `templates/`. |
| **Consequence** | The protected data plane and the control plane are writable through a normal, documented flag with no diagnostic. Contract 3's permission separation is documentation, not enforcement. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | Medium-High / Certain |
| **Smallest remedy** | `assert_protected(layout, dest)` then `assert_writable(layout, dest)` in `cmd_render` before use. Both functions already do exactly the right thing. |
| **Regression test** | `--dest` into each protected root, outside the root, and with `..` → all exit 2 with a `PathSafetyError`; assert no file was created. |

---

### F-10 — Reparse points are detected correctly and consulted nowhere on the write path

| | |
|---|---|
| **Invariant** | I5 · Spec 17.2 ("reject traversal and **deliberately handle** symlinks/reparse points") |
| **Path** | `paths.is_reparse_point` is reachable only from `resolve_within`, whose single production caller is `freeze` (vacancy source). No write — `atomic_write_bytes`, `promote_file`, `submit`, `shutil.copy2` in freeze/branch — passes through it. |
| **Evidence** | `New-Item -ItemType Junction` replacing `runs/<id>/jobs/testetaten_radgiver/out` → junction to `…\Temp\claude\JUNCTION_TARGET`. `is_reparse_point(out/) = True` (the helper is correct). `render --job testetaten_radgiver` → `[OK]`, exit 0, no diagnostic. All four employer deliverables landed in `JUNCTION_TARGET`, outside the run tree. |
| **Consequence** | Same root cause as F-09: correct primitives, no wiring. Exploitability on a single-user machine is low, but the obligation is explicit and the builder report cites "real junction rejection" as evidence for this area. |
| **Disposition** | **FIX** (bundle with F-09) |
| **Severity / Confidence** | Medium / Certain |
| **Smallest remedy** | Route the render out-dir, the transaction dir and job-artifact writes through `assert_writable` (which already ends in `resolve_within`, which already checks every component). |
| **Regression test** | Junction any job `out/` → `render` exits 2 naming the reparse point; nothing is written through it. |

---

### F-11 — Word COM timeout orphans `WINWORD.EXE`; the diagnostic falsely claims the process was terminated

| | |
|---|---|
| **Invariant** | I6 · Spec 16.2 step 7 ("isolated converter state"), Spec 14.3, `GATE-03` |
| **Path** | [pdf.py:convert_word_com](P0.9/Build/runtime/jobbsok/pdf.py) — `subprocess.run(command, timeout=timeout)` kills only the direct child (`powershell.exe`). `winword.exe` is launched by DCOM, is not a child, and survives. The failure string reads *"The Word process was terminated."* |
| **Evidence** | No Word running (`NO_WORD_RUNNING`). `convert_word_com(t.docx, timeout=1)` → `ok=False`, diagnostic `"Word COM export timed out after 1s … The Word process was terminated."` Three seconds later: `tasklist` shows `WINWORD.EXE 23220`, ~229 MB. Full `render_job` with `converter_timeout_seconds=1` (a legal settings value) → `render_state DEGRADED` (correct) and **two** orphaned `WINWORD.EXE` (19056, 10172), ~310 MB combined — one per document. A subsequent successful conversion does **not** reap them. |
| **Consequence** | Orphans accumulate one-per-document across a batch; a 40-job run against a systemically slow or path-broken converter (see F-13) leaves up to 80 orphaned Word processes and multi-GB RSS, each with `AutomationSecurity` force-disabled and `DisplayAlerts` off. The diagnostic actively misleads the operator about cleanup. The degradation *state* is handled correctly (`DEC-41` honoured). |
| **Disposition** | **FIX** |
| **Severity / Confidence** | Medium / Certain |
| **Smallest remedy** | Have the PowerShell script record its `$word` process id (`$word.Application` → via `Get-Process`, or start Word with a known marker) and, on `TimeoutExpired`, kill that pid; failing that, correct the diagnostic to "the PowerShell host was killed; a Word process may remain — check Task Manager." Do not silently keep the false claim. |
| **Regression test** | Convert with `timeout=1`; assert no new `WINWORD.EXE` remains after the call returns. |

**Falsified sub-hypothesis (report this as a non-finding):** I expected `New-Object -ComObject Word.Application` to attach to a running Word instance and for `$word.Quit()` with `DisplayAlerts=0` to silently close the operator's session. **It does not.** With a visible operator Word session open (`operator_open.docx`, pid 6324), a conversion created a *separate* process (6324 ⇒ new pid observed during, 6324 survived) and the operator's window was untouched. Word 16 (Microsoft 365) isolates automation instances. **The per-document one-shot isolation posture is sound; keep it.**

---

### F-13 — Word COM `MAX_PATH`: the render transaction's own staging directory pushes realistic Norwegian names past 260 chars, silently degrading every PDF

| | |
|---|---|
| **Invariant** | `GATE-03` / `GATE-07` / `DEC-41`; Contract 17.2 ("Unicode and long Windows paths") |
| **Path** | `render_job` converts from `TransactionDir(out_dir, prefix=f"render-{job_id}")` — i.e. `…/out/.render-<job_id>.XXXXXXXX/<filename>`. `safe_filename_component` allows 70 chars each for employer and title, so a filename can reach ~149 chars. `paths.MAX_PATH_CHARS = 240` is never applied to render output paths, so the build's own guard does not fire. |
| **Evidence** | Froze a job with a realistic employer/title: `Nordre Follo kommune Virksomhet for økonomistyring og analyse` / `Seniorrådgiver økonomistyring virksomhetsanalyse og rapportering`. `render` → `[DEGRADED] lang_kommune CV: OK/DEGRADED letter: OK/DEGRADED`, diagnostic `"You cannot call a method on a null-valued expression."` Final output path = **231** chars; staged path = **261** chars. The *same DOCX* converts fine from the final `out/` path (231) and from a short temp path. Threshold probe with padded directories: `250 → ok=True`, `256 → True`, `258 → True`, **`260 → False`**, `262 → False`, `266 → False`. At the canonical root (`…\Jobbsøk_26\P0.9\Build`, 62 chars vs the scratch's 45) the same job yields a staged path of ~278 — **worse**. |
| **Consequence** | PDF conversion fails for a large fraction of real Norwegian public-sector employer+title pairs, entirely because of the pipeline's own staging directory, and the operator sees an undiagnosable PowerShell null-reference message with no mention of path length. No test in the suite uses a long employer or title. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | High (product-visible) / Certain (threshold measured) |
| **Smallest remedy** | Use a short staging name (`tempfile.mkdtemp(prefix=".r", dir=out_dir)` drops ~20 chars) **and** convert via a short absolute temp path, copying the PDF back — or convert after promotion. Additionally: cap the combined `employer_title` suffix, and raise an explicit diagnostic when a target path ≥ 255 chars. |
| **Regression test** | Freeze a job with a 60-char employer and a 60-char title at the canonical root depth; assert both PDFs reach `OK`, and assert the staged path length < 250. |

---

### F-12 — The current failure record, `BLOCKED_MANUAL` and the retry scaffolding are unreachable from production

| | |
|---|---|
| **Invariant** | I4 · `DEC-07`, `CTR-03`, `DEC-36`, `ACC-05`, `ACC-14`, Contract 9.3 |
| **Path** | `runtime/jobbsok/failure.py` implements `record()`, `clear()`, `next_retry_stage()` correctly. `grep -rn "import failure\|failure\.record\|failure\.clear\|next_retry_stage" runtime/` → **zero hits in `runtime/jobbsok/`**; every hit is in `runtime/tests/`. `cli.py` never imports the module. `status.py` reads `current/failure.json` but nothing ever writes it. |
| **Evidence** | Static (exhaustive grep) plus behavioural: after `render` reports `[FAILED]` (exit 1) and after `validate` reports `[FAIL]`, `ls runs/<id>/jobs/<job>/current/` contains no `failure.json`; `status` shows `blocked 0`. |
| **Consequence** | `BLOCKED_MANUAL` is unreachable by any operator action. `attempts_used` / `last_successful_stage` / `recommended_next_action` are never populated, so Contract 9.3's required surface does not exist at runtime. `retry_start_stages = [3]` is frozen into every manifest and consumed by nothing. The distinction the spec cares about — a *failed attempt* vs *never started* when no artifact survives — cannot arise. `test_t08_*` and `test_t09_every_required_production_state_is_reachable` all reach these states by calling `failure_module.record(...)` directly. |
| **Disposition** | **FIX** (wire it) — not IMPROVE; `ACC-14` and `CTR-03` are MUST-level. |
| **Severity / Confidence** | High / Certain |
| **Smallest remedy** | Two call sites: (a) in `cmd_validate` / `cmd_render` / `cmd_stage_submit`, on a job-level mechanical failure, `failure.record(..., classification="FAILED", result=result, attempts_used=<prior+1>, ...)`; (b) on success, `failure.clear(...)`. `BLOCKED_MANUAL` when `next_retry_stage(frozen retry_start_stages, attempts_used)` returns `None`. No engine, no automatic advance — exactly the bounded scaffolding `GATE-11` describes. |
| **Regression test** | Through the **CLI only**: submit an invalid artifact → assert `failure.json` exists with `classification: FAILED`; exhaust the configured retries → assert `status` shows `BLOCKED_MANUAL`; submit a valid replacement → assert `failure.json` is gone and archived. |

---

### F-14 — The documented manual-PDF-export recovery can never restore `render_state = OK`

| | |
|---|---|
| **Invariant** | `DEC-41`, Contract 14.2 ("A manual PDF export MAY later update render state after verification"), `GATE-03` safe posture |
| **Path** | `pdf.MANUAL_EXPORT_ACTION` tells the operator: *"Open the DOCX in Word … Save As PDF, then rerun `jobbsok render --job <job_id>` to re-verify the render state."* `render` does not verify existing files; it re-runs the converter. If the converter still fails, state stays `DEGRADED`; if it now succeeds, the manually exported PDF is `REFUSED_FOREIGN` (F-06) because no prior report recorded a hash for it. |
| **Evidence** | Code path plus the F-06 reproduction (`cv.pdf: existing file preserved because no prior render recorded a hash for this file`). |
| **Consequence** | `GATE-03`'s stated fallback — "manual export is the fallback" — is not operable. Every long-name job (F-13) is permanently stuck at `DEGRADED`, so the render axis stops distinguishing "PDF genuinely missing" from "PDF supplied by the human". |
| **Disposition** | **FIX** |
| **Severity / Confidence** | Medium / High |
| **Smallest remedy** | Add a verify-only path: if a PDF already exists beside a promoted DOCX and conversion is unavailable/failed, run `verify_pdf` on it and record `OK` with `promotion: "HUMAN_SUPPLIED"`. Fix F-06 so the hash survives. |
| **Regression test** | Set `converter = "none"`, drop a valid PDF into `out/`, run `render`; assert `cv_pdf == "OK"` and the human's file is not destroyed. |

---

### F-15 — `next` skips the every-command frozen-hash check

| | |
|---|---|
| **Invariant** | I1 · Contract 6.2 ("**Every** deterministic operation MUST verify the manifest and relevant frozen hashes before acting") |
| **Path** | `cmd_next` calls `load_manifest` then `status_module.derive(...)` and never inspects `status["integrity"]`; it returns `EXIT_OK` unconditionally. Every other command either calls `require_intact` (`_context`) or gates on integrity (`cmd_status`). |
| **Evidence** | Appended text to `runs/<id>/frozen/policy/stages/stage1_decision_architecture.md`, then ran the full command surface: `verify-integrity` exit 2 · `status` exit 2 · **`next` exit 0, `Next job : testetaten_radgiver`** · `validate` exit 2 · `context` exit 2 · `render` exit 2 · `finalize` exit 2. |
| **Consequence** | `next` is the continuation entry point (Contract 10.2) — the exact command an operator resuming an interrupted cluster runs first, and the exact place a silently altered stage instruction matters. Bounded, because `context` (which supplies the actual inputs) does fail. |
| **Disposition** | **FIX** |
| **Severity / Confidence** | Medium / Certain |
| **Smallest remedy** | `cmd_next`: `require_intact(layout, manifest)` (one line, matching `_context`). |
| **Regression test** | Tamper a frozen byte; assert **every** subcommand returns non-zero. Parameterise over the full parser's subcommand list so a new command cannot be added without a check. |

---

### F-16 — Document verification uses substring containment and cannot detect a contaminated identity line

| | |
|---|---|
| **Invariant** | Spec 16.7 / Contract 14.3 (CV must verify "candidate identity"), `DEC-39` |
| **Path** | `render._verify_docx.present()` → `if expected and expected not in folded: return False`. |
| **Evidence** | With the master's name line reading `AUDITMARKER_VEGARD HØLAND`, `identity_present` returned **`True`** — `"vegard høland"` is a substring. (Same reproduction as F-02.) |
| **Consequence** | Identity, chronology-anchor and employer-addressing checks pass for any document that *contains* the expected string, however corrupted, prefixed or duplicated. The check proves presence, not correctness — which is defensible for chronology anchors, but not for `identity`, which is the one field `Spec 16.7` singles out. |
| **Disposition** | **IMPROVE** |
| **Severity / Confidence** | Medium / Certain |
| **Smallest remedy** | For `verification.identity`, require the expected value to occupy a whole normalized line (or match on word boundaries), not merely be contained. |
| **Regression test** | Prefix the master's name run; assert `identity_present is False`. |

---

### F-17 — Staleness diagnostics under-report the cascade and misstate the cause

| | |
|---|---|
| **Invariant** | Contract 8.1 ("report all practical independent violations in one pass"; "identify … expected and observed"), Spec 14.3 |
| **Path** | `evaluate_staleness` adds cascaded artifacts to the `stale` **set** but emits a `Violation` only for the artifact whose own recorded binding mismatched. |
| **Evidence** | After replacing the strategy, `validate` printed exactly one warning — about `draft_package` — while `status` correctly reported the final and review stale too. In the branch case (F-08), the emitted text reads *"the strategy was replaced"* when nothing was replaced. |
| **Consequence** | The operator sees one stale artifact and re-runs one stage; two more remain stale. |
| **Disposition** | **IMPROVE** |
| **Severity / Confidence** | Low-Medium / Certain |
| **Smallest remedy** | Emit one violation per member of the final `stale` set, naming the originating replacement. |
| **Regression test** | Replace the strategy; assert three distinct DEC-26 violations naming draft, final and review. |

---

### F-18 — Settings surfaces with no consumer; soft thresholds read live, not frozen

| | |
|---|---|
| **Invariant** | Contract 21 ("avoid … configuration systems with no current consumer"), Spec 3, plus I1 |
| **Path / Evidence** | `grep` over `runtime/jobbsok/`: `pdf_required` **0** hits · `runs_root` **0** · `generated_root` **0** · `pilot_log` **0** · `cv_expected_max_pages` **0** · `letter_expected_max_pages` **0**. `mechanical_correction_attempts` appears only in `settings._check` and `settings.snapshot`, never consumed. `retry_start_stages` likewise (plus dead `next_retry_stage`). `soft_quality_warnings` consumes only `competencies_expected_min/max`. Separately, `cli._thresholds` reads the **live** `policy/settings.toml`, and `soft_warnings` is not in `settings.snapshot`, so a frozen run's editorial warnings track the live file. |
| **Consequence** | `[paths]` is an active trap: an operator changing `runs_root` gets silence, because `Layout` hardcodes the directory names. `pdf_required = false` reads like a switch and is inert. Page-count guidance (`DEC-24`) is measured (`page_count` is in the report) but never surfaced as a warning. |
| **Disposition** | **AMEND** (delete `[paths]`, `pdf_required`; either consume or delete the page thresholds; snapshot `soft_warnings` into the manifest) |
| **Severity / Confidence** | Low / Certain |
| **Smallest remedy** | Delete the unconsumed keys; add `soft_warnings` to `settings.snapshot` and read it from the manifest in `cli._thresholds`. |
| **Regression test** | Assert every key in `settings.toml` is referenced by name somewhere in `runtime/jobbsok/`. |

---

### F-19 — `EXCEPTION` jobs silently accept a full artifact set, can be finalized, and are invisible to `validate`/`render`

| | |
|---|---|
| **Invariant** | `DEC-03` (an exception "MUST remain visible … MUST NOT grow into a second workflow"), `ACC-02` |
| **Path** | `cmd_stage_submit` and `cmd_finalize` do not consult `job_class`; `cmd_validate` and `cmd_render` both `if job["job_class"] == "EXCEPTION": continue`. |
| **Evidence** | `stage-submit --job engelsk_job --stage 1 --artifact strategy` → `[OK] wrote …/engelsk_job/current/strategy.json`, exit 0. `finalize --job engelsk_job --date 2026-08-26` → `Finalized …`, exit 0. `validate --job engelsk_job` → `Checked 0 artifact(s); 0 failed.` `render --job engelsk_job` → no output, exit 0. `status` → `EXCEPTION`. |
| **Consequence** | Work can be poured into an exception job that no command will ever validate, render or report — a silent sink rather than a loud refusal. Counts stay correct, so the `ACC-02` obligation is met; the gap is diagnostic. |
| **Disposition** | **IMPROVE** |
| **Severity / Confidence** | Low / Certain |
| **Smallest remedy** | `cmd_stage_submit` / `cmd_finalize` refuse with a clear message when `job_class == "EXCEPTION"`; `cmd_render --job <exception>` prints `[SKIP]` rather than nothing. |
| **Regression test** | Assert `stage-submit` and `finalize` exit non-zero on an exception job and write nothing. |

---

### F-20 — The traceability suite proves test *names* exist, not that behaviour is covered

| | |
|---|---|
| **Invariant** | Contract §20.1/§20.13 (executable evidence; accurate labelling), `INV-02` |
| **Path** | `test_traceability.py` — `test_tier1_item_has_at_least_one_test` asserts a name matching `test_tNN_*` exists; `test_acceptance_criterion_has_a_named_test` asserts the mapped name exists. Neither inspects what the test does. |
| **Evidence** | Cross-referencing `ACC_COVERAGE` against production reachability: `ACC-04` → `test_t22_protected_inputs_reject_writes` (calls `assert_protected`, which **no production code calls** — F-09). `ACC-05` → `test_t09_every_required_production_state_is_reachable` (injects via `failure_module.record` — F-12; the name asserts the very property it bypasses). `ACC-14` → `test_t08_blocked_manual_wins` (same injection). `ACC-19`'s write-root half inherits `ACC-04`'s gap. `ACC-06` → `test_t09_pdf_degradation…`, which uses `_write_render_report` with `final_package_sha256 = "0"*64` (F-04). `test_t10_invalidation_table_is_exactly_the_frozen_one` asserts the `STALE_SCOPE` constant literal, including `"render"` — which nothing consumes. `test_t02_*` never derives the child's status (F-08). |
| **Consequence** | "208 green, 23/23 Tier-1, 19/19 ACC" is a **name-existence** claim. Four acceptance criteria rest on helpers production never invokes, and three more on injected state. Every finding above except F-13 and F-16 lives inside an area the suite marks covered. |
| **Disposition** | **FIX** (the mapping's meaning), **KEEP** (the idea of an executing matrix — it is good) |
| **Severity / Confidence** | Medium (meta) / Certain |
| **Smallest remedy** | Add a rule: any test cited as ACC evidence must drive the CLI (`jobbsok.cli.main([...])`) or a function reachable from it. Add a static check that every public helper in `paths.py` and `failure.py` has at least one caller under `runtime/jobbsok/`. |
| **Regression test** | The static caller check itself; it fails today on `assert_writable`, `assert_protected`, `failure.record`, `failure.clear`, `next_retry_stage`. |

---

### F-21 — `Build.zip`: an unversioned full copy of the tree, including the authorities and personality profile, in the build root

| | |
|---|---|
| **Invariant** | Contract 3 (permission separation; protected inputs), Spec 17.2 (minimise personal data) |
| **Evidence** | 2.5 MB, 235 entries, timestamped **after** the tree it copies (16:02 vs 04:43). Contains `runs/…/frozen/authorities/{Work_experience,Education,Other_high_value_information,CV_BASELINE}.md` and `frozen/context/PERSONALITY_PROFILE.md`. Not matched by `.gitignore`. |
| **Consequence** | A second, unprotected, staler-or-newer copy of every protected input sitting outside every protected root, easily mistaken for the canonical build. |
| **Disposition** | **AMEND** — move outside the build tree or delete; add to `.gitignore`. |
| **Severity / Confidence** | Low / Certain |
| **Regression test** | Assert no archive in the build root contains a path under `authorities/` or `context/`. |

---

### F-22 — OOXML work covers only `word/document.xml`

| | |
|---|---|
| **Invariant** | Spec 16.3 (no unresolved control in a delivered document), Contract 14.3 |
| **Path** | `docxfill.read_document` / `control_inventory` / `assert_no_controls` / `visible_text` all read `DOCUMENT_PART = "word/document.xml"` only. Headers, footers and footnotes are streamed through byte-identical. |
| **Consequence** | An SDT or private token in a header/footer would neither be inventoried, filled, unwrapped, asserted-against nor leakage-scanned. Currently benign — both supplied masters carry all controls in the body — but it is an untested edge that any future master change opens. |
| **Disposition** | **DEFER** (document the scope now; extend if a master ever gains header content) |
| **Severity / Confidence** | Low / High |
| **Regression test** | Assert no `w:sdt` exists in any `word/header*.xml` / `word/footer*.xml` of either master, as a preflight check. |

---

## 3. Falsified hypotheses — things that are genuinely correct

Stated explicitly so they are not re-litigated:

- **Job containment and targeted operation are exact.** Poisoned `lang_kommune` + healthy `testetaten_radgiver`: `render --job lang_kommune` exit 1; every file under the healthy job byte-identical before/after (full recursive hash comparison). Same for `validate --job`. `INV-05`, `DEC-06`, `ACC-15`, Contract 10.3 hold. (A whole-run `render` does change PDF *bytes* for healthy jobs — that is Word's `CreationDate` stamp, already documented in `test_t20_pdf_container_metadata_variation_is_documented`. DOCX hashes are stable.)
- **Frozen-hash tampering is caught by every command except `next`** (F-15) — including `render`, `finalize`, `context`, `validate`, `status`, each with the correct "restore the frozen bytes or create a child run" remedy and no in-place manifest update. `DEC-40` / Spec 7.3 are honoured where they are checked.
- **Word COM does not hijack or close the operator's Word session** (see F-11). Per-document one-shot isolation with `AutomationSecurity = 3` and read-only open is the right posture.
- **`DEC-41` degradation semantics are correct.** Forced converter failure and genuine timeout both yield `render_state.overall = DEGRADED` with `cv_docx/letter_docx = OK`, `production_state = VALID`, `semantic_final_available = True`, and a human action — no semantic demotion, no `DOCX_ONLY` mode.
- **Prior valid outputs survive a failed replacement.** After a CV build failure, the previous CV DOCX/PDF remain intact on disk and `render` exits 1.
- **Freeze is atomic, exceptions are countable and non-blocking, marker files have no authority.** 3-job freeze: `core 2, exception 1`, exception grouped separately, `next` never returns it.
- **The baseline↔authority reconciliation gate is real and blocking** (`manifest._reconciliation` fails freeze on a recorded-hash conflict) — a Contract 6.1 obligation that is easy to stub and was not.

---

## 4. Positive deviations Codex must preserve

1. **`runs/<id>/frozen/` self-contained input copies.** This is the correct frozen-run model and is *better* than re-hashing live files (ordinary source maintenance between runs cannot red-light an in-flight run). F-01/F-02 are failures to apply it consistently, not reasons to abandon it.
2. **`artifact_hash` excludes the `finalization` block.** A correct reading of `DEC-26`'s two separate rows; without it, `finalize` would mark the review stale and demand a pointless Stage-3 rerun. The fix for F-08 should extend this same precedent to `binding.run_id` / `binding.manifest_sha256`.
3. **The `GATE-02` master repair.** `build_core_properties` rewrites `docProps/core.xml` from scratch with canonically bound prefixes, eliminating a defect class rather than patching a string — strictly better than the gate's stated fallback of building replacement masters.
4. **`_NORWEGIAN_FOLD` in `safe_filename_component`.** P0.7's fold *deleted* `ø`/`å` (`Rådgiver økonomi` → `Radgiver konomi`) on files sent to employers. Explicit mapping first, then NFKD.
5. **stdlib `zipfile` + `ElementTree` instead of lxml/python-docx**, with byte-identical passthrough of every non-`document.xml` part and verbatim restoration of the master's root open tag (`_merge_root_tag`). Two fewer dependencies and a smaller `ACC-19` surface.
6. **Per-file, ownership-checked promotion** replacing P0.7's `rmtree(dest)` + `os.replace`. The mechanism is right; only its memory is broken (F-06).
7. **`ERROR`/`WARNING` severity split mapped onto exit codes**, implementing `INV-07` structurally so semantic-density choices provably cannot fail a command.
8. **Explicit-empty-replacement semantics** with a warning and no fallback — exactly `DEC-23`/Spec 12.2, and precisely what P0.7's `minItems: 1` made unrepresentable.
9. **`next_retry_stage` as a pure function with no engine.** The correct `GATE-11`/`DEC-36` anti-orchestration posture; it needs *wiring* (F-12), not architecture.
10. **The traceability matrix as an executing test.** The idea is right even though the current assertion is too weak (F-20) — strengthen it, do not delete it.

---

## 5. Pre-live-smoke blocker set (exact)

These must be closed **before** the two real-job live smokes, because each corrupts the employer-facing artifact or its provenance record and would make the smoke's evidence untrustworthy:

| # | Finding | Why it blocks the smoke |
|---|---|---|
| **B1** | **F-02** — render reads the live masters; report asserts an unused hash | The delivered document is not frozen-run invariant and its provenance record is false. Any master touch-up during the smoke silently rewrites output. |
| **B2** | **F-07** — render does not enforce the control contract | An unknown control ships internal text into a real CV. With B1 open, one master edit is all it takes. |
| **B3** | **F-13** — `MAX_PATH` staging path | Real Norwegian employers/titles are long; both smoke jobs would degrade to DOCX-only with an undiagnosable error, and F-14 makes that unrecoverable. |
| **B4** | **F-05** — model-assigned document date | The Stage-3 instruction does not specify a *required* field whose natural guess dates the employer's letter wrongly. This will fire on the first real Stage-3 chat. |
| **B5** | **F-01** — live schemas for a frozen run | The smoke's validation evidence is only as stable as an unedited `schemas/`. |
| **B6** | **GATE-10** — `[stages.role_mapping]` is `{SOL_CLASS: "", TERRA_CLASS: ""}` | Already owed. A run frozen today freezes an empty mapping with no warning; `preflight` does not check it. Add the check while filling it in. |

**Blocks the first full batch (not the two-job smoke), but must not reach production:**
F-03 (commands ignore `STALE`) · F-04 (render currentness) · F-08 (branch yields a stale child) · F-12 (failure record / `BLOCKED_MANUAL` unreachable) · F-06 + F-14 (ownership amnesia and the inoperable manual-PDF fallback) · F-09 + F-10 (`--dest` and reparse-point write confinement) · F-15 (`next` integrity check).

**Deferrable:** F-16, F-17, F-18, F-19, F-21, F-22.

---

## 6. Comparison with `BUILDER_REPORT.md`

No prior *forensic* audit exists; the only prior assessment is the builder's own report, read after the above was established.

**Confirmations**

- §3.1 the masters were not Word-openable, and the repair is better than the gate's fallback — confirmed by code (`build_core_properties`) and by successful Word COM conversion today.
- §3.3 LibreOffice absent, Word COM per-document — confirmed (`Word 16.0` returned by the adapter).
- §4 "The document date is outside the semantic hash" — confirmed correct and load-bearing.
- §4 "A failed attempt is not 'never started'" — the *precedence* in `status.py` is correct; but see the disagreement below, since nothing can produce that state.
- §5 the P0.7 reuse ledger and both recorded P0.7 defects — confirmed by inspection.
- §2 items 2, 3, 10 correctly reported as not met; `ACC-20` correctly held out under `INV-08`.
- "Nothing in this build is `PRODUCTION-MODEL_TESTED`" — accurate and well-drawn.

**Disagreements**

| Builder claim | Finding |
|---|---|
| §4 "**A run reads its inputs from its own `frozen/` copies**, and commands verify those." | **False for the two highest-consequence planes.** Schemas (F-01) and Word masters (F-02) are read live; soft thresholds too (F-18). The frozen copies of both exist and hash-verify — and are never read. |
| Repository roles / permission separation → `MECHANICALLY_TESTED` (`test_t22_protected_inputs_reject_writes`) | `assert_protected`/`assert_writable` have **no production caller**; `render --dest` writes into `authorities/` and `templates/` (F-09). |
| Safe path handling, reparse points → `MECHANICALLY_TESTED` "incl. real junction rejection" | The helper rejects junctions; no write path calls it. `render` wrote four deliverables through a junction, exit 0 (F-10). |
| Child branch, "rebind vs regenerate" → `MECHANICALLY_TESTED` | An identical-input child comes out `STALE` with `highest_valid_stage: STRATEGY` (F-08). `test_t02_*` asserts labels and parent immutability, never the child's status. |
| Current failure / `BLOCKED_MANUAL` → `MECHANICALLY_TESTED` | Unreachable from production; every green test injects it (F-12). |
| Three orthogonal axes → `MECHANICALLY_TESTED` | The two semantic axes are sound; the **render axis is never checked for currentness** (F-04), and the covering test hard-codes an impossible binding hash. |
| Document date at finalization → `MECHANICALLY_TESTED` | A model stage can set it and `render` accepts it (F-05). |
| DoD #1 "All 19 ACC map to named executing tests; the mapping is itself a test." | Accurate as written and **insufficient as evidence** — it is a name-existence check; `ACC-04`, `ACC-05`, `ACC-14` and half of `ACC-19` rest on unwired helpers (F-20). |
| §6 "**Needs no further code before those happen.**" | Disagree. Six items (B1–B6) must land before the live smoke; eight more before the batch. |

**New findings** (absent from the builder report in any form): **F-01, F-02, F-03, F-04, F-05, F-06, F-07, F-08, F-09, F-10, F-11, F-12, F-13, F-14, F-15, F-16, F-17, F-19, F-20, F-21, F-22.** F-18 is partially foreshadowed by the report's own "no configuration surface without a consumer" principle, which the shipped `settings.toml` breaks in six places.

---

**Scope note.** Everything above is engineering conformance (`INV-08` loop A). Nothing here speaks to package quality, truthfulness or Bokmål naturalness — those remain owed to the real pilot and to `ACC-20`. Scratch trees left at `…\Temp\claude\jb\A` and `…\Temp\claude\s`; both are disposable. No file in `P0.9/Build/` was modified.