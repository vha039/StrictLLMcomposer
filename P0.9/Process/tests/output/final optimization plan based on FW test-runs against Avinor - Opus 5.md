# Framework post-mortem: weaknesses in the nine Avinor packages, and the optimisation plan

**Scope.** Nine packages (`0d1af3` and `2120b3` excluded). Parts 1 and 2 below were completed
from my own reading of the eighteen documents, the vacancy and the repository **before** the
two prior reports in `output/` were opened. Nothing in the framework, the authorities, the
templates or the generated packages has been modified; this is a proposal.

**Revision note.** `W04b` and `P14` were added after the first issue, at the operator's request,
to cover social-register calibration. They are the only items in this document written with the
prior reports already read; nothing in either report informed them. `P14` is deliberately confined
to the content-locked final polish in Stage 3 and to a file the drafting stages cannot reach —
the reasoning for that constraint is in `P14`'s opening paragraphs and is the single most important
thing about the proposal.

**Paths.** Relative to `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`. `B/` = `P0.9/Build/`.
Line numbers are the files as read on 2026-09-10.

---

## 0. Method

### 0.1 Package identification

| ID | Filename prefix in `cv/` and `soknad/` | Run directory | CV words / letter words | Rendered pages CV / letter |
|---|---|---|---:|---|
| `0fa53b` | `0fa53b_` (no stage suffix) | `r20260908-154257-0fa53b` | 825 / 423 | **3** / 1 |
| `0fa53b-opusx` | `0fa53b_stage3_opusx_20260909T155611Z_` | …`/branches/stage3_opt2_20260909T155611Z` | 714 / 551 | 2 / **2** |
| `0fa53b-solxh` | `0fa53b_stage3_solxh_20260909T155607Z_` | …`/branches/stage3_opt1_20260909T155607Z` | 478 / 374 | ≤2 / 1 |
| `0fa53b-solmed` | `0fa53b_stage3_solmed_20260909T160521Z_` | …`/branches/stage3_solmed_20260909T160521Z` | 461 / 349 | ≤2 / 1 |
| `b5104f` | `b5104f_` | `r20260907-215311-b5104f` | 696 / 428 | 2 / 1 |
| `3eeb10` | `3eeb10_` (no stage suffix) | `r20260905-005939-3eeb10` | 633 / 399 | 2 / 1 |
| `3eeb10-stage1` | `3eeb10_stage1_unknown_20260907T194452Z_` | …`/branches/stage1_unknown_20260907T194452Z` | 698 / 430 | **3** / 1 |
| `6d65bd` | `6d65bd_` | `r20260905-195443-6d65bd` | 499 / 408 | 2 / 1 |
| `93c621` | `93c621_` | `r20260905-115243-93c621` | 438 / 340 | ≤2 / 1 |

Word counts are whitespace-delimited words over all non-empty body paragraphs including the
static CV sections. Page counts are **not** inferred from word count: they are the actual values
in each run's `jobs/avinor_digital_transformasjon/current/render_report.json`, produced by Word
COM at render time. Where a run emitted no page warning the CV is ≤2 and the letter ≤1; the three
bolded values are the runs that emitted one.

Two naming notes, identification only and not policy: the branch directory `stage3_solxh_…`
corresponds to manifest run id `stage3_opt1_…`, and `stage3_opusx_…` to `stage3_opt2_…`. The
DOCX filename prefixes are the stable handle.

One extraction caveat, so nothing below rests on it: a naive XML text dump joins runs across a
tab or a line break, producing artefacts like `HF03.2023` and `hilsenVegard`. Both are correct in
the document — a right-aligned tab stop at 10205 twips and a `<w:br/>` respectively. Neither is a
defect and neither is claimed as one.

### 0.2 What the variants actually isolate

I hashed every file under each run's `frozen/` tree across all eleven runs. Result:

- **`templates/CV_MASTER.docx`, `templates/APPLICATION_MASTER.docx`, `templates/template_map.json`
  and `policy/personality_facets.json` are byte-identical in all eleven runs.** Any defect that
  appears in all nine packages and traces to one of those four files is template-caused with
  certainty, not model variance. This is the strongest causal evidence in the corpus and I lean
  on it hard below.
- **Two policy generations are present in scope.**

| Generation | Packages | Distinguishing marker | `WRITING_DOCTRINE.md` sha | `Work_experience.md` sha |
|---|---|---|---|---|
| **A** (0.9.2) | `3eeb10`, `93c621`, `6d65bd` | `policy/stages/stage2_package_writer.md` present — three-stage pipeline | `5a7c220b` | `0b39a510` |
| **B** (0.9.3) | `3eeb10-stage1`, `b5104f`, `0fa53b`, `-opusx`, `-solxh`, `-solmed` | Stage 2 retired; all three authorities refreshed 2026-09-06 | `78c55890` | `03ebb948` |

- **The four `0fa53b` packages share an identical `frozen/` tree and identical strategies** (bar
  `binding`), and their `personality_facets` selection is `PF-12` + `PF-08` in all four. They
  isolate Stage-3 execution alone, under fixed inputs. One generation per variant is not an
  estimate of a model's expected quality, and the file names alone do not prove which model or
  effort setting ran.
- **`3eeb10` vs `3eeb10-stage1` is not a clean Stage-1 A/B.** Twenty frozen files differ,
  including all three factual authorities. The candidate is the same person; the framework's
  available facts are not the same.

### 0.3 The authority-refresh confound, stated once

Gen B's `Work_experience.md` carries two facts Gen A's does not, both stamped
`bekreftet 2026-09-06`:

- `PRJ-03`: `IN_USE`, *"sykehusdekkende bruk i budsjettprosessene for **2026 og 2027** og
  ferdigstilt 2027-modernisering"*. Gen A's row reads *"2025 version used for 2026 budget;
  broader 2027 redevelopment active"*.
- `PRJ-06`: `COMPLETED`, *"model finished early 2026 and handed over to controllers"*. Gen A's row
  reads *"Architecture supported; implementation/adoption unresolved"*.

So `3eeb10`, `93c621` and `6d65bd` **could not** claim the 2027 process or the handover, and their
"utformet, ikke innført" phrasing was authority-mandated, not editorial timidity. Every comparison
below that touches those two facts is confounded, and I mark it where it bites.

### 0.4 Evidence rules I hold myself to

An absent instruction cannot be quoted. Where a finding is "the framework never says X", I name
the nearest existing text and the precise absence, and "not found" means not found in the files
read, not a proof of absence in every historical copy. Where I can only reach a hypothesis I say
so and name the experiment that would kill it.

### 0.5 What is not broken, recorded so the plan does not touch it

- **Punctuation doctrine holds.** `WRITING_DOCTRINE.md:390-397` bans `–` and `—` in
  employer-facing text. Across all eighteen documents: **zero** en dashes, **zero** em dashes.
  Semicolons appear five times in eighteen documents, consistent with *"bør være uvanlig"*.
- **Zero leakage.** No `EV:`, `BL:`, `EMP_` or `PF-` reference, internal path, template tag or
  review content appears in any employer-facing text.
- **Zero fabrications.** I checked every single-occurrence specific in the corpus against that
  run's own frozen `Work_experience.md`. All are verbatim-supported. Details are in the companion
  rankings document; the point for this plan is that **credibility is not the failing axis**, so
  no proposal below spends budget on it.

---

## Part 1 — Weakness catalogue, worst first

Each entry: the weakness, the evidence in the documents, the causing element in the repository,
and confidence. Causation is given as a **negative contribution that exists** — an instruction,
constraint, example, weighting, schema field, template slot or code path that produces the flaw —
and/or an **absent positive contribution**: what would have prevented it and is not there.

---

### W01 — Requirement coverage is computed at Stage 1 and then thrown away at the stage boundary

**Weakness.** The framework knows exactly what the vacancy asks for, rates the candidate's
relation to each requirement, and then ships a package that never mentions several requirements it
rated as *supported*.

**Evidence in the documents.**
`B/runs/r20260908-154257-0fa53b/jobs/avinor_digital_transformasjon/current/strategy.json`,
`material_requirements`, rates:

| id | text | importance | relation |
|---|---|---|---|
| `R10` | "Utarbeide analyser, beslutningsgrunnlag og presentasjoner for ledelse og styringsgrupper." | IMPORTANT | **SUPPORTED** |
| `R13` | "Erfaring med utvikling av styringsmodeller, beslutningsprosesser eller porteføljestyring er en fordel." | DESIRED | **SUPPORTED** |
| `R14` | "Meget gode skriftlige og muntlige kommunikasjonsevner på norsk og engelsk." | IMPORTANT | **SUPPORTED** |

Counts across all eighteen documents:

| term | occurrences | vacancy uses it |
|---|---:|---:|
| `målbar` | **0** | 1 — the first responsibility bullet |
| `kommunikasjon` | **0** | 2 |
| `beslutningsfora` | **0** | 1 |
| `endringsledelse` | **0** | 1 |
| `bærekraft` | **0** | 2 |
| `styringsgrupp` | **1** — `3eeb10` CV | 1 |
| `portefølje` | **1** — `0fa53b-solmed` letter, inside a disclaimer | 2 |

`engelsk` appears only in the template-rendered `SPRÅK` block, never in model-authored text. The
single positive `styringsgrupp` hit is `3eeb10`'s competency line *"Beslutningsgrunnlag, analyser
og presentasjoner for ledelse og styringsgrupper"* — the ad's own words, asserted in a list, with
no bullet beneath it that evidences the activity.

The evidence exists. `B/authorities/Work_experience.md` §6.9 *Kommunikasjon og interessentarbeid*
lists "Executive/management decision support", "Analytical reports, decision notes and technical
documentation", "Workshops/presentations for mixed audiences". §5.2 lists "Translates
technical/economic context into decision notes, executive summaries, workshops, documentation and
onboarding. Adapts communication to controllers, managers, specialists and technical teams." None
of it reaches employer text in any of the nine packages.

**Causing element — negative.** `B/policy/stages/stage3_final_writer_review.md:54` carries the
entire duty in one clause: *"Address material requirements and gaps truthfully, build specific
motivation, and remove repetition…"*. Nothing downstream can tell whether it happened.

**Causing element — absent.** `B/schemas/package.schema.json:61-97` gives the final package
exactly four CV fields — `headline`, `profile`, `competencies`, `employment_overrides` — and three
letter fields, and **no requirement-coverage field of any kind**. `material_requirements` is a
Stage-1 artefact with `minItems: 1` and a deliberate absence of `maxItems`
(`B/schemas/strategy.schema.json`: *"no hard cap may truncate a material employer requirement"*),
and it has no consumer contract at Stage 3. The requirement list is produced with care and read as
prose.

**Confidence: high.** The gap is arithmetic, not interpretive.

---

### W02 — Vacancy vocabulary is actively pruned, and the models know they are doing it

**Weakness.** The framework treats the employer's own words as the *first* thing to delete, so
requirements survive only when the candidate happens to have a word of his own for them.

**Evidence in the documents.** `3eeb10`'s own `review.json`, `known_limitations`:

> "Porteføljestyring er ikke dokumentert og **ordet er ikke brukt**. Annonsens to punkter der det
> inngår er eller-krav der gevinstrealisering og virksomhetsstyring dekker kravet."

That is a deliberate lexical suppression, recorded by the stage that performed it. The pattern
holds elsewhere: `6d65bd`'s review records that it rejected an Avinor analogy (W12); `93c621`'s
records that the budget tool is *"omtalt som brukt i 2026-prosessen"* and nothing more.

**Causing element — negative, three reinforcing.**

1. `B/policy/writing/WRITING_DOCTRINE.md:475` — *Erstatnings- og komprimeringsrekkefølge*, item 1:
   *"gjengivelse av annonsen og generisk ros"*. The employer's vocabulary is ranked **first** on
   the deletion list, above self-grading, above chronology, above the weakest supporting example.
2. `B/policy/writing/WRITING_DOCTRINE.md:445` — *"Ikke overkorriger med ukritisk annonseekko."*
3. `B/policy/writing/PERSUASION_CALIBRATION.md:128` — *"Bruk arbeidsgiverens substansielle
   vokabular bare der det er dekket."* Correct in principle, but with W01's coverage check absent
   there is no counter-pressure, so *"bare der det er dekket"* collapses into *"sjelden"*.

**Causing element — absent.** No rule anywhere distinguishes *parroting* — reciting the ad's
aspiration back at the employer — from *addressing*: using the employer's term for a capability
the candidate demonstrably has. `Arbeidsgiverbyttetesten` (`:431-455`) tests for the first and is
silent on the second.

**Confidence: high.** Attested by the framework's own review artefacts.

---

### W03 — Three of nine packages breach the page budget, and the measurement arrives after the only stage that could act on it

**Weakness.** The most visible recruiter-facing property of the whole product — does the CV fit
two pages and the letter one — is measured, found failing, and shipped `READY`.

**Evidence in the documents.** From `render_report.json` in each run:

- `0fa53b` — *"CV rendered to 3 pages; editorial target is <=2. Review signal only."* Triage: `READY`.
- `3eeb10-stage1` — *"CV rendered to 3 pages; editorial target is <=2. Review signal only."* Triage: `READY`.
- `0fa53b-opusx` — *"Letter rendered to 2 pages; editorial target is <=1. Review signal only."* Triage: `READY`.

`0fa53b`'s review shows the loop was attempted and failed:

> "CV-en er komprimert etter at en første rendering ga tre sider mot det redaksjonelle målet på to.
> … **Kontroller sidetallet i den rendrede CV-en.** Er den fortsatt over to sider, kort ned punktet
> om prognosearbeid og KI før punktene om gevinst og gjennomføring røres."

There are two Stage-3 handoffs for that job — `stage3-0bc1aa4651607e51` and
`stage3-56ffa3555052a149`. The model compressed, resubmitted, and the CV is **still three pages**.
It then delegated the re-check to the human, in the review, as an instruction.

**Causing element — negative.** `B/prompts/STAGE3_PROMPT.md:112-116` puts `finalize` and `render`
**after** a successful submission: *"Immediately after a successful submission, for that same job:
… finalize … render"*. `B/policy/stages/stage3_final_writer_review.md:176-177` repeats it. The page
count is therefore structurally unavailable to the model at the moment it chooses content and
triage.

**Causing element — negative, reinforcing.** `B/policy/settings.toml:72-79` defines
`cv_expected_max_pages = 2` and `letter_expected_max_pages = 1` under `[render.soft_warnings]`,
prefaced by *"editorial signals only. These emit WARNING and never fail a command."*
`B/policy/writing/WRITING_DOCTRINE.md:331-342` makes the same guarantee doctrinally —
*"Deterministisk validering skal aldri felle en pakke for å avvike fra dem"*, and *"Et dokument
feiler mekanisk bare når det er ubrukelig, korrupt, avklippet eller bryter en verifisert teknisk
grense."* A three-page CV is none of those things.

**Causing element — negative, third order.** `B/policy/settings.toml:70` sets
`pdf_required = false`, and the page count comes from the PDF. If the converter degrades,
`page_count is None` and `B/runtime/jobbsok/render.py:296-305` returns no warning at all — the only
length signal in the system is optional.

**Causing element — absent.** No triage row in
`B/policy/stages/stage3_final_writer_review.md:110-114` mentions document length; nothing makes
overrun a `CHECK` trigger; no `known_limitations` convention flags it.

**Confidence: high.** The chain is fully observable in artefacts.

---

### W04 — The letters volunteer disqualifications on requirements the ad marks as desirable

**Weakness.** Four of nine letters contain a sentence whose only job is to tell Avinor what the
candidate does not have. Three name a requirement the ad lists as a preference rather than a
minimum, and two use the ad's own noun to do it.

**Evidence in the documents.**

- `0fa53b-solmed`: *"Rollen min har vært prosjekt- og metodeorientert, ikke et formelt konsernmandat
  for portefølje- eller programledelse."* — the topic sentence of paragraph four. The ad's R13 is
  `DESIRED` ("er en fordel"); this converts it into a stated gap, in the candidate's own voice,
  using the ad's word `portefølje`.
- `0fa53b-solxh`: *"Min påvirkning har i hovedsak vært funksjonell, gjennom struktur, faglige
  vurderinger og leveranser, ikke gjennom linje- eller programmyndighet."*
- `0fa53b`: *"Målt tidsbesparelse eller feilreduksjon har jeg ikke tall på. Det som er dokumentert,
  er at verktøyet er i bruk."* — placed at the end of the delivery paragraph, so the ad's **first**
  responsibility bullet, *"Sikre at digitale initiativer gir målbar verdi"*, is answered with a
  negation first and the recovery second.
- `0fa53b-opusx`: *"Hvilke gevinster som siden er realisert, kan jeg ikke svare for."* — better
  placed, and immediately recovered by *"Det modellen gjør, er å vise hva anslagene hviler på."*

`b5104f` is the only letter with no self-negation at all. Its limits sit in CV phrasing — *"dels
innført og dels foreslått"*, *"brukt på prosjektnivå"*, *"Kolleger ledet innhold og visuell
utforming"* — and in `review.json`, which is where the framework's own policy says they belong.

**Causing element — negative.** `B/policy/writing/PERSUASION_CALIBRATION.md:129` states the right
rule at the wrong granularity: *"Unngå et defensivt «jeg mangler X»-**avsnitt** med mindre taushet
ville villede vesentlig."* The unit is a paragraph. Every instance above is a clause or sentence
**inside** an otherwise positive paragraph, so all four are literally compliant.

**Causing element — negative, second.** `B/authorities/Other_high_value_information.md:247` holds
exactly the right instruction — `ACCOUNTING_DEFICIT_FRAME`, correction column: *"…keep
non-disqualifying caveat **review-only**"* — but its Trigger column binds it to a single domain:
*"Adjacent **finance** evidence is introduced through what Vegard lacks"*. There is no
`MANDATE_DEFICIT_FRAME`, `PORTFOLIO_DEFICIT_FRAME` or `AUTHORITY_DEFICIT_FRAME` row, so the channel
rule never fires for the deficit that actually recurs.

**Causing element — negative, third.** `B/authorities/Other_high_value_information.md:246`,
`LEADERSHIP_INFLATION`, corrects upward inflation only — *"Functional coordination becomes formal
leader/manager title → Use evidence-based functional leadership wording"*. It has no floor, so
`solxh`'s explicit *"ikke gjennom linje- eller programmyndighet"* is an over-application of an
anti-inflation rule with nothing pushing back.

**Causing element — absent.** Nothing anywhere distinguishes the *cost* of different concessions.
`3eeb10-stage1`'s *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg
ingen bakgrunn."* is nearly free — the recruiter already knows, and naming it buys trust. A
disclaimer about a `DESIRED` requirement is not free: it hands the screener a reason. No policy
surface encodes that asymmetry.

**Confidence: high.**

---

### W04b — The ceiling half of W04: nothing measures or tunes social register, and the one pass that could is unnamed, unbounded and unrecorded

W04 is the **floor** failure — packages talk themselves down. This is the **ceiling** failure on the
same axis: nothing in the framework detects, bounds or tunes the specific constructions that make an
otherwise truthful Norwegian application read as self-important. The two share one dial and the
framework has no instrument on it in either direction.

**Weakness.** The framework states the target impression and provides no way to check whether it was
hit, no way to adjust how hard to push, and no record of what the pass did.

