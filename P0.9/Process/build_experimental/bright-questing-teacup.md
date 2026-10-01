# Relay: a four-stage experimental framework in `P0.9\Build_experimental`

## Context

Vegard copied `P0.9\Build` into `P0.9\Build_experimental` as a playground. The brief: take the optimization pitches from the runf/rung analysis as a starting point and build the framework design worth betting on. No QA, tests, preflight gates or defensive scaffolding; full throttle and risk-neutral. Stages remain **human-started agent sessions**, one goal prompt per stage × cluster (confirmed).

### What the evidence says

| Finding | Source | Design consequence |
|---|---|---|
| Selectivity and economy drive quality. `rung`'s lean strategies (15–20 KB) produced tight packages. `runf`'s rich Opus-on-both-stages strategies (34–41 KB) produced ~25% wordier documents, implementation mechanics in the letters and 3-page CVs. | Both reviewers (mine and Astra's) agree | Lean, binding brief; measured CV capacity |
| Stronger models add about +9 points to letters and +2 to CVs. | Matched vacancies | Reasoning spend goes where the argument is made |
| The final stage repaired every Stage-1 overstatement. | Both new runs | Every writer and editor sees claims *with their ceilings* |
| Recall wins came from non-obvious evidence (STE, §5.2 notes, Sector Alarm, the benefits method). | Package reviews | Filtering **demotes, never deletes** |
| Screen-out defects: self-disqualification, 3-page CV, 2-page letter, employer-blind letter, formula tics. | 30-package ranking | Measure them in-session: preview render, register, tic signals |
| Good gap handling names the gap once and turns it into an argument (Abacus). An explicit track choice helps (Stortinget). The best letter converted an employer fact and closed with a question. | Astra review, curated notes | Brief fields for stance, track, employer fact and moves |
| 0.9.3 cut Stage 2 for three reasons: drafts anchored the final writer and injected fabrications; a complete-package output saved no tokens; in 0.9.2 the polish stage deleted the one judgment example. | 0.9.3 consolidated input | Drafts are bounded to cards; the editor emits **patch ops** only; **keystones** protect judgment sentences |

**Critical environment finding (verified).** `Build_experimental\.venv` is a byte copy of the original environment:
- its `__editable__.jobbsok-0.9.1.pth` points to `P0.9\Build\runtime`;
- its launchers embed `P0.9\Build\.venv\Scripts\python.exe`.

Running it would execute, and could write through, the **live** Build, which is in use right now (runh / Itera Stage 1 at 21:25). Recreate the environment first. Never touch `P0.9\Build`.

## The design

```
Stage 0 SCOUT      cheap (Sonnet 5 High / Terra)          → scout.json          (per job, one session per cluster)
Stage 1 ARCHITECT  Opus 5 xhigh / Sol                     → strategy.json (lean brief) + cv_draft.json
Stage 2 ADVOCATE   Codex GPT-6 Astra (medium)             → letter_draft.json (+ ≤3 cv_ops, keystones)   [skipped if letter mode NONE]
Stage 3 EDITOR     Claude Code Opus 5 (medium) + Fable 5.1 advisor → edits.json (patch ops) + review.json
tool: stage-submit 3 → assemble (cv_draft ⊕ cv_ops ⊕ edits, letter_draft ⊕ edits) → final_package.json → finalize → render
```

**In-session tools the agents call:**
- `cards`: evidence cards, i.e. the section text plus its ceilings, digest row and forbidden/unresolved lines.
- `preview`: renders the in-progress draft; reports pages, the headline's line count, which tail sections fall on page 3, word counts and tics.
- `register`: the cluster's chosen moves and actual first and last sentences, so the letters vary.
- `assemble --dry-run`.

**Stage 2 context is bounded to the ids named in the brief.** `cards` and `context` scope what it receives; the agent sessions still have file access. **Stage 3 cannot regenerate.** It patches, or returns RERUN with a target stage.

## Phase 0: environment and archive (15 min)

1. **Recreate the virtual environment:**
   ```powershell
   cd P0.9\Build_experimental
   Remove-Item -Recurse -Force .venv
   & "C:\Users\veggi\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -e .
   .\.venv\Scripts\python.exe -c "import jobbsok; print(jobbsok.__file__)"   # must show Build_experimental
   ```
   Then bump `pyproject.toml` to version `0.10.0.dev0` and drop the dev extras and pytest config.
2. **Move superseded material into `archive_0.9.3\` (move, don't delete):**
   - `runtime/tests/`
   - `runtime/tools/make_fixtures.py` and `vertical_slice.py`
   - `runtime/jobbsok/failure.py` and `schemas/failure.schema.json`
   - both old stage playbooks, `prompts/STAGE1_PROMPT.md` and `STAGE3_PROMPT.md`
   - `BUILDER_REPORT.md`
3. **Leave `runs/` untouched.** The old runs are read-only seed data. The new runtime does not support revisions 0.9.0 or 0.9.3.

## Phase 1: stage registry and generic artifact core (~2 h)

### New `runtime/jobbsok/pipeline.py`, the single source of truth

```python
ArtifactSpec(name, filename, schema, owner_stage, artifact_role, inputs)   # inputs transitive
StageSpec(n, key, role, playbook, writes, requires, policy={file: [headings] | "ALL"}, personality, evidence_scope)
```

| artifact | owner | artifact_role | inputs |
|---|---|---|---|
| scout | 0 | SCOUT_FACTS | – |
| strategy (brief) | 1 | BRIEF | scout |
| cv_draft | 1 | CV_DRAFT | scout, strategy |
| letter_draft | 2 | LETTER_DRAFT | + cv_draft |
| edits | 3 | EDITS | + letter_draft |
| final_package | tool (Stage-3 submit) | **CURRENT_SEMANTIC_PACKAGE** (keep it: `artifacts.py:150` excludes `finalization` only for this role) | + edits |
| review | 3 | OPERATOR_TRIAGE | + final_package |

- **Binding for every artifact:** `{run_id, job_id, employer, title, playbook_sha256, inputs: {name: artifact_hash}}`.
- **Staleness:** an artifact is stale when `binding.inputs != current input hashes`. This replaces `evaluate_staleness` and the `STALE_SCOPE`/`UPSTREAM_BINDING` tables at `artifacts.py:43-90` and `594-656`.

### Files that derive from the registry; legacy branches are deleted, not generalized

- **`artifacts.py`:**
  - Keep `artifact_path`, `load`, `artifact_hash` (122-152).
  - Make `semantic_state`, `stamp` and `submit_many` generic (history copy plus atomic write).
  - Delete the handoff envelope and `verify_handoff` (218-359), the Stage-3 pair submit (505-587), `LEGACY_*`, `ALIASES` and `MECHANICAL_FIELDS`. The tool-owned fields become `artifact_role`, `binding` and `finalization`.
- **`paths.py`:**
  - Delete `STAGE_WRITE_MAP`, `RETIRED_STAGE_OWNERSHIP` and `TOOLING_OWNED` (200-233).
  - Loosen the run reference and branch component regexes (40-51) to `[a-z0-9][a-z0-9_-]{0,31}`.
- **`manifest.py`:**
  - Delete `LEGACY_SPEC_REVISION`, `STAGE1_POLICY_FILENAMES`, `writing_policy_records` (60-94) and `stage_policy_sha256` (181-199).
  - Freeze stage playbooks by looping over `STAGES` (249-255).
- **`settings.py`:**
  - Remove the role enum (25), the stage1/stage3 checks (76-93) and recovery.
  - Snapshot becomes `{language, personality, role_mapping, render, capacity}`.
- **`policy/settings.toml`:**
  ```toml
  [stages.role_mapping]
  SCOUT = "Claude Code / Sonnet 5 (High)"
  ARCHITECT = "Claude Code / Opus 5 (xhigh)"
  ADVOCATE = "Codex / GPT-6 Astra (Medium)"
  EDITOR = "Claude Code / Opus 5 (Medium) + Fable 5.1 advisor"
  [capacity]
  cv_dynamic_words = 520      # editorial signal; recalibrate in smoke step 3
  letter_words = 400
  ```
- **`validate.py`:** per artifact, run schema, identity and a generic walker. The walker checks that every `EV:` string resolves, plus employment IDs (in overrides and in `cv.override[...]` op targets), facet IDs, and leakage on CV/letter fields (keep 307-310). Delete 37-41, 107-135 and 339-361.
- **`branch.py`:**
  - `--from-stage 0..3 --label L` copies the artifacts owned by stages below N and re-stamps them in registry order.
  - Delete `CONTENT_GOVERNING` and the tables (67-108), the role comparison (147-173), the ancestor snapshot (223-230, 399-411) and revision migration.
- **`schemas.py`:** `SCHEMA_FILES` comes from the registry.
- **`__init__.py`:** revision `0.10.0-exp`.
- **Stub playbooks:** one-line stubs for `policy/stages/stage0_scout.md` … `stage3_editor.md`, so `index build` and `freeze` work.

## Phase 2: schemas (write alongside Phase 1)

**Conventions for all new schemas:**
- Evidence ref pattern: `^EV:(WORK|EDU|OTHER)#(file|preamble|[0-9]{3}-[a-z0-9-]{1,60})$`.
- `artifact_role`, `binding` and `finalization` are tool-owned.
- Run ID pattern in all schemas: `(?:/branches/[a-z0-9][a-z0-9_-]{0,31})?`.

**`scout.schema.json`**
- `vacancy {employer, unit?, title, deadline?, reference?, language nb|nn|en|other, sector}`
- `requirements[1..] {id Qnn, quote≤300, kind MUST|SHOULD|NICE|TASK, relation STRONG|PARTIAL|ADJACENT|GAP|UNKNOWN, refs[]}`
- `thresholds[] {id Tn, quote, dimension YEARS|LEVEL|EDUCATION|LANGUAGE|CLEARANCE|CERTIFICATION|OTHER, required, candidate, status MEETS|MISSES|UNCLEAR, refs[]}`
- `tracks[0..3] {label, quote, fit STRONG|STRETCH|UNDER}`
- `employer_facts[0..5] {fact, quote, conversion}`
- `channel {letter_mode FULL|SHORT|NONE, quote?, route, screening_questions[]}`
- `reader_signals[] {signal, quote}`
- `triage {core[1..12] {ref, why}, reserve[0..15] {ref, why}}`

**`strategy.schema.json`**: the lean brief; replaces the old schema; strings ≤400.
- `position {track, thesis, reader_need, headline_intent}`
- `units[1..3] {id U1-3, refs[1..], proves, employer_problem, ceiling (verbatim from card), placement CV|LETTER|BOTH}`
- `judgment {refs, judgment, ceiling, placement} | null`
- `reserve[0..5] {ref, use_if}`
- `employer_fact {fact, quote, conversion} | null`
- `stances[] {req Qn|Tn, relation MEETS|PARTIAL|ADJACENT|GAP, stance OMIT|BRIDGE|NAME_ONCE, via_ref?, line?}`
- `distinctiveness {facets[0..2] {facet_id PF-nn, behaviour, refs[1..]}, motive, opening_move, closing_move}`
  - `opening_move`: EMPLOYER_FACT | JUDGMENT_CASE | RESULT_CASE | TRACK_CHOICE | PROBLEM | DIRECT_MOTIVE
  - `closing_move`: QUESTION | CONTRIBUTION | NEXT_STEP | MOTIVE_ECHO | PLAIN
- `letter_plan {mode FULL|SHORT|NONE, word_target, paragraphs[0..3] {job, unit_ids[], refs[]}}`
- `traps[] {phrase, ceiling}`
- `outside_scout_refs[]`

**`cv_draft.schema.json`**
- `cv {headline≤70, profile, competencies[1..], employment_overrides[] {employment_id, bullets[]}, tools_line?}`
- `used_evidence_refs[1..]`

**`letter_draft.schema.json`**
- `letter {opening, body_paragraphs[1..], closing}`
- `cv_ops[0..3]` (target `cv.*` only)
- `keystones[0..4] {text, function JUDGMENT|EMPLOYER_FACT|GAP_TURN|TRACK_CHOICE|MOTIVE|CLOSE}`
- `used_evidence_refs[]`

**`edits.schema.json`**
- `ops[]`, `added_refs[]`, `writer_note?`

**Op grammar** (shared by `cv_ops` and `edits.ops`):
- **target:** `^(cv\.(headline|profile|tools_line|competencies(\[\d+\])?|override\[EMP_[A-Z0-9_]+\](\[\d+\])?)|letter\.(opening|closing|body(\[\d+\])?))$`
- **op:** replace | delete | insert_after | insert_item
- **fields:** `find` (exact substring), `with?`, `position after|start|end?`, `ref?`
- **reason:** SCREEN_OUT | TRUTH | TONE | PERSONALITY | DIFFERENTIATION | SOCIAL_RISK | COMPLEMENTARITY | CAPACITY | TIC

**Changes to existing schemas:**
- **Review:** keep the current fields; add `rerun_stage 1|2|null`, required when RERUN.
- **Package:**
  - `source_stage` const ASSEMBLED; generic binding; drop the `allOf` that requires `strategy_sha256`.
  - `letter` may be null (mode NONE); optional `cv.tools_line`.
- **Manifest:** revision const `0.10.0-exp`; `stage_instructions` stage0–3; the new settings snapshot.
- **Status:** `highest_valid_stage` SCOUT|ARCHITECT|ADVOCATE|EDITOR|null; add `next_stage` and `signals[]`.
- **render_report:** `documents` minItems 1; component state gains `SKIPPED`.

## Phase 3: CLI, cards, context, submit, status (~2 h)

### New `runtime/jobbsok/cards.py`, replacing `tools/fetch.py` (reuse `evidence_index.slice_entry`, `digest_rows`, `search`, `ids_for_refs`)

For each evidence ID:
1. **Section text.** Take `slice_entry`. If the body has two or fewer non-empty lines, extend to the whole subtree.
2. **Strip metadata.** Remove `**Selection metadata**` and `**Kompakt evidens- og autoritetskart**` blocks by default (about 15% of bytes); `--full` keeps them.
3. **Digest line.** Append the digest row from WORK §0.3, EDU §0.5 and OTHER §0.2 whose source section resolves to this ID, as `Lifecycle | Can prove | Live ceilings`.
4. **Boundary lines.** Append rows and bullets from WORK §8, §10.1, §10.2 and EDU §4.1/§4.2 that mention any of the card's `source_stated_ids` (PRJ-/CLM-/EMP-/EDU- ids).
5. **Pack.** Header `### <id> · WORK 375-435 · <heading>`. One "Boundaries" appendix: the mandatory sections from `cli.py:958-962`.

**CLI:** `cards --run R (--ids a,b | --job J --stage N | --search T) [--full]`. With `--job/--stage`, the scope comes from the registry:
- stages 0–1: any ID;
- stage 2: the brief's units, judgment, reserve, stances and `via_ref`s;
- stage 3: the draft's `used_evidence_refs` plus the brief's refs.

An out-of-scope ID prints a one-line note and is skipped.

### `context --run --job --stage N [--stats]` (rewrite `cmd_context`, `cli.py:1083-1282`)

- Writes its inputs to `generated/returns/<flat run>/<job>/stage{N}/inputs/`.
- Prints JSON: `{job, role, configured_model, read{}, optional{}, commands{cards, preview, assemble_dry, register, submit}, write{allowed, return_paths (…/stage{N}/<artifact>.semantic.json), schema_paths, tool_owned_fields}}`.
- `--stats` prints bytes and ~tokens per item, which checks the ≥33% cut.

| Stage | read | optional |
|---|---|---|
| 0 | vacancy view (+ pages if flagged); `digests.md` (reuse `cli.py:1018-1041`); `retrieval.md` (§0.4 keyword tables); `catalog.md` (id + heading path); `facts.md` (cards: WORK §0.2/§1.2, EDU §0.1, OTHER §5.1, baseline periods); `policy.md` | full authority paths |
| 1 | scout; vacancy view; `cards_core.md` + boundaries; `reserve.md` (ref, why, digest row); digests; retrieval; catalog; baseline projection (`baseline.py:239-258`); facet index; `policy.md`; `register.md`; capacity; RERUN reasons from the review if any | personality profile, full authority paths |
| 2 | brief; cv_draft; scout without triage; **vacancy view**; `cards_scoped.md` + boundaries; `policy.md`; `register.md` | none; no personality, no V |
| 3 | `assembled_draft.json`; brief; scout facts; vacancy view; `cards_used.md` + boundaries; `personality_distilled.json` (reuse `cli.py:1212-1243`); `policy.md` (voice level from settings); `register.md`; keystones | full authorities via `cards --search` |

**`policy.md`** is assembled per stage from heading sections (reuse `evidence_index._headings`) and prints `policy_missing` for any heading it cannot find. D is WRITING_DOCTRINE, K PERSUASION_CALIBRATION, V FORFATTERSTEMME.
- **Stage 0:** D «Ubetrodd vacancy-innhold».
- **Stage 1:** K in full; D Mål og myndighet, Yrkesanker, Diagnostisk signal, Single Backbone, Integrert bevisenhet, Begrunnet motivasjon, Komplementaritet, Komplett CV-doktrine, Variasjon.
- **Stage 2:** K in full; D Integrert bevisenhet, Vinklingskjeden, Begrunnet motivasjon, Komplementaritet, Tjuesekunderstesten, both bytte-tests, compression order, Tegnsetting.
- **Stage 3:** K and V in full; D Tjuesekunderstesten, Dyplesningen, both bytte-tests, compression order, Variasjon, Tegnsetting, Komplett CV-doktrine.

### `stage-submit --run --job --stage N [--finalize-render]`

Stamp, validate everything, then write all or nothing. On error, print it and exit 1. No handoff file and no failure record.

- **Stage 1:** writes strategy + cv_draft.
- **Stage 2:** dry-runs `cv_ops` against cv_draft and requires every keystone to be found in the letter.
- **Stage 3:**
  1. Stamp and validate the edits.
  2. `assemble`.
  3. Stamp the final (finalization DRAFT) and validate it.
  4. Stamp the review bound to the final's hash.
  5. Write edits, final and review.
  6. With `--finalize-render`, run `finalize_one` (extracted from `cli.py:553-579`) and `render_one` (extracted from 737-880).

### Status and next

- **`status.py` ladder** (replaces 283-475):
  ```
  mode = brief.letter_plan.mode | scout.channel.letter_mode | FULL
  !scout→0; !(strategy&cv_draft)→1; mode≠NONE & !letter_draft→2; !(edits&final&review)→3; review RERUN→rerun_stage; else finalize/render
  ```
- **`next --stage N --cluster C`:** the first job in manifest order whose `next_stage` equals N.
- **Queue line:** `next: Stage N`, triage (+ `rerun_stage`), and signals from the preview JSON and render_report warnings: CV over 2 pages, letter over 1 page, headline over 1 line, first person in the CV, tics (E-3/E-14).

### `register --run [--cluster]` and `signals.py`

- **`register`** prints and writes `generated/views/<run>/register_<cluster>.md`, one row per job: track, opening/closing move, facets, employer fact, headline, the actual first and last letter sentence (final, else draft), `outside_scout_refs`, and tic counts across the cluster.
- **`signals.py` tic patterns:**
  - «forteller gjerne mer i en samtale»
  - «søker…fordi»
  - the cleft motive `Det (som|jeg) …, er`
  - `(vil|kan) jeg (ta med|bidra med)`
  - job title restated in the opening
  - a paragraph ending «avviklet»
  - first person in the CV

## Phase 4: assemble and preview (~2 h)

### `runtime/jobbsok/assemble.py`: `assemble(cv_draft, letter_draft|None, edits|None, baseline_map) -> (package, summary)`

- **Order:** `letter_draft.cv_ops`, then `edits.ops`, each applied sequentially.
- **Targets:**
  - A target is a string slot or a list (competencies, `override[EMP]`, body); `[i]` narrows it.
  - `find` must match exactly one item, once.
  - Matching is exact first, then whitespace-tolerant and quote-tolerant («»“”"'’).
  - A missing override starts from the baseline default bullets.
- **Ops:**
  - replace: once.
  - delete: tidies spaces and punctuation; an emptied list item is removed.
  - insert_after: places `with` right after `find`.
  - insert_item: adds a new list item.
- **Keystones:** an Editor delete covering at least 50% of a keystone fails unless its reason is TRUTH or SCREEN_OUT. Rewording via replace is allowed.
- **Errors are precise and actionable:**
  - `ASSEMBLE FAILED edits op 4/9 [TONE] letter.body[2] replace: find not found … item starts "…"`
  - `…matches 2 items: letter.body[0], letter.body[3]; add [i]`
- **Summary:** ops per document, % of letter characters changed, keystones intact n/m, word counts.
- **CLI:** `assemble --run --job [--dry-run] [--cv F --letter F --edits F]`.

### `runtime/jobbsok/preview.py`: `preview --run --job --stage N [--cv-only]`

1. **Build the package from in-progress returns** (else the current artifacts):
   - Stage 1: the CV only.
   - Stage 2: plus the letter and its `cv_ops`.
   - Stage 3: `assemble` with the in-progress edits.

   Inject `finalization {state: FINALIZED, document_date: today}` to pass `render.py:604-610`.
2. **Filter the template map** to `cv` when there is no letter.
3. **Render** with `render.render_job(..., destination=%TEMP%\jbprev\<job[:20]>\<HHMMSS>)`. This is export mode: no receipt, short path (budget at `render.py:517-538`), fresh folder avoids Word locks.
4. **Analyze with pymupdf:**
   - page count per document;
   - tail headings (TIDLIGERE ERFARING / TILLITSVERV / SPRÅK / KURS / REFERANSER) found past the target page;
   - fill of the last page;
   - headline line count: page-1 lines with font size ≥13 contained in `headline.upper()`;
   - dynamic CV words (headline, profile, competencies, bullets, `tools_line`) and letter words;
   - signals.
5. **Print a four-line report** and write the metrics to `generated/preview/<flat run>/<job>.json`. On a Word COM failure print `pages UNKNOWN` plus words and signals.

### Letter mode NONE, CV-only in five places

1. `cmd_render` passes a filtered map.
2. `preview` passes a filtered map.
3. `render._build_report` (1008-1017) loops over the components present and marks the letter SKIPPED.
4. `verify_receipt` (351-379) filters out the letter.
5. The render_report schema allows it.

If this turns out costly, treat NONE as SHORT.

## Phase 5: CV template and baseline (E-13, 30 min) and source fix

**`templates/template_map.json`:**
- `CV_SUPPORT_SECTION_2` → `none`, which drops REFERANSER.
- `CV_SUPPORT_SECTION_1` → `none`.
- `CV_OPTIONAL_LANGUAGES` → a new source `baseline.languages_and_courses` with heading «SPRÅK OG KURS» and two lines. Add the branch in `render.resolve_control` (198-204).
- `CV_TOOLS_METHODS` → `package.cv.tools_line`, prefix «VERKTØY  », empty means nothing.

**`CV_MASTER.docx` un-bold:**
- Add an `unbold` step to `runtime/tools/prepare_masters.py`. Remove `<w:b />` inside the XML span of these controls: `CV_OPTIONAL_TRUST`, `CV_OPTIONAL_LANGUAGES`, `CV_SUPPORT_SECTION_1/2/3`, `CV_TOOLS_METHODS`.
- Copy every other zip part byte-identical (pattern at `docxfill.py:366-373`), and keep `control_inventory` unchanged.
- The fill step copies runs (`docxfill.py:176-185`), so the change carries through.

**No hash blocker.** CV_BASELINE's hash table covers the three authorities, not the baseline itself (`baseline.py:60-74`), and freeze picks up the masters and map fresh.

**E-16(a), scaffolding only.** Correct the WORK §0.3 digest row for early BAR work to «gikk fra å få eget arbeid kvalitetssikret av andre til selvstendig gjennomføring, kvalitetssikring og lederrapportering». The cards now surface digest rows to every stage. Record the new WORK hash in CV_BASELINE's table.
- Leave CLM-BAR-004 (a fact nugget) unchanged; flag it for Vegard.

## Phase 6: playbooks, prompts, runbook, policy edits (~2 h)

### `policy/stages/stage0_scout.md`
- Extract; don't argue. Use verbatim quotes.
- Thresholds: compare against baseline periods, degrees, languages and clearance → MEETS/MISSES/UNCLEAR.
- **Level and track options**, e.g. «For ansettelse som seniorrådgiver … fortrinnsvis fem års».
- Checkable employer facts, each with the argument it could anchor (Brokio, BNXT, scale, mission).
- **Channel mode with its quote** («Vi krever selvfølgelig ikke søknadsbrev» → NONE/SHORT; "upload an updated copy of your CV" → NONE).
- Ignore FINN match percentages and platform tips.
- Triage: core ≤12, with at least one *non-obvious* candidate per major requirement from the retrieval index. Demote; never drop.

### `stage1_architect.md`
- **Reading:**
  - Read order: scout → vacancy → core cards → a **challenger sweep** of reserve, digests and catalog. Name ≥1 challenger per unit; record `outside_scout_refs`.
  - Fetch any card freely.
- **Positioning:**
  - An explicit track or level choice.
  - A one-sentence thesis.
  - ≤3 units, each with a verbatim ceiling, plus an optional judgment atom.
- **Gaps and employer fact:**
  - NAME_ONCE only for a threshold miss the screener will see anyway: once, turned into an argument (the Abacus pattern), never a list. Otherwise OMIT or BRIDGE (K rule 4).
  - Convert one employer fact.
- **Moves and traps:**
  - Choose opening and closing moves that differ from `register.md`; QUESTION is a legitimate close.
  - Traps: ceilings likely to be stretched («har modernisert», «besvarer KI-henvendelser», years of «eierskap»).
- **Personality:** 0–2 facets, each with a concrete behaviour and evidence, written as content for Stage 2.
- **Brief size:** ≤8 KB. No requirement ledger; stances cover only what matters.
- **CV:**
  - One-line headline naming a function; profile without first person; 6–8 competencies.
  - Status stated once; tools in `tools_line`; bullets carry scope, not mechanics.
  - **Run `preview --stage 1` until the CV is 2 pages with a one-line headline.**

### `stage2_advocate.md`
- **Inputs:** the brief binds; no evidence beyond `cards_scoped`. Stay inside card ceilings and the traps.
- **Structure and moves:**
  - ≤1 page (~350–400 words), ≤3 body paragraphs per the letter plan.
  - Opening and closing moves as chosen.
  - **Write the motive and the facet behaviours as content.**
- **Argument craft:**
  - Complement the CV rather than retelling it: the CV gives scope and delivery, the letter gives choice, judgment and consequence. No sentence repeats a CV bullet.
  - **Judgment over mechanics:** tools and implementation detail only when the ad asks.
  - Each caveat once; status once.
  - One employer-fact conversion, one transfer bridge.
  - Coverage integrated; no bolt-ons.
- **Gaps:** stances applied (NAME_ONCE: one sentence that turns into the argument).
- **Banned formulas:** the tic list plus V's «Mønstre som skal erstattes» names.
- **Keystones and CV ops:** mark 1–4 keystones; ≤3 `cv_ops`, for complementarity only.
- **Before submit:** run `preview --stage 2`.

### `stage3_editor.md`
- **Mode:** patch ops only.
- **Passes, in order:**
  1. **Screen-out:** self-disqualification, pages, headline lines, employer-blind, tics, first person in the CV, bold/format.
  2. **Truth:** every proposition against `cards_used` and boundaries, repairing overstatement *and* understatement.
  3. **Personality, tone and differentiation:** V register pass; variation against `register.md`.
  4. **Social risk:** self-importance, hedging, «vi» vagueness, misread facet risk.
- **Keystones:** reword, don't delete.
- **Loop:** `assemble --dry-run` → `preview --stage 3`.
- **Before submit:** **consult the advisor once per job**, then submit with `--finalize-render`.
- **RERUN instead of rewriting more than ~35%:**
  - Stage 1: wrong track, thesis or units, or an unsupported carrying claim.
  - Stage 2: employer-blind or broken structure.
- **Review:** ≤3 reasons, triage READY/CHECK/RERUN, no apply/no-apply advice.

### Policy text edits
- **V (FORFATTERSTEMME):**
  - Lines 59-61: replace the example with «Bussen kom tjue minutter for sent» framfor «det oppstod en forsinkelse på tjue minutter i bussens ankomst» (E-15).
  - «Mønstre»: add the tic list, the one-bridge rule (E-18) and variation by function (E-7).
- **D (WRITING_DOCTRINE):**
  - CV doctrine: no first person (E-17); one-line headline; capacity signal (E-12).
  - Begrunnet motivasjon: convert one employer fact (E-19).
  - Variasjon: points to the register.
  - Status once (E-8); integrate coverage (E-9).
- **K (PERSUASION_CALIBRATION) rule 4:** add the NAME_ONCE exception with the Abacus example.
- **PERSONALITY_PROFILE:** replace the Stage 2 mentions with Stage 1/3 wording (PP:17, 60, 164).

### Prompts and runbook
- **Four goal prompts:** `prompts/STAGE0_SCOUT.md` … `STAGE3_EDITOR.md`, ≤60 lines each, all pointing at `P0.9\Build_experimental`.
  - Loop: `next` → `context` → read → write returns → `preview` → `stage-submit`.
  - Stop rules; close the cluster with `status` and `register`.
  - Stage 3 targets Claude Code with the advisor.
- **`policy/RUNBOOK.md`:** ≤150 lines. freeze → S0 → S1 → S2 → S3 per cluster; branch `--from-stage`; model mapping.

## Verification: end-to-end smoke on real data (not QA)

1. **Import check:** `import jobbsok` resolves to Build_experimental. Then `index build` and `freeze` on `inbox/batch_input_exp.csv`: the 8 runf+rung rows in 2 clusters, vacancy sources as in `batch_input_runf.csv` / `batch_input_rung.csv`.
2. **Seed drafts** with a 20-line scratchpad script. From the runs `r20260914-211650-5d3516` / `…211651-5dbd38`, copy each job's `current/final_package.json` into:
   - `stage1/cv_draft.semantic.json` `{cv, used_evidence_refs}`;
   - `stage2/letter_draft.semantic.json` `{letter, cv_ops:[], keystones:[], used_evidence_refs}`.
3. **Capacity:** `preview --stage 2` on all 8 jobs, with E-13 off then on.
   - E-13 off: Amesto, BearingPoint and Visma should show 3 pages. E-13 on: expected 2.
   - Set `cv_dynamic_words` from the resulting table.
4. **Assemble:** hand-write Stortinget edits:
   - replace «Jeg forteller gjerne mer i en samtale.» with a question-shaped close;
   - delete one bridge sentence;
   - add one deliberately wrong `find`.

   Read the error, fix it, then run `assemble --dry-run` → `preview --stage 3` → `stage-submit --stage 3 --finalize-render`.
5. **Real chain:** re-freeze after Phase 6, then run on the rung cluster:
   - Stage 0 on all 4 jobs;
   - `context --stage 1 --stats`, compared with the old ≈62k tokens;
   - Stages 1 → 2 → 3 on at least 2 jobs;
   - `status` and `register`;
   - compare against rung/runf packages: pages, cues, and dual review (Opus + Astra).

## Risks and cheap mitigations

| Risk | Mitigation |
|---|---|
| The copied environment writes to live Build | Phase 0 first; the import-path check prints the resolved path |
| The cheap scout misses evidence | Demote-only packs; digests, retrieval index and catalog always present; Architect challenger sweep; `outside_scout_refs` in the register |
| Editor rewrites via large replaces | Summary shows % changed; the playbook says RERUN above ~35%; keystone rule in `assemble` |
| `find` mismatches | Tolerant matcher, precise errors, `assemble --dry-run` in the Stage-3 bundle |
| Word COM unavailable or slow in Codex (Stage 2) | `preview` prints pages UNKNOWN plus word counts; `--cv-only` |
| Advocate writes employer-blind without full context | Vacancy view in `read`; scout employer facts; screen-out pass checks the fact conversion |
| A renamed policy heading silently drops a section | The bundle prints `policy_missing` |
| Runs frozen with the stub playbooks | Re-freeze after Phase 6 |
