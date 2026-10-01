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
