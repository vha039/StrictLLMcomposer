# User work package — context-base review, decisions and questionnaires

Prepared 2026-09-06. Nothing in the repository was modified. This document contains only analysis, decision lists and instructions for other chat instances.

**How to use this document.** §2 gives the measured token economics that justify everything else. §3–§7 are decision lists: read them, mark keep/cut/defer, and return the marked file. §8 is a questionnaire for you to answer so I can finish my own recommendations. §9 contains ready-to-paste briefs for the separate chat instances that will do the fine-tuning work with you. Framework-side engineering recommendations are **not** here — they are in `IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md`, for the finalizing model to adjudicate.

Change-index convention when you return this file: append `[KEEP]`, `[CUT]`, `[DEFER]` or `[EDIT: your note]` to any line. Untouched lines are read as "accept my recommendation."

---

## 1. Scope of what I reviewed

| File | Chars | ≈ Tokens | Read by |
|---|---:|---:|---|
| `authorities/Work_experience.md` | 92,045 | 27,900 | S1, S2, S3 |
| `generated/evidence_index.json` | 75,431 | 22,900 | S1, S2, S3 |
| `context/PERSONALITY_PROFILE.md` | 43,246 | 13,100 | S1 |
| `authorities/Other_high_value_information.md` | 31,785 | 9,600 | S1, S2, S3 |
| `authorities/Education.md` | 25,474 | 7,700 | S1, S2, S3 |
| `policy/writing/WRITING_DOCTRINE.md` | 22,618 | 6,900 | S1, S2, S3 |
| `policy/personality_facets.json` | 15,077 | 4,600 | S1 |
| `policy/stages/stage1…md` | 14,598 | 4,400 | S1 |
| `policy/stages/stage3…md` | 12,015 | 3,600 | S3 |
| `policy/writing/FORFATTERSTEMME.md` | 9,485 | 2,900 | S1, S2, S3 (S1 declared **non-consumer**) |
| `prompts/STAGE3_PROMPT.md` | 9,599 | 2,900 | S3 |
| `policy/stages/stage2…md` | 8,268 | 2,500 | S2 |
| `authorities/CV_BASELINE.md` | 7,294 | 2,200 | via `baseline_map` |
| `generated/baseline_map.json` | 6,972 | 2,100 | S2, S3 |
| `prompts/STAGE2_PROMPT.md` | 6,809 | 2,100 | S2 |
| `policy/writing/PERSUASION_CALIBRATION.md` | 6,001 | 1,800 | S1, S2, S3 |
| `prompts/STAGE1_PROMPT.md` | 5,755 | 1,700 | S1 |

## 2. The measured economics, and the one number that dominates

Static input per job, before the vacancy, upstream artifacts and the model's own output:

| Stage | ≈ Tokens |
|---|---:|
| Stage 1 | 103,500 |
| Stage 2 | 86,400 |
| Stage 3 | 88,300 |
| **Per job** | **278,000** |
| **Per two-job run** | **556,000** |

Three things follow, and the first is much larger than the rest combined.

**2.1 `evidence_index.json` is 22,900 tokens and roughly 82% of it is unusable by a model.** Each of its 144 entries averages 524 characters, carrying `content_sha256` (a 64-character hash the model can do nothing with — 9,216 characters of pure noise across the file), `line_start`, `line_end`, `kind`, and a `source_stated_ids` array. What a writing model actually needs is the evidence id and its heading path, so it can cite correctly. That is roughly 90 characters per entry.

Emitting a slim view in the context bundle — while the full index stays frozen, hashed and authoritative for validation — saves about **19,000 tokens per stage per job, or ~114,000 per two-job run.** It changes no schema, no authority and no instruction. It is transport, which is what `cli.py` already does for every other input.

This single change is worth more than every instruction rewrite in this document combined. It is recommendation **FE-01** in the enhancements file.

**2.2 `Work_experience.md` costs 83,700 tokens per job** because all three stages read all 27,900 of it. About a third is retrieval scaffolding, provenance bookkeeping and pre-written CV prose that the doctrine forbids copying.

**2.3 `FORFATTERSTEMME.md` declares `non_consumer: Stage 1`** in its own front matter, yet the manifest hands all three writing policies to all three stages and folds all three into every stage's governing hash. Two costs: Stage 1 reads 2,900 tokens it is told not to use, and — far more expensively — **a voice-only edit invalidates Stage 1 and forces full regeneration of strategy → draft → final on every job.** That is why the September runs were never a clean A/B, and it makes every future voice iteration cost a complete three-stage rerun. Recommendation **FE-03**.

