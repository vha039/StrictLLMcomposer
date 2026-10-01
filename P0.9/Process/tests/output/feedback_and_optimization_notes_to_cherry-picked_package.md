# Feedback and optimization notes: the cherry-picked Avinor package

**To:** GPT-6 Astra, author of `CV_cherry-picked` and `Søknad_cherry-picked`
**From:** the reviewer who scored it against the nine generated packages
**Value function:** one thing only, the chance that Avinor invites Vegard to a first interview for *Seniorrådgiver Digital Transformasjon*
**Reviewed:** the two PDFs as rendered (CV 2 pages, letter 1 page)

---

## 0. Bottom line

You built the safest package in the corpus, and on this value function it is the second strongest.

| | Cherry-picked | Best package (`b5104f`) |
|---|---:|---:|
| Estimated chance of interview | **31.8%** | **39.8%** |
| Gate 1: CV skim | 85.6 | 89.0 |
| Gate 2: letter read | **78.0** | **90.5** |
| Gate 3: shortlist discussion (tone, coherence, credibility) | **82.5** | 79.3 |
| Knock-out triggers (page overrun, self-disqualification, employer-blind letter) | none | none |

Under 4 000 perturbed runs of the model (every sub-score ±3, weights and multipliers varied), the package ranked second in 100% of draws. That makes the gap real rather than noise, and it also says exactly where the gap is: **almost all of it is the letter read.** On tone and pair coherence you are already ahead of the winner.

The thesis of these notes is simple. **You maximised the floor. The next version should raise the ceiling without lowering the floor.** Every recommendation below is chosen to add reasons to invite without adding a single reason to reject. Modelled together, they move the package to roughly **39-40%**, level with the best package in the corpus, while keeping everything it currently does best.

---

## 1. How the package was scored, so the recommendations make sense

Hiring for this role is a sequence of readers, each of whom can stop reading. The model follows that sequence.

| Gate | What it represents | Built from |
|---|---|---|
| **G1 · CV skim (~45 s)** | Can the reader place him in the right category and find the ad's requirements? | 0.40 requirement coverage · 0.30 altitude (adviser vs specialist) · 0.20 mechanics (length, scannability) · 0.10 evidence density |
| **G2 · letter read** | Does the letter give a reason to invite *this* person to *this* employer? | 0.30 employer specificity · 0.25 judgement shown · 0.20 requirement conversion · 0.15 architecture, opening, close, fit · 0.10 prose |
| **G3 · shortlist** | Would the panel want this person in the room? | 0.35 tone (self-impressedness, Janteloven, Norwegian register) · 0.25 credibility posture · 0.20 CV/letter division of labour · 0.20 consistency |

Gates combine as a weighted geometric mean, so a weak gate cannot be averaged away. Then a small set of binary cues act as thresholds on the odds: CV over two pages (×0.70), letter over one page (×0.75), a self-disqualifying statement on an advertised requirement (×0.85), a letter that never engages the employer (×0.85).

The absolute percentages are anchored estimates. The relative ordering and the size of the gaps are the robust part.

**Your scores on the original document rubrics:**

| Document | Score | Rank in corpus | Sub-scores |
|---|---:|---|---|
| CV | 84 | 3rd of 10 | coverage 84 · evidence 76 · mechanics **93** · altitude 86 · calibration 84 · Norwegian 80 |
| Letter | 79 | tied 5th of 10 | employer specificity **70** · judgement 84 · requirement conversion 86 · architecture **72** · calibration 82 · prose 80 |
| Package | 86 | **1st** of 10 | coverage 84 · division of labour 82 · mechanics **94** · consistency 84 · credibility 86 |
| Tone (lower is better) | CV 15 · letter 23 · package 21 | CV **1st**, letter 3rd | |

The package rubric ranks you first because it measures pair-level properties (fit, duplication, consistency, mechanics) and does not see how persuasive the letter is. The interview model does see that, which is why you land second there.

---

## 2. What to keep: the floor you built

These are the things the package does better than every other package. Do not trade any of them away while optimising.

1. **Zero triggers.** Of the nine generated packages only `b5104f` and `6d65bd` get through with none. Three of the strongest rivals on content (`3eeb10-stage1`, `0fa53b`, `0fa53b-opusx`) each lose roughly a quarter of their odds to a three-page CV or a two-page letter. Your CV is exactly two pages with everything that matters on page 1, and your letter fits on one.
2. **The template defects are gone.** In all nine generated CVs the entire competency block renders as one bold run of up to 81 words. Yours has a bold label and regular content. The generated letters print the job title twice before the first sentence; yours prints it once and uses the second line for `Referanse: 474473271`. That is correct and it is visible to the reader in the first two seconds.
3. **The only evidenced communication paragraph in the corpus.** The ad asks for *"Sterke kommunikasjons- og fasiliteringsferdigheter"* and *"analyser, beslutningsgrunnlag og presentasjoner for ledelse"*. Across eighteen generated documents the word *kommunikasjon* appears zero times. You wrote *"I beslutningsnotater og presentasjoner tilpasser jeg detaljnivået til mottakeren"* and backed it with the health-economist workshop and the cross-organisation teaching. In the CV you added *"Utarbeider beslutningsnotater, presentasjoner og dokumentasjon tilpasset ledere, controllere og fagmiljøer"* and *"lederkommunikasjon"*. This is your single most original contribution. Keep it.
4. **No self-negation anywhere.** Four of the nine generated letters volunteer a disqualifier (*"ikke et formelt konsernmandat for portefølje- eller programledelse"*, *"har jeg ikke tall på"*). You cut every one. Correct.
5. **Lowest CV/letter duplication in the corpus.** One sentence pair at 0.87 similarity (the model handover). Four of the nine generated packages repeat a sentence character for character across the two documents.
6. **Calm, native register.** Best CV tone in the corpus. No announced abstraction, no *"det viktigste beviset mitt"*, no lecturing Avinor about Avinor, no essay-length letter.
7. **Every specific checks out.** Health-economist workshop covering process mapping, avoided cost versus transferred burden, leadership-requested methodology, coding agents in the forecasting work: all present in the source material.

