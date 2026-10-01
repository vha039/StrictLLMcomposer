# Jobbsøk_26 Relay — experimental build

An experimental redesign of the P0.9 harness. A human-approved opportunity set
becomes validated Bokmål CV-plus-letter packages through **four human-started
stages**, each a separately initiated agent session on its own model:

```
Stage 0 SCOUT      -> scout.json                 vacancy facts + evidence triage
Stage 1 ARCHITECT  -> brief.json, cv_draft.json  positioning + the CV layer
Stage 2 ADVOCATE   -> advocacy_draft.json        the letter (or the CV argument)
Stage 3 EDITOR     -> polish.json, review.json   edits, then publish or decline
tool               -> final_package.json         cv_draft ⊕ advocacy ⊕ polish
```

This tree is a playground copied from `../Build`. It does not interpret
0.9.0/0.9.3 runs, and nothing here is authoritative for the live build.

**Start here:** [`policy/RUNBOOK.md`](policy/RUNBOOK.md), then the four goal
prompts in [`prompts/`](prompts/). [`plan/RELAY_PLAN_ACCEPTED.md`](plan/RELAY_PLAN_ACCEPTED.md)
is the design this implements and [`HANDOVER.md`](HANDOVER.md) says what was
actually built.

## What is different from the two-stage harness

- **Layers, not rewrites.** Every semantic artifact is a partial package;
  `assemble` merges them field by field (present replaces, absent inherits,
  empty array clears). The Editor returns only what it changed, and can
  decline with a RERUN review instead of republishing a draft it rejects.
- **Facts travel with ceilings.** `jobbsok cards` returns an evidence section
  together with its digest row and every boundary line that names it. Stage 1
  quotes the ceiling into the brief, and it binds every later stage.
- **Demote, never delete.** The Scout's triage decides what Stage 1 reads
  first; the catalog, digests and retrieval index travel with every bundle and
  any stage can fetch anything. What a stage used beyond the brief is declared.
- **Measure, don't guess.** `jobbsok preview` renders the work in progress to a
  scratch folder and reports pages, headline lines, tail overflow, word counts
  and formula tics, inside the session that is writing.
- **Context and artifact fingerprints.** The stage evidence fingerprint
  namespaces returns and is required at submit. Each artifact binds all its
  declared inputs and its own evidence fingerprint for staleness. The policy
  fingerprint is provenance only, so editing a playbook never invalidates work.
- **Delivery is a choice.** A brief may choose CV-only delivery; the Advocate
  then strengthens the CV and answers the form questions, and rendering
  produces the CV alone.

## Layout

```text
authorities/   three factual authority files + CV baseline   (protected)
context/       personality profile                           (protected)
policy/        settings, writing policy, four stage playbooks (control plane)
prompts/       one goal prompt per stage                     (control plane)
templates/     CV and letter masters + the canonical map     (control plane)
schemas/       artifact schemas                              (control plane)
runtime/       deterministic code
generated/     index, baseline map, bundles, previews, views (disposable)
runs/<run_id>/ immutable manifest, current artifacts, renders
archive_0.9.3/ what the two-stage harness used, kept for reference
```

## Commands

| Command | Purpose |
|---|---|
| `preflight` / `index build\|verify` | environment, masters, generated maps |
| `init-input` / `freeze` | operator batch input, one immutable run |
| `next` / `context` | the next job for a stage, and that stage's bundle |
| `cards` | evidence cards by id, by search, or a stage's default pack |
| `preview` | render the work in progress and measure it |
| `assemble` | merge the layers and show the result |
| `stage-submit` | required `--fingerprint`; Stage 3 either publishes (`--finalize-render` optional) or rejects RERUN (`--reject`), never both |
| `register` | what every letter in a cluster already does |
| `finalize` / `render` | canonical date, then DOCX and PDF |
| `status` / `validate` / `verify-integrity` / `branch` | state, checks, child runs |

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -c "import jobbsok; print(jobbsok.__file__)"
```

The printed path must be inside `Build_experimental`. Two dependencies
(`jsonschema`, `pymupdf`), no network capability, no model client.
