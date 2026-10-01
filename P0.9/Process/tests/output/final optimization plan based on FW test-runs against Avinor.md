# Avinor-testene: svakheter og konkret optimaliseringsplan

Utgangspunktet er godt: Rammeverket finner en troverdig kombinasjon av økonomisk vurdering, gevinstmetodikk og teknisk gjennomføring. Problemet er fordelingen av oppmerksomhet. Det beskriver ofte kontrollen av verktøyet grundigere enn endringen i arbeidet, og kandidatens grense mot konsernansvar tydeligere enn hans dokumenterte samarbeid. Den største forbedringen er å gjøre argumentutvalget mer oppgavedekkende, håndtere forbehold ved selve påstanden og kutte tekniske gjentakelser før innholdslåsen. Deretter bør den konkrete malfriksjonen fjernes.

Dette er et forslag, ikke en implementering. Ingen rammeverksfiler, kandidatfakta eller eksisterende pakker er endret. Del 1 og 2 i dette dokumentet ble ferdigstilt før de to tidligere rapportene i `output/` ble åpnet. Verken `0d1af3` eller `2120b3` er lest eller brukt her.

## Lesemåte, identifikasjon og bevisstyrke

Alle stier nedenfor er relative til `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`. `B/` betyr `P0.9/Build/`. Linjenumrene gjelder filene lest 10. september 2026. DOCX-sitatene gjelder avsnitt i dokumentkroppen; datoer, topptekst og signatur er ikke argumenttekst. En fraværende instruks kan ikke siteres: slike funn er uttrykkelig merket med den nærmeste eksisterende teksten og det presise fraværet. «Ikke funnet» betyr ikke et logisk bevis for fravær i enhver historisk kopi.

| Kort ID | Entydig filprefiks i `cv/` og `soknad/` | CV / brev, ord |
|---|---|---:|
| A | `0fa53b_` uten stage-suffiks | 819 / 422 |
| AX | `0fa53b_stage3_solxh_20260909T155607Z_` | 472 / 373 |
| AM | `0fa53b_stage3_solmed_20260909T160521Z_` | 455 / 348 |
| AO | `0fa53b_stage3_opusx_20260909T155611Z_` | 708 / 550 |
| B | `b5104f_` | 690 / 427 |
| C | `3eeb10_` uten stage-suffiks | 627 / 398 |
| CX | `3eeb10_stage1_unknown_20260907T194452Z_` | 692 / 429 |
| D | `6d65bd_` | 493 / 407 |
| E | `93c621_` | 432 / 339 |

Ord er mellomromsdelte ord i alle ikke-tomme kroppsavsnitt, inkludert statiske CV-seksjoner. Tallene beskriver omfang, ikke kvalitet. Overskrifter, kontakt, avsnittsrekkefølge og tekst er lest i alle 18 DOCX-er. XML-uttrekk kan sammenføye tekst på hver side av en tabulator eller et linjeskift: `HF03.2023` og `hilsenVegard` er derfor ikke funnet som faktiske skrivefeil.

Word COM lot seg ikke starte for ny eksport i denne sesjonen. Eksisterende run-PDF-er ble derfor brukt der run-DOCX var byte-identisk med test-DOCX. PDF-teksten ble også sammenholdt med DOCX. Visuelt inspisert: A CV/brev, AO CV/brev, B CV/brev, C CV/brev og CX brev. AO-brevets eneste avsnittsmismatch i enkel tekstkontroll skyldes sideskift/topptekst inne i avsnittet; teksten fortsetter på neste side. AX, AM, D og E har ikke fått ny visuell sidekontroll; CX-CV-ens run-kopi var ikke byte-identisk og ble ikke brukt som sikker visuell stedfortreder. Ingen universell påstand om feilfri layout følger av tekstlesningen.

### Hva variantene faktisk isolerer

1. **A, AX, AM og AO:** Samtlige filer under deres `frozen/` er identiske. Strategiene er identiske bortsett fra `binding`. Alle åtte test-DOCX-er matcher sine run-utgaver. AX-mappen heter `stage3_solxh_…`, men manifestets `run_id` bruker `stage3_opt1_…`; AO har tilsvarende `stage3_opt2_…`. Dette er navn/identifikasjon, ikke en policyendring. Strategiens `personality_facets` er PF-12 og PF-08 i alle fire. Forskjellene isolerer **den samlede sluttforfatterutførelsen**, under samme fryste input. Filnavn alene beviser ikke modell, reasoning-innstilling eller identisk samtalekontekst. Én generering per variant gir heller ikke et estimat på modellens forventede kvalitet.
2. **C mot CX:** Ikke et rent Stage-1-forsøk. 20 fryste filer er forskjellige: alle tre faktamyndigheter, baseline, personprofil, to genererte indekser, settings, begge stageinstrukser, de tre skrivedokumentene og sju schemaer. Både strategi og slutttekst er nye. Det er særlig viktig at overleveringen av PRJ-06 og 2027-statusen for PRJ-03 er bekreftet i den nyere arbeidsmyndigheten. Virkelighetens person er den samme, men rammeverkets tilgjengelige faktagrunnlag er ikke identisk.
3. **D mot E:** Fryste filer er identiske; strategienes shortlist-tese er også lik. Forskjellen i klarhet og konkret økonomisk resonnering kan ikke tilskrives en endret live-policy. Historiske mellomprodukter og sluttforfatterutførelse er relevante variabler.
4. **B mot A:** Fryste filer samsvarer med dagens Build i begge run. Strategivalg og fasettutvalg er ulike: B velger PF-01/PF-06/PF-19, A velger PF-12/PF-08. Ingen isolert effekt av én fasett kan utledes.

Kontrollankre: `B/runs/r20260908-154257-0fa53b/{frozen,branches/*/frozen,jobs/avinor_digital_transformasjon/current/strategy.json}` og tilsvarende mapper for øvrige run. WORK-hash begynner `0b39a5105f0d` i C/D/E og `03ebb948b03b` i B/A-familien. Doktrinehashene er henholdsvis `5a7c220b9d7b` og `78c55890ecba`. CV-masterhash er `4eab17783800` i begge generasjoner. Hashprefiksene er identifikatorer for den utførte sammenligningen, ikke selvstendige kvalitetsbevis.

## Del 1 — Svakhetskatalog, viktigst først

### W01 — Gevinstgrunnlag blir hovedsvaret på et bredere gjennomføringsoppdrag

**Dokumentbevis:** AX skriver «gjøre gevinstforventninger etterprøvbare før de inngår i prioriteringer». AO avgrenser sitt umiddelbare bidrag til «arbeidet med å gjøre beslutningsgrunnlag etterprøvbare». Dette er relevant, men Avinor etterspør også faktisk oppfølging av verdi, strategiske initiativer, arbeidsformer, prioritering på tvers og mobilisering av andre. A bruker store deler av brevet på proxy-modell og metode, mens workshops får en kort oppramsing. E nevner «arbeids- og prioriteringsstrukturer» uten å vise særlig mye av arbeidet. Alle ni mangler dokumentert realisert økonomisk effekt og dokumentert konsernporteføljeansvar; disse faktagapene kan ikke skrives bort.

**Bidrag som finnes:** `B/policy/writing/WRITING_DOCTRINE.md:130–153`: «ett dominerende arbeidsgiverproblem», «normalt én eller to bærende bevisenheter» og påstanden «En leser vurderer en pakke omtrent som et gjennomsnitt, ikke som en sum». Dette er en seleksjonsprior som kan gjøre to velutviklede tekniske/økonomiske argumenter til erstatning for dekning av en annen avgjørende oppgave. `B/authorities/Work_experience.md:266`, ruten `BENEFITS_STRATEGY_GOVERNANCE`, setter PRJ-04/06 først og PRJ-08 som støtte. Det er rådgivende utvalg, ikke fakta.

**Bidrag som mangler:** En eksplisitt vurdering av hvilket vesentlig kriterium som fortsatt er ubesvart etter at hovedbevisene er valgt, og hvor den gjenværende evidensen faktisk skal synes i paret. Kravregistrering finnes allerede: Stage 1 `:66–72`, og A-strategiens R05/R07/R09 beskriver gapene godt. Mangelen ligger i overgangen fra registrering til synlig dokumentallokering, ikke i et manglende kravschema.