---

## 3. Diagnosis: why the curated package lands second

### 3.1 Curation optimises for the absence of flaws; screeners shortlist on the presence of reasons

Picking the best fragment from each package is a flaw-minimising procedure. Each candidate sentence is judged locally, and the sentence least likely to be wrong wins. That procedure reliably removes defects, and it reliably removes the high-variance moves that make the strongest letters win, because those moves are exactly the ones that *could* have been wrong.

Three moves separate `b5104f`'s letter (90) from yours (79), and all three are high-variance:

| Move in `b5104f` | Why it is risky in isolation | What it buys |
|---|---|---|
| A thesis in the first paragraph: *"Den avstanden lukkes av at gevinstlogikken er avklart før pengene brukes, ikke av flere rapporter etterpå."* | A confident professional position before any evidence | The reader knows in ten seconds what this candidate thinks and why it matters to the unit |
| An Avinor fact turned into an argument: *"Avinor driver 43 lufthavner og flysikringstjenesten … Den rammen kjenner jeg igjen."* | Could read as flattery or as lecturing the employer | The only letter that passes the employer-swap test with a fact rather than a phrase |
| A question as the close: *"…hvordan enheten tenker å måle verdien av initiativene den skal prioritere mellom."* | Unconventional; a formula close is safer | The only close in the corpus that invites a reply |

Your letter has none of the three. It opens *"Jeg søker stillingen som seniorrådgiver i Digital Transformasjon fordi…"* directly under a title line that says the same thing, and closes *"Jeg tar gjerne en samtale om hvordan jeg kan bidra i enheten."*

### 3.2 The letter has no spine

Read in sequence, the letter is five sound paragraphs that do not argue with each other: motivation, budget tool, allocation model, communication, contribution. Each is well-made. None is connected to the others by an idea. The generated letters that score highest on architecture have one spine that every paragraph serves (`opusx`: two questions; `b5104f`: the gap between what an investment was justified by and what can later be shown). Without a spine, a reader remembers episodes, not a candidate.

### 3.3 Merging drifts toward the weakest shared claim

When fragments from several packages describe the same fact, the version most compatible with all of them tends to survive, and that is usually the weakest. Three instances:

- **Sole coder became co-responsible.** CV and letter both say *"hadde hovedansvaret for kodeendringene"*. The source material confirms the stronger statement: *i praksis eneste kodende utvikler for kodeendringene* (confirmed 2026-09-06).
- **Two budget years became one.** The letter says *"Den moderniserte versjonen ble brukt i sykehusets budsjettprosess for 2026."* Your own CV says it is in use for 2026 and 2027, and so does the source.
- **The strongest adoption proof left the letter.** The hospital-wide gevinst methodology, adopted as the standard and still in use about 2.5 years later, is the candidate's best evidence for *"målbar verdi og gevinst"*. It is only in the CV.

Each is individually defensible. Together they make the letter weaker than the facts allow.

### 3.4 The employer is present by name, not by substance

*"Avinors nye transformasjonsmiljø"*, *"hos dere"*, *"i enheten"*, *"i en virksomhet der digitale endringer må fungere med hensyn til både drift og sikkerhet"*. Replace *Avinor* with *Statnett* and change one word, and the letter still works. That is the single largest scored gap (employer specificity 70 versus 92) and the cheapest to close, because the vacancy text gives you the facts.

### 3.5 Summary

Highest floor in the corpus, lower ceiling than the winner. The fix is not a rebuild. It is three letter moves, three restored facts, and four CV bullet upgrades, with the floor held constant.

---

## 4. The letter, paragraph by paragraph

### Header

`Avinor AS / Digital Transformasjon / Oslo, 13. september 2026 / Referanse: 474473271` then `Søknad: Seniorrådgiver Digital Transformasjon`.

**Keep as is.** Correct, uncluttered, and the FINN reference is a small professional touch the generated letters lack.

### Paragraph 1: opening

> Jeg søker stillingen som seniorrådgiver i Digital Transformasjon fordi jeg vil arbeide tettere med hvordan digitale investeringer prioriteres og blir til endringer i driften. Ved Oslo universitetssykehus arbeider jeg med både gevinstvurderinger og praktisk digitalisering. Muligheten til å bruke denne kombinasjonen i Avinors nye transformasjonsmiljø er særlig interessant for meg.

**What works.** The *fordi* clause gives a real reason, and it maps to the unit's mandate (prioritising digital investments, turning them into operational change).

**What costs.**
- The first eight words repeat the title printed immediately above. The most valuable sentence in the letter carries no new information.
- *"denne kombinasjonen"* labels the candidate's own profile as notable, a mild self-impressed marker.
- *"er særlig interessant for meg"* is generic motivation and centres the candidate rather than the work.
- No evidence and no employer fact.

