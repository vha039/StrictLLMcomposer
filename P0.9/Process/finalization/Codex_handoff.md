# Jobbsøk_26 P0.9.1 — handoff after the first two-vacancy pilot

**Prepared:** 2026-08-31  
**Repository:** `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`  
**Implementation root:** `P0.9/Build`  
**Completed pilot run:** `r20260828-213932-7f13b4`  
**Pilot cluster:** `pilot_live_smoke`

## 0. Purpose and evidence discipline

This file is an onboarding handoff for the fresh instance that will plan and
then implement the small set of improvements identified after the first two
real vacancies. It deliberately combines:

- the authority and scope decisions established before P0.9.1;
- the implemented P0.9.1 patch and its later bounded repair;
- the independent acceptance-audit findings;
- current repository evidence from the completed two-vacancy run;
- the latest test result reproduced while preparing this handoff;
- explicit unknowns that the next instance must not fill by inference.

This handoff is **context and evidence, not governing authority**. The next
instance must re-read the current user request, the repository-root `AGENTS.md`,
the two frozen P0.9 architecture files, and the final P0.9.1
specification/instructions before changing anything. Actual current code and
artifacts are implementation truth. Any statement here that disagrees with
current disk state is stale.

Evidence labels used below:

- **USER-REPORTED:** said by the user, but not independently reconstructable
  from repository state alone.
- **CURRENTLY VERIFIED:** read or executed against the repository on
  2026-08-31.
- **HISTORICAL VERIFIED:** supported by retained reports or earlier execution
  evidence, but not rerun in the handoff session.
- **UNKNOWN:** not present in this conversation or the inspected repository;
  obtain it rather than guessing.

## 1. Executive state at handoff

1. **USER-REPORTED:** The initial two-vacancy test is complete, was a
   significant overall success, and exposed some final improvements worth
   planning and implementing in a fresh instance.
2. **CURRENTLY VERIFIED:** Both vacancies reached current, finalized Stage-3
   packages with `semantic_triage = READY`, `production_state = VALID`,
   `highest_valid_stage = FINAL`, current final+review bindings and valid DOCX
   outputs.
3. **CURRENTLY VERIFIED:** The retained run has truthful render degradation:
   both DOCX documents are `OK` for both vacancies, while all four PDFs are
   `DEGRADED` because Word COM activation failed in that run. The semantic
   packages remain valid. Failed conversion produced `page_count = null` and
   `warnings = []`, which is expected.
4. **CURRENTLY VERIFIED:** The earlier acceptance-audit defect in which a
   failed replacement could be hidden behind an older downstream artifact has
   already been fixed in `status.next_job` and `cli.cmd_next`. Its focused
   regression passed again during preparation of this handoff.
5. **CURRENTLY VERIFIED:** The other audit interaction—an old render receipt
   after a replacement Stage-3 final—is intentionally represented as render
   `FAILED`. The runtime was not weakened to relabel an unverifiable receipt.
   The RUNBOOK continuation rule now treats `NOT_RENDERED` **or** `FAILED` as
   owed internal production and repairs it with idempotent `finalize` followed
   by `render`. `DEGRADED` remains terminal and is not rerun automatically.
6. **CURRENTLY VERIFIED:** GATE-10 is closed as `PASS_USER_VERIFIED`; current
   production role mapping is:
   - `SOL_CLASS = "Codex / GPT-5.6 Sol"`
   - `TERRA_CLASS = "Codex / GPT-5.6 Terra"`
7. **CURRENTLY VERIFIED, NEW DEFECT:** A fresh full suite now reports
   **239 passed / 2 failed / 10 skipped**. Both failures are test-only coupling
   to the now-populated production role mapping. This does not show a pilot
   runtime failure, but it must be repaired so the suite is configuration
   independent again. The total suite now contains 251 tests.
8. **UNKNOWN AND LOAD-BEARING:** The user did not state the exact post-pilot
   improvement list, its priorities, or the desired before/after behavior in
   this conversation, and no dedicated improvement report was found in the
   inspected repository or Downloads directory. The fresh instance must load
   that list from the user or an attached source **before designing changes**.
   Do not reverse-engineer the intended list from Stage-3 limitations or this
   handoff.