**Konfidens:** Høy for ubalanse og tilgjengelig motbevis; middels for doktrinens bidrag. At AX og AO divergerer med identisk input viser at dette er en påvirkning, ikke en nødvendig følge. Bekreftes hvis en ny allokeringsinstruks gir konkret workshop-/mottakerarbeid uten å svekke gevinstargumentet; svekkes hvis slikt innhold fortsatt fortrenges ved identisk øvrig input.

### W02 — Ukjent status blir skrevet som et sikkert negativt faktum

**Dokumentbevis:** E CV: «modellen er utformet, ikke innført». D CV: «Arbeidet dokumenterer modelldesign, ikke innføring eller realisert gevinst» er mer presist, men D brev går lenger: «Modellen var et design, ikke en innført løsning». C brev: «Den modellen er utformet, ikke innført.» Nyere A/AX/AM/AO/B/CX sier ferdigstilt og overlevert tidlig i 2026.

**Bidrag som finnes:** I C/D/E sin fryste `authorities/Work_experience.md:633` står «Implementation by branch, final weights, controller handover, organizational use and realized benefits remain unresolved». `:643` sier «implementation/adoption unresolved». Dette støtter et dokumentasjonstak, ikke et kategorisk historisk fravær. Dagens schema `B/schemas/strategy.schema.json`, `evidence_plan[].claim_ceiling`, beskrives som «What this evidence may NOT be used to claim», mens lifecycle er ett valgfritt enum. Det favoriserer en enkel negativ avgrensning dersom forfatteren ikke skiller epistemisk usikkerhet fra faktisk tilstand.

**Bidrag som mangler:** En kort eksplisitt regel om at «ikke dokumentert» ikke betyr «ikke skjedd». Dagens WORK `:110` har allerede flerdimensjonal statuskontroll, og `:575–586` har den senere bekreftelsen; dette trenger ikke et nytt statusapparat.

**Konfidens:** Høy for feilslutningen og kildeforskjellen. De nyere formuleringene er ikke bevis på bedre skriving alene: en faktisk kildeoppdatering forklarer noe av forbedringen. Neste generering må bruke riktig fryst kilde; ingen historisk run skal «repareres» med live-fakta.

### W03 — Ikke-diskvalifiserende begrensninger får egne salgsavsnitt

**Dokumentbevis:** AM: «Rollen min har vært prosjekt- og metodeorientert, ikke et formelt konsernmandat for portefølje- eller programledelse.» AX: «ikke gjennom linje- eller programmyndighet». A: «Målt tidsbesparelse eller feilreduksjon har jeg ikke tall på. Det som er dokumentert, er at verktøyet er i bruk.» AO: «Hvilke gevinster som siden er realisert, kan jeg ikke svare for.» Disse setningene bruker oppmerksomhet på fravær selv når den foregående formuleringen allerede avgrenser hva kandidaten faktisk gjorde.

**Bidrag som finnes:** A-strategiens `risk_notes`, `evidence_plan[].claim_ceiling` og `personality_facets[].expression_ceiling` inneholder nødvendige grenser. Stage 3 `:54–57` ber om gapbehandling; `:138–166` låser deretter forbehold og sier «When you cannot tell … keep it». En overeksplisitt grense kan dermed bli bevart helt til levering.

**Eksisterende motregel:** `PERSUASION_CALIBRATION.md:57`, `:129–136` avviser allerede defensiv gap-prosa. Det ville være feil å si at kalibrering mangler helt. **Det som mangler**, er en konkret anvendelsesregel før låsen: avgrens først arbeidsverb, eierskap og resultat; skriv et eget forbehold bare når den gjenværende teksten ellers ville villede.

**Konfidens:** Høy for symptom; middels for mekanisme. AX/AM har flere mandatforbehold enn A/AO under samme input. Dette peker særlig mot utførelsen og overgangen til innholdslås.

### W04 — Teknisk innsats får mer plass enn hva som endret seg for virksomheten

**Dokumentbevis:** B CV: «om lag 15 ark og 78 globale navn»; A CV: «om lag 80 til 90 prosent av DAX»; AO CV: «GAM-modellering» og «tidsriktige holdout-tester». E beskriver paritetskontroller og risikoregister, men utelater at bemanningsdata gikk fra manuell kopiering til integrasjon. D og CX gjør denne prosessendringen tydeligere. I AX/AM beholdes den konkrete leveransen med langt mindre teknisk tekst.

**Bidrag som finnes:** WORK `:947` foreskriver «problem/scope + personal action + method/control + supported capability/result». De detaljerte PRJ-03/05/06-postene og teknologiinventaret gjør mekanisme lett å hente. Stage 3 `:65–68` sier «When a passage is both important and awkward, keep it». Dette kan belønne bevaring av tekniske detaljer som er unike, men ikke særlig utslagsgivende for denne stillingen.

**Motregler og mangel:** Doktrinen `:158–161`, `:284–287`, `:481–486` og WORK `:384` advarer allerede mot verktøyoverlast. Mangelen er ikke adgang til å kutte. Det mangler en konsekvent prioritering *innenfor hvert case*: endret arbeid og dokumentert mottaker før intern implementasjonsoppskrift. «Unikt» må ikke fungere som synonym for «vesentlig».

**Konfidens:** Høy for observerbar forskjell, middels for kildepriorene. Ingen grunn til å stramme schemaets antall bullets eller avsnitt.

### W05 — Samarbeid vises som deltakerantall og støtteaktiviteter, sjeldnere som arbeid

**Dokumentbevis:** «om lag 50 deltakere» går igjen, men forteller hvem som var rundt prosjektet, ikke hvem kandidaten avklarte hva med. E CV nøyer seg med «samarbeidet på tvers av organisasjonsgrensen». AO CV har et bedre konkret signal: «Lærte opp teknisk personell … gjennom flere arbeidsmøter». C CV har «Testet med faktiske brukere og kjørte avgrensede forbedringsrunder». AX CV utelater det separate tverrorganisatoriske opplæringsbeviset som AM beholder.

**Bidrag som finnes:** WORK `:382`, `:428` legger «50-person stakeholder context» i feltet `ADOPTION_HUMAN_CHANGE`; dette er sant som omfang, men lett å bruke som samarbeidserstatning. Doktrinens begrensede hovedbevisprior fortrenger PRJ-02/08. K `:98–102` lister handlinger uten å kreve at et faktisk samspill blir lesbart.

**Positivt innhold finnes:** WORK `:336–373` PRJ-02, `:317–319` BI-workshop, `:647–651` etableringsarbeid, `:749–756` kommunikasjon. A-strategien velger dessuten PF-08 med gode guardrails. Det er dermed et utvalgs-/realiseringsproblem, ikke mangel på all samarbeidsevidens. Eksakt beslutningsutfall, motstandshåndtering og godkjenningsvei er likevel uavklart, særlig for PRJ-04 (`:464–466`, `:986`).

**Konfidens:** Høy for underutnyttelse; middels for hvorfor. Et nytt menneskelig konfliktforløp må aldri diktes for å fylle hullet.

### W06 — Uenighet med innføringsansvarlig blir et tilbakevendende hovedmotiv

**Dokumentbevis:** CX åpner med «Jeg anbefalte en bredere ombygging enn rammen tillot». AO: «innføringsansvarlig krevde en smal …», fulgt senere av «der hadde jeg vesentlig større frihet». C: «Jeg tok den rammen og kjøpte forsvarligheten med kontroll i stedet for med omfang». D er roligere: «innføringen fikk en smalere ramme». AX beskriver bare den avtalte endringsrammen.

**Bidrag som finnes:** WORK `:396` forteller eksplisitt om kandidatens anbefaling og implementeringslederens beslutning. PF-06 (`personality_facets.json:90–102`) oppmuntrer selvstendig vurdering og konstruktiv uenighet; B-strategien velger denne. Men samme historie finnes også i A-familien uten PF-06, så fasetten er ingen nødvendig årsak. Stemme `:58` foretrekker en spesifikk vurdering fremfor plattityde.