**Recommendation.** Replace the paragraph with one of two openings. Both put evidence or a position in the first sentence.

*Option A, in medias res (recommended).* The strongest opening in the corpus (`0fa53b`, scored 92 on architecture) starts inside the allocation problem. It shows judgement in the first line and it is the candidate's own decision, not a team result.

> Da gevinstene fra en investering i steril logistikk skulle fordeles mellom klinikkene ved Oslo universitetssykehus, fantes det ingen bruksdata som kunne bære en direkte fordeling. Jeg avviste den direkte modellen og bygde i stedet en fordeling på vektede, indirekte indikatorer, der unngåtte kostnader holdes adskilt fra belastning som bare flyttes mellom enheter. Forutsetningene står synlig i modellen, og makrokoden holdt jeg utenfor kjernen, slik at controllerne kan undersøke og justere grunnlaget uten å gå veien om en utvikler. Det er den typen vurdering Digital Transformasjon skal gjøre for Avinor: hva en forventet gevinst faktisk hviler på, før den brukes til å prioritere.

This merges your current paragraph 3 into the opening, so nothing is lost.

*Option B, thesis.* If you judge that a Norwegian public-sector reader prefers to meet the candidate before the case:

> Jeg søker fordi Digital Transformasjon skal gjøre det jeg har arbeidet mest med ved Oslo universitetssykehus: vurdere hva en forventet gevinst faktisk kan bygge på, og få digitale endringer helt fram til bruk.

Option B keeps *"Jeg søker"* but does not restate the title, and it announces the spine that the rest of the letter delivers.

**Expected effect.** Architecture 72 → ~86. Modelled: +1.2 percentage points on its own (more when combined with the close).

### Paragraph 2: budget tool

> I moderniseringen av sykehusets budsjetteringsverktøy hadde jeg hovedansvaret for kodeendringene i 2025. Bemanningsdata måtte tidligere kopieres fra en annen arbeidsbok; jeg integrerte dem i verktøyet. Rammen var å bevare eksisterende funksjon mens løsningen ble forbedret. Jeg gjennomførte derfor endringene funksjon for funksjon, sammenlignet gammel og ny beregning og brukte akseptansekriterier og risikoregister. Arbeidet inngikk i en bred prosess med arbeidsgrupper og kravavklaringer, og jeg laget opplæringsmateriell for controllerne. Den moderniserte versjonen ble brukt i sykehusets budsjettprosess for 2026.

**What works.** Concrete mechanism, calm register, and the constraint is framed without grievance (*"Rammen var å bevare eksisterende funksjon"*), which is socially better than naming the implementation lead.

**What costs.**
- *"hadde jeg hovedansvaret"* understates the confirmed *i praksis eneste kodende utvikler*.
- *"for 2026"* understates 2026 and 2027, and contradicts your own CV by omission.
- The judgement in this episode is missing. The source records two decisions: he evaluated VBA, Office Scripts, Python and AI-assisted alternatives against compatibility, operational risk and maintainability, and he recommended a broader restructuring before executing the narrower scope he was given. The first is the corpus's best evidence for the ad's *"God forståelse for hvordan teknologi kan skape forretningsverdi"*. The second shows that he can hold a view and still deliver inside someone else's frame, which is what a new central unit without line authority needs.
- As the second paragraph, it places a legacy Excel workbook in the reader's first 20 seconds. With Option A opening, it moves to third and that cost disappears.

**Recommendation.**

> Den andre siden av oppgaven er å få en endring gjennomført i et system som ikke kan stoppe. Sykehusets budsjetteringsverktøy er et arvet Excel/VBA-verktøy på om lag 20 år, og i 2025-moderniseringen var jeg i praksis eneste kodende utvikler, i en prosess der om lag 50 personer deltok. Jeg vurderte VBA, Office Scripts, Python og KI-støttede alternativer mot driftsrisiko og vedlikeholdbarhet, og anbefalte en bredere omstrukturering. Rammen ble en smalere endring funksjon for funksjon, og den gjennomførte jeg med kontroll av gammel mot ny beregning, akseptansekriterier og risikoregister. Hele sykehuset brukte verktøyet i budsjettprosessen for 2026, og det brukes i prosessen for 2027.

The *anbefalte / Rammen ble* pair states the disagreement as a fact and moves on. No person is named, and nothing reads as complaint.

**Expected effect.** Judgement 84 → 88, calibration 82 → 86, and it removes the CV/letter year mismatch.

### Paragraph 3: allocation model

Moved into the opening under Option A. If you choose Option B, keep this paragraph in position 2 and add the judgement verb: *"Jeg avviste den direkte modellen…"* instead of *"Jeg valgte…"*. The source literally records that he *rejected false precision*. A rejected option reads senior; a chosen method reads technical.

Also break the chain *"Jeg valgte… Jeg skilte… Jeg holdt…"*. Three consecutive sentences starting with *Jeg* is the most visible prose tic in the letter, and the letter's overall *jeg* density (16 in 334 words, 4.8%) is the highest in the corpus. The reference draft brings it to 12 in 400 words (3.0%), which is the corpus norm.

### New paragraph: the methodology, restored to the letter

The hospital-wide standard is the candidate's strongest answer to *"Erfaring med … gevinstrealisering"* and to *"Sikre at digitale initiativer gir målbar verdi"*. It is also a team result, which gives the letter a natural place for a clean *vi / mitt bidrag* attribution, a construction Norwegian readers reward.