The correct starting posture is therefore: the core pilot succeeded; the
framework is not awaiting another architecture pass; one concrete test-fixture
regression is already visible; all additional improvements require the user's
actual post-pilot observations.

## 2. Authority model and non-negotiable architecture

Apply authority in this order:

1. the fresh instance's explicit user request and any explicitly attached
   post-pilot decision document;
2. `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md`;
3. `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`;
4. explicit user-authorized architecture amendments, if any;
5. actual current `P0.9/Build` behavior as implementation truth;
6. final P0.9.1 specification/instructions for the retained patch and its
   control-plane wording;
7. this handoff, audits, plans and completion reports as evidence only.

The four files under `P0.9/Architecture/` are frozen. Do not edit them unless a
new user request explicitly authorizes an architecture amendment. Files under
`P0.9/Process/` are provenance, not authority. All `AGENTS.md` files under
`P0.7/` describe the retired four-stage system and are hazardous stale context,
not instructions for current work.

Hard boundaries that survived P0.9.1 and the pilot:

- Every material candidate claim must be truthful, correctly attributed and
  interview-defensible.
- Candidate facts can be raised only by the three factual authorities:
  `Work_experience.md`, `Education.md` and
  `Other_high_value_information.md`.
- Candidate, employer and vacancy identity must be exact.
- The deterministic runtime makes no model call, network call, employer
  contact, publication or submission.
- Human approval is mandatory before submission or any irreversible external
  action.
- There is no runtime numeric quality/fit judge, automatic model orchestration
  or automatic retry.
- Every CORE job always receives a Bokmål CV and letter. No language,
  `letter_required`, channel, portal or output-mode branch belongs in core.
- Semantic triage, mechanical/production state and render state remain three
  separate axes.
- Same-run amendment, event sourcing, authoritative progress markers, a
  dedicated RERUN subsystem, a dependency engine, a fourth stage, hard content
  thresholds, multi-model automation and approval abstractions remain
  prohibited redesigns.

## 3. Required operating sequence and provenance wording

The required production behavior remains:

```text
freeze
→ Codex Stage 1 × cluster
→ Stage 2 × cluster
→ Stage 3 × cluster
→ valid final+review
→ explicit finalize
→ render/verify
→ cluster summary
→ human reviews actual rendered package
→ human submits/revises/reruns/drops
```

No routine human checkpoint exists between successful Stage 3 and rendering.
`READY`, `CHECK` and `RERUN` describe semantic repair scope; they do not gate
rendering. Rendering and finalization are reversible internal production, not
human approval. External irreversible action remains human-only.

Use the provenance wording precisely:

- frozen P0.9 **mandates** human approval for submission and irreversible
  external action;
- frozen P0.9 **permits** deterministic rendering and mandates cluster-stage
  operation without routine between-job confirmation;
- frozen P0.9 **permits but does not mandate** rendering every valid Stage-3
  result regardless of triage;
- P0.9.1 **selects** render-all-valid as operating policy.

Never present render-all-valid as a frozen P0.9 rule.

## 4. What P0.9.1 implemented

The original P0.9.1 patch was deliberately small: eight retained changes in
exactly ten files, with no architecture or schema edit.

### 4.1 The eight retained changes

1. **RUNBOOK operating flow:** stage × cluster processing; vacancy-atomic fresh
   `next`/`context`; verbatim emitted submission command; immediate explicit
   finalize/render for all triage values; disk-derived continuation; correct
   `reviewed_by`/`finalized_by` wording; cluster summary; GATE-10 reminder moved
   immediately before `freeze`.
2. **Stage-3 policy references:** Stage 3 names both writing policies and uses
   `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten`.
3. **Stage-3 reset/reconstruction/triage:** explicit cross-job reset;
   reconstructive authority rather than mere polishing; calibrated `READY`;
   immediate deterministic finalize/render without calling it approval.
