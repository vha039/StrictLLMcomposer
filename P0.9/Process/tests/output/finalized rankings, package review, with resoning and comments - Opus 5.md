# Finalized rankings and package review — nine Avinor packages

Companion to `final optimization plan based on FW test-runs against Avinor - Opus 5.md`. The
weakness catalogue and optimisation pitch in that file were completed before the prior reports
were opened; this file is the part that reads them.

**Scope.** Nine packages. `0d1af3` and `2120b3` are excluded throughout, including from every
comparison and every table.

---

## Part 3 — The two prior reports

### 3.1 They are one report

```text
0bb47663f191087f0c7509f8528a833b8627039999f233b65ad1baa556e4b13d  draft - Comparative evaluation of 11 Avinor - Claude.md
0bb47663f191087f0c7509f8528a833b8627039999f233b65ad1baa556e4b13d  draft - Comparative evaluation of 11 Avinor - GPT.md
```

Identical SHA-256, identical byte length (56 116), identical line count (397), and `diff` returns
nothing. **The two files are byte-identical.** There is no second model's answer to cross-reference
against, and no inter-model agreement or divergence can be read from them. I treat them as one
report and refer to it as *the report* below.

That is worth stating plainly rather than passing over: whatever was intended, what is on disk is
one document under two names. If the intent was a two-model comparison, it did not happen.

### 3.2 What the report gets right

Substantial and worth adopting:

- **The framing problem is the corpus's real governing variable.** *"The candidate's strongest
  evidence of execution is the modernisation of a ~20-year-old Excel/VBA budgeting tool. It is also
  the worst possible headline for a Seniorrådgiver Digital Transformasjon."* That is correct, and
  bullet-1 choice does move a CV more than any other single decision here. I keep it, weighted as
  *altitude*.
- **Coverage failure is invisible when you review either document alone.** Its delta #7 is the
  right observation and the right level of abstraction.
- **The letter must carry what the CV structurally cannot** — constraint, rejected option, mandate
  boundary. Its delta #6 is well-founded and its scoring of `R` broadly tracks what I find.
- **`0fa53b-solxh`'s verb move.** *"Avviste direkte fordeling da bruksdata ikke ga et forsvarlig
  grunnlag"* really is the most transferable construction in the corpus. Correct and useful.
- **`b5104f`'s thesis and close are the best in the corpus.** It says so, then ranks the package
  seventh anyway — see 3.3.
- **The final honest note.** *"Not one of the eleven packages evidences porteføljestyring at group
  level, styringsgrupper, or beslutningsfora."* The observation is exactly right. The explanation
  attached to it is wrong; see 3.4.

### 3.3 Where the report is unsupported by the source text

Six corrections. Each is checkable.

---

#### 3.3.1 The "Fabrication watch" is empty. All eight flagged claims are verbatim in the frozen authority.

This is the report's largest error and it distorts three tables. Its method — *"A specific claim
appearing in one or two documents, where nine others render the same episode without it, is a
candidate generator artefact"* — is a reasonable heuristic for a corpus of unknown provenance, and
the report states the caveat honestly. But this corpus has a known provenance: each run froze a copy
of `Work_experience.md`, and the claims can simply be looked up. I looked all eight up in the
frozen authority **of the run that produced the document**.

| Flagged claim | Report's verdict | Frozen authority | Verdict |
|---|---|---|---|
| *"(Excel/VBA, om lag 15 ark og 78 globale navn)"*, `b5104f` | **Highest risk** | `PRJ-03` row: *"Arvet ca. 20 år gammelt Excel/VBA-budsjetteringsverktøy på **ca. 15 ark og 78 globale navn**"* — Gen B only, added 2026-09-06 | **Verbatim. Not a fabrication.** |
| *"Koblet data fra blant annet JIT, ADI, REGERP, GAT…"*, `b5104f` | **High risk** | Both generations: *"Koblet data fra blant annet **JIT, ADI, REGERP, GAT**, personell-/lønnsgrunnlag og DRG-/aktivitetsrapporter."* | **Verbatim. Not a fabrication.** |
| *"Microsoft Fabric, Power Platform, dbt og Pega"*, `b5104f` | Elevated | Both generations, `PRJ-07`: *"…rundt **Fabric, Power Platform, dbt, Pega** og Python"* | **Verbatim. Not a fabrication.** |
| *"Registrert som superbruker for kunstig intelligens ved OUS i om lag tre år"*, `0fa53b` | Elevated; *"arithmetically tight against a 03.2023 start"* | Gen B: *"Vegard er registrert som «SuperBruker – Kunstig intelligens» ved OUS og har hatt betegnelsen **i om lag tre år**. … **Bekreftet 2026-09-06.**"* | **Verbatim, and explicitly confirmed. Not a fabrication.** |
| *"la til GAM-modellering"*, `0fa53b-opusx` | Moderate; *"generator adding technical texture"* | Both generations, `PRJ-05`: *"…automatisering, integrasjon, **GAM**, SARIMAX-evaluering…"* | **Verbatim. Not a fabrication.** |
| *"bemannings-, UTA- og vaktgrunnlag"*, `0fa53b-opusx` | Moderate; *"An inserted sector acronym"* | Both generations, BAR row: *"kvalitetssikring av **bemannings-, UTA- og vaktgrunnlag**"* | **Verbatim, same phrase. Not a fabrication.** |
| *"lekkasjekontroll"*, `3eeb10-stage1` | Low | Both generations: *"time-aware holdouts, **leakage checks**"* | Translation of a supported term. Report's verdict correct. |
| *"Fem arbeidsbøker"*, `3eeb10-stage1` | Cleared by arithmetic | Gen B, `PRJ-06`: *"**fem arbeidsbøker** med fire grenmodeller og én konsolideringsmodell"* | Directly supported, not merely inferable. Report's conclusion correct, its reasoning unnecessary. |

**Eight flags, seven scored as risk, zero fabrications.**

The arithmetic objection to the superuser claim is itself wrong twice over. The designation is not
scoped to OUS tenure — nothing ties it to the employment start — and even if it were, March 2023 to
September 2026 is three and a half years, so *"om lag tre år"* is not tight against it at all.

**What this cost.** The report set `b5104f`'s CV credibility sub-score to **62**, the lowest in its
table, and applied an explicit override — *"−1.3 … four uncorroborated specifics against a stated
background check are under-priced by C alone"* — dropping the CV to fifth. At package level it set
`Z = 58`, again the lowest, and ranked `b5104f` **seventh of eleven** while describing its letter as
having the *"Best thesis and boldest close in the corpus"*. The penalty is entirely spurious and it
lands hardest on the package that used the most evidence.

