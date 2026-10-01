# P0.9 — Independent post-finalization verification

**Date:** 2026-08-24
**Scope:** adversarial verification of the repository state produced by the GPT-5.6 Sol finalization Goal
**Method:** every claim re-tested through the public CLI against disposable scratch copies at a short filesystem path; canonical `P0.9/Build/` re-verified unchanged afterwards. Reviewer findings and Codex's own report were treated as claims, not evidence.

---

## 0. Verdict

**The finalization is genuinely good work.** Twenty-four of the twenty-four material defects I could re-test are actually fixed — not fixed in a test, fixed through the public command path — and several are demonstrated on the exact counterexample artifacts that originally exposed them. Scope discipline held: the four frozen `Architecture/` files are byte-unchanged, no prohibited subsystem appeared, and the dependency surface is still `{jsonschema, pymupdf}`.

**But the terminal classification is wrong in a way that matters.**

> `BLOCKED_USER` was reported because "Word COM cannot activate in this session." That is true of Codex's execution surface and **false of the machine**. In an ordinary interactive Windows session the full suite runs **246 passed, 0 skipped** — the ten "target-Word" tests all pass. Four of the five blocking criteria were blocked by the agent's sandbox, not by the environment.

The honest terminal state is much closer to GO than the report says. The genuinely remaining work is roughly a third of what is listed.

**Recommended classification after re-running the checks below: `GO_FOR_TWO_JOB_SMOKE`, conditional on two human acts** — a visual QA pass and the GATE-10 account facts.

---

## 1. The headline finding

### R1 — The target-Word blocker is an artifact of the agent's session, not the machine

| | |
|---|---|
| **Claim under test** | `DOD-16`, `DOD-17`, `DOD-23`, `DOD-25` = `BLOCKED_USER`; suite = "236 passed, 10 skipped"; `GATE-03` = `BLOCKED_USER target Word session` |
| **What I measured** | `New-Object -ComObject Word.Application` → **`COM_ACTIVATION=OK Version=16.0`**. Full suite in an ordinary session → **`246 passed in 214.33s`**, zero skips. |
| **Mechanism** | `conftest.word_available()` performs a real COM activation probe (a genuine improvement over the old registry check). Codex's process had no usable Windows logon session — Windows error `80070520` — so the probe correctly returned `False` and correctly skipped. The gate is honest; the *conclusion drawn from it* over-generalizes. |
| **The ten tests that now pass** | `test_t19_target_machine_produces_both_docx_and_verified_pdfs`, `test_t19_pdfs_are_independently_verified`, `test_t19_norwegian_glyphs_survive_to_the_pdf`, **`test_t19_public_word_render_handles_realistic_long_norwegian_names`**, `test_t20_first_finalization_fixes_the_date_and_rerender_preserves_it`, `test_t20_rerender_yields_identical_docx_bytes`, `test_t20_pdf_container_metadata_variation_is_documented`, `test_t21_edited_deliverable_survives_a_rerender`, **`test_t21_failed_pdf_rerender_retires_prior_pipeline_pdfs`**, `test_t21_ownership_survives_a_transient_failed_attempt` |
| **Consequence** | `DOD-16` (long Norwegian names, timeout diagnostics), the target half of `DOD-17` (glyphs/open/export), and the `AR-01/03/16/20` subchecks of `DOD-23` are all demonstrably satisfiable **right now**. `DOD-25`'s suite prerequisite likewise. |
| **Severity / Confidence** | High (release-decision impact) / Certain — reproduced twice |
| **Action** | Re-run `pytest -q` from a normal interactive terminal, paste the `246 passed` line into `DOD_AUDIT.md`, and re-classify `DOD-16`, `DOD-17` and `DOD-23` to `PASS`. No code change. |

Codex behaved correctly here: it refused to convert an unavailable check into a pass, and said so explicitly. That is the right instinct and should be preserved. The defect is in the *scope of the inference*, not in the discipline.

---

## 2. What I independently confirmed fixed

Each row was reproduced through the public CLI on a scratch copy. "Original" cites the finding ID from the consolidated review register.

