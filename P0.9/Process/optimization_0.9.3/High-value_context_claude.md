# High-value context — Claude

Essentials only. Everything here is verified against disk unless marked *inferred*. Written for a fresh instance that must act without re-deriving.

## Identity

- Root `R` = `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`; Build `B` = `R/P0.9/Build`; venv `B/.venv`.
- Norwegian Bokmål CV + letter per approved vacancy. Truth outranks persuasion. No portal, no automated submission.
- Authority order: user instruction → `P0.9/Architecture/*NORMATIVE_SPECIFICATION.md` → `*IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md` → root `AGENTS.md` → `P0.9/Process/**` (evidence only). **Reproduced behaviour in `B/` outranks every document.**
- Optimization order: truthful package quality ≫ low human effort > simple robust implementation > model cost > reversibility.
- Hazard: `P0.7/**` holds real but retired instruction sets including `AGENTS.md` files. Ignore, plus `P0.9/archive/`, the Build ZIP, `B/tmp/`.

## The decision that reshapes everything

**Stage 2 is cut.** Active route: Stage 1 (strategy) → Stage 3 (complete final CV+letter + review). Separate instance/chat each; that boundary is immutable.

Evidence: `package.schema.json` requires a complete `cv` and `letter` in every final, **so a draft cannot absorb Stage 3's output obligation — the cost rationale was unachievable by construction.** Measured draft→final letter retention, excluding the one same-instance run: **9.3 / 13.7 / 14.3 / 18.6 / 20.4 / 24.2 / 24.8 / 33.0 %.** Every traced fabrication (D1, D2, and two more in `r20260905-115243` drafts) originated in a Stage-2 draft.

`Spec §22.1` freezes **"three-stage semantics"** (line 1218) → requires an explicit written amendment, not a silent deviation. Also touches `DEC-19`, `INV-09`, `CTR-05/06`, `DEC-26`, §§10–12.

Not just deletion: `package.schema.json:154-158` requires `draft_sha256`; `manifest.schema.json:77,127` requires `stage2`; `artifacts.py:207-213` requires a draft. New finals must bind `strategy_sha256` instead. **Historical runs keep their frozen schemas, bindings and the original hash algorithm.**

## The two defects the whole treatment exists to fix

Both were *unsupported elaboration inside a genuinely supported case* — not status, ownership or scale inflation. The claim-ceiling machinery guards the latter and is blind to the former.

- **D1** — `Vi tok den videre gjennom workshops og opplæring…` attached to `PRJ-04`. `Work_experience.md §4.4` contains **zero** workshop/training/onboarding tokens. Those belong to `PRJ-01`, `PRJ-08`, `§5.2`.
- **D2** — `Det som endret løsningen mest…` The source supports supervised user tests, observed confusing interactions, improvement sprints. Not a comparative ranking.
- **D5** — Huseierne closing asserts the employer *"har vokst forbi styringsformen"*. The ad says growth brought complexity. Employer-state diagnosis stated as fact.

**Repair rule:** never fix incorrectness with blandness. Remove or re-attribute the unsupported element, keep the strongest supported surrounding argument. D1's facilitation bridge survives by citing `PRJ-08`; the durability sentence alone carries adoption.

**Structural cause:** `WRITING_DOCTRINE.md` permitted a separately observed cross-record judgment at `:229-230`, then demanded integration be *"om det bærende caset selv"* at `:235-237`. That contradiction converts a lawful citation into an unlawful absorption. Fix relocates integration from *project history* to *employer argument*.

## Confirmed candidate facts (user-owned, authoritative, 2026-09-06)

- **`i praksis eneste kodende utvikler`** for the 2025 budget modernisation is **correct**. Keep the strong wording; the prior CHECK resolves by confirmation. *(Reverses an earlier recommendation to soften it.)*
- **2027 budgeting tool: modernisation completed with much greater freedom, now in hospital-wide use in the ongoing 2027 process.** `Work §4.3` currently calls it unverified active development. Biggest single change — gives Avinor a two-act arc. **Do not narrate "trust earned"; the cause was not stated.**
- **`PRJ-06` sterile-logistics model completed early 2026 and handed to controllers.** No organisational use, settled weights or realised benefit.
- **Registered "SuperBruker – Kunstig intelligens"** ~3 years; answers technical requests in a Teams channel. No user count, no mandate.
- **English 30-1, Alberta.** No CEFR equivalence.
- **DEFERRED, user must resolve:** "self-developed python repository" for bed-occupancy forecasting vs `Work §4.5`'s recorded distributed authorship (coworker created original XGBoost and much feature/data work). Do not overwrite either attribution.

## Mechanical traps