There is an internal contradiction here too. The report's own CV rubric defines the **top** anchor
for credibility as *"Corroborated specifics + volunteered limits (`dels innført og dels foreslått`,
`ble avviklet`)"*. Both quoted phrases are `b5104f`'s. It scores `b5104f` 62 on the category whose
top anchor it illustrates with `b5104f`'s own text.

In fairness to the report, `EVAL_PROMPT.md:70` instructed it to do exactly this: *"A claim, number,
title, or achievement that appears in only one or two packages is a candidate hallucination from the
generator. Flag every such claim … and penalise it under credibility."* The heuristic was handed to
it. It is still wrong for this corpus, and the report had the means to check.

---

#### 3.3.2 The 2026 vs 2026-and-2027 split is an authority-generation artefact, not a quality difference

The report treats the extra year as earned:

> **2 vs 3 (stage1 → 3eeb10-base):** completeness of outcome. stage1 states *"i sykehusdekkende bruk
> i budsjettprosessene for 2026 og 2027"*; base stops at *"budsjettet for 2026"*. Same work, one
> extra year of demonstrated adoption.

It is not the same work with one extra year claimed. The `PRJ-03` row in `Work_experience.md`
changed on 2026-09-06:

- Gen A (`3eeb10`, `93c621`, `6d65bd`): *"2025 version used for 2026 budget; broader 2027
  redevelopment active"*.
- Gen B (`3eeb10-stage1`, `b5104f`, `0fa53b` family): *"Sykehusdekkende bruk i budsjettprosessene for
  2026 og 2027; 2027-moderniseringen ferdigstilt, bekreftet 2026-09-06"*.

`3eeb10` was frozen on 5 September. It **could not** have written the 2027 claim without inventing
it, and `93c621`'s review records the boundary being observed deliberately: *"uten … påstander om den
pågående 2027-versjonen"*. Ranking a Gen A package down for it penalises correct behaviour.

The same applies to the allocation model. Gen A's `PRJ-06` row reads *"Architecture supported;
implementation/adoption unresolved"*; Gen B's reads *"`COMPLETED`: model finished early 2026 and
handed over to controllers, confirmed 2026-09-06"*. So `3eeb10`'s *"Modellen er utformet; innføring
og endelige vekter er ikke avklart"* and `93c621`'s *"modellen er utformet, ikke innført"* are
faithful renderings of their frozen facts. The report reads them as candour, which is generous but
also wrong in mechanism: they were mandatory.

The report does notice the split — *"One divergence that is not fabrication … both are defensible;
the later variants simply claim the additional year"* — and then prices it anyway in the head-to-head
reasoning. The correction is to neutralise it entirely, which is what I do in Part 4.

---

#### 3.3.3 It never saw the render reports, and its top three packages contain all three page failures

The report evaluates the extracted text. It never opens `render_report.json`, so it cannot see that:

- `0fa53b`'s CV renders to **three pages**;
- `3eeb10-stage1`'s CV renders to **three pages**;
- `0fa53b-opusx`'s letter renders to **two pages**.

Its package top three is `3eeb10-stage1`, `0fa53b-opusx`, `0fa53b` — precisely those three.

It is not blind to length. It scores `0fa53b`'s scannability at 58, calls `opusx` *"1279 words, the
heaviest set here"*, and notes `3eeb10-stage1`'s core-areas block is *"a wall exactly where a
recruiter needs a scan"*. But it prices length as a sub-score in a weighted sum rather than as a
threshold event. A three-page CV for a three-and-a-half-year career is not one component among
seven: it is the first thing the reader perceives, and for a role that is *about* prioritisation it
contradicts the pitch. `0fa53b`'s own review makes the framework's view explicit — it compressed
once, failed, and left an instruction for the human to check the page count.

I weight it as a threshold. That single correction moves `0fa53b` from third to sixth at package
level and is the largest mechanical driver of my divergence.

---

#### 3.3.4 The `93c621` punctuation error is not an error

> **`93c621`** … Weakest move: a bokmål punctuation error in that same sentence (capitalised *"Det"*
> after a colon, where lowercase is required), in a document whose entire claim is precision.

The sentence is *"Avinors nye transformasjonsmiljø skal gjøre mer enn å foreslå teknologi: Det skal
gi ledelsen grunnlag for å prioritere, og hjelpe organisasjonen å realisere verdi i endringer som må
fungere i drift."*

Norwegian orthography takes a capital after a colon when a complete sentence follows, and lowercase
when a fragment or list follows. *"Det skal gi ledelsen grunnlag for å prioritere…"* is a complete
sentence. The capital is correct. Lowercase would be the deviation. The report docked `93c621`'s
Norwegian sub-score to 78 — the lowest in its letter table — for a rule it inverted.

It also missed the genuine defect in the same sentence. `FORFATTERSTEMME.md:139-141` bans exactly
this opening: *"`Når <arbeidsgiver> skal <X>, må <Y> …` som standardåpning. En åpning som bare
refererer arbeidsgiverens egen situasjon tilbake til dem, bruker den viktigste setningen i brevet på
noe leseren allerede vet."* The report calls the opening *"a confident register"* and scores it 82.
Its instinct that something is wrong with the sentence was right; it found the wrong thing.

---

#### 3.3.5 `0fa53b-solmed`'s "firepersoners analyseavdeling" is authority-verbatim, not a slip

> Weakest move: … *"Deltok i etableringsgruppen for en firepersoners analyseavdeling"* misstates the
> fact every other variant renders correctly — it was a four-person *group establishing* the
> department, not a four-person department.

The frozen `Work_experience.md` for that run, `PRJ-01`: *"Greenfield styrings-BI i **en
firepersoners analyseavdeling**"*, and §8 *Godkjente måltall*: *"**Four-person analysis
department** | Team/context scale"*. The department is four people. `solmed`'s phrase is the
authority's own, and the group that established it is separately four people; both are true and
`solmed` states the first. The report's correction is the error, and it used it to drop `solmed`'s
CV to seventh.

---

#### 3.3.6 "b5104f concedes nothing anywhere" is false, and the overlap percentages are unreproducible

> **`b5104f`** … Weakest move: **zero concessions anywhere.** The letter never says what he doesn't
> have.

