---
document: Jobbsøk_26 P0.9 operator runbook
version: 0.9.1
artifact_role: CONTROL_PLANE
---

# Operator runbook

You initiate every semantic stage yourself. Deterministic code prepares
context, validates artifacts, renders documents and derives status. It never
calls a model and never advances a stage on its own.

All commands run from `P0.9/Build`.

## Once per machine

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

Then check the environment and the masters:

```powershell
.\.venv\Scripts\jobbsok.exe preflight
```

Preflight must print `Preflight PASS` before you freeze anything. It checks
the baseline, the evidence index, both Word masters' control contracts, and
that the masters' static furniture still agrees with `CV_BASELINE.md`.

## Starting a batch

1. Put each vacancy file in `inbox/vacancies/` (`.pdf`, `.md` or `.txt`).
2. Fill in `inbox/batch_input.csv` — one row per approved opportunity.
   `.\.venv\Scripts\jobbsok.exe init-input` writes an empty one with the
   right columns.
   - `job_class` is `CORE` or `EXCEPTION`. An exception needs a reason and
     never blocks a core job.
   - There is no language column. Non-Bokmål vacancies are `EXCEPTION`.
3. Before freezing, fill in `[stages.role_mapping]` in
   `policy/settings.toml` with the model and surface actually used for each
   role, and record the account's retention and training posture (`GATE-10`).
   Freeze snapshots this mapping into the manifest; it cannot be changed in
   place afterwards.
4. Freeze:

```powershell
.\.venv\Scripts\jobbsok.exe freeze --input inbox/batch_input.csv --reviewed-by "Vegard Håland"
```

`--reviewed-by` records that **you** reviewed `CV_BASELINE.md` against the
three authority files. If an authority changed since the baseline was
derived, freeze refuses until you re-review and update the recorded hash in
`CV_BASELINE.md`. That is deliberate: the CV's static chronology is rendered
from the baseline, and a silent disagreement would ship as fact.

Freeze prints the `run_id`. Everything afterwards takes `--run <run_id>`.

## Running the three stages

One human instruction initiates one **stage × cluster** Codex task. Codex then
processes vacancies sequentially and vacancy-atomically from current disk
state, without routine between-job confirmation. The human still initiates
each semantic stage; deterministic code never calls a model or advances a
semantic stage on its own.

For each vacancy in Stages 1 and 2:

1. Run `next --run <run_id> --stage <stage> --cluster <cluster>`.
2. Run `context` for that exact run, job and stage.
3. Reset to the bundle's job identity and vacancy. Remembered position in the
   task is never authority.
4. Read exactly what `read` names. Write only `write.allowed`, using
   `write.schema_paths` for nested shape and `write.return_paths` for the
   semantic return files. Never include `write.tool_owned_fields`.
5. Execute `submission.command` **verbatim**. Do not reconstruct it or omit
   the handoff path.
6. If submission is refused, follow the printed `Recovery` next action once.
7. Advance only after a successful commit or an explicit job-local stop.

Stage 3 uses the same vacancy loop. Stage 1 and Stage 2 each submit one file.
Normal Stage 3 mode,
`FINAL_AND_REVIEW`, submits final and review together. If a valid final exists
without a current review, `context` returns `REVIEW_ONLY`; the final is not
regenerated. `context` refuses an `EXCEPTION` or `BLOCKED_MANUAL` job locally;
skip it and continue with independent peers.

After every successful Stage-3 submission, immediately run:

```powershell
.\.venv\Scripts\jobbsok.exe finalize --run <run_id> --job <job_id>
.\.venv\Scripts\jobbsok.exe render   --run <run_id> --job <job_id>
```

Do this for `READY`, `CHECK` and `RERUN` alike, then continue to the next
vacancy without a human checkpoint. Frozen P0.9 mandates human approval before
submission or irreversible external action, permits deterministic rendering,
and requires cluster-stage work without routine between-job confirmation. It
permits but does not require rendering every valid Stage-3 result. P0.9.1
selects render-all-valid as its operating policy because rendering is
reversible and produces the files the human must review.

## Continuing an interrupted cluster

Do not try to reconstruct where you were from chat history — it is never
authoritative. First ask the disk for one complete status snapshot:

```powershell
.\.venv\Scripts\jobbsok.exe status --run <run_id> --json
```

Before requesting more semantic work, complete internal production for every
job where `semantic_final_available` is true, `semantic_triage` is non-null and
`render_state.overall` is `NOT_RENDERED` **or** `FAILED`: run `finalize` and
then `render`. `finalize` is idempotent without `--date`, so this is safe
whether or not the job was already finalized.

A `FAILED` render here is usually not a broken render. Replacing a Stage-3
final supersedes the receipt that described the previous one, so no current
render exists yet and the same two commands repair it. Leave `DEGRADED` alone:
that is a completed render whose PDF needs a manual export, not owed work.

