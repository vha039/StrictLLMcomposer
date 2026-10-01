# Relay — onboarding brief

Context only. The two reports in `reviews/FIRST_CLUSTER_ANALYSIS.md` and
`plan/NEXT_DEVELOPMENT_PLAN.md` cover the first run's results and the proposed
fixes; nothing here repeats them.

## Purpose

One vacancy → one validated Bokmål CV-plus-letter package, built from three
frozen factual authorities. Optimises for **interview odds**: avoid screen-out,
never exceed a documented ceiling, never understate one, and make each package
in a cluster read differently.

## What this tree is

A disposable copy of `../Build` (the live 0.9.3 two-stage harness), redesigned
as a four-stage relay. `../Build` is **read-only — never write to it, including
through venvs, launchers or `.pth` paths**. Breakage here is acceptable.

Revision `0.10.0-exp`. Run everything with `.\.venv\Scripts\jobbsok.exe`;
`import jobbsok` must resolve inside `Build_experimental`.

## Pipeline

```
0 SCOUT     Sonnet 5 high       scout.json                    vacancy facts + evidence triage
1 ARCHITECT Opus 5 xhigh        brief.json + cv_draft.json    positioning + CV layer
2 ADVOCATE  GPT-6 Astra med     advocacy_draft.json           the letter (or the CV argument)
3 EDITOR    Opus 5 med + Fable  polish.json + review.json     edit, then publish or decline
tool                            final_package.json            cv_draft ⊕ advocacy ⊕ polish
```

Each stage is a **separately human-started agent session**, one per stage ×
cluster. There is no model client, no scheduler and no network capability in
the code. Deterministic code does context assembly, validation, merge, render,
status — nothing else.

## Design decisions and why

| Decision | Rationale |
|---|---|
| **Layers, not rewrites.** Every artifact is a partial package; `assemble` merges field by field (present replaces, absent inherits, empty array clears) | 0.9.2's polish stage deleted the judgment sentence. A layer makes the change set explicit and reviewable |
| **Editor may decline.** `stage-submit --stage 3 --reject` writes review only, `rerun_stage` 1 or 2 | Earlier design forced publishing the draft it rejected |
| **Facts travel with ceilings.** `cards` returns section text + digest row (`Lifecycle \| Can prove \| Live ceilings`) + every boundary line naming the section | Stage 3 repaired an overstatement in every 0.9.3 job; ceilings now bind from Stage 1 |
| **Demote, never delete.** Scout triage sets reading order; catalog, digests and retrieval index travel with every bundle; any stage may fetch anything and declares `outside_brief_refs` | Recall wins in the old corpus came from non-obvious evidence a filter would have dropped |
| **Two fingerprints.** `evidence_fingerprint` (frozen facts + upstream artifact hashes) namespaces returns, is re-checked at submit, and **is** the staleness test. `policy_fingerprint` is provenance only | Playbooks are edited constantly here; editing one must not invalidate work |
| **Measure, don't guess.** `preview` renders work-in-progress to `%TEMP%` and reports pages, headline line count, tail overflow, words, tics | The previous corpus shipped three-page CVs because stages estimated |
| **Delivery is a choice.** LETTER_AND_CV / CV_ONLY / CV_PLUS_FORM_ANSWERS. Stage 2 always runs; CV-only returns `letter: null` + `form_answers[]` | A CV-only channel puts *more* argumentative load on the CV, so skipping the persuasion specialist inverts the allocation |
| **Bounded brief (~8 KB), ≤3 units.** | Lean 0.9.3 strategies produced tight packages; Opus-on-both-stages produced ~25% wordier documents |

## Changed from the 0.9.3 baseline

- **Added** Stage 0 and Stage 2. `strategy.json` split into `brief` + `cv_draft`.
- **Removed** the handoff envelope + `verify_handoff`, the failure artifact and
  retry engine, `STAGE_WRITE_MAP`/`RETIRED_STAGE_OWNERSHIP`, legacy revision
  tables, all tests and QA scaffolding. Moved to `archive_0.9.3/`, not deleted.
- **New runtime:** `pipeline.py` (the registry everything derives from),
  `cards.py`, `assemble.py`, `preview.py`, `signals.py`. Rewrote `artifacts.py`,
  `validate.py`, `status.py`, `branch.py`, most of `cli.py`.
- **New schemas:** scout, brief, cv_draft, advocacy_draft, polish. Rewrote
  package (nullable letter, `source_stage: ASSEMBLED`, `tools_line`,
  `form_answers`) and review (generic binding + `rerun_stage`).
- **Templates:** REFERANSER dropped, KURS folded into «SPRÅK OG KURS», support
  blocks un-bolded, `CV_TOOLS_METHODS` wired to `cv.tools_line`.
- **Policy edits** E-7/8/9/12/15/17/18/19 and the K rule-4 NAME_ONCE exception.
- **Source fix:** the WORK §0.3 BAR digest row contradicted its own source
  (said the candidate quality-assured others; source says the reverse).

## Measured before the first run

- Stage 1 context **−38%** (121.8 KB ≈ 36.9k tokens vs ≈197 KB ≈ 59.7k).
  Stage 0 ≈18.1k, Stage 2 ≈13.7k, Stage 3 ≈17.4k.
- Two-page CV boundary now sits **above 605 dynamic words** (all eight prior
  packages re-rendered, including the three that overflowed).
  `[capacity] cv_dynamic_words = 600` is an editorial signal, not a limit.

## Current state

- `r20260916-184816-a1ea76` — 8 jobs, clusters `runf` and `rung`.
  - `rung` (4): through Stage 2. Stage 3 layers written but **unsubmitted**,
    sitting in `generated/returns/<run>/<job>/stage3/<fp8>/`.
  - `runf` (4): not started.
- `r20260916-185207-a37938` — throwaway mechanical fixture, disposable.
- Counterparts for comparison: `r20260914-211651-5dbd38` (`rung`),
  `r20260914-211650-5d3516` (`runf`), same eight vacancies, old harness.
- Everything else under `runs/` is 0.9.0/0.9.3 seed data. Leave it alone.

## Hard constraints

1. Never modify or execute code from `P0.9\Build`.
2. No QA frameworks, test suites, generic preflight, compatibility or migration
   layers, or defensive scaffolding. Checks intrinsic to a mechanism are fine.
3. Stages stay separate human-started sessions. No autopilot, no orchestration.
4. `authorities/` and `context/` are user-owned facts — only Vegard edits a fact
   nugget. Scaffolding is agent-owned.
5. Move superseded files to `archive_0.9.3/`; do not delete.
6. Artifacts change only through `stage-submit`. Never hand-edit `runs/*/current/`.

## Where to look

`AGENTS.md` (how to behave in this tree) · `policy/RUNBOOK.md` (operator loop) ·
`HANDOVER.md` (what was built, what is open) · `runtime/jobbsok/pipeline.py`
(artifacts, stages, policy map, both fingerprints) ·
`plan/RELAY_PLAN_ACCEPTED.md` (the design this implements).
