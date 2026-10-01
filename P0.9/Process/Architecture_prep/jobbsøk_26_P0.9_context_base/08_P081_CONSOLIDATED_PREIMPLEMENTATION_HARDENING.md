---
document: "Jobbsøk_26 P0.8 — Consolidated Pre-Implementation Review"
artifact_role: "canonical consolidated review + patch recommendation"
status: "NON_NORMATIVE_UNTIL_ADOPTED"
target_release: "P0.8.1 contract-hardening before implementation"
primary_specification: "Jobbsok_26_P0.8_architecture_and_specification.md"
consolidates:
  - "Jobbsok_26_P0.8_deep_critical_review_and_improvement_brainstorm.md"
  - "Jobbsok_26_P0.8_addendum_cross_model_consolidation.md"
source_context:
  - "Jobbsok_26_P0.8_architecture_and_specification.md"
  - "Jobbsok_26_preference_and_instruction_profile.md"
  - "Canonical_Conversation_KB_implementing_model_chat.md"
  - "Canonical_Conversation_KB_improvement_and_brainstorming_model_chat.md"
  - "Canonical_Conversation_KB_external_review_model.md"
  - "Jobbsok_26_P0.7_Release(1).zip"
  - "Jobbsok_26_P0.8_kritisk_review_og_forbedringsbrainstorm_Gemini.md"
  - "Jobbsok_26_P0.8_kritisk_review_og_forbedringsbrainstorm_claude.md"
language: "nb-NO"
target_readers:
  - "Vegard"
  - "GPT-5.6 Sol Max implementation model"
  - "future reviewer/maintainer"
---

# Jobbsøk_26 P0.8 — konsolidert pre-implementeringsreview

## 0. Dokumentets rolle og lesekontrakt

Dette dokumentet er den **sømløst konsoliderte versjonen** av det opprinnelige dybdereviewet og det senere kryssmodell-addendumet. Formålet er å bevare all beslutningsrelevant informasjon, begrunnelse, konfliktanalyse og forbedringssignal, samtidig som redundans fjernes og alle senere konfliktløste konklusjoner uttrykkes én gang i sin gjeldende form.

Dokumentet er **ikke i seg selv normativt før det eksplisitt adopteres**. Frem til da er `Jobbsok_26_P0.8_architecture_and_specification.md` den kanoniske P0.8-spesifikasjonen. Dersom dette reviewet adopteres som siste pre-implementeringspatch, bør implementeringsprompten eksplisitt angi at:

```text
P0.8-spesifikasjonen gjelder som base.
De adopterte MUST/P0-patchene i dette dokumentet overstyrer motstridende P0.8-tekst.
DEFERRED/REJECTED-forslag skal ikke implementeres.
Historiske reviewforslag som er eksplisitt konfliktløst her skal ikke gjeninnføres.
```

### 0.1 Prioritetsmerking i dette dokumentet

| Markør | Betydning |
|---|---|
| **P0 / MUST** | Bør avklares eller patches før full implementering; ellers må builderen gjette i en kontrakt som påvirker korrekthet, state, måling eller operatørflyt. |
| **P1 / SHOULD** | Høy forventet nytte og lav/moderat kost; bør normalt inn før pilot eller full batch. |
| **P2 / PILOT** | Skal måles eller vurderes empirisk, ikke låses arkitektonisk nå. |
| **DEFERRED** | Reelt mulig forbedringsområde, men skal ikke bygges uten et konkret aktiveringssignal. |
| **REJECTED** | Forslaget adresserer enten feil problem, skaper mer kompleksitet enn verdi, eller kolliderer med autoritativ produktfilosofi. |

### 0.2 Konfliktregel

Når en eldre anbefaling og addendumets senere vurdering kolliderer, beholdes **problemet og resonnementet**, men bare den sist konfliktløste beslutningen brukes som implementeringsdirektiv. Viktige eksempler:

- tidligere `Top-7 av 8` er **erstattet** av `bottom_k=2 / top_k=6` som primær diskret Top-80-regel ved `n=8`, med obligatorisk sensitivitet mot Top-7 og alle åtte;
- forslag om opptil `15 %` portaloverskridelse som soft issue er **forkastet**; arbeidsgiverens faktiske portalgrense er hard for den leverbare teksten;
- YAML-frontmatter, typografisk auto-fit og 5-gram-sentinel er **ikke** del av anbefalt P0.8-implementering;
- per-jobb authority-hasher erstattes av ett **batch-level context snapshot**.

---

# 1. Teknisk hoveddom

## 1.1 P0.8 har riktig produktarkitektur; siste runde bør være kontrakthardening, ikke redesign

P0.8s fundament bør beholdes. Den viktigste designseieren er at systemet nå eksplisitt optimaliserer **arbeidsgiverpakken** fremfor prosessuniformitet:

```text
Truth hard
+ strongest truthful strategy
+ natural Norwegian persuasion
+ low human rewrite burden
+ selective tail handling
> uniformity, defensive QA and architecture machinery
```

Den trestegs flyten er godt tilpasset modellrollene:

```text
Stage 1 — Sol Max
Employer problem + candidate identity + evidence selection + decision architecture

Stage 2 — Terra Max
Complete native-Norwegian package + first editorial self-edit

Stage 3 — Sol Max
Independent final view + strategic correction + final persuasion + READY/CHECK/RERUN

Deterministic layer
Identity + schemas + baseline merge + exact limits + rendering + partial success

Human
Final semantic/factual authority + submission
```

Dette bør **ikke** utvides med fjerde standardstage, LLM-as-judge, automatisk retry, multi-agent-debatt, vector/RAG-plattform, semantic repair loop, similarity-motor eller automatisk innsending.

## 1.2 Det som fortsatt er svakt er hovedsakelig grensesnittene mellom gode komponenter

Den gjenværende risikoen ligger mindre i topologien enn i steder hvor to deler av systemet møtes og begge er rimelige hver for seg:

1. **operatorinput → `job_identity.json`** er ikke fullt definert;
2. **kanalenum → faktiske leveranser** representeres redundant;
3. **batchplan → freeze** mangler et operativt, reproduserbart snapshot;
4. **Stage 1 → `cluster_plan.json`** mangler maskinell kontrakt;
5. **`progress.json` → artifacts** kan drive fra forventet jobbsett;
6. **semantisk truth boundary → Python-hard-fail** er ikke helt separert;
7. **package JSON → Word-master tags** mangler én entydig kildekartlegging;
8. **Stage 1/Stage 3 epistemisk read order** beskrives sterkere enn den faktiske chat-isolasjonen tillater;
9. **reviewstatus → menneskelig handling** trenger en reparasjonsbasert boundary;
10. **pilot-KPI-er → beslutninger** trenger bedre små-n-, tids- og kostregnskap;
11. **implementeringsbølger → reell læring** bør flytte vertical slice tidligere;
12. **«to scripts» → intern kodeorganisering** bør defineres som to operatør-CLIs, ikke et forbud mot små interne moduler.

Dette er akkurat den typen feil som er billige å løse i spesifikasjonen og dyre å la GPT-5.6 Sol Max improvisere under bygging.

## 1.3 Anbefalt sluttposisjon

**Implementer P0.8 etter én avgrenset P0.8.1-kontraktdiff.** Ikke gjør enda en generell arkitekturrunde etter dette. Den neste store informasjonskilden må være:

```text
working code
→ actual DOCX/PDF
→ two-job live developer smoke
→ one real ~8-job cluster
→ measured package quality + human handling + credits
```

---

# 2. Arkitektur som bør fryses uendret

Følgende valg er sterke nok til at de bør behandles som **frosset target architecture** med mindre implementeringen avdekker en faktisk blokkering.

## 2.1 Produktmål og quality distribution

Behold:

```text
Q_happy = (Median(q) + Mean(Top80%(q))) / 2
```

Formålet er ikke å gi alle 40 jobber identisk kvalitet. Systemet skal maksimere medianen og den sterke majoriteten, samtidig som en svak hale flagges billig og kan tas i separat RERUN. Dette er konsistent med den autoritative kosthierarkien:

```text
Human Effort
> Human Complexity
> LLM Complexity
> LLM Effort / credits
```

## 2.2 Tre standardstager

Behold:

- Stage 1: Sol Max;
- Stage 2: Terra Max;
- Stage 3: Sol Max;
- samme strategisk koherente klynge gjennom alle tre;
- ett jobbobjekt ferdigstilles/persisteres før neste jobb;
- rundt fem klynger med omtrent åtte jobber i første fullbatch;
- normalområde seks til ti, ikke et absolutt arkitektonisk optimum.

Klyngestørrelse er et **empirisk parameter**, ikke en doktrine.

## 2.3 Dynamic CV merge

Behold konseptet:

- baseline eier stabil kronologi og statiske fakta;
- modellene skriver bare headline, profile, competencies og relevante employment-bullet-overrides;
- full kronologi bevares;
- original profesjonell Word-master beholdes;
- Stage 3 kan forbedre dynamiske soner innen truth boundary.

Dette er en av systemets høyeste leverage-beslutninger: færre genererte fakta, lavere tokenmengde og mindre risiko for at modellene «rekonstruerer» datoer/roller.

## 2.4 Stage 3 som fri sluttforfatter

Behold at Stage 3 kan:

- endre headline;
- endre kandidatidentitet;
- bytte hoved-/støtteevidens;
- omfordele argumentet mellom kanaler;
- skrive fullstendig om svak draft;

så lenge påstandene fortsatt er intervju-forsvarlige fra autoritative kilder.

En blueprint er en sterk hypotese, ikke en kontrakt som beskytter middelmådighet.

## 2.5 Partial success

Behold per-jobb transaksjonalitet:

```text
DELIVERED_READY
DELIVERED_CHECK
DELIVERED_RERUN
FAILED
```

Én mekanisk feil skal ikke kaste 39 brukbare pakker. Batch exit code kan være nonzero samtidig som vellykkede outputs bevares.

