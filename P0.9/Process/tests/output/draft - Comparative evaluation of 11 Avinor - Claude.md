I'll start by taking inventory of the working directory.

22 files confirmed. Reading the vacancy first.

Vacancy read. Now extracting all 22 documents to text.

All 22 extracted cleanly. Now reading every document in full.

All 11 CVs read. Now the letters.

All 22 documents read end to end. Now running a systematic cross-corpus fact-frequency check to isolate single-occurrence claims.

All 22 documents read end to end. Report follows.

---

# Comparative Evaluation — 11 CV + Søknad Packages
## Avinor AS, Seniorrådgiver Digital Transformasjon (FINN 474473271)

---

# Phase 0 — Inventory

**22 files found, 22 files opened and read end to end.** Pairing by full filename stem with the `CV_` / `Soknad_` token removed yields **11 clean pairs, zero orphans.**

| ID | CV file | Søknad file |
|---|---|---|
| `0fa53b-base` | `0fa53b_CV_Avinor…` | `0fa53b_Soknad_Avinor…` |
| `0fa53b-opusx` | `0fa53b_stage3_opusx_20260909T155611Z_CV_…_16500c77` | `0fa53b_stage3_opusx_20260909T155611Z_Soknad_…_16500c77` |
| `0fa53b-solmed` | `0fa53b_stage3_solmed_20260909T160521Z_CV_…_16500c77` | `0fa53b_stage3_solmed_20260909T160521Z_Soknad_…_16500c77` |
| `0fa53b-solxh` | `0fa53b_stage3_solxh_20260909T155607Z_CV_…_16500c77` | `0fa53b_stage3_solxh_20260909T155607Z_Soknad_…_16500c77` |
| `3eeb10-base` | `3eeb10_CV_Avinor…` | `3eeb10_Soknad_Avinor…` |
| `3eeb10-stage1` | `3eeb10_stage1_unknown_20260907T194452Z_CV_…_16500c77` | `3eeb10_stage1_unknown_20260907T194452Z_Soknad_…_16500c77` |
| `0d1af3` | `0d1af3_CV_Avinor…` | `0d1af3_Soknad_Avinor…` |
| `2120b3` | `2120b3_CV_Avinor…` | `2120b3_Soknad_Avinor…` |
| `6d65bd` | `6d65bd_CV_Avinor…` | `6d65bd_Soknad_Avinor…` |
| `93c621` | `93c621_CV_Avinor…` | `93c621_Soknad_Avinor…` |
| `b5104f` | `b5104f_CV_Avinor…` | `b5104f_Soknad_Avinor…` |

**Lineage note.** `0fa53b` contributes four packages (base + three stage-3 variants), `3eeb10` two (base + stage1). Within-lineage comparisons isolate single changes and are used as the primary diagnostic below.

**Document sizes (words):** CVs 409–833; letters 336–557. The corpus spans a 2× range in CV length and a 1.7× range in letter length — length is one of the real variables.

---

# Phase 1 — Rubrics

## Rubric A — CV

`Score = 0.22·F + 0.18·E + 0.15·V + 0.18·C + 0.12·S + 0.08·N + 0.07·D` (each sub-score 0–100)

| Cat | Definition | W | Low (≤60) | Mid (~78) | Top (≥90) |
|---|---|---|---|---|---|
| **F — Role fit & framing** | Whether the document presents a *transformation adviser* or a *technical analyst*, given identical facts | .22 | Headline and first bullets lead with Excel/VBA tooling; reads as senior spreadsheet developer | Gevinst present but competing with tooling for the top slot | Headline and profile lead with gevinstmetodikk / styringsmodeller; delivery work is positioned as *proof of execution*, not as the trade |
| **E — Evidence density** | Named systems, scope markers, counts, named outcomes per unit of text | .18 | Present-tense generic duties, no scope | Some scope markers, uneven | Every major bullet carries an artefact, a scale, and a downstream state |
| **V — Outcome & value logic** | Does impact reach *adoption*, not just activity | .15 | Verbs stop at "utviklet", "bidro til" | Outcomes stated but undated/unscoped | Adoption stated with duration and reach ("innført som sykehusdekkende standard … 2,5 år senere") |
| **C — Credibility & non-inflation** | Verifiability under Avinor's stated background check; presence of honest scope markers | .18 | Unsupported precision; no limits anywhere | Clean but uniformly assertive | Corroborated specifics + volunteered limits ("dels innført og dels foreslått", "ble avviklet") |
| **S — Scannability (45 s)** | Payload in the top third; bullet and length discipline | .12 | 8+ core-area items, 5-line bullets, 800+ words | Readable but front-loading imperfect | ≤6 core areas, 2–3-line bullets, best three assets visible without scrolling |
| **N — Norwegian & register** | Bokmål quality, precision, seniority of tone | .08 | Noun-stacking, calques, sloppy compounds | Correct but flat | Precise, economical, senior; correct compound hyphenation |
| **D — Distinctiveness** | Sounds like this person, not a generated template | .07 | Interchangeable noun-pairs | One or two individual sentences | A profile sentence no other candidate could write |

## Rubric B — Application letter

`Score = 0.15·H + 0.18·A + 0.20·J + 0.15·P + 0.17·C + 0.08·N + 0.07·K`

| Cat | Definition | W | Low (≤60) | Mid (~78) | Top (≥90) |
|---|---|---|---|---|---|
| **H — Opening** | What the first 25 words buy | .15 | "Jeg søker stillingen…" + restated ad | Competent abstraction about digital change | In medias res on a concrete problem, or a stated point of view |
| **A — Argument architecture** | Thesis and development vs. episode list | .18 | Three episodes in sequence, no spine | Loose theme | Explicit thesis, each paragraph advancing it, synthesis at the end |
| **J — Judgement shown** | The thing a CV structurally cannot carry: constraints, trade-offs, rejected options | .20 | Narrates the CV | One decision explained | Multiple decisions with the reasoning and the constraint that shaped them |
| **P — Vacancy engagement w/o parroting** | Requirement *converted* into the candidate's own evidence | .15 | Ad phrases recycled as flattery | Ad terms used, lightly earned | Zero lifted phrasing; the ad's demand restated as the candidate's own working principle |
| **C — Credibility & calibration** | Willingness to state what is not known or not held | .17 | No limit named anywhere | One hedge | Explicit non-claims about measurement, mandate, or sector |
| **N — Norwegian prose** | Flow, punctuation, register | .08 | Clumsy, calqued | Correct | Rhythmic, controlled, senior |
| **K — Close** | Does the last line earn a reply | .07 | "Ser frem til å høre fra dere" | Polite, generic | Specific offer or a question back to the reader |

## Rubric C — Package (pair-level only)

`Score = 0.20·X + 0.22·R + 0.20·G + 0.13·W + 0.15·O + 0.10·Z`

