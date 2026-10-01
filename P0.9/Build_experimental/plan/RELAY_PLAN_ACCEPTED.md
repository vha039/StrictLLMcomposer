# Relay — reconciled execution plan for `P0.9\Build_experimental`

## Context

`P0.9\Build_experimental` is a disposable copy of the live build, handed over as a playground: take the runf/rung optimization pitches as a point of departure and build the framework worth betting on. No QA frameworks, test suites, generic preflight, migration systems or defensive scaffolding; lightweight checks intrinsic to a chosen mechanism are fine. Breakage here is acceptable. **`P0.9\Build` must never be modified, including through copied environments or launchers.** Stages stay **separate, human-started agent sessions**, one goal prompt per stage × cluster.

This plan supersedes the earlier draft and folds in the independent review (`Build_experimental/reviews/PLAN_REVIEW_DIFF.md`), adjudicated below against current code.

### Evidence the design answers

| Finding | Consequence |
|---|---|
| Lean strategies (`rung`, 15–20 KB) produced tight packages; Opus-on-both-stages (`runf`, 34–41 KB) produced ~25% wordier documents, mechanics in letters and 3-page CVs | A short brief, measured capacity, specialization per stage |
| Strong models add ≈ +9 points to letters, ≈ +2 to CVs | Reasoning spend goes where the argument is made |
| The final stage repaired every Stage-1 overstatement | Facts always travel with their ceilings (evidence cards) |
| Recall wins came from non-obvious evidence (STE, §5.2 notes, Sector Alarm, benefits method) | Filtering **demotes, never deletes**; later stages may still retrieve |
| Screen-out defects: self-disqualification, 3-page CV, 2-page letter, employer-blind, formula tics | Measure in-session: `preview`, `register`, tic signals |
| Gap named once and turned into an argument (Abacus); explicit track choice (Stortinget); converted employer fact and question close (b5104f) | Brief fields for stance, track, employer fact, moves |
| 0.9.3 cut Stage 2 because drafts anchored the writer, injected fabrications and saved no tokens; 0.9.2's polish stage deleted the judgment sentence | Bounded default evidence pack + ceilings; the editor works in **layers**, declares keystone disposition, and can reject instead of rewriting |

**Environment (verified).** `Build_experimental\.venv` is a byte copy: `__editable__.jobbsok-0.9.1.pth` points at `P0.9\Build\runtime` and the launchers embed `P0.9\Build\.venv\Scripts\python.exe`. Recreate it before anything else.

## Adjudication record

