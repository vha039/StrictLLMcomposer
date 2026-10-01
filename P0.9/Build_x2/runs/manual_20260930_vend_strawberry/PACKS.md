# Manuelle pakker: Vend (1), Strawberry (2)

Skrevet direkte fra de tre kandidatmyndighetene og Stage 3-reglene. Ingen strategi, ingen selected_evidence-pakke, ingen EV-refs, ingen preview/render/submit. Bokmål (frameworkregel), selv om begge annonser er på engelsk.

---

# 1. VEND: Senior Product Analyst, ReCommerce

## Brev

Da gevinstene fra steril logistikk skulle fordeles mellom klinikker, var dataene om faktisk bruk for svake til en direkte fordeling. Jeg utformet i stedet en modell med vektede, indirekte indikatorer og åpne forutsetninger, slik at controllerne selv kan undersøke og justere dem. Modellen ble ferdigstilt og overlevert til controllerne tidlig i 2026. Den måten å tenke om måling på, hva tallene faktisk kan bære, vil jeg bruke i produktanalysen i ReCommerce.

I en analyseavdeling på fire hadde jeg hovedansvaret for datamodellen og beregningene i et styringsdashbord for økonomi, bemanning og aktivitet, mens kolleger ledet innhold og visualisering. Jeg bygde nesten hele den semantiske modellen og valgte stjerneskjema etter å ha vurdert alternativer, fordi det passet Power BI og var lettest å vedlikeholde. Jeg testet dashbordet med faktiske brukere, observerte hvor de ble usikre og brukte det i korte forbedringsrunder. Jeg eide og drev det månedlig fra august 2025 til det ble avviklet rundt februar 2026.

I prognoseprosjektet for pasientvolum og sengebehov, som fortsatt er under utvikling, har jeg arkitekturen og orkestreringen sammen med en kollega og kodeagenter. Jeg definerte og utfordret prognosemålet, og krever tidsbevisste holdouts, sammenligning med enkle baselines og kontroll for lekkasje før et resultat får gjelde. Kodeagentene jobber etter faste prosjektinstruksjoner med krav til tester og gjennomgang, og jeg svarer på tekniske spørsmål om KI som registrert superbruker ved OUS.

Fra økonometrien kjenner jeg spørsmålet om hva som er effekt og hva som er støy, og jeg vil bruke det på eksperimentene i ReCommerce. Jeg vil gjerne høre hvilke definisjoner og målinger dere vil bygge først, og hvor jeg kan komme raskest til nytte.

## CV (dynamiske soner)

**Overskrift:** Samfunnsøkonom | Analytiker for måling og beslutningsstøtte

**Profil:** Samfunnsøkonom med master fra NTNU og rådgiver i økonomi og IKT ved Oslo universitetssykehus. Bygger målemodeller og beslutningsstøtte fra uklare behov til brukt leveranse. Var hovedutvikler av datamodell og beregninger i et brukertestet styringsdashbord og utformet en gevinstmodell med åpne forutsetninger der direkte bruksdata ikke var tilstrekkelige. Har arkitektur og orkestrering i et prognoseprosjekt under utvikling, med tidsbevisst validering og lekkasjekontroll. Bruker Power BI, DAX, SQL, R og Python, og KI-støttet utvikling under menneskelig gjennomgang.

**Nøkkelkompetanser:**
- Måledesign, KPI-er og beslutningsstøtte med åpne forutsetninger
- Semantiske modeller og datamodellering i Power BI, DAX og Power Query
- SQL og analyse i R og Python
- Validering: tidsbevisste holdouts, baselines, lekkasjekontroll og avstemming
- Brukertesting og forbedringsrunder
- KI-støttet analyse og utvikling med menneskelig gjennomgang
- Økonometri og anvendt empirisk metode (NTNU)

