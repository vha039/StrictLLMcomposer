# Working in this tree

This is the Relay build: one vacancy becomes a Bokmål CV-plus-letter package
through four stages, each run by a different model in its own session. You are
almost certainly one of those stages. Deterministic code does the plumbing —
context, validation, merging, rendering, status — and never calls a model.

Run everything with `.\.venv\Scripts\jobbsok.exe` from this folder.

## The map

```
policy/stages/     your playbook - the frozen instruction for your stage
policy/writing/    doctrine (D), persuasion calibration (K), voice (V)
policy/RUNBOOK.md  the operator's view of the whole loop
policy/settings.toml  models per stage role, capacity signals, render config
prompts/           the goal prompt each stage session is started with
authorities/       the three factual sources + the CV baseline (never edit)
context/           the personality profile (interpretive, never facts)
templates/         CV and letter masters + the one canonical control map
schemas/           one schema per artifact; the bundle points you at yours
runs/<run>/        frozen inputs, current artifacts, renders, history
generated/         bundles you were handed, previews, status views (disposable)
runtime/jobbsok/   the code; pipeline.py is the registry everything derives from
archive_0.9.3/     the previous two-stage harness, kept for reference only
HANDOVER.md        what was built, what was measured, what is open
```

Artifacts per job, in order: `scout` → `brief` + `cv_draft` →
`advocacy_draft` → `polish` + `review` → `final_package` (assembled by the
tool). Each is a **layer**: a partial package. Merging replaces present
fields, inherits absent ones, and clears empty arrays.

## The happy path

```powershell
jobbsok next    --run <RUN> --stage <N> --cluster <C>   # pick the job
jobbsok context --run <RUN> --job <JOB> --stage <N>     # your bundle
#   read read.playbook and read.policy in full, then the rest of read.*
jobbsok cards   --run <RUN> --search "<literal>"        # or --ids "EV:...,EV:..."
#   write the semantic fields to write.return_paths.*
jobbsok preview --run <RUN> --job <JOB> --stage <N>     # pages, words, tics
#   iterate until the physical facts are right
#   then run commands.submit exactly as printed
```

Then take the next job. Close the cluster with `jobbsok status --run <RUN>
--json` and `jobbsok register --run <RUN> --cluster <C>`, and report what is
outstanding.

**The bundle is the authority.** It names your job, every file you should
read, the exact paths to write, your schema, and the exact submit command with
its fingerprint. Your memory of the previous job is not authority; reset to the
bundle each time.

## How to reason here

**Priority order when two goods conflict.** Truth beats everything: no claim
past the ceiling on its card, in either direction — understating documented
work is also a defect. Then avoiding screen-out: the letter that volunteers a
gap, the three-page CV, the two-line headline, the employer-blind letter.
Then the argument: does this answer the employer's actual problem. Then
variation across the cluster. Polish last, and never at the cost of the three
above.

**One decision per stage, made properly.** Stage 0 extracts and triages, it
does not argue. Stage 1 decides and does not write letter prose. Stage 2
argues and does not re-decide. Stage 3 edits or declines and does not rebuild.
Reaching into a neighbour's job is how the previous harness produced wordy,
duplicated packages.

**Retrieve cheaply, then deeply.** The default pack in your bundle is the
starting point, not the boundary. When you want more: the catalog and the
retrieval index first (they are already in the bundle), then
`cards --search`, then `cards --ids`, then the frozen authority itself. Every
card carries its own ceilings, digest row and boundary lines — read those, not
just the prose. Every stage receives `digests.md`, `retrieval.md` and `catalog.md`.

**Declare what you used.** Evidence you used beyond what the brief named goes
in `outside_brief_refs` (Stage 1: `outside_scout_refs`). Nobody is punished for
reaching; silently reaching is what breaks the chain of ceilings.

**Demote, never drop.** A triage that hides evidence cannot be undone
downstream. Anything you deprioritise stays listed and fetchable.

**Measure, do not guess.** Page counts, headline line counts, tail overflow
and word counts come from `preview`, which actually renders the document. The
previous corpus shipped three-page CVs because stages estimated instead of
looking.

**Write for a reader who skims in twenty seconds, then reads closely if it
survives.** Concrete verbs, a real decision, its consequence. No self-grading,
no announced abstraction, no restating the ad back to them.

**When something is genuinely wrong upstream, say so instead of patching over
it.** Stage 3 has `--reject`; earlier stages can note it. A quietly repaired
bad decision looks the same as a good one in the record, and the next run
learns nothing.

**Stop when the decision is made.** The brief has a size target because a
longer brief produced a longer, worse package. Depth belongs in the choice and
the ceiling, not in volume.

## When something refuses you

| What you see | What it means | What to do |
|---|---|---|
| `The context changed while this stage was working` | Facts or an upstream layer moved | Re-run `context`, re-read the diff, write to the new return path |
| `Missing return file for <artifact>` | Wrong path | Use `write.return_paths` from the bundle verbatim |
| `contains tooling-owned fields` | You wrote `artifact_role`/`binding`/`finalization`/`source_stage` | Semantic fields only |
| Schema or reference errors | Listed with file, field, expected, observed | Fix once, resubmit the same command |
| `<id> does not resolve` | Evidence id typo or invented | `cards --search` for the real id; never invent one |
| `policy_missing: <file> / <heading>` | A policy heading was renamed | Report it; do not guess the section's content |
| `pages UNKNOWN` in preview | Word COM unavailable here | Use the word counts, and say pages were not measured |
| Render `DEGRADED` | DOCX fine, PDF failed | Not a semantic failure; the human exports by hand |
| `publish refused: triage is RERUN` | Publication and rejection are exclusive | Use `--reject` |
| `--reject is Stage 3 only` | An earlier stage cannot withdraw a package | Submit only that stage's write set |

Nothing here is a gate to be worked around. A refusal is information about
state, and the message names the command that fixes it.

## Never

- Re-submit an upstream artifact once a downstream stage has started without
  telling the operator what it invalidates.

- Edit `authorities/`, `context/`, or another stage's artifact. Facts change
  only through human source maintenance; an artifact changes only by its owning
  stage re-running.
- Hand-edit a file under `runs/*/current/`. Submit through `stage-submit` so it
  is stamped, validated and versioned into `history/`.
- Invent an evidence id, a ceiling, an employer fact or a date.
- Add schema fields, tests, detectors, similarity scores or numeric quality
  measures. Counts and pages are editorial signals only.
- Cross a stage boundary, or run `finalize`/`render` from a stage that is not
  Stage 3 publishing.
- Treat platform text (FINN match percentages, "tips til søknaden") as a
  requirement.

## If you are lost

Read `policy/RUNBOOK.md` for the whole loop, `HANDOVER.md` for what exists and
what is open, and `runtime/jobbsok/pipeline.py` for the registry that defines
every artifact, stage and fingerprint. `jobbsok status --run <RUN>` always
tells you where the run actually stands; disk is the truth, not chat history.