| Cat | Definition | W | Low (≤60) | Mid (~78) | Top (≥90) |
|---|---|---|---|---|---|
| **X — Cross-document consistency** | Dates, scope, titles, numeral convention, framing of the same episode | .20 | Same episode framed incompatibly | Aligned facts, drifting conventions | Facts, hedges and numeral style identical across both |
| **R — Complementarity vs redundancy** | Does the letter *add*, or re-tell | .22 | Letter is the CV with connectives | Some added reasoning | Letter carries only what the CV structurally cannot: constraint, trade-off, concession, motivation |
| **G — Combined vacancy coverage** | What the *set* covers and what it leaves uncovered | .20 | Major assets absent from both documents | Core covered, breadth thin | Gevinst, governance, delivery, facilitation and analysis all evidenced somewhere in the set |
| **W — Voice continuity** | One drafting hand across two instruments | .13 | Two different writers | Compatible | Same voice, correctly modulated by genre |
| **O — 45-second set test** | Reading order effect; combined length | .15 | Both documents open on the same low-value material; >1250 words combined | One document front-loads well | Both open on the strongest asset; set reads in under a minute |
| **Z — Combined credibility risk** | Total unverifiable surface minus total volunteered limits | .10 | Dense unsupported specifics, zero concessions | Balanced | Low unsupported surface, concession present in the letter |

---

# Phase 2 — CVs

## The corpus-wide framing problem

One finding governs the whole CV table. The candidate's strongest *evidence of execution* is the modernisation of a ~20-year-old Excel/VBA budgeting tool. It is also the **worst possible headline** for a Seniorrådgiver Digital Transformasjon. The ad asks for gevinstrealisering, styringsmodeller, porteføljestyring and beslutningsgrunnlag for ledelse; it never asks for a developer. Every CV in this corpus makes a choice about whether that tool goes first — and that single ordering decision moves a CV more than any other variable.

Second governing fact: the candidate started 03.2023. Against "Flere års erfaring fra strategisk utviklingsarbeid", 3.5 years is thin. That means **thinness is not neutral here** — a short CV amplifies the one weakness the candidate cannot argue away, which is why the compressed variants underperform their polish.

## Per-CV analysis

**`0fa53b-opusx` (722 w).** Leads with the discipline, not the job title: *"GEVINSTMETODIKK OG DIGITAL GJENNOMFØRING"*, and the profile closes on a genuine point of view — *"Jeg vurderer hva et gevinstanslag kan bygge på, og gjør forutsetningene synlige for dem som skal bruke tallene."* Ordering is exactly right for this ad: methodology → investment basis → delivery → work-form design. Strongest move: the proxy-model bullet is the most complete piece of evidence in the corpus — *"vektet proxymodell over fire grenmodeller og en konsolideringsmodell, med synlige og justerbare vekter, skjemakontrollert overføring i Power Query og kontroller for umappede rader og skjemaavvik."* Weakest move: it silently drops the base variant's honesty markers and adds two claims found nowhere else in 22 documents (*"la til GAM-modellering"*, *"bemannings-, UTA- og vaktgrunnlag"*).

**`3eeb10-stage1` (706 w).** The most trustworthy CV in the corpus. Profile is distinctive and memorable — *"Arbeider med å få digitale forbedringer gjennom i virksomhetskritiske prosesser som ikke kan stanses underveis."* Volunteers limits twice: *"Enkelte praksiser ble innført, andre foreslått"* and *"Løsningen ble avviklet i februar 2026"*. Strongest move: naming what was *not* adopted, in a document where nobody would have checked. Weakest move: it spends its first two experience bullets on the budget tool before reaching gevinst, and its KJERNEOMRÅDER block is seven items of 15–25 words each — a wall exactly where a recruiter needs a scan.

**`3eeb10-base` (641 w).** Headline hits three ad terms cleanly (*"DIGITALISERING, GEVINSTREALISERING OG VIRKSOMHETSSTYRING"*) and the profile converts the ad's "bygge bro" requirement instead of quoting it: *"Arbeidet mitt ligger der teknologi, økonomi og organisasjon møtes: styringsmodeller, beslutningsgrunnlag og kontrollert innføring."* Strongest move: the most honest single line about the allocation model anywhere — *"Modellen er utformet; innføring og endelige vekter er ikke avklart."* Weakest move: the budget tool again occupies bullet one, and numeral style is mixed inside one document (*"om lag 50"* alongside *"tjue år"*).

**`0fa53b-solxh` (486 w).** The best-edited CV in the corpus. Six core areas, seven bullets, correct ordering. Strongest move: it puts the *decision* in the verb — *"Avviste direkte fordeling da bruksdata ikke ga et forsvarlig grunnlag, og utformet i stedet en vektet proxy-modell"* — which is the single most transferable sentence construction here. Weakest move: it buys that cleanliness by deleting the Power BI ownership, the forecasting work and every honesty marker; for a candidate whose seniority is already the open question, 486 words is under-armed.

**`b5104f` (704 w).** The best headline in the corpus for this specific ad — *"GEVINSTREALISERING, STYRINGSMODELLER OG KONTROLLERT DIGITAL ENDRING"* — with *styringsmodeller* lifted straight from "Vi tror du har" and immediately earned by the bullets below it. Strongest move: it is the only CV that shows an *option appraisal*, which is what a seniorrådgiver actually does: *"Vurderte VBA, Office Scripts, Python og KI-støttede alternativer mot kompatibilitet, driftsrisiko og vedlikeholdbarhet."* Weakest move: it carries four claims that appear in no other document — *"om lag 15 ark og 78 globale navn"*, *"JIT, ADI, REGERP, GAT"*, *"dbt og Pega"*, *"Microsoft Fabric, Power Platform, dbt, Pega og Python"* — against an employer that states it verifies CV contents. It also closes with a tool-list bullet that dilutes a senior register into a résumé of pilots.

**`0fa53b-base` (833 w).** The richest and the least disciplined. Eight core areas; one bullet runs five lines on AI working method (*"prosjektinstruksjoner med omfang, kildepresedens og stoppregler, tilstands- og overleveringsdokumentasjon, tester og bevisplikter"*) — genuinely distinctive, and about something the ad never asks for. Strongest move: the only CV that dates and bounds the BI ownership honestly (*"Eide løsningen fra om lag august 2025 til februar 2026 … Løsningen ble avviklet i februar 2026"*). Weakest move: *"Registrert som superbruker for kunstig intelligens ved OUS i om lag tre år"* appears in no other document, and at 833 words the best material is behind a wall.

**`0fa53b-solmed` (469 w).** Clean, correctly ordered, pleasant. Strongest move: the profile names the four audiences the ad cares about — *"ledere, controllere, fagmiljøer og tekniske samarbeidspartnere."* Weakest move: compression has damaged content. *"Har også vesentlig bidratt til en første komponent i en driftsrapport"* is unparseable for an outside reader, and *"Deltok i etableringsgruppen for en firepersoners analyseavdeling"* misstates the fact every other variant renders correctly — it was a four-person *group establishing* the department, not a four-person department.

**`93c621` (446 w).** Correctly leads with gevinst and keeps the honest caveat (*"modellen er utformet, ikke innført"*). Weakest move: the KJERNEOMRÅDER block is the most template-like in the corpus — *"Gevinstrealisering og verdisikring · Virksomhetsstyring og beslutningsgrunnlag · Digitalisering og kontrollert modernisering"* — eight interchangeable noun-pairs that could belong to any consultant. The headline also runs the full page width without landing a phrase.