**Manglende kalibrering:** Når selve avveiningen er relevant, er den uenige personen ofte ikke det. Rammeverket mangler en presis prior for å beholde kompromisset og egen handling, men utelate hvem som avslo kandidatens foretrukne løsning når det ikke forklarer noe avgjørende.

**Konfidens:** Høy for kilde til historien; middels for sosial skade, som er en arbeidsgiverrettet vurdering. Ikke en påstand om kandidatens faktiske samarbeidsevne.

### W07 — Tverrgående påstander går lenger enn de konkrete bevisene

**Dokumentbevis:** A brev: «mellom begrunnelsen for en investering, prioriteringen mellom flere av dem og den praktiske gjennomføringen». De dokumenterte casene gir ikke i seg selv ansvar for prioritering mellom investeringer. C profil: «Jeg gjennomførte moderniseringen … fram til faktisk bruk» kan leses som eierskap til hele innføringen, mens konkret rolle var kodeansvar innenfor en bredere prosess. CX: «den versjonen er … i … 2026 og 2027» glatter over at 2027-moderniseringen var en ny runde. AO: «de to sidene jeg til nå har arbeidet med hver for seg» er en unødvendig biografisk generalisering om et arbeid som ellers beskrives som integrert.

**Bidrag som finnes:** Syntese og funksjonell ekvivalens tillates i D `:382–386`; hele setningers støtte kreves i K `:40–51`. A-strategien beskriver korrekt grensen mot investerings-/porteføljebeslutninger i R07. Mekanisk validering av `used_evidence_refs` er flat kildeoppløsning, ikke påstandskontroll (`package.schema.json:54`).

**Mangel:** Den eksisterende hele-påstanden-regelen blir ikke stabilt anvendt på profil, overgangssetninger og sammenfatninger. De får mindre kildeoppmerksomhet enn casefakta. En ny semantisk dommer i kode ville ikke løse dette forsvarlig; presiser forfatterens egen kildekontroll på disse setningene.

**Konfidens:** Høy for at formuleringene åpner en sterkere lesning; middels for om en rekrutterer faktisk vil lese dem slik. Avgrens arbeid før du velger `READY`.

### W08 — B sin gevinstmaksime er både retorisk skråsikker og faglig for enkel

**Dokumentbevis:** B: «Den avstanden lukkes av at gevinstlogikken er avklart før pengene brukes, ikke av flere rapporter etterpå.» Avklart gevinstlogikk er ikke tilstrekkelig til å lukke forskjellen mellom antatt og faktisk effekt; rollen omfatter nettopp målbar verdi. C sin «kjøpte forsvarligheten» er en annen skrivekunstformulering som krever ekstra tolkning. CX: «Den viktigste endringen var ikke teknisk» setter opp en unødvendig motsetning når neste setning beskriver teknisk integrasjon med operativ verdi.

**Bidrag som finnes:** Stemme `:50–58` ber om mekanisme, årsak og faglig vurdering. Doktrine `:182–186` tillater «en faglig regel begrunnet i den beslutningen». **Mangel:** En avgrensning av hvor generell regelen kan bli: ett godt case bærer ikke en universell påstand om hva som skaper gevinst eller hva som er viktigst.

**Motregel:** Stemme `:169–177` avviser belæring og metodejargong. Dette er en håndhevingssvikt med et mer konkret korrektiv, ikke fravær av all stilveiledning.

**Konfidens:** Høy for tekst og manglende grunnlag for den bastante mekanismen; middels for de øvrige formuleringenes stilkostnad.

### W09 — Arbeidsgiverspesifisitet blir sektoranalogi, og én variant avviser selve sektoren

**Dokumentbevis:** CX: «Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg ingen bakgrunn.» A: «de samme spørsmålene skal besvares på nytt». B nevner «43 lufthavner», men hovedargumentet er fortsatt at sykehus og Avinor ikke kan stoppe driften. D/AX/AM treffer bedre med oppbyggingen av en ny enhet, prioriteringer og forbindelsen mellom verdi og gjennomføring.

**Bidrag som finnes:** D `:435–447` sier at pakken feiler når åpningen passer etter navnebytte, og setter som mål en pakke som «bare kan tilhøre denne arbeidsgiveren og rollen». Stemme `:69–73` avviser påtatt entusiasme. Dette kan drive en forfatter til overtydelig særpreg eller antientusiasme.

**Mangel:** Skillet mellom konkret rollepassform og absolutt unikhet. Flere arbeidsgivere har samme reelle oppgave. Det mangler også et klart forbud mot å utlede manglende interesse av manglende domeneerfaring. Ingen kandidatkilde etablerer den negative luftfartsmotivasjonen.

**Konfidens:** Høy for CX-problemet; middels/lav for den nøyaktige promptårsaken. Bekreftelse ville kreve utførelseslogg eller et kontrollert nytt utfall. Det er ikke bevist at stemmepolicyen skapte setningen.

### W10 — CV og brev bruker samme dokumentasjonskapasitet flere ganger

**Dokumentbevis:** A og AO gjentar proxy-arkitektur, teknisk refaktorering, kontroller, teamstørrelse og varighet i begge dokumenter. I A kommer de samme tre hovedleveransene i profil, kompetanseblokk, erfaringsbullets og brev. AM og AX kutter teknisk detalj, men brevets metode- og budsjettavsnitt gjenforteller fortsatt mye av CV-en.

**Bidrag som finnes:** Pakken har separate felt for profil, kompetanser, erfaringsbullets, åpning, hovedavsnitt og avslutning (`package.schema.json:63–115`); forfatteren kan dermed fylle hver flate som et selvstendig sammendrag. **Motregel:** D `:289–295` er allerede tydelig om komplementaritet. **Mangel:** En konkret sammenlesning før lås som lar samme case deles, men fjerner gjentatt oppskrift og gir brevet en ny beslutningsfunksjon.

**Konfidens:** Høy for redundans, middels for schemaets indirekte påvirkning. Feltene trengs; ikke endre dem.

### W11 — Kompetanseblokken er en fet sammenhengende katalog

**Dokumentbevis:** Alle CV-er har `KJERNEOMRÅDER` og punkter separert med midtpunkt i ett avsnitt. A fyller blokken med blant annet «Scrum og Kanban, WIP», teknologier og «Strukturert, menneskestyrt bruk av KI …». Visuelt konkurrerer den fete blokken med dokumentets hovedbevis. AO og B har samme problem. AX/AM er roligere, men strukturen er identisk.

**Direkte årsak:** `B/templates/template_map.json:48–54`: `transform: "join_middot"`, `prefix: "KJERNEOMRÅDER  "`. `B/runtime/jobbsok/render.py:153–157` gjør `prefix + " · ".join(items)`. `CV_MASTER.docx`, SDT `CV_CORE_COMPETENCE`, har fet tekst og `w:keepLines`. Dette er en deterministisk konstruksjon, ikke bare et språkvalg.

**Mangel:** Ingen nødvendig ny schemafunksjon. Rendereren støtter allerede separate avsnitt gjennom `return block(items)`.

**Konfidens:** Svært høy. Lesbarhetseffekten er skjønn, men layoutmekanismen er direkte sporet.

### W12 — Malen prioriterer sanitet og referanser foran resten av historikken og språk

**Dokumentbevis:** Alle CV-er: «KURS / Sanitet nivå 2, 04.2014», deretter «REFERANSER / Oppgis ved forespørsel», deretter tidligere erfaring, tillitsverv og språk. I A ligger språk på side 3. Kandidatens utdanning har også lange faste fagdetaljer, mens økonomigraden allerede er tilstrekkelig kvalifikasjonsbevis.

**Direkte årsak:** `CV_BASELINE.md:197–215`; `template_map.json:98–109` fyller alltid OTHER_COURSES og references når de har innhold. I masterens dokumentflyt ligger kontrollene før `CV_PREVIOUS_EXPERIENCE`, `CV_TRUST` og `CV_LANGUAGES`. `Stage3:74–87` gjør dette statisk; forfatteren kan ikke realisere A-strategiens ønske om å nedprioritere sanitet. D `:307–317` gjør komplett kronologi og masterens referanseopplysning til standard.

