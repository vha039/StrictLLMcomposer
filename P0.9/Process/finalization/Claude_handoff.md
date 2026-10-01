# Claude handoff — Jobbsøk_26 state, rulings and traps as of 2026-08-28

**Status:** context file. NOT authority.
**Purpose:** carry forward everything from the P0.9.1 adjudication, implementation, acceptance audit and bounded-repair passes that a fresh instance cannot cheaply re-derive, so the pilot-learned optimization pass spends its effort on new analysis instead of re-discovery.

**How to use this file.** Treat every statement here as a *claim to verify*, exactly as you would treat a prior report. Where this file and the actual repository disagree, the repository wins. Where this file and the frozen architecture disagree, the architecture wins. Its value is that each claim below was verified against the repo at the date shown, and several were verified *by reproduction* — so you can re-check cheaply rather than re-investigate from zero.

Sections 5 and 6 are the highest-value parts. Read them before designing anything.

---

## 1. Authority order (unchanged, settled)

1. Current explicit user instruction and the active prompt.
2. `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` — `FROZEN_NORMATIVE`, revision `0.9.0`. Governs on conflict. §22.1 lists frozen invariants; §22.2 lists builder freedom.
3. `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`. §22 = prohibited redesigns; §24 = you implement, you do not re-adjudicate.
4. Actual repository behaviour, for any claim about implementation state.
5. Everything else — plans, reports, completion narratives, this file — is evidence, not command.

`AGENTS.md` at repo root is ambient authority. Read it first. Note its hazard warning: `P0.7/**/AGENTS.md` files are real, internally consistent instruction sets for a **retired** four-stage workflow. They are not instructions for any current task.

---

## 2. Where things are

```
P0.9/Architecture/     4 files, FROZEN_NORMATIVE. Do not edit.
P0.9/Build/            the implementation. Package version 0.9.1; spec/schema revision 0.9.0.
P0.9/Process/          provenance and planning. Not authority.
  ├─ Architecture_prep/  goal_prep/  plan_prep/
  └─ finalization/       ← this file; existing planning convention for new packages
P0.7/                  superseded asset mine. Never a compatibility target.
```

Build root path contains a non-ASCII character (`Jobbsøk_26`). That is load-bearing for path/quoting verification.

---

## 3. Current system state (verified 2026-08-28)

- **P0.9.1 shipped and verified.** Full deterministic suite: **251 passed / 0 skipped / 0 failed** (~245 s) in an interactive session with Word COM available. Vertical slice PASS, 21 steps, 0 unexpected, 4 outputs, `render overall : OK`. `prepare_masters --check` PASS. `preflight` PASS.
- **GATE-10 is DONE.** `policy/settings.toml` now has `SOL_CLASS = "Codex / GPT-5.6 Sol"`, `TERRA_CLASS = "Codex / GPT-5.6 Terra"`. This was the last human-owed pre-freeze item.
- **The two-vacancy pilot ran.** Run `r20260828-213932-7f13b4`, frozen `2026-08-28T21:39:32Z`, cluster `pilot_live_smoke`, jobs `huseierne_strategi_maalstyring` and `avinor_digital_transformasjon`. Role mapping is snapshotted into that manifest.
- `runs/` also contains `r20260823-050000-fea486`, a **retained synthetic run** from before the pilot. It is inert (every command is `--run`-scoped) but it will appear alongside real runs. Its state is `production VALID · triage CHECK · render FAILED` — that is expected, see §6.2.
- `pilot/PILOT_LOG.csv` was **last modified 2026-08-24** — i.e. the pilot did not write to it. Whether the human observations were captured elsewhere is worth establishing; `ACC-20` and Spec §18.3 expect that log to carry them.
- **`VISUAL_HUMAN`** (sparse/normal/dense visual QA, `ACC-18`, Spec §16.7) remains formally owed; the two pilot renders discharge it in practice on real content.

---

## 4. Verified current-state facts about the code

Each was confirmed against the repository. Re-verify before relying on any of them; a false one changes your plan.