**`6d65bd` (507 w).** Two honesty markers, decent ordering after the first bullet. Weakest move: a genre error. The CV profile contains a pitch — *"For Avinors arbeid på tvers av digitale initiativer er bidraget å gjøre forventet verdi, avhengigheter og vilkår for gjennomføring tydelige før løsningene tas i bruk"* — which is the letter's job, and which welds a supposedly durable document to one application. It also carries the corpus's emptiest bullet ending: *"bidro til en del av en innledende rapport."*

**`2120b3` (413 w).** Same genre error, more explicit: *"For Avinor er denne kombinasjonen relevant når digitale investeringer skal bli til konkrete endringer med tydelig verdilogikk…"* Strongest move: *"var rapportert i bruk om lag 2,5 år senere"* — the *rapportert* hedge is a small, genuinely credible touch nobody else uses. Weakest move: the allocation/investment model — the candidate's single best "beslutningsgrunnlag" evidence and the closest thing he has to the ad's core ask — is **absent entirely**.

**`0d1af3` (409 w).** The thinnest. Four major assets missing: the allocation model, the BI ownership, the forecasting work, the Analyseavdelingen establishment. What remains is stated at duty-level: *"Utformer strukturer for arbeidsinntak, prioritering og avhengigheter, og planlegger og fasiliterer workshops"* — present tense, no scope, no outcome. It is competent and forgettable.

## Head-to-head: what separates adjacent ranks

- **1 vs 2 (opusx → stage1):** ordering. Both are dense and well-written; opusx puts gevinstmetodikk in bullet one and stage1 puts the Excel tool there. That costs stage1 roughly eight points of Fit, which its superior credibility (two volunteered limits vs zero) does not quite recover.
- **2 vs 3 (stage1 → 3eeb10-base):** completeness of outcome. stage1 states *"i sykehusdekkende bruk i budsjettprosessene for 2026 og 2027"*; base stops at *"budsjettet for 2026"*. Same work, one extra year of demonstrated adoption.
- **3 vs 4 (3eeb10-base → solxh):** substance vs speed. solxh scans better and has the sharper verbs; 3eeb10-base has ~150 more words of verifiable content and the honest model caveat. For a thin-seniority candidate, substance wins by a hair. These two are near-indistinguishable.
- **4 vs 5 (solxh → b5104f):** b5104f is the better-argued document and the riskier one. It would outrank solxh on every category except C, where four uncorroborated specifics against a stated background-check regime cost it more than its extra density earns.
- **5 vs 6 (b5104f → 0fa53b-base):** editing. Same lineage of richness; b5104f spends it on ten bullets, base spends it on eleven plus an off-target AI-method essay and 833 words.
- **6 vs 7 (0fa53b-base → solmed):** density beats polish. solmed is cleaner and says materially less.
- **7 vs 8 vs 9 (solmed → 93c621 → 6d65bd):** three competent, forgettable CVs separated by defect type — solmed by a factual slip, 93c621 by template-grade core areas, 6d65bd by putting the pitch inside the CV.
- **10 vs 11 (2120b3 → 0d1af3):** both lose the same four assets; 2120b3 keeps marginally more scope language and the *rapportert* hedge.

## CV rank table

| # | Package | **Final** | F .22 | E .18 | V .15 | C .18 | S .12 | N .08 | D .07 | One-line reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `0fa53b-opusx` | **84** | 90 | 88 | 85 | 76 | 78 | 88 | 85 | Only CV that orders itself by the ad's priorities and still carries full evidence density; two uncorroborated specifics are the sole drag |
| 2 | `3eeb10-stage1` | **83** | 80 | 88 | 86 | 88 | 68 | 86 | 88 | Most trustworthy record in the corpus — volunteers what wasn't adopted — but opens on the Excel tool and buries it under a seven-item core-areas wall |
| 3 | `3eeb10-base` | **82** | 82 | 85 | 82 | 87 | 70 | 87 | 85 | Best profile-to-ad conversion and the frankest model caveat; loses to stage1 only on the 2027 adoption year |
| 4 | `0fa53b-solxh` | **81** | 86 | 74 | 80 | 80 | 90 | 88 | 80 | Best-edited CV and the sharpest verbs; bought its cleanliness by deleting BI, forecasting and every honesty marker |
| 5 | `b5104f` | **80** | 88 | 92 | 84 | 62 | 72 | 87 | 86 | Best headline and the only genuine option appraisal, attached to the corpus's highest fabrication surface *(override: computed 81.3; −1.3 — four uncorroborated specifics against a stated background check are under-priced by C alone)* |
| 6 | `0fa53b-base` | **79** | 82 | 90 | 84 | 74 | 58 | 85 | 87 | Richest content, worst discipline: 833 words, eight core areas, and a five-line AI-method bullet the ad never asked for |
| 7 | `0fa53b-solmed` | **78** | 80 | 70 | 78 | 80 | 86 | 82 | 70 | Clean and correctly ordered, but compression damaged content and introduced the "firepersoners analyseavdeling" slip |
| 8 | `93c621` | **77** | 80 | 70 | 76 | 84 | 82 | 84 | 66 | Leads with gevinst and keeps the honest caveat; core areas are eight interchangeable noun-pairs any consultant could own |
| 9 | `6d65bd` | **76** | 76 | 74 | 78 | 84 | 80 | 80 | 72 | Honest and serviceable, but puts the Avinor pitch inside the CV profile and ends two bullets on near-empty phrases |
| 10 | `2120b3` | **74** | 74 | 62 | 72 | 82 | 84 | 82 | 66 | Same genre error, plus the allocation model — the closest asset to the ad's core ask — is missing entirely |
| 11 | `0d1af3` | **73** | 74 | 58 | 70 | 82 | 84 | 83 | 64 | Four major assets absent; what remains is stated as present-tense duties with no scope or outcome |

---

# Phase 3 — Application letters

## Per-letter analysis

**`0fa53b-base` (429 w).** Opens in medias res, no throat-clearing: *"Da gevinstene fra et sterilforsyningsprosjekt ved Oslo universitetssykehus skulle fordeles mellom klinikkene, fantes det ikke bruksdata som bar en direkte fordeling."* Strongest move — and the single most credibility-building sentence in all 22 documents: *"Målt tidsbesparelse eller feilreduksjon har jeg ikke tall på. Det som er dokumentert, er at verktøyet er i bruk."* A hiring manager who reads that trusts everything around it. Its one ad-phrase is used as a hook, not filler: *"…er kjernen i det Avinor beskriver når enheten for Digital Transformasjon skal sikre at investeringer i teknologi gir faktisk verdi."* Weakest move: paragraph three is dense and Excel-heavy, and the Avinor connection is thinner than the variants'.

**`0fa53b-opusx` (557 w).** The best-architected letter here. It states a thesis and then executes it: *"arbeidet mitt har i hovedsak dreid seg om to spørsmål: hva et gevinstanslag kan bygge på når datagrunnlaget er svakt, og hva som skal til for at en digital endring faktisk blir tatt i bruk."* Answers Q1, answers Q2, synthesises. Strongest move: it shows an integrity decision, not just a technical one — *"I stedet for å presentere indirekte tall som observert bruk, utformet jeg en vektet proxymodell"* — and closes the loop honestly: *"Hvilke gevinster som siden er realisert, kan jeg ikke svare for. Det modellen gjør, er å vise hva anslagene hviler på."* Zero lifted ad phrasing. Weakest move: 557 words with a flat opening line (*"Jeg søker stillingen som seniorrådgiver i Digital Transformasjon."*) — the best-reasoned letter in the corpus spends its most valuable sentence on a formality.