4. **Stage-1 decision density/reset:** explicit reset, decision-dense strategy,
   reference to `Single Backbone og strategisk asymmetri`, and `WRONG_ROUTE`,
   without inventing another quality rubric.
5. **Implementation version:** package/control-plane version `0.9.1`, while
   `SPEC_REVISION`, `SCHEMA_REVISION`, manifest constants and settings spec
   revision remain `0.9.0`.
6. **Context I/O:** all four modes expose real frozen schema paths,
   handoff-scoped return paths and a quoted executable PowerShell submission
   command.
7. **Refusal recovery output:** the just-written failure payload is printed,
   including classification, correction count, semantic attempt and next
   action, without changing state or retry policy.
8. **Soft page warning:** configuration-driven per-document warning only after
   successful PDF page counting, stored in the existing warnings array; failed
   PDF conversion produces no page warning.

`cmd_finalize` received no triage branch because it was already correctly
triage-independent. No change was manufactured.

### 4.2 Original ten-file patch

- `P0.9/Build/BUILDER_REPORT.md`
- `P0.9/Build/policy/RUNBOOK.md`
- `P0.9/Build/policy/stages/stage1_decision_architecture.md`
- `P0.9/Build/policy/stages/stage3_final_writer_review.md`
- `P0.9/Build/pyproject.toml`
- `P0.9/Build/runtime/jobbsok/cli.py`
- `P0.9/Build/runtime/jobbsok/render.py`
- `P0.9/Build/runtime/tests/test_t01_t04_run_lifecycle.py`
- `P0.9/Build/runtime/tests/test_t05_t08_ownership_schema_failure.py`
- `P0.9/Build/runtime/tests/test_t19_t23_render_security.py`

The original final scope gate found no new dependency, command, parser branch,
schema, runtime module, status field, state axis, authority, client, automatic
retry, approval abstraction, hard threshold or architecture edit. The version
edits were exactly four lines.

## 5. Acceptance audit and what happened afterward

### 5.1 Initial independent audit

`OPUS_P0.9.1_FINAL_POST_IMPLEMENTATION_ACCEPTANCE_AUDIT.md` returned
`GO_WITH_MINOR_FIXES`. It found no architecture blocker, but identified:

- an old render receipt after a replacement final could appear as `FAILED`
  while Stage-3 `next` was complete;
- a failed replacement attempt could be hidden from its own stage-specific
  queue by an older valid downstream artifact;
- the audit session could not activate Word COM, so it observed 240 passed and
  10 skipped rather than the target 250/0;
- dormant `converter = "auto"` implements Word→LibreOffice failover, contrary
  to the frozen no-multi-converter boundary, but production uses `word_com`, so
  removal was classified `DEFER` rather than worth a cross-schema cleanup.

It strongly kept the truth boundaries, state separation, three-stage writing
design, P0.9.1 ten-file scope and human-only external action.

### 5.2 Independent target-machine evidence

A second retained audit in Downloads records an unlocked interactive session
on the same machine with:

- full suite **250 passed / 0 skipped / 0 failed**, reproduced twice;
- the Word render file **41 passed**;
- vertical slice PASS with `render overall: OK` and verified PDFs;
- preflight PASS;
- successful-PDF page-warning assertions green.

This proved the earlier `0x80070520` failure was session-context-specific, not
a general machine/converter defect.

### 5.3 Bounded repair pass now present in the repository

The current `BUILDER_REPORT.md` records both reported interactions as reproduced.

**Superseded render receipt:** A proposed runtime reclassification to
`NOT_RENDERED` was rejected after it broke four existing ACC-05/DEC-42
integrity assertions. Because `artifact_hash` deliberately excludes
`finalization`, the bounded code path could not safely distinguish a superseded
receipt from a fabricated/unverifiable binding. The retained solution is
documentation/control-plane only:

- status continues to report an unverifiable receipt as `FAILED` and exposes
  no old output paths;
- interrupted continuation repairs any valid semantic final with render
  `NOT_RENDERED` **or** `FAILED` by running `finalize` then `render`;
- `DEGRADED` stays excluded because it is a completed render needing manual PDF
  export, not owed internal work.