---

## 3. Proposed cuts — context nuggets I judge non-contributing

These are removal proposals for content that costs tokens in every stage and, as far as I can trace, changes no output. Each line is `[ID] section — reason`. Mark `[KEEP]` on anything you want retained.

### Proposed cut: retrieval scaffolding for a retrieval system that does not exist

- `[W-01]` Work §0.4 *Gjenfinningsindeks*, 19 rows of keyword → section — the model is handed the entire file; it never needs a keyword index to find a section inside its own context.
- `[O-01]` Other §0.4 *Gjenfinningsindeks* — same.
- `[E-01]` Education §0.4 *Gjenfinningsindeks* — same.

### Proposed cut: human source-maintenance bookkeeping the model cannot act on

- `[W-02]` Work §0.6 *Stabil claim-proveniens*, 20 rows of `CLM-*` → evidence-record-ID → owning section — the model cannot resolve a `CLM-` id to anything and never cites one. This is lineage for you and for future source maintenance.
- `[O-02]` Other §0.5 *Stabil claim-proveniens* — same.
- `[E-02]` Education §0.6 *Stabil claim-proveniens* — same.
- `[O-03]` Other §10 *Prioriteringer for sterkere evidens* — a roadmap of future evidence to obtain. Valuable to you, inert to a stage.

### Proposed cut: content the file itself forbids using

- `[O-04]` Other §4.6 *Intern kalibrering* — includes "Never use subjective percentile estimates in public material." Self-assessment that must not reach output.
- `[O-05]` Other §6.7 *Selvledelsesrisiko og mottiltak* — explicitly "Do not present this risk in applications." Its countermeasures ("two to four evidence bridges") also restate policy the doctrine now owns.
- `[P-01]` Personality §5 *Typology Translation Layer* — typology labels are banned from employer-facing text by three separate rules. The layer exists to translate *into* a vocabulary nothing may use.

### Proposed cut: job-search workflow, not pipeline input

- `[O-06]` Other §3.1 *Norsk offentlig sektor og helse* search terms.
- `[O-07]` Other §3.2 *Engelsk og privat sektor* search terms.
- `[O-08]` Other §3.3 *Prioritering av søkeord* — all three help **you** find vacancies. By the time Stage 1 runs, the vacancy is already human-approved and attached. Three stages read them for every job.

### Proposed cut: duplicate compressions of the same content

- `[P-02]` Personality §6 *Canonical Full Source Profile*, 215 lines — the pre-adaptation original. §1 and §3 already carry the same content adapted for this framework.
- `[P-03]` Personality §9 *Compact Machine-Oriented Shorthand* and §10 *Human-Readable Canonical Shorthand*, 20 lines — a third and fourth compression of §1.
- `[P-04]` Personality §2 *Facet Index* and §3 *Facet Cards* — duplicated by `policy/personality_facets.json`, which is a separate frozen input carrying the same facet fields **and** is the machine-validated closed set. Keep the JSON; the prose copy is the redundant one.
- `[P-05]` Personality §8 *Retrieval / Context Index* — same reason as `W-01`.

If `P-02` through `P-05` are all cut, `PERSONALITY_PROFILE.md` reduces from ~604 lines to roughly §0, §1, §4 and §7 — the runtime contract, the canonical compression, the anti-inference index and the handoff contract. That is the part Stage 1 actually reasons with.

### Proposed cut: retired writing prescriptions still live inside factual authorities

These are already flagged as defect **E1** in the P0.9.3 plans. They are listed here because the clean fix is source maintenance, which is yours.