**`3eeb10-stage1` (436 w).** Strongest move, and the best single passage in the corpus: *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn. Det er at dere driver noe som ikke kan settes på pause mens det forbedres."* It pre-empts the obvious objection and converts it into the actual argument. Backed by voluntary downscaling — *"Jeg var med i firepersonsgruppen som etablerte Analyseavdelingen, i langt mindre skala"* — and a genuinely specific close. Weakest move: the budget tool arrives in sentence two and holds the floor for two paragraphs, so a strategy-role reader spends the first twenty seconds on Excel.

**`b5104f` (434 w).** Best thesis statement in the corpus: *"Et gjennomgående tema i arbeidet er avstanden mellom hva en investering ble begrunnet med og hva som senere lar seg vise. Den avstanden lukkes av at gevinstlogikken er avklart før pengene brukes, ikke av flere rapporter etterpå."* That is the ad's premise restated as the candidate's own conviction — the highest form of vacancy engagement. Strongest move: the close turns the tables — *"Jeg tar gjerne en samtale om hvordan enheten tenker å måle verdien av initiativene den skal prioritere mellom."* Confident, senior, and it earns a reply. Weakest move: **zero concessions anywhere.** The letter never says what he doesn't have, which against a thin-seniority profile reads as unexamined rather than confident.

**`3eeb10-base` (405 w).** Strongest move: the best reasoning metaphor here — *"Jeg tok den rammen og kjøpte forsvarligheten med kontroll i stedet for med omfang"* — followed by the corpus's clearest working principle: *"Der gevinsten ikke lar seg måle direkte, gjør jeg heller forutsetningen synlig enn å lage presisjon som ikke finnes."* Weakest move: paragraph two is the most technical passage in any letter — *"logikken lå spredt mellom formler, navngitte områder og makrokode i kopier som hadde vokst fra hverandre"* — and a Digital Transformasjon reader files that under "spreadsheet specialist". Real framing damage, self-inflicted early.

**`0fa53b-solxh` (380 w).** Strongest move: the mandate disclaimer, correctly placed — *"Min påvirkning har i hovedsak vært funksjonell, gjennom struktur, faglige vurderinger og leveranser, ikke gjennom linje- eller programmyndighet."* Balanced, correctly sequenced, everything covered. Weakest move: nothing in it is memorable. It is competent in every paragraph and arresting in none — the letter a recruiter finishes and cannot quote back.

**`0fa53b-solmed` (355 w).** Strongest move: the sharpest version of the disclaimer, and it names the gap against the ad's exact word — *"Rollen min har vært prosjekt- og metodeorientert, ikke et formelt konsernmandat for portefølje- eller programledelse."* That is brave and precise. Also good: *"skille tydelig mellom et beslutningsgrunnlag, en forventet gevinst og en effekt som faktisk er målt."* Weakest move: the shortest letter crams two separate episodes into one paragraph and spends two of its scarce phrases on ad vocabulary (*samfunnsoppdrag*, *strategiske initiativer*).

**`6d65bd` (414 w).** Strongest move: real methodological substance, expressed concretely — *"Jeg skilte mellom driftsmessige og økonomiske virkninger, unngåtte kostnader og belastning som flyttes mellom enheter."* That is what gevinstrealisering actually consists of, and no other letter shows it at that grain. Weakest move: structure is a list. Paragraph two is a 150-word block entirely about the Excel tool, placed second, after an opening paragraph of flat self-description.

**`93c621` (346 w).** Strongest move: opens with an assertion about the *role*, not the candidate — *"Avinors nye transformasjonsmiljø skal gjøre mer enn å foreslå teknologi"* — which is a confident register. Weakest move: a bokmål punctuation error in that same sentence (capitalised *"Det"* after a colon, where lowercase is required), in a document whose entire claim is precision. Paragraph four then dissolves into abstraction (*"en meningsfull neste anvendelse av erfaringen min"*).

**`0d1af3` (336 w).** Strongest move: a clean thematic opening — *"digital endring først skaper verdi når prioritering, gjennomføring og bruk henger sammen."* Weakest move: the whole letter stays at that altitude. Three of five paragraphs describe method-in-general rather than an episode, and paragraph four is unbranded consultant-speak: *"Jeg avklarer formål, brukere, avhengigheter, risiko og akseptansekriterier, og omsetter dette til gjennomførbare oppgaver."* It also ends twice — the final one-line paragraph restates the one above it.

**`2120b3` (367 w).** Weakest move, and it's structural: the heaviest vacancy-parroting in the corpus (four lifted phrases). It opens by reciting Avinor's own facts back to Avinor (*"på tvers av 43 flyplasser og i flysikringen"*) and closes by reciting Avinor's own values (*"Avinors kombinasjon av samfunnskritisk infrastruktur, sikker drift og bærekraftig utvikling gjør oppgaven faglig meningsfull."*). Strongest move: paragraph three carries genuine gevinst substance and the *"rapportert i bruk"* hedge. It also ends twice.

## Head-to-head: what separates adjacent ranks

- **1 vs 2 (0fa53b-base → opusx):** the first sentence and the last hundred words. opusx has the better architecture; base has the better opening and is 128 words shorter. In a document read in 45 seconds, the opening wins.
- **2 vs 3 (opusx → stage1):** reasoning depth vs trust. opusx explains more decisions; stage1 makes the single strongest trust move (the aviation concession). opusx edges it on architecture.
- **3 vs 4 (stage1 → b5104f):** calibration. b5104f is the more polished document and concedes nothing; stage1 concedes twice. Against a candidate whose central risk is seniority overclaim, the concession is worth more than the polish.
- **4 vs 5 (b5104f → 3eeb10-base):** opening altitude. Both are strongly reasoned; 3eeb10-base spends paragraph two on named ranges and macro copies and frames itself downward.
- **5 vs 6 (3eeb10-base → solxh):** memorability. solxh is better balanced and has no quotable line; 3eeb10-base has two.
- **6 vs 7 (solxh → solmed):** length. Same lineage, same disclaimer move, solmed 25 words shorter and correspondingly thinner in evidence.
- **7 vs 8 vs 9 (solmed → 6d65bd → 93c621):** 6d65bd has the better substance and the worse structure; 93c621 the better opening and the thinner middle.
- **9 vs 10 vs 11:** a cliff, not a step. 93c621 still argues; 0d1af3 describes method; 2120b3 flatters.

## Application rank table