**Failed semantic replacement hidden by an old final:** Fixed locally:

- `status.next_job(..., failed_at_stage=...)` accepts a transient set;
- `cli.cmd_next` loads existing job-local current failure records and passes
  jobs whose `FAILED` operation matches the selected stage;
- a matching failed job is selected before the highest-valid-stage ladder;
- mismatched stages remain silent; `BLOCKED_MANUAL` remains skipped; successful
  replacement clears the failure and queue;
- no persisted state, status field, command, retry or schema was introduced.

Material repair files:

- `runtime/jobbsok/status.py`
- `runtime/jobbsok/cli.py`
- `runtime/tests/test_t05_t08_ownership_schema_failure.py`
- `policy/RUNBOOK.md`

Historical post-repair proof was **251 passed / 0 skipped / 0 failed**, 130
adversarial passes, canonical masters PASS and vertical slice PASS with four
outputs and Word COM green. The 251 total is the 250-test P0.9.1 baseline plus
one focused recovery regression.

## 6. GATE-10 and pre-pilot closure

The current repository records `GATE-10` as `PASS_USER_VERIFIED` in
`P0.9/Build/evidence/gates/GATE_REPORTS.md`:

- actual role surfaces: GPT-5.6 Sol for `SOL_CLASS`, GPT-5.6 Terra for
  `TERRA_CLASS`;
- local Codex session with direct workspace and CLI access;
- no reliance on cross-session conversation memory for stage context;
- signed-in chats remain in account history until deleted; deletion is
  scheduled within 30 days subject to documented exceptions;
- business inputs/outputs are not used for model training by default, and no
  explicit training opt-in is used;
- each semantic stage uses a fresh agent session and only required repository
  context;
- deterministic runtime performs no model/network/employer/submission action.

The current `policy/settings.toml` contains the two role mappings. The pilot
manifest froze the same mapping, as required. `BUILDER_REPORT.md` records
`GO_FOR_TWO_JOB_PILOT` as the pre-pilot verdict.

Do not blank or overwrite the production mapping merely to make tests pass.
Fix tests so they control their own fixture configuration.

## 7. Completed two-vacancy run

### 7.1 Run identity and aggregate state

- Run: `r20260828-213932-7f13b4`
- Cluster: `pilot_live_smoke`
- Jobs: 2 CORE, no exception
- Stage outcome: 2 current FINAL packages, 2 READY, 2 VALID
- Stale/failed/blocked: 0 semantic jobs
- Render: 2 `DEGRADED`, because DOCX succeeded and automated PDFs did not
- Final document date: 2026-08-29
- Finalizer recorded by runtime: `operator`

Current aggregate status is retained at:
`P0.9/Build/generated/views/r20260828-213932-7f13b4/status.json`.

### 7.2 Vacancy 1 — Huseierne

**Identity**

- Job id: `huseierne_strategi_maalstyring`
- Employer: Huseiernes Landsforbund
- Title: Strategi- og målstyringsrådgiver
- Sequence/priority: 1 / HIGH
- Triage: READY

**Stage-1 route:** Strategy centered on practical governance, shared method,
decision support and implementation rather than pretending direct OKR or
long-tenure/product-organization experience.

**Stage-2 package:** Complete tailored Bokmål CV and letter, using CV as
evidence and the letter as the employer-facing argument.

**Stage-3 reconstruction:** Removed the Stage-2 letter's defensive paragraph
about lacking direct OKR experience and shorter tenure. Those limits were
preserved in review rather than foregrounded to the employer. The employer
text prioritizes truthful transferable evidence and Huseierne's concrete
governance problem.

**Final positioning:** “Samfunnsøkonom og rådgiver | styringsinformasjon,
felles metode og gjennomføring.” The main evidence is the hospital-wide
benefit-realization framework, modernization/use of a business-critical budget
tool, and decision support for economy/staffing/activity/capacity.

**Stage-3 known limitations, not defects:**

- no documented practical OKR experience;
- documented relevant OUS experience starts March 2023 and is shorter than the
  vacancy's five-year minimum;
