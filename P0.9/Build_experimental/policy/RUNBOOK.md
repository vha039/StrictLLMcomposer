---
document: Jobbsøk_26 Relay operator runbook (experimental)
version: 0.10.0-exp
artifact_role: CONTROL_PLANE
---

# Operator runbook

Four human-started stages. You start each one; deterministic code prepares
context, validates returns, assembles the package, renders and derives status.
It never calls a model and never advances a stage on its own.

All commands run from `P0.9/Build_experimental` with `.\.venv\Scripts\jobbsok.exe`.

```
Stage 0 SCOUT      -> scout.json                 vacancy facts + evidence triage
Stage 1 ARCHITECT  -> brief.json, cv_draft.json  positioning + the CV layer
Stage 2 ADVOCATE   -> advocacy_draft.json        the letter (or the CV argument)
Stage 3 EDITOR     -> polish.json, review.json   edits, then publish or decline
tool               -> final_package.json         cv_draft ⊕ advocacy ⊕ polish
```

## Once per machine

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -c "import jobbsok; print(jobbsok.__file__)"
```

The printed path must be inside `Build_experimental`. Then `jobbsok preflight`.

## Starting a batch

1. Vacancy files in `inbox/vacancies/`, one row per approved job in a batch CSV
   (`jobbsok init-input` writes an empty one). `cluster` is your batch label and
   is what every stage session iterates over.
2. Put the models you will actually use in `[stages.role_mapping]` in
   `policy/settings.toml`: SCOUT, ARCHITECT, ADVOCATE, EDITOR. Freeze snapshots
   this, and it cannot be changed in place afterwards.
3. `jobbsok freeze --input inbox/<file>.csv --reviewed-by "<name>"`

## Running the four stages

One session per **stage × cluster**, started by you, on the model mapped to
that stage's role. The ready-to-paste prompts are in `prompts/`:
`STAGE0_SCOUT.md`, `STAGE1_ARCHITECT.md`, `STAGE2_ADVOCATE.md`,
`STAGE3_EDITOR.md`.

Each session loops: `next` → `context` → read → write the return files →
`preview` → `stage-submit`. The context bundle prints every path and the exact
submit command, including the 8-character evidence fingerprint. If the facts or
an upstream layer move while a stage is working, submission is refused and the
session re-runs `context`.

Stage 3 publishes with `--finalize-render`, which finalizes and renders
immediately, or declines with `--reject` and a RERUN review. A declined job
reappears in the queue at the stage the review names, with the editor's reasons
in that stage's next bundle.

## Looking at things

```powershell
jobbsok status --run <RUN>                 # queue: next stage, triage, signals
jobbsok status --run <RUN> --json          # regenerates status.json and queue.md
jobbsok register --run <RUN> --cluster <C> # what every letter in the cluster does
jobbsok cards --run <RUN> --search "<literal>"
jobbsok cards --run <RUN> --ids "EV:WORK#023-..."
jobbsok preview --run <RUN> --job <JOB> --stage 2
jobbsok assemble --run <RUN> --job <JOB> --dry-run
```

`preview` renders the work in progress to a scratch folder and prints pages,
headline lines, tail overflow, word counts and formula tics. It writes no
receipt and touches no canonical output. Page targets are editorial signals;
they never fail a command.

## Rendering

`finalize` assigns the canonical document date; `render` writes the DOCX and
PDF pair per document into `jobs/<job>/out/`. A package with `letter: null`
renders the CV alone and records the letter as SKIPPED. Form answers, when the
Advocate wrote any, land in `out/form_answers.md`.

A failed PDF is `DEGRADED`, never a semantic failure: export it by hand. A
render refuses to overwrite a file you edited yourself; use `--force` or
`--dest`.

## Redoing a stage

```powershell
jobbsok branch --run <RUN> --from-stage <0|1|2|3> --label <short> --reviewed-by "<name>"
```

The child inherits the parent's **factual** inputs, so reused artifacts still
point at the evidence they were written against, and takes the **control
plane** - settings, playbooks, writing policy, templates - live. Artifacts
owned by stages below `--from-stage` are re-stamped into the child; everything
at or above it is regenerated. `--refresh-inputs` re-collects the authorities
too and drops every artifact whose evidence fingerprint changed. The command
prints REUSED/DROPPED per job. The parent is never touched.

## What this system will never do

It will not contact an employer, submit an application, upload anything, or
take any irreversible external action. It has no network capability. Every
submission is yours to make by hand.