- `[W-03]` Work §0.5 item 5 — *"Bruk høyst to hovedcase i en vanlig søknad."* A retired cap.
- `[W-04]` Work §0.5 item 2 — *"Foretrekk støttet operativ bruk, innføring eller varighet når relevansen ellers er lik."* This is the **global maturity ladder** that `PROOF_FUNCTION_LIFECYCLE` replaced, and the instruction that suppressed the concept-stage judgment `EV:WORK#025` for three consecutive runs. Highest-priority cut in this section.
- `[O-09]` Other §3.4, `GENERALIST_BLUR` correction — *"retain only two main proofs and at most one subordinate differentiator"* — verbatim the differentiator cap deleted from doctrine in P0.9.2.
- `[O-10]` Other §1.4 item 4 — *"at most one subordinate execution/adoption/AI differentiator"* — the same retired cap in a second location.
- `[O-11]` Other §7.1 rows 4–5 — routes package norms and Bokmål voice to `Norwegian_application_text_guide.md` and `Norwegian_language_tone_structure_norms.md`. **Neither file exists anywhere in the repository.** Those domains are now owned by `WRITING_DOCTRINE.md` and `FORFATTERSTEMME.md`.

### Proposed cut: copy-temptation surfaces

- `[W-05]` Work §9.1 and §9.2 `CV_ONLY_STARTING_POINT` — pre-written CV bullets. §9's own preamble says "Never copy these sentences into an application," and the doctrine repeats the ban. They cost tokens *and* create the temptation they warn against. §9.3 (story maps) and §9.4 (bullet rule) are genuinely useful and I propose keeping both.

---

## 4. Proposed reconciliations — merge source → destination

Format: `source → destination`. Content is preserved; one copy is deleted.

### Cross-file duplication inside the authorities

- `[R-01]` Work §3.1 *Standard utvalgsruter* (6 route rows) → Other §1.3 *Rutespesifikk identitetskonstruksjon* — two route tables, same purpose, different vocabulary. Other's version is richer and already carries `do_not_lead_with`.
- `[R-02]` Work §6 *Arbeidsavledet kompetanseprofil* (9 subsections, ~8,000 chars) → Other §8.1 *Kompetansegrupper* — Work §6 restates project facts at competence granularity; Other §8.1 is the compact version the CV actually uses. **Partial merge**: keep any §6 line that states a fact not derivable from §4, cut the rest. This one needs your eye; I have marked it `[FLAG-04]` below rather than proposing a blind cut.
- `[R-03]` Other §2.3 *Spor uten overreach* → Other §2.1/§2.2 "Main caution" columns — the same boundaries stated twice in adjacent sections.
- `[R-04]` Other §7.3 *Ordforråd for bidrag, livsløp og resultat* → `WRITING_DOCTRINE.md § Faktamyndighet og lifecycle-skille` — the lifecycle and outcome vocabularies are already normative in doctrine. The authority copy is a second definition of a controlled vocabulary.
- `[R-05]` Other §7.4 *Trygge transformasjoner* → `PERSUASION_CALIBRATION.md § CLAIM_STRENGTH` — allowed/forbidden transformations are claim-strength calibration, and calibration is where a writer looks for them.

### Instruction duplication inside the policy layer

- `[R-06]` The `INV-07` / "deterministisk kode skal aldri felle en pakke" note appears **four times** across `WRITING_DOCTRINE.md` and `FORFATTERSTEMME.md`. → one statement in `WRITING_DOCTRINE.md § Mål og myndighet`.
- `[R-07]` `WRITING_DOCTRINE.md § Variasjon innenfor en klynge` → is restated in the "Between jobs" section of all three stage instructions. Keep the doctrine section; reduce the stage copies to the mechanical reset action only.
- `[R-08]` The three-authority source map appears in Work §0 preamble, Other §7.1, `WRITING_DOCTRINE.md § Mål og myndighet` **and** `§ Faktamyndighet og lifecycle-skille`. → one copy in doctrine. (The base P0.9.3 plan already proposes removing the fourth; this extends it to the authority copies.)

---

## 5. Flagged for your manual review — I am not confident enough to propose