| # | Fact |
|---|---|
| F1 | `cmd_finalize` requires a current valid final **and** review, revalidates the final, and inspects **no** `review.triage`. |
| F2 | `render_job` requires only `finalization.state == "FINALIZED"` and a `document_date`. It reads no triage. |
| F3 | `next_job(stage=3)` returns jobs at `DRAFT`, or `FINAL` with no review; skips `BLOCKED_MANUAL`; stops once final+review are current. |
| F4 | `freeze`/`branch --reviewed-by` are **required** and record a genuine human attestation into `manifest.baseline_reconciliation.reviewed_by`. `finalize --reviewed-by` is optional, defaults `"operator"`, fills `finalization.finalized_by`. **Same flag name, two different meanings.** RUNBOOK now reserves the human's name for `freeze`/`branch` only. |
| F5 | `finalize` is **idempotent** without `--date`: prints `Already finalized on <date>`, exit 0. This makes "run finalize then render" unconditionally safe in recovery. |
| F6 | `failure_module.record()` returns its payload; `_record_stage_failure` returns it; both `stage-submit` refusal branches print a `Recovery:` footer (classification, mechanical corrections, semantic attempts, exact next action). |
| F7 | `artifacts.semantic_fields()` returns **top-level property names only**. Nested shape comes from `write.schema_paths`. |
| F8 | The handoff envelope carries **no timestamp**. Its digest is *stable* across a mechanical-correction retry, and differs across jobs, stages, and `FINAL_AND_REVIEW` vs `REVIEW_ONLY`. Stale-handoff protection is `verify_handoff`, not path freshness. |
| F9 | `render_report.schema.json` already permits per-document `warnings: [string]`. No schema change was needed to persist page warnings. |
| F10 | `status.schema.json` declares `render_state` with `additionalProperties: false`. Adding a field there requires a schema edit — page warnings are therefore **not** visible in `status --json`. |
| F11 | Render component keys are exactly `cv` and `letter`, matching `cv_expected_max_pages` / `letter_expected_max_pages`. |
| F12 | Page targets are now **live** (`[render.soft_warnings]`). A warning is produced **only when PDF conversion succeeds** and yields a page count. When Word COM fails and render is `DEGRADED`, `page_count is None` and **no page warning exists**. |
| F13 | `pyproject.toml` version is read by no code, but the package is installed editable; `.venv/…/jobbsok-0.9.1.dist-info` reports `Version: 0.9.1`. |
| F14 | `SPEC_REVISION` / `SCHEMA_REVISION` are written into every manifest and **hard-pinned by `manifest.schema.json` as `"const": "0.9.0"`**. They cannot change without a schema edit and an amendment. |
| F15 | `policy/settings.toml [spec].revision` / `.schema_revision` are read by **nothing**. `settings.py::_check` never touches `[spec]`. |
| F16 | `settings.snapshot()` freezes `stages.role_mapping` into the manifest. A run frozen with blank mappings records blank model provenance permanently. |
| F17 | `handoff_for` raises a job-local error for `EXCEPTION` and for `BLOCKED_MANUAL` jobs. |
| F18 | `status --json` job entries carry `employer`, `title`, `semantic_triage`, `production_state`, `semantic_final_available`, `render_state`, `stale_scope`, `blocking`, `recommended_action`, `output_paths`. **Only `render_state.overall` is unconditional** — component/limitation/action keys appear when applicable. The whole end-of-cluster summary is derivable from one `status --json` call. |
| F19 | `context` supplies `read.writing_policy` to **all three stages**; `branch.py` binds it to all three. As of P0.9.1 Stage 1 and Stage 3 name it explicitly (Stage 2 always did). |
| F20 | `conftest.py` copies the **real** `authorities/ context/ policy/ templates/ schemas/` trees into every test build root. A test whose expectation depends on a production config value the human is required to change is a defect. |
| F21 | Job ids match `^[a-z0-9][a-z0-9_-]{2,60}$` and pass `require_safe_component`. Non-ASCII enters paths only via the build root. |
| F22 | Six configuration keys are read by **no code**: `[paths].runs_root`, `.generated_root`, `.pilot_log`, `[render].pdf_required`, `[personality].profile`, `.facet_index`, plus `[spec].*`. `paths.py` and `manifest.py` hardcode those paths; `pdf_required` behaviour is hardcoded per `DEC-41`. **Do not wire or delete them** — none causes a production failure, and this was deliberated and deferred. |
| F23 | `artifact_hash` **deliberately excludes** the `finalization` block. `DEC-26` lists "final replaced" and "document date assigned/changed" as two separate staleness rows. Consequence: a *superseded* receipt binding and a *fabricated* one have identical shape. |
| F24 | `assets.settings` resolves to the run's **frozen** `settings.toml` copy, not the live tree. Any test needing different settings must write them **before** `freeze`. |