| # | Original | Test I ran | Result |
|---|---|---|---|
| 1 | `MMR-001` live schemas | Injected an impossible `required` into live `schemas/package.schema.json`, then `validate` | **PASS** — 4/4 artifacts still valid; the run reads its frozen schema |
| 2 | `MMR-002` live masters | Injected `AUDITMARK_` into the live `CV_MASTER.docx` name line, then `render --force` | **PASS** — marker absent from the delivered CV; report binds `a8f90a50` = the frozen master actually consumed, not the poisoned live one |
| 3 | `MMR-004` stale action boundary | Replaced the strategy, then ran each command | **PASS** — `finalize` exit 1, `render` exit 1 *"render requires a current valid final package and current valid review"* |
| 4 | `MMR-005` render currentness | `status` on the original incoherent legacy run | **PASS** — now reports `render: FAILED`, surfaces **zero** output paths, and says *"Rerender from the current eligible semantic final."* Previously it reported `OK` with four stale deliverables |
| 5 | `MMR-006` / `MMR-035` closed-loop handoff | Full round trip: `context` → author semantic fields only → `stage-submit --handoff` | **PASS** — accepted, exit 0, artifact immediately current. `write.semantic_fields` names exactly what the model may return; `tool_owned_fields` names what tooling stamps |
| 6 | — stale-handoff replay | Re-submitted with the now-superseded handoff | **PASS** — refused, exit 1, before any mutation |
| 7 | `MMR-013` branch reuse | Froze fresh → completed all three stages → `branch` with nothing changed | **PASS** — `REUSED ×4`, child derives `VALID / FINAL / semantic_final_available=True / triage CHECK / stale_scope []`, parent integrity intact |
| 8 | `MMR-016` `next` under tamper | Tampered a frozen stage instruction, ran all seven commands | **PASS** — every command exits 2, including `next` |
| 9 | `MMR-017` + RC-9 containment | Wrote `{ this is not json` into a current artifact | **PASS** — `status` exit 1, `validate` exit 1, `next` exit 0, **zero tracebacks** |
| 10 | `MMR-018` model-owned date | Inspected the Stage-3 write contract | **PASS** — `finalization` is tool-owned; the model returns only `cv`, `letter`, `used_evidence_refs`, `writer_note` |
| 11 | RC-9 date parsing | `finalize --date 24.09.2026` | **PASS** — *"Invalid document date '24.09.2026'; expected canonical YYYY-MM-DD"*, exit 1 |
| 12 | `MMR-022` template contract | Froze a run whose master carried a rogue `CV_ROGUE` control, completed it, rendered | **PASS** — refused at point of use naming `unknown controls: {'CV_ROGUE': 1}`, **zero files produced** |
| 13 | `MMR-023` long Norwegian paths | `test_t19_public_word_render_handles_realistic_long_norwegian_names` | **PASS** in a real session |
| 14 | `MMR-024` timeout truthfulness | `convert_word_com(timeout=1)` with no Word running | **PASS** — *"The PowerShell invocation was stopped, but termination of its Word automation process was not proven. Do not end unrelated Word processes…"* An orphan does survive, exactly as the diagnostic now admits |
| 15 | `MMR-026` / `MMR-043` write boundaries | `--dest` into `authorities/`, `templates/`, `../../../schemas`, and an external path | **PASS** — first three `PathSafetyError` exit 2 with nothing written; external export succeeds as `[EXPORT-OK]` and **does not alter canonical status** (still `FAILED`, 0 outputs surfaced) |
| 16 | `MMR-029` leakage | Hyphenated private IDs vs ordinary Norwegian | **PASS** — `EMP-OUS-ANALYSE` / `EDU-NTNU-ECON` caught; `brenner for` and `Master i samfunnsøkonomi` pass |
| 17 | `MMR-030` forced page break | Inspected both masters | **PASS** — 0 hard page breaks, **17/7 controls preserved** (`AR-02` intact) |
| 18 | `MMR-008` failure record | Grepped production call sites | **PASS** — `failure_module.record/clear/next_retry_stage` all called from `cli.py`; no longer test-only |
| 19 | `MMR-044` EXCEPTION containment | `context --stage 1` on an EXCEPTION job | **PASS** — exit 1, *"inert to the core semantic workflow"*; core peer unaffected; counts correct |
| 20 | `MMR-015` Stage-3 recovery | Deleted the review, ran `context --stage 3` | **PASS** — mode `REVIEW_ONLY`, `allowed writes: ['review']` (see R2 for the residual) |
| 21 | `D-01` revision strategy | Inspected version fields | **PASS** — `0.9.0` unchanged everywhere; no blanket bump; `map_version`/`index_version` untouched |
| 22 | `D-03` review orthogonality | Render precondition text + receipt binding | **PASS** — review required to initiate render, absent from receipt identity, exactly as frozen |
| 23 | Contract §22 — no authoritative progress files | Read `verify_handoff` | **PASS** — the handoff is re-derived from live state and compared; the file is a freshness token, never a source of truth, and is `resolve_within`-guarded |
| 24 | Evidence re-derivability | Recomputed `HASHES.sha256`; matched slice `output_hashes` to retained artifacts | **PASS** — 27/27 verified, 0 mismatched, 0 missing; both slice artifacts match |