- no documented formal product-organization experience, private commercial
  P&L responsibility or production-depth Azure/Fabric experience.

**Output evidence:** Current CV and letter DOCX both pass structural/openability,
identity, placeholder/private-token and dynamic-content checks. PDF conversion
in the retained run degraded.

### 7.3 Vacancy 2 — Avinor

**Identity**

- Job id: `avinor_digital_transformasjon`
- Employer: Avinor AS
- Title: Seniorrådgiver Digital Transformasjon
- Sequence/priority: 2 / NORMAL
- Deadline frozen in run: 2026-09-13
- Triage: READY

**Stage-1 route:** Controlled digital change, benefit discipline and
technology-to-business translation in a regulated environment. Claim ceilings
preserved around enterprise portfolio ownership and formal leadership.

**Stage-2 package:** Complete tailored Bokmål CV and letter, grounded in actual
delivery/use and a hospital-wide method rather than generic “transformation”
rhetoric.

**Stage-3 reconstruction:** Made controlled digital change the first proof,
benefit methodology the second, and the creation of the Analysis Department
supporting evidence for Avinor's new transformation environment. Removed an
unimplemented proxy design and the Stage-2 letter's defensive paragraph about
lacking formal responsibility.

**Final positioning:** “Samfunnsøkonom og rådgiver | digital endring, gevinst
og gjennomføring.” The main evidence is modernization of a business-critical
budget tool under controlled operational constraints, the hospital-wide
benefit-realization framework and cross-functional decision support.

**Stage-3 known limitations, not defects:**

- no documented formal enterprise transformation, portfolio, program,
  product, line or personnel responsibility;
- actual use/duration is documented, but quantified gains, safety effect, time
  saving and realized ROI are not;
- aviation is a new domain and current security-clearance status is not
  documented.

**Output evidence:** Current CV and letter DOCX both pass structural/openability,
identity, placeholder/private-token and dynamic-content checks. PDF conversion
in the retained run degraded.

### 7.4 What the pilot demonstrates

- Vacancy-atomic Stage 1 and Stage 2 operation worked for both CORE jobs.
- Fresh context and verbatim submission paths were used.
- The system handled scanned vacancy PDFs with no extracted text by requiring
  visual inspection of original pages.
- An embedded AI-generated JobMatch panel was explicitly excluded as vacancy
  evidence.
- The two jobs received materially different strategic routes.
- Stage 3 acted reconstructively, made CV and letter complementary, preserved
  evidence/claim ceilings, moved candid limitations to operator review and
  returned actionable READY triage.
- Finalize and render produced current employer-facing DOCX files for both
  jobs without making PDF failure a semantic failure.

This is credible evidence that the three-stage design can produce useful,
native, restrained and truth-bound packages. It does not by itself prove
interview conversion or universal cross-job quality.

### 7.5 What is not recorded

`P0.9/Build/pilot/PILOT_LOG.csv` still contains only its header. Therefore the
repository does not currently retain:

- the human's actual quality score or exact edit list per job;
- minutes through submission decision;
- factual corrections made after rendered review;
- final actual repair scope versus Stage-3 triage;
- whether either job was submitted, revised, rerun or dropped;
- portal outcome or interview result.

The user reports significant success and identified improvements, but their
exact content is not in the inspected sources. The next instance should treat
the user's explicit improvement list as new controlling input, not invent a
surrogate from the empty log or from Stage-3 known limitations.

## 8. Newly reproduced current test regression

While preparing this handoff, the focused failed-replacement regression passed:

```text
1 passed in 3.07s
```

The fresh complete suite, using an external basetemp, produced:

```text
239 passed, 2 failed, 10 skipped in 89.76s
```

The ten skips are the known Word-COM-scoped cases in this non-interactive
session. They are skips, not passes. The two failures are new only because the
human correctly populated production role mapping after the tests were written:

1. `test_t05_public_handoff_completes_all_stages_and_review_only`
   asserts `stage1["configured_model"] is None`, but current frozen fixture
   policy yields `"Codex / GPT-5.6 Sol"`.