---

## 5. Findings that should redirect the pilot-learned pass

These four were established today and materially change the root-cause analysis the considerations file proposes. **Verify each yourself, then let them steer the audit.**

### 5.1 The pilot ran with the *current* policy in force

The pilot manifest's frozen `stage_instructions` for all three stages, and both `writing_policy` files, are **byte-identical to the current live files**. Verified by hash comparison.

So the pilot ran with: the Stage-3 writing-policy pointer and its two named final tests, Stage-3 `READY` calibration, Stage-1 and Stage-3 cross-job resets, Stage-1 decision-density and named doctrine sections — all of the P0.9.1 policy work.

**Consequence:** the observed quality defects are *non-compliance with policy that was present, named and frozen*, not gaps in policy coverage. A root-cause analysis that ends in "add a rule" is very likely wrong. The interesting question is why in-force, explicitly-named rules were not honoured — routing, salience, ordering, anchoring, or competing instruction — not what the rules should say.

### 5.2 Mandatory outcomes B and C are already written policy

Verbatim from the frozen writing policy the pilot used:

`WRITING_DOCTRINE.md § Begrunnet motivasjon`
> Motivasjon skal være forankret i: en konkret oppgave eller et reelt virksomhetsproblem … Unngå generisk virksomhetsros, kopierte verdier, prestisjemotivasjon, `brenner for` og entusiasme uten substans.

That **is** outcome B (earned motivation). The Huseierne mission sentence violates an existing rule.

`PERSUASION_CALIBRATION.md § TOO_WEAK`
> Ikke erstatt støttede verb med «bidro litt», «fikk anledning til» eller generelle forbehold. Ikke gjør sannhetsgrensen til defensiv prosa om ikke-diskvalifiserende gap.

That **is** the leverage floor of outcome C. `var rapportert i bruk` violates an existing rule. The doctrine also already separates measured result / verified scope / documented capability / estimate / expected gain, and already forbids lifecycle misrepresentation.

`PERSUASION_CALIBRATION.md § UNNATURAL_NORWEGIAN` already forbids "oversatt amerikansk søknadsretorikk, «brenner for», managementsjargong, nominalisering, mekanisk symmetri og overforklarte relevanssetninger" — which covers much of OBS-04, OBS-08 and OBS-11.

`WRITING_DOCTRINE.md` further already contains, by name: `Tjuesekunderstesten` (recruiter mirror), `Arbeidsgiverbyttetesten` (employer swap, explicitly covering the CV top), `Komplementaritet mellom CV og søknad`, `Single Backbone og strategisk asymmetri`, `Rolig faglig tyngde` (with approved/forbidden verb lists), `Intervjureserve` (compression), `Variasjon innenfor en klynge` (cross-job variation), and `Myke redaksjonelle utgangspunkt` (≈4–8 competencies, CV normally 2 pages, letter normally 1 page, 2–5 body paragraphs — explicitly *not* validation limits).

**The single most likely failure mode of this pass is writing a fourth English copy of rules that already exist in calibrated Norwegian.** That was rejected twice already (§6.4). If a new rule is genuinely needed, first show why the existing one failed.

### 5.3 En/em dashes do not appear in the pilot's semantic output

Verified by direct grep of both pilot `final_package.json` files: **en-dash 0, em-dash 0, in both jobs.**

So OBS-07's premise is not reproduced at the semantic layer. If dashes appear in the rendered employer-facing documents, they come from **static template content**, date/range typography, or the rendering path — not from the stages. Outcome D may therefore need nothing in the semantic instructions at all, and may be either a template matter or purely preventive. Establish where (if anywhere) a dash actually reaches an employer-facing page before designing enforcement.

### 5.4 Typography is a style-map fact, and the masters are hazardous ground

Font sizes declared in `word/styles.xml` (half-point values converted):

```
CV_MASTER.docx           8, 9, 10, 11, 12, 13, 14, 26
APPLICATION_MASTER.docx  8, 9, 10, 10.5, 11, 12, 13, 14, 20, 26
```

