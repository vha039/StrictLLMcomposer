# Jobbsøk_26 — dyp evolusjonsaudit fra verifisert P0.7 til siste rekonstruerbare P0.9-prelock-tilstand

## Status for denne rapporten

Denne rapporten bruker den faktisk opplastede `Jobbsok_26_P0.7_Release(1).zip` som **eksekverbar baseline**, og analyserer deretter bare materialet som tidligere ble identifisert som P0.8 eller nyere. Formålet er ikke å velge den peneste versjonsfortellingen, men å rekonstruere den høyeste informasjonsverdien på hvert granulære designpunkt.

Følgende merge-regel er brukt gjennom hele rapporten:

1. **Nyere eksplisitte brukerbeslutninger/korrigeringer vinner.**
2. **Faktisk implementasjon/testbevis vinner over beskrivelser av hva som skal være implementert.**
3. **P0.8.0 FINAL_NORMATIVE_SPECIFICATION vinner over alle tidligere P0.8-idéer og mellomutkast.**
4. Senere P0.8.1-reviewmateriale får bare overstyre P0.8 i denne *utledede* måltilstanden der det eksplisitt korrigerer, spesifiserer eller tetter et konkret kontrakthull. Historisk sett ble P0.8.1 aldri adoptert som normativ release; dette skillet beholdes.
5. P0.9-brainstorming/review får **ikke** automatisk overstyre P0.8/P0.8.1. Bare eksplisitte senere brukerbeslutninger, faktisk ny ekstern evidens eller direkte presiseringer brukes som oppdateringer. Uvalgte P0.9-alternativer beholdes som åpne forklaringsvariabler.
6. Ekstern research kan oppdatere **faktiske miljø-/plattformantakelser**, men ikke gjøre produktpolitikk eller assistentforslag normative.
7. `Personality.md` og relaterte artefakter er fortolkningskontekst, aldri ny faktamyndighet om kandidatens arbeidshistorikk/prestasjoner.

Dette gir to samtidige sannheter som ikke må blandes:

- **Siste faktisk implementerte release:** P0.7.
- **Siste formelt adopterte komplette arkitekturspesifikasjon:** P0.8.0.
- **Siste mest utviklede kontrakthardening:** P0.8.1-reviewet, men eksplisitt `NON_NORMATIVE_UNTIL_ADOPTED`.
- **Siste prosjektfase / designfront:** P0.9 pre-architecture / pre-lock, med mange nye brukerbeslutninger og evidens, men **uten endelig valgt P0.9-arkitektur eller implementasjon**.

Rapportens «endelige oppsett» er derfor en **utledet latest-state target specification**, ikke en påstått historisk release. Den er eksplisitt merket med autoritetsstatus på punkter som fortsatt er åpne.

---

# 1. Executive verdict

## 1.1 Den viktigste konklusjonen

Jobbsøk_26 har ikke utviklet seg som en lineær serie der P0.8 og P0.9 erstattet alt før seg. Det er mer presist å se utviklingen som fire lag:

```text
P0.7
= faktisk bygget, kjørbar og mekanisk verifisert kapitalbase

P0.8.0
= normativ redesign av produkt- og produksjonsarkitekturen
  som aldri ble implementert

P0.8.1-review
= svært detaljert kontrakthardening av P0.8 før implementasjon,
  men aldri formelt adoptert

P0.9 pre-lock
= ny design-/evidensfase som åpner enkelte produktgrenser,
  runtimevalg og personaliseringsmekanismer på nytt,
  men som eksplisitt stopper før final architecture selection
```

Dette betyr at det **ikke finnes én historisk fil som alene representerer «siste versjon»**. Den mest komplette nåtilstanden må utledes ved å beholde den beste gjeldende informasjonen per designpunkt.

## 1.2 Hva som faktisk er robust på tvers av hele evolusjonen

Følgende har overlevd fra P0.7 gjennom P0.8/P0.8.1 og inn i P0.9 uten reell senere forkastelse:

- tre eksplisitte kandidatmyndigheter som faktakilder;
- avledet CV-baseline som eier statisk kronologi;
- sterke formuleringer tillatt innen dokumenterbar/intervjuforsvarlig sannhet;
- menneskelig godkjente stillinger inn — ingen automatisk GO/NO-GO-router;
- ett jobbobjekt ferdigstilles/persisteres før neste;
- modeller eier semantikk, kode eier deterministisk mekanikk;
- manuelle, separate modellstages fremfor API-orchestrator;
- ingen automatisk innsending/kontakt/publisering;
- mennesket beholder siste semantiske og irreversible myndighet;
- dynamiske CV-soner fremfor å regenerere hele kronologien;
- profesjonelle Word-mastere som designkapital, men bare etter eksplisitt kontroll/adaptasjon;
- partial success — én dårlig jobb skal ikke ødelegge resten;
- den dyreste/kraftigste sluttskriveren må kunne rette tidligere strategi, ikke bare «godkjenne» den;
- ingen vector DB, semantic cache, multi-agent-debatt, auto-router, hidden retry engine, LLM-as-judge-standardstage eller enterprise-stateplattform uten observert behov.

Dette er rammeverkets reelle ryggrad.

## 1.3 Hva som faktisk endret seg

Den største endringen var **ikke** 4 stages → 3 stages. Den var et skifte i hva systemet optimaliserer.

P0.7 var i praksis fortsatt sterkt preget av:

```text
bevar stageintegritet
+ fullfør alle jobs korrekt
+ hard gate på mange mekaniske kvalitetsproxyer
+ lås tidligere strategi/evidens ganske hardt
```

Etter den kritiske P0.7-auditen korrigerte brukeren dette eksplisitt til:

```text
beskytt sannhet hardt
+ maksimer kvaliteten på den sterke majoriteten
+ aksepter en svak hale
+ gjør halen billig å identifisere/rerunne separat
+ ikke la QA-/uniformitetsinfrastruktur konkurrere med faktisk søknadskvalitet
```

Dette blir `Q_happy`-doktrinen og er den egentlige fødselen til P0.8.

## 1.4 Den siste nåværende prioriteringsfunksjonen

Den historiske P0.8-kostheuristikken var:

```text
Human Effort > Human Complexity > LLM Complexity > LLM Effort
```

Senere P0.9-brukersvar gir en bredere, nyere og autoritativ beslutningsrangering for **truth-safe alternativer**:

```text
1. sluttproduktkvalitet
2. menneskelig innsats
3. implementeringshastighet/enkelhet
4. modellkost
5. reversibilitet
```

Den eldre kostheuristikken er fortsatt nyttig *innenfor* alternativer med omtrent samme produktkvalitet, men er ikke lenger toppnivåmålet.

## 1.5 Hva «siste mest utviklede versjon» derfor betyr

Den ærlige betegnelsen er:

> **P0.9-prelock derived target:** P0.8s trestegs Selective Quality-kjerne + de lavrisiko kontrakthardeningene fra P0.8.1 + senere eksplisitte P0.9-brukerbeslutninger + verifiserte miljø-/researchkorreksjoner, mens uavgjorte P0.9-designforker fortsatt er eksplisitt åpne.

Det er **ikke** korrekt å kalle dette en ferdig P0.9-release.

---

# 2. Korpus, autoritet og dokumentroller

## 2.1 Baseline

`Jobbsok_26_P0.7_Release(1).zip` er behandlet som primær kilde for:

- hva som faktisk ble implementert;
- aktive scripts og runtimekontrakter;
- package schema;
- stageinstruksjoner;
- templates;
- test-/renderbevis;
- konkrete migrerbare assets.

Jeg kjørte testsuiten på nytt:

```text
Ran:       34
PASS:      32
SKIP:       2  (PowerShell runtime unavailable)
FAIL:       0
```

De fem dokumenterte SHA-256-hashene for kandidatmyndigheter og Word-mastere matcher også releaserapporten eksakt.

## 2.2 P0.8+ dokumentfamilier

| Dokument/familie | Rolle | Autoritet i denne rekonstruksjonen |
|---|---|---|
| `Canonical_Conversation_KB_improvement_and_brainstorming_model_chat.md` | P0.7 audit + `Q_happy`-målskifte + tidlig P0.8-hypotese | Høy for historisk overgang; forslag er ikke automatisk normative |
| `Jobbsøk_26 Intensjonsprofil.pdf` | produktintensjon, tie-breakers, KISS/sannhet/persuasion | Høy som intensjonsprofil, ikke schema/runtime |
| `Jobbsok_26_LLM_Context_Reference.md` | komprimert maskinlesbar intensjonsprofil | Høy som beslutningskompass |
| `Jobbsok_26_P0.7-P0.8_Selective_Quality_Redesign_integration_summary.md` | chatrekonstruksjon frem til før endelig P0.8 | Historisk/proveniens, underordnet primærspesifikasjon |
| `Canonical_Conversation_KB_external_review_model.md` | sterk ekstern P0.8-konvergens før final spec | Mellomprodukt; senere supersedert der final spec avviker |
| **P0.8 final spec** | `FINAL_NORMATIVE_SPECIFICATION`, v0.8.0 | Høyeste P0.8-autoritet |
| `Jobbsok_26_P0.7_to_P0.8_architecture_redesign_integration_summary.md` | rekonstruksjon som inkluderer faktisk finalisering av P0.8.0 | Proveniens/bekreftelse |
| `jobbsok_26_overordnet_systemanalyse.html` | post-P0.8 systemreview; «implement now» | Sterk analyse, ikke normativ |
| Claude/Gemini P0.8 reviews | uavhengige kontrakt-/implementeringskritikker | Evidens/forslag |
| `P0.8_addendum_cross_model_consolidation.md` | adjudikering av reviewkonflikter | Senere reviewsignal; ikke i seg selv release |
| `deep-research-report (14).md` | ekstern evidensrevisjon 5. august | Factual evidence, ikke produktpolicy |
| `P0.8_consolidated_preimplementation_review.md` | P0.8.1 contract-hardening | Svært høy utviklingsverdi, men eksplisitt non-normative |
| `Brainstorm_Brief.md` | bred P0.9-option space | Eksplorativ, ikke normativ |
| `brainstorm_review.md` | strukturering/pruning: DC/N/K/E | Sterk beslutningsanalyse, fortsatt non-normative |
| `P0.9_prep_package.md` | pre-architecture uncertainty reduction v1 | Plan/prep |
| `P0.9_prep_package(1).md` | faktisk v2 med ny Deep Research brief | Senere prep; v2 overstyrer v1s researchdel |
| `claude_P0.9_architecture_prep_chat_integration_summary.md` | kronologi for prep-løpet | Proveniens |
| `Optimizing P0.9 Architecture_integration_summary.md` | parallell prep-/uncertainty-reduction-chat | Proveniens + brukerkrav |
| `Norwegian application-package research_integration_summary.md` | research-launch-rekonstruksjon | Viktig for formål, men inneholder ikke selve funnene |
| P0.9 External Evidence Report | fullført research | Factual evidence med eksplisitte begrensninger |
| `Personality.md` | kanonisk fortolkningsprofil | Interpretiv, ikke kandidat-faktamyndighet |
| `Personality_P0.9_Framework_Context.md` | runtime-adaptasjon | Provisional design; togglekravet er brukerbesluttet, 20-facet-protokollen ikke |
| BAR-evidensrapporten | kandidat-evidensvedlikehold fra 52 filer | Parallell source-maintenance; ikke automatisk innlemmet i authority files |
| `Jobbsøk_26_integration_summary.md` | nyeste brede state reconstruction + siste brukerbeslutninger | Høy for terminal state og eksplisitte brukerbeslutninger |

Eksakte byte-duplikater er ikke behandlet som selvstendige signaler.

---

# 3. Verifisert P0.7 — hva rammeverket faktisk var

## 3.1 Releasekarakter

P0.7 er ikke en plan. Den er en 52-fils release med:

- root policy/operatorfiler;
- tre kandidatmyndigheter;
- avledet CV-baseline;
- to Word-mastere;
- package contract;
- fire fysiske stageområder;
- tre aktive scripts;
- testfixtures;
- implementerings-, test- og manifestdokumentasjon.

Dette er avgjørende fordi senere P0.8/P0.9-dokumenter kan vurderes som **deltas mot virkelig kode**, ikke bare mot tidligere arkitekturprosa.

## 3.2 P0.7-topologi

```text
~40 godkjente jobber
   |
   +-- 2 makroklynger à ~20
         |
         +-- Stage 1: Terra Max, 2 chatter, 10+10
         +-- Stage 2: Sol Max,   2 chatter, 10+10
               |
               +-- split til 4 miniklynger à ~10
                     |
                     +-- Stage 3: Terra XHigh, selektiv Max, 4 chatter, 5+5
                     +-- Stage 4: Sol XHigh, selektiv Max,   4 chatter, 5+5

Totalt: 12 standardchatter
```

## 3.3 Semantisk rollefordeling

### Stage 1 — kandidatblind vacancyanalyse

- kandidatfiler er forbudt;
- produserer `job_identity.json` og `vacancy_analysis.md`;
- hensikten er å forstå arbeidsgiver før kandidaten introduseres.

### Stage 2 — Sol evidence/strategy

- bygger `CLUSTER_EVIDENCE_BASE.md` med to evidence lanes;
- bestemmer `MINICLUSTER_SPLIT.json`;
- lager `package_blueprint.md` per jobb;
- låser i praksis evidence-/strategigrunnlaget for senere writer.