| ID | Verdict | Decisive reason (verified in code) | Resulting decision |
|---|---|---|---|
| **D01** editorial freedom; drop substring ops | **ACCEPT, modified** | `merge.effective_cv` (merge.py:29-62) already defines replacement semantics for exactly the model-owned zones: present value replaces, absence inherits, empty array clears. A substring matcher plus tolerant matching, punctuation repair and percentage routing is machinery with no equivalent in the repo, and `replace` could erase a keystone while passing a delete-only check. | Stages return **layers** (partial packages), not ops. `assemble` = ordered field merge. Deleted: op grammar, `find`, tolerant matching, punctuation repair, the 50% keystone rule, the 35% rewrite threshold, the `cv_ops ≤3` cap. Kept: the brief is a **strong default with binding ceilings**; the Advocate and Editor may retrieve any frozen card and must declare `outside_brief_refs`; the Editor declares a **keystone disposition** (KEPT/REWORDED/REMOVED + reason) — an intrinsic field, not a lexical check. RERUN is a judgment call, not a percentage. |
| **D02** bind to inputs actually read | **ACCEPT, split in two** | `verify_handoff` (artifacts.py:328-359) recomputes the envelope and refuses a submission whose issued context no longer matches. `branch.branch` re-collects live inputs (branch.py:232) and `_same_governing_inputs` (164-172) is what stops unsafe reuse. `evidence_index.build_index` numbers IDs by heading ordinal, so the same ID can carry changed text. Dropping all of this would let a late return certify claims against evidence it never saw. | One `evidence_fingerprint` per stage over {run, job, stage, frozen authority/index/baseline/vacancy hashes, upstream artifact hashes} → stored in every binding, namespaces in-progress returns, re-checked at submit, and **is** the staleness test. A separate `policy_fingerprint` (playbooks + consumed policy sections) is recorded for provenance and shown in status, but **does not invalidate** — playbooks will be edited constantly here. `branch` inherits the parent's frozen snapshot by default; `--refresh-inputs` re-collects and drops every artifact whose evidence fingerprint changes. Re-stamping never establishes equivalence. |
| **D03** RERUN without manufacturing a final | **ACCEPT** | `schemas/review.schema.json:15` requires `final_package_sha256`; `cmd_finalize` (cli.py:524-579) never inspects triage. So the earlier plan forced the Editor to publish the draft it rejects. | Stage-3 submit has two paths: **reject** (`review` only, triage RERUN, `rerun_stage`, bound to the rejected layer's fingerprint; no final, no finalize/render) and **publish** (polish + assembled final + review bound to the final). Status routes a current RERUN before any missing-final rule. When the targeted stage resubmits, the rejection's fingerprint no longer matches, routing moves on, and its reasons are passed forward as advice. |
| **D04** CV-only jobs | **ACCEPT, modified** | Visma's vacancy says «Vi krever selvfølgelig ikke søknadsbrev» and adds application questions; Norwegian's says "upload an updated copy of your CV". Neither forbids a letter, and a CV-only channel puts *more* argumentative load on the CV — so skipping the persuasion specialist inverts the intended allocation. | Scout records `letter_requirement REQUIRED|OPTIONAL|UNSPECIFIED` + quote + `screening_questions[]`. The Architect makes an explicit `delivery` choice: LETTER_AND_CV / CV_ONLY / CV_PLUS_FORM_ANSWERS. **Stage 2 always runs**: for CV-only it returns `letter: null`, CV replacement fields carrying the argument, and `form_answers[]` for screening questions. Artifact renamed `advocacy_draft`; keystones cover either document; rendering is conditional on document presence; `assemble` writes `out/form_answers.md` when answers exist. The registry dependency stays unconditional (one graph). First CV-only job: compare the Architect's CV against the Advocate's in the human trial. |
| **D05** smoke ≠ model trial | **ACCEPT** | `cmd_context` requires current upstream artifacts, and the new registry requires scout + brief, so seeded CV/letter returns cannot legally pass `stage-submit`. One implementing session also cannot stand in for four independently human-started sessions (`prompts/STAGE1_PROMPT.md` confines a session to one stage). | Deterministic completion = the command chain exercised on constructed layers through `assemble`/`preview`/`render` library calls plus a real `freeze`/`context`/`status` pass. `stage-submit` is exercised only by the real chain. Implementation ends by printing the four goal prompts and stopping; the quality comparison happens after those human-started sessions run. |

**Own additions (high return on complexity):** `form_answers` as a first-class deliverable; RERUN reasons forwarded into the re-run stage's bundle; `register` carries delivery and employer fact; `cards --ids` accepts `CLM-/PRJ-/EMP-` source ids as well as `EV:` ids; artifact renames (`brief`, `advocacy_draft`, `polish`) since legacy revisions are dropped.

## The design

```
Stage 0 SCOUT      cheap (Sonnet 5 High / Terra)        → scout.json
Stage 1 ARCHITECT  Opus 5 xhigh / Sol                   → brief.json + cv_draft.json            (layer 1)
Stage 2 ADVOCATE   Codex GPT-6 Astra (medium)           → advocacy_draft.json                   (layer 2: letter|null, CV replacements, keystones, form_answers)
Stage 3 EDITOR     Claude Code Opus 5 (med) + Fable 5.1 → polish.json (layer 3) + review.json, or review-only rejection
tool  stage-submit 3 → assemble(layers) → final_package.json → finalize → render (+ out/form_answers.md)
```

- **Layers, not ops.** Every semantic artifact is a partial package. `assemble` merges in order (cv_draft → advocacy_draft → polish): a present field replaces, an absent field inherits, an empty array clears (the `merge.effective_cv` contract, applied one level up).
- **Ceilings bind; the brief is a strong default.** Later stages may retrieve any frozen card, and must declare `outside_brief_refs`. Cards always carry the claim's ceiling, digest row and boundary lines.
- **The Editor edits or rejects.** It has no "regenerate everything" mandate: it returns the fields it changed, the keystone disposition, and either publishes or returns RERUN with a target stage.
- **In-session tools:** `cards`, `preview` (render the in-progress layers; pages, headline lines, tail overflow, words, tics), `register` (cluster variation), `assemble --dry-run`.

## Phase 0 — environment and archive (15 min)

```powershell
cd P0.9\Build_experimental
Remove-Item -Recurse -Force .venv
& "C:\Users\veggi\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -c "import jobbsok, sys; print(jobbsok.__file__)"   # MUST print a Build_experimental path
```
- Abort everything if that path shows `P0.9\Build`.
- `pyproject.toml` → version `0.10.0.dev0`; drop dev extras and pytest config.
- Move (never delete) into `archive_0.9.3\`: `runtime/tests/`, `runtime/tools/make_fixtures.py`, `runtime/tools/vertical_slice.py`, `runtime/jobbsok/failure.py`, `schemas/failure.schema.json`, `policy/stages/stage1_decision_architecture.md`, `policy/stages/stage3_final_writer_review.md`, `prompts/STAGE1_PROMPT.md`, `prompts/STAGE3_PROMPT.md`, `BUILDER_REPORT.md`.
- Leave `runs/` untouched (read-only seed data). The new runtime supports only its own revision.

## Phase 1 — registry, artifact core, fingerprints, branch (~2 h)

### `runtime/jobbsok/pipeline.py` — one source of truth

```python
ArtifactSpec(name, filename, schema, owner_stage, artifact_role, inputs)     # inputs transitive
StageSpec(n, key, role, playbook, writes, requires, policy={file: [headings] | "ALL"},
          personality, evidence_scope, reads)
```

| artifact | file | owner | artifact_role | inputs |
|---|---|---|---|---|
| scout | scout.json | 0 | SCOUT_FACTS | – |
| brief | brief.json | 1 | BRIEF | scout |
| cv_draft | cv_draft.json | 1 | CV_LAYER | scout, brief |
| advocacy_draft | advocacy_draft.json | 2 | ADVOCACY_LAYER | + cv_draft |
| polish | polish.json | 3 | POLISH_LAYER | + advocacy_draft |
| final_package | final_package.json | tool (Stage-3 publish) | **CURRENT_SEMANTIC_PACKAGE** (keep the string: `artifacts.py:150` excludes `finalization` only for this role) | + polish |
| review | review.json | 3 | OPERATOR_TRIAGE | publish: + final_package · reject: + advocacy_draft |

**Binding on every artifact:** `{run_id, job_id, employer, title, evidence_fingerprint, policy_fingerprint, inputs: {name: artifact_hash}}`.

- `evidence_fingerprint = sha256_canonical_json({run_id, job_id, stage, frozen: {WORK, EDU, OTHER, CV_BASELINE, evidence_index, baseline_map, vacancy_normalized}, upstream: {artifact: hash}})` — computed in `pipeline.evidence_fingerprint(context, job, stage)`.
- `policy_fingerprint` covers the stage playbook and its consumed policy sections. **Provenance only.**
- **Staleness** = recomputed `evidence_fingerprint` ≠ stored. This replaces `STALE_SCOPE`, `UPSTREAM_BINDING` and `evaluate_staleness` (artifacts.py:43-90, 594-656). Status prints which component changed.

### Files

- **`artifacts.py`** (rewrite to ~200 lines): keep `artifact_path`, `load`, `artifact_hash` (122-152); make `semantic_state`, `stamp`, `submit_many` generic (history copy + atomic write); delete the handoff envelope and `verify_handoff` (218-359), the Stage-3 pair submit (505-587), `LEGACY_*`, `ALIASES`, `MECHANICAL_FIELDS`. Tool-owned fields are `artifact_role`, `binding`, `finalization`.
- **`paths.py`**: delete `STAGE_WRITE_MAP`, `RETIRED_STAGE_OWNERSHIP`, `TOOLING_OWNED` (200-233); loosen the run-reference and branch-component patterns (40-51) to `[a-z0-9][a-z0-9_-]{0,31}`.
- **`manifest.py`**: delete `LEGACY_SPEC_REVISION`, `STAGE1_POLICY_FILENAMES`, `writing_policy_records` (60-94) and `stage_policy_sha256` (181-199); freeze playbooks by looping over `STAGES` (249-255).
- **`settings.py` / `policy/settings.toml`**: drop the role enum and recovery block; snapshot `{language, personality, role_mapping, render, capacity}`.
  ```toml
  [stages.role_mapping]
  SCOUT = "Claude Code / Sonnet 5 (High)"
  ARCHITECT = "Claude Code / Opus 5 (xhigh)"
  ADVOCATE = "Codex / GPT-6 Astra (Medium)"
  EDITOR = "Claude Code / Opus 5 (Medium) + Fable 5.1 advisor"
  [capacity]
  cv_dynamic_words = 520     # editorial signal, recalibrated in the smoke
  letter_words = 400
  ```
- **`validate.py`**: per artifact — schema, identity, then one generic walker that resolves every `EV:` string, checks employment and facet IDs and runs the leakage scan on CV/letter fields (keep 307-310). Delete 37-41, 107-135, 339-361.
- **`branch.py`**: `--from-stage N --label L` copies the parent's frozen snapshot and the artifacts owned by stages below N, re-stamping bindings; `--refresh-inputs` re-collects live inputs and drops artifacts whose evidence fingerprint changes. Delete `CONTENT_GOVERNING` (67-108), the role comparison (147-173), the ancestor snapshot (223-230, 399-411) and revision migration.
- **`schemas.py`**: `SCHEMA_FILES` from the registry. **`__init__.py`**: revision `0.10.0-exp`.
- Stub playbooks `policy/stages/stage{0..3}_*.md` so `index build` and `freeze` run.

## Phase 2 — schemas (with Phase 1)

Conventions: ref pattern `^EV:(WORK|EDU|OTHER)#(file|preamble|[0-9]{3}-[a-z0-9-]{1,60})$`; `artifact_role`, `binding`, `finalization` tool-owned; run-id pattern `(?:/branches/[a-z0-9][a-z0-9_-]{0,31})?`.

- **`scout.schema.json`** — `vacancy{employer, unit?, title, deadline?, reference?, language, sector}`; `requirements[1..]{id Qnn, quote≤300, kind MUST|SHOULD|NICE|TASK, relation STRONG|PARTIAL|ADJACENT|GAP|UNKNOWN, refs[]}`; `thresholds[]{id Tn, quote, dimension YEARS|LEVEL|EDUCATION|LANGUAGE|CLEARANCE|CERTIFICATION|OTHER, required, candidate, status MEETS|MISSES|UNCLEAR, refs[]}`; `tracks[0..3]{label, quote, fit STRONG|STRETCH|UNDER}`; `employer_facts[0..5]{fact, quote, conversion}`; `submission{letter_requirement REQUIRED|OPTIONAL|UNSPECIFIED, quote?, route, screening_questions[]}`; `reader_signals[]{signal, quote}`; `triage{core[1..12]{ref, why}, reserve[0..15]{ref, why}}`.
- **`brief.schema.json`** (strings ≤400) — `position{track, thesis, reader_need, headline_intent}`; `delivery LETTER_AND_CV|CV_ONLY|CV_PLUS_FORM_ANSWERS` + `delivery_reason`; `units[1..3]{id, refs[1..], proves, employer_problem, ceiling (verbatim), placement CV|LETTER|BOTH}`; `judgment{…}|null`; `reserve[0..5]{ref, use_if}`; `employer_fact{fact, quote, conversion}|null`; `stances[]{req, relation, stance OMIT|BRIDGE|NAME_ONCE, via_ref?, line?}`; `distinctiveness{facets[0..2]{facet_id, behaviour, refs}, motive, opening_move EMPLOYER_FACT|JUDGMENT_CASE|RESULT_CASE|TRACK_CHOICE|PROBLEM|DIRECT_MOTIVE, closing_move QUESTION|CONTRIBUTION|NEXT_STEP|MOTIVE_ECHO|PLAIN}`; `letter_plan{word_target, paragraphs[0..3]{job, unit_ids, refs}}`; `traps[]{phrase, ceiling}`; `outside_scout_refs[]`.
- **`cv_draft.schema.json`** — `cv{headline≤70, profile, competencies[1..], employment_overrides[]{employment_id, bullets[]}, tools_line?}`; `used_evidence_refs[1..]`.
- **`advocacy_draft.schema.json`** — `letter{opening, body_paragraphs[1..], closing} | null`; `cv{…partial, same shape as cv_draft.cv, all properties optional…}`; `keystones[0..4]{id Kn, text, document LETTER|CV, function JUDGMENT|EMPLOYER_FACT|GAP_TURN|TRACK_CHOICE|MOTIVE|CLOSE}`; `form_answers[]{question, answer}`; `used_evidence_refs[]`; `outside_brief_refs[]`; `notes?`.
- **`polish.schema.json`** — `cv{…partial…}?`; `letter{…partial: any of opening/body_paragraphs/closing…}?`; `form_answers[]?`; `keystone_disposition[]{id, disposition KEPT|REWORDED|REMOVED, reason}`; `changes[]{field, reason SCREEN_OUT|TRUTH|TONE|PERSONALITY|DIFFERENTIATION|SOCIAL_RISK|COMPLEMENTARITY|CAPACITY|TIC}`; `added_refs[]`; `outside_brief_refs[]`.
- **`review.schema.json`** — keep triage/reasons/known_limitations/diagnostics; binding becomes `{run_id, job_id, inputs{}}`; add `rerun_stage 1|2|null`; conditional: `triage == RERUN` requires `rerun_stage` and binds `advocacy_draft`; otherwise requires the `final_package` hash.
- **`package.schema.json`** — `source_stage` const `ASSEMBLED`; generic binding; `letter` may be null; optional `cv.tools_line`, `form_answers[]`; drop the `allOf` requiring `strategy_sha256`.
- **`manifest` / `status` / `render_report`** — revision `0.10.0-exp`; `stage_instructions` stage0–3; new settings snapshot; `highest_valid_stage` SCOUT|ARCHITECT|ADVOCATE|EDITOR|null plus `next_stage`, `signals[]`, `stale_reason`; `documents` minItems 1 and component state gains `SKIPPED`.

## Phase 3 — CLI: cards, context, submit, status, register (~2 h)

### `runtime/jobbsok/cards.py` (replaces `tools/fetch.py`; reuse `evidence_index.slice_entry`, `digest_rows`, `search`, `ids_for_refs`)

Per ID: section text (extend to the subtree when the body has ≤2 non-empty lines) → strip `**Selection metadata**` / `**Kompakt evidens- og autoritetskart**` blocks unless `--full` → append the matching digest row as `Lifecycle | Can prove | Live ceilings` → append rows and bullets from WORK §8/§10.1/§10.2 and EDU §4.1/§4.2 that mention the card's `source_stated_ids`. Header: `### <id> · WORK 375-435 · <heading>`. The pack ends with one **Boundaries** appendix (the mandatory sections at `cli.py:958-962`).

`cards --run R (--ids … | --job J --stage N | --search T) [--full]`. `--ids` accepts `EV:` ids and `CLM-/PRJ-/EMP-/EDU-` source ids. `--job/--stage` builds that stage's default pack (Stage 2: the brief's units, judgment, reserve, stances; Stage 3: the draft's `used_evidence_refs` plus the brief's). **No refusal outside the pack** — retrieval stays open and the artifact declares `outside_brief_refs`.