- **CV employment override FULLY REPLACES** that employment's bullet array. Absent → baseline defaults. Present-empty → renders nothing, does **not** restore defaults. The one rule whose violation yields a valid artifact and a wrong document. It currently lives only in the Stage-2 file being deleted — **must land in Stage 3 before deletion.**
- **ATX headings are load-bearing.** `evidence_index.py` derives the index from headings; every `EV:` id encodes a heading slug. Changing a heading breaks historical references. Edit bodies and rows, keep headings and their order.
- **A section fetch is not recursive.** `evidence_index.py:174-184` ends a section at the next heading, so fetching `W §10` does *not* include `§10.1/§10.2`. Request child ids explicitly.
- **`_reconciliation` (`manifest.py:243-277`) blocks freeze/branch** when live authority hashes differ from those recorded in `CV_BASELINE.md`. After any authority edit: refresh those recorded hashes, then `jobbsok.exe index build`, then branch.
- **`ACC-03`** proves parent immutability by hashing the whole parent tree before/after (`branch.py:181-185`, `:334-348`, compared *before* `staging.rename` at `:357`). Nested child storage must stage outside the ancestor and add only the new destination — never exempt existing branches.
- **Seven schemas constrain `run_id` to a flat `r…` pattern.** A nested branch reference fails schema validation before any `Layout` change matters.
- `MAX_PATH_CHARS = 240`; `render.py:454-545` already budgets and compacts output filenames. Use the render receipt's actual paths, never hardcoded ones.
- `status --json` **writes** `generated/views/…`; `context` writes handoffs and return dirs. `next` and `verify-integrity` are genuinely read-only.
- Both `runb` vacancies are **scanned PDFs, zero extractable text**, `requires_source_inspection = true`. Render pages to inspect. Exclude FINN Kortversjonen, AI-generated skill tags and JobbMatch — they are not employer requirements.

## Facet contract (exact)

`strategy.schema.json` `personality_facets` items, `additionalProperties: false`. Allowed: `facet_id`, `plain_language_label`, `evidence_refs`, `expression_ceiling`, `expression_guardrail`, **`vacancy_relevance`**, `intended_employer_interpretation`, `misread_risk`. Required: first four.

`cli.py:1044-1056` forwards exactly six downstream: `plain_language_label`, `expression_ceiling`, `expression_guardrail`, `vacancy_relevance`, `intended_employer_interpretation`, `misread_risk`. **No `expression_mode` field exists anywhere.** `facet_id` and `evidence_refs` stay in the strategy.

Selection is 0–3 facets; zero is valid. Typology and `PF-` codes never reach employer text.

## Token economics

Static input per two-job run ≈ **556,000** (S1 103.5k, S2 86.4k, S3 88.3k per job). Dominant items: `Work_experience.md` 27.9k and `evidence_index.json` 22.9k, each read by every stage. `evidence_index.json` is ~82% unusable by a model — 144 entries × 524 chars, including a 64-char `content_sha256` each.

`EV:` ids are self-describing slugs, so a bare id list is ~2,400 tokens. The index already stores `line_start`/`line_end`, so a ~30-line `fetch.py` returns verbatim frozen source by id. Output tokens cost ~4–5× input; `strategy.json` ≈ 9,600 output tokens/job of which `role` + `claim_ceiling` ≈ 2,000.

Projected after cut + fetch + digests + context cuts: **≈ 180–210k**.

## Forbidden, permanently

New schemas beyond the migration, enums, semantic validators, preservation fields, drop/survival logs, quality or fit scores, final-vs-strategy comparators, extra semantic stages, second model calls, best-of-N, automatic orchestration, retry frameworks, migration/compatibility layers, monitoring, AI-detector optimisation, Lix/word/paragraph/density targets, knowledge graph, decision/archetype cache, PDF repair as a semantic concern, rolling back `fortsatt i bruk` to `rapportert i bruk`, Build↔Process-v2 mirror divergence or a sync script.

## Frontier

Eight runs. Named comparison parent: **`r20260905-005939-3eeb10`** (retains the two original scanned employer PDFs; both jobs FINAL, render OK; H READY, A CHECK). Baseline `r20260902-210926-0d1af3`. Texture reference `r20260828-213932-7f13b4`. Three post-treatment runs (`114519`, `115243`, `195443`) use *different, text-extractable* vacancy PDFs — corroborating evidence only, never a same-input arm.

Jobs: `avinor_digital_transformasjon`, `huseierne_strategi_maalstyring`, cluster `runb`.

Suite: 247 passed, 10 Word-COM skips. That is mechanical evidence at its own scope — not semantic truth, not `PRODUCTION-MODEL_TESTED`.

## Live plan documents

`P0.9/Process/optimization_0.9.3/`:

- `P0.9.3_FINAL_SEMANTIC_PLAN.md` and `P0.9.3_FINAL_OPERATIONAL_PLAN.md` — **the only implementation authorities.**
- Superseded, do not read: `P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md`, `P0.9.3_CLAUDE_REVIEW_AND_PLAN_DIFF.md`, `User required optimizations.md`, `IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md`, `P0.9.3_CONSOLIDATED_FINAL_INPUT.md`, `FINAL_ITERATION_PROMPT.md`, `FINAL_PLAN_CONSOLIDATION_PROMPT.md`.

## Standing epistemics

Never claim an interview-probability number or measured uplift. Distinguish observed behaviour, inference and editorial judgment. A passing suite, valid JSON, `READY`, or an existing PDF is not evidence of truth. Artifacts cannot prove a prior agent's private read order, edit history or scope authorisation — do not certify those.