### Stage 3 — Terra drafting

- skriver `draft_package.json`;
- bruker bare dynamiske CV-overrides mot baseline;
- skriver norsk employer-facing tekst;
- skal ikke rendere.

### Stage 4 — Sol Writer/Recruiter Mirror

- redigerer draft til `final_package.json`;
- er konstruktiv editor, ikke veto-gatekeeper;
- produserer private `review_flags.md`;
- er likevel mer bundet til Stage 3/evidence lock enn den senere P0.8-filosofien tillater.

## 3.4 Mekanisk bane

Tre aktive scripts:

```text
scripts/ingest.py
scripts/advance.ps1
scripts/finalize.py
```

`advance.ps1` eksisterer fordi P0.7 fysisk kopierer kontrollert output fra makro-Stage 2 til miniklynge-Stage 3. Dette skaper både mekanisk gating og operatørfriksjon.

## 3.5 P0.7 package contract

`contract_version = 0.7`.

Kjerneformen er:

```text
job
  job_id
  batch_id
  macro_cluster_id
  mini_cluster_id
  employer
  title
  unit?
  reference?
  language=nb-NO
  letter_required

cv_overrides
  baseline_version
  profile
  key_competencies[4..8]
  experience_overrides[1..4]
    employment_id
    bullets[1..5]

application
  null | opening + body_paragraphs + closing

portal_answers[]
  question_id
  question
  answer
  max_words?
  max_chars?
```

Det mangler et eget `headline`/candidate-identity-felt. P0.7-rendereren utleder funksjonell identitet fra kompetansene — en senere eksplisitt kvalitetsfeil.

## 3.6 P0.7 truth model

Tre filer er eneste kandidat-faktamyndigheter:

- `Work_experience.md`
- `Education.md`
- `Other_high_value_information.md`

`CV_BASELINE.md` er avledet og kan aldri oppgradere en claim over kilden.

Vacancy er inputdata, ikke instruksjonsmyndighet.

## 3.7 P0.7 finalizer

Finalizer gjør blant annet:

- expected/completed reconciliation;
- job/batch/cluster/path/employer/title-kryssvalidering;
- baselineversjon;
- employment-ID-kontroll;
- portalgrenser;
- brev/no-letter-kontrakt;
- hard CV ≤2 A4;
- hard application ≤1 A4;
- private leakage-/placeholderkontroll;
- DOCX/PDF-rendering fra originale mastere;
- ingen overskriving uten `--force`.

Dette er mekanisk sterkt, men noen kvalitetsproxyer er for harde i forhold til senere produktmål.

## 3.8 Templatefunn fra den faktiske builden

Dette er et nytt og viktig kryssreferansefunn mellom baseline og senere research.

### CV-master

- 17 Word content controls (`w:sdt`);
- **0 data-bound SDT-er**;
- 0 tabeller;
- 0 text boxes;
- 0 drawings;
- én dokumentseksjon;
- navn + «CV» ligger i header;
- ellers er hovedinnholdet én lineær tekstflyt.

### Søknadsmaster

- 7 SDT-instanser / 6 unike tags;
- **0 data-bound SDT-er**;
- 2 tabeller;
- 0 text boxes;
- 0 drawings;
- kontaktinformasjon ligger i header.

### Kritisk konsekvens

P0.7 `finalize.py` fyller SDT-ene direkte i OOXML og kjører deretter `unwrap_content_controls()` før LibreOffice. `validate_rendered_docx()` feiler dersom en eneste `w:sdt` fortsatt finnes.

Dermed gjelder ikke den senere generiske Deep Research-advarselen «LibreOffice/content controls er risikable» på den enkle måten den kan leses:

- de konkrete masterne er ikke data-bound;
- LibreOffice trenger ikke tolke content-control-logikken;
- P0.7s testkjede har allerede bevist fylling → unwrap → DOCX/PDF i kontrollert miljø.

**Reell gjenværende risiko:** target-Windows/headless-LO og ATS/parsing i faktiske portaler er ikke lokalt verifisert. Dessuten ligger kandidatnavnet i CV-header, mens ekstern research advarer mot kritisk ATS-innhold i headers. Det er et konkret template-spike-punkt, ikke en grunn til å kaste masteren.

## 3.9 Verifisert releasebevis

Jeg re-kjørte P0.7-testene nå:

- 34 kjørt;
- 32 PASS;
- 2 SKIP fordi PowerShell runtime ikke er installert;
- 0 FAIL.

Kontrollert E2E og rendering passerer. Testene viser blant annet:

- PDF ingest;
- package/schema/identity;
- negative finalizerfeil;
- partial-like job failure handling i finalizer;
- eldre employment override;
- dense/sparse CV-render;
- letter/no-letter;
- portal;
- privat/offentlig separasjon.

Men to fundamentale ting er fortsatt `NOT RUN`:

1. ekte Terra/Sol-produksjonsstages;
2. en reell vacancy-pilot.

P0.7 er derfor **mekanisk validert, men semantisk produkt-uvalidert**.

---

# 4. Hvorfor P0.7 ble forlatt: audit → målfunksjonsskifte

## 4.1 Auditfunnene som faktisk drev redesign

P0.7-auditen identifiserer flere feil. De viktigste for P0.8 er:

### A. Mutable-draft integrity bypass

Finalizerens no-new-employment-kontroll kan sammenligne mot en Stage-4-kontrollert draftkopi. Den mekaniske kontrollen kan derfor omgås.

Den første reaksjonen var strengere immutability. Senere produktanalyse viste imidlertid at **selve «Stage 4 kan aldri hente ny baseline-kjent evidence» var feil kvalitetsmål**.

Dette er et godt eksempel på evolusjonsmønsteret:

```text
faktisk defekt beholdes som sannhet
→ opprinnelig remedie forkastes
→ P0.8 løser problemet ved å validere mot baseline + source truth,
  samtidig som Final Sol får strategisk frihet
```

### B/C. `_DONE.md` og review-heading substring-theatre

P0.7 kan validere tilstedeværelse av strenger uten å bevise riktig struktur/semantikk. P0.8 fjerner store deler av denne statusoverflaten og går til parsebare artefakter + minimal progress.

### D. Duplicate portal question IDs

Dette er en billig, synlig, employer-facing feil og overlever som mekanisk hard rule.

### G. Sparse CV tvunget til to sider

Dette er et direkte sluttproduktproblem. P0.8 gjør sidebudsjett soft og lar sparse CV bli én side.

### H. Kandidatidentitet ikke eksplisitt

P0.8 introduserer dedikert `headline`.

## 4.2 Brukerens eksplisitte målkorreksjon

Den viktigste hendelsen i hele P0.8-linjen er at brukeren korrigerer den defensive auditlogikken:

- systemet skal ikke optimere worst-case uniformitet;
- svake ~20 % kan tas separat;
- stor gevinst kan komme av at ~75–80 % er svært sterke;
- QA-systemet må ikke stjele kompleksitetsbudsjett fra skriverkvalitet.

Resultatet er `Q_happy`:

```text
Q_happy = (Median(q) + Mean(Top80%(q))) / 2
```

Dette flytter designet fra «batch compiler correctness» til «selective quality production system».

---

# 5. P0.8.0 — den første komplette normative redesignen

## 5.1 Normativ status

P0.8-filen sier eksplisitt:

```text
release: P0.8
specification_version: 0.8.0
status: FINAL_NORMATIVE_SPECIFICATION
supersedes:
  - P0.7 architecture and runtime design
  - all preliminary P0.8 brainstorming and alternative architectures
```

Dette er den historiske autoritetsgrensen. Ekstern reviewtekst som kaller seg «endelig» før denne filen må underordnes der de er uenige.

## 5.2 Topologisk redesign

P0.8 kollapser P0.7s fire semantiske stages til tre:

```text
P0.7 Stage 1 vacancy analysis
+
P0.7 Stage 2 evidence/strategy
        ↓
P0.8 Stage 1 Decision Architecture — Sol Max

P0.7 Stage 3 drafting
        ↓
P0.8 Stage 2 Native Package Writer — Terra Max

P0.7 Stage 4 mirror
        ↓
P0.8 Stage 3 Final Writer & Selective Review — Sol Max
```

Klyngemodellen blir flat:

```text
~40 jobber
→ normalt 5 klynger à ~8
→ normalområde 6–10
→ 3 chatter per klynge
→ 15 standardchatter
```

Viktig: P0.8 **øker** standard chat count fra 12 til 15. Forenklingen ligger i:

- én klyngetype;
- ingen makro→mini-split;
- ingen `advance.ps1`;
- færre status-/handoffartefakter;
- kortere semantisk kjede;
- klarere rollefordeling;
- mindre fysisk kopiering/state.

## 5.3 Sol–Terra–Sol som kvalitetsarkitektur

### Stage 1 — Sol Max

Sol får de mest ikke-lineære valgene:

- employer problem;
- decision tests;
- selection regime;
- kandidatidentitet;
- headline-hypotese;
- evidence pair;
- shortlist thesis;
- motivation bridge;
- channel allocation.

Stage 1 beholder en kandidatblind **Phase A**, men kandidatbevisst strategi skjer i samme cluster-chat. Senere review presiserer korrekt at dette er en **read-order/debiasing protocol**, ikke ekte kognitiv isolasjon.

### Stage 2 — Terra Max

Terra får den outputtunge oppgaven:

- komplett CV-dynamikk;
- komplett søknad;
- portal answers når relevant;
- naturlig Bokmål;
- én helhetlig package før neste jobb.

### Stage 3 — Sol Max

Final Sol er ikke en reviewer i snever forstand. Den er endelig forfatter:

- kan bytte headline;
- kan bytte primary identity;
- kan bytte evidence pair;
- kan omfordele kanalroller;
- kan skrive flere seksjoner på nytt;
- kan full-rewrite;
- kan gjøre målrettet source-check.

Dette er rammeverkets sentrale «compensating freedom»-mekanisme: tidligere handoffartefakter må hjelpe, ikke fange sluttskriveren.

## 5.4 Review blir handling, ikke poeng

P0.7s `review_flags.md` erstattes av `review.json`:

```text
READY
CHECK
RERUN
```

- ingen numeric quality score;
- ingen confidence;
- maks tre konkrete reasons;
- finalizer kan legge mekaniske soft reasons i review queue uten å omskrive modellens canonical review.

## 5.5 Partial success blir eksplisitt produktregel

Finalizerklassene:

```text
DELIVERED_READY
DELIVERED_CHECK
DELIVERED_RERUN
FAILED
```

Batch kan returnere nonzero uten at gode jobbutdata destrueres.

## 5.6 Sannhets- og evidenceendring

P0.8 beholder tre authorities + baseline, men fjerner P0.7s sterke evidence-lock:

- Stage 1 lager evidensposter med `evidence_id/source/heading/core fact/contribution/lifecycle/safe strong formulation`;
- Stage 2 bruker strategiens evidence;
- Stage 3 kan velge annerledes evidence hvis den reåpner kilden og holder claim ceiling.

`used_evidence_refs` blir en eksplisitt intern provenanceflate.

## 5.7 CV-modellen forbedres direkte

P0.8 package får eksplisitt:

```text
headline
profile
key_competencies
employment_overrides
```

Baseline beholder:

- arbeidsgiver;
- formell tittel;
- periode;
- education;
- språk;
- øvrige statiske seksjoner.

Employment override er ment å bytte bullets, ikke rekonstruere employment identity.

## 5.8 Renderingendringen

P0.8 beholder P0.7-masterne som designbase, men krever kirurgisk tilpasning:

- direct headline;
- færre/ryddigere aktive tags;
- weak forced page split fjernes;
- sparse CV kan bli 1 side;
- normal/dense typisk 2;
- >2 sider rendres og gir CHECK, ikke nødvendigvis hard reject.

Dette er en direkte konsekvens av `Q_happy`: god prosa skal ikke kastes på grunn av et mekanisk proxyproblem som et menneske kan fikse lokalt.

## 5.9 Runtime og state

P0.8 fjerner:

- `_DONE.md`;
- stor `BATCH_STATUS.md`;
- `BLOCKED.md` som primær state;
- `advance.ps1`;
- broad `CLUSTER_EVIDENCE_BASE.md`;
- `MINICLUSTER_SPLIT.json`.

State blir:

```text
canonical semantic artifacts
+
minimal progress.json
```

Dette er en fundamental reduksjon i state-surface.

---

# 6. P0.8.1 review — hva den faktisk løser, og hva den ikke har rett til å erklære

## 6.1 Status

`Jobbsok_26_P0.8_consolidated_preimplementation_review.md` er eksplisitt:

```text
status: NON_NORMATIVE_UNTIL_ADOPTED
target_release: P0.8.1 contract-hardening before implementation
```

Den sier samtidig at P0.8s **produktarkitektur er riktig** og at neste runde bør være contract hardening, ikke redesign.

Historisk må P0.8.0 derfor fortsatt stå som canonical. Men for å rekonstruere den **mest utviklede targeten** er reviewet svært viktig, fordi mange punkter er rene manglende kontraktdetaljer snarere enn nye produktvalg.

## 6.2 De viktigste direkte hardeningene

### Canonical input / deliverables

P0.8 har redundant `channel`, `letter_required`, `portal_required` og planstate. P0.8.1 anbefaler én maskinlesbar kilde for faktisk leveransekrav, med derivert state fremfor flere parallelle bools/enums.