2. `test_t05_context_exposes_configured_capability_surface`
   tries the literal replacement `SOL_CLASS = ""` → synthetic value. The
   production line is no longer blank, so replacement is a no-op and context
   returns the real mapping rather than `"synthetic-sol-surface"`.

This directly violates the earlier explicit requirement: **do not write a test
whose expected outcome depends on a production configuration value the human
must change**, because `conftest.py` copies the real `policy/` tree.

Smallest sufficient repair, to be planned—not performed by this handoff:

- remove the irrelevant `configured_model is None` assertion from the public
  all-stage handoff test, or make that test set its own explicit fixture mapping
  before freeze;
- make the capability-surface test replace the `SOL_CLASS` mapping regardless
  of its current value, scoped to the `[stages.role_mapping]` line, then assert
  the test-owned synthetic value;
- do not change production `settings.toml`, runtime behavior, schema or
  GATE-10 evidence to accommodate the test;
- after the repair, current expected totals are **241 passed / 10 skipped** in
  a session without Word COM and **251 passed / 0 skipped / 0 failed** in the
  unlocked interactive target session.

Prefer modifying the two existing assertions/helpers in the existing test
file. Do not add a new test file or configuration subsystem.

## 9. Residual issues and their correct disposition

### KEEP

- frozen truth and evidence boundaries;
- exact immutable freeze/currentness model;
- Stage 1 strategy ownership, Stage 2 draft ownership, Stage 3 final+review
  ownership;
- reconstructive Stage 3 and triage-independent rendering;
- failure records separate from last valid artifacts;
- no-clobber, output containment and current receipt verification;
- PDF failure as render degradation only;
- human-only submission/external action;
- the current two-role mapping and GATE-10 record;
- the RUNBOOK solution for superseded render receipts;
- the current failed-replacement queue repair.

### FIX IN THE FRESH PASS

- the two production-configuration-dependent tests above;
- the user's actual post-pilot improvements, but only after their exact
  desired behavior and evidence are loaded.

### PILOT FIX ONLY IF ACTUALLY OBSERVED

- native voice or employer specificity misses;
- incorrect READY/CHECK/RERUN calibration;
- cross-job semantic carryover;
- insufficient CV tailoring or CV/letter repetition;
- page-target warning usefulness;
- material operator handling burden.

Do not generalize from one stylistic preference into a new global rubric unless
both real packages show a recurring material miss.

### DEFER

The dormant `converter = "auto"` branch sequentially tries Word COM and
LibreOffice, while frozen P0.9 prohibits multi-converter failover
infrastructure. The exact production snapshot uses `word_com`; removal would
touch config, schemas, runtime and tests without helping the observed pilot.
Keep it deferred unless a future user decision deliberately revises converter
policy.

## 10. Historical guardrails for the improvement plan

The original planning request imposed these useful anti-redesign constraints.
They remain good defaults unless the new explicit post-pilot decision overrides
them:

- Prefer no code where behavior is already correct.
- Minimize diff surface; every changed line must trace to an observed defect or
  explicit user decision.
- Reuse existing code paths, helpers, fixtures and test files.
- No drive-by refactor.
- Use TDD for mechanical changes that can produce plausible but wrong output:
  first add/extend the assertion, run it and observe the expected failure, then
  implement.
- Do not substring-test Markdown prompt quality. Human/model quality is not
  proven by prompt text assertions.
- Do not add a preflight warning for `[stages.role_mapping]`; the human gate is
  already documented and frozen into the manifest.
- Do not wire unrelated dead settings (`runs_root`, `generated_root`,
  `pilot_log`, `pdf_required`, personality profile/index or `[spec].*`) unless
  the new observed defect actually requires them.
- Do not add warnings to status; its schema is closed.
- Do not add a new English writing rubric. Existing Norwegian gates live in
  `policy/writing/WRITING_DOCTRINE.md`.
- Do not edit Stage 2 or `policy/writing/*` merely because they were read.
- Do not rename/migrate `reviewed_by` or `finalized_by`; human attribution is on
  freeze/branch, and finalize records only the internal operator.