## 2.6 Menneskelig sluttmyndighet og manuell innsending

Behold:

- mennesket som endelig faktavalidator;
- mennesket som endelig claim-strength-validator;
- menneskelig kvalitetsvurdering som eval-fasit;
- manuell submission;
- ingen employer contact/publication/profile mutation fra systemet.

---

# 3. Konsolidert endringsregister

Dette er den korteste komplette oversikten over anbefalt siste spesifikasjonsdiff.

| ID | Prioritet | Endring | Hvorfor |
|---|---|---|---|
| **CR-01** | P0 | Definer én kanonisk maskinlesbar jobb-/leveranseinput før ingest | `job_identity.json` kan ellers ikke bygges deterministisk fra nåværende `batch_plan.json` |
| **CR-02** | P0 | Fjern eller derivér redundant `channel`/`letter_required`/`portal_required`-state | hindrer inkonsistente representasjoner av samme leveransekrav |
| **CR-03** | P0 | Gjør freeze operativ med immutable `context_snapshot.json` | beskytter mot mid-run authority/baseline/policy/template drift |
| **CR-04** | P0 | Opprett `cluster_plan.schema.json` og set-likhetsregler | Stage 2/3 styrer etter en maskinkritisk fil som i dag bare har prosekontrakt |
| **CR-05** | P0 | Initialiser Stage 2/3-progress først når `cluster_plan` finnes; reconcile på continuation | unngår at `progress.next` følger gammel batchordre |
| **CR-06** | P0 | Finalizer må enumerere forventede jobber fra frozen plan, ikke oppdagede outputmapper | manglende final/review må bli synlig status, ikke forsvinne |
| **CR-07** | P0 | Skill mekanisk hard failure fra semantisk hard truth policy | Python kan ikke bevise unsupported claims bare ved string/schema checks |
| **CR-08** | P0 | Skill soft writing targets fra absolute schema bounds; portal limits er hard exception | unngår at «soft» kvalitetspreferanser blir skjulte hard failures |
| **CR-09** | P0 | Lås package→template source map | builderen skal ikke gjette hvilke baseline/packagefelt som fyller masterens content controls |
| **CR-10** | P1 | Operationaliser Stage 1/3 read-order som debiasingprotokoll, ikke «ekte isolasjon» | cluster-chat kan ikke kognitivt glemme tidligere kilder |
| **CR-11** | P0 | Eksplisitt full bullet-array replacement per `employment_id` | fjerner partial-merge-ambiguity |
| **CR-12** | P0 | `used_evidence_refs` MÅ reflektere faktisk final evidence | løser `skal`/`kan`-konflikt og bevarer provenance |
| **CR-13** | P0 | Definer READY/CHECK/RERUN etter reparasjonsomfang | gjør review handlingsbart og målbart |
| **CR-14** | P0 | RERUN = Sol Max, én jobb per separat chat | lukker modell-/efforthullet i den svakeste halen |
| **CR-15** | P0 | Legg til chat-/stage-level `PILOT_RUN_LOG.csv` | platform cost oppstår per chat, ikke naturlig per jobb |
| **CR-16** | P0 | Lås small-n Top-80 og sensitivitet | pilotens KPI er ellers matematisk tvetydig |
| **CR-17** | P1 | Logg total human handling time i tillegg til edit time | edit-minutter alene undervurderer operatørkost |
| **CR-18** | P1 | Gjør Priority A/B-evaluering eksplisitt confounded | A får både tidlig posisjon og ekstra microvariation |
| **CR-19** | P1 | Én LibreOffice conversion-call per jobb + render wall-time | lavrisiko ytelsesgevinst uten ny dokumentservice |
| **CR-20** | P0 | Flytt one-job vertical slice og Tier-0-tester tidligere | beviser den vanskeligste mekanikken før store tokens brukes på releasepolish |
| **CR-21** | P1 | Definer to operator-facing CLIs, men tillat smale interne Python-moduler | hindrer både script-sprawl og kunstige monolitter |
| **CR-22** | P1 | Kryss-klynge human phrase/convergence spot-check | dekker en reell blindflekk uten similarity engine |
| **CR-23** | P0 | Stage completion krever standard validator exit 0 | schema/artifactfeil skal repareres før stage markeres complete |
| **CR-24** | P1 | Fjern optional Terra clustering-preflight fra FIRST_RUN_READY-scope | lav verdi, modellrollebrudd og unødvendig implementeringsscope |
| **CR-25** | P1 | Lås post-pilot A/B-/routing-decision rule | hindrer arkitekturendring fra ett støyete 8-jobbs signal |

---

# 4. P0 — Intake, identitet og leveransekontrakt

## 4.1 CR-01: `job_identity.json` mangler en fullt definert inputkilde

### Problem

P0.8 sier at ingest skal bygge `job_identity.json` fra `batch_plan.json` og operatorinput, og at employer, title, unit, reference, language, channel og portalgrenser ikke skal kreativt infereres senere. Samtidig er `batch_plan.json` i den normative spesifikasjonen primært et batch-/cluster-membership-objekt med jobb-ID-er, ikke en komplett maskinlesbar identity intake.

Dermed mangler systemet den deterministiske overgangen:

```text
human-approved vacancy + human channel decision
→ canonical machine-readable intake
→ immutable job_identity.json
```

Uten patch må implementeringsmodellen velge mellom å:

- parse employer/title/channel fra vacancy;
- lese fritekst i `notes.md`;
- utvide `batch_plan.json` på egen hånd;
- introdusere en ekstra inputfil;
- eller la Stage 1 «bekrefte» identiteten senere.

Alle er plausible; bare noen er ønskelige.

### Anbefalt kontrakt

Gjør `batch_plan.json` til den **eneste human-authored machine authority** for job membership og required outputs. Eksempel på ønsket prinsippform:

```json
{
  "schema_version": "0.8.1",
  "batch_id": "B01",
  "approved": true,
  "jobs": [
    {
      "job_id": "B01_J001_example",
      "employer": "Example AS",
      "title": "Senioranalytiker",
      "unit": null,
      "reference": null,
      "language": "nb-NO",
      "required_outputs": ["CV", "APPLICATION"],
      "portal_questions": [],
      "document_date": null
    }
  ],
  "clusters": [
    {
      "cluster_id": "B01_C01_analysis",
      "jobs": ["B01_J001_example"]
    }
  ]
}
```

Dette er et **konseptuelt eksempel**, ikke krav om akkurat feltnavnene. Det normative poenget er:

> Ingest skal aldri måtte «forstå» hvilke employer-facing deliverables som kreves. Operatoren låser dem maskinlesbart før ingest.

`notes.md` kan fortsatt gi fritekstkontekst, men skal ikke være den skjulte kilden til maskinkritisk identity/deliverable-state.

## 4.2 CR-02: Redundant channel-state bør normaliseres

### Nåværende spenning

P0.8 har flere representasjoner av det samme:

- `channel ∈ {CV_ONLY, CV_APPLICATION, PORTAL_ONLY, HYBRID}`;
- `letter_required`;
- `portal_required`;
- portal questions;
- faktisk presence/null i package (`application`, `portal_answers`);
- `cv_overrides` er samtidig alltid required i packagekontrakten.

Dette gir mulige ugyldige kombinasjoner:

```text
channel=CV_ONLY + letter_required=true
channel=PORTAL_ONLY + cv_overrides required
portal_required=false + portal_questions nonempty
HYBRID + application=null
```

### Anbefalt løsning

Ha **én kanonisk required-output-representasjon**. Reneste form er:

```text
required_outputs = subset of {CV, APPLICATION, PORTAL}
```

Derivér alt annet fra denne:

```text
CV in required_outputs          <=> cv_overrides required/non-null
APPLICATION in required_outputs <=> application required/non-null
PORTAL in required_outputs      <=> portal answers must cover all required questions
```

Hvis det er viktig å beholde `channel` av hensyn til lesbarhet eller migrering, skal det være et **derived field** med deterministisk mapping og validatorassertion — aldri en andre autoritet.

Tilsvarende kan `letter_required` og `portal_required` beholdes som derived compatibility fields i 0.8.1 dersom det reduserer migreringsarbeid, men de skal ikke kunne redigeres uavhengig.

### `notes.md`

Kanal-/deliverable-overstyring via `notes.md` er bare gyldig **før ingest**. Etter at identity er generert/frosset, er notes ikke en latent mutasjonskanal.

---

# 5. P0 — Freeze, provenance og runtime state

## 5.1 CR-03: Freeze må bli et faktisk maskinelt tidspunkt

### Problem

P0.8 bruker språk som:

- batch plan fryses når første Stage 1-chat starter;
- identity fryses etter ingest;
- en endring etter freeze krever operator handling, ny hash og revalidation.

Men «første Stage 1-chat starter» er en menneskelig hendelse uten deterministisk maskinsignal, og den omtalte «nye hash»-mekanismen er ikke komplett spesifisert.

### Anbefalt freeze-semantikk

Gjør **successful ingest of an approved batch** til freeze boundary.

```text
Human edits inbox/batch_plan/notes
→ ingest --source ...
→ validate
→ normalize
→ create identities
→ create context snapshot
→ mark runtime batch frozen
→ Stage 1 may start
```

Etter dette:

- Stage-modeller leser frozen runtime inputs;
- kildene skal ikke muteres midt i batchen;
- en eksplisitt operatorendring krever re-ingest/re-freeze;
- påvirkede stageartefakter skal ikke silently blandes med ny grunnlagsversjon.

## 5.2 Batch-level `context_snapshot.json`

Opprett ett generated runtime-artefakt:

```text
runs/<batch_id>/context_snapshot.json
```

Minimumsinnhold:

```text
snapshot_id
created_at
specification_version
batch_plan_sha256
candidate_authority hashes
CV_BASELINE hash/version
WRITING_STANDARD hash/version
PERSUASION_CALIBRATION hash/version
MODEL_ROUTING hash/version
schema hashes/versions
Word-master hashes
stage-instruction hashes
```