- `[FLAG-01]` **Education §2, 43 course rows with per-course "safe content ceiling"** (~8,000 chars, read by three stages). Used only when a vacancy states a strict formal criterion, which neither current vacancy does. Options: keep as-is; keep but move behind an explicit "open only for a strict formal criterion" instruction; or reduce to the six courses that carry the master-level method claim. My inclination is the middle option, but it depends on how often you expect strict-criterion vacancies.
- `[FLAG-02]` **Work §4 per-project selection metadata** (10 projects × ~12 fields: `selection_value`, `best_for_roles`, `role_signals`, `employer_problem_signals`, `differentiator`, `adoption_human_change_evidence`, `public_narrative_potential`, `interview_defensibility`, `do_not_lead_with`). Roughly 15,000 characters. Stage 1 now has its own seven-criterion ranking, so much of this is a parallel ranking system. But `do_not_lead_with` and `interview_defensibility` are genuinely load-bearing and I would keep both. Needs a field-by-field decision, not a block cut.
- `[FLAG-03]` **Other §4 (KI-støttet arbeidskompetanse), ~6,000 chars.** Neither current vacancy rewards it, and §4.1 itself says `IDENTITY-AI` is subordinate unless AI is decisive. It is real, differentiating evidence for a narrow class of roles. Keep, but consider whether three stages must read it for every vacancy.
- `[FLAG-04]` **Work §6** — see `[R-02]`. Partial merge, needs your eye on which lines state a non-derivable fact.
- `[FLAG-05]` **Other §2.1/§2.2 role-family tables.** Overlap `[R-01]`'s destination and Work §3.1. Three overlapping route/role systems total. Consolidating all three into one is right; which one survives is a judgment about which vocabulary you find most useful.
- `[FLAG-06]` **Personality §4 *Global Anti-Inference Index***. I propose keeping it — it is the only place the anti-stereotype boundaries live — but it is ~22 lines read only by Stage 1, and `personality_facets.json` carries `misread_risk` per facet. Possible partial overlap.

---

## 6. Enhancement candidates — evidence that would measurably improve the letter

Format `[ID] — "description"`. You fine-tune the exact asks elsewhere; these are the targets, ranked by effect on interview probability.

Most of these are already recorded as unresolved in `Work §10.2` and `Other §9`. The value here is the ranking, not the discovery.

- `[ENH-01]` — "PRJ-04: your individual contribution split, and whether you personally facilitated its adoption (workshops, training, onboarding) or only co-developed the method." **Highest value.** This is the one that converts the D1 defect from a deletion into a re-attribution, and `PRJ-04` is the carrying case in both current letters.
- `[ENH-02]` — "PRJ-03: reconfirm whether 'i praksis eneste kodende utvikler' is accurate for the 2025 modernisation." Removes the only outstanding Avinor `CHECK`.
- `[ENH-03]` — "PRJ-01: approximate user count, report/page scale, or any observed adoption signal for the management dashboard." Currently every scale detail is unresolved, which forces vague wording in the strongest BI evidence.
- `[ENH-04]` — "PRJ-06: current status — has any branch been implemented, weights finalised, or the model handed to controllers since it was designed?" Would move a `CONCEPT` judgment toward `PILOT`/`IMPLEMENTED` and materially strengthen the gevinst argument.
- `[ENH-05]` — "Current role, forward-looking: what are you working on now, and what changed in the last six months?" The authorities are heavy on 2023–2025 and thin on the present, which weakens recency in every opening.
- `[ENH-06]` — "PRJ-02: the unit, the report name, and whether your contribution is still in use." Currently unresolved, which blocks a clean 'bridge to the data organisation' claim.
- `[ENH-07]` — "PRJ-03: status of the 2027 version — delivered, in progress, or paused?" Affects whether the strongest execution case ends on a live or a historical note.
- `[ENH-08]` — "Superuser responsibility: which system, what scope, roughly how many users, over what period." Recorded as unresolved in three places; would add a durable support/enablement claim.
- `[ENH-09]` — "Any measured before/after evidence for any project — time, error rate, cycle time, adoption." Every current claim ends at 'documented capability' because no measurement exists. One real number would materially change several arguments.
- `[ENH-10]` — "English proficiency: is there a test score or standardised level, if a portal demands one?" Low value now; blocks nothing.

---

## 7. Instruction-layer review — necessity, ownership and compression

I applied your four tests to every section of the six instruction files. Full per-instruction tables would be unreadable here; what follows is the set of findings that survived, with the reasoning that produced them.

### 7.1 Instructions that fail the "which stage needs this" test

| Instruction | Currently read by | Actually needed by | Proposal |
|---|---|---|---|
| All of `FORFATTERSTEMME.md` | S1, S2, S3 | S2, S3 | Stage-filter the bundle. The file's own front matter already says `non_consumer: Stage 1`. |
| `D § Tegnsetting` | S1, S2, S3 | S2, S3 | Stage 1 authors no employer-facing prose. |
| `D § Komplett CV-doktrine` + `§ Myke redaksjonelle utgangspunkt` | S1, S2, S3 | S2, S3 (S1 needs only the top-zone category rule) | Keep one sentence in S1's route; the rest is realization. |
| `D § Dyplesningen` | S1, S2, S3 | S2, S3 | Stage 1 allocates; it does not realize depth. |
| `K § MATERIAL_REQUIREMENTS_AND_GAPS` | all three | all three | No change — S1 encodes, S2/S3 realize. Correct as-is. |