Dette er en ekte kontraktforbedring fordi inkonsistente representasjoner ellers er mulig.

### Freeze + context snapshot

P0.8 sier batch fryses ved Stage 1-start, men har ikke et fullstendig operativt snapshot. P0.8.1 anbefaler immutable `context_snapshot.json` ved ingest/freeze.

Dette blir senere videreutviklet i P0.9-reviewet til `N-01`: ett freezeobjekt med statiske invalidation classes.

### `cluster_plan` må få schema

P0.8 lar Stage 1 skrive en maskinkritisk `cluster_plan.json`, men har ikke schemafil for den. P0.8.1 legger til schema + set equality mot frozen job set.

### Expected-job reconciliation

Finalizer skal enumerere forventede jobs fra frozen plan, ikke «oppdage» outputmapper. Manglende output må være synlig failure/status.

### Mechanical-hard vs semantic-hard

Python kan validere:

- ID;
- schema;
- kjent employment;
- required artifact;
- eksakt portal limit;
- template contract;
- render/open/selectability;
- leakage med høy-presisjonsregler.

Python kan **ikke** bevise at en fri formulering er semantisk dokumentert eller at claim-strength er riktig. Det må forbli modell/human domain.

Denne distinksjonen er sentral og bør anses som en av de sterkeste P0.8.1-presiseringene.

### Full bullet-array replacement

`employment_overrides` betyr full erstatning av bullet-array for den aktuelle `employment_id`, ikke partial merge. Dette fjerner en reell implementeringsambiguity.

### Final evidence refs må reflektere faktisk sluttpakke

Hvis Stage 3 bytter evidence, skal `used_evidence_refs` oppdateres. Provenance skal beskrive det som faktisk leveres, ikke det Stage 1 opprinnelig valgte.

### Reviewstatus etter repair scope

En god operasjonell definisjon er:

- `READY`: ingen materiell handling utover normal skim/faktasjekk;
- `CHECK`: 1–3 lokale avklaringer/reparasjoner; ingen ny backbone;
- `RERUN`: identitet/evidence/motivation/channel-backbone eller multisection rewrite må rekonstrueres.

Dette er langt bedre enn en vag «confidence».

### RERUN-kontrakt

P0.8.1 spesifiserer Sol Max, én jobb per separat RERUN-chat, med målrettet authority access.

### Stage validator før completion

Artefakt skal ikke markeres complete før standard validator exit 0.

Senere `N-04` kompletterer dette med bounded same-session repair.

## 6.3 Pilot-/evalhardening

### Small-n Top80

For `n=8` er 20 % = 1,6. P0.8.1 gjør dette eksplisitt:

```text
bottom_k = max(1, floor(0.20*n + 0.5))
top_k    = n - bottom_k
```

For 8 jobs:

```text
bottom_k=2
top_k=6
```

Men rapporter også:

- raw q;
- median;
- mean all 8;
- mean top 7;
- mean top 6;
- primary `Q_happy`.

### Human total time

Edit-minutter alene undervurderer menneskekost. Logg review/rerun/total handling.

### Credits på riktig enhet

Stagechatter er cluster-level, ikke naturlig per-job. Derfor bør kost logges per faktisk run/chat og bare fordeles med eksplisitt estimat hvis nødvendig.

### Priority A/B er confounded

P0.8 gir A både prediksjonslabel, tidlig posisjon og mer microvariation. Da kan A-success ikke tolkes som prediksjonskvalitet. Dette åpner senere DC-6.

## 6.4 Implementation sequence blir bedre

P0.8.1 flytter «bevis den vertikale mekanikken» mye tidligere:

```text
A authority-preserving migration + contract patch
B one-job deterministic vertical slice
C template/render hardening
D stage instructions + validators
E multi-job mechanics
F Tier0/1 QA + two-job live smoke
G docs/release polish
H real ~8-job product pilot
```

Dette er en klar forbedring over å bygge hele repository-/test-/releaseoverflaten før den vanskeligste kjeden er bevist.

## 6.5 Low-value forslag som blir eksplisitt avvist

Cross-model consolidation rydder bort blant annet:

- YAML duplicate strategy state;
- typografisk auto-fit;
- 5-gram similarity gate;
- 15 % portal tolerance;
- per-job authority snapshot copies;
- LibreOffice service/daemon;
- ny judge-stage;
- auto rerun;
- DB/event sourcing;
- vector/RAG.

Dette er viktig fordi senere P0.9 ikke starter fra et tilfeldig brainstormfelt; mye kompleksitet er allerede bevisst beskåret.

---

# 7. P0.9 — fra «patch P0.8» til kontrollert reopening av designrommet

## 7.1 Brainstorm Brief er eksplorativt, ikke en spec

`Brainstorm_Brief.md` er eksplisitt laget for å bevare en stor option space. Den stabile kjernen er fortsatt:

- source-governed truth;
- persuasion-first;
- CV + application som sentral arbeidsgiververdi;
- dynamic CV;
- deterministic mechanics vs semantic models;
- manual stage initiation;
- no-submit;
- partial success;
- constructive final writer;
- human semantic authority.

Det som åpnes er særlig:

1. product boundary/portal;
2. personality/authenticity;
3. context preparation/Luna;
4. strategy artifact format;
5. runtime tree/state/provenance;
6. priority/order/treatment;
7. implementation/test sequence.

## 7.2 `brainstorm_review.md` gjør option space beslutningsbart

Det viktigste bidraget er ikke én anbefalt bundle, men en normalisert decision matrix.

### DC-1 Product boundary

- **1a:** invariant CV+application core, portal detached, nb-NO only, no channel enum — reviewerens sterkeste;
- 1b: behold portal core som P0.8.1-control.

Brukeren har senere eksplisitt gitt **tillatelse** til 1a-prinsippene, men ikke valgt dem som endelig arkitektur.

### DC-2 Personality

- control: ingen personality;
- testbare, begrensede varianter;
- full profile til alle stages forkastes.

Senere brukerbeslutning: personality skal være optional via `SETTINGS.md`. Default ON/OFF er fortsatt åpent.

### DC-3 Context

- 3a direct retrieval;
- **3b deterministic lossless evidence index**;
- 3c 3b + Luna advisory prep;
- aggressive global/cascading model-filtre prunes.

External Evidence Report gjør 3c mindre attraktiv som default fordi Luna viser svakere svært-lang-kontekst-resultater, mens 3b er tapsfri og modellfri. Men senere integrasjonssammendrag advarer korrekt mot å kalle 3b «bevist bedre» før lokal nytte er målt.

### DC-4 Strategy artifact

- Markdown med stabile labels = control;
- JSON + lokal validator = mulig;
- JSON + deterministisk Markdown-view = mulig;
- model-written dual truth = forkastet.

External research presiserer at JSON Schema Structured Outputs ikke er garantert i manuell chat. JSON må derfor lokalt valideres/repareres dersom valgt.

Ingen endelig formatbeslutning finnes.

### DC-5 State/runtime

- P0.8.1 stage-centric snapshot/progress = control;
- partitioned manifest + job-centric tree + redusert progress = lovende alternativ;
- full state derivation uten progress prunes.

Senere bruker sier eksplisitt at P0.9 **kan og bør bruke fresh runtime architecture**, at bakoverkompatibilitet med gammel tree ikke kreves, og at job-centric tree er tillatt dersom bedre. Dette åpner DC-5, men velger ikke 5b.

### DC-6 Priority/order/treatment

Den sterkeste nye idéen er **6b**:

- behold order (distinct jobs early, similar separated);
- fjern differentiated treatment/microvariation;
- la A/B være ren prediksjonslabel for evaluering.

Dette løser P0.8.1s confounding. Men heller ikke 6b er eksplisitt brukeradoptert.

### DC-7 Implementation

Konvergerer med P0.8.1 vertical-slice-first, med tillegg av template spike og små paired tests før en pilot dersom de ellers ville kontaminere baseline.

## 7.3 N-mekanismene

### N-01 — partitioned invalidation i ett freezeobjekt

Fire statiske klasser:

```text
SOURCE_TRUTH   -> semantic outputs for affected jobs stale
WRITING_POLICY -> draft/final stale; strategy bare hvis policy påvirker strategy
RENDER_ASSET   -> rerender only
SCHEMA         -> revalidation only
```

Dette er en elegant videreutvikling av P0.8.1 `context_snapshot`: mer presis invalidation uten runtime dependency engine.

### N-02 — `evidence_outside_prep`

Hvis prep/index brukes, kan final package registrere refs som sluttforfatteren måtte hente utenfor prepared context. Dette er diagnostikk, ikke sannhetsbevis.

### N-03 — deterministic evidence index

Et modellfritt indeksobjekt over stabile authority-seksjoner:

```text
evidence_id
source_file
heading_path
section_hash
approx_size
lifecycle_label?
claim_ceiling_marker?
```

Ingen vacancy-relevance, ingen filtering. Det er derfor mer en navigasjonsstruktur enn RAG.

### N-04 — validator failure protocol

```text
validator exit != 0
→ modellen leser feilen
→ reparerer artefakten i samme session
→ revalidate
→ maks 2 repair attempts
→ tredje failure registreres, ikke completed, fortsett uavhengig jobb
```

Senere brukerbeslutning tillater eksplisitt deterministic validators + same-session repair. External research presiserer at dette krever en overflate som faktisk kan kjøre lokal kode, f.eks. Codex; vanlig webchat kan ikke antas å kunne gjøre det.

### N-05 — upstream claim repair trace

En liten reviewindikator gjør det målbart hvor ofte Final Sol måtte reparere unsupported upstream claims.

### N-06 — protocol-not-isolation

Kandidatblind read-order, final independent read, prep tiers osv. er **behavioral protocols**, ikke mekaniske boundaries. Dette hindrer falske tester som bare beviser at instrukstekst finnes.

---

# 8. P0.9 prep og ekstern research — hvilke gamle antakelser som faktisk endres

## 8.1 Prep v1 → v2

`P0.9_prep_package(1).md` er ikke en download-duplikat. Diffen begynner ved researchdelen og erstatter den opprinnelige norske application-channel briefen med en bredere, mer systematisk P0.9 Deep Research brief med:

- OpenAI execution facts;
- long-context/context preparation;
- norske portaler/public sector;
- Word/LibreOffice/security;
- eksplisitt evidence tagging;
- arkitekturbeslutningsguardrails.

Resten av prep-pakken organiserer:

- brukerquestionnaire;
- vacancy inventory;
- template spike;
- environment preflight;
- quality anchor set;
- precedence/conflict table.

Dette er **uncertainty-reduction**, ikke P0.9-arkitektur.

## 8.2 Viktige researchoppdateringer

### Context window != garantert full oppmerksomhet

Store context windows betyr ikke at alle store filer sikkert er fullt aktive/retrieved i alle surfaces. Lost-in-the-middle og file ingestion/retrieval gjør «bare last alt og stol på modellen» til en empirisk antakelse, ikke en kontrakt.

### Luna er billig, men long-context-risk er reell

Researchrapporten viser stor forskjell mellom Sol/Terra og Luna på svært lang multi-needle-context. Dermed er billig Luna-prep ikke gratis kvalitetsmessig.

Dette støtter å teste 3c mot 3b, ikke å gjøre Luna til default.

### Structured Outputs er ikke chatgaranti

Et `strategy.json` generert i manuell Work/Codex-interaksjon må fortsatt lokalt valideres. Schema-garanti fra API kan ikke backportes til chat.

### Same-session validator repair er surface-avhengig

Codex kan kjøre local validator og reparere. Plain webchat kan ikke antas å ha den capabilityen. Dette må inn i final surface-routing.

### Norske portaler er per-vacancy/per-employer

Format-, attachment-, letter- og portalgrenser må leses per vacancy. Hardkoding av en global Webcruiter-policy er feil.

### Kvalifikasjonsprinsippet påvirker evidensdekning, men ikke nødvendigvis brevstil

Utlysningens krav er sentrale for offentlig vurdering. Men den senere integrasjonen korrigerer en oversterk researchinferens: dette betyr **ikke** at søknadsbrevet juridisk må være en punktvis checklist.

### Portal/application kan være free-text eller questions

Dette styrker argumentet for å skille kanaldata fra rik DOCX-layout og er relevant for DC-1, men velger ikke automatisk detached portal.

### Prompt injection

Vacancyfiler er untrusted data. Regex er ikke en «AI firewall». Riktig boundary er:

- data/instruction-separasjon;
- least privilege;
- bounded tooling;
- human irreversible gate.

## 8.3 Researchfunn som baselineanalysen nå nyanserer

### Content controls

Researchrapporten advarer spesielt mot data-bound Word SDT og community-observerte LO-problemer. Den faktiske P0.7-masteren:

- har **ingen data-bound SDT**;
- blir fylt og unwrapped før konvertering;
- har allerede kontrollert DOCX/PDF-pass.

Det er derfor feil å konkludere «P0.9 må fjerne content controls». Riktig konklusjon er:

> Bevar OOXML-fyll/unwrap-teknikken inntil en target-machine template spike viser en faktisk feil. Ikke la generisk research erstatte konkret lokal release-evidens.

### CV parseability

P0.7 CV har ingen tabeller/text boxes/drawings i body — positivt. Men kandidatnavnet ligger i header — et konkret område å teste/evt. duplisere parse-sikkert dersom faktisk ATS-resultat tilsier det.