### `context --run --job --stage N [--stats]` (rewrite `cmd_context`, cli.py:1083-1282)

Writes inputs to `generated/returns/<flat run>/<job>/stage{N}/<fp8>/inputs/` where `fp8` is the first 8 chars of the evidence fingerprint. Prints `{job, role, configured_model, evidence_fingerprint, read{}, optional{}, commands{cards, preview, assemble_dry, register, submit}, write{allowed, return_paths, schema_paths, tool_owned_fields}}`. `--stats` prints bytes and ≈tokens per item (the ≥33% context cut is measured here).

| Stage | read | optional |
|---|---|---|
| 0 | vacancy view (+ page images when flagged); `digests.md` (reuse cli.py:1018-1041); `retrieval.md` (§0.4 keyword tables); `catalog.md` (id + heading path); `facts.md` (WORK §0.2/§1.2, EDU §0.1, OTHER §5.1, baseline periods); `policy.md` | full authority paths |
| 1 | scout; vacancy view; `cards_core.md` + boundaries; `reserve.md`; digests; retrieval; catalog; baseline projection (baseline.py:239-258); facet index; `policy.md`; `register.md`; capacity; `rerun_advice.md` when a RERUN review targets this stage | personality profile, full authorities |
| 2 | brief; cv_draft; scout (minus triage); **vacancy view**; `cards_scoped.md` + boundaries; `policy.md`; `register.md`; `rerun_advice.md` | further cards via `cards --ids/--search` |
| 3 | `assembled_draft.json` (cv_draft ⊕ advocacy_draft); brief; scout facts; vacancy view; `cards_used.md` + boundaries; `personality_distilled.json` (reuse cli.py:1212-1243); `policy.md` + voice level; `register.md`; keystones | further cards |