| # | Package | **Final** | H .15 | A .18 | J .20 | P .15 | C .17 | N .08 | K .07 | One-line reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `0fa53b-base` | **90** | 95 | 88 | 92 | 86 | 96 | 89 | 82 | Opens in medias res on a real problem and contains the corpus's most trust-building sentence: *"Målt tidsbesparelse … har jeg ikke tall på"* |
| 2 | `0fa53b-opusx` | **88** | 66 | 95 | 94 | 88 | 94 | 90 | 88 | Best architecture and deepest reasoning, zero parroting; wastes its most valuable sentence on a formality and runs 557 words |
| 3 | `3eeb10-stage1` | **87** | 72 | 82 | 90 | 92 | 96 | 90 | 88 | Pre-empts the aviation objection and converts it into the argument; opens on the Excel tool and holds it two paragraphs |
| 4 | `b5104f` | **86** | 92 | 90 | 86 | 84 | 78 | 91 | 92 | Best thesis and boldest close in the corpus; concedes nothing anywhere, which reads as unexamined against a thin-seniority profile |
| 5 | `3eeb10-base` | **85** | 76 | 80 | 92 | 88 | 92 | 91 | 72 | Two of the best reasoning lines here; paragraph two frames the candidate down to spreadsheet specialist |
| 6 | `0fa53b-solxh` | **82** | 74 | 84 | 78 | 84 | 90 | 88 | 78 | Balanced, honest about mandate, correctly sequenced — and impossible to quote back afterwards |
| 7 | `0fa53b-solmed` | **80** | 76 | 80 | 78 | 76 | 90 | 87 | 72 | Sharpest mandate disclaimer in the corpus, in the thinnest letter; two ad phrases it could not afford |
| 8 | `6d65bd` | **79** | 70 | 72 | 82 | 80 | 88 | 85 | 74 | Best gevinst substance at grain level, delivered as an episode list behind a flat opening and a 150-word Excel block |
| 9 | `93c621` | **78** | 82 | 76 | 76 | 74 | 86 | 78 | 70 | Confident opening assertion undercut by a bokmål punctuation error in the same sentence and an abstraction-heavy fourth paragraph |
| 10 | `0d1af3` | **72** | 76 | 70 | 66 | 66 | 78 | 84 | 66 | Stays at method-in-general altitude throughout, concedes nothing, and ends twice |
| 11 | `2120b3` | **70** | 72 | 70 | 68 | 54 | 80 | 84 | 68 | Recites Avinor's facts and values back to Avinor; makes the flattery move three times and the evidence move twice |

---

# Phase 4 — Packages

Read as a recruiter would: CV first, then letter, in sequence.

**`3eeb10-stage1` — 89.** The best-functioning pair. Consistency is flawless: both documents say *"budsjettprosessene for 2026 og 2027"*, both spell numerals out (*"rundt femti"*, *"to og et halvt"*, *"tjue år"*), both hedge the same episodes the same way. Complementarity is the highest here because the letter does the one thing a CV structurally cannot — it concedes. *"Der har jeg ingen bakgrunn"* and *"i langt mindre skala"* have no possible CV equivalent, and they convert the CV's density from assertion into testimony. Coverage is broad: gevinst method, allocation model, controlled delivery, work-intake design, facilitation, forecasting, BI. The one defect is reading order: **both** documents open on the budget tool, so the set spends the recruiter's first thirty seconds in each on Excel/VBA. That is what keeps it from 92, not anything it says.