Filtering by stage is a `cli.py` transport change, not a policy change. It is recommendation **FE-03**.

### 7.2 Instructions that are necessary but over-expressed

The writing policies are written in discursive Norwegian with substantial rationale. Compression is available, but **not uniformly**, and this is where I want to push back on one of your framings.

You said the files need not be human-readable. That is true for *you*, but models comply measurably better with rules that carry their reason, and the rules in this framework that most often fail are precisely the counterintuitive ones:

- *"Ikke konstruer et svakt andre case"* works because the Presenter's-Paradox sentence explains that readers average rather than sum.
- *"Samlokalisering er ikke integrasjon"* works because it says what happens otherwise — the weakest item gets cut.
- *"Lifecycle bounds what an item may claim; it does not rank it down"* is the fix for a three-run failure and would be ignored as a bare assertion.

So my recommendation is **selective compression**:

- **Compress hard**: procedure, enumerated steps, routing tables, restated boundaries, front-matter provenance prose, and any rule stated more than once. Target register: terse directive, full words, no notation or abbreviation.
- **Preserve**: the rationale attached to counterintuitive rules, and the concrete examples in `K § CLAIM_STRENGTH`.

Estimated effect: 30–40% reduction across `D`/`K`/`V`/`S1`/`S2`/`S3` with no rule loss, versus roughly 55% if rationale is stripped — at a real and unmeasurable cost to output quality, which is priority 1 and ranked far above token cost in `AGENTS.md`'s own optimization order.

**Why I do not recommend notation or abbreviation.** It saves perhaps another 8% and buys three failure modes: you can no longer review the files, I can no longer verify a rule survived an edit, and a near-frontier model asked to follow an abbreviated rule under load tends to reconstruct its meaning rather than obey it. That trade fails MVP-KISS.

### 7.3 Instructions I judge unnecessary

- `[I-01]` The four `INV-07` non-validation notes — see `[R-06]`. No stage builds validators; the note addresses a reader who does not exist in the stage loop.
- `[I-02]` `S1 § Read order` steps 1–2 restate what the context bundle's own ordering already implies. Low value, ~6 lines.
- `[I-03]` Front-matter `provenance` blocks in `D`, `K` and `V` (~30 lines total) are read as content by every stage and describe editorial history no stage acts on.
- `[I-04]` `prompts/README.md` is not routed to any stage and is read only by you. No action needed; noting it so nobody "optimizes" it into the stage path.

### 7.4 Where the base P0.9.3 plan already covers this

The P0.9.3 base plan plus my diff already remove: two overlapping S1 maps, repeated category/lifecycle definitions in S1, the repeated gap paragraph and standalone prohibitions in S2, the replacement/lifecycle/gap redefinitions in S3, and the duplicated three-authority map in D. **Do not schedule those twice.** The work in §7.1–§7.3 above is additive to that plan, not a replacement for it.

---

## 8. Questionnaire for you — return this section marked

Answer format is chosen to minimise your effort: Y/N first, then multiple choice, then multi-select. Pre-filled answers are written as your own words; correct only where wrong.

### Q1 — Context cuts (Y/N)

1. **Q1.1** Cut all three retrieval indexes (`W-01`, `O-01`, `E-01`)? → **Y**
2. **Q1.2** Cut all three claim-provenance maps (`W-02`, `O-02`, `E-02`)? → **Y**
3. **Q1.3** Cut the job-search taxonomy (`O-06`, `O-07`, `O-08`)? → **Y**
4. **Q1.4** Cut the duplicate personality compressions (`P-02`, `P-03`, `P-05`)? → **Y**
5. **Q1.5** Cut the personality facet prose (`P-04`) and keep only `personality_facets.json`? → **Y**
6. **Q1.6** Cut the typology translation layer (`P-01`)? → **Y**
7. **Q1.7** Cut the pre-written CV bullets (`W-05`, §9.1/§9.2) while keeping §9.3 story maps and §9.4 bullet rule? → **Y**
8. **Q1.8** Cut the internal self-calibration sections (`O-04`, `O-05`)? → **Y**
9. **Q1.9** Cut the future-evidence roadmap from the authority file (`O-03`), keeping it as a personal note elsewhere? → **Y**

