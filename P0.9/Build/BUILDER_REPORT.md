# Jobbsøk_26 P0.9.1 implementation report

**Regenerated:** 2026-08-28

**Implementation release:** `0.9.1`

**Specification/schema revision:** `0.9.0` / `0.9.0`

**Verdict:** `BLOCKED_USER`

The eight retained P0.9.1 changes and the triage characterization test are
implemented at the specified ten-file scope. A later bounded repair pass added
one queue fix and one documentation reconciliation; see "Bounded repair pass"
below. No real vacancy or model output was consumed.

The target interactive Word COM gate **was not reachable from the
implementation session** but has since been reproduced green in an interactive
session on the same machine, path and virtual environment: **251 passed / 0
skipped / 0 failed**, vertical slice PASS with `render overall : OK` and four
outputs including verified PDFs. The Word failure recorded further below was a
session-context limitation, not a machine or converter defect.

`GO_FOR_TWO_JOB_SMOKE` remains withheld on **human-owed items only**:
`GATE-10` (populate `[stages.role_mapping]` and record the account's
retention/training posture, before the first real freeze) and sparse/normal/
dense human visual QA of rendered output (`VISUAL_HUMAN`, `ACC-18`, Spec 16.7),
which the two real CORE vacancies discharge on real content. No mechanical gate
is outstanding.

## Focal correction

The active control plane now runs one human-initiated stage per cluster and
processes vacancies sequentially from current disk state. After every valid
Stage-3 final + review, the operator immediately finalizes and renders the job
for `READY`, `CHECK` and `RERUN`; rendering is not human approval, and only the
human may submit externally. The documentation states the provenance precisely:
frozen P0.9 permits render-all-valid, while P0.9.1 selects it as operating
policy.

## Implemented scope

1. `policy/RUNBOOK.md` now defines the stage×cluster vacancy loop, disk-derived
   continuation, bounded recovery, immediate Stage-3 finalize/render,
   triage-independent rendering, truthful `reviewed_by`/`finalized_by` usage,
   one `status --json` summary, advisory page-warning limitations, and the
   relocated pre-freeze `GATE-10` role-mapping instruction.
2. `policy/stages/stage3_final_writer_review.md` now names the two writing-policy
   files, applies `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten` before
   triage, resets between jobs, calibrates `READY`, and directs immediate
   deterministic finalize/render without presenting it as approval.
3. `policy/stages/stage1_decision_architecture.md` now resets between jobs,
   requires decision-dense fields, and points to `Single Backbone og strategisk
   asymmetri` and `WRONG_ROUTE` without adding a new quality rubric.
4. The package version and the three changed control-plane frontmatter versions
   are `0.9.1`; all specification/schema version values remain `0.9.0`.
5. `jobbsok context` now emits exact frozen `schema_paths`, disposable
   handoff-scoped `return_paths`, and a fully quoted executable PowerShell
   submission command for all four modes.
6. A refused `stage-submit` now prints the just-written recovery classification,
   mechanical-correction count, semantic-attempt count and exact next action.
   Recovery state and exit codes are unchanged.
7. Successful PDF conversion now derives a configuration-driven soft page
   warning. It uses the existing per-document `warnings` array, changes no
   status/triage/render state and changes no exit code. `render` prints warnings
   for `OK` documents.
8. Existing tests were extended at their owning boundaries; no new test file or
   harness was added.

One review correction was made after implementation: the RUNBOOK now states
explicitly that Stage 3 uses the same vacancy loop as Stages 1 and 2. It is a
local documentation fix that prevents a first-batch control-plane ambiguity and
adds no behavior or surface.

## Files changed

Exactly ten baseline-tracked files differ:

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

The supplied checkout contains no Git metadata at the repository or Build root,
so per-change Git commits were impossible without inventing repository history.
External pre-change hashes and per-change snapshots were used instead. The final
hash comparison covers 99 active source/evidence files while excluding `.venv`,
caches, `runs/`, `generated/` and editable-install metadata.

## TDD evidence

- Triage characterization ran first on the unmodified runtime: **3 passed / 0
  failed**. Public `finalize` was already independent of `READY`, `CHECK` and
  `RERUN`, so no finalization code was changed.
- Change 6: the extended context test first failed with missing
  `write.schema_paths`; after implementation the focused test passed and the
  complete T05–T08 file was **36 passed**.
- Change 7: both recovery-output assertions first failed; after implementation
  both passed and the complete T05–T08 file remained **36 passed**.
- Change 8: the helper test first failed because `_page_target_warning` did not
  exist; after implementation the focused helper/degraded-PDF proof was **2
  passed**, and the render/security file was **31 passed / 10 skipped** in the
  non-COM session.
- Traceability plus lifecycle after documentation/version changes: **89 passed**.
- Bytecode compilation of `runtime/jobbsok` and `runtime/tests`: **PASS**.

## Phase-5 verification

### Exact full suite

Command used from the real non-ASCII Build root, with basetemp outside Build:

```powershell
.\.venv\Scripts\python.exe -m pytest runtime/tests -q -p no:cacheprovider --basetemp <external-scratch>
```

Observed: **240 passed / 10 skipped / 0 failed**, 75.67 s. The post-patch target
total is 250 tests; the ten skips are not counted as passes:

1. `test_t19_target_machine_produces_both_docx_and_verified_pdfs`
2. `test_t19_pdfs_are_independently_verified`
3. `test_t19_norwegian_glyphs_survive_to_the_pdf`
4. `test_t19_public_word_render_handles_realistic_long_norwegian_names`
5. `test_t20_first_finalization_fixes_the_date_and_rerender_preserves_it`
6. `test_t20_rerender_yields_identical_docx_bytes`
7. `test_t20_pdf_container_metadata_variation_is_documented`
8. `test_t21_edited_deliverable_survives_a_rerender`
9. `test_t21_failed_pdf_rerender_retires_prior_pipeline_pdfs`
10. `test_t21_ownership_survives_a_transient_failed_attempt`