`policy.md` is assembled from heading sections (reuse `evidence_index._headings`) and prints `policy_missing` for any heading it cannot find. D = WRITING_DOCTRINE, K = PERSUASION_CALIBRATION, V = FORFATTERSTEMME.
- **S0:** D «Ubetrodd vacancy-innhold».
- **S1:** K in full; D Mål og myndighet, Yrkesanker, Diagnostisk signal, Single Backbone, Integrert bevisenhet, Begrunnet motivasjon, Komplementaritet, Komplett CV-doktrine, Variasjon.
- **S2:** K in full; D Integrert bevisenhet, Vinklingskjeden, Begrunnet motivasjon, Komplementaritet, Tjuesekunderstesten, both bytte-tests, compression order, Tegnsetting.
- **S3:** K and V in full; D Tjuesekunderstesten, Dyplesningen, both bytte-tests, compression order, Variasjon, Tegnsetting, Komplett CV-doktrine.

### `stage-submit --run --job --stage N [--reject] [--finalize-render]`

Recompute the evidence fingerprint; if it differs from the one the returns were written under, refuse with one line naming the changed component and the `context` command to re-run. Then stamp, validate, write all-or-nothing. No handoff file, no failure artifact, no retry engine.
- **Stage 1** writes brief + cv_draft. **Stage 2** writes advocacy_draft (schema alone enforces the shape; keystone text must appear in the document it names).
- **Stage 3 publish:** validate polish → `assemble` → stamp the final (finalization DRAFT) → validate → stamp the review bound to the final → write polish, final, review. `--finalize-render` then calls `finalize_one` (extracted from cli.py:553-579) and `render_one` (from 737-880).
- **Stage 3 reject (`--reject`):** validate and write **review only**, triage RERUN, `rerun_stage` 1 or 2, bound to the advocacy_draft's fingerprint. No polish, no final, no render.