The `10.5` in the application master is exactly the half-point micro-tuning outcome A wants removed, and the `9` entries in the CV master match the observed small CV body. **There are multiple body-ish styles to normalize, not one.**

Hazard, and it is a real one: the P0.7 masters were **invalid OOXML** — Word rejected them; only LibreOffice tolerated them. Two independent defects (`docProps/core.xml` binding `dcterms` to prefix `ns2` while using it in a QName-typed attribute; `w:pPr` ordering `spacing` before `pBdr` against ECMA-376 `CT_PPr`). They were repaired by `runtime/tools/prepare_masters.py`, which also retargeted the font to **Calibri**. Pristine originals are archived under `evidence/gates/GATE-02/original_p07_masters/`.

Therefore any master edit must keep `prepare_masters --check` green, preserve the control contract (**17 CV controls, 7 letter controls**, asserted by `preflight` and by tests), preserve `GATE-06` parseability, and be verified by opening the result **in Word**, not only by parsing text. P0.7's "rendering PASS" meant LibreOffice; treat any inherited rendering claim at the scope actually tested.

Note also F12: if you change typography and then want page-warning evidence, that evidence exists **only when PDF conversion succeeds**.

---

## 6. Settled rulings — do not re-litigate

Each of these was contested at least once and settled on evidence. Reopening them costs a cycle and lands in the same place.

### 6.1 Render-before-review provenance

Frozen P0.9 **mandates**: human approval gates submission and irreversible external action only (§2.5, §17.5); deterministic code may render (§6.2); cluster-stage jobs proceed without routine between-job confirmation (§6.3); the three state axes stay separate and must not be collapsed (§7.5 `DEC-42`); `RERUN` starts nothing (§7.6, `DEC-37`).

Frozen P0.9 **permits but does not require** rendering every valid Stage-3 result regardless of triage.

P0.9.1 **selects** render-all-valid as operating policy. Keep that distinction in any document you write. Do not present the selected policy as a frozen rule, and do not "discover" that the architecture mandates it.

### 6.2 A superseded render receipt stays `FAILED` — the `NOT_RENDERED` idea was tried and rejected

An independent audit proposed representing a receipt invalidated solely by a replaced semantic final as `NOT_RENDERED` rather than `FAILED`. It was **implemented, tested and reverted**. Do not re-propose it without new evidence.

Why it fails: by F23, `artifact_hash` excludes `finalization` by design, so a *superseded* binding and a *fabricated* binding are indistinguishable in shape. The change consequently also reclassified an unverifiable receipt and broke four pre-existing assertions — `test_t09_semantic_final_is_not_inferred_from_a_render_file` ("a receipt without its current semantic final cannot remain current") and `test_t09_pdf_degradation_does_not_change_semantic_triage[READY|CHECK|RERUN]` ("an unverified synthetic receipt must not be presented as current"). Both carry explicit `ACC-05`/`DEC-42` rationale. Separating the cases would need output-existence and hash logic far beyond a bounded repair, trading an integrity property for a transient exit code.

Resolution shipped: runtime unchanged; `RUNBOOK.md` recognizes the state. The interrupted-cluster rule covers `NOT_RENDERED` **or** `FAILED`, explains that a `FAILED` render usually means a superseded receipt that `finalize` + `render` repairs, and keeps `DEGRADED` out (a completed render whose PDF needs manual export).

**This is why the retained synthetic run shows `render FAILED`.** It is expected, not a defect.

### 6.3 `DEC-38` means *explicit*, not *human*

`DEC-38`/`ACC-17`: the date becomes canonical when the package is "explicitly finalized/approved for first rendering … not an incidental render side effect." The load-bearing force is **explicitness**, not human agency — §17.5 enumerates the human-only acts and date assignment is absent; §6.2 grants rendering to tooling. `finalize` stays a separate explicit command; only the acting party changed. Settled; do not reopen.

### 6.4 Duplicating the Norwegian doctrine in English was rejected twice

A five-item Stage-2 gate and a nine-item Stage-3 English rubric were both proposed and both deleted, because they restate `WRITING_DOCTRINE.md` in weaker English and create a second source of truth that will drift. The accepted alternative was a **named-section pointer**: Stage 3 applies `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten` by name; Stage 1 points at `Single Backbone og strategisk asymmetri` and `WRONG_ROUTE`. See §5.2 before proposing new prose rules.