Anti-regression spot checks: `AR-05` Norwegian fold intact (`Rådgiver økonomi` → `Radgiver_okonomi`, not `Radgiver konomi`); `AR-16` still stdlib-only OOXML, dependencies unchanged; `AR-02` control inventory preserved through the master repair.

---

## 3. Residual findings

### R2 — Review-only recovery gives the operator the wrong next action — **Medium**

With a valid current final and a missing review — the precise interrupted-Stage-3 scenario this repair was built for:

```
next --stage 3   → selects the right job, then says  action: "Finalize and render."
finalize         → exit 0   (succeeds; assigns/updates the canonical document date)
render           → exit 1   "requires a current valid final package and current valid review"
```

`context --stage 3` knows the truth (`mode: REVIEW_ONLY`), but the status/queue action text does not. An operator following the queue's own advice runs `finalize` — which **succeeds and mutates the canonical employer-facing document date on an incomplete Stage 3** — then hits a refusal at `render`.

This contradicts `DFS-05` ("continuation commands must reflect the actual remaining Stage-3 work"). No employer output is corrupted, because `render` holds the line. Smallest remedy: derive the recommended action from the same `semantic_state` that `context` uses, and have `finalize` require a current valid review for symmetry with `render` (`DEC-21` step 1 names both). **Confidence: certain, reproduced.**

### R3 — `framework.zip` contradicts `DOD-24` in the current tree — **Medium-low**

`DOD-24` is recorded `PASS` — *"Nested archive absent … no distribution archive created."* The build root currently holds **`framework.zip`, 34 MB, 2 692 entries, timestamped 02:36** (ten minutes after the Goal ended). It contains `.venv/`, `.pytest_cache/`, and **twelve copies of protected candidate inputs** (`authorities/*.md`, `frozen/authorities/*.md`, `PERSONALITY_PROFILE.md`).

The old 2.5 MB `Build.zip` was indeed removed, as claimed. Whoever created this one, the *repository state* now contradicts the criterion, and `.gitignore` still has no rule that would prevent recurrence:

```
.venv/
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/
```

Remedy: delete or relocate the archive, add `*.zip` to `.gitignore`, and re-verify `DOD-24` against the tree rather than against the moment it was written.

### R4 — `DOD-18` has no fixture scaffolding — **Low-medium**

`DOD-18` requires sparse/normal/dense representative packages rendered through target Word with human visual judgment. There is no generator: the only occurrence of "sparse"/"dense" in the tooling is a prose comment in `prepare_masters.py`. A human must hand-build two extra packages before the one criterion that genuinely needs a human can even begin. Half a day of avoidable friction on the critical path. Remedy: a small fixture generator producing the three density variants through the normal render path.

### R5 — The legacy run keeps four orphan employer documents — **Low**

`runs/r20260823-050000-fea486/jobs/testetaten_radgiver/out/` still holds four employer-facing files whose receipt no longer verifies. `status` is now honest about this (`render: FAILED`, no output paths surfaced), which is arguably *better* evidence than deleting them — the run is now a live demonstration of the receipt fix. But the files exist on disk and a human browsing `out/` would find deliverable-looking documents with no valid provenance. Remedy: either delete them or leave a `SUPERSEDED` marker in the directory.

### R6 — Staleness diagnostics still under-report the cascade — **Low**

Replacing the strategy produces one `DEC-26` warning naming `draft_package` only, while `status` correctly derives `stale_scope: [draft, final, review]`. `validate` exits 0. The exit code is defensible (`DFS-04` explicitly allows read-only diagnostics to report without failing), but the operator sees one stale artifact where three exist. Carried over unchanged from the pre-finalization state.