**EMP_OUS_ANALYSE (erstatter alle baselinepunkter):**
- Hovedutvikler av datamodell og beregninger i et styringsdashbord for økonomi, bemanning og aktivitet i en analyseavdeling på fire: nesten hele den semantiske modellen, det meste av ETL i Power Query og om lag 80-90 prosent av DAX. Kolleger ledet innhold og visualisering. Eier med månedlig drift fra om lag august 2025 til avviklingen rundt februar 2026.
- Gjennomførte veiledede tester av dashbordet med faktiske brukere, observerte hvor de ble usikre og brukte tilbakemeldingene i avgrensede forbedringsrunder.
- Utformet en modell for gevinstfordeling og investeringsvalg i steril logistikk der direkte bruksdata ikke bar en forsvarlig fordeling: vektede, indirekte indikatorer, synlige og justerbare forutsetninger og kontroller for umappede rader og avvik, fordelt på fem arbeidsbøker. Ferdigstilt og overlevert til controllere tidlig i 2026.
- Har arkitektur, orkestrering og automatisering i et pågående prognoseprosjekt (14, 90 og 365 dager) for pasientvolum og kapasitet, sammen med en kollega og kodeagenter. Definerte og utfordret prognosemålet, krevde tidsbevisste holdouts, baselines og lekkasjekontroll og la til GAM-modellering. Under utvikling.
- Medutviklet en metode for gevinstrealisering og gevinstestimering i et team på fire. Innført som sykehusdekkende standard og fortsatt i bruk om lag 2,5 år senere.
- Ledet en intern workshop om datamodellering, Power Query og DAX for økonomer og helseøkonomer, og lærte opp teknisk personale i en annen rapporterings- og dataorganisasjon i Power BI og semantiske modeller.
- Registrert KI-superbruker ved OUS i om lag tre år, med svar på tekniske henvendelser i en Teams-kanal.

**EMP_OUS_BAR (erstatter alle baselinepunkter):**
- Overtok hele den tildelte månedsoppgjørsflyten innen om lag tre måneder, med avstemming, kvalitetssikring, resultatforklaring og rapportering til klinikkledere.
- Utviklet på eget initiativ Excel/VBA-verktøy for konvertering og validering ved overgangen til REGERP. Brukt av økonomirådgivere i flere klinikker kort etter overgangen.
- Leverte seksjonsvise DRG-estimater med Stata, R og Power Query til budsjett og planlegging, og bygget et eget budsjetthjelpeark.

Andre ansettelser: baselinepunkter uendret.

## Review
- **triage:** READY
- **reasons:**
  1. Flere utlyste kjerneområder er ikke dokumentert: produkteksperimenter (A/B), markedsplass-/produktteam, Tableau, Amplitude, Snowflake, Streamlit og dbt (dbt kun pilot-eksponering). Teksten påstår ingen av dem. Handling: bestem om paret sendes med dette som kjent hull.
  2. SQL er dokumentert som "gjentatte ganger del av stacken", ikke verifisert flytende. Handling: ikke hevd flytende SQL i intervju uten å kunne vise det.
  3. Annonsen er engelsk (arbeidsspråk engelsk og norsk), paret er Bokmål. Handling: bestem språk før innsending; engelsk versjon kan lages.
- **known_limitations:** ingen produkteksperimentering eller markedsplasserfaring; ingen dokumentert Tableau/Amplitude/Snowflake/Streamlit; dashbordet er avviklet (historisk, ikke nåværende eierskap); prognoseprosjektet er under utvikling med delt forfatterskap og uten verifisert ytelse; gevinstmodellens organisatoriske bruk og realisert gevinst er uavklart; eksperimentsetningen bygger på akademisk økonometri, ikke praktisk erfaring.
- **material_strategy_change:** Rute valgt fra kildene: målejudgment (gevinstmodellen) + semantisk modell + prognosevalidering + KI-arbeidsmåte, ikke BI-backend-identitet. Ingen strategifil å sammenligne med.
- **upstream_claim_repaired:** Ingen (ingen oppstrømsstrategi fantes).
- **notes:** Uløst IMPORTANT: "Design and interpret experiments" er ubesvart i begge dokumenter utover økonometribroen i brevets avslutning. Ingen støttet evidens finnes for produkteksperimenter.

---