- Do not add new command, schema, state, dependency, client, automatic retry,
  approval abstraction or hard threshold without exceptional observed need.
- Do not edit `P0.9/Architecture/*`.

## 11. Recommended fresh-instance workflow

### Phase A — establish the actual requested delta

1. Read completely:
   - repository-root `AGENTS.md`;
   - both final P0.9.1 attached documents;
   - `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md`;
   - `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`;
   - this handoff;
   - `OPUS_P0.9.1_FINAL_POST_IMPLEMENTATION_ACCEPTANCE_AUDIT.md`;
   - current `P0.9/Build/BUILDER_REPORT.md` bounded-repair and pre-pilot
     sections;
   - current pilot `status.json`, both `review.json` files and, only as needed,
     final packages.
2. Obtain the user's exact post-pilot improvement list. Record each requested
   before/after outcome and whether it is mechanical, control-plane,
   employer-facing semantic quality or operator friction.
3. Reconcile each claim against current code. Explicitly distinguish:
   - already correct → KEEP/no change;
   - test-only defect;
   - observed production defect;
   - preference that can be learned during the next real batch;
   - prohibited redesign.
4. Re-baseline current files. This is not a Git repository. Do not assume the
   old ten-file P0.9.1 hash registry describes the post-pilot tree.

### Phase B — plan the smallest sufficient patch

1. Consolidate symptoms by root cause; one repair should not produce multiple
   overlapping abstractions.
2. Give documentation-only, test-only and runtime changes separate plan
   sections.
3. Name exact files, functions, assertions and public flows.
4. Preserve current role mapping and the completed pilot run.
5. Use scratch basetemp/work directories outside `P0.9/Build` for destructive
   verification.
6. If the user asks for a plan-only turn, do not implement, regenerate views,
   render, freeze, branch or mutate run state.

### Phase C — implement and verify

1. Start with the current role-mapping test regression because it is bounded,
   test-only and independently reproduced.
2. For each additional mechanical change, demonstrate the old failure before
   changing production code.
3. Run focused tests, then the adversarial regression set, then the full suite.
4. In an unlocked interactive Windows/Word session require **251 passed / 0
   skipped / 0 failed** after the test repair, unless the deliberate patch adds
   a justified new test (then adjust the arithmetic explicitly).
5. Run canonical-master and vertical-slice proofs with external scratch paths.
6. Exercise actual public commands from the real non-ASCII Build path. Inspect
   output rather than inferring success from exit status alone.
7. Recheck final scope: no unintended dependency/schema/command/module/state/
   authority/client/retry/approval/threshold/architecture change.
8. Preserve the completed pilot artifacts. Do not use the real pilot run for
   destructive recovery tests.

## 12. Exact PowerShell verification commands

Run from:
`C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build`

```powershell
# Focused current queue repair
.\.venv\Scripts\python.exe -m pytest `
  runtime\tests\test_t05_t08_ownership_schema_failure.py::test_t08_failed_replacement_is_surfaced_by_its_own_stage_queue `
  -q -p no:cacheprovider `
  --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-focused

# Full suite; use a fresh external basetemp path
.\.venv\Scripts\python.exe -m pytest runtime\tests -q -p no:cacheprovider `
  --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-full

# Adversarial regressions
.\.venv\Scripts\python.exe -m pytest `
  runtime\tests\test_t09_t12_state_evidence.py `
  runtime\tests\test_t13_t15_merge_leakage_personality.py `
  runtime\tests\test_t16_t18_containment_template.py `
  runtime\tests\test_traceability.py `
  -q -p no:cacheprovider `
  --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-adversarial

# Canonical masters
.\.venv\Scripts\python.exe -m tools.prepare_masters --check

# Vertical slice, entirely outside Build
.\.venv\Scripts\python.exe -m tools.vertical_slice `
  --out C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-evidence `
  --workdir C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-work

# Read-only inspection of the completed pilot view
Get-Content -Raw `
  .\generated\views\r20260828-213932-7f13b4\status.json