### Status, next, register

- **Ladder** (replaces status.py:283-475): `!scout → 0`; `!(brief & cv_draft) → 1`; `!advocacy_draft → 2`; **current review with RERUN → its `rerun_stage`**; `!(polish & final & review) → 3`; else finalize/render.
- **`next --stage N --cluster C`** returns the first job in manifest order whose `next_stage` is N.
- **Queue line:** `next: Stage N`, triage (+ rerun_stage), delivery mode, and signals from `generated/preview/<run>/<job>.json` and `render_report`: CV > 2 pages, letter > 1 page, headline > 1 line, first person in CV, tics.
- **`register --run [--cluster]`** prints and writes `generated/views/<run>/register_<cluster>.md`: track, delivery, opening/closing move, facets, employer fact, headline, the actual first and last letter sentence, `outside_brief_refs`, and cluster tic counts.
- **`signals.py`** patterns: «forteller gjerne mer i en samtale»; «søker…fordi»; the cleft motive `Det (som|jeg) …, er`; `(vil|kan) jeg (ta med|bidra med)`; title restated in the opening; paragraph ending «avviklet»; first person in the CV.

## Phase 4 — assemble and preview (~1.5 h)

### `runtime/jobbsok/assemble.py`

`layer_merge(base, patch)`: for each field present in the patch, replace; absent inherits; an empty array clears (mirrors `merge.effective_cv`). `employment_overrides` merge by `employment_id`; a present entry replaces that employment's bullets.