### R7 — Template-contract failure aborts run-global — **Low, informational**

A rogue control in the frozen master yields `ConfigurationError`, exit 2, aborting the whole run rather than failing one job. Defensible under `D-04`: the master is a run-global asset and every job would fail identically. Noted so it is a decision rather than an accident.

### R8 — The slice's run is not retained — **Informational, resolved differently than proposed**

`slice_evidence.json` documents run `r20260824-000759-517caf`, which is not in `runs/`. My earlier review flagged this pattern as fatal. Codex resolved it the other way `DOD-22` permits: it retains `manifest.json`, both semantic and full `fixtures/`, `queue.md` and exactly two `artifacts/` — and I verified both artifact hashes match the recorded `output_hashes`. The claims are re-derivable by re-running the slice tool. **This is an acceptable resolution**, and the evidence set is now replacement-based rather than append-based, which fixes the orphan-PDF problem the previous slice had.

---

## 4. Design decisions worth protecting

Things a future agent could plausibly "improve" and must not:

- **`FrozenRunAssets`** (`manifest.py`) — one resolver owning schemas, settings, maps and masters for a frozen run. `template_path()` refuses any template-map reference that is not one of the run's frozen templates, which closes the unknown-master case and the live-read case in the same three lines.
- **`stage_policy_sha256`** — a content-governing digest over stage instruction + writing policy + personality (Stage 1 only) + capability role + configured model. Not a dependency graph; exactly the surface that governs semantics.
- **`semantic_state()`** — one currentness predicate consumed by status, next, context, submit, finalize and render. `DFS-04` implemented structurally rather than by convention.
- **`write.semantic_fields` / `tool_owned_fields`** in the context bundle — this is what makes the manual workflow completable. Do not let a schema field drift back into model ownership.
- **Handoff tokens that are re-derived, never trusted** — the file is proof of freshness, not state.
- **The truthful timeout diagnostic** — it admits the orphan rather than claiming a kill. Do not "strengthen" it into an unproven `Stop-Process`.
- **Refusing to convert a skip into a pass** — the discipline that produced R1's over-conservative verdict is the same discipline that keeps the evidence honest. Fix the inference, keep the instinct.

---

## 5. Recommended closure sequence

1. **Re-run the suite from an ordinary interactive terminal.** Expect `246 passed, 0 skipped`. Record it verbatim in `DOD_AUDIT.md`, `BUILDER_REPORT.md` and `GATE_REPORTS.md`, replacing the `236/10` figures and the "Word COM cannot activate" framing with "unavailable in the finalization agent's session; verified in an interactive session on 2026-08-24".
2. **Re-classify `DOD-16`, `DOD-17`, `DOD-23` → `PASS`**, and `GATE-03`, `GATE-05` (static half), `GATE-06`, `GATE-07` accordingly.
3. **Fix R2** — the review-only action text, and `finalize`'s missing review precondition. One small change; it is the only functional defect I found.
4. **Fix R3** — remove `framework.zip`, add `*.zip` to `.gitignore`.
5. **Optionally fix R4** — a sparse/dense fixture generator, to make step 6 cheap.
6. **Human: `DOD-18`** — render sparse/normal/dense and look at them. This one genuinely cannot be automated.
7. **Human: `DOD-19`** — supply the `SOL_CLASS`/`TERRA_CLASS` surfaces and the account's file-access and retention posture.
8. **Run `/review`** in a fresh session for `DOD-25`.
9. Then `GO_FOR_TWO_JOB_SMOKE`.

Steps 1–5 are hours. Steps 6–7 are the real gate, and they always were.

---

## 6. Scope and integrity of this pass

Nothing in the canonical repository was modified by this verification. All destructive reproduction ran on disposable copies under the system temp directory. Re-verified after completion:

- the four `P0.9/Architecture/` files — unchanged (`3c60e6c6`, `8174f1f9`, `bb5b52e8`, `5dd3b2bd`);
- `P0.9/Build/` — only `.pytest_cache` touched, by the suite run;
- `P0.9/Process/` — only `EXECUTION_LEDGER.md` differs, written by the finalization Goal itself;
- root `AGENTS.md` — unchanged, and its paths now correctly route to `P0.9/Process/goal_prep/Implementation_Roadmap/00_READ_FIRST.md`.

One orphaned `WINWORD.EXE` created by my timeout probe was terminated.