# 2. STRAWBERRY: MarTech Specialist (12 måneders prosjektstilling)

## Brev

Ved overgangen til REGERP måtte gamle konteringslinjer over i det nye formatet. Jeg tok selv initiativ til Excel/VBA-verktøy som konverterte og validerte linjene, og lærte VBA fra grunnen underveis. Økonomirådgivere i flere klinikker brukte verktøyene kort etter overgangen.

I 2025 gjennomførte jeg kodeendringene i moderniseringen av sykehusets budsjettverktøy, i praksis som eneste utvikler, innenfor en prosess med om lag 50 deltakere og en egen implementeringsleder. Hovedendringen erstattet manuell kopiering av bemanningsdata fra en annen arbeidsbok med integrerte data. Rammen var en smal refaktorering, funksjon for funksjon, der omtrent 80 prosent av endringene skulle bevare eksisterende oppførsel. Jeg sammenlignet gamle og nye funksjoner for å avdekke logikkdrift, arbeidet mot akseptansekriterier og et risikoregister, og laget opplæringsmateriell for controllerne. Moderniserte versjoner av verktøyet er brukt sykehusdekkende i budsjettprosessene for 2026 og 2027.

Kravene avgjør mye før utviklingen begynner. Jeg har utformet strukturerte spørreskjemaer for arbeidsinntak som fanger formål, brukere, beslutningsbehov, avhengigheter, risiko, prioritet og akseptansekriterier, og vurdert Forms, Loop, Power BI og lavkodealternativer for samme behov. Når andre skal bruke det som er bygget, følger jeg opp: jeg har lært opp teknisk personale i en annen organisasjon i Power BI og modellering, og svarer på tekniske henvendelser i en Teams-kanal som registrert KI-superbruker. I sykehusmiljøet jobber jeg under personvern- og sikkerhetskrav, og har blant annet gått gjennom notebooks og repositorier for gjenværende sensitive data.

Arbeidet mellom markedsføringsteamene og arkitektene, der krav blir til oppsett man kan dokumentere og drifte, ligner det jeg allerede gjør mellom økonomi og IT. Jeg vil gjerne høre hvilke oppsett og integrasjoner som står først i køen for MarTech-teamet, og hvordan dere ser for dere at de første ukene i prosjektet skal brukes.

## CV (dynamiske soner)

**Overskrift:** Rådgiver Økonomi og IKT | Krav, dataløsninger og innføring

**Profil:** Rådgiver i økonomi og IKT ved Oslo universitetssykehus med master i samfunnsøkonomi fra NTNU. Omsetter uklare behov til avgrensede tekniske løsninger med krav, kontroller, dokumentasjon og opplæring. Gjennomførte kodeendringene i moderniseringen av sykehusets budsjettverktøy i 2025, i en prosess med om lag 50 deltakere. Har bygget egne verktøy for datakonvertering og validering ved en systemovergang og koblet data fra flere kildesystemer i økonomiprosesser. Arbeider under personvern- og sikkerhetskrav, støtter kolleger som registrert KI-superbruker og bruker KI-støttet utvikling under menneskelig gjennomgang.

**Nøkkelkompetanser:**
- Behovsavklaring, kravstruktur og akseptansekriterier
- Datamodeller, SQL og Power Query, og sammenkobling av kildesystemer
- Kontrollert endring: funksjonsvis sammenligning, risikoregister og dokumentasjon
- Onboarding, opplæring og teknisk brukerstøtte
- Datakvalitet og personvernbevisst arbeid i regulert miljø
- KI-støttet utvikling med menneskelig gjennomgang