### Hvorfor batch-level, ikke per job

De tre candidate authorities, baseline, stage policy og masters er globale for batchen. Å kopiere samme hashes inn i 40 `job_identity.json` gir redundant state, større driftflate og dårligere signal/kompleksitetsforhold.

`job_identity.json` kan eventuelt peke på `snapshot_id`.

### Runtime-regel

Ved stage-start, continuation eller finalization:

```text
current relevant file hashes
!= frozen snapshot
→ stop with explicit RUN_CONTEXT_CHANGED
→ operator chooses explicit re-freeze/restart
```

Dette skal **ikke** bli en provenance-platform eller event store. Ett JSON-objekt og en enkel hashcheck er tilstrekkelig.

## 5.3 CR-05: `progress.json` må følge den faktiske stageordren

P0.8 lar Stage 1 endre jobbrekkefølgen etter strategisk vurdering og skriver denne til `cluster_plan.json`. Hvis ingest samtidig preinitialiserer Stage 2/3 `progress.json` fra original batchordre, kan `remaining`/`next` være i konflikt med den planen Stage 2 faktisk skal følge.

### Anbefaling

- Ingest initialiserer Stage 1-progress.
- Stage 2-progress opprettes første gang Stage 2 starter, **etter** validert `cluster_plan.json`.
- Stage 3-progress opprettes første gang Stage 3 starter, også fra `cluster_plan.json`.
- Continuation rekonstruerer/reconcilerer status fra:
  1. expected job set;
  2. valid artifact presence;
  3. progress index.

`progress.json` er en recovery-indeks, ikke en selvstendig truth source.

## 5.4 CR-06: Expected-job reconciliation må være eksplisitt

Finalizer må aldri anta at «jobbene som finnes i Stage 3-output-mappen» er batchen.

### Normativ algoritme

```text
expected_jobs = frozen batch/cluster plan filtered by CLI scope

for each expected_job:
    require identity
    inspect expected final/review artifacts
    validate if present
    classify READY/CHECK/RERUN/FAILED

for any discovered output not in expected_jobs:
    surface CONFIG/ROGUE_OUTPUT issue
    never silently treat it as an approved job
```

Dette sikrer at:

- en manglende finalpakke ikke forsvinner fra rapporteringen;
- en halvkjørt cluster fortsatt kan finaliseres med partial success;
- `--job`, `--cluster-id` og batchmode har samme expected-set-semantikk;
- `check-only` kan vise både manglende og ekstra artefakter.

---

# 6. P0 — `cluster_plan.json` må bli en ekte kontrakt

## 6.1 CR-04: Maskinkritisk fil uten schema er unødvendig risiko

`cluster_plan.json` bestemmer:

- Stage 2-/Stage 3-rekkefølge;
- Priority A/B;
- hvilke jobber som inngår;
- hva `progress` skal forvente;
- grunnlaget for early/late-analysis.

Likevel har P0.8 fem JSON-schemas og ingen dedikert `cluster_plan.schema.json`.

### Anbefaling

Legg til:

```text
schemas/cluster_plan.schema.json
```

Minimumsregler:

```text
schema_version exact
batch_id exact
cluster_id exact
ordered_jobs nonempty
unique job_id
priority enum A|B
all batch-cluster jobs exactly once
no unknown job IDs
no duplicate order position
```

Eventuell kort rationale/variation note kan være med, men filen skal ikke bli et nytt blueprint.

### Cross-validation

Stage 1 completion krever:

```text
set(cluster_plan.job_ids) == set(batch_plan.cluster.job_ids)
```

Stage 2/3 completion og finalizer skal bruke samme forventede sett.

### Repository-konsekvens

Alle steder som sier «exactly five schemas» må oppdateres. **Antallet schemafiler er ikke en produktverdi i seg selv.** Riktig kontrakt er viktigere enn kosmetisk filminimalisme.

---

# 7. P0 — Truth: hva kode kan bevise og hva modeller/mennesket må eie

## 7.1 CR-07: Skill tre valideringsklasser

P0.8 har en riktig hard truth boundary, men enkelte formuleringer kan få en builder til å forsøke å gjøre semantiske faktafeil til deterministiske Python-gates uten en faktisk claim graph.

Den riktige modellen er:

### Klasse A — mekanisk/deterministisk hard failure

Kode kan faktisk bevise dette:

- invalid/unreadable JSON;
- schemafeil;
- wrong/mismatched job ID, employer, title eller frozen identity field;
- unknown `employment_id`;
- baseline version/hash mismatch;
- manglende required deliverable;
- portal answer over faktisk hard employer limit;
- duplicate/missing required portal question IDs;
- statiske kandidatfelt injisert i forbudt dynamisk struktur;
- kjent private/internal metadata leakage etter høy-presisjonsregler;
- missing/unreadable master;
- render/conversion failure;
- mistet static chronology i merged CV;
- expected-job-set mismatch.

### Klasse B — semantisk hard truth policy

Dette er fortsatt absolutt forbudt, men kan normalt ikke bevises av enkel deterministic code:

- unsupported personal ownership;
- team-resultat presentert som individuelt resultat;
- pilot presentert som production;
- funksjonelt ansvar oppgradert til formell tittel/mandat;
- udokumentert personnel responsibility;
- causal result/metric uten støtte;
- påstand som går utover claim ceiling.

Dette skal beskyttes av:

1. authority-bound stage instructions;
2. explicit evidence refs;
3. Stage 3 truth audit;
4. human final semantic/factual review.

Koden skal ikke late som den «verifiserer sannhet» når den bare verifiserer struktur/provenance.

### Klasse C — soft quality/review

- CV over ønsket sidebudsjett;
- application over omtrent én side;
- genericity;
- weak motivation;
- extensive Stage 3 rewrite;
- alternate valid evidence route;
- package similarity;
- phrase/convergence risk;
- layout balance.

Disse skal ikke gjøre en ellers sannferdig, sterk pakke mekanisk unusable.

---

# 8. P0 — Hard limits versus writing targets

## 8.1 CR-08: «Soft» i proseksjonen må ikke bli «hard» i JSON schema

Hvis spesifikasjonen omtaler for eksempel headline `15–140` som et **soft skriveintervall**, men schema bruker nøyaktig `minLength=15` og `maxLength=140`, er intervallet de facto hardt. Det samme prinsippet gjelder profile/application-lengder.

### Anbefalt trelagsmodell

| Type | Eksempel | Enforcement |
|---|---|---|
| **Employer/business hard limit** | portal `max_chars`/`max_words` | strict fail until deliverable fits |
| **Structural absolute safety bound** | runaway JSON string / unreasonable array count | generous schema bound |
| **Quality target** | headline target, profile target, ~1 page application, 1–2 page CV | stage instruction + soft review |

En writing target skal ikke være en tight schema gate med mindre det **bevisst** skal være et hardt produktkrav.

## 8.2 Portalgrensen er hard

Dette er en eksplisitt konfliktløst konklusjon.

P0.8s ordlyd om «mindre portalgrense» som soft issue er uheldig. Forslaget om å definere «mindre» som opptil 15 % overskridelse er også forkastet.

Arbeidsgiverens portal aksepterer ikke et over-limit svar fordi systemet kaller overskridelsen «minor».

### Normativ regel

```text
Employer-facing portal answer > declared hard limit
→ not DELIVERED_READY
→ finalizer hard failure for that required deliverable/job until answer is within limit
```

Hvis en lengre formulering er verdifull som privat arbeidsnotat, kan den bevares separat. Den faktiske `answer`-verdien som skal limes inn må være gyldig.

---

# 9. P0 — Dynamic CV merge og Word rendering

## 9.1 CR-11: Employment override er full replacement

Eksakt regel:

> Når `employment_overrides` inneholder en post for en `employment_id`, erstatter override-postens `bullets` hele `default_bullets`-arrayet for det arbeidsforholdet. Det finnes ingen posisjonell merge, append, implicit retention eller partial fallback. Når ingen override finnes, beholdes hele baseline-arrayet.

Konsekvens:

```text
baseline = 4 bullets
final override = 1 bullet
→ rendered employment = exactly 1 bullet
```

Et override-array med null bullets er invalid; maksimum følger packagekontrakten. Eldre employment overrides skal rendres i sitt definerte slot eller gi en eksplisitt mekanisk feil — aldri silently droppes for å redde sideantall.

## 9.2 CR-09: Package-to-template source map må spesifiseres én gang

P0.7 hadde faktisk, hardkodet renderlogikk som fylte masterens content controls. P0.8 endrer blant annet headline-semantikken, men spesifikasjonen bør eksplisitt låse alle source→tag mappings slik at builderen ikke må gjette.

Minimumskart:

| Word content control | Kanonisk kilde i P0.8 |
|---|---|
| `CV_FUNCTIONAL_IDENTITY` | `final_package.cv_overrides.headline` — **direkte**, ingen concat av competencies |
| `CV_PROFILE` | `final_package.cv_overrides.profile` |
| `CV_CORE_COMPETENCE` | `final_package.cv_overrides.key_competencies`, rendret med masterens eksisterende stil |
| `CV_CURRENT_ROLE_TOP_EVIDENCE` | effective merged bullets for baseline employment(s) eksplisitt mappet til current-role slot |
| `CV_EARLY_ROLE_EVIDENCE` | effective merged bullets for employment(s) eksplisitt mappet til early-role slot |
| `CV_RELEVANT_MASTER_SUBJECTS` | definert baseline education source; ikke modell-inferert uten eget overridefelt |
| `CV_RELEVANT_BACHELOR_SUBJECTS` | definert baseline education source; ikke modell-inferert uten eget overridefelt |
| `CV_SUPPORT_SECTION_1/2` | eksplisitt baseline/support mapping |
| `CV_OPTIONAL_PREVIOUS_EXPERIENCE` | baseline employment rows i definert previous-experience region |
| `CV_OPTIONAL_TRUST` | baseline trust/board data |
| `CV_OPTIONAL_LANGUAGES` | baseline language data |
| `APP_EMPLOYER` | frozen identity employer |
| `APP_UNIT_OPTIONAL` | frozen identity unit |
| `APP_DATE` | explicit document-date rule |
| `APP_JOB_TITLE` | frozen identity title |
| `APP_REFERENCE_OPTIONAL` | frozen identity reference |
| `APPLICATION_BODY` | opening + body paragraphs + closing fra final package |

