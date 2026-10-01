# Relay — implementation handover

Built 2026-09-16 against `plan/RELAY_PLAN_ACCEPTED.md`. Implementation is
complete at the plan's deterministic stop line: mechanics are exercised, no
stage model sessions were run, and nothing here is a quality claim.

## What exists

**Runtime** (`runtime/jobbsok/`)
- `pipeline.py` — the stage registry: seven artifacts, four stages, the policy
  section map per stage, and both fingerprints. Everything else derives from it.
- `artifacts.py` — generic load/stamp/submit; staleness compares every declared
  input, then the artifact's frozen-evidence fingerprint.
- `cards.py` — evidence cards (section + digest row + boundary lines naming it),
  the boundary appendix, the catalog, the digests, the retrieval index, the
  facet projection, and each stage's default pack.
- `assemble.py` — `layer_merge` and `assemble`, plus the change summary.
- `preview.py` — renders work in progress to a scratch folder and measures it.
- `signals.py` — word counts and the formula tics this corpus produced.
- `branch.py` — inherits the parent's facts, takes the control plane live,
  `--refresh-inputs` re-collects and drops what no longer matches.
- `validate.py`, `status.py`, `cli.py` — generic validation, the 0→1→2→3 ladder
  with RERUN routing, and the command surface.

**Control plane** — four playbooks in `policy/stages/`, four goal prompts in
`prompts/`, a rewritten `policy/RUNBOOK.md`, `[stages.role_mapping]` with the
four stage roles and a `[capacity]` block, and the policy edits E-7, E-8, E-9,
E-12, E-15, E-17, E-18, E-19 plus the K rule-4 NAME_ONCE exception.

**Schemas** — `scout`, `brief`, `cv_draft`, `advocacy_draft`, `polish`,
`package` (nullable letter, `source_stage: ASSEMBLED`, optional `tools_line`
and `form_answers`), `review` (conditional binding + `rerun_stage`), plus
manifest/status/render_report updates.

**Templates** — REFERANSER dropped, KURS folded into «SPRÅK OG KURS», the
support blocks un-bolded (the step is reproducible in
`runtime/tools/prepare_masters.py::unbold_support_blocks`), and
`CV_TOOLS_METHODS` wired to `cv.tools_line`.

**Sources** — the WORK §0.3 BAR digest row now matches its own source (the row
said the candidate quality-assured others; the source says the reverse), and
CV_BASELINE records the new WORK hash. CLM-BAR-004 is untouched and still
flagged for Vegard.

## Measured

**Context.** Stage 1 on a realistic ten-card core pack: 121.8 KB ≈ 36.9k tokens,
against ≈197 KB ≈ 59.7k for the old Stage 1 that read all three authorities in
full — **−38%**. Stage 0 ≈ 18.1k tokens, Stage 2 ≈ 13.7k, Stage 3 ≈ 17.4k.

**CV capacity.** The eight 14 September packages, re-rendered through the new
template after E-13. Every one of them now fits two pages, including the three
that overflowed before:

| Job | Dynamic CV words | Pages before (runf/rung) | Pages now | Headline lines |
|---|---:|---|---:|---:|
| Tieto | 488 | 2 | 2 | 2 |
| BearingPoint | 588 | **3** | 2 | 2 |
| Amesto | 591 | **3** | 2 | 1 |
| Visma | 605 | **3** | 2 | 2 |
| Stortinget | 431 | 2 | 2 | 1 |
| Norwegian | 504 | 2 | 2 | 1 |
| EIE | 424 | 2 | 2 | 2 |
| Abacus | 459 | 2 | 2 | 2 |

So the two-page boundary now sits above 605 dynamic words. `[capacity]
cv_dynamic_words` is set to **600** as an editorial signal, not a limit; the
five two-line headlines are a separate, still-open defect that Stage 1's
preview loop is meant to catch.

The raw table is in `generated/preview/capacity_table.json`.

## Exercised

- `index build`, `preflight`, `freeze` (8 jobs, clusters `runf`/`rung`, run
  `r20260916-184816-a1ea76`).
- Layer smoke: the eight packages split into CV and advocacy layers, assembled
  and previewed; one CV-only case (letter null + form answers) and one polish
  layer replacing a closing and adding a tools line.
- Full mechanical chain on a throwaway one-job run `r20260916-185207-a37938`:
  stage 0 → 1 → 2 → 3 with fixture content, the `--reject` path (review only,
  queue routed back to Stage 2 with the editor's reasons), then publish with
  `--finalize-render`, then a CV-only republish where the receipt records the
  letter as SKIPPED and `out/form_answers.md` is written.
- A stale fingerprint is refused with the exact `context` command to re-run.
- `cards --search`/`--ids`, `assemble` from explicit files, `register`,
  `validate` (7 artifacts, 0 failures), `status --json`, `next`, and `branch`
  in both inherit and `--refresh-inputs` modes.

## Deviations from the plan, and why

1. **`vacancy_original` moved to `optional`.** It is the source PDF; counting
   375 KB of PDF as "read" made `--stats` meaningless.
2. **Catalog trimmed to the leaf heading and the facet index projected** into a
   choosing surface (`facets.md`, ~3 KB instead of 15 KB). Without these two
   the Stage-1 reduction was 29%, under the plan's target.
3. **A mechanical four-stage chain was run** on a separate throwaway run. The
   plan said stage-submit belongs to the real chain; leaving the submit path
   entirely unexecuted would have handed the first human session an untested
   command. The fixture content is deliberately trivial and lives only in
   `r20260916-185207-a37938`.
4. **`prepare_masters.py` gained the un-bold step** rather than the master
   being edited only once by hand, so the change is reproducible.
5. **Old runs were left in place** and the two-stage runtime was moved to
   `archive_0.9.3/` rather than deleted.

## Open

- **Two-line headlines** in five of eight CVs. The signal exists; the fix is
  editorial and belongs to Stage 1.
- **Resolved: leftover letter files.** Stage-3 rejection or a republish that
  drops a document withdraws receipt-named products to `out/withdrawn/<timestamp>/`.
  Unreceipted files remain untouched. `stage-submit` requires a fingerprint;
  publishing and RERUN rejection are mutually exclusive.
- **The fixture run** `r20260916-185207-a37938` and the two empty branch
  children of the 8-job run can be deleted whenever you like.
- **CLM-BAR-004** — moving the demand-driven-allocation phrase from the claim
  text to the ceiling column is still a Vegard decision.
- **`branch --refresh-inputs` drop behaviour** was exercised on a run without
  artifacts; the drop path itself has not been seen with a real fact change.

## Next

The four human-started sessions, in order, on the models in
`[stages.role_mapping]`. Prompts: `prompts/STAGE0_SCOUT.md`,
`STAGE1_ARCHITECT.md`, `STAGE2_ADVOCATE.md`, `STAGE3_EDITOR.md`. Run
`r20260916-184816-a1ea76` holds the same eight vacancies as runf and rung, so
the resulting packages are directly comparable with them.