---

# 9. Personality-linjen — hva som faktisk er besluttet

## 9.1 `Personality.md`

Dette er et rikt interpretivt selvmodell-/arbeidsstildokument. Det kan være nyttig for:

- candidate positioning;
- misread prevention;
- motivasjon;
- tone/authenticity;
- hvilken factual evidence som bør fremheves.

Det kan **ikke** etablere nye employer-facing fakta.

## 9.2 Framework-adaptasjonen

`Personality_P0.9_Framework_Context.md` foreslår:

- `SETTINGS.md::personality`;
- OFF/ON;
- 0–3 selected facets;
- Sol velger facets;
- Terra får bare distilled guidance;
- Final Sol kan suppress/replace;
- 20 PF-IDs.

Seneste autoritet må splittes:

### Brukerbesluttet

- personality-funksjonen skal være **optional**;
- styring via `SETTINGS.md` er ønsket;
- originalprofilen er en composite av flere frameworks/instruments/self-synthesis.

### Ikke besluttet

- default ON/OFF;
- eksakt 20-facet runtime interface;
- 0–3-regelen;
- stage handoff-formatet;
- om personality faktisk forbedrer sluttkvalitet.

Dermed kan final spec kreve en **off-safe toggle boundary**, men ikke late som PF-01…PF-20 er adoptert produktkontrakt.

---

# 10. BAR-evidensrapportens plass

`deep-research-report (16).md` er relevant for senere Jobbsøk_26 fordi den rekonstruerer BAR-erfaring fra 52 filer og foreslår vedlikehold av `Work_experience.md`.

Men siste eksplisitte brukerbeslutning sier at alle tre kandidatmyndighetene er **CURRENT** og immutable under produksjon.

Derfor:

- BAR-rapporten kan være input til en separat fact-maintenance-runde;
- den kan ikke automatisk endre production authority;
- den skal ikke leses som en fjerde runtime truth source;
- hvis den senere medfører godkjent oppdatering av `Work_experience.md`, må baseline regenereres og ny run freeze etableres.

Dette er et godt eksempel på «nyere dokument finnes» uten at det automatisk overskriver eksisterende authority.

---
# 11. Granulær supersession-matrise — hva er faktisk gjeldende nå?

Dette er kjernen i «latest wins only where it truly supersedes»-metoden. Hver rad behandles som et eget granularitetspunkt. En senere tekst får **ikke** lov til å erstatte eldre informasjon bare fordi dokumentet er nyere; den må faktisk endre, spesifisere, bygge på eller ugyldiggjøre samme punkt.

Statusetiketter brukt videre:

- **VERIFIED-P0.7** — observert i den faktiske P0.7-releasen og/eller rerun-verifisert her.
- **USER-CURRENT** — eksplisitt senere brukerbeslutning; høyeste nåværende policyautoritet.
- **INHERITED-P0.8** — siste normative regel fra P0.8.0 som ikke er senere erstattet.
- **DERIVED-HARDENING** — senere review/research som direkte reparerer et konkret kontraktproblem uten å endre produktideen; historisk ikke formelt adoptert som release, men bør inngå i den beste nåværende målspesifikasjonen.
- **PROVISIONAL** — sterk kandidat eller tillatelse, men ikke valgt.
- **OPEN** — eksplisitt uløst; eldre normative default beholdes bare som fallback/control, ikke som bevis på at P0.9-valget er tatt.

| Granulært punkt | P0.7 | P0.8.0 | Senere P0.8.1/P0.9 | Nåværende beste tolkning |
|---|---|---|---|---|
| Primær bruker | Én kandidat | Én kandidat | Samme kandidat, gjenbruk over flere batches / mulig lang levetid | **USER-CURRENT:** personlig, gjenbrukbart same-candidate-system; ikke flerbrukerprodukt |
| Batchstørrelse | ~40 | ~40 | ~40 fortsatt | **USER-CURRENT/INHERITED:** rundt 40 godkjente stillinger som normalbatch |
| Kvalitetsmål | Implisitt robusthet | `Q_happy` | ~30 sterke av ~40; svak hale kan rerun/drop/separat | **USER-CURRENT:** sterk majoritet, ikke uniformitet |
| Objektivrangering | KISS/human effort | pakke/intervjukvalitet først | quality > human effort > implementation speed > model cost > reversibility | **USER-CURRENT** |
| Candidate truth | 3 authority-filer | arves | Alle tre eksplisitt CURRENT og immutable i run | **USER-CURRENT** |
| Authority maintenance | Utenfor run | Utenfor run | BAR-rapport kan informere separat maintenance | **USER-CURRENT:** ingen automatisk authority-oppdatering i production |
| Job freeze | Batchplan | Frozen intake | Jobs normalt frozen; sene endringer unntak | **USER-CURRENT** |
| Semantiske stages | 4 | 3 | Ingen senere eksplisitt endring | **INHERITED-P0.8:** 3 stages |
| Stage 1-modell | Terra Max | Sol Max | Ingen senere endring | **INHERITED-P0.8:** Sol Max |
| Stage 2-modell | Sol Max | Terra Max | Ingen senere endring | **INHERITED-P0.8:** Terra Max |
| Stage 3-modell | Terra XHigh | Sol Max | Final Sol eksplisitt ELASTIC | **USER-CURRENT + INHERITED:** Sol Max med full truth-bounded rekonstruksjonsmyndighet |
| Stage 4 | Sol XHigh | Fjernet | Ikke gjeninnført | **INHERITED-P0.8:** ingen separat fjerde semantic stage |
| Cluster count | 4×~10 | ~5×~8 | Ikke omvalgt; promptbudsjett nå 20–25 | **INHERITED control:** ~5×8, men empirisk parameter, ikke dogme |
| Cluster range | ~10 | normalt 6–10, max 10 standard | Ikke endret | **INHERITED-P0.8** |
| Within-stage execution | Cluster chats | ett cluster per chat, jobs sekvensielt | Eksplisitt bekreftet uten routine confirmations | **USER-CURRENT** |
| API orchestrator | Ingen | Ingen | Manuelt initierte distinkte model chats eksplisitt | **USER-CURRENT:** ingen normal API-orkestrering |
| Lokale scripts | 3 (`ingest`, `advance`, `finalize`) | 2 (`ingest`, `finalize`) | Lokale validators/scripts tillatt i session | **INHERITED + USER-CURRENT:** liten deterministisk kodeflate; ikke skjult orchestrator |
| Product core | CV/app/portal iht. channel | CV/app/portal iht. identity | CV+application invariant **kan** velges | **OPEN:** P0.8-integrert portal er control; invariant CV+application er tillatt kandidat |
| Portal | Integrert | Integrert | Kan detach-es post-package | **OPEN P0.9:** ikke lat som valgt; behold eksakt hard validation dersom integrert |
| Language | `nb-NO` i schema | nb/en | Første release kan være nb-NO-only | **PROVISIONAL permission:** real vacancy inventory avgjør |
| Rare cases | Branches | channel-aware | Kan håndteres separat | **USER-CURRENT:** core trenger ikke universaliseres for sjeldne avvik |
| Dynamic CV | Begrensede overrides | headline/profile/competencies/employment bullets | Samme scope eksplisitt tillatt | **INHERITED + USER permission:** dette er sterk current default |
| CV headline | Ikke eksplisitt felt | Eksplisitt | Ikke reversert | **INHERITED-P0.8** |
| Employment override | Delvise bullets | dynamisk | Review: full bullet-array replacement | **DERIVED-HARDENING:** eksplisitt replacement-semantikk |
| Full chronology | Ja | Ja | Ikke reversert | **INHERITED-P0.8** |
| Strategy artifact | Stage2 evidence base | `strategy.md` | JSON/prose-format åpnet som valg | **OPEN:** Markdown er siste normative control |
| Strategy size | N/A | 900–1400 soft, max 1800 | 400–1000 anbefalt i review | **OPEN:** behold 900–1400 som control til test viser bedre |
| Strategy independence | Fysisk stage isolation | candidate-blind Phase A + candidate-aware Phase B | N-06: protocol, ikke ekte boundary | **DERIVED-HARDENING:** beskriv read-order/protocol ærlig; ikke påstå isolasjon |
| Evidence retrieval | Shared evidence base | job-local exact cited sources | Deterministisk evidence index kandidat | **OPEN:** direct retrieval er control; index er low-risk kandidat, ikke valgt |
| Cheap Luna prep | Ingen | Ingen | Foreslått/testbar; research viser long-context-risk | **PROVISIONAL/TEST-ONLY:** ikke core uten lokal gevinst |
| Personality | Ingen runtime | Ingen | Optional via SETTINGS user-current; runtime details open | **USER-CURRENT toggle boundary; OPEN default/interface** |
| Final writer authority | Begrenset av mutable draft/evidence lock | Full truth-bounded rebuild | ELASTIC eksplisitt bekreftet | **USER-CURRENT** |
| Final evidence refs | Svak mutable-draft lock | `used_evidence_refs` | Må synkes mot faktisk sluttpakke | **DERIVED-HARDENING** |
| Upstream correction trace | Ingen | Ikke eksplisitt | N-05 foreslått | **PROVISIONAL/HARDENING kandidat:** billig observability, men ikke user-locked |
| Review | Heading/state, sårbart | READY/CHECK/RERUN | Definer etter repair scope | **DERIVED-HARDENING:** handlingsbasert status uten score |
| RERUN | Ikke P0.8-stil | ett-jobb rerun | Sol Max, egen chat, targeted source | **DERIVED-HARDENING:** sterkeste komplette kontrakt |
| Partial success | Begrenset | Eksplisitt | Bekreftet | **INHERITED-P0.8** |
| Validator gate | Tests/scripts | implisitt/kontrakt | Stage complete først etter validator exit 0 | **DERIVED-HARDENING** |
| Repair protocol | Manuell | Ikke fullt spesifisert | N-04 max 2 same-session repairs, tredje fail og continue | **DERIVED-HARDENING**, men execution-surface-avhengig |
| Machine input | `job_identity`/batch | `batch_plan` + job identity | CR-01 canonical job/deliverable input | **DERIVED-HARDENING** |
| Required outputs | Channel + booleans | Redundante signaler | Ett canonical required-output state | **DERIVED-HARDENING** |
| Context freeze | Hashes | frozen artifacts | `context_snapshot.json`; N-01 static invalidation classes | **DERIVED-HARDENING** |
| State tree | Stage-centric | Stage-centric `progress.json` | Job-centric tillatt; manifest options | **OPEN:** P0.8.1 stage-centric control, fresh tree allowed |
| Progress | Flere markers | minimal progress | artifact-primary; validators/reconcile | **INHERITED + HARDENING:** ingen `_DONE`-teater |
| Expected jobs | Input/markers | plan | Finalizer må derive fra frozen plan | **DERIVED-HARDENING** |
| Rendering | P0.7 SDT fill→unwrap→LO | gjenbruk med kirurgisk templateendring | Legacy assets må reviewes; LO headless unverified current machine | **USER-CURRENT + VERIFIED baseline:** reuse candidate, target-machine spike obligatorisk før adoption |
| Content controls | 17/7 plain SDTs, unwrapped before LO | planlagt reuse | Generic research warning | **VERIFIED-P0.7 dominates generic warning:** ikke forkast uten lokal fail |
| CV page budget | <=2 hard i P0.7 finalizer | 1/2 dynamisk; >2 → CHECK | Hard-vs-soft review | **INHERITED/HARDENED:** soft writing/page target; overflow gir review, ikke sannhetskorrupsjon |
| Letter page | <=1 hard | <=1 target | Mechanical-vs-soft skille | **HARDENING:** behandle som writing/render review target med eksplisitt absolute safety bound om nødvendig |
| Portal limits | Hard | hard | 15% tolerance avvist | **HARDENING:** eksakt hard når portaloutput finnes |
| LO invocation | per doc/job i baseline | behold enkel rendering | ett isolert conversion transaction/job anbefalt; ingen daemon | **DERIVED-HARDENING**, test target Windows |
| Human approval | Ja | Ja | Eksplisitt | **USER-CURRENT hard boundary** |
| Auto submission | Nei | Nei | Eksplisitt nei | **USER-CURRENT hard non-goal** |
| Routine human confirmations | Noe mulig | minimeres | Eksplisitt unngå | **USER-CURRENT** |
| Prompt budget | 12 chats + reruns | 15 standard | normal total ~20–25, ingen absolutt ceiling | **USER-CURRENT:** økonomisk envelope, ikke stage count |
| Pilot | Controlled fixture only i release | real ~8-job pilot definert | opptil 3–4 high-value prelock tests; historical anchors dårlige | **USER-CURRENT + INHERITED:** små beslutningstester først ved behov, deretter real cluster pilot |
| Pilot quality metric | Ikke real | Q_happy + Top80 | small-n Top6/Top7/all sensitivity | **DERIVED-HARDENING** |
| Human time metric | Ikke komplett | edit time | total handling time | **DERIVED-HARDENING + USER target 10–20 min/submitted** |
| Reuse legacy tree | Ja | migrasjon | Ikke nødvendig | **USER-CURRENT:** ingen backward compatibility-plikt |
| Reuse legacy assets | release assets | byte-identical/reuse-with-verification | kun etter eksplisitt review/adaptation/optimization/polish | **USER-CURRENT** |