### Render-slot-problemet

Builderen bør ikke spre hardkodede employment-ID-lister gjennom `finalize.py`. En enkel løsning er å legge et stabilt renderfelt i baseline, for eksempel:

```text
render_region = CURRENT_TOP | EARLY_EVIDENCE | PREVIOUS
```

eller én samlet baseline-level render map. Dette er mekanisk metadata, ikke kandidatfakta.

### Education-tagene

Hvis `CV_RELEVANT_MASTER_SUBJECTS` og `CV_RELEVANT_BACHELOR_SUBJECTS` faktisk skal være dynamisk jobbrelevante, krever det et eksplisitt `education_overrides`-design. P0.8 har ikke dette. Derfor bør de i 0.8.1 behandles som **stabile baselinefelter** eller renames for å unngå at builderen introduserer skjult modellseleksjon.

## 9.3 CR-19: LibreOffice — optimaliser prosessstart, ikke bygg en service

P0.7s converter starter en separat LibreOffice-prosess per dokument. For en jobb med CV + application betyr det minst to prosessstarter. På 40 jobber kan oppstartskost bli merkbar, selv om den ikke rettferdiggjør en persistent UNO-service.

### Anbefalt P0.8-implementering

Per jobb:

1. generer alle required DOCX til samme jobbtemp;
2. kall LibreOffice **én gang** med alle jobbens DOCX-filer;
3. bruk én isolert user/profile-tempcontext for jobben;
4. valider hver forventet PDF separat;
5. promover jobbens output atomisk først når alle required outputs er gyldige.

Logg:

```text
render_wall_seconds
converted_document_count
converter_timeout/failure
```

### Ikke bygg nå

- persistent LibreOffice daemon;
- UNO service;
- converter pool;
- cross-job background queue.

Aktiver først hvis målt render/rerender-tid faktisk blir en vesentlig del av operatørarbeidet.

## 9.4 Typografisk auto-fit er DEFERRED

Forslaget om å redusere paragraph spacing/line spacing 5–10 % når CV-en «nesten» går over to sider adresserer et reelt irritasjonsproblem, men er feil første løsning:

- linje-/tegnestimat predikerer ikke Word/LibreOffice-layout robust;
- dokumenter får skjult, ulik typografi;
- visuell QA blir vanskeligere;
- det kan gjøre en ellers profesjonell 3-siders CV mindre lesbar bare for å tilfredsstille en soft target.

Hvis pilotdata viser gjentatte near-overflow-caser, vurder én **preapproved COMPACT master/render profile** med visuelt verifisert design. Ikke kontinuerlig auto-fit.

---

# 10. Stage 1 → Stage 2: handoff uten ny redundant state

## 10.1 Bekymringen er reell: Markdown→JSON kan tape struktur

Stage 1 produserer `strategy.md`; Stage 2 skal gjøre strategien til strict `draft_package.json`. En semistrukturert Markdown-fil kan gi:

- mistet evidence priority;
- feil parsing av objection/reframe;
- uklart skille mellom main/support evidence;
- ekstra reasoning effort hos Terra;
- inconsistent `used_evidence_refs`.

## 10.2 YAML-frontmatter er likevel ikke anbefalt

Gemini-forslaget om machine-readable YAML-frontmatter i `strategy.md` har en intuitiv gevinst, men ville duplisere:

- identity;
- priority;
- headline;
- evidence pair;
- channel/deliverables;

som allerede finnes eller bør finnes i autoritative runtimeobjekter/strukturerte strategiseksjoner.

Det skaper et nytt spørsmålet: hvilken kopi vinner når YAML og Markdown divergerer?

### Bedre løsning

Behold `strategy.md`, men gjør kritiske seksjoner **semi-strukturelt entydige**:

```text
## PRIMARY CANDIDATE IDENTITY
Identity: ...
CV headline: ...

## MAIN EVIDENCE 1
Evidence ref: ...
Claim ceiling: ...
Employer bridge: ...
Channel role: ...

## MAIN EVIDENCE 2
Evidence ref: ...
Claim ceiling: ...
Employer bridge: ...
Channel role: ...

## OBJECTION AND REFRAME
Objection: ...
Reframe: ...
```

De eksakte labelene kan følge nåværende P0.8-headings; poenget er stabile labels + én betydning per label.

En validator kontrollerer **presence/uniqueness/known refs**, men gjør ikke semantisk parsing til et nytt schema.

---

# 11. Stage epistemics: behold debiasing, ikke påstå umulig isolasjon

## 11.1 CR-10: Stage 1 «candidate blind» er en read-order heuristic i en cluster-chat

Når samme Sol-chat prosesserer flere jobber, kan modellen ha sett candidate authorities under jobb 1 før den starter jobb 2. Den kan ikke faktisk «glemme» kandidaten.

Dermed bør Stage 1-kontrakten si:

> Candidate-blind Phase A er en **per-job debiasing protocol**, ikke fysisk context isolation.

### Operativ sekvens per jobb

1. åpne `job_identity` + vacancy (+ channel facts) først;
2. skriv/forplikt en bounded employer-side vurdering før kandidatoppslag;
3. åpne bare nødvendige candidate sources;
4. bygg candidate-aware strategy;
5. persistér jobben før neste.

Dette bevarer den kognitive fordelen uten å bygge en ekstra blind Stage 0.

## 11.2 Stage 3 «independent final view» har samme egenskap

Stage 3 skal først danne en egen end-state-vurdering før den leser strategy/draft. Det er riktig, men heller ikke ekte fysisk isolation når jobber behandles i samme chat.

### Operativ sekvens

1. åpne vacancy + frozen identity;
2. form en kort intern vurdering av employer problem, likely identity og evidence route;
3. først deretter åpne current job’s `strategy.md` + `draft_package.json`;
4. les targeted authority refs ved behov;
5. skriv final + review;
6. persistér før neste jobb.

Ikke opprett et nytt permanent «independent_view.json» med mindre pilot viser at protocolen ikke fungerer. Artefaktproliferasjon er ikke målet.

## 11.3 Hva piloten må teste

Fordi debiasing ikke kan garanteres av filstruktur alene, mål indirekte:

- Stage 3 strategy/evidence deltas;
- early-vs-late quality;
- repeated opening/headline patterns;
- human rewrite by job position;
- cross-cluster convergence.

---

# 12. P0 — Evidence provenance

## 12.1 CR-12: `used_evidence_refs` har én gjeldende modalitet

P0.8 bruker både «skal registrere» og «kan endres» om Stage 3s evidence refs. Dette må samles til én regel:

> `used_evidence_refs` MÅ representere den evidensen finalpakken faktisk bruker i sine materielle hovedpåstander. Stage 3 MÅ legge til nye refs når den introduserer/bytter hoved- eller støtteevidens, og MÅ fjerne refs som ikke lenger brukes dersom listen ellers ville være misvisende. Listen kan være uendret når evidensen faktisk er uendret.

Validatoren kan sjekke at refen finnes i frozen context/authority universe. Det er **ikke** semantisk claim-verification.

## 12.2 Strategy change skal ikke kreve «draft preservation»

Når Stage 3 velger en bedre gyldig evidence route:

- finalpakken vinner;
- refs oppdateres;
- review kan registrere strategy delta;
- Stage 3 skal ikke tvinges tilbake til Stage 1 bare fordi endringen er stor.

Dette er en sentral Selective Quality-endring fra tidligere streng stage immutability.

---

# 13. P0 — Review og RERUN som handling, ikke selvkritikk

## 13.1 CR-13: Definer status etter reparasjonsomfang

Issue-category alene er ikke nok. «Weak motivation» kan være én setning eller symptom på feil backbone. `CLAIM_STRENGTH` kan være ett verb eller et helt feil evidence pair.

Den robuste boundaryen er hvor mye sammenhengende beslutningsarkitektur som må rekonstrueres.

| Status | Gjenværende arbeid etter Stage 3 | Tillatt human action |
|---|---|---|
| **READY** | ingen identifisert materiell issue | skim + eventuell mikropolish |
| **CHECK** | 1–3 isolerte, lokalt reparerbare issues | lokal faktasjekk/ordlyd/spacing/kort avsnitt; ingen ny backbone |
| **RERUN** | minst ett issue krever ny coherent identity/evidence/motivation/channel decision eller fler-seksjons rewrite | separat one-job Sol-runde |

### Obligatoriske review-invarianter

```text
READY  -> reasons = []
CHECK  -> 1..3 concise reasons
RERUN  -> 1..3 concise reasons
```

### Truth boundary

Hvis Stage 3 ser en **kjent unsupported claim**, skal den reparere den før den lagrer finalpakken. RERUN er ikke et lager for kjent usann employer-facing tekst.

## 13.2 Stage 3-review er kalibrering, ikke uavhengig QA

Stage 3 skriver både finalpakken og `review.json`. Derfor må `TailRecall20` tolkes som:

```text
How well does Sol's own confidence/triage align with Vegard's later judgment?
```

ikke:

```text
independent second-review accuracy
```

Dette er fortsatt riktig MVP-design. En fjerde judge-stage ville koste mer og risikere å redusere sluttforfatterfriheten.

Et særlig viktig pilotsignal er **systematisk overtillit**:

```text
many READY
+ low human scores
+ high edit burden
→ review calibration problem and/or Stage 3 quality problem
```

## 13.3 CR-14: RERUN-modell og effort må låses

Første release:

```text
RERUN = GPT-5.6 Sol, Max effort, one job per separate chat
```

RERUN er ikke en fjerde standardstage. Det er en out-of-band gjentakelse av sluttforfatter-/strategiarbeidet for en pakke som allerede er identifisert som en tail case.