Each reported the same legitimate but unresolved reason: **Word COM is
unavailable; GATE-03 fallback is DEGRADED render state.** The required target
result remains **250 passed / 0 skipped / 0 failed** in an unlocked interactive
Windows session with Word COM available.

### Environment and regressions

- Real-root `jobbsok preflight`: **PASS**; Python 3.14.3, UTF-8 stdout, 17 CV
  controls, 7 letter controls, 144 evidence entries, 6 employments and 4
  educations.
- `tools.prepare_masters --check`: **PASS**; zero property-order, font or forced
  page-break repairs remain; 17/7 control contracts preserved.
- Vertical slice with workdir and evidence output outside Build: **21 expected
  outcomes / 0 unexpected**, two DOCX outputs, render `DEGRADED`, **PASS**.
- Adversarial untouched-area regressions (`test_t09_t12`, `test_t13_t15`,
  `test_t16_t18`, `test_traceability`): **130 passed / 0 skipped / 0 failed**.
- Installed editable distribution metadata reports `jobbsok 0.9.1`.

### Public-command smoke by actual output

Synthetic run `r20260827-225044-dc49bc` ran from the real Build root whose path
contains `ø`.

- Actual `context` JSON was inspected for `STRATEGY`, `DRAFT`,
  `FINAL_AND_REVIEW` and `REVIEW_ONLY`. Every schema path existed inside that
  run's frozen schema copy; every return parent existed under
  `generated/returns`; context created neither a return file nor a canonical
  semantic artifact; every path and handoff was quoted; no angle placeholder
  remained. Pair and review-only used different handoff-scoped locations.
- All four emitted `submission.command` values were executed verbatim in
  PowerShell. Each returned 0 and wrote only its expected canonical artifact(s).
- Real public `finalize` returned 0 for `READY`, `CHECK` and `RERUN` after
  restoring the same unfinalized synthetic final each time. Every result wrote
  `finalization.state = FINALIZED` and `finalized_by = operator` with no
  `--reviewed-by` flag.
- A repeat `finalize` without `--date` returned 0 and printed the existing-date
  idempotent message.
- Public render returned 0 with both DOCX `OK` and both PDFs `DEGRADED`. The two
  failed conversions had `page_count = null` and `warnings = []`; no page
  warning printed. This is the specified failure behavior, not a page-warning
  defect. Status remained semantic `RERUN`, production `VALID`, render
  `DEGRADED`, proving the three axes remain separate.

The synthetic run and its run-specific generated state were moved intact to
external scratch after inspection. The retained historical run/view and all
retained evidence were preserved byte-for-byte.

## Final scope gate

Before this report changed, the pre-task registry contained 99 active files and
the current registry contained the same 99: **0 new, 0 missing, exactly 9
changed**. With this report, the patch is exactly the ten files listed above.

- zero new commands or parser branches;
- zero schema or schema-file edits;
- zero dependencies or runtime modules;
- zero manifest/status fields, state axes or authoritative artifacts;
- zero model/network clients, automatic retries, approval abstractions, numeric
  judges or hard page/count thresholds;
- zero edits to `P0.9/Architecture/`, `policy/settings.toml`,
  `stage2_package_writer.md` or `policy/writing/*`;
- `SPEC_REVISION = "0.9.0"`, `SCHEMA_REVISION = "0.9.0"`, manifest schema
  constants `0.9.0`, and `policy/settings.toml [spec].schema_revision = "0.9.0"`;
- exactly four version-line changes: `pyproject.toml`, `RUNBOOK.md`, Stage 1 and
  Stage 3, all `0.9.0` to `0.9.1`.

## Target Word attempt and remaining gate

Direct Word COM conversion failed before producing an automation instance; the
public render reported COM class-factory failure and returned the correct
degraded result. A separate attempt to launch Word through the interactive
Windows app-control surface was refused because Word use was not approved for
that surface. Therefore this execution context does not prove Word COM
activation, PDF conversion, PDF page counts, warning display/persistence for an
`OK` PDF, Norwegian glyphs in PDF, stable Word/PDF rerender, or the Word-scoped
ownership/timeout paths.

`GO_FOR_TWO_JOB_SMOKE` remains withheld until an unlocked interactive Windows
session runs the exact full suite with **250 passed / 0 skipped / 0 failed** and
observes the successful-PDF warning behavior. When that gate is green, the next
action is the two deliberately chosen real CORE vacancies; no further design
pass is warranted.

Semantic product quality is not proven by this patch or its engineering tests
(`INV-08`). The first two real jobs still own `READY` calibration, actual
employer-facing quality, handling time and page-warning usefulness; the later
representative cluster owns cross-job semantic carryover evidence. Before the
first real freeze, the human must populate `[stages.role_mapping]` and record
the account's retention/training posture (`GATE-10`).

## Bounded repair pass — two audited defects

Both reported defects were reproduced from a clean frozen run through the public
CLI before anything was changed.

### Defect 1 — superseded render receipt after a replacement Stage-3 final

**Reproduced.** After `stage-submit` committed a replacement Stage-3 final+review,
`status` reported `render_state.overall = FAILED`, `production_state = VALID`,
`semantic_final_available = true`, `output_paths = []`, and `status` exited 1.
The recorded limitation was `binding.document_date expected None observed
'2026-08-28'` — the replacement final is `DRAFT`, so no render can correspond to
it yet.

**Both representations were implemented and tested.** Representing a superseded
receipt as `NOT_RENDERED` was tried first. It works for the reported case, but it
cannot be made correct within this scope:

- `artifact_hash` deliberately excludes `finalization` (DEC-26 lists "final
  replaced" and "document date assigned/changed" as two separate rows), so a
  superseded binding and a fabricated binding have the identical shape;
- consequently the change also reclassified an unverifiable receipt, breaking
  four pre-existing assertions —
  `test_t09_semantic_final_is_not_inferred_from_a_render_file` ("a receipt
  without its current semantic final cannot remain current") and
  `test_t09_pdf_degradation_does_not_change_semantic_triage[READY|CHECK|RERUN]`
  ("an unverified synthetic receipt must not be presented as current"). Those
  assertions carry an explicit `ACC-05`/`DEC-42` rationale;
- separating the two would require output-existence and hash logic well beyond a
  bounded repair, and would weaken an integrity property to remove a transient
  exit code.

**Resolution: the existing status representation is correct.** The runtime is
unchanged and `policy/RUNBOOK.md` now recognizes the state. The interrupted-
cluster rule covers `NOT_RENDERED` **or** `FAILED`, explains that a `FAILED`
render usually means a superseded receipt that `finalize` + `render` repairs,
and states that `DEGRADED` is a completed render and not owed work. The status
section records that `status` exits non-zero while a job is in that state.

### Defect 2 — failed replacement hidden by an older valid downstream stage

**Reproduced exactly as reported.** With a complete valid chain, a refused
Stage-1 return produced:

```text
failure operation   : STAGE1        classification : FAILED
production_state    : FAILED        highest_valid_stage : FINAL
recommended_action  : Correct the reported mechanical defects once ...
next --stage 1      : Nothing outstanding for that selection.
next (no stage)     : Next job : testetaten_radgiver
```

A refused return never displaces the current artifact, so the stage ladder alone
reported nothing outstanding for the very stage whose correction the same run had
just recorded.

**Fixed** in `status.next_job` and `cli.cmd_next`. `cmd_next` reads the existing
current failure record for each manifest job and passes the ids whose record is a
`FAILED` attempt at the requested stage; `next_job` returns such a job before
consulting the stage ladder. After the fix `next --stage 1` returns the job while
`--stage 2` and `--stage 3` stay silent, and a successful replacement clears the
record and the queue falls silent again.

No new command, schema, status field, state axis, persistent state, dependency or
retry behaviour was introduced. `BLOCKED_MANUAL` is still skipped, so bounded
recovery and vacancy atomicity are unchanged.

### Materially changed files

| File | Change |
|---|---|
| `runtime/jobbsok/status.py` | `next_job` gains an optional `failed_at_stage` set and returns a matching job before the stage-ladder check |
| `runtime/jobbsok/cli.py` | `cmd_next` builds that set from existing failure records when `--stage` is given |
| `runtime/tests/test_t05_t08_ownership_schema_failure.py` | new `test_t08_failed_replacement_is_surfaced_by_its_own_stage_queue` |
| `policy/RUNBOOK.md` | continuation rule covers `FAILED`; render-axis and stage-queue notes |

`runtime/jobbsok/render.py`, all schemas, `policy/settings.toml`, the stage
instructions and `P0.9/Architecture/` are untouched.
`runtime/tests/test_t19_t23_render_security.py` was edited during the rejected
first approach and restored byte-for-byte (39,011 bytes).

### Verification after the repair

| Proof | Result |
|---|---|
| Focused defect-2 regression | 1 passed |
| Full deterministic suite | **251 passed / 0 skipped / 0 failed**, 245.86 s |
| Adversarial state/recovery (`t09_t12`, `t13_t15`, `t16_t18`, traceability) | 130 passed |
| `tools.prepare_masters --check` | PASS — 0 reorders, 0 font retargets, 0 page-break removals, control contract preserved |
| `tools.vertical_slice` | **PASS** — 21 steps, 0 unexpected, 4 outputs, `render overall : OK` |
| Word COM target path | Green — 0 skipped in the full suite |
| Final scope inspection | 4 source files changed; evidence artifacts regenerated by the slice |

251 = the 250-test post-P0.9.1 baseline plus the one new regression.

Semantic product quality remains unproven by any of this (`INV-08`).

## Pre-pilot closure — 2026-08-28

**Verdict:** `GO_FOR_TWO_JOB_PILOT`.

The two approved CORE vacancy sources, batch order/priority/deadlines, current
role mappings and GATE-10 account/privacy facts were independently checked.
`jobbsok preflight`, `jobbsok index verify` and the current intake/source checks
pass. Earlier `BLOCKED_USER` language above is superseded for the pilot-start
decision; real-job visual and semantic quality is the pilot evidence. No real
run was frozen by this closure check.

---

# P0.9.2 — final pilot-learned optimization pass

**Status: steps 0-6 complete; A1 is mechanically green; stopped at A1's two
human gates.**
Two halts happened and both are recorded below in the order they occurred: a
plan/repository conflict at step 2 (F1 versus Windows MAX_PATH), and a
pre-existing letter-render defect that A1 exposed. Both were reported with
evidence before being corrected under explicit authorisation, neither was worked
around. Vegard discharged the voice-file gate and the Word-open hard stop on
2026-09-02. Nothing is claimed as passed that was not run.

**22 final diffs** (21 tracked by the step-0 snapshot plus `docxfill.py`),
`generated/evidence_index.json` byte-identical, suite **257 / 0 / 0**, and Run A1
green on every mechanical criterion.

What remains is human: the B0-versus-A1 visual A/B, the cross-identity Word open
from `out/`, then Run B and the representative cluster.

## What landed

| File | Change | Step |
|---|---|---|
| `runtime/tests/conftest.py` | `import re`; new `set_role_mapping(layout, *, sol, terra)` helper | 1 (F2) |
| `runtime/tests/test_t05_t08_ownership_schema_failure.py` | `set_role_mapping` import; `test_t05_public_handoff_...` takes `layout` and calls `freeze` itself; `configured_model is None` -> `== "synthetic-sol"`; `test_t05_context_exposes_...` uses the helper | 1 (F2) |
| `runtime/jobbsok/render.py` | em dash -> period in the previous-employment line (D1); en dashes -> `\|` in the document title (D2); render workspace staged under `out_dir` (F1); `import tempfile` removed; **destination-aware output-name budget centralized in `render_output_paths`, with `verify_receipt` re-deriving canonical paths through it** | 2 |
| `runtime/jobbsok/atomicio.py` | `import secrets`; `TransactionDir` gains keyword-only `inherit_parent_permissions` (default `False`, so `cli.py` rollback stays private) | 2 (F1) |
| `runtime/tests/test_t19_t23_render_security.py` | new `test_t19_previous_employment_line_uses_plain_punctuation` (T4) and `test_t19_render_stages_beside_destination_with_inherited_permissions` (T5); **one output-path-length assertion added to the existing long-Norwegian-name test** | 2 |

| `policy/writing/WRITING_DOCTRINE.md` | A3 page-discipline paragraph; new `# Tegnsetting` section before `# Tjuesekunderstesten` | 3 |
| `policy/writing/PERSUASION_CALIBRATION.md` | C1 provenance-voice bullet plus the **generic** `riktig` / `for svakt` / `for sterkt` worked example, appended to `# TOO_WEAK` | 3 |
| `policy/writing/FORFATTERSTEMME.md` | **new file** (E1), nine sections, no `Motivasjonsregister` | 3 |
| `policy/stages/stage1_decision_architecture.md` | B1 + B3 + C2: field-to-section routing table, `evidence_plan[].role` framing, `structure_guidance` is not a template | 3 |
| `policy/stages/stage2_package_writer.md` | E2: the voice file added to `## Inputs` as a light prior | 3 |
| `policy/stages/stage3_final_writer_review.md` | B2 + C2 + E2: named-section list incl. `Tegnsetting`; **mission language cannot evidence the swap test**; independent thesis before reading upstream; voice governs expression only; repair duty made symmetric | 3 |
| `policy/RUNBOOK.md` | new `### After you review a package` step, then the pilot-log row instruction | 3 |
| `pyproject.toml` | version `0.9.1` -> `0.9.2` | 3 |

Thirteen files differ from the step-0 snapshot and one is new: **14 of the 21
expected final diffs**. Every step-4 and step-5 target is verified untouched -
`CV_BASELINE.md`, both `generated/*.json`, both masters, `prepare_masters.py`,
`leakage.py`, `test_t16_t18_containment_template.py` and `pilot/PILOT_LOG.csv`. `policy/`, `authorities/`,
`generated/`, `templates/`, `pyproject.toml` and `leakage.py` are untouched;
`policy/writing/FORFATTERSTEMME.md` does not exist yet.

## Step 0 - snapshot

`P0.9/Process/finalization_snapshots/pre_0.9.2/` created (did not previously
exist). `REGISTRY.sha256` holds 22 manifest rows, one recorded `ABSENT`
(`policy/writing/FORFATTERSTEMME.md`). `source_tree/` holds the 21 existing
targets plus the header-only `pilot/PILOT_LOG.csv`; every copy verified
byte-equal to its source. `b0/` holds the four pilot DOCX with their hashes.
The pilot run was read, never written; no ownership taken, no access forced.

## Step 1 - F2 (ISS-14). GATE MET.

- Full suite, canonical tree (mapping populated): **`251 passed in 262.14s`** -
  251 / 0 / 0, no skips, Word COM available this session.
- Blank starting state, disposable scratch copy outside the Build tree with
  `SOL_CLASS = ""` / `TERRA_CLASS = ""`: **`2 passed in 5.62s`**.
- Canonical `policy/settings.toml` sha256
  `2649eab7316dbf8c593c48adf175a96d4f5881237862177774d835fe6a2c2b4e` before and
  after; unchanged. The canonical file was never blanked. Scratch tree removed.
- Scope of the blank-state proof, stated rather than overclaimed: the two
  affected F2 tests, not the whole suite.

## Step 2 - D1, D2, F1, T4, T5. GATE FAILED.

Full suite after step 2: **`1 failed, 252 passed in 254.62s`**.

Failing: `test_t19_public_word_render_handles_realistic_long_norwegian_names`
-- `assert 'DEGRADED' == 'OK'`. This test passed in the step-1 run.

D1, D2, T4 and T5 are sound; the failure is attributable to one line.

### Confirmed conflict: F1 versus Windows MAX_PATH under Word COM

`MASTER_IMPLEMENTATION_PLAN.md` section 7.1 moves the render workspace from
`%TEMP%` to `out_dir`, noting only that `.rnd.<8 hex>` is short and that the
longest current output path is about 200 characters. That premise holds for the
retained pilot run. It does not hold for a realistic long Norwegian employer
plus title, which the suite already tests.

Measured evidence:

| Observation | Value |
|---|---|
| Failing test `out` directory | 133 chars |
| Rendered filename | 134 chars |
| Word-visible **staged** path after F1 | **282 chars** |
| Word COM diagnostic | `You cannot call a method on a null-valued expression` / `Word COM export returned exit code 1` (both PDFs) |
| Both DOCX in the same run | `OK` - only the PDF step fails |

Isolated boundary probe, converting the same DOCX at three path lengths with
`pdf.convert(converter="word_com")`:

```
docx path len=180  ok=True   exit=0
docx path len=255  ok=True   exit=0
docx path len=265  ok=False  exit=1   <- same null-valued-expression diagnostic
```

Attribution: a scratch copy carrying D1, D2, T4, T5 and the `atomicio`
parameter, with **only** the `render.py` staging location reverted to
`%TEMP%`, passes the test (`1 passed in 9.44s`).

Mechanism: before F1, Word opened the staged DOCX at a short `%TEMP%` path
(about 53 chars plus filename) and the long destination path was only ever
touched by Python, which handles >260. After F1 Word must open the file at the
destination depth plus the 14-character `\.rnd.<8 hex>` segment, and Word is
bound by `MAX_PATH` = 260 where Python is not.

Production reach, not only a test artifact: the canonical `out` directory is
129-130 chars, so after F1 the Word-visible staged path exceeds 260 once the
output filename passes about 115 characters. The pilot's longest is 68, so the
pilot is unaffected; the tested `Nordre Follo kommune ...` name is 134 and is
not unrealistic for this candidate's market. `GATE-07` and Contract 17.2 make
long Windows paths an explicit obligation, and this test is where that
obligation is exercised.

No trivial tweak rescues it: dropping the `rnd` prefix entirely saves 4
characters against a 22-character overrun.

**Halted here rather than adapted.** Choosing between the available directions
is design authority this pass does not hold. Recorded for decision, with the
change set left exactly as the plan specifies so the evidence is reproducible.

## Step 2, resumed - destination-aware output-name compaction. GATE MET.

Directed correction: keep F1's inheriting `TransactionDir` under `out_dir`, and
make the output *filename* destination-aware. Not `%TEMP%` staging, and not a
rejection-only cap.

`render_output_paths` becomes the single producer of output names and budgets
them against the **staged** path, which is the longer of the two:

```
staged   = destination / ".rnd.<8 hex>" / filename     <- what Word opens
promoted = destination / filename                      <- what the human opens
budget   = MAX_PATH_CHARS - len(resolved destination) - 15
```

The 15 is derived from `RENDER_STAGING_PREFIX = "rnd"`, which is then passed to
the `TransactionDir(...)` call, so the budget and the real staging segment
cannot drift apart. Budgeting the staged path covers the promoted path by
construction, exactly 15 characters shorter.

- A filename is **preserved byte-for-byte** whenever it fits.
- Otherwise the employer/title suffix is truncated to the remaining room and
  `_<8 hex>` is appended, where the digest is
  `sha256_canonical_json({job_id, employer, title})` over the complete
  untruncated identity, so employers that ASCII-fold together stay distinct.
  The employer component leads the suffix, so a meaningful employer prefix
  survives truncation by construction.
- If the room left for a name is under `MIN_EMPLOYER_PREFIX_CHARS = 8`,
  `render_output_paths` raises `ConfigurationError` before anything is written,
  naming the destination, the budget and the minimum needed. Minimum name is 29
  characters, so a destination deeper than 196 refuses.

Consistency: `render_job` stages and promotes through it; **`verify_receipt` no
longer rebuilds the filename by hand** and re-derives the canonical paths through
it (without this, a compacted render would fail receipt verification and
`status` would report it as not-current); the no-clobber lookup keys on the name
recorded in the previous report, which stays correct because a run/job's
canonical `out_dir` never changes; `cli.py` already called the same function.

### Verification - six checks, each actually run

| # | Check | Result |
|---|---|---|
| 1 | Long-Norwegian-name test: four outputs, verified PDFs | **`1 passed in 8.99s`**; `render_state OK`; cv/pdf `OK` 2 pages, letter/pdf `OK` 1 page; four files present, 37-292 KB |
| 2 | Every absolute output path <= 240 | longest promoted **226**; asserted in-test against `MAX_PATH_CHARS` |
| 3 | Word COM reopens a **promoted final** DOCX | probe on the 222-character promoted CV: **`ok = True, exit = 0`**, 292 496-byte PDF produced. The fix covers the human-visible final path, not only staging |
| 4 | Normal-length pilot/fixture names unchanged | all four pilot DOCX names recomputed by the new code **MATCH** the files on disk (185-198 chars); the standard fixture names are identical to the vertical-slice artifacts already on disk |
| 5 | T5 green, inheriting staging beside `out_dir` | passed in the full run and by name |
| 6 | Full suite | **`253 passed in 223.05s`** - 253 / 0 / 0, no skips, Word COM available |

Named confirmation of the three affected tests together:
`3 passed, 40 deselected in 10.96s`.

Compacted names produced for the long identity (digest `e11d2ef6`):

```
CV_Nordre_Follo_kommune_Virksomhet_for_okonomistyring_og_analyse_Senio_e11d2ef6.docx
Soknad_Nordre_Follo_kommune_Virksomhet_for_okonomistyring_og_analyse_Senio_e11d2ef6.docx
```

The existing `startswith("CV_Nordre_Follo_kommune")` and
`startswith("Soknad_Nordre_Follo_kommune")` assertions still hold.

### Consequences recorded rather than glossed

- A compacted name is **destination-dependent**, so a `--dest` export of such a
  job gets a different filename than its canonical output. Harmless here:
  `--dest` is a non-authoritative export, it does not update the report, and the
  no-clobber lookup is canonical-only. But `RUNBOOK.md`'s "four deterministic
  matching export filenames" line is true only within one destination.
- A run rendered *before* this change whose name would now compact would leave
  its old file orphaned in `out/`. No live case exists: every pilot name is
  63-67 characters and compacts for nobody, so no migration is built.
- Scope unchanged: no new file, test, dependency, command, flag, schema field,
  runtime module or state axis. Two files already inside the change surface, two
  module-level constants and one private helper in `render.py`, reusing
  `paths.MAX_PATH_CHARS`, `paths.safe_filename_component` and
  `hashing.sha256_canonical_json`.

### Deviation recorded

T4 asserts **em dash only**, per `MASTER_VERIFICATION_AND_ACCEPTANCE.md` section
2.4 ("no em dash"), not "no em or en dash" as the execution plan's step-2 text
said. The en dashes on those lines come from `CV_BASELINE` period ranges, which
D3 fixes at step 4 and T3 guards at step 5; asserting them at step 2 would fail
the gate on work that has not landed. T4's non-vacuity was proved separately: the
same extraction against the retained pilot CVs finds the heading and all four
lines, and every one of them carried the em dash that D1 removes.

## Step 3 - policy, versions and the voice file. WORK DONE; GATE IS HUMAN.

All Norwegian transcribed character-for-character, `> ` blockquote formatting
preserved, LF endings, no BOM, verified after writing.

Outcome B adds **no doctrine text**, as reconciled. Verified by section-level
comparison against the step-0 snapshot: `Begrunnet motivasjon`,
`Arbeidsgiverbyttetesten`, `Rolig faglig tyngde` and `Single Backbone og
strategisk asymmetri` are all byte-unchanged. B is carried entirely by the
Stage-1 routing table and the one Stage-3 sentence.

The C1 example is **generic** and carries all three boundaries (`riktig`,
`for svakt`, `for sterkt`); checked to contain no `2,5`, no `gevinstrealisering`,
no `sykehus`, no `OUS`. The concrete `PRJ-04` instance lives in the Run B
acceptance criteria and in this report, as a check rather than a template:
the pilot understatement to repair is
`var rapportert i bruk om lag 2,5 år senere`, present in **both** pilot finals.

`FORFATTERSTEMME.md` carries **no `§ Motivasjonsregister`** (ledger 7.1
reversal), verified by search. It needs no schema, code or manifest change:
`manifest.py` globs `policy/writing/*.md` into an unbounded `writing_policy`
array, and frozen inputs are verified per recorded entry inside each run's own
`frozen/` copy, so existing runs cannot break.

### RUNBOOK placement - deviation from the plan's stated anchor, with reason

`MASTER_IMPLEMENTATION_PLAN.md` section 4.4 asks for the pilot-log row "in the
per-vacancy loop, immediately after the human reviews the rendered package."
**No such operation exists in the RUNBOOK**, and one cannot be created there:
the per-vacancy loop closes with *"then continue to the next vacancy **without a
human checkpoint**"*, which is frozen behaviour (Spec 6.3, `DEC-12`). Writing the
row inside that loop would have encoded row-before-review *and* contradicted the
architecture.

Placed instead as one new human step at the end of `## Finalizing and rendering`,
beside the two existing human-facing post-render subsections and outside the
loop, establishing review -> handling decision -> row in that order. The row
paragraph itself is the plan's text verbatim. The review step names **both DOCX
plus whichever current PDFs exist**, and states that a missing or degraded PDF
never blocks review (`DEC-41`) - requiring "four files" would have made a
degraded render block semantic review. Verified: the loop still reads "without a
human checkpoint".

### Verification

- Full suite after step 3: **`253 passed in 227.28s`** - 253 / 0 / 0, no skips.
  This also proves that adding a third file to `policy/writing/` does not disturb
  the frozen-input machinery, since `conftest` copies the real `policy/` tree into
  every build root and freeze globs that directory.
- Six control-plane files plus `pyproject.toml` at `0.9.2`; `FORFATTERSTEMME.md`
  ships at `0.9.2`. `SPEC_REVISION`, `SCHEMA_REVISION`, the `manifest.schema.json`
  consts and `settings.toml [spec]` all remain `0.9.0`.
- `CV_BASELINE.md` is **not** version-bumped: it has no `version:` key, it sits in
  `authorities/` which Contract 3 classes as protected data plane rather than
  control plane, and its `baseline_version` also flows into `baseline_map.json`.

### Flagged: the version marker outruns the change set

`pyproject.toml` now reads `0.9.2` while 14 of 21 diffs have landed, because plan
section 8 places version bumps in step 3. Stated here rather than moved, since
moving it is not this pass's authority.

## Step 4 - D3 and the generated maps. GATE MET.

Sixteen edits inside the fenced JSON of `authorities/CV_BASELINE.md`, each
anchored on both its line number **and** its exact expected fragment, applied
only after all sixteen validated. Two unit names take a **comma**
(`Direktørens stab, Analyseavdelingen`, `Barne- og ungdomsklinikken, Stab`),
because a hyphen there would itself be the clause-dividing hyphen outcome D
prohibits; the thirteen ranges take a plain hyphen.

The four `authority_anchor` values on lines 88, 102, 116 and 130 are asserted
unchanged and still carry their en dashes: they are inert, never rendered, and
two are verbatim cross-references into `Work_experience.md`. After the edit the
file holds **exactly 4 en dashes and 0 em dashes** - those four.

`CV_BASELINE.md` is deliberately not version-bumped: it has no `version:` key,
it sits in `authorities/` which Contract 3 classes as protected data plane, and
its `baseline_version` also flows into `baseline_map.json`.

| Command | Result |
|---|---|
| `jobbsok index build` | `evidence_index.json : 144 entries` / `baseline_map.json : 6 employments`, exit 0 |
| `jobbsok index verify` | **`Index verify PASS`**, exit 0 |
| `evidence_index.json` | **byte-identical**, `16d5206a9dc34786` before and after - it is built only from the three authority files, which D3 does not touch |
| `baseline_map.json` | regenerated; dash-bearing values now **4, all `baseline_provenance`** (was 20, of which 16 rendered) |

**The D3/D4 coupling demonstrated rather than asserted.** With D3 landed and D4
not yet, `jobbsok preflight` failed with exactly **8 errors**, one per
dash-bearing `static_baseline_assertion`, each naming the master text that no
longer matches the baseline. That is the predicted count exactly, and it is why
the two must land together.

## Step 5 - A1, A2, D4 through one prepare_masters write. GATE IS HUMAN.

The transform is position-keyed, never value-keyed. A value map would not even
be correct once: the same current value maps to two different targets (20 -> 28
for headings but -> 24 for the role line; 18 -> 24 for body zones but -> 20 for
subordinate ones; 19 -> 24 for record titles but -> 20 for the two content
zones). Anchors are SDT tags for the 24 controls and transform-invariant
visible-text substrings for the static furniture, each verified unique, each
stopping short of the dash the same pass rewrites.

Guarantees built in rather than hoped for:

- **Total coverage.** The resolved paragraph indices must equal the full body
  set exactly once each, and the number of `w:sz` elements the table visits must
  equal the number present. A missed or double-claimed paragraph is a refusal,
  not a wrong binary.
- **No insertion.** Only `w:val` is rewritten and two elements are removed, so
  ECMA-376 child order cannot move; `reorder_properties` is re-run afterwards
  and must return 0.
- **Validate before mutate.** Every pass queues its mutations and nothing is
  applied until all of them validate, so a refusal leaves the parsed tree
  untouched.
- **Pair atomicity.** `main()` stages and validates both masters, then promotes
  both or neither.
- `w:szCs` is never read, written or created; `stylesWithEffects.xml`,
  `docDefaults`, every unapplied style and both headers/footers are untouched.

### Write, then check - the counters matched the predictions exactly

| | CV | Letter |
|---|---|---|
| typography normalizations | **48** (41 run sizes + 3 styles + 4 removed elements) | **8** (7 run sizes + 1 style) |
| dash normalizations | **8** | **1** |
| control contract | **preserved, 17 controls** | **preserved, 7 controls** |

A following `--check` reported **0 / 0 / 0 / 0 / 0** for all five counters on
both masters, exit 0. That is a real idempotence proof because the first run
actually wrote; two dry runs would prove nothing.

### Measured result in the regenerated masters

| | CV | Letter |
|---|---|---|
| inline `w:sz` (half-points) | `{48: 1, 28: 10, 24: 12, 20: 18}` = 41 runs | `{20: 7}` |
| all within `{16, 20, 24, 28, 48}` | yes | yes |
| `w:szCs` in `document.xml` | 0 | 0 |
| en / em dashes | 0 / 0 | 0 / 0 |
| applied styles | `Normal` 24, `ListBullet` 24, `Heading1` 28 | `Normal` 24, **`Title` 40 retained** |

`jobbsok preflight`: **`Preflight PASS`**, exit 0 - the 8 errors are gone, so D3
and D4 agree.

`runtime/jobbsok/leakage.py:98` `KNOWN_GOOD_PHRASES` updated to
`"Direktørens stab, Analyseavdelingen"` to mirror the baseline. No test failed
without it, because leakage does not inspect punctuation; it was found by the
scope-gate diff count, not by the suite.

### The three new tests, and proof they are not vacuous

T1 `test_t16_master_typography_uses_the_discrete_scale` (inline sizes **and**
every applied style, with `Title = 40` asserted as a named exception rather than
ignored), T2 `test_t16_subordinate_zones_are_not_title_formatted`, T3
`test_t16_masters_and_baseline_contain_no_en_or_em_dash`. They carry the
`test_t16_` prefix because `MASTER_VERIFICATION_AND_ACCEPTANCE.md` section 2.4
names them so; the traceability registry maps by prefix, so both items stay
satisfied. Observation only, no deviation.

Each assertion was replayed against the **step-0 snapshot** masters and baseline
and would have failed there:

```
CV     inline sizes off-scale : ['17','18','19','49']
CV     applied styles         : Normal 18/24, ListBullet 18/24, Heading1 20/28
CV     dashes                 : 8 en
Letter inline sizes off-scale : ['17']      applied: Normal 21/24
Letter dashes                 : 1 en
T2     both zones             : b=True, color=17324D
T3     old baseline map       : 16 non-provenance dash values
```

### Suite and scope

- Full suite: **`256 passed in 229.72s`** - 256 / 0 / 0, no skips, Word COM
  available. That is the plan's post-implementation target reached exactly.
- **21 final diffs**, one new file, `generated/evidence_index.json`
  byte-identical, `pilot/PILOT_LOG.csv` untouched.
- Must-not-change verified against the pilot manifest's own frozen hashes: **17
  of 26 frozen inputs still match byte-for-byte**, and the 9 that differ are
  exactly this pass's targets. `settings.toml`, `template_map.json`,
  `PERSONALITY_PROFILE.md`, `personality_facets.json`, the three authority files
  and every schema are untouched.
- The archived P0.7 originals under `evidence/gates/GATE-02/original_p07_masters/`
  are unchanged, and no `*.prepared.docx` was left behind.

### Word: supporting evidence only, the gate is still owed

Word COM opened and exported both regenerated masters (`ok=True, exit=0`;
267 321-byte and 181 400-byte PDFs), and the ten Word-COM tests in the suite
convert documents generated from them.

**This does not discharge the hard stop.** The converter runs with
`DisplayAlerts = 0`, and Word's own open-and-repair is exactly what masked the
P0.7 defect: those masters *did* open, after silent repair, while a human saw a
repair prompt. A clean COM export is consistent with a file Word would still
complain about interactively. The gate needs a human opening both files in Word
and seeing no repair prompt.

## Step 6 - Run A1. HALTED on a pre-existing defect A1 was built to expose.

Hard stop 2 was discharged by Vegard on 2026-09-02: both regenerated masters
open in Word with no repair prompt. Vegard then attested the
baseline-to-authorities reconciliation, so `freeze --reviewed-by` was run with
his explicit authorisation, not on inference.

Run `r20260902-155301-2120b3`, cluster `verify_a1`, the same two vacancies.
The reconciliation passed on its own terms: `CV_BASELINE.md`'s recorded
derivation hashes still match all three live authorities, because D3 changed
punctuation only and touched neither the table nor the authority files.

Replay per plan section 9.2: fresh `context` per job per stage, the pilot
artifact projected minus exactly `artifacts.MECHANICAL_FIELDS`, and the emitted
`submission.command` executed verbatim. **No model calls.** Every stage
committed at exit 0; the stripped keys matched the contract exactly
(strategy 6, draft 3, final 4, review 2), and no non-semantic key survived.

### What A1 proves - the deterministic half, on real pilot content

| Check | Result |
|---|---|
| CV page count | **2 pages**, both jobs - the A1 typography target |
| Page warning | none |
| Extracted text, every produced document | **zero en dashes, zero em dashes** |
| Residual SDT / placeholder | 0 / none, all four DOCX |
| Both DOCX per job | `OK` |
| CV PDF | `OK`, both jobs |

Outcome A and the deterministic half of outcome D are therefore demonstrated on
the real employer-facing documents, not on a fixture.

### ISS-13 closed on a real promoted file

`icacls` on the A1 CV, compared with the pilot's:

```
A1    ... VHAALA\veggi:(I)(F)   -- every ACE inherited, no protected descriptor
PILOT ... Access is denied.     -- veggi cannot even read the ACL
```

That is MVA section 4.2 check 1, discharged with direct before/after evidence.
Check 2, a human opening both DOCX straight from `out/` in Word, remains human -
though this session read both files from `out/` as `vhaala\veggi` with no copy
step, which the pilot outputs still refuse.

### The halt: letter PDF DEGRADED - pre-existing, outside this change surface

Both jobs render `render_state.overall = DEGRADED`, because the letter PDF fails
Word conversion with `The file appears to be corrupted.` MVA section 3.4
requires `render overall : OK`, so A1 cannot be accepted as it stands.

**This pass did not cause it.** Controlled comparison:

| Document | Master | Word conversion |
|---|---|---|
| A1 letter | new | **fails** - "file appears to be corrupted" |
| **B0 letter** | **old, pre-change** | **fails identically** |
| A1 CV | new | succeeds, 2 pages |

The pilot's own render was `DEGRADED` too, but for an unrelated reason -
`Retrieving the COM class ...`, a Word-COM-unavailable session fact. That outage
**masked** this defect. A1 is the first time Word has actually been available to
attempt the pilot letter.

**Root cause, precisely.** The letter master's fourth table cell contains
`tcPr` plus the `APP_REFERENCE_OPTIONAL` block control and no direct `w:p`.
When a job has no reference, `fill_block(root, tag, [])` empties the control and
`unwrap_content_controls` then removes the `w:sdt`, leaving the cell holding
**only `tcPr`**. ECMA-376 requires a `w:tc` to contain at least one block-level
element; Word rejects the file as corrupt. Measured:

```
A1 letter  (huseierne, no reference)  cells=4  EMPTY_CELLS=1  [['tcPr']]
A1 letter  (avinor,    no reference)  cells=4  EMPTY_CELLS=1  [['tcPr']]
B0 letter  (old master, no reference) cells=4  EMPTY_CELLS=1  [['tcPr']]
master     APPLICATION_MASTER.docx    cells=4  EMPTY_CELLS=1  [['tcPr','sdt']]
vertical-slice letter (reference set) cells=4  EMPTY_CELLS=0  []
```

**Why no test caught it.** The vertical-slice and suite fixtures set
`reference = 2026/1234`, so the cell keeps a paragraph and converts cleanly -
which is why the suite is a genuine 256 / 0 / 0 with the new masters.
ElementTree parses the empty cell happily, and `_verify_docx` checks text,
identity and SDT residue, not cell well-formedness. Both real pilot jobs have no
reference, which is ordinary for Norwegian vacancies.

### The fix, authorised 2026-09-02 - bounded to the broken invariant

Vegard authorised the repair explicitly, so `runtime/jobbsok/docxfill.py` leaves
the *Must not change* list for this one change. Scope kept to the invariant that
was actually violated:

- one function, `repair_empty_table_cells(root)`, which gives back a `w:p` to any
  `w:tc` left with no block-level child;
- one call site, in `write_filled_docx`, between `unwrap_content_controls` and
  `assert_no_controls` - unwrapping is what can empty a cell;
- nothing else touched. `fill_block` keeps its meaning, so an emptied control
  still renders as absent rather than as a blank line anywhere outside a table
  cell. The CV master has no tables, so the repair is provably a no-op there.

Rejected as too broad: making `fill_block` leave a placeholder paragraph
whenever `items` is empty. That would put spurious blank paragraphs into the six
`source: none` CV zones, a visible regression, to fix a table-cell problem.

**Regression test:** `test_t18_cleared_control_in_a_table_cell_leaves_a_valid_cell`
fills the real letter master with `APP_REFERENCE_OPTIONAL` cleared and asserts
every cell keeps a block-level child, and that the cleared control still renders
as absent. Proven non-vacuous by neutralising the repair:

```
WITH the fix      empty cells = 0  []           -> PASS
WITHOUT the fix   empty cells = 1  [['tcPr']]   -> FAIL
```

**Authorised scope change, recorded rather than absorbed:** new tests 5 -> **6**,
edited runtime modules 4 -> **5** (`docxfill.py` added), expected final diffs
21 -> **22**. Every other budget line is unchanged.

**Rollback gap, stated plainly.** `docxfill.py` was never one of the 22 manifest
paths, so the step-0 snapshot holds no copy of it and cannot restore it. The
change is small and fully reversible by description: delete
`repair_empty_table_cells` and the single call to it in `write_filled_docx`.
Nothing else in that module was touched.

### A1 re-rendered: GREEN

Both jobs `[OK]` - `CV: OK/OK  letter: OK/OK`, four documents each, the letter
PDFs `CREATED` and the rest `REPLACED` under the ordinary no-clobber path.

| MVA 3.4 check | Result |
|---|---|
| CV page count | **2**, both jobs |
| Letter page count | **1**, both jobs |
| Page warning | none |
| Extracted text, **all four documents per job** | **zero en dashes, zero em dashes** |
| `render_state.overall` | **OK**, both jobs |
| Parseability (`GATE-06`, `DEC-39`) | identity, phone and email extractable from all four PDFs; reading order intact |
| Residual SDT / placeholder | 0 / none |

ISS-13 check 1 on all four promoted files of a job:
`protected=False`, with an inherited `VHAALA\veggi` ACE on each. The pilot's
equivalents still answer `Access is denied` to `veggi`.

Full suite after the fix: **`257 passed in 237.91s`** - 257 / 0 / 0, no skips.

## Owed

**The stop — the two A1 human gates.** Nothing mechanical remains in A1.

1. **The B0-versus-A1 visual A/B** (MVA 4.1) - body legibility, hierarchy
   name > headings > body and record titles > subordinate detail, CV page 2
   meaningfully populated, TIDLIGERE ERFARING clearly subordinate, no orphan or
   widow, the letter's address block reading as metadata. This discharges
   `VISUAL_HUMAN` / `ACC-18` on real content, which it never has been. Guard the
   other way too: if 12 pt at `w:line="252"` reads cramped, that is the trigger
   for the single canonical `w:line` adjustment held in reserve under A5.
2. **ISS-13 check 2** - open both DOCX in Word straight from
   `runs/r20260902-155301-2120b3/jobs/<job>/out/`, no copy step. Check 1 is
   already discharged above.

Then step 7's remaining artifacts - the adversarial set, the vertical slice and
the closing scope gate. Then Run B, the blind voice A/B, the two hand-written
pilot-log rows, and the representative cluster.

`evidence/finalization/HASHES.sha256` is now stale for `BUILDER_REPORT.md`,
`policy/RUNBOOK.md`, `pyproject.toml`, `runtime/jobbsok/render.py`,
`runtime/tools/prepare_masters.py` and both masters. It records no entry for
`docxfill.py`. It is outside the declared change surface and was deliberately
not regenerated. `evidence/gates/GATE_REPORTS.md` describes the `--check` output
without the two new counters; also left, also recorded.

No human, cross-identity, Word-open, semantic-model or cluster gate is claimed by
anything recorded above.

Semantic product quality remains unproven by any of this (`INV-08`).