Denne matrisen viser hvorfor «P0.9 = nyeste dokument» ville være en dårlig mergealgoritme. På enkelte felt er P0.8.0 fortsatt det høyeste gyldige punktet; på andre har senere brukerpolicy eller P0.8.1-hardening overtatt.

---

# 12. Dokument-for-dokument: kausal sammenheng i P0.8+-korpuset

Tabellen under er ikke bare kronologi; den viser **hva hvert dokument tilfører den kumulative state-maskinen**.

| Dokument | Rolle i evolusjonen | Autoritetsnivå | Hva det faktisk endrer / tilfører |
|---|---|---|---|
| `Canonical_Conversation_KB_improvement_and_brainstorming_model_chat.md` | P0.7 audit + overgang | Historisk/decision evidence | Identifiserer konkrete P0.7-feil og, viktigst, brukerens målskifte fra uniform robusthet til `Q_happy`/strong-majority |
| `Jobbsøk_26 Intensjonsprofil.pdf` | Produktkonstitusjon/intensjonsprofil | Høy designkontekst, ikke release | Samler North Star, sannhet, persuasion, human-role og kosthierarki; 3-stage som hypotese |
| `Jobbsok_26_LLM_Context_Reference.md` | Kompakt maskinlesbar intent-reference | Derivert, ikke release | Samme prinsipper i mer effektiv runtime-/reviewform |
| `Jobbsok_26_P0.7-P0.8_Selective_Quality_Redesign_integration_summary.md` | Historisk chatrekonstruksjon | Meta-evidens | Bevarer hvordan P0.8 ble utviklet; stopper før final norm |
| `Canonical_Conversation_KB_external_review_model.md` | Ekstern konvergens | Nær-final, men supersedert | Gir en svært utviklet 3-stage/15-chat-modell; enkelte mekanismer senere ryddes opp |
| **P0.8.0 normative spec** | Arkitektur-release | **Siste formelt adopterte arkitektur** | Fastsetter 3-stage Sol→Terra→Sol, ~5×8, 15 chats, 2 scripts, READY/CHECK/RERUN, dynamic CV, partial success, free final writer |
| `Jobbsok_26_P0.7_to_P0.8_architecture_redesign_integration_summary.md` | Terminalhistorikk | Meta-evidens | Bekrefter at final P0.8.0 faktisk ble produsert/verifisert og at P0.7 fortsatt var executable baseline |
| `jobbsok_26_overordnet_systemanalyse.html` | Systemreview | Advisory | Argumenterer for å fryse produktarkitekturen og gjøre kirurgiske avklaringer før build |
| Claude critical review | Uavhengig contract review | Advisory | Finner input/state/schema/routing/pilot-hull |
| Gemini critical review | Uavhengig second opinion | Advisory | Finner overlappende og nye schema/render/phrase-drift-problemer |
| Cross-model addendum | Adjudikering | Sterk advisory | Sorterer ekte funn fra overengineering; avviser bl.a. YAML/auto-fit/5-gram/portal tolerance |
| Deep Research P0.8 | Ekstern evidens | Empirisk/advisory | Tester antakelser om context, portaler, LO, security; støtter KISS men gjør flere detaljer betingede |
| **Consolidated preimplementation review** | P0.8.1 contract hardening | `NON_NORMATIVE_UNTIL_ADOPTED` | CR-01…CR-25: gjør P0.8 implementerbar og målbar uten å redesigne produktet |
| `Brainstorm_Brief.md` | Reopen design space | **NON-NORMATIVE** | Spør om P0.8.1 fortsatt er optimal gitt ny info; åpner product/context/personality/state/strategy forks |
| `brainstorm_review.md` | Option-space strukturering | **NON-NORMATIVE** | DC-1…7, N-01…06, K-bundles; pruner svake alternativer, men velger ikke arkitektur |
| `P0.9_prep_package.md` | Uncertainty-reduction v1 | Prep | Bygger questionnaire, lokal prep og external research plan før final architecture |
| `P0.9_prep_package(1).md` | Uncertainty-reduction v2 | Prep, nyere | Erstatter researchdelen med sterkere Deep Research brief; **ekte revisjon, ikke kopi** |
| P0.9 prep integration summaries | Chatkronologi | Meta-evidens | Slår fast at P0.8 er siste adopterte norm og P0.9 fortsatt er decision-ready-but-undecided |
| Norwegian application research summary | Research launch record | Meta-evidens | Viser hvilke portal/render/ATS-spørsmål som ble sendt ut; inneholder ikke i seg selv svarene |
| Full P0.9 External Evidence Report | External facts | Empirisk/advisory | Long-context, model/context risk, chat-vs-API JSON, portalvarians, LO/security; lukker noen premisser, ikke DC-valgene |
| `Personality.md` | Ny interpretiv source | Source, ikke fact authority | Gjør personality/authenticity til konkret mulig input fremfor abstrakt idé |
| `Personality_P0.9_Framework_Context.md` | Runtime-adaptasjon | Proposal | Foreslår facet-interface/stage handoff; bare optional toggle er senere user-locked |
| BAR evidence report | Candidate fact-maintenance side stream | Research/source proposal | Kan forbedre `Work_experience.md` senere, men endrer ikke current production authority automatisk |
| **Latest broad integration summary** | Terminal state reconstruction | Høy provenance-verdi | Fanger eksplisitte brukerbeslutninger D-001…D-049 og bekrefter: ingen final P0.9 architecture/build ennå |

## 12.1 Den faktiske evolusjonsgrafen

```text
P0.7 release (IMPLEMENTED, testet på fixtures)
    |
    +--> konkret audit av runtime/QA/schema/layout
    |
    +--> USER GOAL SHIFT: strong-majority / Q_happy
             |
             v
        P0.8 design convergence
             |
             +--> intent/context profiles
             +--> external review
             v
        P0.8.0 FINAL NORMATIVE SPEC
        (3 stages, Sol→Terra→Sol, ~5×8, 15 chats, 2 scripts)
             |
             +--> critical reviews (Claude/Gemini)
             +--> cross-model adjudication
             +--> external/deep research
             v
        P0.8.1 CONTRACT-HARDENING
        (CR-01…25; NON-NORMATIVE_UNTIL_ADOPTED)
             |
             v
        P0.9 exploratory reopening
             |
             +--> Brainstorm Brief
             +--> DC/N/K option-space review
             +--> prep package v1→v2
             +--> external evidence
             +--> Personality source/runtime candidate
             +--> latest user questionnaire/decisions
             v
        CURRENT TERMINAL STATE
        = no final P0.9 architecture selected
        + substantial later user policy
        + mature hardening candidates
        + open forks still requiring lock
```

## 12.2 Den viktigste ikke-lineære egenskapen

Korpuset er **ikke** en lineær serie av specs. Det er tre parallelle spor etter P0.8.0:

1. **Contract hardening:** gjør eksisterende P0.8 mekanisk tryggere og implementerbar.
2. **Product/architecture reopening:** spør om deler av P0.8 bør forenkles eller bygges annerledes i P0.9.
3. **Evidence/context enrichment:** external research, Personality og candidate-source review.

Et senere dokument i spor 3 har derfor ingen automatisk rett til å overskrive en normativ regel i spor 1 eller P0.8.0. Bare eksplisitt beslutning eller direkte kausal refinement gjør det.

---

# 13. Fullstendig utledet «latest-developed current target»

## 13.1 Status og navngivning

Denne seksjonen er **ikke** en påstand om at prosjektet historisk har godkjent eller implementert «P0.9 final».

Den mest presise etiketten er:

> **Jobbsøk_26 — DERIVED CURRENT TARGET after P0.7 / P0.8.0 / P0.8.1-hardening / P0.9 decision-basis**

Den består av:

- senere eksplisitte brukerbeslutninger der de finnes;
- ellers siste normative P0.8-regel;
- direkte P0.8.1-hardeninger der de reparerer et konkret hull uten å gjøre et uløst produktvalg;
- åpne P0.9-forks eksplisitt markert som åpne, med siste normative kontrollvariant bevart.

Dette gir en **komplett og konsistent måltilstand uten å forfalske prosjektets beslutningshistorikk**.

---

## 13.2 Produktdefinisjon

**USER-CURRENT**

Jobbsøk_26 er et privat, lokalt, manuelt operert og gjenbrukbart system for **én kandidat**. Det skal brukes over flere jobbsøkerbatches, potensielt over lang tid, men skal ikke generaliseres til et fler-kandidat-SaaS-/produktproblem.

Systemets oppgave er å transformere en menneskelig godkjent og normalt frosset batch av omtrent 40 stillinger til sannferdige, strategisk sterke og arbeidsgiverbrukbare søknadspakker med så lite menneskelig arbeid som mulig uten å kompromittere sluttkvalitet.

Systemet skal **ikke**:

- finne eller søke på stillinger automatisk som del av core runtime;
- kontakte arbeidsgivere;
- sende søknader;
- gjøre irreversible handlinger på kandidatens vegne;
- omskrive canonical candidate truth under et production run;
- optimalisere alle stillinger likt dersom ressursene heller bør brukes på den sterke majoriteten;
- bygge generell agent-/DB-/vector-/router-infrastruktur uten dokumentert kvalitetsgevinst.

Mennesket har alltid siste approval og submission.

---

## 13.3 Mål- og prioriteringsfunksjon

### Hard constraints

**USER-CURRENT**

1. Sannhet / factual identity.
2. Employer usability / package integrity.
3. Human final authority / no automatic submission.

Ingen sannhetsrisiko kan forsvares av høyere persuasion eller lavere arbeid.

### Truth-safe optimaliseringsrangering

**USER-CURRENT**

Når alternativer begge er sannhetssikre:

1. **Sluttpakkekvalitet / interview probability**
2. **Lavt menneskelig arbeid**
3. **Rask/enkel implementering**
4. **Modellkostnad**
5. **Reversibility**

Dette overskriver eldre heuristikker der reversibility/KISS kunne dominere mer.

### Distribusjonsmål

**USER-CURRENT + INHERITED-P0.8**

P0.8s `Q_happy` er fortsatt den beste eksplisitte formaliserte kvalitetsfunksjonen:

```text
Q_happy = (median(q) + mean(top_80_percent(q))) / 2
```

Den senere brukerpolicyen spesifiserer intensjonen enda tydeligere:

- omtrent **30 sterke pakker av ~40** er et godt resultat;
- svak hale kan få targeted rerun;
- enkelte svake/rare cases kan droppes eller håndteres separat;
- systemet skal ikke ødelegge median/top-end ved å overinvestere i nederste hale.

`Q_happy` er dermed fortsatt gyldig som produkt-/pilotmål, men må ikke bli en mekanisk «score the model while writing»-mekanisme.

---

# 14. Canonical source-of-truth og run-freeze

## 14.1 Kandidatmyndigheter

**USER-CURRENT**

Følgende tre filer er current factual authorities og immutable under production:

- `Work_experience.md`
- `Education.md`
- `Other_high_value_information.md`

CV-baseline og alle runtime-derivater er sekundære produkter.

Ingen:

- Personality-fil;
- BAR research report;
- tidligere CV;
- assistant memory;
- strategy;
- package draft;

får etablere nye kandidatfakta uten støtte i authority-laget.

## 14.2 Claim-/evidence-regel

**INHERITED-P0.8 + DERIVED-HARDENING**

Hver material employer-facing påstand skal kunne spores til:

- source file;
- source heading/section;
- eventuelt stabil evidence/claim-ID der den finnes;
- korrekt lifecycle (`CURRENT`, `HISTORICAL`, `CONTEXT_ONLY`, etc. der source-formatet støtter det);
- claim ceiling / formulering som ikke går lenger enn evidensen.

Final writer har lov til å velge **annen** sann evidence enn strategy foreslo. Derfor må final package sine `used_evidence_refs` representere **faktisk** sluttinnhold, ikke bare upstream planning.

## 14.3 Run freeze

**USER-CURRENT + DERIVED-HARDENING**

Normalt production-flow:

1. Human approves batch.
2. Candidate authorities er CURRENT.
3. Ingest validerer canonical intake.
4. Ved vellykket ingest fryses run-input.
5. En immutable `context_snapshot.json` eller funksjonelt tilsvarende manifest lagrer hashes/versions/paths for alt run-critical materiale.

Senere jobbendringer er exception path, ikke normal mid-run mutation.

### Static invalidation classes

**DERIVED-HARDENING / N-01**

Freezeobjektet bør klassifisere dependencies minst som:

- `SOURCE_TRUTH`
- `WRITING_POLICY`
- `RENDER_ASSET`
- `SCHEMA`

En endring skal rapportere hvilken scope som er stale. Ingen automatisk «smart invalidation engine» er nødvendig; formålet er deterministisk observability.

---

# 15. Canonical intake og required-output-modell

## 15.1 Batch authority

**DERIVED-HARDENING**

Det bør finnes ett canonical machine-readable batch-/job-input før produksjon. P0.8s `batch_plan.json` er nærmeste normative startpunkt, men P0.8.1s viktigste forbedring er å fjerne redundante og konfliktbare outputsignaler.

Per jobb skal canonical state representere minst:

```json
{
  "job_id": "...",
  "cluster_id": "...",
  "employer": "...",
  "title": "...",
  "unit": null,
  "reference": null,
  "language": "nb-NO",
  "required_outputs": ["CV", "APPLICATION"],
  "vacancy_source": "...",
  "vacancy_hash": "..."
}
```