### RERUN må ha kildetilgang

Hvis en RERUN skal kunne bytte evidence pair eller candidate identity, kan den ikke være begrenset til vacancy + old final + review. Den må kunne åpne:

- frozen identity;
- strategy/final/review;
- `WRITING_STANDARD`/calibration;
- targeted candidate-authority sections;
- baseline/evidence refs ved behov.

Ellers får man en «fri» strategirunde som i praksis er låst til tidligere evidens.

---

# 14. P0 — Stage completion og validatorarkitektur

## 14.1 CR-23: Modellen skal validere før den markerer seg ferdig

Schema-/artifactfeil bør fanges **inne i stagen** før neste chat/finalizer må bruke tokens på reparasjon.

### Krav

Før `progress` flytter jobben til `completed`:

- Stage 1: strategy + cluster plan contract validation;
- Stage 2: package schema + job identity + employment IDs + deliverable logic;
- Stage 3: final package + review schema + cross-object identity/status rules.

Validator må returnere exit code 0.

## 14.2 Ikke gjeninnfør `_DONE.md`

P0.7 viste hvorfor substring-/markerfiler kan gi falsk trygghet. Completion er:

```text
valid required artifact
+ validator pass
+ progress reconciliation
```

ikke presence av en tekstfil.

## 14.3 Standard validator, ikke ad hoc one-liners

Gemini foreslo en lokal `python -c jsonschema.validate(...)`. Kjernen er riktig, men ad hoc commands sprer kontraktlogikk.

Beste design:

```text
two operator-facing CLIs:
  scripts/ingest.py
  scripts/finalize.py

+ optional narrow internal Python modules:
  validation/contracts/rendering helpers
```

Stage-modeller kan kalle én stabil intern validator-entrypoint. Dette er **ikke** en ny operatørstage eller workflow-script.

---

# 15. P1 — Public CLI contract versus intern implementering

## 15.1 CR-21: «To scripts» bør bety to operator commands

Det verdifulle kravet er:

```text
Operator should only need to understand:
  ingest
  finalize
```

Det er mindre verdifullt å tvinge all intern logikk inn i to enorme Python-filer bare for å kunne si at repositoryet har «exactly two .py files».

### Anbefalt kontrakt

**Offentlig/operator-facing:**

```text
python scripts/ingest.py ...
python scripts/finalize.py ...
```

**Intern implementation:**

Builder kan bruke små private moduler når dette reduserer duplisering eller forbedrer testbarhet, for eksempel:

```text
contracts.py
validation.py
rendering.py
io_helpers.py
```

men skal ikke opprette:

- ny workflow-orchestrator;
- model runner;
- retry engine;
- state machine;
- background service;
- third human workflow command uten behov.

### Testkonsekvens

`test_repository_contract.py` bør teste **public surface og forbudte arkitekturkomponenter**, ikke et rigid Python-filantall som gjør refaktorering til «kontraktsbrudd».

---

# 16. P0/P1 — Testsuite og implementeringsrekkefølge

## 16.1 Problemet er ikke «15 testfiler»; problemet er når man betaler for dem

Et større antall små testfiler er ikke i seg selv overengineering. Flere P0.8-tester beskytter direkte mot observerte P0.7-feil: partial success, private leakage, per-job rerender, identity og rendering.

Men det er lav leverage å bruke store Sol Max-mengder på release-polish og syntetiske edge cases **før** den vanskeligste vertikale kjeden er bevist.

## 16.2 CR-20: Vertical slice først

### Revidert implementeringssekvens

#### Wave A — authority-preserving migration + adopted contract patch

- unpack/inspect P0.7;
- byte-preserve candidate authorities + original masters;
- patch P0.8→P0.8.1 contracts;
- define canonical intake/deliverables/freeze/schemas.

#### Wave B — minimal deterministic spine

Implementer akkurat nok til:

```text
one approved fixture
→ ingest
→ frozen identity/context
→ synthetic valid final package
→ dynamic CV merge
→ DOCX/PDF + portal output
→ review/status
```

Dette er en **mechanical vertical slice**, ikke live model pilot.

#### Wave C — render/template hardening

- exact tag-source map;
- sparse/normal/dense render;
- selectable PDF;
- page/layout inspection;
- single-job atomic output.

#### Wave D — stage instructions + validators

- Stage 1/2/3 local instructions;
- read-order/debiasing;
- standardized artifact validation;
- progress creation/recovery.

#### Wave E — multi-job mechanics

- partial success;
- expected-set reconciliation;
- continuation;
- `--job` rerender;
- rollback-safe `--force`;
- converter failure isolation.

#### Wave F — Tier 0/Tier 1 QA

- automated contracts;
- all-page visual QA;
- two-job live developer smoke.

#### Wave G — docs/release polish

- Tier 2;
- manifests/packaging;
- operator docs;
- pilot logs;
- release evidence.

#### Wave H — real 8-job product pilot

Først nå måles actual package quality.

## 16.3 Test Tier 0 — MÅ før første reelle model output

- schema parse + representative positive/negative fixtures;
- batch-plan/job-identity crosscheck;
- freeze/context-snapshot checks;
- baseline parse, unique employment IDs, complete chronology;
- employment full-replacement semantics;
- required deliverables;
- hard portal limit behavior;
- unknown employment ID;
- high-precision private leakage;
- template tag/source contract;
- one-job mechanical vertical slice;
- PDF open/selectable text;
- sparse + normal visual inspection.

## 16.4 Test Tier 1 — MÅ før 8-job product pilot

- expected-job reconciliation;
- partial success;
- `--job` rerender;
- rollback-safe `--force`;
- no-letter/no-portal/portal-required cases;
- older employment override;
- progress set reconciliation + continuation;
- Stage 1/2/3 critical validator contracts;
- dense rendering + all-page visual QA;
- converter timeout/failure isolation;
- review queue READY/CHECK/RERUN/FAILED sorting;
- cross-file deliverable invariants;
- rogue/extra artifact detection.

## 16.5 Test Tier 2 — før 40-job full release, ikke nødvendigvis før developer smoke

- deterministic ZIP/release packaging;
- exhaustive manifest/meta cleanup;
- broad repository-absence checks;
- secondary fixture variants uten direkte truth/output risk;
- documentation consistency checks;
- golden regression packages **etter** at et menneskelig godkjent pilotresultat finnes.

## 16.6 Unngå keyword-theatre i stage-contract tests

Tester som bare søker etter tilfeldige nøkkelord i instruksjonsfiler kan gjenta P0.7s `_DONE`-/substring-problem i ny form.

Hvis stage metadata må være maskinlesbar, bruk stabile eksplisitte contract lines eller valider faktisk artefaktadferd. Ikke kall «ordet finnes i Markdown» for proof of semantic contract.

---

# 17. Pilotdesign: gjør tallene beslutningsbrukbare

## 17.1 CR-16: Small-n Top-80

P0.8 definerer Top-80 som at bunn-20 % tas ut. Ved `n=8` er bunn-20 = 1,6 jobber. Det finnes ingen eksakt heltallsløsning.

### Gjeldende anbefaling

Bruk nearest integer med eksplisitt half-up-semantikk:

```text
bottom_k = max(1, floor(0.20 * n + 0.5))
top_k    = n - bottom_k
Top80Mean = mean(top_k highest human scores)
```

For `n=8`:

```text
bottom_k = 2
top_k = 6
```

25 % ekskludert ligger nærmere nominelle 20 % enn 12,5 %.

### Obligatorisk sensitivitetsrapport for liten n

For 8-jobspiloten rapporteres samtidig:

```text
raw q scores
median
mean(all 8)
mean(top 7)
mean(top 6)   <- primary discrete Top80 approximation
Q_happy(primary)
```

Dette gjør at en routingbeslutning ikke skjules bak ett avrundingsvalg.

### Historisk konflikt som nå er lukket

En tidligere anbefaling brukte `ceil(0.8*n)` og dermed Top-7. Denne er **superseded** som primærregel, men Top-7 beholdes som sensitivitet.

## 17.2 Ikke bruk én 8-jobbs `Q_happy` som presis Max/XHigh-dom

En klynge er liten og jobbene er heterogene. Resultatet er en **observational product signal**, ikke et stabilt estimat av 40-jobbs distribusjonen.

Før modellrouting endres permanent bør man se:

- package quality;
- edit/handling time;
- READY-rate;
- Stage 3 rewrite severity;
- early/late pattern;
- minst én replikasjon eller en liten paired/counterbalanced comparison.

## 17.3 CR-15: Credits må logges på den enheten de faktisk oppstår

P0.8 har allerede credit-kolonner i `PILOT_LOG.csv`. Problemet er ikke at feltene mangler; problemet er **accounting unit**.

Én Stage 1/2/3-chat behandler en klynge med flere jobber. Hvis plattformen rapporterer cost per chat/turn:

- kopierer man cluster cost til åtte jobbrader, åttedobles totalsummen;
- deler man den likt på åtte, skapes falsk per-jobb-presisjon.

### Anbefaling: `PILOT_RUN_LOG.csv`

Én rad per faktisk stage-chat/continuation:

```text
run_id;
batch_id;
cluster_id;
stage;
model;
effort;
started_at;
ended_at;
jobs_planned;
jobs_completed;
continuation_of;
platform_input_credits;
platform_output_credits;
platform_total_credits;
measurement_source;
notes
```

Per-job `PILOT_LOG.csv` beholder quality/review/time-attributter. Hvis en estimert cost allokeres per jobb, må den merkes `estimated=true` og metode oppgis.

### Korrekt cost-metrikk

```text
cluster_credits_per_ready =
    actual credits across all cluster stage runs
    / submit-ready jobs in cluster
```

Tilsvarende på batchnivå.

## 17.4 CR-17: Edit time alene måler ikke menneskekost

`minutes_per_ready` er nyttig, men kan undervurdere workflowen:

- READY skim tar tid selv uten edits;
- CHECK-verifisering kan ta tid før edit;
- RERUN prep/review tar tid;
- rerender/submission preparation tar noe tid.

Legg derfor til minst:

```text
human_edit_minutes
human_review_minutes
human_rerun_handling_minutes
human_total_minutes
```

Eller én enkel `human_total_minutes` i tillegg til edit time hvis loggingen ellers blir tung.

Primær produktfailure er omfattende menneskelig rekonstruksjon, ikke noen ekstra sekunder med kontroll.

## 17.5 CR-18: Priority A/B er både prediksjon og behandling

Priority A-jobber:

- prosesseres tidlig;
- kan få extra microvariation;
- kan dermed få bedre conditions enn B.

Hvis A dominerer Top-80, beviser det ikke at Stage 1 **predikerte** high-upside korrekt; det kan delvis være behandlingseffekt.

### Post-pilot tolkningsregel

- B lykkes like godt uten ekstra compute → A/B kan være svak/unødvendig;
- A lykkes, men bare etter ekstra microvariation/early position → policy kan være nyttig, prediction validity er fortsatt ukjent;
- A/B like quality + like review time → vurder å fjerne A/B for enklere drift;
- B gjentatte ganger dominerer → Stage 1-prioritering eller upside-antakelsen er feilkalibrert.

Ikke endre policy fra én enkelt A/B mismatch. Se etter mønster over minst to klynger eller en kontrollert test.

## 17.6 TailRecall20

Fordi Stage 3 vurderer sitt eget sluttprodukt:

```text
TailRecall20 = calibration of self-triage against human judgment
```

Ikke uavhengig QA-recall.

Rapporter sammen med `review_load`; høy recall kan være trivielt hvis modellen flagger nesten alt.

## 17.7 Early-versus-late

`jobs 1–4` versus `5–8` er et nyttig deskriptivt signal for context decay/phrase drift, men med fire observasjoner per gruppe er det ikke et inferensielt bevis.

Ved vedvarende signal:

- reduser cluster size;
- stram per-job source reopen;
- vurder continuation/splitting;

før mer kompleks memory-/retrieval-infrastruktur vurderes.

---

# 18. Cross-job og cross-cluster konvergens

## 18.1 Reell blindflekk

P0.8 har gode intra-cluster tiltak:

- source reopen per job;
- one-job-at-a-time persistence;
- cluster notes;
- explicit distinctness/convergence risk;
- Stage 3 final writer.

Men separate clusterchatter har ikke delt minne om sluttprosa fra andre klynger. Samme retoriske åpning eller headline-form kan derfor dukke opp i cluster 1 og 4 uten at en model ser det.

## 18.2 CR-22: Human cross-cluster spot-check

Etter at flere klynger er ferdige:

> Sammenlign headline, første profile-setning og application opening for 2–3 READY-pakker fra ulike klynger. Se etter faktisk gjenbrukt sluttprosa, samme retoriske åpning eller motivasjonsformulering som kunne flyttes ordrett mellom arbeidsgivere.

Bevar naturlig repetisjon av:

- dokumenterte fakta;
- tekniske produktnavn;
- jobbtitler;
- nødvendig norsk standardterminologi.

Dette bør ta få minutter, ikke bli en ny review-stage.

## 18.3 5-gram-sentinel er REJECTED i P0.8

Hvorfor:

- høy false-positive-rate på legitim standardprosa;
- lav recall for semantisk kopiering med små ordendringer;
- gjør Python til stiljudge;
- kan tvinge dårligere ordlyd bare for å unngå string overlap;
- bryter med explicit deferral av large similarity engine.

### Aktiveringskriterium for senere kode

Hvis pilot/full batch viser minst to **materielle** cross-cluster collisions som mennesket faktisk ville redigert, kan neste versjon vurdere en **ikke-blokkerende diagnostikk**, helst først eksakte duplikate hele setninger over en minimumslengde — ikke hard 5-gram gate.

---

# 19. Optional clustering preflight

## 19.1 CR-24: Terra preflight kolliderer med modellrollelogikken

P0.8 sier:

- Sol eier non-linear high-downstream strategy;
- clustering baseres på employer problem, candidate identity, evidence pool, selection regime;
- optional clustering preflight rutes likevel til Terra XHigh.

Dette er intern inkonsistens. Preflight er riktignok ikke autoritativ, men en dårlig anbefaling skaper fortsatt operatorarbeid.

## 19.2 Anbefalt beslutning

For FIRST_RUN_READY:

- manuell clustering er eneste required flow;
- optional preflight tas ut av DoD/tests/repository requirement;
- operator kan bruke en ad hoc model-assist prompt ved behov;
- hvis en standard preflight senere formaliseres, bruk gjeldende strategimodell, normalt Sol XHigh, uten å gjøre den til en ny stage.

Dette er et **scope-kutt**, ikke funksjonstap.

---

# 20. Forslag som er vurdert og bevisst ikke implementert

## 20.1 YAML machine block — REJECTED for P0.8

**Problem den forsøker å løse:** Markdown→JSON handoff-friksjon.

**Hvorfor ikke:** duplisert state, nytt authority-spørsmål, unødvendig struktur for en LLM-consumer.

**Behold kjernen:** stabile headings + exact key/value labels + evidence block validator.

**Revisit:** bare hvis developer smoke viser faktisk Stage 2-mislesing.

## 20.2 Typografisk auto-fit — DEFERRED

**Problem:** CV 2 sider + få linjer.

**Hvorfor ikke nå:** skjult layoutmutation og dårlig forutsigbarhet.

**Revisit:** målte gjentatte near-overflows som gir reell human edit cost.

## 20.3 N-gram/similarity engine — REJECTED/DEFERRED

**Problem:** phrase drift.

**Hvorfor ikke nå:** false positives, Python-semantikk, anti-KISS.

**Revisit:** observerte materielle collisions som human spot-check ikke skalerer for.

## 20.4 Authority hashes per `job_identity` — REJECTED plassering

**Problem:** source drift.

**Riktig løsning:** batch-level `context_snapshot.json` + optional `snapshot_id` i identity.

## 20.5 15 % portal tolerance — REJECTED

**Problem:** P0.8s ord «mindre» er uklart.

**Riktig løsning:** employer limit hard; privat lengre variant kan være separat.

## 20.6 Persistent LibreOffice service — DEFERRED

**Problem:** process startup.

**Riktig første tiltak:** one conversion call per job + timing.

## 20.7 Fjerde reviewer / LLM-as-judge — REJECTED for P0.8

**Problem:** Stage 3 self-review er ikke uavhengig.

**Riktig løsning:** human calibration metrics; ikke ny judge-stage.

## 20.8 Numeric quality/confidence in `review.json` — REJECTED

Human `q` er evalfasit. Modellen skal levere READY/CHECK/RERUN + korte reasons, ikke produsere pseudo-presise self-scores.

## 20.9 Automatisk retry/recovery-loop — REJECTED

Recovery er file-based og manuelt startet. En dårlig jobb skal kunne RERUN separat; systemet skal ikke bli en skjult retry engine.

---

# 21. Korrigeringer av eksterne reviewpåstander

Denne delen bevarer nyttig signal uten å importere stale eller feilaktige detaljer.

## 21.1 Gemini — signal som beholdes

Behold:

- handoff-friksjon mellom `strategy.md` og package JSON;
- bullet replacement-ambiguity;
- LibreOffice startup cost;
- phrase drift;
- lokal validation before completion;
- source/context drift.

Ikke importer:

- `_DONE` som completionmekanisme;
- `experience_overrides` dersom kanonisk P0.8-navn er `employment_overrides`;
- feil authority filename (`Other_high_value_info.md` versus kanonisk `Other_high_value_information.md`);
- påstanden om at headline mangler — P0.8 har allerede eksplisitt headline;
- udefinerte rolle-ID-er som ikke finnes i kandidatontologien;
- garantier som «100 % precision», «90 % færre feil» eller «100 % vanntett».

## 21.2 Claude — signal som beholdes

Behold:

- `used_evidence_refs` modalitetskonflikt;
- RERUN routing;
- clustering-model-role-spenning;
- cross-cluster review;
- testtiering;
- Stage 3 self-review-tolkning;
- behov for explicit pilot decision rules.

Korriger:

- `PILOT_LOG.csv` har allerede credit-kolonner; mangelen er cost-allocation unit;
- 15 % portal tolerance er ikke grunnlagt;
- den beskrevne floor/ceil-formuleringen var internt inkonsistent;
- antall testfiler alene er ikke bevis på overengineering.

## 21.3 Tidligere egen anbefaling — eksplisitt revisjon

Bare én materiell tidligere recommendation endres:

```text
OLD: n_top = ceil(0.8*n), i.e. Top7 for n=8
NEW: bottom_k = round_half_up(0.2*n), i.e. bottom2 / Top6 for n=8
     + mandatory Top7/all8 sensitivity
```

Resten av hovedrapportens P0-funn er integrert i dette dokumentet.

---

# 22. Normativ patchtekst — komprimert implementeringspayload

Denne delen er skrevet for å kunne løftes direkte inn i en P0.8.1-spesifikasjon eller implementeringsprompt. Den er **anbefalt**, ikke adoptert før brukerbeslutning.

## 22.1 Canonical job intake

> Before ingest, every approved job MUST have one machine-readable canonical identity/deliverables entry owned by the operator. Ingest MUST NOT infer required employer-facing deliverables from prose. `notes.md` may clarify context but is not a post-ingest authority for job identity or required outputs.

## 22.2 Deliverable state

> One canonical `required_outputs` representation MUST determine whether CV, application and/or portal output is required. Any retained `channel`, `letter_required` or `portal_required` fields are derived compatibility fields and MUST cross-validate exactly against the canonical representation.

## 22.3 Freeze/context

> Successful ingest of an approved batch creates the frozen runtime boundary and writes one immutable `context_snapshot.json` containing the batch/spec/source/policy/schema/master hashes needed to detect mid-run context drift. Runtime stages MUST NOT silently mix artifacts produced under different snapshots.