### Q2 — Retired prescriptions inside the authorities (Y/N)

10. **Q2.1** Remove the retired case caps and maturity ladder (`W-03`, `W-04`, `O-09`, `O-10`)? → **Y**
11. **Q2.2** Fix the dangling routes to the two non-existent guide files (`O-11`) by pointing them at `WRITING_DOCTRINE.md` and `FORFATTERSTEMME.md`? → **Y**
12. **Q2.3** Do you want these done as source maintenance by you, or specified precisely for a chat instance to draft and you to approve? → **Specified for a chat instance to draft; I approve before it lands.**

### Q3 — Instruction compression (multiple choice, pick one)

13. **Q3.1** Compression register for `D`/`K`/`V`/`S1`/`S2`/`S3`:
    - (a) Selective — compress procedure and duplication, preserve rationale for counterintuitive rules. ~30–40% reduction. ← **my recommendation**
    - (b) Aggressive — strip rationale everywhere. ~55% reduction, unmeasured quality risk.
    - (c) Notation/abbreviation. Rejected in §7.2; listed for completeness.
    - (d) None this pass.
    → **(a)**

### Q4 — The caching idea (multiple choice, pick one)

14. **Q4.1** You proposed a central "job archetype → strategy-stage evidence selected" cache. I see two versions with very different risk:
    - (a) **Deterministic evidence digest** — code-generated, non-prescriptive: every record with its lifecycle, ceiling headline and `EV:` id, in one compact table. No history, no decisions, no archetypes. Captures most of the token win with no convergence risk. ← **my recommendation**
    - (b) **Decision cache** — what you described: prior archetype → evidence selected. Real risk: it becomes a de-facto authority, induces convergence across vacancies (the exact failure the employer-swap test and `Variasjon innenfor en klynge` exist to prevent), and `Other §0.3` already forbids using prior applications as candidate evidence. Two vacancies is also far too few to define an archetype.
    - (c) Both — (a) now, (b) revisited after ten or more real vacancies.
    → **(a)**

### Q5 — Enhancement priorities (multi-select)

15. **Q5.1** Which enhancement candidates will you actually answer in the next two weeks? → **ENH-01, ENH-02, ENH-04, ENH-05**
16. **Q5.2** Is `ENH-01` (PRJ-04 facilitation) answerable from memory, or does it need you to check records? → **Answerable from memory.**

### Q6 — Scope and sequencing (multiple choice)

17. **Q6.1** Should the context-file work happen **before** the P0.9.3 semantic implementation, or after?
    - (a) Before — the authorities feed every stage, and `W-04`'s maturity ladder actively fights the new lifecycle rule.
    - (b) After — keep the P0.9.3 treatment comparable to its baseline by holding inputs fixed. ← **my recommendation, with one exception**
    - (c) Split — do only the retired-prescription removals (`Q2`) before, everything else after.
    → **(c)**

    Reasoning for the pre-filled answer: changing the authorities changes every stage's governing hash and would make the planned two-job comparison a multi-variable test. But `W-04` and `O-09`/`O-10` are *actively fighting* the treatment being tested, so leaving them in place biases the experiment against its own hypothesis. The split answer removes the conflicting instructions and holds everything else fixed.

18. **Q6.2** Do you want the framework enhancements in `IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md` adjudicated by the finalizing Codex model, or pre-approved by you first? → **Adjudicated by the finalizing model; I will review its decisions.**

### Q7 — Free text, only where genuinely needed

19. **Q7.1** Anything in §3–§5 you want kept that I proposed cutting, beyond what you marked inline? → *(leave blank if inline marks are complete)*
20. **Q7.2** Any context content you know is missing entirely — a project, a role, a qualification not represented in the three authorities? → *(short answer)*

---

## 9. Briefs for the separate fine-tuning chat instances

Each block is self-contained and ready to paste. They are sequenced; later ones assume earlier ones are done.

### Brief A — Authority source maintenance (retired prescriptions)