**Mangel:** Manglende relevant prioritering av *presentasjon*, ikke manglende kandidatfakta. Statisk mal kan forbedres uten at modellen får skrive kronologi. Flytt språk og referanser, og skjul kurskontrollen i felles masteroppsett; ikke slett faktakilden eller eldre arbeidsforhold.

**Konfidens:** Svært høy for mekanisme, høy for lav verdi av akkurat sanitetskurset i denne rådgiverrollen. Kurs kan ha verdi for andre stillinger; kostnaden ved global skjuling må aksepteres eksplisitt i implementeringsvalget.

### W13 — Lang CV og brev får dårlig sideøkonomi; én konkret sammenbindingsfeil forsterker det

**Dokumentbevis:** A CV har tre sider; tredje side inneholder bare tidligere erfaring, tillitsverv og språk og mye ubrukt plass. AO brev har to sider, med slutt på et avsnitt og avslutning/signatur på en svært glissen side 2. A brev, B brev og C brev er én side. AO CV er to sider selv om den er betydelig lengre enn AX/AM i tekst.

**Direkte medvirkning:** `CV_MASTER.docx`, SDT-en `CV_OPTIONAL_PREVIOUS_EXPERIENCE`, prototypeavsnittet med `{{CV_PREVIOUS_EXPERIENCE_CONTENT}}`, har `w:keepNext`. `docxfill.py:225–233` kopierer avsnittsegenskapene til hver tidligere rolle. Hele rekken blir dermed bundet videre, også mot neste overskrift. Det er en konkret unødvendig pagineringsbinding; den eksakte sidegevinsten ved å fjerne den er ikke testet her. Brevets lengdeproblem følger i hovedsak av beholdt innhold, ikke en påvist tilsvarende keepNext-feil.

**Andre bidrag:** `settings.toml:76–79` har allerede myke mål; `render.py:291–305` lager sideadvarsel og `:702–707` kaller den ved PDF-kontroll. Varsel er ikke en redaksjonell reparasjon. Stage-3-teksten leveres og låses før denne sidestatusen finnes.

**Konfidens:** Høy for sideutfall og XML-kjeden; middels for hvor mye akkurat bindingen forklarer A sin ekstra side. Ikke innfør hardt sidekrav eller automatisk fontkrymping.

### W14 — Faglig substans forsvinner i enkelte korte CV-er

**Dokumentbevis:** E: «Deltok i et firepersonersteam» viser teamet, men utelater kandidatens forskningssyntese og økonomiske vurdering. D beholder mer av dette. AX: «Avviste direkte fordeling …» viser en konkret beslutning; AM: «Utformet en vektet modell …» er roligere, men noe mindre tydelig på aktiv faglig utfordring. AX utelater tverrorganisatorisk opplæring som AM har. Brevets innhold gjør noe av tapet mindre, men CV-en må kunne vurderes selvstendig.

**Bidrag som finnes:** D `:59–60`, `:140–153` prioriterer minste bevissett og støtter kutting; erfaringsoverskriving er full erstatning (`Stage3:80–85`, `package.schema.json:79`). **Mangel:** En konkret diskriminering mellom overflødig metodeinventar og personlig handling, mottaker og arbeidsendring. D `:481–486` forsøker allerede å bevare signal; ingen ny minimumslengde er nødvendig.

**Konfidens:** Høy for forskjell, middels for årsak. Kortere er verken automatisk bedre eller dårligere; erstatningens informasjonsverdi avgjør.

### W15 — Kildespråk og uklar norsk slipper gjennom

**Dokumentbevis:** AO CV: «det som omtales som en driftsrapport»; A/B: «revisjoner for umappede rader»; CX: «Hovedutvikler på baksiden»; flere: «onboarding», «WIP-design», «verdibegrunnelse», «paritetskontroll» og «atferdsbevarende». Ikke alle fagord er feil, men en leder må flere steder oversette teksten før relevansen blir klar. «Revisjoner» er særlig upresist når meningen er datakontroller, og «på baksiden» er et uheldig forsøk på å oversette backend.

**Bidrag som finnes:** WORK PRJ-02 har uavklart rapportnavn (`:985`) og PRJ-06 bruker «audits» (`:573`); mange råposter er engelske. K `:58–63` sier allerede at dokumentasjonsstemmen skal bort, men illustrerer dette med bruksstatus, ikke tekniske leveransebeskrivelser. **Mangel:** Situasjonsbestemt oversettelse til hva kontrollen eller leveransen gjør, samtidig som ukjent eksakt navn ikke gjøres til en generell usikkerhet om eget arbeid.

**Konfidens:** Høy for kildesmitte i AO, middels for ordvalgsvurdering. Bruk ikke en automatisk svarteliste; Power BI, SQL og presise tekniske begreper kan være riktig i CV.

### W16 — Åpning og avslutning bruker oppmerksomhet uten å øke vurderingsgrunnlaget

**Dokumentbevis:** A begynner med et langt sterilforsyningscase før yrkesanker er eksplisitt i brevet. AO bruker «Jeg søker stillingen …» og en lang innledning til to spørsmål, før to svært lange caseforklaringer. Avslutningene varierer over «Jeg tar gjerne en samtale …»; AO gjentar «gjerne» og snevrer intervjuet inn til én fordelingsmodell. B spør hvordan enheten tenker å måle verdi, som er faglig relevant, men svakere som siste bidragsmarkør.

**Bidrag som finnes:** Stemme `:133–143` avviser noen bestemte standardmønstre; brevets schema krever åpning og avslutning. D `:231–232` ber om konkret bidrag og naturlig invitasjon. **Mangel:** En positiv prior for at åpningen etablerer kandidat og begrunnet bidrag raskt, og at en kort ordinær avslutning er bedre enn tvunget særpreg. Ingen grunn til å forby «Jeg søker» eller «gjerne» som strenger.

**Konfidens:** Middels. Et case først kan fungere godt, særlig når pakken leses samlet. Her er problemet hvor lenge klassifiseringen utsettes og hvor mye avslutningen gjentar.

### W17 — Gevinstmetodikkens sterkeste resultat er lite konkretisert i faktagrunnlaget

**Dokumentbevis:** Nesten alle bruker «sykehusdekkende standard» og «om lag 2,5 år senere». Dette er god adopsjonsevidens, men kandidaten kan ikke vise hvilken konkret metodisk forbedring han selv utformet, hvilket ledelsesvalg den støttet, eller hvordan effekten ble fulgt opp. Brevene gjentar derfor generelle bidrag som «forskningssyntese» og «standardisering».

**Årsak som fravær:** WORK `:466`: «Exact name, dates, individual subcomponents, approval route, users/projects and measured effect remain unresolved»; `:986` gjentar dette. Tilsvarende mangler finnes for workshoputfall og rapportmottakere (`:979`, `:984–985`). Dette er det tydeligste ekte datagapet. PRJ-06 har en langt mer konkret dokumentert avveining (`:563–573`), og får derfor uforholdsmessig stor plass.

**Konfidens:** Høy. Bare kandidatbekreftet tilleggsinformasjon kan fylle hullet. Ikke legg inn oppdiktede prosesser, gevinstansvarlige, KPI-er, tidsbesparelser eller styringsgrupper for å gjøre historien hel.

### W18 — Små faste gjentakelser og toppsonens lange etiketter bruker unødvendig plass

**Dokumentbevis:** Alle brev har både «Stilling: Seniorrådgiver Digital Transformasjon» og «Søknad: Seniorrådgiver Digital Transformasjon». Flere CV-overskrifter gjentar samfunnsøkonom, nåværende rolle og tre fagområder i versaler. Dette er ikke en alvorlig feil alene, men forsterker en allerede tett toppsone.

**Direkte årsak:** `template_map.json`, `documents.letter.controls.APP_JOB_TITLE.count = 2`, og to tilsvarende SDT-er i `APPLICATION_MASTER.docx`. Headline er et fritt tekstfelt med upper-transform (`template_map.json:28–34`); ingen egen kortfattet rollefordeling mellom headline og profil er operasjonalisert utover generell yrkesankerregel.

**Konfidens:** Svært høy for tittelduplisering, middels for virkningen av headline-lengde. Lav prioritet sammenlignet med W01–W07.