### 6.5 Attribution is fixed by documentation, not migration

The `--reviewed-by` collision (F4) is resolved by RUNBOOK wording. A rename or field migration of `reviewed_by`/`finalized_by` was considered and rejected: `finalized_by` is already correctly named and its default `"operator"` is already truthful.

### 6.6 Preflight role-mapping warning: rejected, and now moot

Proposed, deleted. Its test would have read the real `policy/` tree through `conftest.py` (F20) and failed the moment `GATE-10` was performed — which has now happened. The hole was closed by *moving* the existing RUNBOOK reminder to immediately before `freeze`. Zero code.

### 6.7 Bounded recovery is bounded and loop-safe

Refusal 1 → `FAILED`, correct once with the same handoff. Refusal 2 → correction limit reached, request fresh Stage-3 context (the configured semantic retry). Refusal 3 → correct once under the new attempt. Refusal 4 → `BLOCKED_MANUAL`, after which `context` refuses and `next` skips. A repeated `job_id` from `next` means recovery in progress, not a hang — documented in the RUNBOOK. `next --stage N` also surfaces a job whose current failure record is a `FAILED` attempt at that same stage, so a failed *replacement* no longer hides behind an older valid downstream artifact.

---

## 7. Environment traps

- **There is no `.git` anywhere in this checkout.** Git commits and `git diff` are impossible. Use an external pre-change snapshot plus `git diff --no-index`, or a hash registry. Any plan step that says "commit per change" is wrong here.
- **Word COM availability is session-dependent.** The P0.9.1 implementation session could not activate it and reported 240 passed / 10 skipped; an interactive session on the same machine, path and venv reproduced **251 passed / 0 skipped**. A COM failure is a session-context fact, not a converter defect. Do not change converter code because one agent context could not activate Word.
- **Reading CLI output through a pipe can mangle non-ASCII.** Inspecting `jobbsok context` through a shell pipe produced `JobbsÃ¸k` in path strings; reading the same output from a file as explicit UTF-8 resolved every path correctly. Verify paths by `Path(...).is_file()`, not by eyeballing piped text.
- **Test settings must be written before `freeze`** (F24). The existing `staged` fixture freezes immediately, so a test needing different settings needs its own fixture ordering.
- **`staged` fixture finals are not finalized** — `test_t19_render_refuses_before_finalization` depends on that.
- Use scratch paths outside `P0.9/Build/` for destructive work and for `--basetemp`. Do not inventory `.venv/`, `__pycache__/`, `.pytest_cache/`.
- Running a public-command smoke from the real Build root **creates a real run in `runs/`**. Move it to scratch afterwards, or it sits in the operational run list.

---

## 8. Verification baselines and commands

```powershell
.\.venv\Scripts\python.exe -m pytest runtime/tests -q -p no:cacheprovider --basetemp <scratch outside Build>
.\.venv\Scripts\python.exe -m tools.prepare_masters --check
.\.venv\Scripts\python.exe -m tools.vertical_slice --workdir <scratch>
.\.venv\Scripts\jobbsok.exe preflight
```

| Proof | Expected |
|---|---|
| Full suite, Word COM available | **251 passed / 0 skipped / 0 failed** |
| Full suite, no Word COM | 241 passed / 10 skipped — **skips are not passes**, name each |
| Adversarial set (`t09_t12`, `t13_t15`, `t16_t18`, `traceability`) | 130 passed |
| `test_t19_t23_render_security.py` alone | 41 passed |
| `prepare_masters --check` | PASS, 0 reorders, 0 font retargets, 0 page-break removals, control contract preserved |
| Vertical slice | PASS, 21 steps, 0 unexpected, 4 outputs, `render overall : OK` |

251 = the 250-test post-P0.9.1 baseline plus one regression added in the bounded-repair pass. `runtime/tests/test_traceability.py` enforces that every Tier-1 item and mechanical `ACC` id names a real test by `test_tNN_` prefix — new tests must keep the owning prefix.

---

## 9. What P0.9.1 changed (so you can tell new from old)

Eight changes plus one characterization test, across ten files:

1. `RUNBOOK.md` rewritten for the Codex **stage × cluster** operator model: vacancy loop, `submission.command` run verbatim, immediate Stage-3 `finalize`+`render` for all three triage values, disk-derived continuation, bounded-recovery rule, `--reviewed-by` rule, summary from one `status --json`, page-warning limitations, `GATE-10` reminder relocated to just before `freeze`.
2. Stage 3: false "human explicitly finalises" sentence removed; `READY` calibrated against defensive `CHECK`.
3. Stage 3: writing policy named; `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten` applied before triage; cross-job reset added.
4. Stage 1: cross-job reset, decision density, named doctrine-section pointer.
5. Versions: `pyproject.toml` and the three changed control-plane frontmatters → `0.9.1`; everything normative stays `0.9.0`.
6. `cmd_context`: additive `write.schema_paths` + `write.return_paths`, and a literally executable `submission.command` (no angle-bracket placeholders).
7. `stage-submit` refusal prints the recovery record it already wrote.
8. `[render.soft_warnings]` page targets connected to advisory warnings; `render` prints document warnings even when the document is `OK`.

Bounded repair afterwards: `next --stage N` surfaces a failed replacement at that stage (`status.next_job` + `cmd_next`); RUNBOOK recognizes the superseded-receipt state.

**Stage 2's instruction and `policy/writing/*` were deliberately not touched** in any of this.

---

## 10. Deferred — reasons on record

Rejected or deferred after deliberation: a preflight role-mapping warning; wiring the six dead settings (F22); adding `warnings` to `status` (needs a schema edit, F10); any new English quality rubric in a stage file; renaming/migrating `reviewed_by`/`finalized_by`; new commands (`review`, `release`, `approve`, `restart`, `unblock`, …); a preview-render mode; a second approval/release state; render→Stage-3 feedback automation; generic `--json`; an intake compiler; new vacancy fields; new output modes; CV-section visibility schema; dormant template zones; automatic employer research; duplicate-vacancy detection; evidence-excerpt commands; automatic pilot-log tooling; concurrency; LLM-as-judge or any runtime numeric score; hard page/bullet/competency/paragraph limits; deterministic truncation or auto-fit; a similarity/convergence detector; any migration or compatibility shim.

A deferred item returns only on repeated real-production evidence that also beats the smallest local remedy.

---

## 11. The MVP-KISS rules that governed — and how this pass differs

The three prior passes ran under a hard filter: prefer deletion to addition, documentation to code, one helper to a subsystem, an existing command composed by the operator to new runtime; between two correct options take the smaller; if unsure whether something is needed, don't build it. Expansion budget was literally zero across every axis.

**This pass deliberately relaxes that**, per the active prompt: minor complexity increases are acceptable where the expected employer-facing gain is significant and pilot-evidenced, and the change surface must be wide enough to fully realize the gain — *but only that wide*. The invariants that did **not** relax: no new semantic stage, no numeric quality score or LLM judge, no deterministic humanizer, no personality-derived facts, no automatic submission, no truncation to satisfy page targets, no architecture amendment without an explicit smallest normative diff.

Useful question when weighing a candidate change: *would I delay the representative cluster to implement this?* If not, record it and move on.

---

## 12. Open and owed

- `pilot/PILOT_LOG.csv` appears not to have received the two-job observations (§3). Spec §18.3 and `ACC-20` expect per-job triage, actual repair scope, submit-ready, factual corrections, human minutes, render issues, friction and outcome.
- `VISUAL_HUMAN` formally owed; practically discharged by inspecting the two pilot renders.
- Semantic product quality remains unproven by any mechanical evidence (`INV-08` forbids citing engineering results as product evidence).
- Cross-job semantic carryover under a real shared context window is unproven at cluster scale — §6.4 of the frozen spec explicitly declines to claim it is controlled, and defers it to `EXP-01`/`EXP-07`.
- The output-directory ACL/access issue reported during the pilot has not been reproduced or root-caused in this line of work.

---

## 13. One-paragraph orientation

The framework is architecturally settled and mechanically green. Three prior passes removed speculative expansion and closed the last local defects; the two-vacancy pilot then succeeded on real work. What remains is a *writing-quality* problem, not a systems problem — and the strongest available evidence says the relevant rules already exist, in Norwegian, in files the pilot actually froze and used. Spend this pass finding out why in-force rules did not reach the page, and change the smallest thing that makes them reach it.