The letter does not, correctly — see 3.4. The **CV** carries five bounded limits: *"Kolleger ledet
innhold og visuell utforming"*; *"Eide løsningen fra ca. august 2025 til februar 2026, da den ble
avviklet"*; *"dels innført og dels foreslått"*; *"brukt på prosjektnivå"*; *"Deltok i tidlig tilgang
og piloter"*. The report's package-level claim — *"nothing anywhere in the set says what the
candidate does not have"* — is contradicted by five clauses in the document it just finished
scoring.

On overlap: the report reports *"11.2% of the letter's 5-grams appear in the CV"* for `opusx`,
*"4.3%"* for `solmed` and *"2.0%"* for `6d65bd`, with no stated method. I could not reproduce those
figures and the ordering they imply is partly wrong: on sentence-level similarity, `6d65bd` — the
claimed lowest — has a 0.93 pair, while `solmed`, the claimed middle, has a 0.95. More importantly,
a 5-gram percentage smears the signal that actually matters, which is that **four of the nine
packages ship a sentence that is character-for-character identical in CV and letter**:

- `0fa53b`, `0fa53b-opusx`, `3eeb10` — *"Rammeverket ble innført som sykehusdekkende standard og var
  fortsatt i bruk om lag [to og et halvt / 2,5] år senere."*
- `b5104f` — *"Verktøyet er i sykehusdekkende bruk i budsjettprosessene for 2026 og 2027."*

That is a named doctrine violation (`WRITING_DOCTRINE.md:291-293`) present in every package, and the
report does not register it.

### 3.4 Where the report judged on something other than the documents

Two places, both consequential.

**The concession heuristic is undifferentiated.** The report's delta #2 is *"Concede something
specific, in the letter"*, and it applies it uniformly: `3eeb10-stage1`'s aviation line, `solmed`'s
mandate line and `solxh`'s authority line are all scored as virtues, and the report's Phase 6 edit
list recommends *importing* `solmed`'s mandate sentence into the hybrid *"instead of leaving the
reader to find the gap"*.

These are not the same move.

- *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn."*
  costs almost nothing. The recruiter can already see there is no aviation on the CV; naming it
  first converts a visible fact into evidence of self-knowledge, and `3eeb10-stage1` immediately
  turns it into the argument.
- *"Rollen min har vært prosjekt- og metodeorientert, ikke et formelt konsernmandat for portefølje-
  eller programledelse."* costs a great deal. The ad lists `porteføljestyring` under *"er en
  fordel"* — a preference, not a minimum — and this sentence converts a preference the screener
  might not have checked into a stated gap, in the candidate's own voice, in the ad's own noun.

The framework's own policy takes my side. `PERSUASION_CALIBRATION.md:129`: *"Unngå et defensivt «jeg
mangler X»-avsnitt med mindre taushet ville villede vesentlig."* Silence would not mislead here: no
package claims a corporate mandate anywhere. And
`Other_high_value_information.md:247` says where such a caveat belongs — *"keep non-disqualifying
caveat **review-only**"*. Every one of these limits is already recorded in `review.json`
`known_limitations`, which is the channel that exists for it. The report scored up a move the
system it was evaluating scores down, without checking.

**"The underlying experience isn't there."** The report's closing corpus-wide note:

> Not one of the eleven packages evidences porteføljestyring at group level, styringsgrupper, or
> beslutningsfora … **No amount of reordering fixes it, because the underlying experience isn't
> there.** The three packages that say so out loud are the ones that survive an interview.

The observation is right. The diagnosis is wrong, and it is the kind of wrong that changes what you
would do about it. Stage 1 for `0fa53b` rates **R10** — *"Utarbeide analyser, beslutningsgrunnlag og
presentasjoner for ledelse og styringsgrupper"* — as `IMPORTANT` / **`SUPPORTED`**, with evidence
refs attached, and **R13** — *"styringsmodeller, beslutningsprosesser eller porteføljestyring"* — as
`DESIRED` / **`SUPPORTED`**. `Work_experience.md` §6.9 carries *"Executive/management decision
support"* and *"Workshops/presentations for mixed audiences"*; §5.2 carries *"decision notes,
executive summaries, workshops, documentation and onboarding"* adapted *"to controllers, managers,
specialists and technical teams"*.

Bounded evidence for R10 and R13 exists and the framework rated it as such. It did not reach
employer text, in nine of nine packages, because of the mechanism traced in the companion document:
requirement coverage is computed at Stage 1 and has no consumer at Stage 3, and the deletion order
ranks the employer's own vocabulary first. That is a framework defect with a specific fix. "The
experience isn't there" would mean there is nothing to do.

The report could not have seen this — its prompt scoped it to twenty-two documents and it never
opened the repository. I note it as the boundary of its method rather than as carelessness.

### 3.5 Deep reading of the six packages in the report's top-5s

Union of its CV top 5, letter top 5 and package top 5: `0fa53b-opusx`, `3eeb10-stage1`, `3eeb10`,
`0fa53b-solxh`, `b5104f`, `0fa53b`. All six are in scope; none of the excluded packages appears.
Reading each as CV, letter, and pair.

---

#### `b5104f` — the report's CV 5th, letter 4th, package 7th

**CV.** The best requirement-mapped CV in the corpus after `3eeb10`, and the densest.
`used_evidence_refs` = 19, second only to `3eeb10-stage1`. Headline —
*"SAMFUNNSØKONOM OG RÅDGIVER | GEVINSTREALISERING, STYRINGSMODELLER OG KONTROLLERT DIGITAL
ENDRING"* — takes `styringsmodeller` from *"Vi tror du har"* and earns it below. The `PRJ-03` bullet
is the only option appraisal in the corpus: *"Vurderte VBA, Office Scripts, Python og KI-støttede
alternativer mot kompatibilitet, driftsrisiko og vedlikeholdbarhet"* — which is what a
seniorrådgiver does, as distinct from what a developer does, and it is the most direct available
answer to the ad's *"God forståelse for hvordan teknologi kan skape forretningsverdi"*. It is also
one of only two CVs carrying `PRJ-09`: *"Designet og evaluerte i tillegg arbeidsinntak,
spørreskjemaer og kravstruktur … brukt på prosjektnivå."*

Its review shows this was deliberate, not luck:

> "PRJ-07 … og PRJ-09 … er tatt inn i CV-en selv om de ikke sto i evidensplanen, fordi annonsens
> punkter om arbeidsformer og teknologiforståelse ellers ville hvilt på arbeidsmodellen alene."

That is requirement-coverage reasoning, performed by hand, in the one package that has it.