## Del 2 — Optimaliseringsplanen

### Endringsrekkefølge og avgrensning

**Første leveranse:** O1–O4 nedenfor: oppgavedekning, konkret før-lås-redigering, statuspresisjon og mindre defensiv prosa. De endrer semantisk atferd uten nytt schema eller runtime-komponent. **Deretter:** O5–O7 for sosialt register, norsk og motivasjon; O8–O10 som en samlet maljustering. **Separat og bare med nye kandidatopplysninger:** O11. **Ikke lever:** forslagene i O12.

Ikke gjennomfør alle som en udifferensiert bunt dersom formålet også er å lære hvilken endring som virker. Første nye Avinor-generering bør sammenlignes med en uendret kontroll under samme faktagrunnlag, strategi og forfatterinnstilling. For å måle Stage-1-endringen må Stage 1 faktisk kjøres på nytt; en Stage-3-gren med gammel strategi kan bare vise effekten av sluttforfatterendringen. Dette er et manuelt engangsforsøk, ikke en ny testplattform, modellorkestrator eller runtime-rangering.

### O1 — La hovedargumentet dekke oppdraget, ikke erstatte det

**Endring 1:** `B/policy/writing/WRITING_DOCTRINE.md:149–153`, erstatt hele avsnittet som begynner «Begrunnelsen er rangering, ikke telling» med:

```text
Begrunnelsen er arbeidsgiverens beslutning, ikke telling. Et ekstra bevis har
verdi når det besvarer en vesentlig usikkerhet de øvrige bevisene lar stå åpen.
En svak gjentakelse kan svekke pakken; et kort, konkret bevis for en annen
avgjørende oppgave kan styrke den. Velg ikke flere case for å vise bredde, og
ikke færre case for å oppnå symmetri. Behold de erfaringene som samlet gjør
kandidatens relevante bidrag forståelig og troverdig.
```

Dette fjerner en ubegrunnet generell gjennomsnittspåstand uten å innføre den motsatte «mest mulig er best»-regelen. Resten av Single Backbone beholdes.

**Endring 2:** `B/policy/stages/stage1_decision_architecture.md:66–72`, erstatt de to avsnittene fra `material_requirements retains` til `actual employer task` med:

```text
material_requirements retains every material minimum, important and desired
requirement using the existing importance/relation/note/evidence_refs fields.
In note, distinguish the supported part of the requirement from the remaining
uncertainty. Preserve alternatives such as “lead or support”; do not turn them
into a requirement for formal leadership. Adjacent evidence is not fulfillment
of a minimum. objections handles real gaps without manufacturing new ones.

After choosing the carrying evidence, identify any important employer task
that this evidence still leaves unanswered. Use cv_direction.emphasis and
application_direction.structure_guidance to allocate the strongest available
evidence for that task to the CV, the letter or both with different functions.
If the sources contain no such evidence, retain the gap; do not fill it with
an adjective, stakeholder count or an invented action. The allocation is a
proposal to the final writer, not a coverage quota or a new schema field.
motivation_bridge connects the supported contribution to the actual employer
task and explains why that work is a credible next application of the experience.
```

**Endring 3:** Stage 3 `:54–55`, erstatt punkt 5 med:

```text
5. Read the pair against the vacancy's important tasks. Address material
   requirements and gaps truthfully. Where strong available evidence answers
   an important task still left unclear, make that contribution visible in
   the document best suited to it. Build specific motivation and remove
   repetition that adds neither a new function nor useful detail. Do not turn
   this reading into a requirement checklist in the employer-facing text.
```

**Mitigerer:** W01, W05, W14, deler av W17. Avinor-utslaget bør være et lesbart bidrag til arbeidsformer/fasilitering og leder-/mottakerarbeid ved siden av gevinst og levering. PRJ-02 eller PRJ-08 kan bære dette; ingen av dem er obligatorisk case i alle jobber.

**Avhengigheter og kostnad:** Bruker eksisterende `note`, `cv_direction.emphasis` og `application_direction.structure_guidance`; `strategy.schema.json:48–135` trenger ingen endring. Ny Stage-1-instruks krever ny fryst kontekst og ny strategi. Andre stillinger kan få noe mer relevant bredde og litt lengre brev. En svak fasiliteringssetning skal ikke få plass bare fordi annonsen nevner workshops. Risikoen motvirkes av fortsatt marginalverdivurdering.

**Neste output:** En leser kan peke på kandidatens faktiske samspill med andre, ikke bare «50 deltakere», og forklare hva dette sier om minst én oppgave utover modellering og koding. Ingen påstand om ledelse av 50 personer eller konsernportefølje skal oppstå.

### O2 — Gjør den siste substansielle redigeringen før innholdslåsen eksplisitt

**Sted:** `B/policy/stages/stage3_final_writer_review.md:65–68`. Dagens tekst begynner «A realization-only pass follows» og pålegger bevaring av viktig, vanskelig stoff. Erstatt blokken i sin helhet med:

```text
Before the realization-only pass, complete the substantive edit of the pair.
For each carrying experience, retain the personal action, the relevant change
in work or decision, its recipient where documented, and the source-supported
status. Keep technical detail when it explains a material decision or makes
the contribution credible; remove it when it merely inventories implementation.

Read the CV and letter together. The same case may appear in both, but the
letter must add judgment, a consequential choice or employer relevance rather
than repeat the CV's implementation sequence. Check the headline, profile,
transitions and summary sentences against the sources as carefully as case
sentences: they may not enlarge ownership, merge project histories or turn
an intended use into an observed result.

Make these evidence, allocation and deletion decisions now. Once the content
lock begins, preserve the chosen meaning and improve only its realization.
An important awkward sentence must be rewritten; a unique but low-value detail
need not survive merely because no other sentence says it.
```

**Mitigerer:** W04, W07, W10, W13, W14. Dette plasserer seleksjonsavgjørelsen før låsen, der eksisterende arkitektur allerede tillater den. Selve `Final polish — content lock` på `:133–171` forblir uendret.

**Avhengigheter og kostnad:** D `Erstatnings- og komprimeringsrekkefølge` og V `Rangorden` fortsetter å gjelde. Ingen ny pass-artifact, modellkall eller logging. Forfatteren bruker litt mer oppmerksomhet på paret. Et detaljrikt teknisk CV-signal kan forsvinne; det er riktig bare når det ikke endrer arbeidsgiverens relevante vurdering. For data science-roller vil eksempelvis tidsbasert validering ofte overleve, mens den kan tas ut her.

**Neste output:** Budsjettcaset skal forklare integrasjonen av bemanningsdata og den faktisk leverte bruken minst like tydelig som kontrollmetoden. A sin DAX-andel og B sine 78 navn skal ikke returnere uten en konkret stillingsgrunn. Samme refaktoreringsoppskrift skal ikke stå fullstendig både i CV og brev.

### O3 — Skill ukjent tilstand fra dokumentert fravær

**Sted:** `B/policy/writing/PERSUASION_CALIBRATION.md`, etter `PROOF_FUNCTION_LIFECYCLE:118`, før neste domenetittel. Dagens domene skiller tilstander, men har ingen eksplisitt epistemisk negativregel. Tilføy denne teksten:

```text
Ukjent status er ikke et negativt historisk faktum. «Innføring er ikke
dokumentert» gir ikke grunnlag for «løsningen ble ikke innført». Bruk det
kilden faktisk bekrefter, for eksempel utforming, ferdigstilling eller
overlevering, og avgrens en eventuell videre resultatpåstand. Skriv bare at
noe ikke skjedde når kilden fastslår dette. Hold uavklart bruk, eierskap og
effekt atskilt fra leveransens dokumenterte tilstand.

Når kilden beskriver flere leveranser eller årganger, skal en statuspåstand
gjelde riktig leveranse. Felles verktøynavn gjør ikke to moderniseringsrunder
til én uendret versjon.
```

**Mitigerer:** W02 og versjonsdelen av W07. Forskjellen mellom «ferdigstilt og overlevert» og «organisatorisk i bruk» bevares.