**EMP_OUS_ANALYSE (erstatter alle baselinepunkter):**
- Gjennomførte kodeendringene i moderniseringen av et arvet Excel/VBA-budsjettverktøy i 2025, i praksis som eneste kodende utvikler, i en interessentprosess med om lag 50 deltakere. Integrerte bemanningsdata som tidligere måtte kopieres fra en annen arbeidsbok. Kontrollerte endringene funksjon for funksjon mot tidligere oppførsel, med akseptansekriterier og risikoregister, og laget opplæringsmateriell for controllere. Moderniserte versjoner er brukt sykehusdekkende i budsjettprosessene for 2026 og 2027.
- Utformet strukturerte spørreskjemaer for arbeidsinntak (formål, brukere, beslutningsbehov, avhengigheter, risiko, prioritet, akseptansekriterier) og evaluerte Forms-, Loop-, Power BI-, Pega- og lavkodealternativer. Design og evaluering på prosjektnivå.
- Hovedutvikler av datamodell og ETL i et styringsdashbord for økonomi, bemanning og aktivitet. Testet med faktiske brukere og drev det månedlig som eier fra om lag august 2025 til avviklingen rundt februar 2026.
- Utformet en gevinstmodell i fem arbeidsbøker med synlige, justerbare forutsetninger og Power Query-overføring med skjemakontroll, slik at controllere kan justere uten utvikler. Ferdigstilt og overlevert tidlig i 2026.
- Lærte opp teknisk personale i en annen rapporterings- og dataorganisasjon i Power BI og modellering, og ledet en intern BI-workshop for økonomer.
- Har arkitektur og orkestrering i et pågående prognoseprosjekt sammen med en kollega og kodeagenter, med prosjektinstruksjoner, tester og gjennomgang. Registrert KI-superbruker i om lag tre år, med svar på tekniske henvendelser i en Teams-kanal.

**EMP_OUS_BAR (erstatter alle baselinepunkter):**
- Utviklet på eget initiativ Excel/VBA-verktøy for konvertering og validering ved overgangen til REGERP og lærte VBA gjennom arbeidet. Brukt av økonomirådgivere i flere klinikker kort etter overgangen.
- Koblet data fra flere kildesystemer (blant annet JIT, ADI, REGERP, GAT og personell- og lønnsgrunnlag) i kontrollkritiske økonomiprosesser, dokumenterte arbeidssteg og utviklet kontroll- og valideringslogikk.
- Overtok hele den tildelte månedsoppgjørsflyten innen om lag tre måneder og rapporterte til klinikkledere.

Andre ansettelser: baselinepunkter uendret.

## Review
- **triage:** READY
- **reasons:**
  1. Minstekravet "3+ års hands-on MarTech/Marketing Operations" er ikke oppfylt, og kildene har ingen Braze-, mParticle-, Dynamic Yield-, Contentful-, API- eller webhook-erfaring. Teksten påstår ingenting av dette, men svarer heller ikke på kravet. Handling: bestem selv om søknaden sendes som overførbarhetscase; ikke lov plattformerfaring i intervju.
  2. "AI-piloter i live bruk" er ikke dokumentert (prognoseprosjektet er under utvikling, plattformpiloter er eksploratoriske). KI-superbruker og KI-støttet utvikling er brukt som tilgrensende bevis uten pilot- eller produksjonspåstand.
  3. Annonsen er engelsk; paret er Bokmål. Fristen er i dag og stillingen fylles løpende. Engelsk versjon kan lages.
- **known_limitations:** ingen MarTech-plattformerfaring; ingen API/webhook-erfaring dokumentert (SQL og datamodeller støttet); ingen personalisering eller kundeengasjement i praksis (Sector Alarm 2013 er salg, ikke brukt); SQL-dybde ikke verifisert; spørreskjema- og verktøyarbeidet er design og evaluering, ikke utrullet.
- **material_strategy_change:** Rute: ROLE-DIGITAL-01 (krav til kontrollert løsning, opplæring, dokumentasjon), med rask verktøylæring (VBA fra grunnen, månedsoppgjør på ca. tre måneder) som svar på om kandidaten kommer raskt i gang. Ingen strategifil å sammenligne med.
- **upstream_claim_repaired:** Ingen.
- **notes:** Uløst MINIMUM/IMPORTANT: MarTech-erfaring (3+ år), plattformerfaring og AI-piloter er ubesvart i begge dokumenter fordi ingen støttet evidens finnes. Brevets avslutning knytter motivasjon til krav-til-oppsett-arbeidet, ikke hoteller eller merkevare.