`assemble(cv_draft, advocacy_draft, polish|None) -> (package, summary)`:
- `cv` = cv_draft.cv ⊕ advocacy_draft.cv ⊕ polish.cv
- `letter` = polish.letter ⊕ advocacy_draft.letter (null stays null)
- `form_answers` = the last layer that supplies them
- `used_evidence_refs` = union of all layers' refs, `added_refs` and `outside_brief_refs`
- **summary**: fields changed per layer, word counts, keystone disposition, refs added outside the brief.

CLI `assemble --run --job [--dry-run] [--cv F --advocacy F --polish F]`. `--dry-run` prints the summary and the merged document text without writing.

### `runtime/jobbsok/preview.py` — `preview --run --job --stage N [--cv-only]`

1. Build the package from in-progress returns (else current artifacts): Stage 1 = CV only; Stage 2 = ⊕ advocacy; Stage 3 = ⊕ polish. Inject `finalization {state: FINALIZED, document_date: today}` to pass `render.py:604-610`.
2. Filter the template map to `cv` when `letter` is null or `--cv-only`.
3. `render.render_job(..., destination=%TEMP%\jbprev\<job[:20]>\<HHMMSS>)` — export mode, no receipt, short path (budget at render.py:517-538), fresh folder avoids Word locks.
4. pymupdf analysis: pages per document; tail headings (TIDLIGERE ERFARING / TILLITSVERV / SPRÅK / KURS / REFERANSER) past the target page; last-page fill; headline line count (page-1 lines ≥13 pt contained in `headline.upper()`); dynamic CV words and letter words; tic signals.
5. Print four lines; write `generated/preview/<flat run>/<job>.json`. On a Word COM failure print `pages UNKNOWN` plus words and signals (Codex sandboxes may have no COM).

### CV-only rendering (five touch points)

`cmd_render` and `preview` pass a filtered template map; `render._build_report` (1008-1017) loops over present components and marks the letter `SKIPPED`; `verify_receipt` (351-379) filters it out; the schema allows it.

## Phase 5 — CV template, baseline, source fix (~40 min)