Then run `next` and generate fresh `context` for the selected job. Never reuse
an old handoff or submission command.

## Finalizing and rendering

`finalize` is internal document-production finalization: it confirms a current
valid final and review, assigns or preserves the canonical document date,
records the operator and enables rendering. It is not human semantic approval
and authorizes no external action. Run it without `--reviewed-by`; the human's
real name belongs only on `freeze` and `branch`.

```powershell
.\.venv\Scripts\jobbsok.exe finalize --run <run_id> --job <job_id>
.\.venv\Scripts\jobbsok.exe render   --run <run_id> --job <job_id>
```

A later pure rerender keeps that date. Pass `--date` only when you have made
a semantic change that genuinely warrants a new one.

Render produces four files per job in `runs/<run_id>/jobs/<job_id>/out/`:
CV DOCX + PDF and letter DOCX + PDF.

Page-target warnings are advisory. They print in the `render` output and are
stored in `render_report.json`; they do not change triage, render state or exit
code, and they are not present in `status --json`. A warning exists only when
PDF conversion succeeds and supplies a page count. If conversion fails and
render is `DEGRADED`, no page warning is produced; that is expected.

### If a PDF fails

Both DOCX files are the conforming result. A failed or missing PDF shows as
render `DEGRADED`, never as a semantic problem, and the queue tells you to:

> Save/export the PDF manually for human submission use. Automated status
> remains DEGRADED unless the configured converter later produces a verified
> current PDF.

### If you edited a delivered file by hand

A rerender will refuse to overwrite it and will say so. Either:

- `--force` to replace it with a fresh render, or
- `--dest <dir>` to write the new render somewhere else and keep yours.

Your edited file is never destroyed silently.

An explicit `--dest` is a non-authoritative export. Repeating it replaces the
four deterministic matching export filenames in that directory; keep edited
submission copies under different names or elsewhere. It never changes the
canonical receipt, status or history.

## Seeing where everything stands

```powershell
.\.venv\Scripts\jobbsok.exe status --run <run_id>
```

Three independent axes, never collapsed:

- **triage** — `READY`, `CHECK`, `RERUN`, or blank before a final and review
  exist. `RERUN` is advice, not an action: you decide which ordinary stage to
  restart.
- **production** — `NOT_STARTED`, `VALID`, `FAILED`, `STALE`,
  `BLOCKED_MANUAL`, `EXCEPTION`.
- **render** — `NOT_RENDERED`, `OK`, `DEGRADED`, `FAILED`.

`READY` with a degraded PDF is a normal, valid combination.

Render `FAILED` covers both a genuinely broken render and a receipt whose
semantic final has been superseded — the ordinary state immediately after a
Stage-3 rerun, before the new final is finalized and rendered. `status` exits
non-zero while any job is in that state; `finalize` and `render` clears it.

A stage-scoped `next` also surfaces a job whose current failure record is a
failed attempt at that same stage, even when older downstream artifacts are
still valid. That is the recorded correction, not a new queue entry.

The status view and queue are disposable. Never edit them; regenerate them.
Build the end-of-cluster summary from one `status --run <run_id> --json` call,
not from task memory. Report page warnings separately from the `render` output
seen in the vacancy loop; they remain durable in each `render_report.json`.

## When something says run-integrity failure

A file the run froze no longer matches its recorded hash. The run is not
stale — it is compromised. Either restore the frozen bytes, or:

```powershell
.\.venv\Scripts\jobbsok.exe branch --run <old_run_id> --reviewed-by "Vegard Håland"
```

Branching creates a child run and leaves the parent untouched. Artifacts
whose governing inputs are unchanged are carried over and rebound; anything
else must be regenerated by its owning stage, and the command tells you
which is which. There is no way to amend a frozen run, by design.

## When a job gets stuck

If the bounded recovery path is exhausted the job becomes `BLOCKED_MANUAL`
and other jobs keep going. The record carries the diagnostic, the last
successful stage, attempts used and a recommended next action. Restart an
ordinary stage manually, or drop the job — both are your call.

A repeated Stage-3 result from `next` is bounded recovery, not a stuck loop:
one same-handoff mechanical correction, then the configured fresh Stage-3
semantic attempt, then one correction for that attempt. If it still fails,
the job becomes `BLOCKED_MANUAL`; `context` refuses it and `next` skips it.

## Before the first real batch

- Run two real jobs end to end before processing a whole cluster.
- Keep your quality scores in `pilot/PILOT_LOG.csv`. Nothing in the runtime
  reads that file, and nothing ever will.

## What this system will never do

It will not contact an employer, submit an application, upload anything, or
take any irreversible external action. It has no network capability at all.
Every submission is yours to make by hand.