> Metodedelen har jeg arbeidet med sammen med andre. Analyseavdelingens første store oppdrag, bestilt av ledelsen, var å forbedre sykehusets metodikk for gevinstrealisering og estimering. Vi var fire som utviklet den reviderte metodikken, og mitt bidrag lå i forskningssyntesen, metodeforbedringen og de økonomiske vurderingene. Den ble felles standard for hele sykehuset, og om lag 2,5 år senere var den fortsatt i bruk.

Word this differently from the CV bullet. Eight of nine generated packages ship *"ble innført som sykehusdekkende standard og var fortsatt i bruk om lag … år senere"* in **both** documents; the reference wording avoids that.

**Expected effect.** Requirement conversion 86 → 88; adds the letter's only explicit team attribution.

### Paragraph 4: communication

> I beslutningsnotater og presentasjoner tilpasser jeg detaljnivået til mottakeren. Jeg har ledet en intern BI-workshop for økonomer og helseøkonomer om blant annet prosesskartlegging, datamodellering og datakvalitet. Gjennom arbeidsmøter har jeg også lært opp teknisk personell i et annet rapporteringsmiljø. Erfaringen med å forklare faglige valg for ulike mottakere vil jeg ta med inn i samarbeidet hos dere.

**Keep the substance.** It is unique in the corpus (section 2, item 3).

**Tighten.**
- The first sentence is a skill self-description. Lead with who the documents are for (*ledere, controllere og fagmiljøer*), which is evidence of audience rather than a claim of ability, and names the leadership audience the ad asks about.
- The last sentence is a closing moral that tells the reader what to conclude. Cut it; the evidence already says it.

> Mye av arbeidet er å forklare valgene for dem som skal bruke dem. Til ledere, controllere og fagmiljøer skriver jeg beslutningsnotater og presentasjoner med detaljnivå etter mottaker. Jeg har ledet en intern BI-workshop for økonomer og helseøkonomer, og gjennom flere arbeidsmøter har jeg lært opp teknisk personell i et annet rapporteringsmiljø.

### Paragraph 5: contribution

> Hos Avinor vil jeg bruke denne erfaringen til å avklare hva et initiativ skal endre, hvem som berøres og hvordan forventet verdi kan etterprøves. Det gir et konkret utgangspunkt for å støtte prioritering og gjennomføring sammen med fagmiljøene, i en virksomhet der digitale endringer må fungere med hensyn til både drift og sikkerhet.

**What works.** A controlled, specific future contribution that matches the unit's mandate.

**What costs.**
- *"Det gir et konkret utgangspunkt"* grades the candidate's own contribution.
- *"drift og sikkerhet"* is the only employer substance in the whole letter, and it is generic.

**Recommendation.** Put the Avinor fact here, turned into the candidate's own working condition, then the contribution.

> Avinor holder 43 flyplasser og flysikringstjenesten i drift hver dag mens tjenestene utvikles. Den betingelsen har jeg arbeidet under siden 2023: en forbedring må kunne innføres uten at driften stopper. Hos dere vil jeg bidra til at verdiantakelsene bak et initiativ er etterprøvbare før det prioriteres, og til at endringen er tenkt helt fram til fagmiljøene som skal bruke den.

Why the fact goes here and not in the opening: an opening that recites the employer's own situation back to them spends the first sentence on something the reader knows (this pattern is explicitly flagged in the framework's voice policy, and `93c621`, which opens that way, has the worst tone score in the corpus). Placed late and immediately converted into *"Den betingelsen har jeg arbeidet under"*, the same fact becomes recognition, not flattery.

**Considered and not recommended: the Avinormodellen analogy.** The vacancy describes the model where the large airports finance the small ones. Structurally it is the same problem as the sterile-logistics allocation: who carries the cost, who receives the benefit, and how to distribute across units when direct measurement does not exist. It is the most intelligent connection available in the material. It is also high variance: in writing, a candidate explaining the employer's own funding model to them can read as presumptuous, and one of the generated runs considered it and rejected it for that reason. Keep it for the interview, where it lands as insight rather than instruction.

**Expected effect.** Employer specificity 70 → ~88. Modelled: **+3.1 percentage points**, the largest single gain available.

### Close

> Jeg tar gjerne en samtale om hvordan jeg kan bidra i enheten.

This is the most common closing in the corpus, and a known generic pattern. It asks for nothing and offers nothing specific.

> Jeg forteller gjerne mer om fordelingsmodellen og budsjettarbeidet i en samtale, og er nysgjerrig på hvordan enheten vil følge opp verdien av initiativene den prioriterer.

It offers specific material and asks the unit a question that shows he has thought about their problem. *nysgjerrig* also appears in the ad; used here as a verb of genuine interest rather than a claimed trait, it reads naturally, but it is a judgement call (section 10).

---

## 5. The CV, section by section

### Headline

`SAMFUNNSØKONOM | GEVINSTREALISERING OG DIGITALISERING` (53 characters, one line)

Right category, correct length, and the short line is a real mechanical advantage (the generated headlines run to 96 characters in forced caps). The weakness is that *digitalisering* is generic and the ad's key noun is *gjennomføring* (*gjennomføringskraft*, *høy gjennomføringsevne*).

**Recommendation:** `SAMFUNNSØKONOM | GEVINSTREALISERING OG DIGITAL GJENNOMFØRING` (59 characters, still one line at the current size).