Real faults: the last competency is a tool list (*"Plattformutforsking: Microsoft Fabric, Power
Platform, dbt og Pega"*), the 96-character headline is the longest in the corpus and will wrap as an
all-caps banner, and it carries a numeral-convention split against its own letter (`2,5` / `50` in
the CV, *"to og et halvt"* / *"femti"* in the letter).

**Letter.** The best in the corpus and I do not think it is close. The thesis is the ad's premise
restated as a conviction: *"Et gjennomgående tema i arbeidet er avstanden mellom hva en investering
ble begrunnet med og hva som senere lar seg vise. Den avstanden lukkes av at gevinstlogikken er
avklart før pengene brukes, ikke av flere rapporter etterpå."* It is the only letter that uses an
Avinor fact — *"Avinor driver 43 lufthavner og flysikringstjenesten, og den nye enheten skal øke
gjennomføringskraften i noe som allerede må virke hver dag"* — and the only one that then converts
it: *"kontroller er det som gjør endring mulig, ikke det som utsetter den."* The close asks the
employer a question — *"hvordan enheten tenker å måle verdien av initiativene den skal prioritere
mellom"* — which is the only closing in the corpus that escapes the pattern banned at
`FORFATTERSTEMME.md:133` by doing something else rather than by rewording it.

**Pair.** Combined 1 124 words, CV two pages, letter one — the only substantial package that is
mechanically clean throughout. The division of labour is real: the CV records the option appraisal,
the letter narrates the decision inside it. Against that: one verbatim-shared sentence, the sterile
logistics episode at near-equal length in both, and the numeral seam.

**Verdict.** The report ranked this seventh of eleven at package level on a credibility penalty that
does not survive checking, and on a "zero concessions" claim contradicted by five clauses in the CV
it had just read. Removing the spurious penalty and adding the render evidence makes it the
strongest package in the corpus on my rubric. This is my largest divergence.

---

#### `3eeb10-stage1` — the report's CV 2nd, letter 3rd, package 1st

**CV.** The most evidence-dense document here: 23 `used_evidence_refs`, comfortably the highest, and
the only Gen B CV besides `b5104f` that carries `PRJ-09` (*"arbeidsinntak og kravavklaring,
oppgavenedbryting, avhengigheter, arbeidsmengde og prioritering"*). Profile is genuinely distinctive
— *"Arbeider med å få digitale forbedringer gjennom i virksomhetskritiske prosesser som ikke kan
stanses underveis"* — and it volunteers limits twice. Its review is the most thorough in the corpus,
with eleven `known_limitations` and an upward repair of an understatement in the forecasting
ownership.

And it renders to **three pages**. Seven competencies of 15–25 words each, thirteen bullets, and the
template's twelve lines of 2013–2020 furniture on top. For a three-and-a-half-year career this is a
prioritisation failure in a document applying for a prioritisation role. The report scores its
scannability 68 and moves on; I treat it as a threshold event, which is what separates my second
place from its first.

Its other real fault is ordering: bullets one and two are the budget tool. A reader of a Digital
Transformasjon CV spends the first fixation on a legacy Excel workbook.

**Letter.** Second best in the corpus, and it contains the corpus's single best move:

> "Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn. Det
> er at dere driver noe som ikke kan settes på pause mens det forbedres."

Three short sentences that pre-empt the obvious objection, decline to manufacture a domain bridge,
and convert the refusal into the actual argument. It is backed by voluntary downscaling —
*"Jeg var med i firepersonsgruppen som etablerte Analyseavdelingen, **i langt mindre skala**"* — and
by an unusually plain register: *"Det arbeidet handlet mest om det udramatiske: hvordan oppdrag tas
inn og avklares, hvordan arbeid prioriteres, og hvilke arbeidsformer vi faktisk holdt fast ved i
motsetning til dem vi bare foreslo."* Against it: the opening is *"Jeg søker stillingen som…"*
followed immediately by the budget tool, so paragraphs one and two are both Excel.

**Pair.** The most consistent set in the corpus. Both documents say *"budsjettprosessene for 2026 og
2027"*, both spell numerals out (*"rundt femti"*, *"to og et halvt"*, *"tjue år"*), both hedge the
same episodes the same way. Complementarity is the highest here — the letter concedes what a CV
cannot. The set's cost is the three-page CV and that both documents open on the tool.

**Verdict.** The report's package first place is well-argued and I nearly keep it. It goes second
only because of the render evidence the report did not have.

---

#### `3eeb10` — the report's CV 3rd, letter 5th, package 4th

**CV.** Under-appreciated by the report, and on one dimension the best in the corpus. Its
`KJERNEOMRÅDER` is the only competency block that maps the ad's requirement language directly:

> "Styringsmodeller, beslutningsprosesser og strukturert arbeidsinntak · **Beslutningsgrunnlag,
> analyser og presentasjoner for ledelse og styringsgrupper** · …"

That second item is the ad's R10 in the ad's own words, and it is the corpus's only occurrence of
`styringsgrupper` anywhere. The first is R13. No other CV names either. The report never mentions
this, which is a miss: it is the single clearest instance of a package answering a requirement the
other eight leave silent.

The honest limitation is that it is asserted rather than earned — there is no bullet beneath it
showing a decision paper going to a styringsgruppe. Still: a recruiter scanning for the phrase finds
it here and nowhere else. Elsewhere the CV is solid: 13 refs, two pages, 633 words, `styringsmodeller`
also in the headline. Its fault is ordering — bullet one is the budget tool, again.

**Letter.** This is where I depart from the report most sharply. It scores the letter fifth of
eleven at 85, with *"P — Vacancy engagement"* at **88**.

The letter body never writes the word **Avinor**. The only occurrence in the file is the
template-filled address block. It names the unit twice — *"seniorrådgiver i Digital Transformasjon"*,
*"den nye enheten"* — and contains no fact about the employer, no reference to aviation,
infrastructure, safety, the samfunnsoppdrag or the unit's stated mandate. Substitute Statnett, Bane
NOR, Vegvesenet or Helse Sør-Øst for Avinor and every sentence remains true and appropriate. That is
the framework's own `Arbeidsgiverbyttetesten` (`WRITING_DOCTRINE.md:431-455`) failing on its first
criterion: *"åpningen fortsatt passer uten andre endringer"*. A vacancy-engagement score of 88 is not
supportable.

What the letter does have is the best prose in the corpus. *"Jeg tok den rammen og kjøpte
forsvarligheten med kontroll i stedet for med omfang"* is the best single sentence in eighteen
documents, and *"Der gevinsten ikke lar seg måle direkte, gjør jeg heller forutsetningen synlig enn
å lage presisjon som ikke finnes"* is the clearest statement of professional principle anywhere
here. The close asks about them — *"hvordan den nye enheten arbeider nå"* — which is good. Paragraph
two is also the most technical passage in any letter (*"logikken lå spredt mellom formler, navngitte
områder og makrokode i kopier som hadde vokst fra hverandre"*), and the report is right that it
frames the candidate downward.

**Pair.** Mechanically the cleanest substantial set: 633 + 399 = 1 032 words, two pages plus one,
perfect numeral consistency, no factual drift. Its weakness is that both documents lead with the
tool and both carry the same allocation-model hedge in near-identical form.

**Verdict.** The report has the CV about right and the letter too high. On my rubric the CV rises
(the R10/R13 mapping is worth real credit) and the letter falls hard (employer-blind), and the two
roughly cancel at package level.

---

#### `0fa53b-opusx` — the report's CV 1st, letter 2nd, package 2nd

**CV.** Excellent, and the report's first place is defensible. Ordering is exactly right for this ad
— method, then investment basis, then delivery, then work design — and the profile ends on a real
point of view: *"Jeg vurderer hva et gevinstanslag kan bygge på, og gjør forutsetningene synlige for
dem som skal bruke tallene."* The proxy-model bullet is the most complete piece of evidence anywhere
in the corpus. Against it: the `KJERNEOMRÅDER` block is 81 words, the longest here, and under W08
that is 81 words of solid bold; `used_evidence_refs` is 12, mid-table; and it drops `PRJ-01` and
`PRJ-09` entirely.

**Letter.** The best-architected letter here. The two-question thesis is stated and then executed:
*"arbeidet mitt har i hovedsak dreid seg om to spørsmål: hva et gevinstanslag kan bygge på når
datagrunnlaget er svakt, og hva som skal til for at en digital endring faktisk blir tatt i bruk."*
It shows an integrity decision rather than a technical one — *"I stedet for å presentere indirekte
tall som observert bruk, utformet jeg en vektet proxymodell"* — and its concession is the
best-executed of the four, negation immediately recovered.

Two faults the report half-sees. The opening, *"Jeg søker stillingen som seniorrådgiver i Digital
Transformasjon"*, is the fourth statement of the role in four lines (W09), so the letter's most
valuable sentence carries no information at all. And it **renders to two pages** at 551 words. For a
Norwegian søknad that is a recognised negative signal, and the framework's own target
(`settings.toml:77`) is one. There is a small prose fault too: *"Jeg stiller gjerne til samtale, og
går da **gjerne** nærmere inn på…"* repeats the adverb inside one sentence.

**Pair.** 714 + 551 = 1 265 words, the heaviest set. Perfect internal consistency, genuine division
of labour — the letter supplies the rejected option, the mandate constraint and the deliberate
design choice, none of which the CV carries. One verbatim-shared sentence.

**Verdict.** The report's CV first place is reasonable; I put it second behind `b5104f` on coverage.
Its letter second place is too high once the page overrun is priced. Package fourth rather than
second.

---

#### `0fa53b` — the report's CV 6th, letter 1st, package 3rd

**CV.** The richest and the least disciplined: 825 words, 16 refs, eight competencies, a five-line
bullet on AI working method, and **three pages**. The AI material is genuinely distinctive —
*"prosjektinstruksjoner med omfang, kildepresedens og stoppregler, tilstands- og
overleveringsdokumentasjon, tester og bevisplikter"* — and the ad never asks for it. It also carries
the honest BI dating that ends on *"Løsningen ble avviklet i februar 2026"* (W05).

**Letter.** The report's first place, and it is a strong letter. The opening is the best in the
corpus and the only genuine in-medias-res: *"Da gevinstene fra et sterilforsyningsprosjekt ved Oslo
universitetssykehus skulle fordeles mellom klinikkene, fantes det ikke bruksdata som bar en direkte
fordeling."* The judgement content is deep, and the single ad-phrase it uses is used as a hook, not
filler.

Where I part company is the sentence the report calls *"the corpus's most trust-building sentence"*
and *"the highest-value two sentences in the corpus"*: *"Målt tidsbesparelse eller feilreduksjon har
jeg ikke tall på. Det som er dokumentert, er at verktøyet er i bruk."*

I read it as a net cost, for three reasons. It answers the ad's **first** responsibility bullet —
*"Sikre at digitale initiativer gir målbar verdi og gevinst"* — with a flat statement that the
candidate has no numbers. It is ordered negation-first, recovery-second, so the clause that lands is
the negative one. And nothing in the letter would have misled without it: no measured saving is
claimed anywhere, which is exactly the condition under which
`PERSUASION_CALIBRATION.md:129` says the defensive move should be omitted, and the limit is already
in `review.json`. `opusx` makes the same move better, at lower cost, in a less damaging position.
This is a judgement call and the report's is defensible; I think it is wrong, and the framework's
own policy agrees with me.

**Pair.** 825 + 423 = 1 248 words, and the CV is three pages. The AI material has no counterpart in
the letter, so it reads as an unresolved tangent. The review candidly records that compression was
attempted and delegates the re-check to the human.

**Verdict.** Letter third rather than first; CV falls on the page overrun; package sixth rather than
third. Worth saying plainly: **deleting two CV bullets would put this package back into the top
three.** The content is there; the discipline is not.

---

#### `0fa53b-solxh` — the report's CV 4th, letter 6th, package 5th

**CV.** The best-edited document in the corpus, and I agree with the report on the verb:
*"Avviste direkte fordeling da bruksdata ikke ga et forsvarlig grunnlag, og utformet i stedet en
vektet proxy-modell med synlige forutsetninger og vekter."* Judgement verbs read senior; construction
verbs read technical. Six competencies, seven bullets, 478 words, comfortably within budget.

The cost is severe and the report names it: `used_evidence_refs` = 7, tied for lowest. Its own review
records the deletions — *"Strategiens bredere CV-rute er komprimert ved å utelate KI-arbeid og
tverrorganisatorisk Power BI-kompetanseoverføring"* — and the BI ownership, the forecasting work and
`PRJ-09` all go with them. For a candidate whose open question is seniority and breadth, this is a
document that answers the question in the wrong direction.

**Letter.** Balanced, correctly sequenced and, as the report says, unmemorable. It names Avinor more
often than any other letter (five occurrences) without ever saying anything about Avinor. Its
concession — *"Min påvirkning har i hovedsak vært funksjonell … ikke gjennom linje- eller
programmyndighet"* — is the self-negation problem of W04, and its close is the banned pattern
reworded (W16).

**Pair.** 852 words, the second-fastest set, and the least additive: the letter walks the CV's
bullets in the CV's order with connective tissue, at 0.98 sentence similarity on one pair. Combined
coverage is the thinnest of the six packages here.

**Verdict.** The report's CV fourth is roughly right, though for different reasons than it gives.
Its package fifth is too high: on combined coverage and division of labour this is the weakest of
the nine, and I rank it ninth.

---

## Part 4 — My rankings

### 4.1 The ranking foundation

**What this vacancy actually selects on.** Seven responsibility bullets, seven *"Hvem er du"*
bullets, five *"Vi tror du har"* bullets, and no hard minimum beyond higher education. The ad says
outright that background may vary — *"Du kan ha erfaring fra strategiske roller, utviklingsmiljøer
eller operasjonelt lederansvar — det viktigste er at du forstår hvordan endring faktisk skjer"* —
and that the unit is being built from scratch. A screener working through a large pile is checking
breadth against a long list and forming a category impression in the first fixation.

**What that implies for weighting.** Two things do not discriminate in this corpus and should not
carry weight. First, **facts**: they are fixed, one person, one authority. Second, **credibility**:
I verified every single-occurrence specific against the frozen authority and found zero
fabrications, so a credibility axis would score nine packages within a few points of each other and
add noise. What does discriminate is **how much of the requirement surface the package touches**,
**at what altitude it places the candidate**, and **whether the artefact is one a recruiter can
actually read in the time available**. So coverage and altitude dominate, mechanics is weighted
like a real category rather than a tiebreak, and calibration is weighted modestly — where its
discriminating content is not truthfulness but whether the package talks itself down.

**CV**

`Score = 0.26·K + 0.20·E + 0.18·M + 0.14·A + 0.12·C + 0.10·N`

| Cat | Measures | W |
|---|---|---|
| **K — Requirement coverage** | How many of the ad's twelve substantive requirement themes the CV touches, and whether the ad's own terms appear where the evidence covers them | .26 |
| **E — Evidence density and mechanism** | Named artefacts, scale markers, decisions and controls per unit of text; `used_evidence_refs` as a cross-check | .20 |
| **M — Recruiter mechanics** | Rendered page count against the two-page budget; payload in the top third; competency-block length; bullet discipline | .18 |
| **A — Positioning altitude** | Senior adviser or technical specialist. Bullet-1 choice, headline, where the tools sit | .14 |
| **C — Claim calibration** | Authority-faithful and non-inflated **and** not self-negating. Penalises both directions | .12 |
| **N — Norwegian and distinctiveness** | Bokmål quality, register, and whether a sentence could only be this person's | .10 |

**Letter**

`Score = 0.22·S + 0.20·J + 0.18·K + 0.16·A + 0.14·C + 0.10·N`

| Cat | Measures | W |
|---|---|---|
| **S — Employer specificity** | Survives `Arbeidsgiverbyttetesten`: names Avinor facts, addresses a decision problem only Avinor has | .22 |
| **J — Judgement shown** | Constraints accepted, options rejected, trade-offs named — what a CV structurally cannot carry | .20 |
| **K — Requirement conversion** | The ad's demands turned into the candidate's own evidence, and how much of the surface is reached | .18 |
| **A — Architecture, opening and instrument fit** | Thesis, first 25 words, close, and whether it fits on one page | .16 |
| **C — Calibration** | Hedge placement and cost. Domain concession rewarded; self-negation on a DESIRED requirement penalised | .14 |
| **N — Prose** | Rhythm, syntactic variety, register | .10 |

**Package**

`Score = 0.26·G + 0.22·R + 0.20·M + 0.16·X + 0.16·Z`

| Cat | Measures | W |
|---|---|---|
| **G — Combined coverage** | What the *set* reaches across both documents, including whether the set ever says why Avinor | .26 |
| **R — Division of labour** | Does the letter add reasoning the CV cannot; verbatim reuse penalised | .22 |
| **M — Set mechanics** | Both page budgets, combined length, what each document opens on | .20 |
| **X — Consistency** | Facts, numeral convention, hedge alignment across the pair | .16 |
| **Z — Credibility posture** | Net of supported strength against volunteered disqualification | .16 |

**Neutralised throughout.** The Gen A / Gen B authority split (§3.3.2). `3eeb10`, `93c621` and
`6d65bd` are scored against what their frozen authority permitted, so no package gains or loses for
the 2027 budget process or the `PRJ-06` handover.

---

### 4.2 CV top 5

| # | Package | Score | K .26 | E .20 | M .18 | A .14 | C .12 | N .10 | Reasoning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **`b5104f`** | **88** | 92 | 94 | 76 | 92 | 88 | 84 | The broadest requirement reach in the corpus (10 of 12 themes) and the densest evidence at 19 refs, with `styringsmodeller` taken from *"Vi tror du har"* and earned immediately below it. The only CV showing an option appraisal — *"Vurderte VBA, Office Scripts, Python og KI-støttede alternativer mot kompatibilitet, driftsrisiko og vedlikeholdbarhet"* — which is the most direct answer available to the ad's technology-value bullet, and one of only two carrying `PRJ-09` arbeidsinntak evidence. Its review proves the coverage was reasoned, not accidental. Every specific is verbatim in its frozen authority; the report's four "fabrication" flags do not survive checking. Costs: 96-character all-caps headline, a tool list as the final competency, and a numeral convention that does not match its own letter. |
| 2 | `0fa53b-opusx` | 85 | 84 | 86 | 72 | 94 | 86 | 90 | The best-ordered CV for this specific ad: gevinstmetodikk, then investment basis, then delivery, then work design. Profile lands a genuine point of view — *"Jeg vurderer hva et gevinstanslag kan bygge på, og gjør forutsetningene synlige for dem som skal bruke tallene"* — and the proxy-model bullet is the most complete single piece of evidence anywhere here. Held off first place by reach rather than quality: 12 refs, `PRJ-01` and `PRJ-09` dropped entirely, and an 81-word competency block that is the longest in the corpus and, under the bold defect, the heaviest to look at. |
| 3 | `3eeb10` | 82 | 88 | 84 | 76 | 70 | 84 | 88 | The only CV in the corpus that answers R10 in the ad's own words — *"Beslutningsgrunnlag, analyser og presentasjoner for ledelse og styringsgrupper"* — and one of two that names R13's `styringsmodeller`. The prior report missed both. Profile converts the ad's *"bygge bro"* rather than quoting it: *"Arbeidet mitt ligger der teknologi, økonomi og organisasjon møtes."* The R10 line is asserted rather than earned by a bullet beneath it, and the document opens on the twenty-year-old budget tool, which is the wrong first fixation for this role. Scored against its own Gen A authority throughout. |
| 4 | `0fa53b-solxh` | 80 | 76 | 68 | 90 | 86 | 82 | 88 | The best-edited document in the corpus and the sharpest verbs — *"Avviste direkte fordeling da bruksdata ikke ga et forsvarlig grunnlag"* puts the decision in the verb, which no other CV does. Six competencies, 478 words, well inside the page budget, correct ordering. It bought that cleanliness by deleting the BI ownership, the forecasting work, the AI method and `PRJ-09`, landing at 7 evidence refs, tied lowest. For a candidate whose open question is breadth, an under-armed CV answers it the wrong way. |
| 5 | `3eeb10-stage1` | 80 | 88 | 94 | 52 | 70 | 90 | 88 | The richest record here — 23 evidence refs, the highest in the corpus, `PRJ-09` present, and two volunteered limits in a document where nobody would have checked. Its profile is the most memorable: *"…virksomhetskritiske prosesser som ikke kan stanses underveis."* It **renders to three pages**, which for a three-and-a-half-year career is a prioritisation failure in a CV applying for a prioritisation role, and bullets one and two are the Excel tool. The closest call in this table: on raw material it beats `solxh` easily, and on the artefact a recruiter receives it does not. |

Ranked 6–9: `6d65bd` 78, `0fa53b` 77, `0fa53b-solmed` 77, `93c621` 76. `0fa53b` has the corpus's
richest content and its worst discipline — 825 words, three pages, an off-target AI essay, and a
bullet ending on *"Løsningen ble avviklet"*. `93c621` is last on evidence: 438 words, 7 refs, and
`PRJ-01`, `PRJ-05` and `PRJ-10` dropped entirely, with eight interchangeable noun-pairs in the
competency block.

---

### 4.3 Letter top 5

| # | Package | Score | S .22 | J .20 | K .18 | A .16 | C .14 | N .10 | Reasoning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **`b5104f`** | **90** | 92 | 88 | 90 | 94 | 84 | 88 | The best thesis in the corpus, and it is the ad's own premise turned into a conviction: *"Den avstanden lukkes av at gevinstlogikken er avklart før pengene brukes, ikke av flere rapporter etterpå."* The only letter that uses a fact about Avinor and then converts it — *"43 lufthavner og flysikringstjenesten"* into *"kontroller er det som gjør endring mulig, ikke det som utsetter den."* The only close that escapes the banned closing pattern by doing something else rather than rewording it: it asks the employer how the unit intends to measure value. One page, 428 words. Its lack of a stated concession is a deliberate and correct channel choice — five bounded limits sit in the CV and eight more in `review.json`. |
| 2 | `3eeb10-stage1` | 86 | 88 | 86 | 86 | 76 | 92 | 88 | Contains the strongest single move in eighteen documents: *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn. Det er at dere driver noe som ikke kan settes på pause mens det forbedres."* It names the objection the reader was already forming, refuses to build a fake domain bridge, and converts the refusal into the argument — a concession that costs almost nothing and buys a great deal, which is exactly the asymmetry the other three concessions in the corpus get wrong. Backed by voluntary downscaling (*"i langt mindre skala"*) and an unusually plain register. Costs: a boilerplate opening followed immediately by two paragraphs of Excel. |
| 3 | `0fa53b` | 84 | 76 | 90 | 82 | 92 | 74 | 90 | The best opening in the corpus and the only true in-medias-res: *"Da gevinstene fra et sterilforsyningsprosjekt … fantes det ikke bruksdata som bar en direkte fordeling."* Deep judgement content, and its one ad phrase is used as a hook. Held to third by its calibration: *"Målt tidsbesparelse eller feilreduksjon har jeg ikke tall på"* answers the ad's first responsibility bullet with a negation, ordered negative-first, when nothing in the letter would have misled without it and the limit is already in `review.json`. The prior report calls this the corpus's best two sentences; I read it as its most expensive. |
| 4 | `0fa53b-opusx` | 81 | 72 | 94 | 88 | 62 | 84 | 84 | The deepest reasoning and the best architecture: a stated two-question thesis, both questions answered, then synthesised, with an integrity decision rather than a technical one at its centre. Its concession is the best-executed of the four — negation immediately recovered by *"Det modellen gjør, er å vise hva anslagene hviler på."* It **renders to two pages** at 551 words, against a one-page instrument, and spends its most valuable sentence restating a job title already printed twice above it. Architecture cannot outrun instrument fit. |
| 5 | `3eeb10` | 79 | 55 | 94 | 76 | 84 | 82 | 94 | The best prose in the corpus. *"Jeg tok den rammen og kjøpte forsvarligheten med kontroll i stedet for med omfang"* is the best sentence in eighteen documents, and *"Der gevinsten ikke lar seg måle direkte, gjør jeg heller forutsetningen synlig enn å lage presisjon som ikke finnes"* the clearest principle. It ranks fifth because the **body never writes the word Avinor** — the only occurrence is the template address block — and contains no fact about the employer, aviation, infrastructure or the samfunnsoppdrag. Swap in Statnett, Bane NOR or Helse Sør-Øst and nothing needs changing: a flat failure of the framework's own `Arbeidsgiverbyttetesten`. The prior report scored its vacancy engagement 88; that is not supportable. |

Ranked 6–9: `6d65bd` 77, `0fa53b-solxh` 76, `93c621` 75, `0fa53b-solmed` 74. `6d65bd` has the best
gevinst substance at grain level — *"Jeg skilte mellom driftsmessige og økonomiske virkninger,
unngåtte kostnader og belastning som flyttes mellom enheter"* — delivered as a list behind a flat
opening, with four consecutive sentences beginning *"Jeg"*. `93c621` opens on the pattern
`FORFATTERSTEMME.md:139-141` bans by name. `solmed` is last: the thinnest letter carrying the
costliest self-negation.

---

### 4.4 Package top 5

| # | Package | Score | G .26 | R .22 | M .20 | X .16 | Z .16 | Reasoning |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | **`b5104f`** | **85** | 92 | 78 | 88 | 76 | 88 | The only substantial package that is mechanically clean end to end — CV two pages, letter one, 1 124 words combined — attached to the broadest requirement coverage in the corpus and the only set that ever tells the reader why Avinor. Division of labour is real: the CV records the option appraisal, the letter narrates the decision inside it and adds the thesis. Faults are genuine but second-order: one verbatim-shared sentence, the sterile-logistics episode at near-equal length in both, and a numeral seam (`2,5`/`50` in the CV against *"to og et halvt"*/*"femti"* in the letter). The report placed this seventh of eleven on a credibility penalty that does not survive checking against the frozen authority. |
| 2 | `3eeb10-stage1` | 84 | 90 | 88 | 56 | 94 | 92 | The best-functioning pair in the corpus on everything except the artefact. Flawless consistency, the highest combined evidence reach, and the only set where the letter does something the CV structurally cannot — it concedes, and converts the concession into the argument. What holds it off first place is that its CV renders to three pages and both documents open on a legacy Excel workbook, so the recruiter's first thirty seconds in each go to the least role-relevant asset. |
| 3 | `3eeb10` | 82 | 76 | 72 | 92 | 92 | 84 | Mechanically the cleanest set here after `b5104f` — 1 032 words, perfect numeral consistency, no factual drift — carrying the corpus's only competency mapping to `styringsgrupper` and `styringsmodeller` and its best single sentence. It loses coverage points at set level for the thing that is invisible inside either document alone: **across both documents the set never says anything about Avinor.** Both also lead with the tool, and both carry the same allocation-model hedge in near-identical form. |
| 4 | `0fa53b-opusx` | 81 | 82 | 86 | 62 | 92 | 86 | The best-framed pair: both documents lead with gevinstmetodikk, and the letter's two-question thesis is a direct expansion of the CV's profile sentence. Genuine complementarity — the letter supplies the rejected option, the mandate constraint and the deliberate design choice, none of which the CV carries. The cost is bulk: 1 265 words, the heaviest set in the corpus, with the letter running onto a second page, and a verbatim-shared sentence. |
| 5 | `6d65bd` | 80 | 78 | 68 | 88 | 88 | 80 | Fifth by mechanical soundness and requirement reach rather than by flair, and it is the weakest entry in this table. It carries `PRJ-09` arbeidsinntak and the `PRJ-07` platform appraisal — both directly answering the ad's arbeidsformer and technology bullets, and both absent from four of the nine packages — and the letter has the finest-grained gevinst reasoning here. It is 907 words across two clean documents. Against it: the CV profile does the letter's job (*"For Avinors arbeid på tvers av digitale initiativer er bidraget å gjøre forventet verdi … tydelige"* — a pitch, agentless, inside a document that should outlive one application), the letter is a list behind a flat opening, and the same caveat is reworded in both documents rather than divided. It ranks fifth largely because the packages around it have harder failures. |

Ranked 6–9: `0fa53b` 79, `0fa53b-solmed` 78, `93c621` 77, `0fa53b-solxh` 75.

- **`0fa53b` 6th.** The corpus's best letter opening and 16 evidence refs, dragged down by a
  three-page CV whose AI material has no counterpart in the letter. Worth stating explicitly:
  **deleting two CV bullets would move this package into the top three.** The content is there.
- **`0fa53b-solmed` 7th.** The least redundant of the `0fa53b` family in content, and the costliest
  self-negation in the corpus.
- **`93c621` 8th.** Fast and consistent at 778 words, and the thinnest evidence base: the set omits
  the BI ownership, the forecasting work and the DRG work entirely.
- **`0fa53b-solxh` 9th.** The fastest set and the least additive — a letter that re-walks the CV's
  bullets in the CV's order at 0.98 sentence similarity — with the thinnest combined coverage of the
  nine.

---

### 4.5 What else the corpus gives up

**`used_evidence_refs` tracks package quality more closely than any prose judgement.** Refs by
package: `3eeb10-stage1` 23, `b5104f` 19, `0fa53b` 16, `3eeb10` 13, `opusx` 12, `6d65bd` 10,
`solmed` 9, `93c621` 7, `solxh` 7. My package top five is `b5104f`, `3eeb10-stage1`, `3eeb10`,
`opusx`, `6d65bd` — the top five by refs with `0fa53b` displaced by its page overrun. The count is a
free proxy for how much of the authority a package actually reached, and it is already in every
final package. Worth watching per run.

**Compression is a coverage decision that presents as an editing decision.** `solxh` and `93c621`
are the two best-edited CVs and the two thinnest sets. Both reviews record the deletions as
improvements — `solxh`: *"Strategiens bredere CV-rute er komprimert ved å utelate KI-arbeid og
tverrorganisatorisk Power BI-kompetanseoverføring"* — and both landed at 7 refs. The framework has a
compression order (`Erstatnings- og komprimeringsrekkefølge`) and no compression budget, so a writer
that decides to tighten has no signal telling it when tightening has become thinning. This is the
mirror image of W03: too long is measured too late, too thin is never measured at all.

**What the strongest packages do that the others do not.** Four transferable moves, each visible as
a spread in this corpus:

1. **Reason about requirement coverage explicitly, and record it.** `b5104f` alone pulled `PRJ-07`
   and `PRJ-09` into the CV *because* the ad's arbeidsformer and technology bullets would otherwise
   have rested on the work model alone, and said so in its review. It is the only package whose
   review contains that reasoning, and it has the broadest coverage. That is the whole of proposal
   P8 in the companion document, performed by hand, once.
2. **Use a fact about the employer, then convert it.** Naming *"43 lufthavner og
   flysikringstjenesten"* is worth little on its own; following it with *"kontroller er det som gjør
   endring mulig, ikke det som utsetter den"* is worth a great deal. Eight of nine letters do
   neither.
3. **Concede the free thing, not the expensive one.** `3eeb10-stage1` concedes a domain the
   recruiter can already see is missing and gets trust for it. `solmed` and `solxh` concede a
   requirement the ad marks as merely desirable and get nothing for it. Same rhetorical move,
   opposite sign.
4. **Put the decision in the verb.** *"Avviste direkte fordeling da bruksdata ikke ga et forsvarlig
   grunnlag"* does in one clause what *"Utformet en modell for gevinstfordeling"* needs three
   sentences to imply. Judgement verbs read senior; construction verbs read technical. This is the
   one move the prior report identified that I would adopt unchanged.

**What the prior report missed entirely.** Three things, all invisible from the extracted text
alone. The three rendered page failures, and that all three sit in its own top three. The verbatim
CV/letter sentence duplication in four of nine packages, against a named doctrine rule. And the
`3eeb10` competency line naming `styringsgrupper` — the one place in the whole corpus where a
package answers the requirement the report correctly identified as universally unanswered, and then
concluded could not be answered at all.