**`0fa53b-opusx` — 87.** The best-framed pair. Both documents lead with gevinstmetodikk; the letter's two-question thesis is a direct expansion of the CV's profile sentence. Highest lexical overlap in the corpus (11.2% of the letter's 5-grams appear in the CV), but the overlap is entity names, not argument — the letter adds the rejected option, the mandate constraint (*"innføringsansvarlig krevde en smal, funksjonsvis refaktorering"*), and the deliberate design choice (*"Kjerne-VBA holdt jeg bevisst utenfor"*), none of which the CV carries. Perfect internal consistency. The cost is bulk: 722 + 557 = **1279 words, the heaviest set here**, and neither document opens fast.

**`0fa53b-base` — 84.** The corpus's best letter attached to its sixth-best CV. The letter's calibration (*"har jeg ikke tall på"*) is precisely the complement a dense CV needs, and the division of labour is clean. The pair breaks on the CV side: 833 words, and the AI-methodology material — including *"Registrert som superbruker for kunstig intelligens ved OUS i om lag tre år"* — has no counterpart anywhere in the letter, so it reads as an unexplained tangent that the set never resolves. A recruiter reaching the letter has already spent their attention.

**`3eeb10-base` — 82.** Internally excellent, externally mis-aimed. Consistency is perfect and both documents keep the honest caveat — but that *is* the redundancy: the same hedge on the same episode in near-identical words (*"Modellen er utformet; innføring og endelige vekter er ikke avklart"* / *"Den modellen er utformet, ikke innført"*). Both lead with the budget tool, and the letter's paragraph two is the most technical passage in any letter here. The set reads as an outstanding controlled-delivery engineer applying for a strategy role.

**`0fa53b-solxh` — 81.** The fastest set in the corpus (866 words combined) and the least additive. The letter walks the CV's bullets in the CV's order with connective tissue; read in sequence, the second document teaches you approximately one new thing — the functional-not-line-authority point. Coverage is correspondingly thin: no BI ownership, no forecasting, no decommissioning honesty anywhere in the set.

**`0fa53b-solmed` — 80.** Genuinely non-redundant — the lowest overlap of any 0fa53b variant (4.3%) — and the letter's mandate disclaimer is the best-aimed concession in the corpus. But combined coverage is the problem: between both documents the set never mentions the styringsløsning, the forecasting work, the risikoregister, or the ~50-stakeholder scale. *(Override: computed 82.6; −2.6. The O and R categories over-reward brevity here. For a candidate whose seniority is the open question, a set this thin does not read as senior, and that is disqualifying against this ad in a way the category weights do not capture. The same reasoning takes solxh from 81.9 to 81.)*

**`b5104f` — 79.** Individually the fourth-best letter and fifth-best CV; as a pair, the highest-risk set here. The CV carries four uncorroborated specifics and the letter carries zero concessions, so nothing anywhere in the set says what the candidate does not have — against an employer that states *"Vi gjennomfører bakgrunnssjekk for å bekrefte opplysninger i CV og vitnemål."* Redundancy is also real: the sterile-logistics episode runs at near-equal length in both, and the VBA/Office Scripts/Python appraisal appears in both. Voice has a visible seam — the CV uses *"2,5 år"*/*"rundt 50"*, the letter *"to og et halvt"*/*"rundt femti"*/*"tjue år"*. Defensible as genre convention, but read in sequence the two documents don't sound like one drafting pass.

**`6d65bd` — 78.** Lowest literal overlap in the corpus (2.0%) — but the redundancy is semantic, not lexical: the same design-not-adopted caveat, the same budget tool at length, the same four-person group, all reworded rather than divided. The CV's Avinor-directed profile sentence duplicates the letter's function outright, so the set makes its pitch twice and its case once.

**`93c621` — 77.** Shortest combined set (792 w), consistent throughout (*"2026-prosessen"* in both, *"ikke innført"* in both). But the letter's paragraph two and the CV's first two bullets carry the same two episodes in the same order with the same caveats — this is the third package where the pair duplicates a hedge rather than dividing labour. Coverage thin on both sides.

**`0d1af3` — 74.** The worst combined coverage here. The allocation model, the BI ownership, the forecasting work and the Analyseavdelingen establishment are absent from **both** documents — four assets the corpus proves he has, invisible to this recruiter. The letter's paragraphs two and three restate the CV's bullets one and two with connective prose and no added reasoning. Consistency is perfect, which is cheap when there is little to be inconsistent about.

**`2120b3` — 73.** Same four coverage gaps, plus the parroting compounds across the pair: the CV profile addresses Avinor, the letter opens on Avinor's facts and closes on Avinor's values. Voice continuity is technically high — it is continuously the wrong register. The set flatters three times and evidences twice.

## Package rank table

| # | Package | **Final** | X .20 | R .22 | G .20 | W .13 | O .15 | Z .10 | One-line reason |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `3eeb10-stage1` | **89** | 96 | 92 | 86 | 96 | 70 | 90 | Flawless consistency and the only pair where the letter concedes what the CV cannot; loses points because both documents open on Excel |
| 2 | `0fa53b-opusx` | **87** | 94 | 90 | 86 | 94 | 76 | 80 | Best-framed pair — both lead with gevinst, letter supplies every constraint the CV omits; 1279 words is the heaviest read here |
| 3 | `0fa53b-base` | **84** | 92 | 88 | 90 | 90 | 62 | 76 | Corpus's best letter and broadest coverage, dragged by an 833-word CV whose AI tangent the letter never resolves |
| 4 | `3eeb10-base` | **82** | 92 | 76 | 82 | 92 | 68 | 88 | Internally excellent and externally mis-aimed; both documents lead with the tool and duplicate the same hedge |
| 5 | `0fa53b-solxh` | **81** | 92 | 66 | 74 | 92 | 92 | 84 | Fastest set in the corpus and the least additive — the letter re-walks the CV and adds one new point *(override: computed 81.9, see solmed note)* |
| 6 | `0fa53b-solmed` | **80** | 88 | 78 | 70 | 90 | 90 | 86 | Genuinely non-redundant with the sharpest mandate concession, but the set omits four assets and reads junior *(override: computed 82.6; −2.6, brevity over-rewarded)* |
| 7 | `b5104f` | **79** | 84 | 74 | 92 | 80 | 84 | 58 | Best-argued letter bolted to the highest-risk CV; four uncorroborated specifics, zero concessions, and a visible numeral seam |
| 8 | `6d65bd` | **78** | 88 | 74 | 76 | 82 | 76 | 84 | Reworded rather than divided — lowest literal overlap, high semantic redundancy, and the CV does the letter's job |
| 9 | `93c621` | **77** | 88 | 66 | 68 | 84 | 88 | 84 | Fast and consistent, but the pair duplicates two episodes and their caveats instead of splitting record from reasoning |
| 10 | `0d1af3` | **74** | 90 | 58 | 56 | 86 | 86 | 82 | Four proven assets missing from both documents; the letter narrates the CV with connectives and no added judgement |
| 11 | `2120b3` | **73** | 90 | 60 | 56 | 84 | 82 | 80 | Same coverage holes, and the set flatters Avinor three times while evidencing twice |

---

# Fabrication watch

**Method.** Eleven renderings of one factual base. A specific claim appearing in one or two documents, where nine others render the same episode without it, is a candidate generator artefact. **Caveat stated plainly:** single occurrence is *evidence of risk, not proof of falsehood* — a longer variant naturally surfaces true detail the compressed ones drop. But this employer states *"Vi gjennomfører bakgrunnssjekk for å bekrefte opplysninger i CV og vitnemål"*, which makes unverifiable precision an asymmetric bet. Penalised under **C** (CV) and **Z** (package), proportionally.

| Claim | Package | Occurrences / 22 | Assessment |
|---|---|---|---|
| *"(Excel/VBA, om lag 15 ark og 78 globale navn)"* | `b5104f` CV | **1** | **Highest risk.** Two precise counts of an internal artefact. Nine other renderings describe the same tool with no counts. Precision of exactly this kind is what a verification call tests. |
| *"Koblet data fra blant annet JIT, ADI, REGERP, GAT og DRG-/aktivitetsrapporter"* | `b5104f` CV | **1** | **High risk.** REGERP and DRG are corpus-wide; *JIT*, *ADI*, *GAT* appear nowhere else. Also opaque acronyms to an Avinor reader — cost without benefit. |
| *"Plattformutforsking: Microsoft Fabric, Power Platform, dbt og Pega"* / *"…dbt, Pega og Python"* | `b5104f` CV | **1** (Fabric 2, dbt/Pega 1) | **Elevated.** `6d65bd` corroborates *"Fabric og Power Platform"*; *dbt* and *Pega* are unique to b5104f and stated twice within it. |
| *"Registrert som superbruker for kunstig intelligens ved OUS i om lag tre år."* | `0fa53b-base` CV | **1** | **Elevated.** A named internal designation with a duration. Also arithmetically tight against a 03.2023 start. |
| *"…la til GAM-modellering og stiller krav om tidsriktige holdout-tester"* | `0fa53b-opusx` CV | **1** (GAM) | **Moderate.** *holdout* is corroborated by `3eeb10-stage1`; *GAM-modellering* is unique. Reads as a generator adding technical texture. |
| *"kvalitetssikring av bemannings-, UTA- og vaktgrunnlag"* | `0fa53b-opusx` CV | **1** (UTA) | **Moderate.** Nine variants render this as *"bemannings- og vaktgrunnlag"*. An inserted sector acronym. |
| *"lekkasjekontroll"* | `3eeb10-stage1` CV | **1** | **Low.** Standard companion to holdout testing, which is corroborated. Plausible domain detail. |
| *"Fem arbeidsbøker"* | `3eeb10-stage1` CV | **1** | **Cleared.** Arithmetically corroborated by the corpus-wide *"fire grenmodeller og en konsolideringsmodell"* (= 5). Not a fabrication. |

**Corroborated across ≥6 documents and treated as the stable factual base:** the four-person gevinstrealisering team and its adoption as sykehusdekkende standard ~2.5 years on; the ~20-year-old Excel/VBA budgeting tool, ~50 stakeholders, sole/principal coding developer, the narrower mandate imposed by the implementation lead, ~80% behaviour-preserving refactoring, differansekontroll + akseptansekriterier + risikoregister, controller onboarding; the sterile-logistics weighted proxy model with four branch models plus consolidation, visible adjustable assumptions, VBA deliberately excluded, handed to controllers early 2026; the four-person Analyseavdelingen establishment group; the Power BI backend ownership and its February 2026 decommissioning; the REGERP conversion tools; and the entire education, earlier-experience, tillitsverv and language blocks, which are byte-identical across all eleven.

**One divergence that is not fabrication.** The budget tool's adoption scope splits 6/5 across the corpus between *"budsjettprosess for 2026"* and *"budsjettprosessene for 2026 og 2027"*. Given a 2026-09 application date and the 2027 process running now, both are defensible; the later variants simply claim the additional year. **Critically, no package contradicts itself on this axis** — every pair states the same scope in CV and letter. Verified across all eleven.

---

# Phase 5 — The three tables together

## CV rank

| # | Package | Score | F | E | V | C | S | N | D | Reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `0fa53b-opusx` | 84 | 90 | 88 | 85 | 76 | 78 | 88 | 85 | Ad-priority ordering with full evidence density; two uncorroborated specifics the only drag |
| 2 | `3eeb10-stage1` | 83 | 80 | 88 | 86 | 88 | 68 | 86 | 88 | Most trustworthy record; opens on Excel, buried under a core-areas wall |
| 3 | `3eeb10-base` | 82 | 82 | 85 | 82 | 87 | 70 | 87 | 85 | Best profile-to-ad conversion, frankest caveat; loses on the 2027 adoption year |
| 4 | `0fa53b-solxh` | 81 | 86 | 74 | 80 | 80 | 90 | 88 | 80 | Best-edited, sharpest verbs; paid for it by deleting BI, forecasting and every hedge |
| 5 | `b5104f` | 80 | 88 | 92 | 84 | 62 | 72 | 87 | 86 | Best headline and only real option appraisal, highest fabrication surface |
| 6 | `0fa53b-base` | 79 | 82 | 90 | 84 | 74 | 58 | 85 | 87 | Richest content, worst discipline — 833 words and an off-target AI essay |
| 7 | `0fa53b-solmed` | 78 | 80 | 70 | 78 | 80 | 86 | 82 | 70 | Clean but compression-damaged; introduces a factual slip |
| 8 | `93c621` | 77 | 80 | 70 | 76 | 84 | 82 | 84 | 66 | Right ordering, honest caveat, template-grade core areas |
| 9 | `6d65bd` | 76 | 76 | 74 | 78 | 84 | 80 | 80 | 72 | Puts the Avinor pitch in the CV; two near-empty bullets |
| 10 | `2120b3` | 74 | 74 | 62 | 72 | 82 | 84 | 82 | 66 | Genre error plus the allocation model missing entirely |
| 11 | `0d1af3` | 73 | 74 | 58 | 70 | 82 | 84 | 83 | 64 | Four assets absent; duties stated without scope or outcome |

## Application rank

| # | Package | Score | H | A | J | P | C | N | K | Reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `0fa53b-base` | 90 | 95 | 88 | 92 | 86 | 96 | 89 | 82 | In medias res opening + the corpus's most trust-building sentence |
| 2 | `0fa53b-opusx` | 88 | 66 | 95 | 94 | 88 | 94 | 90 | 88 | Best architecture, deepest reasoning, zero parroting; flat opening, 557 words |
| 3 | `3eeb10-stage1` | 87 | 72 | 82 | 90 | 92 | 96 | 90 | 88 | Converts the aviation objection into the argument; opens on Excel |
| 4 | `b5104f` | 86 | 92 | 90 | 86 | 84 | 78 | 91 | 92 | Best thesis, boldest close, zero concessions anywhere |
| 5 | `3eeb10-base` | 85 | 76 | 80 | 92 | 88 | 92 | 91 | 72 | Two outstanding reasoning lines; paragraph two frames him down |
| 6 | `0fa53b-solxh` | 82 | 74 | 84 | 78 | 84 | 90 | 88 | 78 | Balanced and honest; nothing quotable afterwards |
| 7 | `0fa53b-solmed` | 80 | 76 | 80 | 78 | 76 | 90 | 87 | 72 | Sharpest mandate concession in the thinnest letter |
| 8 | `6d65bd` | 79 | 70 | 72 | 82 | 80 | 88 | 85 | 74 | Best gevinst substance, delivered as a list behind an Excel block |
| 9 | `93c621` | 78 | 82 | 76 | 76 | 74 | 86 | 78 | 70 | Confident opening undercut by a punctuation error in the same sentence |
| 10 | `0d1af3` | 72 | 76 | 70 | 66 | 66 | 78 | 84 | 66 | Method-in-general throughout; concedes nothing; ends twice |
| 11 | `2120b3` | 70 | 72 | 70 | 68 | 54 | 80 | 84 | 68 | Recites Avinor back to Avinor; flatters more than it evidences |

## Package rank

| # | Package | Score | X | R | G | W | O | Z | Reason |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `3eeb10-stage1` | 89 | 96 | 92 | 86 | 96 | 70 | 90 | Only pair where the letter concedes what the CV cannot; both open on Excel |
| 2 | `0fa53b-opusx` | 87 | 94 | 90 | 86 | 94 | 76 | 80 | Best-framed pair; 1279 words is the heaviest read in the corpus |
| 3 | `0fa53b-base` | 84 | 92 | 88 | 90 | 90 | 62 | 76 | Best letter, broadest coverage, dragged by an 833-word CV with an unresolved tangent |
| 4 | `3eeb10-base` | 82 | 92 | 76 | 82 | 92 | 68 | 88 | Excellent internally, mis-aimed externally; duplicates its own hedge |
| 5 | `0fa53b-solxh` | 81 | 92 | 66 | 74 | 92 | 92 | 84 | Fastest and least additive; letter adds one new point |
| 6 | `0fa53b-solmed` | 80 | 88 | 78 | 70 | 90 | 90 | 86 | Non-redundant with the sharpest concession; omits four assets, reads junior |
| 7 | `b5104f` | 79 | 84 | 74 | 92 | 80 | 84 | 58 | Best-argued letter, highest-risk CV, zero concessions, visible numeral seam |
| 8 | `6d65bd` | 78 | 88 | 74 | 76 | 82 | 76 | 84 | Reworded rather than divided; CV does the letter's job |
| 9 | `93c621` | 77 | 88 | 66 | 68 | 84 | 88 | 84 | Duplicates two episodes and their caveats instead of splitting record from reasoning |
| 10 | `0d1af3` | 74 | 90 | 58 | 56 | 86 | 86 | 82 | Four proven assets missing from both documents |
| 11 | `2120b3` | 73 | 90 | 60 | 56 | 84 | 82 | 80 | Flatters three times, evidences twice |

**Near-indistinguishable pairs, ordered anyway:** `3eeb10-base` / `0fa53b-solxh` at CV level (0.5 pt computed apart — substance-per-word broke it) and `0fa53b-solmed` / `0fa53b-solxh` at package level (0.7 pt — coverage broke it).

---

# Phase 6 — The strongest set

**Strongest CV: `0fa53b-opusx` (84). Strongest letter: `0fa53b-base` (90).** Same lineage, different stage — the base letter was never paired with the opusx CV.

## Does the mix hold together?

**Facts — clean.** Both state *"i sykehusdekkende bruk i budsjettprosessene for 2026 og 2027"*. Both date the proxy model to *"tidlig i 2026"* and hand it to controllers. Both state the four-person team and the ~2.5-year standard. The CV's *"Var i praksis eneste kodende utvikler"* and the letter's *"Jeg gjorde i praksis alle kodeendringene"* are the same claim. **No contradiction found.**

**Critically:** the letter's *"Målt tidsbesparelse eller feilreduksjon har jeg ikke tall på"* is not undercut anywhere in the opusx CV — the CV makes no measured-savings claim. The concession lands cleanly.

**Three real seams:**
1. **Numeral convention clashes.** CV: *"2,5 år"*, *"om lag 50"*, *"20 år"*. Letter: *"to og et halvt"*, *"om lag femti"*, *"tjue år"*. Genre-defensible in isolation; read in sequence it is a visible seam.
2. **Scrum/Kanban is orphaned.** The letter claims *"med Scrum- og Kanban-strukturer"*; the opusx CV's Analyseavdelingen bullet says only *"oppgavehierarki og WIP-styring"*. The letter introduces a term the CV does not anchor.
3. **Two unsupported CV specifics survive** (*GAM-modellering*, *UTA-*) with no letter counterpart.

**Redundancy:** the sterile-logistics episode appears in both, but correctly divided — the letter leads with the *problem*, the CV with the *artefact*. Acceptable as-is.

**Tone:** the CV is analytical and compressed; the letter is narrative and concessive. That is a productive contrast, not a clash — record vs. argument, which is what the pair rubric rewards.

## Hybrid scored against Rubric C

| X | R | G | W | O | Z | **Total** |
|---|---|---|---|---|---|---|
| 92 | 94 | 90 | 88 | 82 | 82 | **89** |

## Does it beat the best intact package?

**No — it ties it.** Hybrid 89.0 vs `3eeb10-stage1` 88.6. That gap is noise, and I will not dress it up as a win.

The reason is worth stating: the hybrid trades **trust for framing.** It gains the better opening order (gevinst first in both documents, where stage1 opens on Excel in both) and the corpus's best letter opening. It gives up stage1's spotless verification record and its aviation concession — the single strongest trust move in 22 documents, for which the hybrid has no equivalent.

**The useful finding is that a lightly edited hybrid clears both, by roughly 3 points.** The edits are cheap and the ceiling is real: **~92**.

## Concrete edits to make the mixed set coherent

**In the `0fa53b-opusx` CV:**

1. In the forecasting bullet, cut `la til GAM-modellering og` — leaving *"Bygde orkestratoren og det meste av automatikken rundt, og stiller krav om tidsriktige holdout-tester, baselinjer og akseptansekriterier."* Single-occurrence claim; the sentence loses nothing.
2. In the final BUK bullet, change `kvalitetssikring av bemannings-, UTA- og vaktgrunnlag` to `kvalitetssikring av bemannings- og vaktgrunnlag` — matches nine other renderings and removes an acronym opaque to an Avinor reader.
3. Delete the eighth KJERNEOMRÅDER item, `KI-støttet utvikling med menneskelig gjennomgang, validering og ansvar` — the ad never asks for it, and the block should hold six, not eight.
4. In the Analyseavdelingen bullet, change `ansvars- og avhengighetsfordeling, oppgavehierarki og WIP-styring` to `ansvars- og avhengighetsfordeling, Scrum- og Kanban-strukturer, oppgavehierarki og WIP-styring` — anchors the term the letter uses.
5. Change `om lag 2,5 år senere` to `om lag to og et halvt år senere`, `om lag 50 deltakere` to `om lag femti deltakere`, and `på om lag 20 år` to `på om lag tjue år` — aligns to the letter's convention and removes the seam.

**In the `0fa53b-base` letter:**

6. In paragraph 3, cut `innenfor en prosess med om lag femti deltakere i arbeidsgrupper og kravavklaringer` — the CV carries the number; spend the space on reasoning.
7. **Import stage1's concession.** Insert before the closing paragraph: *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn. Det er at dere driver noe som ikke kan settes på pause mens det forbedres."* This is the corpus's strongest trust move and the hybrid's only structural gap.
8. **Import solmed's mandate line.** In paragraph 4, after *"Noe ble tatt i bruk, annet ble lagt fram som forslag."*, insert: *"Rollen min har vært prosjekt- og metodeorientert, ikke et formelt konsernmandat for portefølje- eller programledelse."* Pre-empts the ad's *porteføljestyring* requirement instead of leaving the reader to find the gap.
9. **Do not touch** *"Målt tidsbesparelse eller feilreduksjon har jeg ikke tall på. Det som er dokumentert, er at verktøyet er i bruk."* — the highest-value two sentences in the corpus.
10. **Do not touch** the opening sentence. Every alternative in the corpus is worse.

---

# The deltas — what actually separates top from bottom

Eight transferable moves, each demonstrated by the spread in this corpus:

1. **Lead with the requirement you match best, not the work you did most of.** Every top-four package opens on gevinst/value logic; every bottom-two opens on the Excel tool or on Avinor flattery. Identical facts, ~15 points of separation.
2. **Concede something specific, in the letter.** All four top packages name a limit; both bottom packages name none. `3eeb10-stage1`'s *"Der har jeg ingen bakgrunn"* and `0fa53b-base`'s *"har jeg ikke tall på"* buy more credibility than any additional achievement would have.
3. **Convert the ad; never quote it.** `2120b3` hits four lifted phrases and ranks last; `0fa53b-opusx` hits zero and ranks second. The strongest conversion is `b5104f`'s *"Den avstanden lukkes av at gevinstlogikken er avklart før pengene brukes, ikke av flere rapporter etterpå"* — the ad's premise, in the candidate's own conviction.
4. **Put the decision in the verb.** *"Avviste direkte fordeling da bruksdata ikke ga et forsvarlig grunnlag"* (`solxh`) does in one clause what *"Utformet en modell for gevinstfordeling"* (`0fa53b-base`) needs three to imply. Judgement verbs read senior; construction verbs read technical.
5. **Keep the pitch out of the CV.** `2120b3` and `6d65bd` both open the CV profile with *"For Avinor…"*. Both rank 9th–10th. It duplicates the letter and dates a document that should outlive one application.
6. **Let the letter carry what the CV structurally cannot:** the constraint (*"implementeringsansvarlig satte en smalere ramme"*), the rejected option, the mandate boundary, the thing you don't know. The packages that split record from reasoning score 84–89; the ones where the letter re-narrates score 73–79.
7. **Cover the assets somewhere in the set.** `0d1af3` and `2120b3` lose the allocation model, the BI ownership, the forecasting work and the department establishment from *both* documents. That is a coverage failure, not a length failure — and it is invisible when you review either document alone.
8. **Do not buy density with unverifiable precision.** `b5104f` has the best headline and the best-argued letter in the corpus and lands 7th at package level, because *"om lag 15 ark og 78 globale navn"* and *"JIT, ADI … GAT"* are exactly what a stated background check tests. Corroborated scope (*"om lag 50 deltakere"*) is worth more than uncorroborated precision.

**One honest corpus-wide weakness, not graded on a curve.** Not one of the eleven packages evidences **porteføljestyring at group level, styringsgrupper, or beslutningsfora** — three things the ad asks for explicitly. The best packages handle this by naming the gap (`solmed`, `solxh`); the rest leave the recruiter to find it. No amount of reordering fixes it, because the underlying experience isn't there. The three packages that say so out loud are the ones that survive an interview.

---

**Pipeline read:** the `0fa53b` stage-3 relay and the `3eeb10` stage-1 pass both improved on their bases — but in opposite directions. Stage-3 `opusx` bought framing and lost hedges; `3eeb10-stage1` bought hedges and kept the bad ordering. Neither stage learned to do both, which is precisely the ~3-point gap the hybrid edit list closes.

Want this as a published page with the three tables side by side and the edit list as a checklist? One call.