### Profile

> Samfunnsøkonom med master fra NTNU og rådgiver økonomi og IKT ved Oslo universitetssykehus. Har medutviklet sykehusets felles gevinstmetodikk og hatt hovedansvaret for kodeendringene i et budsjetteringsverktøy i sykehusdekkende bruk. Kombinerer økonomisk vurdering med praktisk digitalisering, behovsavklaring og samarbeid mellom økonomi-, fag- og teknologimiljøer.

Clean and correctly anchored. Three adjustments: restore the confirmed sole-coder statement, add the allocation model (currently absent from the top zone, and it is his most individually attributable judgement), and replace *"Kombinerer…"* (a trait) with the working space that matches the ad.

> Samfunnsøkonom med master fra NTNU og rådgiver økonomi og IKT i Analyseavdelingen ved Oslo universitetssykehus. Har vært med på å utvikle sykehusets felles metodikk for gevinstrealisering, utformet en etterprøvbar modell for gevinstfordeling der direkte data manglet, og vært i praksis eneste kodende utvikler i moderniseringen av et budsjetteringsverktøy i sykehusdekkende bruk. Arbeider mellom økonomisk vurdering, beslutningsgrunnlag for ledere og praktisk digital gjennomføring.

### Kjerneområder

> Gevinstrealisering og investeringsvurdering · Beslutningsgrunnlag og lederkommunikasjon · Digitalisering av økonomi- og arbeidsprosesser · Prioritering og arbeidsformer · Workshopfasilitering og kompetanseoverføring · Power BI, Power Query, Excel/VBA og SQL

Six items, regular weight, tools last. Keep the format. Two content gaps: nothing touches the ad's *styringsmodeller / beslutningsprosesser* (listed as an advantage), and *"Digitalisering av økonomi- og arbeidsprosesser"* is the least specific item.

> Gevinstrealisering og investeringsvurdering · Beslutningsgrunnlag og presentasjoner for ledere · Arbeidsformer, arbeidsinntak og styringsstruktur · Kontrollert endring av virksomhetskritiske løsninger · Workshopfasilitering og kompetanseoverføring · Power BI, Power Query, Excel/VBA, SQL, R og Python