**Evidence in the documents.** I scored all nine letters on three dimensions: *selvhøytidelighet*
(the framework's own term), Janteloven violation, and Norwegian professional-culture dis-alignment.
Low is good; the composite is the unweighted mean.

| Package | Self-impressedness | Janteloven | Culture dis-alignment | Composite |
|---|---:|---:|---:|---:|
| `3eeb10-stage1` | 14 | 8 | 14 | **12** |
| `3eeb10` | 16 | 12 | 18 | **15** |
| `b5104f` | 30 | 20 | 22 | **24** |
| `0fa53b-solmed` | 20 | 10 | 44 | **25** |
| `0fa53b` | 34 | 26 | 34 | **31** |
| `6d65bd` | 44 | 32 | 42 | **39** |
| `0fa53b-solxh` | 48 | 36 | 46 | **43** |
| `0fa53b-opusx` | 58 | 30 | 52 | **47** |
| `93c621` | 62 | 58 | 64 | **61** |

Two readings matter for the design of the fix.

**The dimension is two-sided.** `0fa53b-solmed` is third-best on self-impressedness and best-but-one
on Janteloven, and second-worst on register — because *"Rollen min har vært prosjekt- og
metodeorientert, ikke et formelt konsernmandat for portefølje- eller programledelse"* is through the
floor, not over the ceiling. Any mechanism that only measures boastfulness will score
self-disqualification as a virtue. That is precisely the failure this catalogue's W04 documents, and
it is why the fix must carry an invariant floor rather than a single direction of travel.

**The two ends are jointly achievable.** `b5104f` (24) and `3eeb10-stage1` (12) are the two
best-covered packages in the corpus *and* two of the three least self-impressed. There is no inherent
trade-off between presenting the candidate as qualified and staying inside Norwegian register — the
spread is execution, not physics.

Ten recurring markers, all corpus-observed:

| ID | Marker | Observed |
|---|---|---|
| M1 | Defining the employer's own mandate before establishing standing | `93c621`: *"Avinors nye transformasjonsmiljø skal gjøre mer enn å foreslå teknologi: Det skal gi ledelsen grunnlag for å prioritere…"* |
| M2 | Exact-fit claim, especially to a definition just supplied | `93c621`: *"har jeg arbeidet med **nettopp** koblingen mellom verdipåstander, tekniske valg og gjennomføring"* |
| M3 | Employer-as-venue — their task framed as a use of him | `93c621`: *"…til en meningsfull neste anvendelse av erfaringen min"* |
| M4 | Self-ranking of own evidence | `0fa53b-opusx`: *"Det er den formen for gevinstarbeid jeg kjenner best"* |
| M5 | Announced abstraction as the organising device | `0fa53b-opusx`: *"arbeidet mitt har i hovedsak dreid seg om to spørsmål"* |
| M6 | Standing self-characterisation | `6d65bd`: *"Mitt bidrag er å gjøre behov og forutsetninger tydelige…"*, *"Gevinstarbeidet mitt omfatter…"* |
| M7 | Relevance bridge rebuilt more than once | `0fa53b-solxh`: three separate *"For Avinor … er dette relevant"* constructions |
| M8 | Stacked closing morals | `93c621`: *"Erfaringen har lært meg at endring i kritiske arbeidsprosesser må være både mulig å ta i bruk og mulig å kontrollere."* |
| M9 | Subject monotony | `6d65bd`: four `Jeg`-initial sentences in one paragraph, three consecutive |
| M10 | Instrument overrun | `0fa53b-opusx`: 551 words across two pages for a one-page instrument |

**Causing element — negative.** `B/policy/writing/FORFATTERSTEMME.md:94-123`,
*§ Selvfremstilling som skal bort*, names exactly three of these — M4, M5 and M8 — and the corpus
duly shows the other seven surviving. `§ Mønstre som skal erstattes` (`:125-143`) names five more,
but lexically, and W16 shows what happens to a lexical rule: it gets paraphrased around.

**Causing element — negative, second, and it is the same class as W06.** M3's wording is lifted from
the doctrine. `B/policy/writing/WRITING_DOCTRINE.md:229`: *"Motivasjon skal forklare hvorfor akkurat
dette arbeidet er **en meningsfull neste bruk av kandidatens erfaring**."* `93c621` ships *"en
meningsfull neste anvendelse av erfaringen min."* The doctrine's sentence is written *about* the
candidate, from the system's point of view; transposed into first person it inverts who the sentence
serves, and that inversion is exactly what makes it read as self-centred. The framework taught the
model the phrase and the perspective flip did the damage.

**Causing element — absent, four things.**

1. **No diagnostic.** `B/policy/stages/stage3_final_writer_review.md:156-160` states the target —
   *"Express the locked content so a Norwegian hiring manager is likely to experience the writer as
   competent, grounded, useful, interesting, credible and easy to work with, rather than
   impressive-seeking, intense or self-conscious"* — and gives the writer nothing to check itself
   against. There is no marker inventory anywhere.
2. **No tunable intensity.** The pass is a single fixed instruction. There is no setting, so the
   trade-off between assertiveness and social conformity cannot be moved without editing policy, and
   two runs cannot be compared at different settings.
3. **No record.** `schemas/review.schema.json` carries `material_strategy_change` and
   `upstream_claim_repaired` as optional diagnostics precisely so the pilot can see what a stage did
   (`stage3_final_writer_review.md:125-127`). Nothing equivalent exists for the polish pass, so a
   human cannot tell whether it fired, did nothing, or over-fired into W04 territory.
4. **The floor is stated but not bound to the instrument.** `stage3_final_writer_review.md:168-171`
   already says the right thing — *"Do not solve self-importance by weakening owned accomplishments.
   Adding hedges, softening work verbs, introducing self-deprecation or replacing `jeg` with a vague
   `vi` all damage the register this pass exists to protect."* But it is a free-standing warning, not
   a property of a calibrated mechanism, so there is nothing that guarantees *turning the pass up can
   never turn the claims down*.

**Confidence: high** for the markers and their causes; **medium** for the claim that a named,
levelled inventory fixes them — that is P14's bet, and its next-run signal is written to falsify it.

---

### W05 — Lifecycle honesty is mandated with no channel rule, so audit limits land in CV bullets

**Weakness.** CV bullets end on what the work did *not* achieve.

**Evidence in the documents.**

- `0fa53b` CV: *"Eide løsningen fra om lag august 2025 til februar 2026 … **Løsningen ble avviklet
  i februar 2026.**"* — the terminal clause of the flagship BI bullet.
- `3eeb10-stage1` CV: *"Løsningen ble avviklet i februar 2026."*
- `b5104f` CV: *"Eide løsningen fra ca. august 2025 til februar 2026, da den ble avviklet."*
- `6d65bd` CV: *"Arbeidet dokumenterer modelldesign, ikke innføring eller realisert gevinst."*
- `3eeb10` CV: *"Modellen er utformet; innføring og endelige vekter er ikke avklart."*
- `93c621` CV: *"modellen er utformet, ikke innført."*

**Causing element — negative.** `B/authorities/Work_experience.md:932-945`, §9.3
*Intervjuforsvarlige historiekart*, is the richest raw material in the authority: an eight-row
table with columns `Story | Problem | Personal contribution | Control/proof | Status/value |
**Limit**`. Every row's `Limit` cell is a negative — *"no quantified impact"*, *"no quantified
efficiency"*, *"Implementation/adoption/benefits unresolved"*, *"no quantified saving"*, *"no
generalized accuracy"*. The column carries **no channel marking**. It is not tagged `REVIEW_ONLY`,
`INTERNAL_ONLY` or anything else, and it sits in the same row a writer reads to build the bullet.

**Causing element — negative, second.** `B/policy/writing/WRITING_DOCTRINE.md:359-367` requires
distinguishing seven lifecycle states, `DECOMMISSIONED` among them, and
`B/policy/writing/PERSUASION_CALIBRATION.md:108-109` says *"Planlagt, utforskende, pilot, aktiv
utvikling, implementert, i bruk, fullført og avviklet er ulike tilstander. Bruk verb som
samsvarer."* Correct, and it produces *"avviklet"* faithfully.

**Causing element — absent.** Nothing says a `DECOMMISSIONED` artefact's *build* achievement may be
presented without terminating on the end state, or that an item whose only honest framing is a
negation may simply be omitted from the CV and kept for interview. `Intervjureserve`
(`WRITING_DOCTRINE.md:282-287`) exists for exactly this shape of decision and is scoped to
*"detaljer som viser dybde, men som ville fortrenge toppsignal"* — depth, not liability.

**Confidence: high.**

---

### W06 — A worked example in the calibration policy became the corpus's stock phrase

**Weakness.** The single most repeated sentence in the corpus is a policy template.

**Evidence.** `B/policy/writing/PERSUASION_CALIBRATION.md:65-72`:

```text
Mønstereksempel, med generisk innhold. …
riktig:      «… ble innført som Y-standard og var fortsatt i bruk om lag N år senere.»
```

Shipped, near-verbatim, in **eight of nine packages, in both documents**:

- `0fa53b` CV **and** letter, identical: *"Rammeverket ble innført som sykehusdekkende standard og
  var fortsatt i bruk om lag to og et halvt år senere."*
- `0fa53b-opusx` CV **and** letter, identical, with `2,5` for the numeral.
- `3eeb10` CV **and** letter, identical.
- `3eeb10-stage1`, `6d65bd`, `93c621`, `b5104f`, `0fa53b-solmed`: same frame, minor variation.

**Causing element — negative.** The example is labelled *"med generisk innhold"* — generic
*content*. Its **syntax** is not marked as illustrative, so it was copied as a form. The
surrounding section is about claim strength, not phrasing, but it is the only fully written-out
sentence in the three writing-policy files, which makes it the most concrete phrasing signal
available to a writer.

**Causing element — absent.** No line in `PERSUASION_CALIBRATION.md`, `WRITING_DOCTRINE.md` or
`FORFATTERSTEMME.md` says examples are calibration and not phrasing to reuse.

**Confidence: high.** Eight of nine, both documents, near-verbatim, matching a template that
exists in exactly one place.

---

### W07 — Every package duplicates a formulation across CV and letter; four duplicate a sentence verbatim

**Weakness.** The doctrine's complementarity rule is violated by 9 of 9 packages.

**Evidence.** Sentence-level similarity between CV prose and letter prose, per package, at ≥0.80:

| package | pairs ≥0.80 | worst pair |
|---|---:|---|
| `0fa53b` | 1 | **1.00** — *"Rammeverket ble innført som sykehusdekkende standard og var fortsatt i bruk om lag to og et halvt år senere."* |
| `0fa53b-opusx` | 2 | **1.00** — same sentence with `2,5`; plus 0.99 on the STE handover |
| `b5104f` | 2 | **1.00** — *"Verktøyet er i sykehusdekkende bruk i budsjettprosessene for 2026 og 2027."* |
| `3eeb10` | 2 | **1.00** — same standard sentence; plus 0.83 profile↔opening |
| `0fa53b-solxh` | 1 | 0.98 |
| `0fa53b-solmed` | 1 | 0.95 |
| `3eeb10-stage1` | 2 | 0.93 |
| `6d65bd` | 1 | 0.93 |
| `93c621` | 1 | 0.86 |

**Causing element — negative.** Nothing produces it; the failure is a missing check against an
explicit rule.

**Causing element — absent.** `B/policy/writing/WRITING_DOCTRINE.md:291-293` states the rule —
*"Søknaden skal ikke gjenfortelle et helt CV-punkt bare for å innføre sin egen tolkning av det, og
**samme argument skal ikke ha samme formulering i begge dokumenter**"* — and no step anywhere
compares the two documents. Stage 3 authors both in one pass, so it is uniquely able to check, and
`B/policy/stages/stage3_final_writer_review.md:41-72` never asks it to. The `Sequence` block's
step 5 says only *"remove repetition that adds neither a new function nor useful detail"*, which
reads as within-document repetition.

Note for Part 2: `WRITING_DOCTRINE.md:496-498` explicitly forbids building an automatic similarity
detector — *"det finnes ingen automatisk likhetsdetektor i baseline, og det skal ikke bygges en
(Spec 3, Contract 22)"*. That constrains the fix to an authoring duty, which is the correct place
for it anyway.

**Confidence: high.**

---

### W08 — `KJERNEOMRÅDER` renders as a single bold block of up to 81 words in all nine CVs

**Weakness.** The CV's second-most-prominent zone is an unbroken wall of 12-point bold navy text.

**Evidence.** In all nine CVs the entire control content — the label plus every competency — is one
`<w:r>` carrying `<w:b/>`:

| package | words in the single bold run |
|---|---:|
| `0fa53b-opusx` | 81 |
| `0fa53b` | 78 |
| `3eeb10` | 74 |
| `b5104f` | 52 |
| `93c621` | 41 |
| `0fa53b-solxh` | 40 |
| `0fa53b-solmed` | 38 |
| `6d65bd` | 31 |

(`3eeb10-stage1` likewise.) Rendered, `0fa53b`: *"KJERNEOMRÅDER  Gevinstrealisering: metodikk,
estimering og standardisering · Beslutningsgrunnlag og investeringsvurdering under svakt
datagrunnlag · …"* — all bold, one paragraph.

**Causing element — negative, a three-link chain.**

1. `B/templates/template_map.json:48-55` — `CV_CORE_COMPETENCE` declares
   `"transform": "join_middot"` and `"prefix": "KJERNEOMRÅDER  "`. The label is part of the *text*,
   not a separate run.
2. `B/runtime/jobbsok/render.py:155-156` —
   `return block([prefix + " · ".join(items)] if items else [])`. One string, one paragraph.
3. `B/runtime/jobbsok/docxfill.py:176-185` — `_set_paragraph_text` deep-copies the *first* template
   run and reuses its `rPr` for the whole text:
   `run = copy.deepcopy(template_run) …; _set_run_text(run, text)`. The master's placeholder run is
   bold because the label is bold, so the payload inherits it.

`template_map.json` is byte-identical in all eleven runs, so this is not model variance under any
reading.

**Confidence: high.**

---

### W09 — The letter names the role three times in its first three lines

**Weakness.** Before the first sentence of argument, the reader has been told the job title twice
by the template and, in four of nine letters, a third time by the model.

**Evidence.** Every letter opens:

```text
Avinor AS
Digital Transformasjon                                    Oslo, 8. september 2026
Stilling: Seniorrådgiver Digital Transformasjon
Søknad: Seniorrådgiver Digital Transformasjon
```

Then `0fa53b-opusx`: *"Jeg søker stillingen som seniorrådgiver i Digital Transformasjon."* Also
`3eeb10`, `3eeb10-stage1` and, in variant form, `0fa53b-solmed`. `0fa53b-opusx` spends the letter's
highest-value sentence on the fourth restatement of a fact already stated three times above it.

**Causing element — negative.** `B/templates/template_map.json:200-206`:

```json
"APP_JOB_TITLE": { "kind": "inline", "count": 2, "source": "job.title", "required": true,
  "note": "Appears twice in the master: the reference block and the subject line. Both are filled." }
```

Documented as deliberate. The second row of the two-column header table also has an empty right
cell (`<w:p />`), so the `Stilling:` line occupies a half-empty row directly above a `Title`-styled
paragraph that repeats it.

**Causing element — absent.** No instruction tells the writer that the subject line already exists,
so an opening that restates it is redundant. `FORFATTERSTEMME.md:139-141` bans one kind of weak
opening but not this one.

**Confidence: high.**

---

### W10 — About twelve lines of 2013–2020 low-relevance CV furniture that no stage can remove

**Weakness.** Every CV ends with four fixed sections that cost roughly a sixth of a page and carry
almost nothing for this vacancy, while `porteføljestyring` and `kommunikasjon` get zero words (W01).

**Evidence.** Identical in all nine CVs:

```text
KURS               Sanitet nivå 2, 04.2014.
REFERANSER         Oppgis ved forespørsel.
TIDLIGERE ERFARING 07.2015-08.2021 Hjelpearbeider, TKS Heis …
                   02.2015-04.2015 Butikkmedarbeider/vikar, Ahlsell …
                   03.2014-02.2015 Vakt- og sikringssoldat, Luftforsvaret …
                   10.2013-03.2014 Sikkerhetskonsulent, Sector Alarm …
TILLITSVERV        Styremedlem/beboerrepresentant … 10.2017-01.2019.
                   Økonomiansvarlig og nestleder, 01.2019-01.2020.
                   Styreleder og økonomiansvarlig, 01.2020-08.2020.
SPRÅK              Norsk: Morsmål / Engelsk: Flytende skriftlig og muntlig
```

This matters most for `0fa53b` and `3eeb10-stage1`, whose CVs run to three pages: part of the
overflow is content no stage authored and no stage may drop.

**Causing element — negative.** `B/templates/template_map.json:98-135` binds
`CV_SUPPORT_SECTION_1` → `baseline.sections[OTHER_COURSES]`, `CV_SUPPORT_SECTION_2` →
`baseline.references_text`, `CV_OPTIONAL_PREVIOUS_EXPERIENCE` → `effective.previous_employments`,
`CV_OPTIONAL_TRUST` → `baseline.sections[OTHER_TRUST]`, `CV_OPTIONAL_LANGUAGES` →
`baseline.languages`. All are `"required": false`, and `fill_block` documents that an empty list
clears a control — but the source is a static baseline lookup with no decision input.

**Causing element — absent.** `B/schemas/package.schema.json:61-97` gives the CV four writable
fields. `B/policy/stages/stage3_final_writer_review.md:77-78` states the ceiling plainly: *"Write
all four dynamic zones: headline, profile, competencies and employment_overrides."* There is no
`include_support_sections`, no per-section relevance flag, no way for any stage to say that a
door-to-door alarm-sales role from 2013 is not worth four lines on a seniorrådgiver CV.
`B/authorities/Other_high_value_information.md:78` even states the intended rule — *"Brukes når
stillingen belønner ansvar, styring, sikkerhet, representasjon eller tidlig lederskap; **utelates
når plassen er mer verdt for nåværende faglig evidens**"* — and no mechanism exists to act on it.

**Confidence: high.**

---

### W11 — Five live content controls in the masters are wired to nothing, including a whole "selected evidence" section

**Weakness.** The CV master contains a structural slot that would carry vacancy-specific evidence,
and it is switched off.

**Evidence.** `CV_MASTER.docx` carries 17 SDTs. Five are dead in the map: `CV_VALUE_PROPOSITION`
(`B/templates/template_map.json:36`), `CV_TOOLS_METHODS` (`:56`), `CV_SELECTED_EVIDENCE_HEADING`
(`:68`), `CV_SELECTED_EVIDENCE` (`:74`), `CV_SUPPORT_SECTION_3` (`:111`) — each `"source": "none"`.

`CV_SELECTED_EVIDENCE` plus its heading is the exact shape W01 needs: a short, model-authored,
vacancy-selected evidence block sitting above the chronology, where a recruiter reading for
`porteføljestyring`, `styringsmodeller` or `beslutningsgrunnlag for ledelse` would find it.

**Causing element — negative.** The `"source": "none"` bindings, plus the absence of a
corresponding field in `package.schema.json`.

**Confidence: high.**

---

### W12 — Employer facts are not usable as rhetoric, and a model can be seen deciding so

**Weakness.** Eight of nine letters contain no fact about Avinor. The strongest analogy available
in the vacancy — the **Avinormodellen**, where the large airports cross-subsidise the small ones,
which is structurally the same problem as Vegard's weighted proxy allocation of benefits between
clinics — is used by nobody.

**Evidence.** Avinor-specific facts in the nine letter bodies:

| package | employer fact used |
|---|---|
| `b5104f` | *"Avinor driver 43 lufthavner og flysikringstjenesten, og den nye enheten skal øke gjennomføringskraften i noe som allerede må virke hver dag."* |
| `3eeb10-stage1` | *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn."* — a fact used as a negation |
| the other seven | none |

`3eeb10`'s letter body **never writes the word "Avinor" at all** — the only occurrence in the file
is the template-filled address block.

And `6d65bd`'s `review.json`, `material_strategy_change`, records the decision explicitly:

> "Motivasjonen er knyttet til investeringsbeslutning, driftsendring og oppbygging av en ny enhet
> fremfor en **udokumentert likestilling av Avinormodellen og sykehusfinansiering**."

A model found the analogy, classified it as an unsupported equivalence claim, and dropped it.

**Causing element — negative.** `B/policy/writing/WRITING_DOCTRINE.md:227-229` — *"Unngå generisk
virksomhetsros, kopierte verdier, prestisjemotivasjon"* — plus `:382-386` under *Faktamyndighet*:
*"Sterk syntese og funksjonell ekvivalens er tillatt når de er intervjuforsvarlige … Det tillater
ikke nytt faktum, høyere eierskap eller sterkere status."* Read together, a stated structural
analogy to a public employer fact lands in the same bucket as a factual equivalence claim, and the
deletion order (W02) removes it first.

**Causing element — absent.** No section anywhere licenses the move *"the employer's published fact
X is structurally the same problem as my documented work Y"* as a **rhetorical** device distinct
from a **factual** claim about the employer.

**Confidence: high — the causal claim is attested by a model's own review artefact.**

---

### W13 — Nothing in the current generation owns "how confident should this sound"

**Weakness.** The framework has an owner for truth (the authorities), for claim strength
(`CLAIM_STRENGTH`), for attribution (`CONTRIBUTION_AND_TEAM`), for lifecycle
(`PROOF_FUNCTION_LIFECYCLE`) and for expression (`FORFATTERSTEMME`) — and, since 0.9.3, no owner
for register confidence.

**Evidence — lineage.** Two deletions in the Gen A → Gen B refactor.

1. `WRITING_DOCTRINE.md` Gen A carried a *Jante-kalibrering* paragraph, deleted in Gen B:

   > "Jante-kalibrering betyr sterke arbeidsverb og nøktern selvevaluering. **Det betyr ikke svake
   > verb, mange forbehold eller undersalg.** Bruk blant annet `utviklet`, `analyserte`,
   > `strukturerte`, `koordinerte`, `tok hovedansvar for`, `implementerte` når implementert …
   > Unngå `unik`, `eksepsjonell`, `fremragende`, `best` og `ledende ekspert`."

   Gen B replaces the whole thing with three abstract lines at `:120-124` and a pointer to
   `PERSUASION_CALIBRATION.md`. That file's entire *"for svakt"* list is two bullets (`:53-63`),
   and it is `status: ACTIVE_MINIMAL` with a governance gate at `:11` — *"Bare eksplisitte,
   gjenbrukbare korreksjoner fra Vegard skal legges til her."* The verb ladder and the explicit
   anti-undersalg counterweight were removed and never landed anywhere.

2. `FORFATTERSTEMME.md § Kanalkalibrering`, Gen A: *"**Søknad:** moderat. Åpning,
   argumentrekkefølge, motivasjon, **sikkerhetsnivå** og avslutning er der stemmen hører hjemme."*
   Gen B (`:150-152`): *"Stemmen former ordlyd, lokal rytme og sosial temperatur … Den velger ikke
   argumentrekkefølge, nytt innhold eller **en annen påstandsstyrke**."* Confidence level was
   removed from the voice's remit and not assigned elsewhere.

**Evidence — output, and it is weaker than I would like.** Gen A's hedges are lifecycle statements
about the model — *"utformet, ikke innført"* — which its authority mandated (§0.3). Gen B's escalate
into capability and authority disclaimers: *"ikke et formelt konsernmandat"*, *"ikke gjennom linje-
eller programmyndighet"*, *"kan jeg ikke svare for"*, *"Der har jeg ingen bakgrunn"*. **But `b5104f`
is Gen B and has none**, so run variance is large and the correlation is weak.

**Confidence: medium — hypothesis.** What would confirm it: re-run one `0fa53b` Stage-3 branch with
the *Jante-kalibrering* paragraph restored verbatim into `PERSUASION_CALIBRATION § CLAIM_STRENGTH`
and nothing else changed, then count self-negating clauses in the letter. What would kill it: the
count does not fall, or a Gen A run reproduced under Gen B authorities hedges just as much.

---

### W14 — The authority's index was flipped from demand-side routing to supply-side ceilings

**Weakness.** Gen A's `Work_experience.md` opened with a table mapping **vacancy signals to
evidence**. Gen B replaced it with a table mapping **records to what they may not claim**.

**Evidence — lineage.** Gen A, in `3eeb10`'s frozen copy, header
`| Stillingssignal | Primær evidens | Rutingsoppsummering – aldri ordrett output |`, with rows
including:

> `Gevinstrealisering, offentlig metode, strategi` → `PRJ-04`
> `Digitalisering, krav, funksjonell leveranseledelse` → `PRJ-08` / `PRJ-09`
> `Standardisering, innføring og kontinuerlig forbedring` → `PRJ-04` + `PRJ-03` + `PRJ-01`/`PRJ-08`
> `Endring på tvers av enheter/faggrupper` → `PRJ-03` + `PRJ-04` + `PRJ-02`/`PRJ-08`

Gen B, in `0fa53b`'s frozen copy, replaces it with
`| Record | Source section | Lifecycle | Can prove | **Live ceilings** |`, where the widest column
in every row is the list of things that may not be claimed.

Gen A also carried two selection rules Gen B deletes: *"Foretrekk støttet operativ bruk, innføring
eller varighet når relevansen ellers er lik"* and *"Bruk høyst to hovedcase i en vanlig søknad."*

**Evidence — output.** `PRJ-09` — arbeidsinntak, kravavklaring, kravstruktur — is the evidence that
answers the ad's *"Videreutvikle arbeidsformer, styringsmodeller og prosesser"*:

| generation | packages carrying `PRJ-09` evidence |
|---|---|
| A (3) | `3eeb10` (*"strukturert arbeidsinntak med formål, avhengigheter, risiko og akseptansekriterier"*), `93c621` (*"arbeidsinntak"*), `6d65bd` (*"Designet arbeidsinntak som avklarer formål, brukere, beslutningsbehov, avhengigheter og akseptansekriterier"*) — **3/3** |
| B (6) | `3eeb10-stage1`, `b5104f` — **2/6**; all four `0fa53b` variants carry `PRJ-08` only |

**Confidence: medium — hypothesis.** The four `0fa53b` packages are correlated samples, so the
effective n on the B side is three. What would confirm it: re-run a `0fa53b` Stage 1 and Stage 3
with the Gen-A demand-side routing table restored *alongside* the Gen-B ceiling table, and check
whether `PRJ-09` returns. What would kill it: it returns without the table, or a Gen A run without
it still routes correctly.

---

### W15 — Three authority sections that would carry vacancy vocabulary are heading-only

**Weakness.** The authority has a section reserved for exactly the thing W01 and W02 are missing,
and it is empty.

**Evidence.** `B/authorities/Other_high_value_information.md`:

```text
## 3. Søke- og titteltaksonomi
### 3.1 Norsk offentlig sektor og helse          (line 233, empty)
### 3.2 Engelsk og privat sektor                 (line 235, empty)
### 3.3 Prioritering av søkeord med høy verdi    (line 237, empty)
### 3.4 Utvalgsrisiko og rutekorrigering         (line 239, populated)
```

*"Prioritering av søkeord med høy verdi"* — prioritisation of high-value keywords — is a heading
with no body. Likewise `B/authorities/Work_experience.md:928` and `:930`,
`### 9.1 CV_ONLY_STARTING_POINT – Analyseavdelingen` and `### 9.2 … tidlig OUS`, both empty,
directly beneath a paragraph instructing the reader to *"velg fra støttede atomer"* — atoms that are
not there. The CV bullet source is therefore §9.3's story map and §4's project detail alone, which
is consistent with the CV bullet counts ranging from 7 to 13 and CV length from 438 to 825 words
across nine renderings of one person.

Also empty: `Other_high_value_information.md:119` §0.5 and `Work_experience.md:112` §0.6, both
titled *Stabil claim-proveniens*; and `B/context/PERSONALITY_PROFILE.md` §§2, 3, 5, 6, 8, 9, 10.
§§2–3 are legitimately retired to `personality_facets.json` per §7; §6 *Canonical Full Source
Profile* is not, and Stage 3 is separately told *"The full profile is not supplied."*

**Confidence: high** for the emptiness; **medium** for the causal link to CV length variance.

---

### W16 — The banned closing pattern was evaded lexically, not semantically

**Weakness.** A rule written as a phrase gets dodged by rephrasing.

**Evidence.** `B/policy/writing/FORFATTERSTEMME.md:133`:

> 1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …` som avslutning.

Shipped:

- `0fa53b-solmed`: *"Jeg tar gjerne en samtale om hvordan erfaringen min kan brukes i oppbyggingen
  av Digital Transformasjon."*
- `93c621`: *"Jeg tar gjerne en samtale om hvordan denne erfaringen kan brukes i Avinors videre
  digitale transformasjon."*
- `0fa53b-solxh`: *"Jeg tar gjerne en samtale om hvordan denne kombinasjonen av økonomisk analyse,
  gevinstarbeid og praktisk digitalisering kan brukes i Avinors arbeid med prioritering og
  transformasjon."*

Same move, one verb swapped. The two closings that genuinely escape the pattern do so by asking the
employer something: `b5104f` — *"Jeg tar gjerne en samtale om hvordan enheten tenker å måle verdien
av initiativene den skal prioritere mellom."* — and `3eeb10` — *"…og tar gjerne en samtale om
hvordan den nye enheten arbeider nå."*

**Causing element — negative.** The rule is stated as a string, with a disclaimer that it is not a
string (`:127-131`), while the *replacement* is described only negatively: *"Avslutt heller med noe
som bare gjelder denne stillingen."* The listed item is concrete; the alternative is abstract, so
the concrete half is what binds.

**Confidence: high.**

---

### W17 — `93c621`'s opening is the pattern `FORFATTERSTEMME` bans by name

**Evidence.** `B/policy/writing/FORFATTERSTEMME.md:139-141`:

> 4. `Når <arbeidsgiver> skal <X>, må <Y> …` som standardåpning. En åpning som bare refererer
>    arbeidsgiverens egen situasjon tilbake til dem, bruker den viktigste setningen i brevet på noe
>    leseren allerede vet.

`93c621` letter, first sentence: *"Avinors nye transformasjonsmiljø skal gjøre mer enn å foreslå
teknologi: Det skal gi ledelsen grunnlag for å prioritere, og hjelpe organisasjonen å realisere
verdi i endringer som må fungere i drift."*

**Causing element — absent.** The rule exists and nothing applies it. `93c621` is a Gen A
three-stage run; unlike `6d65bd`'s review, which names the doctrine sections it applied, `93c621`'s
review records no check against the named `FORFATTERSTEMME` sections at all.

**Confidence: high** for the violation; **medium** for the "not applied" inference.

---

### W18 — Every generated document carries false provenance metadata

**Weakness.** All eighteen DOCX files tell Word they were created on **23 December 2013** in
**Microsoft Macintosh Word**, with `Pages 1` and `Words 0`.

**Evidence.** `docProps/core.xml` in every file:
`<dcterms:created>2013-12-23T23:15:00Z</dcterms:created>`, and the same for `modified`.
`docProps/app.xml`: `<Application>Microsoft Macintosh Word</Application>`, `<Pages>1</Pages>`,
`<Words>0</Words>` — including on `0fa53b`'s three-page CV. The one exception is
`3eeb10-stage1`'s CV, which someone opened and resaved in real Word: `Pages 2`, `Words 930`,
`Application: Microsoft Office Word`.

**Causing element — negative.** `B/runtime/jobbsok/docxfill.py:436-446`, `_core_properties`, updates
four fields only:

```python
values.update(
    {"title": title, "subject": subject, "creator": creator,
     "lastModifiedBy": creator}
)
```

`created` and `modified` are read from the P0.7 master and written back unchanged. And `:366-373`
streams every other part through byte-identical by design — *"Only word/document.xml and
docProps/core.xml are rewritten"* (`:327-329`) — so `app.xml` keeps the master's application string
and stub counts.

**Causing element — absent.** The framework already owns a canonical document date —
`final.finalization`, surfaced as `document_date`, with `B/templates/template_map.json:190`
insisting *"Never date.today() at render time (DEC-38)"*. Nothing connects it to the OPC metadata.

**Confidence: high.** This is adjacent to the known P0.7 class of defect: the same function's
docstring (`:405-417`) explains that the P0.7 masters' core-properties part was invalid OOXML that
Word rejected and LibreOffice tolerated. The date carry-through survived that repair.

---

### W19 — The headline is force-uppercased with no length budget

**Evidence.** `B/templates/template_map.json:28-35` sets `"transform": "upper"` on
`CV_FUNCTIONAL_IDENTITY`, and the master run also carries `<w:caps/>` at `sz 28` — 14 pt — bold.
Headline lengths: `b5104f` 96 chars, `0fa53b-opusx` 84, `93c621` 84, `3eeb10-stage1` 81, `0fa53b`
81, `3eeb10` 73, `0fa53b-solmed` 67, `6d65bd` 62, `0fa53b-solxh` 55. At 14 pt caps across an 18 cm
measure the longer ones wrap to a two-line all-caps banner directly under the name.

**Causing element — absent.** No soft warning, no editorial default, no guidance in *Komplett
CV-doktrine* about headline length. `settings.toml` bounds competency count (4–8) and page count,
not this.

**Confidence: medium** — I have the character counts and the type size, but did not re-render each
CV to confirm the wrap point for every one.

---

### W20 — Provenance and naming drift in the control plane

**Evidence.**

- `B/policy/settings.toml:41` — `SOL_CLASS = "Codex / GPT-5.6 Sol"`, and it is the **only** role
  mapping. The `0fa53b` Stage-3 branches were plainly not all run by that surface — the filenames
  say `opusx`, `solxh`, `solmed` — yet each branch's frozen `settings.toml` snapshots the same
  single value. Any later reader of the manifest will attribute all four to one model.
- Branch directory `stage3_solxh_20260909T155607Z` vs manifest run id `stage3_opt1_…`;
  `stage3_opusx_…` vs `stage3_opt2_…`.
- `B/context/PERSONALITY_PROFILE.md:18` still declares
  `restricted_consumers: ["Stage 2 writer: distilled selected-facet guidance only"]`, and `:60`
  instructs *"Give the Stage-2 writer only distilled selected-facet guidance"*, against
  `B/policy/stages/stage3_final_writer_review.md:11` — *"Stage 2 is retired."*

**Confidence: high.**

---

## Part 2 — Optimisation plan

Ordered by expected effect per unit of change. Each item gives the exact location, the current text
or behaviour, the full replacement, the catalogue items mitigated, the mechanism, the cost, and the
observable next-run signal.

Three constraints bound every proposal, and I have respected them:

- `B/policy/writing/PERSUASION_CALIBRATION.md:11` — that file takes only explicit reusable
  corrections from Vegard. Everything I propose for it is written as such a correction, for him to
  accept or reject, not as a model-authored rule.
- `B/policy/writing/WRITING_DOCTRINE.md:40-42` and `:496-498` — semantic writing guidance may never
  become a deterministic failure, and no similarity detector may be built.
- `B/policy/settings.toml:7-9` — nothing may branch the product.

---

### Tier 1 — ship first: small, local, high effect

---

#### P1 · Stop printing the job title twice in the letter header

**File:** `B/templates/template_map.json`, `documents.letter.controls.APP_JOB_TITLE`, lines 200–206.

**Current:**

```json
        "APP_JOB_TITLE": {
          "kind": "inline",
          "count": 2,
          "source": "job.title",
          "required": true,
          "note": "Appears twice in the master: the reference block and the subject line. Both are filled."
        },
```

**Replacement:**

```json
        "APP_JOB_TITLE": {
          "kind": "inline",
          "count": 1,
          "source": "job.title",
          "required": true,
          "note": "The subject line only. Printing the role twice within three lines spends the reader's first fixation on a repetition; the reference-block instance was removed from APPLICATION_MASTER.docx and that row now carries the date alone."
        },
```

**Paired master edit, by the human, once:** in `APPLICATION_MASTER.docx`, delete the
`APP_JOB_TITLE` content control and the `Stilling: ` literal from the header table's second row,
and remove that row's empty right cell. `WRITING_DOCTRINE.md:346-352` places template structure and
typography with the human, in the masters, which is where this belongs.

Preflight will enforce agreement: `require_template_contract`
(`B/runtime/jobbsok/docxfill.py:130-150`) fails loudly if the map and the master disagree on
control counts, which is the desired behaviour and the reason to change both together.

**Mitigates:** W09.

**Mechanism.** Removes one of three restatements. The remaining two — the subject line, and the
writer's opening where the writer chooses to use one — are what a Norwegian reader expects.

**Cost.** Requires touching a master, which is a human action outside the pipeline and invalidates
the `templates/` hashes recorded in `B/evidence/finalization/HASHES.sha256` and the GATE-02
inventory; those need regenerating. The map-only variant (leave the master, add `fill` / `clear`
keys and teach `fill_inline` to honour them) avoids that but puts branching logic into the
renderer for one control, which is worse. Take the master edit.

**Next-run signal.** The rendered letter shows the role name once above the body, and the first
body sentence is argument rather than restatement.

---

#### P2 · Make `KJERNEOMRÅDER` a bold label followed by regular text

**Files:** `B/templates/template_map.json:48-55`, `B/runtime/jobbsok/render.py:145-157`,
`B/runtime/jobbsok/docxfill.py:176-185` and `:230`.

**Current, map:**

```json
        "CV_CORE_COMPETENCE": {
          "kind": "block",
          "count": 1,
          "source": "package.cv.competencies",
          "transform": "join_middot",
          "prefix": "KJERNEOMRÅDER  ",
          "required": true
        },
```

**Replacement, map:**

```json
        "CV_CORE_COMPETENCE": {
          "kind": "block",
          "count": 1,
          "source": "package.cv.competencies",
          "transform": "join_middot",
          "label": "KJERNEOMRÅDER",
          "label_separator": "  ",
          "required": true,
          "note": "The label keeps the template run's bold weight; the joined competencies are emitted as a second run with bold cleared. Emitting label and payload as one run made the whole block bold, which is what the master's placeholder formatting implied and not what the zone is for."
        },
```

**Replacement, `render.py:155-156`:**

```python
        if transform == "join_middot":
            if not items:
                return block([])
            label = spec.get("label")
            if label:
                separator = spec.get("label_separator", "  ")
                return block([(label + separator, " · ".join(items))])
            return block([prefix + " · ".join(items)])
```

— that is, a block item may now be a `(label_text, body_text)` tuple as well as a plain string.

**Replacement, `docxfill.py`** — add a two-run variant beside `_set_paragraph_text`:

```python
def _set_paragraph_runs(paragraph: ET.Element, label: str, body: str) -> None:
    """Emit a bold label run followed by a regular body run.

    The label inherits the template run's properties unchanged; the body run is
    the same properties with <w:b/> removed, so a long payload does not inherit
    the placeholder's label weight.
    """
    template_run = paragraph.find(f".//{W}r")
    properties = paragraph.find(f"{W}pPr")
    for child in list(paragraph):
        if child is not properties:
            paragraph.remove(child)
    label_run = copy.deepcopy(template_run) if template_run is not None else ET.Element(f"{W}r")
    _set_run_text(label_run, label)
    body_run = copy.deepcopy(label_run)
    body_props = body_run.find(f"{W}rPr")
    if body_props is not None:
        for bold in body_props.findall(f"{W}b"):
            body_props.remove(bold)
    _set_run_text(body_run, body)
    paragraph.append(label_run)
    paragraph.append(body_run)
```

and in `fill_block` at `:230`, branch: if `text` is a 2-tuple call `_set_paragraph_runs`, else
`_set_paragraph_text` unchanged.

**Mitigates:** W08, and materially helps W03 by making the block scannable rather than merely
shorter.

**Mechanism.** A bold label reads as a label; 40–80 words of bold body text reads as a wall and
defeats the zone's purpose, which `WRITING_DOCTRINE.md:320-325` describes as making the
occupational anchor legible *"på første skanning"*.

**Cost.** Touches the renderer — the highest-blast-radius change in Tier 1. `_set_paragraph_text`
stays byte-compatible for every other control, so the risk is confined to one control. One real
failure mode: if the master's placeholder run does not carry `<w:b/>` directly but inherits bold
from a paragraph style, the `findall(f"{W}b")` removal is a silent no-op and the fix does nothing —
verify against the rendered output, not the code. Render receipts compare visible text, not runs,
so no receipt changes.

**Next-run signal.** Open the rendered CV: `KJERNEOMRÅDER` is bold and the competencies are not.

---

#### P3 · Stop stamping 2013 and "Microsoft Macintosh Word" on every document

**File:** `B/runtime/jobbsok/docxfill.py`, `_core_properties` (`:436-446`) and
`write_filled_document` (`:366-373`).

**Current:**

```python
def _core_properties(
    archive: ZipFile, title: str, subject: str, creator: str
) -> bytes | None:
    if CORE_PART not in archive.namelist():
        return None
    values = read_core_properties(archive)
    values.update(
        {"title": title, "subject": subject, "creator": creator,
         "lastModifiedBy": creator}
    )
    return build_core_properties(values)
```

**Replacement:**

```python
APP_PART = "docProps/app.xml"


def _core_properties(
    archive: ZipFile, title: str, subject: str, creator: str, document_date: str
) -> bytes | None:
    """Write core properties, including a truthful creation date.

    The P0.7 masters carry created/modified = 2013-12-23T23:15:00Z. Carrying
    that through means every delivered application tells Word it was written in
    2013. The canonical document date already exists on the final package
    (DEC-38) and is the only defensible value here.
    """
    if CORE_PART not in archive.namelist():
        return None
    values = read_core_properties(archive)
    stamp = f"{document_date}T00:00:00Z"
    values.update(
        {"title": title, "subject": subject, "creator": creator,
         "lastModifiedBy": creator, "created": stamp, "modified": stamp,
         "revision": "1"}
    )
    return build_core_properties(values)


_APP_APPLICATION = re.compile(rb"<Application>.*?</Application>", re.S)
_APP_STALE_COUNT = re.compile(
    rb"<(Pages|Words|Characters|CharactersWithSpaces|Lines|Paragraphs)>.*?</\1>", re.S
)


def _app_properties(archive: ZipFile) -> bytes | None:
    """Remove the master's application identity and its stale statistics.

    Word recomputes Pages/Words on open; shipping Pages=1 on a three-page CV is
    simply wrong for anything that reads the part without opening the document.
    """
    if APP_PART not in archive.namelist():
        return None
    raw = archive.read(APP_PART)
    raw = _APP_APPLICATION.sub(b"<Application>Jobbsok_26</Application>", raw)
    raw = _APP_STALE_COUNT.sub(b"", raw)
    return raw
```

and in the writer loop, a third branch beside the existing two:

```python
            for item in source.infolist():
                if item.filename == DOCUMENT_PART:
                    target.writestr(item, document_bytes)
                elif item.filename == CORE_PART and core_bytes is not None:
                    target.writestr(item, core_bytes)
                elif item.filename == APP_PART and app_bytes is not None:
                    target.writestr(item, app_bytes)
                else:
                    target.writestr(item, source.read(item.filename))
```

The caller in `B/runtime/jobbsok/render.py` already resolves `document_date` for the letter's
`APP_DATE` control; pass the same value here so CV and letter agree.

**Mitigates:** W18.

**Mechanism.** Metadata is the one part of the artefact a background-check process or an ATS reads
without a human. Avinor states it verifies CV contents; a 2013 creation date on a 2026 application
is a gratuitous inconsistency.

**Cost.** `write_filled_document`'s docstring claim — *"every other zip part is streamed through
byte-identical"* — stops being true and must be updated, and any hash-based evidence pinning
`app.xml` bytes will move; check `B/evidence/finalization/HASHES.sha256` and the GATE-02 inventory
before shipping. Removing `<Pages>` entirely is safer than writing a computed value, because the
renderer does not know the page count at fill time — it learns it later, from the PDF (W03).

**Next-run signal.** `unzip -p out.docx docProps/core.xml` shows the document date; `app.xml` has
no `Microsoft Macintosh Word` and no `Pages`.

---

#### P4 · Fix the granularity and the channel of the "no defensive paragraph" rule

**File:** `B/policy/writing/PERSUASION_CALIBRATION.md`, `§ MATERIAL_REQUIREMENTS_AND_GAPS`, items
4–5 (`:129-131`). Proposed as an explicit correction from Vegard, per `:11`.

**Current:**

```text
4. Unngå et defensivt «jeg mangler X»-avsnitt med mindre taushet ville villede
   vesentlig.
5. Hold det uløste gapet synlig i `review.json` for mennesket.
```

**Replacement:**

```text
4. Unngå defensiv prosa om et ikke-diskvalifiserende gap. Regelen gjelder setningen og
   leddet, ikke bare avsnittet: en negasjon inne i et ellers positivt avsnitt er den samme
   feilen i mindre format. Skriv ikke «ikke et formelt konsernmandat», «ikke gjennom linje-
   eller programmyndighet», «det har jeg ikke tall på» eller «der har jeg ingen bakgrunn»
   som en påstand om kandidaten. Unntaket er der taushet ville villede vesentlig, altså der
   teksten ellers ville invitere til en slutning som ikke holder.
5. Kanal: det uløste gapet hører hjemme i `review.json`, ikke i arbeidsgiverteksten. Dette
   gjelder alle gap, ikke bare regnskapsnære (`Other_high_value_information.md § 3.4`).
6. Kostnaden er ulik. Et gap arbeidsgiveren allerede kan se, typisk bransje eller domene,
   koster lite å nevne og kan kjøpe tillit. Et krav annonsen selv merker som ønskelig eller
   som en fordel, koster mye: å nevne det med annonsens eget ord gir screeneren en grunn.
   Skriv i stedet den nærliggende overførbare evidensen positivt, og la review bære grensen.
7. Hold det uløste gapet synlig i `review.json` for mennesket.
```

(renumber the following items).

**Also required for coherence** — add a row to `B/authorities/Other_high_value_information.md § 3.4`,
after line 247:

```text
| `MANDATE_DEFICIT_FRAME` | Ansvarsnivå, portefølje-, program- eller linjemyndighet introduseres gjennom det Vegard ikke har | Skriv den dokumenterte funksjonelle påvirkningen positivt: omfang, beslutning, kontroll, overlevering, tverrfaglig gjennomslag. Hold mandatgrensen i review, ikke i arbeidsgiverteksten |
```

**Mitigates:** W04, and part of W05.

**Mechanism.** Moves the rule's unit from paragraph to clause, which is the level at which every
observed instance occurred, and generalises the correct channel rule that already exists in one
domain-scoped row of the authority.

**Cost, and it is real.** This is the item most likely to over-correct. `PROOF_FUNCTION_LIFECYCLE`
(`:104-118`) legitimately requires state-accurate verbs, and `CLAIM_STRENGTH` (`:36-38`) allows a
strong formulation carried with a precise note. A writer that reads P4 as *"never state a
boundary"* will start overclaiming, which the framework rightly treats as the worse failure
(`B/prompts/STAGE3_PROMPT.md:150-152`). Item 6 keeps the distinction visible and the existing
`:53-63` *"for svakt"* block still guards the opposite ditch — but ship P4 and P12 together, never
P4 alone.

**Next-run signal.** Count negation clauses about the candidate's own authority or measurement in
the nine letters. Today: four packages, five clauses. Target: zero outside a case where silence
would mislead, **with the same limits still present in `review.json` `known_limitations`** — that
second half is the check that the fix moved the content rather than deleting it.

---

#### P5 · Mark the story map's `Limit` column as review-only

**File:** `B/authorities/Work_experience.md`, §9.3, immediately above the table at line 934.

**Current.** The heading `### 9.3 Intervjuforsvarlige historiekart` is followed directly by the
table header `| Story | Problem | Personal contribution | Control/proof | Status/value | Limit |`.

**Replacement.** Insert before the table:

```text
**Kolonnebruk.** `Problem`, `Personal contribution`, `Control/proof` og `Status/value` er
materiale for arbeidsgivertekst. **`Limit` er `REVIEW_ONLY`.** Kolonnen setter taket for hva de
fire andre kolonnene kan si, og skal ikke skrives ut som en setning i CV eller brev. Et punkt
som bare kan skrives sant ved å ende på det arbeidet ikke oppnådde, hører til i
intervjureserven eller i `review.json`, ikke i CV-en.
```

**Mitigates:** W05.

**Mechanism.** The limit currently sits in the same visual row as the material with nothing marking
it as a different kind of thing. The authority already uses channel tags elsewhere —
`INTERNAL_ONLY`, `REVIEW_ONLY` in `Other_high_value_information.md` — so this applies an existing
vocabulary rather than inventing one.

**Cost.** Low. The risk is a writer reading `REVIEW_ONLY` as *"the ceiling does not apply to the
text"*, which would be exactly backwards; the wording states the ceiling function explicitly to
block that. Note also that `0fa53b`'s honest BI bullet is genuinely good evidence and this change
should not delete it — it should turn *"Eide løsningen fra om lag august 2025 til februar 2026 …
Løsningen ble avviklet i februar 2026"* into a bullet that leads with what was built and carries
the dates without terminating on the decommissioning.

**Next-run signal.** No CV bullet ends on a clause whose only content is a negative, and
`review.json` `known_limitations` still names the decommissioning and the unrealised benefits.

---

#### P6 · Label the worked example as calibration, not phrasing

**File:** `B/policy/writing/PERSUASION_CALIBRATION.md:65-72`.

**Current:**

```text
Mønstereksempel, med generisk innhold. Kilden sier at noe «ble innført som
Y-standard» og er «oppgitt aktivt om lag N år senere»:
```

**Replacement:**

```text
Mønstereksempel for **styrkenivå**, med generisk innhold. Eksempelet viser hvor sterkt en
påstand kan sies, ikke hvordan setningen skal formuleres. Formuleringen er ikke en mal: skriv
setningen på nytt for den enkelte jobben, og bruk ikke den samme konstruksjonen i både CV og
søknad. Kilden sier at noe «ble innført som Y-standard» og er «oppgitt aktivt om lag N år
senere»:
```

**Mitigates:** W06, and part of W07.

**Mechanism.** The example is the most concrete phrasing artefact in the writing policy, so it
functions as a template whether or not it was meant to. Saying so is the whole fix.

**Cost.** Near zero. Slight risk that a writer, told not to reuse the construction, weakens the
claim instead of rewording it; the surrounding `riktig / for svakt / for sterkt` block at `:69-71`
already guards that and the replacement keeps it.

**Next-run signal.** The phrase *"ble innført som sykehusdekkende standard og var fortsatt i bruk om
lag …"* appears in at most one of the two documents per package, and its wording differs between
packages.

---

#### P7 · Give Stage 3 an explicit CV/letter division-of-labour pass

**File:** `B/policy/stages/stage3_final_writer_review.md`, `## Sequence`, after step 7 (`:63`).

**Current.** Step 5 says *"…remove repetition that adds neither a new function nor useful detail."*
Nothing compares the two documents.

**Replacement — insert as a new step 8, renumbering the existing 8:**

```text
8. Before the realization pass, read the CV and the letter against each other once. No
   sentence may appear in both in the same or near-identical wording (D Komplementaritet
   mellom CV og søknad). Where the same fact belongs in both, the CV states the record and the
   letter states the reasoning, the constraint or the decision, in different words and at a
   different grain. This is an authoring duty, not a validator: no deterministic check exists
   for it and none may be built (D Variasjon innenfor en klynge).
```

**Mitigates:** W07.

**Mechanism.** Stage 3 authors both documents in one call, so the comparison is free there and
nowhere else. The duty sits before the content lock, because rewording one of a duplicated pair
changes what the employer learns from the letter and is therefore out of the polish pass's scope
(`:148`).

**Cost.** Adds a pass to an already long instruction, and that instruction's own drift note
(`B/prompts/STAGE3_PROMPT.md:141-144`) warns that this stage buys smoothness with signal. Word the
duty as *"different words and a different grain"*, never *"delete one"*, or the fix will produce
thinner letters. `Erstatnings- og komprimeringsrekkefølge` still governs what goes if something
must.

**Next-run signal.** Re-run the similarity check. Today 9/9 packages have a pair at ≥0.80 and 4/9
have one at 1.00. Target: zero pairs at 1.00 and at most one ≥0.90 per package.

---

### Tier 2 — ship second: structural, larger blast radius

---

#### P8 · Carry requirement coverage across the stage boundary

The highest-value item in the plan and the most expensive. Tier 2 only because it touches a schema.

**File 1:** `B/schemas/package.schema.json`. Add to the root object's `properties`, and to
`required`:

```json
    "requirement_coverage": {
      "type": "array",
      "minItems": 1,
      "description": "One entry per material_requirements[] item in the bound strategy. No maxItems: no cap may truncate a material employer requirement (Spec 8.3, DEC-33). This records where the final package addresses each requirement; it is a coverage account, not a score, and no numeric field belongs here.",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["requirement_id", "where"],
        "properties": {
          "requirement_id": { "type": "string", "pattern": "^R[0-9]{2,3}$" },
          "where": { "enum": ["CV", "LETTER", "BOTH", "NONE"] },
          "how": { "type": "string" }
        }
      }
    },
```

**File 2:** `B/policy/stages/stage3_final_writer_review.md`, step 5 (`:54`).

**Current:**

```text
5. Address material requirements and gaps truthfully, build specific motivation,
   and remove repetition that adds neither a new function nor useful detail.
```

**Replacement:**

```text
5. Address material requirements and gaps truthfully, build specific motivation, and remove
   repetition that adds neither a new function nor useful detail. Then account for coverage:
   return one `requirement_coverage` entry per `material_requirements` item. Every MINIMUM or
   IMPORTANT requirement the strategy marks SUPPORTED must be `CV`, `LETTER` or `BOTH`, and
   `how` must name the concrete evidence that carries it, not the requirement restated. A
   SUPPORTED requirement returned as `NONE` is a decision you are making: say why in the
   review's `known_limitations`. `ADJACENT`, `GAP` and `UNKNOWN` requirements may be `NONE`
   without explanation. Coverage is an account of the text you wrote; it never licenses
   claiming a requirement the evidence does not carry (K MATERIAL_REQUIREMENTS_AND_GAPS 1),
   and it is not a reason to import the advertisement's vocabulary where it is not covered
   (K 3).
```

**File 3:** `B/runtime/jobbsok/validate.py` — the mechanical check is membership and shape only:
every `requirement_id` exists in the bound strategy, every strategy requirement appears exactly
once, `where` is in the enum. **No check on whether coverage is adequate** — that is semantic, and
`WRITING_DOCTRINE.md:40-42` forbids failing a package on it.

**Mitigates:** W01 primarily; W02 and W12 substantially, because a writer that must account for R10
and R13 has a reason to look for the evidence in §5.2 / §6.9 and to use the employer's term where
it is genuinely covered.

**Mechanism.** The requirement list already exists, already carries relation ratings, and already
has evidence refs attached. The only thing missing is an obligation to say what happened to each
one. Making the account a returned artefact converts a sentence of advice into a step the writer
cannot skip, without turning any editorial judgement into a hard gate.

**Cost, and it is substantial.**

- `package.schema.json` is frozen per run (`DEC-40`), so this lands in a new run only, and every
  consumer of the final package must tolerate the new field. Check `merge.py`, `artifacts.py` and
  the `write.semantic_fields` list the CLI emits in the Stage-3 context bundle:
  `STAGE3_PROMPT.md:102-107` tells the model to populate *exactly* `write.semantic_fields`, so the
  CLI must advertise the new field or the model will correctly refuse to write it.
- **Real risk of checkbox prose.** A writer forced to account for R14 — *kommunikasjonsevner på
  norsk og engelsk* — may bolt "Gode kommunikasjonsevner på norsk og engelsk" into the profile,
  which is exactly the generic self-characterisation `CLAIM_STRENGTH:28-31` and `FORFATTERSTEMME §
  Selvfremstilling` exist to prevent. The `how` field's wording — *"name the concrete evidence that
  carries it, not the requirement restated"* — is the guard, and it is a soft one. Mitigate by
  pairing with P9, which gives that evidence somewhere structural to live, and by watching for this
  exact failure mode in the next run.
- `REVIEW_ONLY` mode has no final to account for; the field must be conditional on `write.allowed`
  including the final package.

**Next-run signal.** Three things, in order of importance. (a) `requirement_coverage` shows R10, R13
and R14 as `CV`, `LETTER` or `BOTH` rather than `NONE`. (b) The words `styringsgrupp`, `portefølje`
and a communication claim appear in employer text **attached to evidence** — *"planla og fasiliterte
workshops og utarbeidet beslutningsgrunnlag for klinikkens ledere"* counts; *"gode
kommunikasjonsevner"* does not. (c) `used_evidence_refs` rises, because the evidence that carries
R10 and R13 sits in §5.2, §6.9, `PRJ-08` and `PRJ-09`, which the current packages under-use.

---

#### P9 · Wire the dead "selected evidence" block

**File 1:** `B/templates/template_map.json:68-80`.

**Current:**

```json
        "CV_SELECTED_EVIDENCE_HEADING": {
          "kind": "block",
          "count": 1,
          "source": "none",
          "required": false
        },
        "CV_SELECTED_EVIDENCE": {
          "kind": "block",
          "count": 1,
          "source": "none",
          "required": false
        },
```

**Replacement:**

```json
        "CV_SELECTED_EVIDENCE_HEADING": {
          "kind": "block",
          "count": 1,
          "source": "literal:UTVALGTE LEVERANSER",
          "required": false,
          "note": "Rendered only when CV_SELECTED_EVIDENCE resolves to a non-empty list; an empty resolved list clears both controls."
        },
        "CV_SELECTED_EVIDENCE": {
          "kind": "block",
          "count": 1,
          "source": "package.cv.selected_evidence",
          "required": false,
          "note": "Three to five vacancy-selected delivery lines, above the chronology. This is where evidence that answers a named requirement goes when it would otherwise be buried in an employment bullet or absent (see requirement_coverage)."
        },
```

**File 2:** `B/schemas/package.schema.json`, `cv.properties`:

```json
        "selected_evidence": {
          "type": "array",
          "maxItems": 5,
          "items": { "type": "string", "minLength": 1 },
          "description": "Optional. Three to five vacancy-selected delivery lines rendered above the chronology. An absent or empty array renders nothing. Same factual authority and claim ceilings as every other zone; not a place for competencies restated as achievements."
        },
```

**File 3:** `B/policy/stages/stage3_final_writer_review.md:77-78`.

**Current:** *"Write all four dynamic zones: headline, profile, competencies and
employment_overrides."*

**Replacement:** *"Write the four required dynamic zones — headline, profile, competencies and
employment_overrides — and, when the vacancy rewards it, the optional selected_evidence block. Use
selected_evidence for a delivery that answers a named requirement and would otherwise sit too deep
in an employment bullet to be found in a first scan. Leave it absent when the top zone and the
bullets already carry the answer; an empty or absent array renders nothing."*

**Mitigates:** W11, W01, and helps W03 by giving the writer somewhere to put the strongest three
lines instead of lengthening the employment bullets.

**Cost.** Adds a fifth zone to a CV that already runs long in two of nine packages — this must ship
with P10 or it will make the page problem worse. `require_override_bullets_visible` in the map's
`verification` block needs checking against the new control. Real risk of the block becoming a
competency list restated as achievements; the schema description is the only guard.

**Next-run signal.** The block appears, carries three to five lines, and the lines are deliveries
with scope, not adjectives. Cross-check against `requirement_coverage`: the block should be where
R10 or R13 is carried.

---

#### P10 · Move the page measurement in front of triage

Addresses W03 — the measurement exists and arrives too late.

**Change 1, `B/prompts/STAGE3_PROMPT.md`, between steps 5 and 6 (`:102-111`).** Insert a probe
render between authoring and submission:

```text
5b. **Probe the length before you submit.** Write the return, then run

    .\.venv\Scripts\jobbsok.exe render --run <run_id> --job <job_id> --probe

    which fills and converts the current return without finalizing, committing or producing a
    delivered artifact, and prints the page count for both documents. If the CV exceeds two
    pages or the letter one, compress by D Erstatnings- og komprimeringsrekkefølge and
    re-probe before submitting. Never buy pages with typography: the master's type is the
    human's, set once (D Myke redaksjonelle utgangspunkt). If the probe degrades and returns
    no page count, submit and note it — do not loop.
```

`--probe` is a new flag on the existing `render` command: the same fill and convert path, writing
to a temporary staging directory, emitting no receipt and no `render_report.json`, mutating no run
state. `render.py` already stages to a temporary directory (`RENDER_STAGING_PREFIX`, `:651`), so
the probe short-circuits an existing path rather than adding one.

**Change 2, `B/policy/stages/stage3_final_writer_review.md`, beneath the triage table (`:110-114`):**

```text
A CV over two pages or a letter over one is a bounded, known, local repair. If you submit one
without having compressed it, triage is `CHECK`, and the reason names the document and the
page count. It is not `READY`: a normal human skim does not tell the reader that the CV runs
to three pages, and correcting it is editorial work you were able to do.
```

**Mitigates:** W03 completely, W10 partially — the writer feels the cost of the fixed sections and
can compress its own zones around them — and W08 indirectly.

**Mechanism.** The framework's position that page count is editorial rather than mechanical is
right and I am not proposing to change it. `DEC-24` / `DEC-33` and `WRITING_DOCTRINE.md:331-352`
stay intact: nothing fails, no validator gates. The change is that the editorial signal reaches the
editor while the editor is still working.

**Cost.**

- Adds a Word COM round trip inside the authoring loop. `converter_timeout_seconds = 180` and
  `invocation_granularity = "per_document"` mean two conversions per probe, so a probe cycle can
  cost minutes and a writer that probes three times has spent ten. Probing the CV only is a
  reasonable narrowing.
- `pdf_required = false` means the probe can return nothing; the instruction handles that
  explicitly above.
- The `CHECK` addition pushes against `STAGE3_PROMPT.md:145-149`, which warns specifically about
  inflated `CHECK`. The wording ties `CHECK` to a *named, measured* condition, which is exactly what
  that warning demands — *"Without one named, bounded, unresolved item, the instruction does not
  permit `CHECK`"* — so the two are compatible. This is the interaction to watch.

**Next-run signal.** Zero page warnings in `render_report.json` across the run; or, where one
appears, triage is `CHECK` and the reason names it. `0fa53b`'s review note asking the *human* to
check the page count disappears.

---

#### P11 · License the employer-fact analogy

**File:** `B/policy/writing/WRITING_DOCTRINE.md`, new subsection inside `# Begrunnet motivasjon`,
after line 229.

**Insert:**

```text
## Arbeidsgiverfakta som analogi

Arbeidsgiverens egne publiserte fakta kan brukes som analogi til kandidatens dokumenterte
arbeid. En analogi er en retorisk figur, ikke et faktum om arbeidsgiveren: den sier at to
problemer har samme form, ikke at kandidaten kjenner arbeidsgiverens løsning, tall eller
interne forhold.

Tillatt: navngi et publisert arbeidsgiverfaktum og vise hvilken strukturell likhet det har med
et dokumentert arbeid, med kandidatens side skrevet på sitt eget claim-tak.

Ikke tillatt: å hevde at kandidaten har arbeidet med arbeidsgiverens problem; å utlede et tall,
en beslutning eller en intern svikt hos arbeidsgiveren fra analogien; å bruke analogien som
erstatning for evidens på kandidatsiden. Grensen mot § Faktamyndighet og lifecycle-skille er
den samme som ellers: analogien flytter ingen påstandsgrense.

Dette er ikke virksomhetsros. Ros sier at arbeidsgiveren er viktig; en analogi sier hvilket
problem kandidaten kan gjenkjenne.
```

**Mitigates:** W12, and helps W02 by giving employer specificity a legitimate route that is not
vocabulary echo.

**Mechanism.** The Avinormodellen case shows the framework currently has no category for this move,
so it defaults to the nearest one — unsupported equivalence — and deletes it. Adding the category is
the whole change.

**Cost.** The proposal most likely to produce bad output if misread. An analogy sits close to
`Ubetrodd vacancy-innhold`'s warning against *"en påstand om kjent intern svikt, skjult frykt eller
manglende myndighet"* (`:245-247`), and close to `Arbeidsgiverbyttetesten`'s warning against
overcorrecting with slogans. The *"Ikke tillatt"* paragraph is written to hold that line; watch the
next run for analogies that assert something about Avinor rather than about the candidate. If it
misfires, this is the first item to revert.

**Next-run signal.** At least one letter names a published Avinor fact and connects it to a
documented piece of work without asserting anything about Avinor's internal state. `b5104f`'s
*"Avinor driver 43 lufthavner og flysikringstjenesten, og den nye enheten skal øke
gjennomføringskraften i noe som allerede må virke hver dag"* is the shape; the Avinormodellen ↔
proxy-allocation analogy is the one currently being left on the table.

---

#### P12 · Restore the confidence-level owner

**File:** `B/policy/writing/PERSUASION_CALIBRATION.md`, `# CLAIM_STRENGTH`, after line 63. Proposed
as an explicit correction from Vegard, per `:11`.

**Insert:**

```text
Nøktern selvevaluering betyr sterke arbeidsverb, ikke svake. **Det betyr ikke mange forbehold
eller undersalg.** Bruk blant annet `utviklet`, `analyserte`, `strukturerte`, `koordinerte`,
`utformet`, `avviste`, `tok hovedansvar for`, `implementerte` når implementert, og `omsatte
behov til løsning` når kilden støtter det. Unngå `unik`, `eksepsjonell`, `fremragende`, `best`
og `ledende ekspert`.

Registeret er ikke stemmens ansvar. `FORFATTERSTEMME.md` former hvordan noe sies og kan ikke
endre påstandsstyrken; sikkerhetsnivået i teksten eies her.
```

**Mitigates:** W13, and works with P4 as its counterweight.

**Mechanism.** Restores the deleted verb ladder and the explicit anti-undersalg clause, and assigns
the ownership the Gen A → Gen B refactor left unclaimed. The second paragraph closes the hole
created when `sikkerhetsnivå` was removed from `FORFATTERSTEMME § Kanalkalibrering`.

**Cost.** Low, but this restores 0.9.2 text into a 0.9.3 file, so the version header and any
provenance note should say so. The verb list will be treated as a list of examples — W06's lesson —
and that is acceptable here because it is a ladder of *strength*, not of phrasing, and the verbs are
ordinary enough not to become a stock construction.

**Next-run signal.** Re-run one `0fa53b` Stage-3 branch with only this change and count
self-negating clauses. This is also the experiment that confirms or kills W13.

---

#### P13 · Restore demand-side routing, and fill the empty taxonomy sections

**File 1:** `B/authorities/Work_experience.md`, §0. Keep the Gen-B `Record | … | Live ceilings`
table and reinstate the Gen-A signal table **above** it, restored from
`B/runs/r20260905-005939-3eeb10/frozen/authorities/Work_experience.md` (header
`| Stillingssignal | Primær evidens | Rutingsoppsummering – aldri ordrett output |`), with rows
updated for the Gen-B lifecycle facts. Both tables, in that order: what answers which employer
signal, then what each record may not claim.

**File 2:** `B/authorities/Other_high_value_information.md:237`, `### 3.3 Prioritering av søkeord med
høy verdi` — currently a heading with no body. Fill it with the ranked vacancy-vocabulary map for
the role families the candidate actually applies to, at minimum: `gevinstrealisering`,
`porteføljestyring`, `virksomhetsstyring`, `styringsmodeller`, `beslutningsgrunnlag`,
`beslutningsprosesser`, `styringsgrupper`, `endringsledelse`, `fasilitering`,
`gjennomføringskraft`, `målbar verdi` — each with the sections and records that cover it and the
ceiling that applies.

**Mitigates:** W14, W15, and materially supports P8 by giving the coverage account somewhere to look.

**Cost.** Authority edits are the highest-consequence edits in the system —
`WRITING_DOCTRINE.md:21-28` makes these three files the sole owners of candidate facts. Neither
change adds a fact: File 1 restores an index that existed, File 2 is a routing map rather than
evidence. Both must be marked as navigation in the terms the system already uses — *"Digester og
keyword-indekser er navigasjon"*, `stage1_decision_architecture.md:23-24` — or a writer may cite
them as sources.

**Next-run signal.** `PRJ-09` and the §5.2 / §6.9 evidence appear in packages that currently omit
them; the `requirement_coverage` account for R08, R09 and R10 names concrete records.

---

#### P14 · A tunable social-register calibration, inside the content lock and nowhere else

Addresses **W04b**, and closes the loop with **W04** and **P4/P12** — those three own the floor of
the register axis, this owns the ceiling.

**The design constraint that decides everything else.** This mechanic must not reach the drafting
stages. A social-register instruction read during evidence selection or letter construction does not
produce a better-calibrated argument; it produces a *smaller* one, because the cheapest way to sound
less self-important while still writing is to claim less. That is the failure mode this framework
spent a generation escaping, and it is still visible in the corpus as W04. So the mechanic is
realization-only, it is bound to the content lock, and it is placed in a file the drafting stages
structurally cannot read.

**Why the placement is airtight rather than merely instructed.** `FORFATTERSTEMME.md` already
declares `factual_authority: false`, `claim_authority: false`, `strategy_authority: false`,
`qualification_authority: false`, `primary_consumer: Stage 3` and
`non_consumer: "Stage 1 (filen er ikke del av denne fasens writing_policy-rute)"`.
`stage1_decision_architecture.md:32-33` confirms it from the other side — *"voice is not an input to
this stage"* — as does `prompts/STAGE1_PROMPT.md:95`: *"voice is Stage-3-only."* Putting the marker
inventory in `FORFATTERSTEMME.md` means no drafting stage can reach it without violating an existing
routing contract. No new isolation machinery is needed; the framework already built it.

---

**P14a · The knob.** `B/policy/settings.toml`, new table, after `[personality]` (`:21-28`).

```toml
[voice]
# DEC-4x: social register calibration for the content-locked final polish in
# Stage 3. Realization-only. Snapshotted into the manifest at freeze like every
# other setting (DEC-40), so tuning applies to a new or child run and two
# settings can be compared as branches of one run.
#
# This dial raises how much SELF-PRESENTATION is recast. It can never lower how
# strongly a supported claim is stated. The floor in FORFATTERSTEMME.md
# § Sosial kalibrering i sluttpussen is invariant at every level, including 4.
#
# Consumed only by Stage 3. FORFATTERSTEMME.md is not on Stage 1's
# writing_policy route, so this value is unreachable from drafting.
#
# 0 off · 1 light · 2 standard · 3 firm · 4 maximum conformity
social_register_calibration = 2
```

`2` is the default I would ship. `4` is documented as having a real cost in assertiveness and is not
a default.

---

**P14b · The inventory and the floor.** `B/policy/writing/FORFATTERSTEMME.md`, new section between
`## Selvfremstilling som skal bort` (`:94`) and `## Mønstre som skal erstattes` (`:125`).

```text
## Sosial kalibrering i sluttpussen

Denne seksjonen gjelder bare den innholdslåste sluttpussen i Stage 3. Nivået settes i
`policy/settings.toml [voice] social_register_calibration` og følger med i Stage-3-bundelen.

Målet er å presentere kandidaten så kvalifisert som evidensen bærer, uten at teksten leses
som selvhøytidelig, jantebrytende eller fremmed for norsk arbeidslivsregister. Dette er tre
uttrykksrisikoer. Ingen av dem er en grunn til å si mindre.

### Gulvet, som er likt på alle nivåer

Kalibreringen kan aldri:

1. legge til et forbehold på en kildestøttet påstand;
2. bytte et støttet arbeidsverb mot et svakere;
3. innføre selvironi, selvkritikk eller en setning om hva kandidaten ikke har;
4. omtale et krav annonsen merker som ønskelig eller som en fordel, som noe kandidaten
   mangler;
5. bytte `jeg` mot et diffust `vi` på dokumentert personlig arbeid;
6. fjerne en teamramme som er faktisk påkrevd.

Gulvet gjelder også på nivå 4. Å skru dette opp gjør teksten mindre selvutstillende, aldri
mindre kvalifisert. Skjer det siste, er kalibreringen brukt feil, og review skal si det.

### Markørene

Hver markør **omskrives**. Den slettes ikke, og innholdslåsen gjelder uendret: arbeidsgiveren
skal lære nøyaktig det samme av den omskrevne setningen. Sletting er bare tillatt der
innholdslåsens egen slettelisens allerede gjelder.

| ID | Markør | Omskriving |
|---|---|---|
| M1 | Teksten definerer arbeidsgiverens eget oppdrag før kandidatens ståsted er etablert | Fjern definisjonen. La kandidatens dokumenterte arbeid bære det samme poenget. |
| M2 | Påstand om eksakt treff, særlig mot en definisjon teksten selv nettopp ga | Bytt treffpåstanden mot gjenkjennelse: hva kandidaten kjenner igjen, ikke hvor godt han passer. |
| M3 | Arbeidsgiverens oppgave framstilt som en anvendelse av kandidatens erfaring | Snu retningen: hva kandidaten gjør for oppgaven, ikke hva oppgaven gjør for kandidaten. |
| M4 | Kandidaten rangerer sin egen evidens for leseren | Stryk rangeringen. Rekkefølgen i teksten sier det allerede. |
| M5 | Annonsert abstraksjonsnivå brukt som tekstens organiserende grep | Behold strukturen, fjern kunngjøringen av den. |
| M6 | Stående selvkarakteristikk (`Mitt bidrag er å …`, `Arbeidet mitt omfatter …`) | Bytt mot den konkrete handlingen som allerede står i samme avsnitt. |
| M7 | Relevansbroen bygget mer enn én gang | Behold den sterkeste. Én tydelig kobling er nok. |
| M8 | Mer enn ett avsnitt som ender på en lærdom til leseren | Behold høyst én, og bare der koblingen ikke allerede er åpenbar. |
| M9 | Subjektmonotoni: en rekke setninger som begynner på `Jeg` | Varier setningsåpningen. Ikke bytt til passiv og ikke svekk verbet. |
| M10 | Brevet går ut over sitt format | Komprimer etter D Erstatnings- og komprimeringsrekkefølge. Aldri ved typografi. |

### Nivåene

| Nivå | Navn | Markører i spill |
|---|---|---|
| 0 | Av | Ingen. Sluttpussen kjører som før. Brukes for å reprodusere en historisk kjøring. |
| 1 | Lett | M4, M5, M8 — de tre mønstrene § Selvfremstilling som skal bort allerede navngir. |
| 2 | Standard | Nivå 1 pluss M1, M2, M3, M6, M7. Normalinnstillingen. |
| 3 | Fast | Nivå 2 pluss M9, M10, og en uhedget åpningstese som det følgende ikke dekker. |
| 4 | Maksimal konformitet | Nivå 3 med lavere terskel for hva som teller som markør. Har en reell kostnad i gjennomslag; ikke en standardinnstilling. |

### Registrering

Si i review hva som ble omskrevet og bekreft at gulvet holdt. Fant du ingen markører, si det.
Ingen tallverdi, ingen score, ingen kvalitetspåstand.
```

---

**P14c · Bind the pass to the knob.** `B/policy/stages/stage3_final_writer_review.md`.

Inside the content-lock blockquote, after the existing final paragraph (`:156-160`), add:

```text
>
> Then apply `V Sosial kalibrering i sluttpussen` at the level the bundle's
> `settings.voice.social_register_calibration` names. Recast every marker that
> section lists at or below that level. Recast, never delete; the content lock
> above is unchanged and the employer must learn exactly the same thing from the
> recast sentence.
```

And extend the anti-underselling paragraph at `:168-171` with one sentence:

```text
That floor is also the calibration's floor, and it does not move with the level.
`social_register_calibration` raises how much self-presentation is recast; it never lowers how
strongly a supported claim is stated. If a package comes back from a higher setting sounding
less qualified, the setting was applied wrongly — say so in the review rather than shipping it.
```

---

**P14d · The record.** `B/schemas/review.schema.json`, alongside the two existing optional
diagnostics (`material_strategy_change`, `upstream_claim_repaired`):

```json
    "register_calibration": {
      "type": ["string", "null"],
      "description": "Optional diagnostic. What the content-locked social-register pass recast, at the level settings.voice.social_register_calibration named, and confirmation that the invariant floor held. No numeric value, no score: this is a process signal, not a quality fact (Spec 7.5)."
    },
```

The file is `additionalProperties: false`, so this genuinely requires the schema edit; the shape
matches the two fields already there exactly.

---

**P14e · Surface it.** `B/runtime/jobbsok/cli.py` — include `voice.social_register_calibration` in
the **Stage-3** context bundle only, and not in Stage 1's. `STAGE3_PROMPT.md:102-107` instructs the
model to populate exactly `write.semantic_fields`, so `register_calibration` must be advertised
there too or the model will correctly decline to write it.

---

**Ship-this-first subset, if the plumbing is a burden.** P14b + P14c alone, with the level written
into `FORFATTERSTEMME.md` as *"Nivå 2 gjelder inntil `settings.toml` bærer verdien"*. That is two
policy-file edits, no schema, no code, no settings, and it delivers the inventory and the floor —
which is where the effect actually comes from. P14a, P14d and P14e turn it into a dial you can tune
and audit, and they can follow.

---

**Mitigates:** W04b directly; W04 and W16 partially (M3 and M8 are the two patterns W16 shows
escaping a lexical rule, and a named marker with a recast instruction is harder to paraphrase around
than a banned phrase).

**Mechanism.** Three things the current pass lacks, in order of contribution. A **named inventory**
converts *"do not sound self-important"* — which a model can agree with while changing nothing —
into ten specific constructions with a recast for each. An **invariant floor bound to the same
instrument** makes the safe direction structural rather than a nearby warning, so the pass cannot
buy conformity with claim strength. A **level** makes the trade-off adjustable without a policy edit,
and lets two settings be compared as branches of one run.

**Cost, and there are four real ones.**

- **Recast quality is not free.** M1, M2 and M3 are the markers whose recasts most easily lose
  content. `93c621`'s opening carries a real proposition about what the unit must do; deleting the
  presumption without deleting the proposition is genuine writing work, and a lazy application will
  produce a blander opening. The instruction says *recast, never delete* for exactly this reason,
  and the content lock backs it, but this is where the mechanic will fail first if it fails.
- **It adds a step to a pass the framework already warns about.** `STAGE3_PROMPT.md:141-144` names
  *"buying smoothness with signal"* as one of three places this stage reliably drifts. P14 adds work
  to precisely that pass. The floor is the mitigation; the review record is the detection.
- **Level 4 has a stated cost and someone will use it as a default.** The setting comment and the
  level table both say so. That is as much as policy can do.
- **A fifth optional review field is more surface.** `review.schema.json` is a small, deliberately
  disciplined artefact and this is the third optional diagnostic on it. Justified because the pass is
  otherwise unobservable, but it is not free.

**What gets worse.** At level 3 and above, letters will get slightly less distinctive. M5 and M6 are
also, in small doses, *voice* — `0fa53b-opusx`'s two-question frame is the clearest architecture in
the corpus and M5 will flatten it. The honest trade is that the corpus's most architecturally
self-aware letter is also its most self-impressed, and this dial cannot separate those two properties
perfectly. Level 2 is the default precisely because it leaves M5 alone.

**Next-run signal, written to be falsifiable.** Re-score the nine markers on the next run's letters.

- **Working:** M1, M2, M3, M6 and M7 absent; composite for the worst package below ~40; and — the
  test that matters — `used_evidence_refs`, letter word count and `requirement_coverage` are
  **unchanged or higher** than the same run at level 0.
- **Failing into W04:** any new clause matching floor items 1–4; a drop in evidence refs; or a letter
  that shortened without a marker being removed. If register improves and evidence falls, the
  mechanic has reproduced the underselling pathology in a new costume and should be reverted to
  level 1 or 0.
- **The A/B is already designed.** Branch one run at `0`, `2` and `4` from the same frozen strategy,
  exactly as the four `0fa53b` Stage-3 branches did. Same inputs, one variable, three outputs.

---

### What I would not ship

- **A CV/letter similarity detector.** `WRITING_DOCTRINE.md:496-498` forbids it explicitly —
  *"det finnes ingen automatisk likhetsdetektor i baseline, og det skal ikke bygges en"* — and it
  would be the wrong instrument anyway: the failure in W07 is a missing authoring pass, and a
  detector would push writers to paraphrase around a threshold rather than divide labour. P7 is the
  right shape.
- **A deterministic marker counter, or any numeric register score.** P14's inventory is a writing
  instrument, not a validator. Counting M1–M10 mechanically would fail a package for a formulation,
  which `WRITING_DOCTRINE.md:40-42` forbids outright, and it would immediately be gamed by
  paraphrase — W16 shows exactly that happening to a lexical rule. `review.schema.json` also bars a
  numeric quality field by design, and `register_calibration` is deliberately prose. The three
  scores in W04b are my analysis of a finished corpus, not a runtime artefact, and they should never
  become one.
- **A hard page or word validator.** Breaches `DEC-24` / `DEC-33` and
  `WRITING_DOCTRINE.md:331-342`, and would fail packages for editorial judgement. P10 gets the same
  result by moving a measurement rather than adding a gate.
- **A schema field, drop log or preservation ledger for evidence survival.** That problem —
  `EV:WORK#025` deleted by Stage 3 in three consecutive runs — was diagnosed and fixed at the
  ranking layer in the 0.9.2 pass, and the fix held: the judgement survived into `3eeb10`'s finals.
  Re-adding bookkeeping would re-solve a solved problem in the wrong layer.
- **Any per-job language, channel, portal or `letter_required` switch.** `settings.toml:7-9` and
  `DEC-01` / `DEC-02` / `DEC-04` rule it out, and nothing in this catalogue needs it.
- **Reworking `personality_facets.json`.** `PF-09`'s prevention rule — *"Do not claim universal
  communication excellence"* — is a plausible contributor to `kommunikasjon` = 0, but `PF-09` was
  not selected in any of the six strategies I inspected (selections were `PF-01`, `PF-06`, `PF-08`,
  `PF-11`, `PF-12`, `PF-19`), so the causal link is unproven, and the file is byte-identical across
  every run. Leave it. P8 addresses the symptom from the requirement side, which is where the
  evidence points.
- **Renaming the branch directories or backfilling `settings.toml`'s role mapping.** W20 is real but
  cosmetic against the rest of this list. Fix it opportunistically when a run is next created, and
  update `PERSONALITY_PROFILE.md`'s retired Stage-2 references at the same time.

---

### Shipping order, and what I expect from it

| Order | Items | Effect per unit of change |
|---|---|---|
| 1 | P1, P6, P5 | Highest. Three small text or map edits; each removes a defect that reaches every package. |
| 2 | P4 **+** P12 **+** P14b/P14c | High. The floor and the ceiling of one axis. All four are policy-text edits, no schema and no code. Shipping any one alone moves the register in a single direction, which is the failure mode all four exist to prevent. |
| 3 | P2, P3 | High, but touches code. Confine each to one control and one function. |
| 4 | P7 | High. One instruction step against a defect present in 9/9 packages. |
| 5 | P10 | High, expensive at runtime. The only fix for the three page failures. |
| 6 | P8 **+** P9 together | Highest total effect, largest blast radius. P8 without P9 risks checkbox prose; P9 without P8 lengthens the CV for no reason. New run only. |
| 7 | P14a, P14d, P14e | Medium. Turns the register pass into a dial you can tune and audit. Ship after one run at the fixed default has shown the inventory works — there is no point plumbing a setting for a mechanism that has not demonstrated an effect. |
| 8 | P13, P11 | Medium, and the two most likely to misfire. Ship after P8 so the coverage account can show whether they are working. |

If only four things ship: **P4 + P12 + P14b/P14c** as one unit, **P7**, and **P10**. That unit
covers both directions of the register axis; P7 covers the duplicated formulation in 9/9 packages;
P10 covers the artefact a recruiter sees first. None of them touches a schema or a frozen contract,
and together they are perhaps a day of careful policy-text work.