## 22.4 Cluster plan

> `cluster_plan.json` MUST validate against a dedicated schema. Its job-ID set MUST equal the frozen cluster membership exactly, with every job appearing once and only once. Stage 2 and Stage 3 use its ordered job list as their canonical processing order.

## 22.5 Progress

> `progress.json` is a recovery index, not source of truth. Stage 2/3 progress MUST be initialized from the valid `cluster_plan.json`; continuation MUST reconcile expected jobs, valid artifacts and progress before resuming.

## 22.6 Expected-set finalization

> Finalizer MUST enumerate expected jobs from the frozen batch/cluster plan for the selected CLI scope. Missing final/review artifacts MUST become explicit per-job incomplete/failure states; discovered output for non-expected jobs MUST be surfaced and never silently accepted.

## 22.7 Truth enforcement

> Deterministic code owns objective mechanics and machine-verifiable identity/provenance/limit/rendering checks. Semantic truth constraints remain absolute, but are enforced through authority-bound model instructions, evidence references and human final review unless they are mechanically provable from structured data.

## 22.8 Portal limits

> Employer portal `max_words`/`max_chars` are hard limits for the deliverable answer. An over-limit required answer cannot be `DELIVERED_READY`. No generic percentage tolerance applies.

## 22.9 Employment override semantics

> Presence of an `employment_override` for an `employment_id` replaces the complete baseline `default_bullets` array for that employment. Merge-by-position, append, implicit retention and partial fallback are prohibited. Absence of an override retains the complete baseline array.

## 22.10 Evidence refs

> Stage 3 MUST update `used_evidence_refs` whenever the final package introduces, removes or replaces material evidence. The final list must reflect evidence actually used in the employer-facing final package. Existence validation is not semantic claim validation.

## 22.11 Review boundary

> `READY` has no material unresolved issue and `reasons=[]`. `CHECK` is used only for one to three isolated, locally repairable issues that do not require a new package backbone, main evidence pair or broad cross-channel rewrite. `RERUN` is used when the remaining issue requires a new coherent identity/evidence/motivation/channel decision or multi-section rewrite. Stage 3 MUST repair any known unsupported claim before saving any status.

## 22.12 RERUN route

> Pilot/default RERUN uses GPT-5.6 Sol at Max effort, one job per separate chat. RERUN is an out-of-band final-writer revision, not a fourth standard stage and not an automatic retry. It may open targeted frozen candidate authorities when replacing evidence or identity.

## 22.13 Stage validation

> A job MUST NOT be added to `completed` until its required stage artifacts pass the standardized stage validator with exit code 0 and cross-object identity checks. `_DONE.md` or equivalent marker files are not completion authority.

## 22.14 Top-80 small-n

> `bottom_k = max(1, floor(0.20*n + 0.5))`; `top_k=n-bottom_k`. For pilots below 20 packages, raw scores and adjacent-cut sensitivity MUST be reported. A single small-n `Q_happy` MUST NOT alone determine permanent model-routing changes.

## 22.15 Credit accounting

> Credits are recorded at the granularity exposed by the platform. Cluster-stage chat costs are logged once in `PILOT_RUN_LOG.csv` and MUST NOT be copied into every per-job row. Any per-job allocation is explicitly estimated with documented allocation method. `credits_per_ready` uses actual cluster/batch credits divided by submit-ready jobs.

## 22.16 Human effort

> Pilot logging MUST distinguish human edit time from total human handling time, or at minimum record both `human_edit_minutes` and `human_total_minutes`.

## 22.17 Converter batching

> Finalizer SHOULD render all required DOCX files for one job before PDF conversion and pass all of that job's DOCX paths to one isolated LibreOffice invocation. Output remains transactional per job. Cross-job converter services are deferred until measured runtime justifies them.

## 22.18 Cross-cluster review

> After multiple clusters are finalized, the operator performs a brief cross-cluster spot-check of CV headlines, profile openings and application openings from multiple READY packages. The check targets actual reusable prose/rhetorical convergence, not legitimate repetition of facts, titles or technical terms.

## 22.19 Clustering preflight

> Manual clustering is the only FIRST_RUN_READY requirement. A standardized model preflight is optional and outside the release DoD; if later formalized, strategic clustering should use the current strategy model rather than the output-writer model.

## 22.20 Public code surface

> P0.8 exposes two operator-facing commands: ingest and finalize. Internal Python modules are permitted when they reduce duplication or improve contract testability, but MUST NOT introduce a model runner, retry engine, database/state machine, third workflow stage or autonomous action surface.

---

# 23. Revidert implementeringsplan for GPT-5.6 Sol Max

## 23.1 Builderens presedens

Etter adoptering anbefales:

```text
1. Candidate authorities — truth within their domains
2. Explicit implementation prompt + adopted consolidated patch directives
3. P0.8 normative specification where not patched
4. Original Word masters for layout/design
5. Compatible P0.7 code/assets
6. Historical reports/reviews only as rationale
```

## 23.2 Før kode

Builder MUST:

1. inventory P0.7 release;
2. hash/copy candidate authorities and masters;
3. build a conflict map from this document to affected P0.8 sections;
4. lock package/identity/deliverable/cluster/freeze contracts;
5. explicitly list DEFERRED/REJECTED features to avoid accidental scope expansion.

## 23.3 Implementer i risikoorden, ikke dokumentrekkefølge

### Step 1 — contracts

- `batch_plan`/canonical job input;
- job identity;
- required outputs;
- cluster plan schema;
- package/review/progress schemas;
- context snapshot;
- baseline semantics.

### Step 2 — one-job deterministic vertical slice

No live model required. Use a hand-authored valid package fixture.

Acceptance:

```text
ingest
→ frozen runtime
→ final package validates
→ merge complete CV
→ render original masters
→ PDF opens/selectable
→ portal obeys limits
→ status/review queue generated
```

### Step 3 — stage contracts

- Stage 1 read order + strategy format;
- Stage 2 package writer;
- Stage 3 final writer/review;
- standardized validators;
- progress/continuation.

### Step 4 — multi-job mechanics

- expected set;
- partial success;
- per-job transaction;
- `--job` rerender;
- force/rollback;
- converter batching.

### Step 5 — Tier 0/1 + visual QA

- automated tests;
- actual page images/PDF inspection;
- no claim of render readiness without visual evidence.

### Step 6 — two-job live developer smoke

Choose two meaningfully different but manageable approved vacancies to test:

- three model stages;
- artifact handoffs;
- schema validators;
- continuation if needed;
- actual final DOCX/PDF;
- human review burden.

This is **not** the product pilot; it is an integration smoke.

### Step 7 — patch only observed integration defects

Do not introduce new architecture unless the defect cannot be fixed locally.

### Step 8 — one real ~8-job cluster pilot

Measure quality, human handling, review calibration, credits and order effects.

### Step 9 — only then test one model/effort variable

First candidate: Stage 3 Sol Max versus XHigh, ideally on a small paired/counterbalanced set so job difficulty does not masquerade as model effect.

---

# 24. Acceptance matrix før første 8-job pilot

| Domain | Acceptance test | Required outcome |
|---|---|---|
| Authority | original authority files hash-preserved | PASS |
| Identity | every job has canonical machine input → immutable identity | PASS |
| Deliverables | exactly one source of required-output truth | PASS |
| Freeze | context snapshot generated + drift detected | PASS |
| Cluster plan | schema valid + exact job-set equality | PASS |
| Progress | stage order reconciles against cluster plan | PASS |
| Expected set | missing/extra stage artifacts surfaced | PASS |
| Package schema | positive + negative fixtures | PASS |
| Merge | full replacement + fallback + older employment | PASS |
| Static chronology | no dropped always-include employment | PASS |
| Portal | exact question set + hard limits | PASS |
| Leakage | known private IDs/review/source metadata blocked | PASS |
| Template map | every content control has one canonical source | PASS |
| Rendering | sparse/normal/dense, all pages inspected | PASS |
| PDF | opens + selectable text | PASS |
| Partial success | one job may fail without destroying another | PASS |
| Rerender | `--job` touches only intended job transaction | PASS |
| Stage validator | invalid artifacts cannot become completed | PASS |
| Live smoke | two jobs complete all three stages | PASS/explicitly understood defect only |
| Human review | READY/CHECK/RERUN meanings usable in practice | PASS |

---

# 25. Pilotlogg — anbefalt endelig form

## 25.1 Per-job `PILOT_LOG.csv`

Behold/utvid til å dekke:

```text
batch_id
cluster_id
job_id
priority
position_in_cluster
stage1_model
stage1_effort
stage2_model
stage2_effort
stage3_model
stage3_effort
predicted_review_status
human_quality_score
human_submit_ready
human_edit_minutes
human_total_minutes
human_bottom20
system_caught_bottom20
stage3_strategy_delta
stage3_rewrite_severity
fact_correction_required
cross_cluster_phrase_issue
notes
```

Credits kan stå her bare hvis de er reelt målbare per jobb eller eksplisitt estimated.

## 25.2 Run-level `PILOT_RUN_LOG.csv`

```text
run_id
batch_id
cluster_id
stage
model
effort
started_at
ended_at
jobs_planned
jobs_completed
continuation_of
platform_input_credits
platform_output_credits
platform_total_credits
measurement_source
notes
```

## 25.3 Derived metrics

```text
Median(q)
Top80Mean(primary + sensitivity)
Q_happy
submit_ready_rate
TailRecall20
review_load
human_edit_minutes_per_ready
human_total_minutes_per_ready
credits_per_ready
early_vs_late quality delta
READY false-confidence count
RERUN rate
Stage3 strategy-change rate
```

## 25.4 Interpretation hierarchy

Når metrics kolliderer:

```text
truth violation
> package/interview quality
> human reconstruction burden
> operator complexity
> review calibration
> credits
> batch uniformity
```