- **`templates/template_map.json`**: `CV_SUPPORT_SECTION_2` → `none` (drops REFERANSER); `CV_SUPPORT_SECTION_1` → `none`; `CV_OPTIONAL_LANGUAGES` → new source `baseline.languages_and_courses`, heading «SPRÅK OG KURS» (add the branch in `render.resolve_control`, near 198-204); `CV_TOOLS_METHODS` → `package.cv.tools_line`, prefix «VERKTØY  ».
- **`CV_MASTER.docx` un-bold**: add an `unbold` step to `runtime/tools/prepare_masters.py` removing `<w:b />` inside `CV_OPTIONAL_TRUST`, `CV_OPTIONAL_LANGUAGES`, `CV_SUPPORT_SECTION_1/2/3`, `CV_TOOLS_METHODS`; copy every other zip part byte-identical (docxfill.py:366-373); control inventory unchanged. The fill step copies those runs (docxfill.py:176-185), so it carries through.
- **No hash blocker**: CV_BASELINE's table hashes the three authorities (baseline.py:60-74), not itself; `freeze` picks up masters, map and baseline fresh; frozen runs keep their copies.
- **E-16(a), scaffolding only**: correct the WORK §0.3 digest row for early BAR work to «gikk fra å få eget arbeid kvalitetssikret av andre til selvstendig gjennomføring, kvalitetssikring og lederrapportering», then record the new WORK hash in CV_BASELINE's table. Cards now surface digest rows to every stage, so the error would otherwise propagate. Leave CLM-BAR-004 (a fact nugget) for Vegard.

## Phase 6 — playbooks, prompts, runbook (~2 h)

**`stage0_scout.md`** — extract, don't argue; verbatim quotes; thresholds against baseline periods, degrees, languages, clearance; level/track options («fortrinnsvis fem års»); checkable employer facts with the argument each could anchor; `letter_requirement` with its quote and any screening questions; ignore FINN match percentages and platform tips; core ≤12 with at least one non-obvious candidate per major requirement; **demote, never drop**.

**`stage1_architect.md`** — read scout → vacancy → core cards → a **challenger sweep** of reserve, digests and catalog (≥1 challenger per unit; record `outside_scout_refs`); explicit track choice and one-sentence thesis; **explicit delivery choice** with reason; ≤3 units each with a verbatim ceiling plus an optional judgment atom; NAME_ONCE only for a threshold miss the screener will see anyway — once, turned into an argument, never a list (otherwise OMIT or BRIDGE, K rule 4); convert one employer fact; opening and closing moves different from `register.md` (QUESTION is legitimate); traps for the «har modernisert» class; 0–2 facets with a concrete behaviour; brief ≤8 KB, no requirement ledger. CV: one-line functional headline, no first person, 6–8 competencies, status once, tools in `tools_line`, scope over mechanics; run `preview --stage 1` until the CV is 2 pages with a one-line headline.