`required_outputs` er den beste hardeningformen fordi den kan uttrykke CV/application/portal uten redundant `channel` + booleans som kan være uenige.

**Viktig P0.9-open fork:** dersom portal senere eksplisitt detach-es fra core, skal `PORTAL` ikke late som et core required output; portal workflow kan i stedet ha egen downstream input/state. Intakeformatet må derfor finaliseres etter product-boundary-valget.

## 15.2 `job_identity`

**INHERITED-P0.8 + HARDENING**

`job_identity.json` skal være deterministisk derivert/validert fra canonical intake og vacancy — ikke en konkurrerende sannhetskilde. Den bør inneholde stabile runtimefelter som:

- job/batch/cluster IDs;
- employer/title/unit/reference;
- language;
- required outputs;
- exact portal questions/limits dersom portal er core;
- source path/hash;
- document date hvor relevant.

Schema- og set-equality-validering må sikre at cluster-/jobplan nøyaktig matcher frozen approved set.

---

# 16. Runtime-topologi

## 16.1 Tre semantic stages

Ingen senere autoritativ beslutning erstatter P0.8s tre-stage-arkitektur. Den er derfor den **gjeldende derived control architecture**.

### Stage 1 — Decision Architecture

**INHERITED-P0.8**

- Modell: **Sol Max**.
- Input: vacancy/job identity først; deretter relevante candidate authorities/policies.
- Arbeidsmønster: candidate-blind employer/problem model først som **PROTOCOL**, ikke påstått security/isolation boundary; deretter candidate-aware strategy.
- Output: en job-specific strategy med valgt professional identity, employer thesis, evidence pair/support, objection/reframe, motivation bridge, channel allocation og writer instructions.
- Skal ikke skrive ferdig søknadspakke.

### Stage 2 — Native Package Writer

**INHERITED-P0.8**

- Modell: **Terra Max**.
- Input: vacancy, frozen identity, strategy og eksakt kandidat-evidence som trengs.
- Oppgave: skrive komplett draft package i naturlig norsk, med dynamic CV, application og eventuelle core portal answers.
- Skal ikke opptre som egen reviewer/judge.

### Stage 3 — Final Writer & Selective Review

**USER-CURRENT + INHERITED-P0.8**

- Modell: **Sol Max**.
- `ELASTIC` authority innen truth constraints.
- Leser vacancy/identity først som en independence/read-order-protokoll, deretter upstream artifacts.
- Kan endre:
  - headline;
  - professional identity;
  - strategy;
  - evidence pair;
  - employment override IDs/bullets;
  - CV/application struktur;
  - argument allocation;
  - portal answers;
  - hele teksten.
- Kan hente targeted authority evidence som Stage 1/2 overså.
- Må oppdatere `used_evidence_refs` til faktisk sluttpakke.
- Leverer `final_package.json` + `review.json`.

Stage 3 skal **ikke** bindes av P0.7s mutable-draft/evidence-lock-feil. Upstream strategy er advisory planning, ikke factual ceiling.

## 16.2 Clustering og chat count

**INHERITED-P0.8 + USER-CURRENT economics**

Normal control:

- ~40 jobs;
- ~5 clusters;
- ~8 jobs/cluster;
- normalt 6–10, standard max ~10;
- samme cluster brukes gjennom de tre core stages;
- ett stage-cluster = én manuelt initiert modellchat;
- jobs behandles sekvensielt i chatten uten routine human confirmations.

Det gir **15 core stage chats**.

Den senere brukerbeslutningen om **~20–25 prompts som normalt totalbudsjett** betyr ikke at stagecount skal økes til 20–25. Den gir headroom til:

- high-value prelock tests;
- targeted RERUNs;
- eventuelle exceptional cases;
- uten at man må bygge en ny semantic stage.

Det finnes ingen absolutt prompt ceiling dersom dokumentert kvalitetsgevinst forsvarer mer, men terskelen for ytterligere prompts skal stige raskt.

## 16.3 Manual execution boundary

**USER-CURRENT**

Semantic stages skal normalt startes manuelt som separate model chats. Det skal ikke bygges et skjult API-/agent-orchestrator-system bare for å gjøre dem automatiske.

Lokale deterministic scripts/validators kan brukes av operator eller modellen på en lokal/Codex-capable surface.

---

# 17. Strategy contract

## 17.1 Gjeldende format

**INHERITED-P0.8 / OPEN P0.9**

`strategy.md` er siste normative control. Senere JSON/prose-alternativer er ikke valgt.

Det er derfor feil å bytte til JSON bare fordi Structured Outputs eksisterer i API-verdenen. I Work/chat må JSON fortsatt lokalt valideres, og research viser at «strict JSON guarantee» ikke kan antas.

## 17.2 Minimumsinnhold

Strategy skal minst etablere:

1. employer/problem model;
2. primary candidate identity;
3. explicit CV headline;
4. shortlist thesis / hvorfor kandidaten er relevant;
5. top evidence 1;
6. top evidence 2;
7. support evidence;
8. alternative route dersom hovedvinkelen er svak;
9. likely objection;
10. truthful reframe;
11. motivation bridge;
12. CV vs application allocation;
13. writer instructions;
14. priority/order metadata dersom funksjonen beholdes.

Hver evidence block skal ha source/provenance og contribution logic, ikke bare et påstandsnavn.

## 17.3 Lengde

**OPEN**

- Siste normative target: ca. 900–1400 ord; soft max ca. 1800.
- Senere review anbefaler ca. 400–1000 for mindre context anchoring/bloat.

Ingen senere user-decision låser kompresjonen. Derfor skal implementation bruke P0.8-control eller teste compact strategy som et lite high-value experiment før endelig lock.

---

# 18. Package schema og dynamic CV

## 18.1 Package authority

**INHERITED-P0.8**

Et package artifact skal inneholde dynamisk content, ikke kopier av statiske CV-fakta.

Conceptual schema:

```json
{
  "schema_version": "...",
  "source_stage": "STAGE2_DRAFT | STAGE3_FINAL",
  "job": { "job_id": "...", "employer": "...", "title": "..." },
  "baseline_version": "...",
  "used_evidence_refs": [],
  "cv_overrides": {
    "headline": "...",
    "profile": "...",
    "key_competencies": [],
    "experience_overrides": []
  },
  "application": {},
  "portal_answers": []
}
```

Portalblokken er conditional på product-boundary-valget.

## 18.2 Dynamic CV surface

**INHERITED-P0.8 + USER PERMISSION**

Første current target kan med fordel begrense dynamic CV til:

- headline;
- profile;
- key competencies;
- employment bullets.

Dette er nok fleksibilitet til å endre candidate framing vesentlig uten å gjøre CV-en til et fullstendig fri-form-dokument.

### Employment override semantics

**DERIVED-HARDENING**

Hvis en employment entry overrides, skal dens dynamic bullet-array være **full replacement** for den renderte bulletseksjonen, ikke uklare partial patches som kan gi blandet gammel/ny argumentasjon.

Always-include chronology/static dates/titles kommer fra baseline/source, ikke LLM-pakken.

## 18.3 Explicit headline

**INHERITED-P0.8**

P0.7 manglet et eksplisitt dynamic headline-felt og måtte indirekte utlede identity. P0.8s eksplisitte headline er en klar kvalitetsforbedring og skal beholdes.

---

# 19. Application og portal

## 19.1 Application

**INHERITED-P0.8**

Application skal:

- være native norsk, ikke «oversatt engelsk»;
- være persuasion-first men truth-bounded;
- komplementere CV i stedet for å repetere den;
- prioritere 2–3 mest sannsynlige employer pain points/selection criteria fremfor checklisteprosa;
- bruke konkret evidence der det øker employer confidence;
- unngå jantelovsbrudd/inflatert selvros;
- være kort nok til faktisk rekruttererbruk.

P0.7s søknadsmaster og P0.8s renderingstilnærming gir fortsatt et godt fysisk utgangspunkt.

## 19.2 Portal — eksplisitt åpent produktvalg

P0.8.0 integrerer portal answers i core package. Senere review og brukerbeslutninger gjør følgende klart:

- portal prevalence antas lav (~20 %) med lav confidence;
- portal answers **kan** skilles ut som downstream workflow;
- rare/nonconforming cases kan håndteres separat;
- real vacancy inventory bør avgjøre dette.

Derfor er current derived state:

> **OPEN P0.9 boundary.** Inntil eksplisitt valgt annerledes er P0.8s integrerte portalmodell control-fallback, men den må ikke omtales som «latest user-selected P0.9 design».

Hvis integrert:

- exact field/question IDs må være unike;
- exact char limits er hard mechanical constraints;
- ingen 15 % tolerance;
- outputs må valideres deterministisk.

Hvis detached:

- core producerer godkjent CV + application først;
- downstream portal step leser frozen vacancy portal fields + approved final package;
- den kan ikke introdusere nye candidate claims uten authority support;
- den får egen validator/state og påvirker ikke core package readiness med mindre portal faktisk er required for submission.

---

# 20. Review, READY/CHECK/RERUN og partial success

## 20.1 Review-status

**INHERITED-P0.8 + DERIVED-HARDENING**

Det skal fortsatt være bare tre operator-facing statuser:

- `READY`
- `CHECK`
- `RERUN`

Ingen confidence score, LLM-as-judge-poeng eller ornamental QA-rangering skal inn i core.

### Semantikk etter repair scope

- **READY:** ingen identifisert issue som krever menneskelig innholdsbeslutning eller separat rewrite.
- **CHECK:** lokalt/avgrenset forhold mennesket realistisk kan kontrollere/reparere raskt, f.eks. page/layout edge, ambiguity eller en konkret minor issue.
- **RERUN:** problemet er så sentralt at pakken bør få en ny one-job final-writing pass fremfor at mennesket skal omskrive den.

Review reasons: korte, maskinlesbare reason codes + maks få konkrete reasons.

## 20.2 RERUN-kontrakt

**DERIVED-HARDENING**

RERUN bør være:

- Sol Max;
- én jobb;
- egen chat;
- targeted vacancy + relevant authorities + siste package/review;
- ikke full cluster rerun;
- kan gjøre full truth-bounded rewrite.

Resultatet erstatter bare den jobben og skal gjennom samme deterministic finalization/validation.

## 20.3 Partial success

**INHERITED-P0.8**

En problemjobb skal ikke blokkere resten av batchen. Runtime skal kunne levere READY/CHECK packages og markere enkelte jobber FAILED/RERUN separat.

Final batch status kan følge en deterministisk precedence, eksempelvis:

```text
FAILED > DELIVERED_RERUN > DELIVERED_CHECK > DELIVERED_READY
```

men statusnavn skal ikke forveksles med package-quality score.

---

# 21. Deterministisk validation og repair

## 21.1 Mechanical vs semantic hard

**DERIVED-HARDENING**

Validators skal primært kontrollere ting kode faktisk kan vite sikkert:

### Mechanical hard

- schema;
- required fields;
- set equality;
- IDs;
- duplicate portal question IDs;
- exact char limits;
- source hashes/freeze integrity;
- path/file existence;
- package→template mappings;
- no unresolved placeholders;
- no private/internal IDs i leveranse;
- expected job count;
- rendered output existence;
- no residual content controls etter finalization hvis samme teknik brukes.

### Semantic hard policy

Sannhet er hard constraint, men **ikke** fordi en regex kan bevise semantisk truth. Semantic verification skal komme fra:

- authority discipline;
- evidence refs;
- model instructions;
- final writer targeted source checking;
- human review.

Ikke bygg falsk sikkerhet ved å kalle heuristiske semantic checks «hard validators».

## 21.2 Stage completion

**DERIVED-HARDENING**

Et stage/job er ikke `completed` før den relevante deterministic validatoren returnerer exit 0.

`_DONE.md`-fil eller substring-markører alene er utilstrekkelig.

## 21.3 Repair protocol

**DERIVED-HARDENING + USER permission**

Når execution surface faktisk kan kjøre lokalt verktøy i samme session:

1. validator fail;
2. modellen leser presis feil;
3. reparerer samme artifact;
4. revaliderer;
5. maks **2 repair attempts**;
6. tredje fail → record job/stage failure og gå videre der partial-success-reglene tillater det.

Dette er bounded deterministic repair, ikke auto-agentloop.

**Surface caveat:** plain ChatGPT Work/chat kan ikke uten videre antas å ha Codex-local filesystem/tool semantics. Final implementation må eksplisitt definere om validatoren kjøres av Codex/local session, operator, eller en annen supported surface.

---

# 22. Runtime state og filstruktur

## 22.1 Hva som er låst

**USER-CURRENT**

- lokal Windows repo/filesystem er runtime authority;
- fresh P0.9 tree er tillatt/ønsket;
- backward compatibility med P0.7/P0.8 directory tree er ikke et krav;
- state skal være filbasert og auditabel;
- semantic stages manuelt initiert;
- deterministic scripts små og eksplisitte.

## 22.2 Hva som fortsatt er åpent

Eksakt **stage-centric vs job-centric** tree er ikke valgt.

P0.8/P0.8.1-control har:

- batch/cluster planning;
- stage-specific artifact trees;
- minimal `progress.json`.

P0.9 review åpner en mer job-centric/manifest-basert layout.

### Derived requirement uansett tre

Tree-valget må tilfredsstille:

1. én frozen canonical job-set authority;
2. artifact-primary state;
3. expected-set reconciliation;
4. ingen konkurrerende progress-sannheter;
5. enkle deterministic validators;
6. partial success per job;
7. tydelig stale-scope dersom static dependency endres;
8. enkel human navigasjon;
9. ingen runtime DB nødvendig.

En mulig fresh tree som oppfyller dette — **illustrativ, ikke historisk user-selected** — er:

```text
Jobbsok_26/
  authority/
    Work_experience.md
    Education.md
    Other_high_value_information.md
  policy/
    SETTINGS.md
    writing_policy.md
    [optional personality source/reference]
  templates/
    CV_MASTER.docx
    APPLICATION_MASTER.docx
  schemas/
  scripts/
  runs/
    <batch_id>/
      manifest.json
      context_snapshot.json
      clusters/
      jobs/
        <job_id>/
          vacancy/
          strategy/
          draft/
          final/
          render/
          review/
      run_log.csv
```

Det er fullt mulig å implementere samme kontrakter stage-centric. Tree-valget skal derfor ikke avgjøres av estetikk, men med en billig no-model spike som måler code/path complexity og operator usability.

---

# 23. Personality — full current kontrakt uten å overpåstå

## 23.1 Låst boundary

**USER-CURRENT**

Personality skal være **optional** og styres via `SETTINGS.md` eller funksjonelt tilsvarende toggle.

## 23.2 Authority

**STRONG DERIVED RULE**

Personality er interpretiv context, aldri factual/claim authority.

Den kan hjelpe med:

- genuine positioning;
- tone;
- misread prevention;
- preference for how real facts uttrykkes;
- motivation framing.

Den kan ikke gjøre «system thinker», «leader», «AI specialist» eller andre employer-facing claims sanne uten authority evidence.

## 23.3 Åpne runtimevalg

Følgende er **ikke** user-locked:

- default ON/OFF;
- eksakt PF-01…PF-20-contract;
- 0–3 facets;
- om Sol skal velge facets og Terra få distilled handoff;
- om funksjonen faktisk øker blind vurdert pakkequality.

Siden brukeren aksepterer opptil 3–4 små high-value prearchitecture tests, er personality en legitim paired-test-kandidat dersom architecture model mener beslutningen kan påvirke mange jobber.

Off-mode må alltid være fullverdig: ingen pipelinekomponent kan kreve personality for å fungere.

---

# 24. Evidence navigation/context prep — hva bør være core?

## 24.1 Current control

**INHERITED-P0.8**

Modellene kan lese canonical authority direkte og gjøre targeted retrieval basert på vacancy/strategy.

## 24.2 Deterministisk evidence index

**PROVISIONAL STRONG CANDIDATE / N-03**

En lossless navigation index med f.eks.:

- `evidence_id`;
- source file;
- heading/path;
- section hash;
- approximate size;
- lifecycle;
- claim ceiling;

kan redusere navigation cost uten å filtrere eller score evidence.

Viktig designregel: indexen skal **ikke** være retrieval authority og skal ikke skjule source. Den er bare kart.

Dette er langt tryggere enn embedding/vector/cheap-model relevance filter fordi den ikke introduserer relevance gate eller hidden loss.

## 24.3 Luna/prep

**PROVISIONAL/TEST-ONLY**

Luna/cheap-model prep kan teoretisk spare Sol/Terra context/arbeid, men external research gjør det klart at lang context + billigere modell kan miste eller ankre informasjon. Derfor:

- ikke globalt corpus-filter;
- ikke relevance tiers som hard gate;
- hvis testet: advisory/job-local slice;
- alltid mulig for Sol/Terra å gå direkte til canonical source;
- mål Stage 3 escape/repair, ikke bare tokenbruk.

N-02 `evidence_outside_prep` kan være en nyttig observability-metrikk hvis prep innføres, men den er meningsløs dersom direct retrieval er eneste mode.

---

# 25. Priority A/B — separer tre konsepter

P0.8 brukte priority til både order og microrefinement. P0.8.1/review identifiserer confounding.

Current derived analysis skiller:

1. **Prediction:** forventet payoff/fit/priority.
2. **Order:** når jobben behandles i clusteret.
3. **Treatment:** hvor mye ekstra modellarbeid den får.

**OPEN P0.9**

Sterkeste simple candidate er DC-6b:

- behold prediction label;
- bruk den eventuelt til order;
- ikke automatisk koble label til ekstra compute/microvariation i core.

Dette bevarer nyttig sequencing uten å gjøre pilotresultater umulige å tolke. Men siden user ikke eksplisitt har valgt 6b, er P0.8 A/B-control formelt siste normative behavior frem til architecture lock.

---

# 26. DOCX/PDF rendering — baseline-evidens + senere hardening

## 26.1 Hva P0.7 allerede beviser

**VERIFIED-P0.7**

CV-masteren:

- 17 plain Word content controls;
- 17 unike CV-tags;
- 0 data bindings;
- 0 tables;
- 0 text boxes;
- 0 drawings;
- enkel flow;
- header/footer med kandidatnavn/page number.

Application-masteren:

- 7 content controls / 6 unike tags;
- 2 tabeller;
- 0 data binding;
- ingen drawings/text boxes.

`finalize.py` fyller SDT-innhold og **unwrap-er content controls før LibreOffice**. Validatoren feiler dersom `w:sdt` står igjen.

Dermed er det teknisk feil å generalisere external community warning om content controls til «P0.7-template er ubrukelig». LibreOffice trenger ikke tolke disse controls som runtime data-bindingmekanisme.

## 26.2 Hva som likevel må verifiseres på nytt

**USER-CURRENT + RESEARCH**

- LibreOffice er ikke installert på nåværende target machine ennå;
- vanlig DOCX→PDF fungerer, men `soffice --headless` er ikke verifisert;
- legacy assets må eksplisitt reviewes/adapted/optimized/polished før P0.9 reuse.

Derfor er en **template/render spike på target Windows** en høy-prioritert prelock/implementation gate.

## 26.3 Rendering contract

**INHERITED-P0.8 + HARDENING**

Finalizer skal:

1. lese validated final package;
2. merge static baseline + dynamic overrides deterministisk;
3. fylle templates;
4. unwrap/rydde temporary controls hvis dagens teknik beholdes;
5. validere DOCX-struktur;
6. kjøre headless LO i isolert profile/context;
7. produsere PDF;
8. kontrollere sideantall/basic render sanity;
9. markere READY/CHECK/RERUN/FAILED uten å stoppe andre jobs.

Ingen LO daemon eller kompleks pooling trengs.

## 26.4 P0.8 layoutforbedring

Behold:

- explicit headline;
- sparse CV kan være 1 side;
- normal/dense CV 2 sider;
- ikke tving svakt innhold til 2 sider;
- >2 sider gir normalt CHECK/review i stedet for skjult content deletion;
- application ca. 1 side target.

## 26.5 Parseability-risk som fortsatt bør testes

CV-body er allerede uvanlig parseability-vennlig: ingen body tables/textboxes/drawings. Et konkret mulig risikopunkt er kandidatnavn/kontaktinfo i header. Test med faktisk text extraction/portal hvis mulig før template redesign; ikke gjør speculative layoutendring uten signal.

---

# 27. Security og untrusted vacancy content

**RESEARCH-BACKED HARDENING**

Vacancy text og eksterne dokumenter er untrusted content, ikke instructions.

Pipeline skal derfor:

- behandle stillingsannonsen som data;
- eksplisitt ignorere instruksjoner i vacancy som forsøker å styre modellen/systemet;
- aldri la vacancy endre canonical authority/policies/scripts;
- kjøre lokale scripts med minste nødvendige filesystem scope;
- unngå unødvendig network access i validation/render;
- kreve human approval før ekstern irreversible action;
- logge artifact provenance fremfor å stole på modellens hukommelse.

Dette krever ikke et stort security framework; det er en system-/prompt-/filesystem boundary.

---

# 28. Pilot- og evalueringssystem

## 28.1 Før architecture lock

**USER-CURRENT**

Opptil ca. **3–4 små high-decision-value tester** er akseptable. Ikke kjør dem bare fordi de finnes.

Rangert etter beslutningsverdi ut fra dagens åpne hull:

1. **Actual vacancy inventory / channel census** — ofte analyse, ikke modelltest; avgjør portal/language/rare-case boundary.
2. **Target Windows template/headless-LO spike** — direkte blocker for rendering reuse.
3. **Tree/manifest no-model spike** — hvis stage-centric vs job-centric påvirker implementasjon vesentlig.
4. Én av strategy-format/personality/context-prep paired tests **bare** dersom final architecture model vurderer at fork-en er load-bearing.

Historiske søknader/interview conversion skal ikke brukes som sterk benchmark; brukeren har eksplisitt sagt at de er for lite sammenlignbare.

## 28.2 Før full batch

**INHERITED-P0.8 + HARDENING**

Kjør først en liten live-model smoke, deretter en reell clusterpilot på omtrent 8 representative stillinger.

### Human quality

For hver package:

- human 1–10 quality;
- submit-ready yes/no;
- factual correction needed yes/no;
- total human handling minutes;
- review status;
- Stage 3 material delta;
- position in cluster;
- rerun needed/result.

### Small-n distribution metrics

For `n=8`:

- raw scores;
- median;
- mean(all 8);
- mean(top 7);
- mean(top 6);
- `Q_happy` med eksplisitt definert top-set;
- bottom-2 details.

Dette unngår at «Top80» later som en presis estimand på lite n.

### Review calibration

`TailRecall20` eller tilsvarende skal forstås som **self-triage calibration**, ikke independent QA:

- hvor ofte systemet selv merker reelt svak tail;
- hvor mange gode pakker som unødvendig sendes til CHECK/RERUN;
- human review load.

### Cost/time

Mål:

- model credits per chat/run — ikke falsk per-job-presisjon dersom måleenheten ikke støtter det;
- total human handling time, ikke bare ren editor time;
- wall clock for deterministic finalization/render hvor nyttig.

### Current human envelope

**USER-CURRENT**

- ca. 5–10 timer/uke tilgjengelig for review+submission;
- ca. 10–20 minutter human tid per submitted package er akseptabelt;
- første batch ønskes i 1–4 uker, med enkelte relevante deadlines under 2 uker.

Dette gjør lang prearchitecture-perfeksjonering kostbar.

---

# 29. Implementation strategy — beste nåværende sekvens

Denne sekvensen kombinerer P0.8s normative buildplan, P0.8.1s bedre vertical-slice-logikk og siste P0.9-policy om rask første batch.

## Gate 0 — lås bare de beslutningene som faktisk er load-bearing

Før kodebredden økes:

- analyser faktisk vacancy batch;
- velg portal core vs detached;
- bekreft language scope;
- velg execution surface for same-session validator repair;
- gjør target-Windows LO/template spike;
- velg stage-centric vs job-centric state hvis en rask spike viser reell forskjell;
- bestem om strategy/personality/context forks må testes nå eller kan stå på control/default.

**Stopping rule:** hvis et valg ikke realistisk endrer første-batch kvalitet, human load eller en irreversible implementation decision, defer det.

## Wave 1 — authority + canonical contracts

- arkiver P0.7 uendret som releasebevis;
- kopier/versjoner current 3 candidate authorities;
- lag canonical intake/required-output contract;
- schema-valider batch/cluster/job set;
- freeze `context_snapshot` med hashes;
- implementer static invalidation reporting;
- etabler settings boundary, personality toggle selv om default fortsatt må velges.

## Wave 2 — one-job deterministic spine

Før modelstages:

- ingest én jobb;
- validate identity/input;
- aksepter en fixture `final_package.json`;
- merge til DOCX;
- render PDF;
- validate output;
- record review/delivery state.

Målet er å bevise hele mekaniske banen før 40-jobbstate finnes.

## Wave 3 — template/render hardening

- kjør real target Windows/LO;
- test P0.7 masters før redesign;
- implementer P0.8 headline + 1/2-page behavior;
- verify content-control unwrap;
- test selected text extraction/ATS-risk pragmatisk;
- dokumenter exact package→template mapping.

## Wave 4 — stage contracts + validators

Implementer:

- Stage 1 strategy contract;
- Stage 2 draft package schema;
- Stage 3 final package/review schema;
- evidence ref sync;
- validator exit-0 completion rule;
- bounded repair protocol på chosen execution surface;
- RERUN contract.

## Wave 5 — multi-job/cluster mechanics

- frozen cluster plans;
- set equality;
- sequential jobs per cluster chat;
- artifact-primary state;
- partial success;
- expected-job reconciliation;
- run log.

## Wave 6 — Tier-0/Tier-1 QA + live two-job smoke

- schema/unit tests;
- duplicate IDs;
- freeze mismatch;
- failed job continuation;
- render edge cases;
- evidence ref drift fixture;
- two real jobs med live Sol/Terra/Sol.

Reparer kontrakter før full cluster.

## Wave 7 — release documentation

- `START_HERE.md`;
- operator runbook;
- exact model/settings per stage;
- validation/repair instructions;
- no-submit boundary;
- release manifest/hashes;
- known limitations.

## Wave 8 — real 8-job pilot

Kjør full clusterpilot og evaluer distribution, human load og failure modes.

## Wave 9 — rest of batch

Bare hvis pilot ikke avdekker load-bearing problem. Kirurgiske fixes foretrekkes fremfor ny redesignrunde.

---

# 30. Avgrenset «do not build»-liste