*Styringsstruktur* rather than *styringsmodeller* is deliberate: the evidence (governance contribution to the methodology, the department's work model, the intake design) supports the structure of how work is governed at project and department level, not ownership of an enterprise governance model.

### Yrkeserfaring: Analyseavdelingen

Seven bullets today. Order, altitude and the first bullet are right. The gaps are evidence depth and one missing requirement area.

| # | Current | Assessment | Recommendation |
|---|---|---|---|
| 1 | Gevinst framework, team of four, leadership request, hospital-wide standard, ~2.5 years | Correct first bullet. Uses the stock construction that also appears in the letter in most packages. | Keep; compress the ending so the CV and letter wordings differ (reference below). |
| 2 | Budget tool, *"Hadde hovedansvaret"*, 50 involved, 2026 and 2027 | Longest bullet (5 lines); understates the sole-coder fact; the last two sentences spend a line on budget years. | Restore *i praksis eneste kodende utvikler*; compress the years into one clause. Leave the option appraisal to the letter. |
| 3 | Allocation model | No judgement verb; the architecture that shows scale is missing. | Lead with the rejected option; add the branch structure. |
| 4 | Establishment group; *"Arbeidet omfattet både innførte arbeidsformer og forslag"* | Ends on a hedge; the intake design, the most direct evidence for *arbeidsformer og styringsmodeller*, is absent. | Merge in the intake design; remove the terminal hedge (describe what he designed, which needs no implemented/proposed caveat). |
| 5 | Power BI teaching; *"Bidro vesentlig til en første komponent i en driftsrapport"* | The second sentence is opaque to an outside reader. The BI build itself, where he wrote nearly the whole semantic model and 80-90 percent of the DAX, is absent. | Replace with the backend build plus the teaching, in past tense, without ending on the decommissioning. |
| 6 | Decision support, notes, presentations for leaders | Unique and valuable. | Keep; tighten. |
| 7 | Forecasting architecture; *"fordelt mellom meg, en kollega og kodeagenter"* | *meg* inside a subjectless CV bullet is a register slip. | Rephrase without the pronoun. |

Reference bullets, in recommended order:

1. Utviklet sammen med tre kolleger sykehusets reviderte metodikk for gevinstrealisering og estimering, på oppdrag fra ledelsen, med bidrag til forskningssyntese, metodeforbedring og økonomiske vurderinger. Innført som sykehusdekkende standard, fortsatt i bruk om lag 2,5 år senere.
2. Avviste direkte gevinstfordeling mellom klinikker i steril logistikk da bruksdataene ikke bar den, og utformet i stedet en vektet proxymodell med fire grenmodeller, en konsolideringsmodell og synlige, justerbare forutsetninger. Ferdigstilt og overlevert til controllere tidlig i 2026.
3. I praksis eneste kodende utvikler i 2025-moderniseringen av sykehusets arvede Excel/VBA-budsjetteringsverktøy, innenfor en interessentprosess med om lag 50 deltakere. Integrerte bemanningsdata og sikret endringene med differansekontroll, akseptansekriterier og risikoregister. I sykehusdekkende bruk i budsjettprosessene for 2026 og 2027.
4. Utarbeider analyser, beslutningsnotater og presentasjoner for ledere, controllere og fagmiljøer innen økonomi, bemanning, aktivitet og pasientflyt.
5. Deltok i firepersonersgruppen som etablerte Analyseavdelingen: utformet arbeidsinntak med formål, avhengigheter og akseptansekriterier, oppgavestruktur og prioritering, og planla og fasiliterte workshops. Vurderte Forms, Loop, Power BI og lavkodealternativer for inntak og krav.
6. Var hovedutvikler på backend i en styringsløsning i Power BI: nesten hele den semantiske modellen, det meste av ETL og om lag 80-90 prosent av DAX, med brukertester og en intern workshop for økonomer og helseøkonomer. Lærte også opp teknisk personell i en annen rapporteringsorganisasjon i semantisk modellering.
7. Har ansvar for arkitektur, orkestrering og integrasjon i et pågående prognoseprosjekt for pasientvolum og kapasitet; implementeringen deles med en kollega og kodeagenter, med menneskelig gjennomgang og tidsbasert validering.

Why the allocation model moves to bullet 2, above the budget tool: it is the candidate's own decision under uncertainty and the closest single match to the unit's purpose (*sikre at investeringer i teknologi gir faktisk verdi*). The budget tool is execution evidence; it belongs third.

### Yrkeserfaring: Barne- og ungdomsklinikken

Good as is. One precision gain: *"seksjonsvise aktivitetsestimater"* → *"seksjonsvise DRG-prognoser"*, which is the actual artefact and reads as forecasting competence rather than a generic estimate.

### Page 2: education and supporting sections

Page 2 is about 35% empty. That is room, not waste, and the additions above will use some of it. Two small gains:

- **Language line.** The ad asks for *"Meget gode … kommunikasjonsevner på norsk og engelsk"*. *"Engelsk: Flytende skriftlig og muntlig"* is a bare assertion. The candidate went to upper secondary school in Calgary, Canada (2011-2013). *"Engelsk: Flytende skriftlig og muntlig (videregående skole i Calgary, Canada)"* turns the assertion into a fact at the cost of five words.
- **Tidligere erfaring.** Four entries of two lines each for 2013-2021 roles. One line each (employer, role, period) recovers space for the new evidence on page 1 flowing over, if needed. Keep the Luftforsvaret line as a neutral fact; do not use it as aviation proximity.

---

## 6. The package as a pair

- **Division of labour.** With the recommendations, the CV carries the record (framework, model architecture, sole coder, BI build, intake design, forecasting), and the letter carries the reasoning (rejected options, the disagreement and the execution inside the narrower scope, choosing what goes to controllers and why, the communication practice, the Avinor recognition). That is the split that scores highest.
- **Consistency.** Use one numeral convention across both documents: numerals for measured quantities (*om lag 50*, *2,5 år*, *20 år*, *43*). The strongest generated package lost points for a visible seam between *2,5* in the CV and *to og et halvt* in the letter.
- **No sentence in both.** After the edits, check that no sentence appears in near-identical form in both documents. The two highest-risk sentences are the methodology adoption statement and the model handover.
- **Spine.** The pair should say one thing: *he works on both halves of the unit's problem, deciding what a benefit can rest on and getting change into use without stopping operations, and he explains both to the people who decide.* Every paragraph and every top-zone bullet should serve that sentence.

---

## 7. Fact bank

Everything below is supported by the candidate's source material. The middle column is the strongest phrasing the source supports; the right column is where the statement stops.

| Fact | Strongest supported phrasing | Stops at |
|---|---|---|
| Allocation model, steril logistikk | Direct allocation unsupported by usage data; he *rejected false precision* and designed a weighted proxy model: five workbooks, four branch models and one consolidation model; visible, configurable weights and assumptions; schema-controlled Power Query transfer; audits for unmapped rows; operational, financial, quality, **avoided-cost** and **transferred-burden** mechanisms kept separate; completed and handed over to controllers early 2026 | Not "in use", not realised benefits, not ownership of clinic estimates |
| Gevinst methodology | Analyseavdelingen's first major project, **requested by leadership**; four-person team; his contribution: research synthesis, methodological, economic/strategic and governance input; adopted as the hospital-wide standard; in use about 2.5 years later | Not sole author or method lead; "about 2.5 years later", not "still today" |
| Budget tool | ~20-year-old Excel/VBA tool (~15 sheets, 78 global names); 2025 modernisation integrated employee, employment and staffing data; **i praksis eneste kodende utvikler** (confirmed 2026-09-06); ~50-person stakeholder process; **recommended a broader restructuring**, a narrow function-by-function refactor was required; ~80% behaviour-preserving; differential control, acceptance criteria, risk register; controller onboarding; **evaluated VBA, Office Scripts, Python and AI-assisted approaches** against compatibility, operational risk and maintainability; hospital-wide use in the **2026 and 2027** budget processes; 2027 modernisation completed | Not original creator or budget owner; no quantified time or error savings |
| Communication | Decision notes, executive summaries, presentations, documentation and onboarding adapted to managers, controllers, specialists and technical staff; **led an internal BI workshop for economist and health-economist colleagues** covering process mapping, ETL, star schemas, semantic models, data quality and performance; cross-organisation Power BI teaching over several working sessions | No claimed decisions caused or measured training impact |
| Work model and intake | Four-person group that established Analyseavdelingen; team structure alternatives, responsibilities and dependencies, Scrum/Kanban, task hierarchy, WIP design, Loop workspaces; intake design with purpose, users, decision needs, dependencies and acceptance criteria; evaluated Forms, Loop, Power BI, Pega and low-code alternatives, used at project level | Mix of implemented and proposed; no formal organisation-design mandate |
| BI build | Greenfield management BI; almost the entire semantic model, most of the ETL in Power Query M, ~80-90% of the DAX; user tests and improvement rounds; owned roughly August 2025 to February 2026, then decommissioned | Colleagues led content and visuals |
| Forecasting | Active 14-, 90- and 365-day forecasts of patient volume, beds and capacity; he owns architecture, orchestrator, automation and integration; added GAM, evaluated SARIMAX; implementation shared with a colleague and coding agents | No production deployment, no verified model performance |
| Platforms | Early access and pilots around Microsoft Fabric, Power Platform, dbt, Pega and Python, assessed against concrete hospital constraints | Pilot and exploratory only |
| AI superuser | Registered *SuperBruker, Kunstig intelligens* at OUS for about three years; answers technical questions in a Teams channel | No user counts or governance mandate |
| Month-end close, clinic | Took over the full assigned flow within about three months; independent reconciliation, control, result explanation and reporting to clinic management | Assigned clinic flow only |
| English | Upper secondary school in Calgary, Canada, 2011-2013 (English 30-1) | No CEFR level or test score |
| **Avinor (from the vacancy)** | ~3 000 employees; 43 airports and the air navigation service; nearly 600 000 departures and landings and 53 million passengers a year; the Avinormodellen cross-subsidy; the new unit's mandate: *styrke gjennomføringskraften i digitaliseringsarbeidet i konsernet og sikre at investeringer i teknologi gir faktisk verdi for virksomheten*; hiring several *seniorrådgivere* | Facts about Avinor only; no claims about Avinor's internal state |

---

## 8. Reference implementation: the full letter

A complete draft assembling the paragraph recommendations in section 4. It is 400 words, one page at the current typography, 12 uses of *jeg* in 400 words, no dashes. It is a reference, not a mandate: you own the final wording.

> Da gevinstene fra en investering i steril logistikk skulle fordeles mellom klinikkene ved Oslo universitetssykehus, fantes det ingen bruksdata som kunne bære en direkte fordeling. Jeg avviste den direkte modellen og bygde i stedet en fordeling på vektede, indirekte indikatorer, der unngåtte kostnader holdes adskilt fra belastning som bare flyttes mellom enheter. Forutsetningene står synlig i modellen, og makrokoden holdt jeg utenfor kjernen, slik at controllerne kan undersøke og justere grunnlaget uten å gå veien om en utvikler. Det er den typen vurdering Digital Transformasjon skal gjøre for Avinor: hva en forventet gevinst faktisk hviler på, før den brukes til å prioritere.
>
> Metodedelen har jeg arbeidet med sammen med andre. Analyseavdelingens første store oppdrag, bestilt av ledelsen, var å forbedre sykehusets metodikk for gevinstrealisering og estimering. Vi var fire som utviklet den reviderte metodikken, og mitt bidrag lå i forskningssyntesen, metodeforbedringen og de økonomiske vurderingene. Den ble felles standard for hele sykehuset, og om lag 2,5 år senere var den fortsatt i bruk.
>
> Den andre siden av oppgaven er å få en endring gjennomført i et system som ikke kan stoppe. Sykehusets budsjetteringsverktøy er et arvet Excel/VBA-verktøy på om lag 20 år, og i 2025-moderniseringen var jeg i praksis eneste kodende utvikler, i en prosess der om lag 50 personer deltok. Jeg vurderte VBA, Office Scripts, Python og KI-støttede alternativer mot driftsrisiko og vedlikeholdbarhet, og anbefalte en bredere omstrukturering. Rammen ble en smalere endring funksjon for funksjon, og den gjennomførte jeg med kontroll av gammel mot ny beregning, akseptansekriterier og risikoregister. Hele sykehuset brukte verktøyet i budsjettprosessen for 2026, og det brukes i prosessen for 2027.
>
> Mye av arbeidet er å forklare valgene for dem som skal bruke dem. Til ledere, controllere og fagmiljøer skriver jeg beslutningsnotater og presentasjoner med detaljnivå etter mottaker. Jeg har ledet en intern BI-workshop for økonomer og helseøkonomer, og gjennom flere arbeidsmøter har jeg lært opp teknisk personell i et annet rapporteringsmiljø.
>
> Avinor holder 43 flyplasser og flysikringstjenesten i drift hver dag mens tjenestene utvikles. Den betingelsen har jeg arbeidet under siden 2023: en forbedring må kunne innføres uten at driften stopper. Hos dere vil jeg bidra til at verdiantakelsene bak et initiativ er etterprøvbare før det prioriteres, og til at endringen er tenkt helt fram til fagmiljøene som skal bruke den.
>
> Jeg forteller gjerne mer om fordelingsmodellen og budsjettarbeidet i en samtale, og er nysgjerrig på hvordan enheten vil følge opp verdien av initiativene den prioriterer.

If it runs past one page, trim in this order: the option-appraisal clause in paragraph 3, then the final sentence of paragraph 1. Do not trim the Avinor paragraph or the close; they carry most of the modelled gain.

---

## 9. Priorities and expected effect

Modelled cumulatively on the interview model, starting from 31.8%.

| Order | Change | Gate | Cumulative chance of interview | Risk if done badly |
|---:|---|---|---:|---|
| 1 | Avinor fact turned into the candidate's working condition, placed late in the letter | G2 employer specificity 70 → 88 | **34.9%** | Reads as flattery if not converted in the next sentence |
| 2 | Replace formula opening (Option A or B) and formula close (question to the unit) | G2 architecture 72 → 86 | **36.1%** | Option A needs a clear bridge to the unit in its last sentence |
| 3 | Restore judgement and adoption in the letter: rejected direct model, option appraisal, broader restructuring recommended, methodology paragraph | G2 judgement 84 → 88, conversion 86 → 88 | **36.9%** | Length; watch the one-page limit |
| 4 | Break *jeg* chains; cut the closing moral in the communication paragraph | G2 prose 80 → 84 | **37.1%** | None |
| 5 | CV: headline *gjennomføring*; profile with the allocation model and sole coder; *styringsstruktur* competency; bullets 2, 3, 5, 6 upgraded | G1 coverage 84 → 88, altitude 86 → 90, evidence 76 → 80 | **39.2%** | Page 1 overflow; keep to two pages |
| 6 | One numeral convention; 2026 and 2027 in both documents; no sentence in both | G3 consistency and credibility | **39.9%** | None |
| 7 | English line with Calgary schooling; DRG-prognoser; compact earlier roles | G1 coverage, small | ~40% | None |

Items 1-3 are about two-thirds of the total and all sit in the letter.

---

## 10. Regressions to avoid

Each of these is observed in at least one generated package, and each would cost more than the corresponding gain above.

- **A defensive clause about what he lacks.** *"ikke et formelt konsernmandat"*, *"har jeg ikke tall på"*, *"der har jeg ingen bakgrunn"* as a disqualifier. Limits belong in your own notes, not in the text.
- **A CV over two pages or a letter over one.** The two most content-rich generated packages lost a quarter of their odds this way. Adding evidence is exactly how that happens.
- **A bold competency block, or a second job-title line in the letter header.** You fixed both; keep them fixed.
- **The same sentence in both documents,** especially the methodology adoption sentence.
- **An opening that defines Avinor's job for Avinor.** Worst tone score in the corpus.
- **A pitch to Avinor inside the CV profile.** The CV is the record; the pitch lives in the letter.
- **CV bullets that end on what did not happen** (*"…da den ble avviklet"*, *"…ikke innført"*).
- **Turning the communication paragraph into a trait claim** (*"gode kommunikasjonsevner"*). Its value is that it is evidence.
- **Claiming portfolio, programme or steering-group responsibility.** Not supported, and not needed: the ad lists portfolio management as an advantage.
- **Dashes** (– and —) in the Norwegian text.
- **Essay length.** The most elegant generated letter ran to 551 words and two pages, and scored worst on tone after the one that lectured the employer.

---

## 11. Reflection: where these notes may be wrong, and where your judgement should win

1. **The floor may be worth more than the model credits.** If Avinor's first screen is HR-led, high-volume and conservative, and letters are read only for CVs that survive, then G2 carries less weight than 0.35 and your package sits closer to the winner than eight points. That is the scenario where curation was the right strategy. The recommendations are designed to be safe under both scenarios: none of them adds a trigger.
2. **The Avinor-fact move rests on thin corpus evidence.** Exactly one generated letter does it, and that letter is the winner. I believe it is right because it is the direct remedy for the employer-swap test and because of how hiring managers read, not because the corpus proves it. If it reads to your Norwegian ear as flattery, keep the conversion sentence and choose a different fact from the vacancy (the unit's own mandate is the obvious alternative).
3. **In medias res is taste-sensitive.** Some Norwegian public-sector readers prefer meeting the candidate before the case. That is why Option B exists. A formula opening is not fatal; it is wasted space.
4. **More evidence is also the road to page three.** Both three-page CVs in the corpus came from the impulse behind item 5. The reference bullets are written to be close to line-neutral on page 1; the flow-over goes to page 2, which has room.
5. ***Styringsstruktur* versus *styringsmodeller*.** I chose the weaker word because the evidence is project- and department-level. If you read the material as supporting *styringsmodeller* at that level, it maps more directly to the ad's wording; I would still not put it in the headline.
6. ***nysgjerrig* in the close** echoes the ad's own word. I think it reads as genuine because it is attached to a concrete question. If it reads as an echo to you, *"og vil gjerne høre hvordan enheten…"* does the same job, at the cost of a second *gjerne*.
7. **Jeg density.** Norwegian letters legitimately use *jeg* often. The penalty in the model is small; the chain of three consecutive *Jeg*-sentences is the part worth fixing.
8. **The absolute numbers are anchored estimates.** "Average package ≈ 22%, excellent ≈ 45%" reflects assumptions about the applicant pool, the plural hiring and the candidate's partial fit (strong on gevinst and decision support; about 3.5 years of relevant experience; no aviation; no portfolio mandate). The +8 points is a relative estimate and is the number to trust.
9. **The DOCX files carry stale document properties.** The PDFs are clean (created 2026-09-13). The DOCX core properties say created 2013-12-23 and the application field says *Microsoft Macintosh Word*, inherited from the original template. If a DOCX is what gets uploaded, regenerate those properties.
10. **What I cannot judge as well as you can:** the fine Norwegian rhythm of the reference draft, and whether its first paragraph is one sentence too long for a first read. Treat the draft as a specification of *what* the letter should do, and write *how* it sounds.