**`stage2_advocate.md`** — the brief binds on ceilings and is the default on selection; retrieve more cards when the argument needs it and declare `outside_brief_refs`. Letter ≤1 page (~350–400 words), ≤3 body paragraphs, the chosen moves, motive and facet behaviours written as content. Complement the CV: the CV gives scope and delivery, the letter gives choice, judgment and consequence; no sentence repeats a CV bullet. Judgment over mechanics — tools only when the ad asks. Each caveat once; status once; one employer-fact conversion; one transfer bridge; coverage integrated, no bolt-ons. Banned formulas (tic list + V's «Mønstre»). **CV-only delivery:** `letter: null`, strengthen the CV through replacement fields, answer screening questions in `form_answers`. Mark 1–4 keystones. Run `preview --stage 2` before submitting.

**`stage3_editor.md`** — work in layers: return only the fields you change, with a reason each. Passes in order: (1) screen-out — self-disqualification, pages, headline lines, employer-blind, tics, first person in the CV; (2) truth — every proposition against `cards_used` and boundaries, repairing overstatement *and* understatement; (3) personality, tone, differentiation — V register pass, variation against `register.md`; (4) social risk. Declare a disposition for every keystone; preserve its **argument function**, reword freely, remove only with a TRUTH or SCREEN_OUT reason. Loop `assemble --dry-run` → `preview --stage 3`. **Consult the advisor once per job before submitting.** Choose `--reject` (RERUN) when upstream reconsideration is genuinely cheaper than editing — wrong track, thesis or units, an unsupported carrying claim (Stage 1); an employer-blind or structurally broken letter (Stage 2) — rather than rebuilding the package yourself. Review: ≤3 reasons, no apply/no-apply advice.

**Policy text edits** — V lines 59-61: «Bussen kom tjue minutter for sent» framfor «det oppstod en forsinkelse på tjue minutter i bussens ankomst» (E-15); V «Mønstre»: tic list, one-bridge rule (E-18), variation by function (E-7). D CV doctrine: no first person (E-17), one-line headline, capacity signal (E-12); Begrunnet motivasjon: convert one employer fact (E-19); Variasjon points to the register; status once (E-8); integrate coverage (E-9). K rule 4: add the NAME_ONCE exception with the Abacus example. PERSONALITY_PROFILE: replace the Stage-2 mentions (PP:17, 60, 164).

**Prompts and runbook** — `prompts/STAGE0_SCOUT.md` … `STAGE3_EDITOR.md`, ≤60 lines each, pointing at `P0.9\Build_experimental`: loop `next` → `context` → read → write returns → `preview` → `stage-submit`; stop rules; close the cluster with `status` and `register`; Stage 3 names the advisor call and both submit paths. `policy/RUNBOOK.md` ≤150 lines: freeze → S0 → S1 → S2 → S3 per cluster, RERUN routing, `branch --from-stage`, model mapping.

## Deterministic completion (implementation stop boundary)

The implementing session finishes here. It exercises mechanics only — no stage model sessions, no quality claims.

1. **Environment**: `import jobbsok` resolves inside `Build_experimental`.
2. **Freeze**: `index build`, then `freeze` on `inbox/batch_input_exp.csv` (the 8 runf + rung rows, 2 clusters, existing vacancy sources).
3. **Layer smoke via library calls** (scratchpad script, ~20 lines; no `stage-submit`): read each job's `current/final_package.json` from `runs/r20260914-211650-5d3516` and `…-5dbd38`, split it into a `cv_draft`-shaped layer and an `advocacy_draft`-shaped layer, then call `assemble` and `preview` directly.
   - Expected: E-13 off → 3-page CVs for Amesto, BearingPoint, Visma; E-13 on → 2 pages. Set `cv_dynamic_words` from the measured table.
   - One CV-only case with `letter: null` plus `form_answers` renders the CV alone and writes `out/form_answers.md`.
   - One polish layer replacing a closing paragraph and one CV bullet exercises `layer_merge` and the summary.
4. **Command chain**: `context --stage 0 --stats` for one job (record the token delta against the ≈62k baseline); `status`, `next`, `register`, `cards --job … --stage 2`, `assemble --dry-run`, `branch --from-stage 2` and `branch --from-stage 2 --refresh-inputs` after touching a policy file, confirming reuse and drop behave as specified.
5. **Hand over**: print the four goal prompts and stop. Implementation is complete at this line.

## Human-started trials (after implementation, not part of it)

Vegard starts one session per stage × cluster, in order, on the rung cluster first: Stage 0 (Sonnet) → Stage 1 (Opus xhigh) → Stage 2 (Astra medium) → Stage 3 (Opus medium + Fable advisor, `--finalize-render`). Then compare the resulting packages against the existing rung/runf packages on pages, screen-out cues, and a dual review (Opus and Astra). Only that comparison decides whether the relay beats the two-stage harness, whether Stage 2 earns its keep on CV-only jobs, and where the capacity setting lands.

## Risks and cheap mitigations

| Risk | Mitigation |
|---|---|
| The copied environment writes to live Build | Phase 0 first; abort on the printed path |
| A cheap Scout misses evidence | Demote-only packs; digests, retrieval index and catalog always present; Architect challenger sweep; `outside_scout_refs` and `outside_brief_refs` in the register |
| Late return certifies against changed evidence | Evidence fingerprint in the returns path and re-checked at submit |
| Playbook churn marks everything stale | Policy fingerprint is provenance only |
| Editor quietly rewrites the package | Layers make the change set explicit; keystone disposition; `--reject` is the sanctioned alternative |
| Word COM missing in a Codex sandbox | `preview` prints pages UNKNOWN with word counts; `--cv-only` |
| Advocate writes employer-blind | Vacancy view in `read`; scout employer facts; Editor screen-out pass |
| A renamed policy heading silently drops a section | `policy_missing` printed in the bundle |
| Runs frozen against stub playbooks | Re-freeze after Phase 6 |

## After plan acceptance

Once the user explicitly accepts this plan:

1. Immediately save the accepted plan to a durable location inside `P0.9/Build_experimental` (`P0.9/Build_experimental/plan/RELAY_PLAN_ACCEPTED.md`).
2. Then create and output one optimized `/goal` prompt instructing myself to execute the **entire** accepted plan.
3. That prompt must be **strictly under 4,000 characters** including the `/goal` prefix; initialize execution from the repository; point to the saved plan as the authoritative implementation specification; preserve material scope, constraints and stop conditions; require inspection of actual repository state before changes; prohibit modifying `P0.9/Build`; instruct full execution rather than re-planning; and preserve the human-started stage boundaries. Verify the character count before output.
4. After outputting that single prompt, **HALT**.
5. Do not start implementation until the user initializes execution with that `/goal`.