**Avhengigheter og kostnad:** Kalibreringsfilen er uttrykkelig bruker-eid (`:11`, `:83–84`). Dette er et skrevet forslag til brukerens godkjenning, ikke allerede godkjent varig kalibrering. Ved implementering må endringen behandles som en eksplisitt kalibreringsendring. Ingen fakta omskrives; WORK `:110` støtter prinsippet allerede. Kan gi noen formuleringer med tydeligere usikkerhet, men skal vanligvis gjøre teksten enklere ved å stoppe ved den støttede leveransen.

**Neste output:** Ingen «ikke innført» når den fryste kilden bare sier uavklart. 2026/2027 beskrives som bruk i to budsjettprosesser uten påstand om samme uendrede versjon. Eldre run skal ikke tilføres 2026-09-06-bekreftelser i ettertid.

### O4 — Avgrens påstanden først; gi ikke fraværet et eget avsnitt

**Sted:** `B/policy/writing/PERSUASION_CALIBRATION.md:125–136`, erstatt hele den nummererte listen og avsluttende setning med:

```text
1. Antyd aldri at et uoppfylt minstekrav er oppfylt. Bevar også arbeidsgiverens
   alternative innganger; et ønske om å lede eller støtte er ikke et krav om
   formelt ledermandat.
2. Beskriv først den nærliggende erfaringen positivt og presist: hva kandidaten
   gjorde, med hvem, innenfor hvilket omfang og med hvilken dokumentert status.
3. Bruk arbeidsgiverens substansielle vokabular bare der det er dekket. Et
   fremtidig bidrag skal fremstå som en anvendelse av erfaring, ikke som et
   allerede oppnådd mandat eller resultat.
4. Legg bare til et eksplisitt forbehold i arbeidsgiverteksten når den presise
   positive formuleringen ellers fortsatt ville villede vesentlig. Et kjent
   fravær av måling eller formell myndighet krever ikke en egen setning når
   teksten allerede bare hevder leveranse, bruk eller et avgrenset bidrag.
5. Hold relevante uløste gap synlige i review.json for mennesket. Review kan
   ikke legitimere en kjent udokumentert påstand i arbeidsgiverteksten.
6. Et kjent gap alene tvinger ikke CHECK når ingen faktabekreftelse eller lokal
   reparasjon gjenstår.

Den positive overføringsbroen beskriver erfaringen kandidaten faktisk har.
Den skal verken skjule et vesentlig gap eller presentere fraværet som hovedsak.
```

**Mitigerer:** W03, delvis W01/W16. Konkret Avinor-konsekvens: «Var … eneste kodende utvikler … innenfor en interessentprosess» avgrenser eierskap; «verktøyet er i … bruk» hevder ikke målt besparelse. Da trengs normalt ikke et separat avsnitt om manglende programmyndighet eller tall.

**Avhengigheter og kostnad:** Samme kalibreringseierskap som O3. Stage 3 må bruke dette i punkt 5–7 før låsen, ikke slette materielle forbehold under sluttpussen. En forfatter kan overforenkle; derfor beholdes testen om vesentlig villedning. Ingen automatisk fjerning av setninger med «ikke».

**Neste output:** AX/AMs generelle mandatforbehold forsvinner eller erstattes av konkret workshop-/leveransearbeid, samtidig som verken profil eller avslutning antyder konsernmyndighet. A/AO beholder det dokumenterte resultatet uten dobbelt negativt etterskrift.

### O5 — Velg selve kompromisset fremfor historien om hvem som begrenset kandidaten

**Sted:** `B/policy/writing/WRITING_DOCTRINE.md`, etter `Integrert bevisenhet:193`. Tilføy:

```text
En dokumentert uenighet er verdifull når den forklarer en viktig avveining,
beslutning eller samarbeidsmåte. Når samme poeng fremgår av rammen kandidaten
arbeidet innenfor og handlingen han valgte, bruk den kortere fremstillingen.
Ikke gjør hvem som avslo kandidatens foretrukne løsning til et hovedmotiv uten
at dette gir arbeidsgiveren nødvendig informasjon. Bevar reell attribusjon,
og ikke omskriv et pålagt kompromiss til kandidatens opprinnelige anbefaling.

Et enkelt case kan begrunne en avgrenset faglig vurdering. Det gir ikke i seg
selv grunnlag for en generell regel om hva som alltid skaper verdi, hva andre
gjør feil, eller hvilken innsats som er den viktigste. Avgrens regelen til det
erfaringen faktisk viser, eller la handlingen stå uten en læresetning.
```

**Mitigerer:** W06, W08. Dagens faktasetning i WORK `:396` beholdes: den er sann og kan være relevant i andre sammenhenger. PF-06 skal heller ikke slettes; det er ikke bevist at den skaper problemet.

**Avhengigheter og kostnad:** D eier argumentvalg; V eier uttrykk. Plasseringen unngår å gi stemmepolicyen ny faktavalgmyndighet. Noe farge og intervjuforberedende detalj forsvinner. Til gjengjeld blir avveiningen mindre personkonfronterende. Faglig utfordring skal fortsatt kunne være tydelig, særlig proxy-avvisningen.

**Neste output:** «Endringsrammen krevde …» kan erstatte flere setninger om innføringsleder, uten at teksten hevder kandidaten valgte rammen selv. B sin maksime om rapporter kommer ikke tilbake. Proxy-valget beholder årsaken: direkte data bar ikke fordelingen.

### O6 — Gjør fagspråket lesbart uten å tømme det

**Sted 1:** `B/authorities/Work_experience.md:945–949`, kun den redaksjonelle regelen, erstatt hele seksjonen med:

```text
### 9.4 Regel for CV-punkter

Dette er rådgivende utvalgsmetadata, ikke kandidatfakta. La et CV-punkt vise
personlig arbeid, relevant omfang og en dokumentert leveranse eller tilstand.
Ta med metode eller kontroll når den forklarer en viktig vurdering eller gjør
bidraget troverdig. Ikke fyll alle ledd i en fast problem–handling–metode–resultat-
formel. Velg detaljer etter arbeidsgiverens oppgave og bevar teamgrensen.
Fravær av målt effekt skal ikke erstattes med en oppfunnet effekt eller en
udokumentert påstand om redusert risiko.
```

**Sted 2:** `B/policy/writing/FORFATTERSTEMME.md`, under `Setningsarkitektur`, etter `:89`, tilføy:

```text
- Gjør faguttrykk forståelige gjennom handlingen de beskriver. Behold presise
  verktøynavn og fagord når mottakeren trenger dem; forklar eller erstatt intern
  metodejargong når den bare krever oversettelsesarbeid. En kontroll for rader
  som mangler kobling skal ikke bli en «revisjon» bare fordi kilden sier audit.
- Ukjent eksakt navn på et dokument eller en enhet gjør ikke dokumentert eget
  arbeid usikkert. Bruk en korrekt generell betegnelse og et presist arbeidsverb
  fremfor formuleringer som «det som omtales som». Ikke finn på det manglende navnet.
```

**Mitigerer:** W04, W14, W15. Den første endringen fjerner en konkurrerende obligatorisk formel i en faktamyndighet uten å endre fakta. Den andre retter et observert oversettelsesproblem.

**Avhengigheter og kostnad:** Endring i WORK krever vanlig regenerering av evidence index og baseline-kildelenker fordi filhash endres; bruk eksisterende vedlikeholdsrute i RUNBOOK, ikke manuell redigering av genererte hasher. Selv en metadataendring påvirker fryste bindinger. Kan derfor utsettes til neste ordinære kildevedlikehold, mens stemmetillegget leveres først. Ingen arbeidspåstand blir nye fakta. Litt teknisk presisjon kan gå tapt hvis regelen brukes mekanisk; «paritetskontroll» er tillatt når relevant og forståelig.

**Neste output:** «kontroller for umappede rader» eller en tilsvarende forståelig formulering, ikke «revisjoner». Ingen «hovedutvikler på baksiden». E sin metodebullet får personlig bidrag der dette har beslutningsverdi; ingen nødvendig økning i samlet lengde.

### O7 — Bytt absolutt unikhet mot konkret rollepassform

**Sted 1:** `B/policy/writing/WRITING_DOCTRINE.md:431–455`, erstatt hele `Arbeidsgiverbyttetesten` med:

```text
# Arbeidsgiverbyttetesten

Bytt arbeidsgiver og rolle mentalt. Undersøk om teksten faktisk er valgt for
oppgavene i denne annonsen, eller bare har fått nytt navn og ny tittel.

En pakke er for generell når yrkesanker, hovedbevis, motivasjon og ønsket
bidrag kunne vært valgt uten å lese stillingen. Reparer med en konkret
oppgave, en relevant beslutningssituasjon og støttet erfaring som gjør
bidraget troverdig. Samme erfaring kan være riktig for flere arbeidsgivere
med tilsvarende behov; absolutt unikhet er ikke et mål.

Skill den overførbare arbeidsbetingelsen fra sektorens særlige oppgaver.
Erfaring fra én samfunnskritisk virksomhet etablerer ikke kompetanse eller
myndighet i en annen. Beskriv forbindelsen uten å gjøre virksomhetene like.
Manglende domeneerfaring er ikke bevis på manglende interesse for domenet.

Motivasjonen skal vise hvorfor denne oppgaven er en meningsfull neste bruk
av kandidatens erfaring. Ikke konstruer en privat interesse eller avvisning,
og ikke bruk virksomhetstall som erstatning for en relevant oppgavekobling.
Testen gjelder både CV-toppen og søknaden, med respekt for dokumentenes ulike
funksjoner og uten krav om at arbeidsgivernavnet må stå i CV-profilen.
```

**Sted 2:** `B/policy/writing/FORFATTERSTEMME.md:133–134`, erstatt det første mønstereksempelet med:

```text
1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …`
   som lang standardavslutning. Avslutt kort og naturlig. Et konkret bidrag
   som allerede er klart, trenger ikke gjentas for å gjøre siste setning unik.