> **Task.** Remove retired writing prescriptions from the three candidate factual authorities in `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\authorities\`, without touching any candidate fact, ceiling or boundary.
>
> **Targets, exact:** `Work_experience.md` §0.5 items 2 and 5; `Other_high_value_information.md` §3.4 `GENERALIST_BLUR` row and §1.4 item 4; `Other_high_value_information.md` §7.1 rows 4–5.
>
> **What "optimal" means.** Every factual statement, claim ceiling and prohibition survives byte-identical. Only *writing prescriptions that the P0.9.2 doctrine superseded* are removed, and the two dangling file routes are repointed to `WRITING_DOCTRINE.md` and `FORFATTERSTEMME.md`. The files remain valid inputs: heading structure must not change, because `evidence_index.json` is generated from ATX headings and every `EV:` id encodes its heading path. **Changing a heading breaks every historical evidence reference.** Add no new prescription.
>
> **How to work with the user.** Draft each edit as a before/after pair. Ask only Y/N questions. Pre-fill every answer as the user's own words, never as a guess or suggestion. Do not ask open questions where a Y/N or multiple choice will do.
>
> **Constraint.** These files are protected inputs (`Contract §3`). Present the diff; the user applies it or explicitly authorises you to. Do not regenerate `evidence_index.json` — that is a separate human-invoked maintenance step.

### Brief B — Context-base reduction

> **Task.** Apply the approved cuts and reconciliations from `User clarifications, optimizations, expansions, decisions and other user-work.md` §3 and §4 to the authorities and `context/PERSONALITY_PROFILE.md`.
>
> **What "optimal" means.** Maximum token reduction with zero loss of any candidate fact, ceiling, boundary or unresolved-item record. A cut is correct only if you can state which stage decision would change without it, and the answer is "none."
>
> **Hard constraints.** ATX heading structure is load-bearing — `evidence_index.json` derives from it and `EV:` ids encode heading paths. Prefer removing table rows and paragraphs *within* a section over removing a section. Where a whole section must go, list it explicitly so the user can decide whether to regenerate the index.
>
> **Order.** Personality profile first (largest clean duplication, single-stage impact, lowest risk), then `Other`, then `Education`, then `Work` last and most carefully.
>
> **Reporting.** After each file: before/after character count, the list of removed nuggets by ID, and an explicit statement of what a stage can no longer do.

### Brief C — Instruction compression

> **Task.** Compress `policy/writing/{WRITING_DOCTRINE,PERSUASION_CALIBRATION,FORFATTERSTEMME}.md` and `policy/stages/stage{1,2,3}_*.md`.
>
> **Register.** Terse directive, full words, no notation, no abbreviation. Compress procedure, enumeration, routing tables, front-matter provenance prose and anything stated more than once. **Preserve the rationale attached to counterintuitive rules** — specifically the Presenter's-Paradox ranking argument, the co-location/integration distinction, and the proof-function lifecycle explanation. Models comply better with reasons, and these three rules exist because they previously failed without them.
>
> **Sequencing constraint.** Do this **after** the P0.9.3 semantic implementation lands, never during it. The P0.9.3 plan specifies exact replacement text against exact current wording; compressing first would invalidate every selector in it.
>
> **Verification.** After each file, list every normative rule before and after and prove one-to-one survival. A rule that changed scope, gained a condition or lost a boundary is a defect, not a compression.
>
> **Target.** 30–40% reduction. Do not chase a number past the point where a rule loses its reason.

---

## 10. What I am *not* proposing, and why

- **A knowledge graph over the authorities.** The selection problem is judgment about employer fit, not traversal. A graph adds a build step, a schema, a validator and a new failure mode, and would not have prevented either observed defect.
- **Code writing candidate facts into `strategy.json`.** `evidence_plan[].role` and `claim_ceiling` are per-vacancy judgments, not quotations. Deterministic authorship of semantic fields also breaks `INV-09` stage-scoped write ownership (`paths.py::STAGE_WRITE_MAP`). Detail in `IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md` **FE-07**.
- **A semantic validator for proposition support.** Both observed defects cite a resolvable `EV:` id pointing at a record that genuinely exists; the invented element is a verb and its object. No mechanical check reaches that, and `validate.py:138-166` says so in its own docstring.
- **Cutting `Work §8` (approved metrics) or `§10` (forbidden/unresolved).** These are the ceiling registry. They are the reason the packages are truthful. Keep both verbatim.