Basert på hele P0.8+-korpuset er følgende fortsatt utenfor første current target med mindre nye data viser tydelig gevinst:

- full API orchestration;
- multi-agent framework;
- vector DB / embeddings / semantic cache;
- global cheap-model relevance filter;
- automated employer research pipeline;
- LLM-as-judge core gate;
- hidden automatic rerun loops;
- per-job authority-file copies;
- YAML dual truth;
- heavyweight database/state service;
- plugin architecture;
- LO daemon/pooling;
- automated submission;
- generalized multi-candidate product abstractions;
- sophisticated optimization av rare channels som kan håndteres separat.

Dette er ikke ideologiske forbud. De må ganske enkelt slå den senere brukerens eksplisitte prioriteringsrangering før de fortjener implementation cost.

---

# 31. Åpne pre-lock-beslutninger — det som faktisk mangler før en sann «P0.9 final» kan skrives

Dette er den komplette listen over load-bearing eller potensielt load-bearing forks som materialet fortsatt ikke lukker.

| # | Beslutning | Current control/fallback | Ledende kandidat | Hva som bør avgjøre |
|---:|---|---|---|---|
| 1 | Portal i core? | P0.8 integrert | Detached post-package | Faktisk vacancy inventory + human friction |
| 2 | Language scope | nb/en supported | nb-NO-only first | Faktisk batch |
| 3 | Runtime tree | Stage-centric P0.8.1 | Fresh job-centric manifest | Cheap no-model spike / operator clarity |
| 4 | Strategy artifact | Markdown | JSON+prose eller compact MD | 2-job paired test kun hvis material |
| 5 | Strategy length | 900–1400 soft | 400–1000 | Quality/context test |
| 6 | A/B semantics | P0.8 prediction+order+treatment | Prediction/order only | Architecture judgment/pilot interpretability |
| 7 | Deterministic evidence index | Direct source retrieval | N-03 lossless index | Implementation cost vs navigation gain |
| 8 | Luna prep | Ingen | Advisory job-local slice | Local paired test; external research cautions |
| 9 | Personality default | Ingen feature P0.8 | Optional ON/OFF | Paired quality test or user preference |
| 10 | Personality interface | N/A | distilled 0–3 facets | Bare hvis feature viser gevinst |
| 11 | Validator execution surface | Operator/local scripts | Same-session Codex repair | Actual Work/Codex workflow |
| 12 | Exact cluster sizing/order | ~5×8 | Same unless pilot says otherwise | Real batch + early/late quality drift |

Ingen andre åpne designspørsmål i korpuset fremstår som nødvendige før første implementation pass.

---

# 32. «Latest-developed» full system contract — kondensert normativ visning

Dette er den mest praktiske én-sides kontrakten som kan avledes uten å late som åpne P0.9-valg er tatt.

## Product

- **Single candidate, reusable local system** over multiple batches.
- Normal batch ≈40 human-approved/frozen vacancies.
- Optimize strong majority; ~30 strong packages is acceptable target distribution.
- Truth + employer usability hard constraints.
- Human owns final approval/submission; no auto-submit.
- Rare cases may be handled outside core.

## Authorities

- `Work_experience.md`, `Education.md`, `Other_high_value_information.md` are CURRENT factual authorities.
- Immutable during run.
- Personality/research/drafts cannot create facts.
- Run snapshot hashes all critical inputs/assets/contracts.

## Execution

- Windows/local repo/files authority.
- Distinct manually initiated semantic chats; no normal API orchestrator.
- **3 core stages:** Sol Max strategy → Terra Max writer → Sol Max elastic final.
- ~5 clusters × ~8 as current empirical default.
- One cluster chat processes jobs sequentially without routine human confirmations.
- Normal total prompt envelope ~20–25 for ~40 jobs, with no absolute ceiling if quality justifies it.

## Stage 1

- Vacancy-first employer/problem understanding.
- Candidate-blind first pass is protocol, not security boundary.
- Candidate-aware strategic evidence selection.
- Produces strategy, not package prose.

## Stage 2

- Native Norwegian package drafting.
- Dynamic CV: headline/profile/competencies/employment bullets.
- Application complements CV.
- Portal if product boundary retains it.

## Stage 3

- Sol Max ELASTIC within truth.
- Can reconstruct strategy/package and retrieve alternate canonical evidence.
- Final evidence refs must match actual content.
- Produces final package + READY/CHECK/RERUN review.

## Mechanical runtime

- Canonical validated intake/required-output state.
- Freeze after successful ingest.
- Small deterministic code surface.
- Artifact-primary state; no marker-file theatre.
- Stage complete only after validator exit 0.
- Bounded repair; partial success.
- Expected-job reconciliation against frozen plan.

## Rendering

- P0.7 Word masters are **reuse candidates, not blind carry-forward**.
- Baseline fill→unwrap technique is technically credible and locally evidenced.
- Target Windows/headless LibreOffice spike is mandatory before release.
- Preserve P0.8 direct headline + flexible 1/2-page CV behavior.
- Exact portal limits hard; prose/page targets mostly soft/reviewable.

## Review

- READY/CHECK/RERUN only; no confidence score.
- One-job Sol Max RERUN for rewrite-level defects.
- Human review target roughly 10–20 min/submitted package.

## Pilot

- Up to 3–4 small high-decision-value prelock tests.
- Two-job live smoke before real cluster.
- ~8-job cluster pilot before full batch.
- Measure quality distribution, human handling time, factual corrections, review calibration, Stage3 deltas and run-level model cost.

## Open before formal P0.9 lock

- portal boundary;
- first-release language scope;
- exact runtime tree;
- strategy format/size if worth testing;
- A/B role;
- optional evidence index/Luna prep;
- personality default/interface;
- exact validator execution surface;
- target-machine rendering result.

---

# 33. Hva P0.7-mappen endrer i tolkningen av hele P0.8+-historien

P0.7-builden gjør fire ting som de abstrakte senere rapportene ikke kunne gjøre alene.

## 33.1 Den setter et ekte engineering floor

Vi vet nå at prosjektet allerede hadde:

- schemas;
- release manifest;
- deterministic scripts;
- identity validation;
- fixture E2E;
- rendering path;
- controlled failure handling;
- Word masters;
- tests.

P0.8/P0.9 skal derfor vurderes som **migrasjon fra fungerende system**, ikke greenfield idémyldring.

## 33.2 Den skiller verified weakness fra speculative weakness

Eksempel: P0.7 har faktisk mutable-draft/evidence-lock-problem i architecture/validation logic; det er en reell redesign-driver.

Derimot er «Word content controls er sikkert ubrukelige» ikke støttet av baseline. Faktisk implementation unwrap-er dem før LO og har ingen data bindings.

## 33.3 Den viser at P0.8s viktigste endring er kvalitetsallokering, ikke bare KISS

P0.7 var allerede forholdsvis enkel. P0.8s store verdi er derfor:

- færre semantic passes;
- sterkere modell på strategy og final;
- final writer elasticity;
- job-local strategy/evidence;
- strong-majority objective;
- selective review/rerun;
- dynamic CV identity.

Det er en **quality architecture**, ikke bare en code cleanup.

## 33.4 Den skjerper reuse-standarden

Siste brukerpolicy sier at legacy assets bare kan reuse-es etter review/adaptation/optimization/polish. P0.7-baselinen lar dette gjøres selektivt:

- candidate authorities: retain/current;
- schemas: redesign where contract flaws exist;
- `advance.ps1`: architecture-obsolete under P0.8 three-stage topology;
- `ingest.py`: logic concepts reusable, contract changes required;
- `finalize.py`: rendering/merge techniques highly reusable, schema/status behavior needs redesign;
- Word masters: strong reuse candidates, but require P0.8 headline/layout/target-machine verification;
- P0.7 tests: test patterns/fixtures reusable, expected contracts must update.

---

# 34. Verification record for denne analysen

## 34.1 P0.7 actual build

Jeg har ikke basert P0.7-delen på summaries alene.

Utført mot opplastet release:

- pakket ut releasen;
- lest release docs, schemas, scripts, stage instructions og tests;
- kjørt unittest-suiten;
- kontrollert dokumenterte hashes mot faktiske files;
- strukturinspisert begge Word masters;
- renderet CV/application og visuelt kontrollert sider;
- inspisert `finalize.py` sin content-control/LibreOffice-bane.

Resultat:

```text
34 tests discovered
32 PASS
2 SKIP/BLOCKED (PowerShell runtime unavailable in current container)
0 FAIL
```

De fem dokumenterte SHA-256-hashene for candidate authorities/Word masters matchet releaserapporten.

Dette validerer **release artifact consistency og controlled fixture behavior**, ikke real frontier-model package quality.

## 34.2 Hva P0.7 fortsatt ikke beviser

- real Terra/Sol chats på faktiske vacancies;
- 40-jobb batch behavior;
- real target Windows PowerShell execution i denne analysen;
- dagens target Windows headless LibreOffice;
- employer portal parsing;
- interview conversion;
- P0.8/P0.9 implementation.

## 34.3 P0.8+ evidence

P0.8+-analysen har eksplisitt separert:

- normative P0.8 spec;
- meta/integration summaries;
- advisory critical reviews;
- external research;
- non-normative P0.8.1 hardening;
- non-normative P0.9 option-space;
- senere eksplisitte brukerbeslutninger.

Dette reduserer risikoen for at «nyere fil» blir forvekslet med «ny autoritet».

---

# 35. Residual risks og hostile-review pass

En kritisk reviewer bør fortsatt utfordre følgende før implementation lock.

## 35.1 «Derived hardening» er analytisk, ikke historisk release authority

CR-01…CR-25/N-01/N-04 osv. er svært sterke forbedringer, men P0.8.1 sier selv `NON_NORMATIVE_UNTIL_ADOPTED`. Rapporten inkluderer bare de direkte, ikke-kontroversielle kontrakthardeningene i current target og merker dem som derived.

## 35.2 Product boundary er ikke avgjort

Å skrive en «final P0.9 spec» som enten inkluderer eller fjerner portal nå ville være overclaim. Real vacancy inventory er den enkle manglende inputen.

## 35.3 Tree/state er fortsatt et ekte valg

Fresh runtime er user-approved, men fresh ≠ job-centric. Ikke gjør et estetisk treevalg om et 30-minutters no-model spike kan vise complexity.

## 35.4 Work vs Codex capability må konkretiseres

User har Work/Desktop + Codex/local tooling, men manual stage chats og same-session validator execution kan bety ulike surfaces. Architecture må beskrive operatørflyten eksplisitt; ellers blir N-04 pseudo-automation.

## 35.5 P0.7 renderbevis må ikke overgeneraliseres

Det er sterkere enn generic content-control warnings, men dagens maskin mangler verifisert headless LO. Target spike gjenstår.

## 35.6 `Q_happy` er evalfunksjon, ikke online judge

Ikke bygg en scoremodell som optimaliserer proxy under writing. Human pilot ratings er fortsatt hovedsignal.

## 35.7 P0.9 research hadde input gaps

External Evidence Report manglet flere sentrale project artifacts da den ble skrevet. Den er nyttig til facts, men ikke kompetent til å erklære endelig DC/N bundle.

## 35.8 Latest integration summary er provenance-rich, men ikke selv en architecture spec

Den registrerer user decisions korrekt, men «D-xxx» skal anvendes på relevante granularitetspunkter, ikke kopieres ukritisk inn som ny runtime.

---

# 36. Endelig konklusjon

Den mest robuste rekonstruerte historien er:

> **P0.7 var den siste faktisk bygde og kontrollerte releasen.** Den var allerede relativt enkel og engineering-messig reell, men hadde kvalitets-/authority-/state-hull og var ikke live-pilotert med frontiermodellene. Brukeren endret deretter selve optimaliseringsmålet fra batch-uniformitet til sterk-majoritet (`Q_happy`). Dette utløste **P0.8.0**, en komplett normativ redesign til tre stages, Sol→Terra→Sol, ca. 5×8 clusters, 15 core chats, to scripts, dynamic CV, elastic final writer, partial success og READY/CHECK/RERUN. P0.8.0 ble aldri implementert. Cross-model review og research produserte deretter en svært moden **P0.8.1 contract-hardening**, men den ble eksplisitt aldri adoptert som norm. P0.9-fasen åpnet designrommet kontrollert, samlet ekstern evidens og personality-context og innhentet senere brukerbeslutninger som endret generality, tidsbudsjett, promptbudsjett, reuse-policy og tradeoff-rangering. Den fasen sluttet fortsatt før en final P0.9 architecture-definition/build.**

Dermed er den beste nåværende tekniske måltilstanden **ikke** «P0.8.0 uendret», og heller ikke «en ferdig P0.9». Den er:

> **P0.8s tre-stage quality architecture + direkte P0.8.1 contract hardening + senere user-current P0.9 policy, med eksplisitte åpne forks bevart som forks i stedet for å bli gjettet bort.**

Det er den høyeste informasjonsfronten materialet faktisk støtter.

For å gjøre dette til en ekte **P0.9 FINAL_NORMATIVE_SPECIFICATION** trengs ikke en ny bred researchrunde. Det trengs først og fremst at de få åpne punktene i §31 låses — helst ved faktisk vacancy inventory, target render spike og eventuelt én eller to små tester — og deretter at en architecture-definition model skriver én ny canonical spec som eksplisitt adopterer de valgte hardeningene og løser open forks.