```

**Mitigerer:** W09, W16. Avinor-brevet bør ha en konkret kobling til oppbygging av enheten, prioritering og gjennomføring. Det trenger ikke en usann privat luftfartsinteresse eller en avvisning av luftfart.

**Avhengigheter og kostnad:** Stage 1 og 3 ruter allerede til D; Stage 3 til V. Ingen promptduplisering. Kan redusere særpreg i åpning/avslutning, men styrker substansiell spesifisitet. En ren annonseparafrase består fortsatt ikke.

**Neste output:** Ingen «ikke luftfarten i seg selv». Ingen påstand om at OUS og Avinor har samme problem. Kort avslutning uten nytt miniforedrag; kandidat og bidrag kan identifiseres tidlig i brevet, selv om et godt case fortsatt kan komme først.

### O8 — Bruk den eksisterende avsnittsrenderingen for kompetanser

**Sted:** `B/templates/template_map.json:48–55`. Erstatt kontrollobjektet i sin helhet med:

```json
"CV_CORE_COMPETENCE": {
  "kind": "block",
  "count": 1,
  "source": "package.cv.competencies",
  "required": true
}
```

**Tilpass masteren samtidig:** I `B/templates/CV_MASTER.docx`, SDT `CV_CORE_COMPETENCE`, behold ett prototypeavsnitt. Fjern fet direkteformatering fra tekstrunnen, behold masterens eksisterende lesbare skriftstørrelse, sett `w:keepLines`, ikke `w:keepNext`, `w:spacing before="0" after="28" line="250" lineRule="auto"`. Hvert kompetanseelement blir ett eget normalt avsnitt. Ikke legg inn et nytt obligatorisk SDT eller en ny tittel; fravær av «KJERNEOMRÅDER» foran første linje er tilsiktet. Profiloverskriften og etterfølgende Yrkeserfaring beholder hierarkiet.

**Mitigerer:** W11. `render.py:157` støtter dette allerede. Ingen Python-endring er nødvendig.

**Avhengigheter og kostnad:** Hver kompetanse får egen linje; en lang liste kan bruke mer høyde enn midtpunktavsnittet. Derfor skal dette ses sammen med O2 og på både AX-lengde og A-lengde før det velges. Ikke øk sidebudsjett eller krymp font for å redde en katalog. Kompetanseantall forblir mykt; schemaet endres ikke. Tabell-/tokolonnekompetanser foreslås ikke fordi de ville tilføre mer layoutkompleksitet.

**Neste output:** Kompetansene er individuelt skannbare, og normalvekten lar faktiske erfaringer dominere. Ingen rå JSON-liste, duplisert prefix eller tom placeholder. Ny visuell kontroll må vise om netto høyde er akseptabel; denne endringens eksakte sideeffekt er ennå ikke verifisert.

### O9 — Fjern utilsiktet sammenbinding og omprioriter CV-ens statiske avslutning

**Sted 1:** `B/templates/CV_MASTER.docx`, i SDT-en `CV_OPTIONAL_PREVIOUS_EXPERIENCE`, prototypeavsnittet med `{{CV_PREVIOUS_EXPERIENCE_CONTENT}}`: fjern `<w:keepNext/>`, sett `<w:keepLines/>`. Behold tabulatorer, datoer, font og øvrige avstander. Nåværende «hold med neste» blir kopiert til alle eldre roller av `docxfill.py:231`. Erstatningen holder én rolle samlet, men binder ikke hele historikken til neste seksjon.

**Sted 2:** Flytt de komplette eksisterende SDT-ene i masterens `word/document.xml`, identifisert ved følgende faktiske tagger, slik at rekkefølgen etter utdanning blir:

```text
CV_OPTIONAL_PREVIOUS_EXPERIENCE
CV_OPTIONAL_TRUST
CV_OPTIONAL_LANGUAGES
CV_SUPPORT_SECTION_1
CV_SUPPORT_SECTION_2
CV_SUPPORT_SECTION_3
```

Flytt hver kontroll samlet med både heading- og content-avsnitt; behold nesting, tagger og placeholders uendret. Dette flytter referanseopplysningen til slutt, etter den faktiske historikken og språk.

**Sted 3:** `template_map.json:98–103`, erstatt kursobjektet med:

```json
"CV_SUPPORT_SECTION_1": {
  "kind": "block",
  "count": 1,
  "source": "none",
  "required": false
}
```

Dette skjuler den nåværende kursseksjonen i den felles CV-malen. Kursfakta, baseline-elementet og alle arbeidsforhold beholdes. En fremtidig eksplisitt kilde-/malvedlikeholdsoppgave kan prioritere kurset tilbake dersom det faktisk blir relevant.

**Mitigerer:** W12, W13. Det er ikke garantert at A blir to sider; først bør unødvendig innhold fjernes etter O2. Sidebrudd skal deretter følge innhold, ikke en kjede av keepNext.

**Avhengigheter og kostnad:** Ingen endring av `always_include`, statisk identitet, utdanningsrekkefølge eller språkfakta. Ingen modellstyrt seksjonsvelger. Global skjuling av kurs mister et svakt sikkerhets-/ansvarssignal i andre roller; derfor kommer den etter de semantiske tiltakene, og kan droppes hvis brukeren ønsker kurset fast. Flytting av SDT-er krever eksisterende mal-/parsebarhetskontroll og visuell åpning på en kort og en lang CV. Referanser beholdes fordi doktrinen krever opplysningen når masteren bruker den.

**Neste output:** Språk og full arbeidskronologi kommer før referanser. Sanitetskurset forsvinner uten at en tom KURS-overskrift blir igjen. Tidligere roller kan fordeles over sider, men en enkelt rolles linjer brytes ikke unødvendig. Ingen påstand om to sider før faktisk render.

### O10 — Fjern den ene doble brevtittelen og avkort toppetiketten semantisk

**Sted 1:** `B/templates/APPLICATION_MASTER.docx`, fjern referanseblokkens avsnitt `Stilling: {{APP_JOB_TITLE}}` med dets inline-SDT. Behold dokumentets emnelinje `Søknad: {{APP_JOB_TITLE}}`, mottaker, enhet, dato og optional reference. Det tomme cellearealet må kollapse naturlig; ikke behold en tom rad med fast høyde.

**Sted 2:** `B/templates/template_map.json`, erstatt `APP_JOB_TITLE` med:

```json
"APP_JOB_TITLE": {
  "kind": "inline",
  "count": 1,
  "source": "job.title",
  "required": true,
  "note": "Filled once in the letter subject line."
}
```

Oppdater samme fils toppnivå-`note` fra påstanden om 7 kontroller / 6 unike / to APP_JOB_TITLE til følgende fulltekst:

```text
The ONE canonical package-to-template map (Contract 13.3). Code, documentation
and tests consume this file and no other. Duplicate, missing or unknown controls
fail preflight rather than being ignored (Spec 16.3). CV_MASTER.docx carries 17
non-data-bound SDTs, one per tag. APPLICATION_MASTER.docx carries 6, one per tag.
Neither master uses w:dataBinding or docPartObj.
```

**Sted 3:** D `Yrkesanker`, etter `:100`, tilføy:

```text
La CV-overskriften navngi yrkesankeret og den viktigste relevante funksjonen.
Profilen kan forklare nåværende rolle og hovedbevis. Ikke pakk tittel, grad,
hele fagbredden og alle hovedleveransene inn i samme overskrift.
```

**Mitigerer:** W18 og litt W16. Ikke bygg en tredje overskriftsflate.

**Avhengigheter og kostnad:** `docxfill.require_template_contract` sammenligner faktiske antall; map og master må endres sammen. `docxfill.py` sin innledende historiske dokumentasjon nevner gammel beholdning, men er ikke runtime-autoritet; eventuell oppdatering av den er dokumentasjonsvedlikehold, ikke nødvendig ny logikk. Eksisterende tester som uttrykkelig forventer to forekomster, må tilpasses den nye faktiske kontrakten hvis de finnes; ikke legg til et nytt testapparat. Gevinsten er liten og dette skal ikke forsinke O1–O4.

**Neste output:** Stillingen er korrekt i én emnelinje, ingen tom rad, mottaker/dato/referanse fungerer fortsatt. CV-overskriften kan leses raskt uten å konkurrere med profilen.

### O11 — Fyll bare de kildehullene som kan endre kandidatens argument

**Prioriterte innhentinger:**

1. PRJ-04: Én konkret metodisk forbedring Vegard selv bidro til, hva som var utilstrekkelig før, og hva teamet faktisk endret. Deretter hvem som godkjente standarden og hvilken observerbar bruk som ligger bak varighetsopplysningen.
2. PRJ-08 eller PRJ-02: Ett konkret workshop-/arbeidsmøte, mottakere på forsvarlig identifikasjonsnivå, hva Vegard gjorde, og hvilket dokumentert neste steg møtet førte til. Ikke et krav om å fortelle en konflikt eller dramatisere motstand.
3. PRJ-03: Bare dersom det finnes reelle opplysninger: målt før/etter, observasjonsperiode og hva målet faktisk omfatter. Intet krav om prosentgevinst for å gjøre caset gyldig.

**Eksakte nåværende steder:** WORK `:466`, `:659`, `:984–991`. **Erstatningsatferd, i fullstendig form:**

```text
Behold eksisterende kandidatfakta og claim-tak uendret inntil Vegard bekrefter
en konkret tilleggsopplysning. Når en opplysning er bekreftet, før den i riktig
prosjektpost med personlig bidrag, teamramme, dato eller observasjonsperiode,
mottaker og dokumentert tilstand. Fjern bare den delen av uavklartregisteret
som bekreftelsen faktisk avklarer. Oppdater den tilhørende digest-raden og
claim-atomene uten å utvide andre påstander. Regenerer evidence index og
baseline-kildelenker gjennom eksisterende vedlikeholdsrute, og bruk det nye
grunnlaget først i en ny fryst run.
```

Ingen ferdig faktasetning kan skrives nå uten å finne på innhold. Dette er den eneste bevisst betingede delen av planen, og den skal ikke blokke de øvrige endringene.

**Mitigerer:** W17, potensielt W01/W05. **Kostnad:** Kandidatens tid; nye opplysninger kan være mindre sterke enn forventet. Hvis svarene ikke finnes, behold eksisterende ærlige bidrag og dropp datainnhentingen. **Neste output:** Minst ett genuint nytt konkret bidrag, ikke bare mer presis innpakning av samme «forskningssyntese».

### O12 — Dette ville jeg ikke implementert

| Fristende tiltak | Beslutning og konkret grunn |
|---|---|
| Endre `settings.toml` til én «vinner-modell» | Ikke nå. Filen beskriver roller/operatørmapping, ikke kvalitetsscorer eller automatisk kall. Enkeltutfall og filnavn etablerer ingen forventet modellrangering. |
| Nye numeriske vekter for gevinst, språk, personlighet i runtime | Nei. Det finnes ingen runtime kvalitetsdommer som skal vektes om. Rangeringen i en menneskelig evalueringsrapport er noe annet enn et semantisk runtime-scorefelt. |
| Skru av personlighet eller legge til flere fasetter | Nei. Null valgte fasetter er allerede lovlig; A-familiens to identiske fasetter gir svært ulik tekst. Først rett seleksjon og realisering. |
| Hard grense på ord, bullets, case eller én/to sider | Nei. Ville kunne fjerne nettopp samarbeid og faglig vurdering. DEC-24/33 skiller redaksjonelt mål fra mekanisk feil. |
| Automatisk korting, fontkrymping eller ny layoutmotor | Nei. Den observerte feilen kan håndteres med innholdsprioritering og eksisterende master-/map-egenskaper. |
| Endre `package.schema.json` til én obligatorisk caseformel eller kravmatrix | Nei. De eksisterende feltene kan bære bedre tekst; en ny fast form kan øke JSON-rytme og oppdiktede forbindelsesledd. |
| Automatisk krav-/påstandsdommer, ny reviewer-agent eller ekstra modellrunde | Nei. Ikke nødvendig for denne endringen, og i konflikt med skillet mellom mekanikk og semantisk vurdering. |
| Full omskriving av faktamyndighetene eller personprofilen | Nei. Kildene har gode, nødvendige grenser og mye uutnyttet evidens. W17 krever nye fakta, ikke mer prosa. |
| Fjerne alle tekniske begreper, alle tall eller alle forbehold | Nei. Proxy-valget, kodeansvaret, faktisk bruk, teamet og nødvendige grenser er noe av det som gjør søkeren troverdig. |
| Gjenbruke en «Avinor-vinnertekst» som universelt eksempel i prompten | Nei. Ville sementere tre bestemte case og sektoranalogien i andre stillinger. Implementer beslutningsreglene, ikke et fasitsvar. |

## Samlet avhengighets- og gjennomføringsvurdering

`prompts/STAGE1_PROMPT.md:35–43` og `STAGE3_PROMPT.md:25–33` peker allerede på fryste instrukser. De skal ikke fylles med kopier av de nye reglene. `runtime/jobbsok/cli.py:980–1064` gir Stage 1 full kildeadgang og Stage 3 digester/selektiv henting uten lukket univers; `:1211–1243` sender de seks destillerte personlighetfeltene videre. Ingen dokumentert feil her krever ny hentemotor. `schemas/strategy.schema.json` har allerede materialkrav, notat, evidensrolle og dokumentretning. `schemas/package.schema.json` har allerede den nødvendige elastisiteten.

De foreslåtte endringene har derfor **ingen ny runtime-kode**, ingen schemautvidelse, ingen automatisk modellrouting og ingen nye tester eller vedvarende kontrollartefakter. Malendringene bruker allerede implementert oppførsel. Ved implementering skal eksisterende relevante schema-/mal-/renderkontroller kjøres, og faktiske dokumenter åpnes visuelt. Dette er verifikasjon av endringen, ikke et nytt produksjonssystem. Kildeendringer krever eksisterende indeks-/baselinevedlikehold. Fryste run endres ikke på stedet; ny eller egnet child-run må bruke den nye konteksten.

Suksess er at neste pakke gjør **økonomisk skjønn, gjennomført arbeidsendring og konkret samspill med andre** lettere å se, med færre tekniske gjentakelser og færre unødvendige negative selvbeskrivelser. Intervjuutfall er ikke målt i dette korpuset. Ingen tallfestet økning i intervjusannsynlighet kan utledes av forslagene.