```

Do not reuse a basetemp directory from an interrupted run without first
choosing another path. Do not treat skipped tests as passes.

For public-command smoke, use a fresh scratch run rather than the retained
pilot. Inspect all four actual `jobbsok context` JSON modes, execute one emitted
`submission.command` verbatim in PowerShell, exercise all triage values,
repeat finalize without `--date` to prove idempotence, and inspect actual render
receipts. On PDF conversion failure, confirm explicitly that no page warning is
produced.

## 13. High-value file/function map

| Concern | Current location |
|---|---|
| Frozen behavior | `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` |
| Build/prohibited redesign contract | `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md` |
| Operator flow/continuation | `P0.9/Build/policy/RUNBOOK.md` |
| Role mapping/settings | `P0.9/Build/policy/settings.toml` |
| Stage 1 policy | `P0.9/Build/policy/stages/stage1_decision_architecture.md` |
| Stage 2 policy | `P0.9/Build/policy/stages/stage2_package_writer.md` |
| Stage 3 policy | `P0.9/Build/policy/stages/stage3_final_writer_review.md` |
| Status axes/currentness/queue | `P0.9/Build/runtime/jobbsok/status.py` (`_derive_job`, `next_job`) |
| Public context/next/finalize/render | `P0.9/Build/runtime/jobbsok/cli.py` |
| Artifact stamping/replacement | `P0.9/Build/runtime/jobbsok/artifacts.py` |
| Render and warnings | `P0.9/Build/runtime/jobbsok/render.py` |
| Converter behavior | `P0.9/Build/runtime/jobbsok/pdf.py` |
| Failure record | `P0.9/Build/runtime/jobbsok/failure.py` |
| Test fixture policy copy | `P0.9/Build/runtime/tests/conftest.py` |
| Current failing + recovery tests | `P0.9/Build/runtime/tests/test_t05_t08_ownership_schema_failure.py` |
| Render/security tests | `P0.9/Build/runtime/tests/test_t19_t23_render_security.py` |
| GATE-10 evidence | `P0.9/Build/evidence/gates/GATE_REPORTS.md` |
| Patch/repair ledger | `P0.9/Build/BUILDER_REPORT.md` |
| Acceptance audit | `OPUS_P0.9.1_FINAL_POST_IMPLEMENTATION_ACCEPTANCE_AUDIT.md` |
| Completed pilot status | `P0.9/Build/generated/views/r20260828-213932-7f13b4/status.json` |
| Huseierne final review | `P0.9/Build/runs/r20260828-213932-7f13b4/jobs/huseierne_strategi_maalstyring/current/review.json` |
| Avinor final review | `P0.9/Build/runs/r20260828-213932-7f13b4/jobs/avinor_digital_transformasjon/current/review.json` |
| Pilot evaluation log | `P0.9/Build/pilot/PILOT_LOG.csv` (currently header only) |

## 14. Launch/stop criteria for the fresh pass

The fresh pass is done when:

- every explicit post-pilot improvement is either implemented and verified,
  shown already correct, or deliberately deferred with user-visible rationale;
- the two role-mapping-dependent tests are configuration independent;
- the full suite is green in the target Word session with zero skips;
- public flow and rendered outputs remain truthful and current;
- the completed pilot run and GATE-10 mapping/evidence are preserved;
- no frozen architecture or prohibited surface was expanded;
- remaining concerns are genuinely best learned from more real vacancies.

Stop and escalate only if a proposed improvement requires a real architecture
amendment, a destructive/irreversible action, unavailable user-owned evidence,
or an expensive unrecoverable choice. Otherwise prefer the smallest working
repair and continue.

## 15. Bottom line for the next instance

This is not a failed system awaiting rescue. The two-vacancy run produced two
current READY packages with distinct strategies, reconstructive Stage 3 work,
truthful claim ceilings and valid final DOCX output. The right task is a bounded
post-pilot refinement, not a redesign.

Before acting, obtain the user's exact improvement list. Then preserve what the
pilot proved, fix the current test-fixture coupling, make only observed
high-ROI changes, re-establish 251/0/0 on target Word, and return to real
vacancies.