En modellvariant som er litt billigere, men øker full rewrite per package, er dårligere. En variant som flagger alt CHECK og får 100 % TailRecall20 er heller ikke god.

---

# 26. Risiko- og aktiveringsregister

| Risiko | Nåværende mottiltak | Når mer system faktisk er berettiget |
|---|---|---|
| Stage 2 misleser strategy | exact headings/labels + validator | gjentatte reelle handoff-feil → vurder structured machine block |
| cross-cluster phrase reuse | human spot-check | >=2 materielle redigerte collisions → enkel diagnostic |
| near-overflow CV | better master + soft review | gjentatte handling-minutter → preapproved COMPACT profile |
| LibreOffice latency | one invocation/job + timing | render dominates workflow → vurder persistent converter |
| Stage 3 overconfidence | TailRecall/review load/human q | systematisk READY-miss → vurder review policy eller separat judge experiment |
| cluster late-job decay | 6–10 size + source reopen + measure positions | repeatable degradation → smaller clusters/continuation split |
| authority drift | context snapshot | behov for multi-version concurrent runs → først da mer provenance state |
| RERUN volume too high | Sol Max one-job | vedvarende stor tail → fix upstream strategy/writer before auto-retry |
| Priority A useless | pilot logging | repeated no-benefit → remove A/B |
| model Max cost high | baseline metrics | paired XHigh test preserving quality + human time |
| test suite cost | tiers + vertical slice | observed regressions determine added tests |

---

# 27. «Do not build» — eksplisitt scope firewall

GPT-5.6 Sol Max bør få denne listen i implementeringsprompten for å unngå at en «forbedringsvillig» builder bruker tokens på systemet i stedet for produktet.

**Ikke bygg i P0.8.1 uten eksplisitt ny beslutning:**

- vector database;
- embeddings/RAG retrieval platform;
- semantic cache;
- candidate memory/archetype memory;
- multi-agent/subagent system;
- agent debate;
- LLM-as-judge standardstage;
- automatic model router;
- full-package best-of-N;
- semantic auto-repair loop;
- hidden automatic retry;
- database/state machine/event sourcing;
- provenance platform utover small context snapshot;
- large similarity engine;
- n-gram hard/soft gate;
- typographic adaptive auto-fit;
- LibreOffice service/daemon;
- automatic employer research;
- automatic job search;
- automatic submission/contact/profile mutation;
- numeric fit probability;
- generalized release governance platform;
- per-job duplicate authority snapshots;
- new stage purely for candidate-blindness;
- new RERUN stage folder in standard topology;
- `_DONE.md` revival;
- rigid «exactly N Python files» repository contracts.

---

# 28. Hva denne siste spesifikasjonsrunden faktisk kjøper

Det sentrale spørsmålet er ikke «kan systemet spesifiseres enda mer?». Det kan det alltid. Spørsmålet er hvor den neste enheten av pre-implementation reasoning har positiv forventet verdi.

Denne konsoliderte patchen har høy forventet verdi fordi den:

- fjerner steder der builderen ellers må velge mellom to plausible implementasjoner;
- reduserer risikoen for at hard og soft policy bytter plass;
- gjør runtime freeze/recovery reproduserbar;
- hindrer lost/missing jobs og duplicate state;
- holder modeller frie på semantikk og kode streng på mekanikk;
- gjør pilotens metrics faktisk fortolkbare;
- legger dyr Sol Max-innsats etter, ikke før, den første vertikale mekaniske sannhetstesten;
- bevarer KISS ved å eksplisitt avvise sofistikerte løsninger på ennå umålte problemer.

Det er **ikke** en begrunnelse for å gjøre P0.8 større. Tvert imot: den beste konsoliderte retningen er et litt mindre, men mer entydig system.

---

# 29. Endelig anbefalt P0.8.1-diff i prioriteringsrekkefølge

Hvis spesifikasjonen bare skal endres én siste gang, gjør dette i denne rekkefølgen:

1. **Canonical machine-readable job/deliverables intake** før ingest.
2. **Single-source deliverable state**; derive/remove channel booleans.
3. **Batch freeze + `context_snapshot.json`**.
4. **`cluster_plan.schema.json` + exact membership reconciliation**.
5. **Stage 2/3 progress created from cluster plan**.
6. **Expected-job finalizer enumeration**.
7. **Mechanical-hard versus semantic-hard matrix**.
8. **Portal hard limit + hard/soft/target classification**.
9. **Exact package→template source map**.
10. **Full employment bullet replacement semantics**.
11. **Mandatory final `used_evidence_refs` synchronization**.
12. **READY/CHECK/RERUN repair-scope boundary**.
13. **RERUN = Sol Max / one job / targeted authority access**.
14. **Standard validator before completed**.
15. **Small-n Top-80 + sensitivity**.
16. **Run-level credit ledger + total human handling time**.
17. **Priority A/B confounding/decision rule**.
18. **One LibreOffice conversion invocation per job**.
19. **Test tiers + mechanical vertical slice before breadth**.
20. **Two operator CLIs, internal-module freedom**.
21. **Cross-cluster human phrase spot-check**.
22. **Remove Terra clustering preflight from first-run scope**.
23. **Freeze deferred/rejected list explicitly**.

Når disse er enten adoptert eller eksplisitt forkastet med begrunnelse, er den siste spesifikasjonsrunden ferdig.

---

# 30. Stopping rule

**Ikke gjør en ny generell reviewrunde etter denne dersom følgende er sant:**

- identity/deliverable intake har én kanonisk kilde;
- freeze/context provenance er operativ;
- `cluster_plan` er schema-valid;
- expected job set kan reconcileres;
- hard/soft truth og length semantics er entydige;
- template source map er låst;
- override/evidence/RERUN-reglene er entydige;
- pilot-cost og Top-80-reglene er definerte;
- vertical-slice acceptance tests er klare;
- deferred features har eksplisitte activation criteria;
- implementeringsmodellen kan begynne med én jobb uten å måtte ta en ny arkitekturbeslutning.

Etter dette er høyeste informasjonsverdi:

```text
implement
→ render
→ inspect
→ run real models
→ score actual packages
→ measure human minutes
→ measure credits
→ change one observed bottleneck at a time
```

**End-state vurdering:** P0.8 trenger ikke mer konseptuell intelligens før implementering. Det trenger noen få skarpe kontrakter slik at den intelligensen som allerede er i designet faktisk overlever overgangen til kode, stage-instruksjoner, dokumenter og reelle søknader.

---

# Appendiks A — komprimert LLM-handoff

Dette appendikset er laget for en builder som trenger maksimal signalrate.

## A.1 Build target

```text
Build P0.8.1 as a manual, file-based, three-stage Selective Quality MVP.
Do not redesign topology.
Do not expand scope.
Protect candidate truth absolutely.
Optimize final employer-facing package quality and human rewrite burden.
```

## A.2 Standard model route

```text
Stage 1: GPT-5.6 Sol Max
Stage 2: GPT-5.6 Terra Max
Stage 3: GPT-5.6 Sol Max
RERUN:   GPT-5.6 Sol Max, one job/chat
```

## A.3 Operator-facing deterministic surface

```text
ingest.py
finalize.py
```

Private helper modules are allowed; new workflow/orchestration surfaces are not.

## A.4 Canonical runtime chain

```text
operator-approved batch/job/deliverables input
→ ingest
→ job_identity + context_snapshot + Stage1 progress
→ Stage1 strategy + cluster_plan
→ Stage2 draft package
→ Stage3 final package + review
→ finalize expected job set
→ baseline merge
→ DOCX/PDF/portal
→ READY/CHECK/RERUN/FAILED
→ human final review
→ manual submission
```

## A.5 Non-negotiable P0.8.1 deltas

```text
single canonical deliverable state
context snapshot at ingest freeze
cluster_plan schema
expected-job reconciliation
mechanical vs semantic hard truth split
portal exact hard limits
template source map
full employment bullet replacement
final evidence refs synchronized
review status by repair scope
RERUN Sol Max
stage validator before completed
small-n Top80 rule + sensitivity
run-level credits
human total time
vertical slice + test tiers
```

## A.6 Do not accidentally implement

```text
YAML strategy duplicate state
5-gram similarity gate
auto-fit typography
15% portal tolerance
per-job authority hash copies
judge stage
auto rerun
model router
DB/state machine
vector/RAG platform
auto submission
```

## A.7 First proof, before broad polish

```text
one fixture job:
intake → ingest → freeze → valid synthetic final → merge → original master → PDF → review status
```

Then:

```text
two live jobs through Sol→Terra→Sol
```

Then:

```text
one ~8-job real cluster pilot
```

Only measured failure justifies the next architecture change.

---

# Appendiks B — source/provenance map

This consolidation uses the following source roles:

| Source | Role in this consolidated report |
|---|---|
| `Jobbsok_26_P0.8_architecture_and_specification.md` | normative P0.8 baseline whose ambiguities/gaps are reviewed |
| `Jobbsok_26_preference_and_instruction_profile.md` | authoritative product intent, cost hierarchy, truth/persuasion/KISS constraints |
| `Canonical_Conversation_KB_implementing_model_chat.md` | P0.7 implementation history, release evidence, migration context |
| `Canonical_Conversation_KB_improvement_and_brainstorming_model_chat.md` | optimization-objective shift, design trajectory, open empirical questions |
| `Canonical_Conversation_KB_external_review_model.md` | independent architecture synthesis and intermediate critique |
| `Jobbsok_26_P0.7_Release(1).zip` | implemented mechanical baseline and reusable code/assets |
| original deep review | primary systematic P0.8 contract/architecture critique |
| cross-model addendum | later conflict resolution + non-redundant Gemini/Claude signal |
| Gemini review | micro-contract/implementation hypotheses; filtered for stale state and overengineering |
| Claude review | contract modality, routing, test sequencing, measurement and cross-cluster critique |

The consolidation intentionally does **not** treat external review prose as authority over the current P0.8 spec or candidate sources. Review findings become recommendations only through the explicit decisions in this document.
