# Jobbsøk_26 P0.8 — addendum etter kryssmodell-review

**Formål:** konsolidere all reell, ikke-redundant signalverdi fra de to nye reviewrapportene, kryssreferert mot den opprinnelige P0.8-spesifikasjonen, min tidligere dybderapport, P0.7-releasen, de tre prosjekt-KB-ene og den autoritative preferanse-/instruksjonsprofilen.  
**Avgrensning:** dette dokumentet gjentar ikke hovedanalysen. Det inneholder bare nye mikro-kontrakter, nye risikoperspektiver, reviderte konklusjoner, eksplisitte konflikter og forslag som enten bør innarbeides, modifiseres, utsettes eller forkastes før implementering.  
**Kildelabeler:**

- **Egen rapport:** `Jobbsok_26_P0.8_deep_critical_review_and_improvement_brainstorm.md`
- **Gemini:** `Jobbsok_26_P0.8_kritisk_review_og_forbedringsbrainstorm_Gemini.md`
- **Claude:** `Jobbsok_26_P0.8_kritisk_review_og_forbedringsbrainstorm_claude.md`
- **Normativ spesifikasjon:** `Jobbsok_26_P0.8_architecture_and_specification.md`
- **Preferanseprofil:** `Jobbsok_26_preference_and_instruction_profile.md`
- **Historikk/KB:** de tre `Canonical_Conversation_KB_*.md`-filene
- **Implementert baseline:** `Jobbsok_26_P0.7_Release(1).zip`

---

## Teknisk sammendrag

De to nye rapportene endrer **ikke** hoveddommen: P0.8 har riktig produktmål, trestegsarkitektur, modellrollefordeling, truth boundary, dynamisk CV-merge, partial-success-prinsipp og menneskelig sluttmyndighet. De gir heller ikke grunnlag for en ny topologi eller en større P0.9-lignende utvidelse.

De tilfører likevel flere nyttige deltaer:

1. **To kontraktspresiseringer bør inn:**
   - et `employment_override` erstatter hele bullet-arrayet for den aktuelle `employment_id`; det finnes ingen posisjonell eller delvis merge;
   - `used_evidence_refs` **må** oppdateres ved evidensbytte; ordet «kan» i artefaktseksjonen må ikke gjøre sporbarheten valgfri.
2. **RERUN mangler eksplisitt modell-/effortstandard.** Første release bør bruke **Sol Max**, én jobb per chat, fordi RERUN per definisjon gjelder strategisk svake pakker som krever ny sammenhengende sluttforfatterbehandling.
3. **Renderingsytelse bør optimaliseres uten å bygge en ny dokumentmotor.** P0.7 starter LibreOffice én gang per dokument. P0.8 bør rendre alle nødvendige DOCX-er for én jobb først og konvertere dem i én LibreOffice-kall per jobb, deretter måle faktisk tid i developer-smoke/pilot.
4. **Kryss-klynge-frasedrift er en reell blindflekk.** P0.8 håndterer konvergens innen en klynge, men ikke mellom fem separate klyngechatter. Riktig MVP-respons er en kort menneskelig batch-stikkprøve, ikke en 5-gram-similaritetsmotor i `finalize.py`.
5. **Testsuiten bør tieres etter når den skaper beslutningsverdi.** Hard truth, identity, leakage, portal, merge og render må være på plass før reelle modellkjøringer; releasepolish og enkelte strukturtester kan vente til den mekaniske vertikalskiven og developer-smoken har bevist at systemet faktisk henger sammen.
6. **Creditloggingen er mindre mangelfull enn Claude hevder, men har en reell måleenhetsfeil.** P0.8 definerer allerede CSV-kolonner for credits. Det som mangler er hvordan cluster-chat-kostnad skal tilordnes per jobb uten å fabrikkere presisjon. Løsningen er en separat chat-/stage-run-ledger og cluster-level `credits_per_ready`.
7. **Den valgfrie clustering-preflighten bryter modellrollelogikken.** Klynging er strategisk syntese, mens Terra ellers er definert som outputmodell. Preflighten bør fjernes fra `FIRST_RUN_READY`-scope eller rutes gjennom gjeldende strategimodell, normalt Sol XHigh, uten å bli en fjerde stage.
8. **Jeg reviderer min tidligere Top-80-avrundingsanbefaling.** For en 8-jobbers observasjonspilot er nærmeste heltallsrepresentasjon av bunn-20 % to jobber, ikke én. Bruk `bottom_k = max(1, floor(0.20*n + 0.5))`, men rapporter sensitivitet for både én og to ekskluderte jobber. Ingen Max/XHigh-beslutning bør tas fra én 8-jobbers `Q_happy` alene.

Tre av Geminis mest profilerte forslag bør **ikke** implementeres nå:

- YAML-frontmatter som dupliserer strategiinnhold;
- skjult typografisk auto-fit som endrer spacing per dokument;
- en automatisk 5-gram «phrase collision sentinel».

De adresserer reelle bekymringer, men den foreslåtte mekanikken bryter med prosjektets autoritative kost-/kompleksitetshierarki og introduserer mer redundant state, falske positiver og skjult dokumentvariasjon enn den fjerner.

---

# 1. Hvordan de to rapportene differensierer fra hovedrapporten

## 1.1 Claude tilfører mest kontrakts- og styringssignal

Claude-rapporten er i hovedsak en kontraktsrevisjon. Den peker på:

- modalitetskonflikter (`skal` versus `kan`);
- modellrolleinkonsistens i clustering-preflight;
- manglende RERUN-ruting;
- batch-bred stilkonvergens;
- testrekkefølge;
- tolkning av Priority A/B og pilotdata.

Dette er den mest nyttige typen tillegg fordi den ligger nær implementeringsmodellens faktiske feilmåter: den kan bygge en rimelig løsning som likevel ikke er den tilsiktede løsningen.

Claude har samtidig tre svakheter som må filtreres:

1. Den hevder at `PILOT_LOG.csv`-feltene ikke er definert, men §40.1 i P0.8 inneholder allerede en eksplisitt header med modell, effort, human score, edit minutes og input/output/total credits.
2. Top-80-avsnittet anbefaler språklig «floor», men eksempelet setter `bottom_k=2` for `floor(1.6)`, som matematisk er inkonsistent. Rapportens hovedpoeng — at regelen må låses — er riktig; den konkrete formuleringen er ikke det.
3. Forslaget om 15 % portaloverskridelse som soft toleranse er et vilkårlig terskelvalg uten støtte i portalenes faktiske kontrakt eller prosjektets autoritative krav om at portalsvar skal være innen grensen.

## 1.2 Gemini tilfører mest implementasjonshypoteser, men har mer stale state

Gemini-rapporten fokuserer på:

- handoff mellom Markdown og JSON;
- bullet-merge;
- reviewkalibrering;
- LibreOffice-ytelse;
- frasekonvergens;
- lokal schema-validering;
- context fingerprinting.

Den inneholder verdifulle mikroobservasjoner, men flere detaljer viser at rapporten blander final P0.8 med eldre eller eksterne mellomforslag:

- den bruker `experience_overrides`, mens final P0.8 bruker `employment_overrides`;
- den nevner `_DONE`, som P0.8 eksplisitt har fjernet;
- den bruker filnavnet `Other_high_value_info.md`, ikke det kanoniske `Other_high_value_information.md`;
- den foreslår et eksplisitt headline-felt som allerede finnes og er required i `cv_overrides`;
- YAML-eksempelet introduserer en ny rolle-ID (`ROLE-PROCESS-01`) som ikke finnes i noen godkjent identitetsontologi;
- «100 % presisjon», «90 % færre sidefeil» og «100 % optimalisert/vanntett» er ubegrunnede garantiutsagn.

Gemini bør derfor leses som en **idébank**, ikke som et presist patchsett.

## 1.3 Relasjon til egen rapport

Min egen rapport var bredere og fant flere grunnleggende kontraktshull:

- manglende identitetsinput;
- redundant channel/deliverable-state;
- manglende `cluster_plan`-schema;
- ikke-operativ freeze;
- expected-job-reconciliation;
- hard mekanikk versus semantisk hard policy;
- package-to-template source map;
- Stage 1/3-epistemisk rekkefølge;
- pilotmatematikk og human total time;
- context snapshot;
- public CLIs versus interne moduler;
- vertical-slice-implementering.

De nye rapportenes viktigste rolle er derfor ikke å erstatte hovedrapporten, men å **finjustere noen av dens kontrakter og tilføre enkelte smale blindsoner**.

---

# 2. Full delta-klassifisering

| ID | Påstand/forslag | Kilde | Forhold til egen rapport | Validitet | Integrert beslutning |
|---|---|---|---|---|---|
| G1 | Markdown→JSON gir handofftap; legg YAML-frontmatter i `strategy.md` | Gemini 16–19, 56–74 | Ny bekymring, ny løsning | Bekymring plausibel; løsning dupliserer state | Ikke YAML nå; stram eksisterende nøkkel-/evidensblokker og valider dem |
| G2 | Override med én bullet versus fire baselinebullets er tvetydig | Gemini 23–27 | Ny mikro-kontrakt | Reell presisjonsverdi | Presiser full array replacement, ingen posisjonell merge |
| G3 | RERUN versus CHECK mangler tvingende boundary | Gemini 31–34 | Allerede delvis dekket i egen §5.5 | Riktig, men kategoribaserte triggere blir for grove | Definer etter reparasjonsomfang: lokal patch versus ny sammenhengende backbone |
| G4 | Per-dokument LibreOffice-start kan bli treg | Gemini 38–40 | Ny operasjonell risiko | Bekreftet av P0.7-koden | Én conversion-call per jobb; benchmark før større optimalisering |
| G5 | Phrase drift sent i klynge | Gemini 44–46 | Egen rapport dekker klyngeintern konvergens, ikke batchbred | Reell | Legg batch-/kryss-klynge-stikkprøve; ikke similarity engine |
| G6 | Stage-modellen bør kjøre schema-validering før completion | Gemini 78–84 | Egen rapport anbefaler validatorhelper | Riktig kjerne, feil som ad hoc one-liner | Standard validator, exit 0 før progress→completed, ingen `_DONE` |
| G7 | Typografisk auto-fit via spacing-reduksjon | Gemini 88–95 | Ny | Risiko > dokumentert verdi | DEFERRED; eventuelt preapproved compact master etter målt behov |
| G8 | 5-gram collision sentinel i finalizer | Gemini 99–103 | Ny | Høy false-positive/low semantic recall | Forkast i P0.8; manuell stikkprøve og aktiveringskriterium |
| G9 | Headline må bli required | Gemini 107–109 | Allerede i P0.8 og egen rapport | Falsk positiv | Ingen endring |
| G10 | Authority hashes i hver `job_identity.json` | Gemini 113–115 | Samme problem som eget `context_snapshot` | Problemet reelt; plassering dårlig | Batch-level context snapshot, ikke 40 duplikater |
| C1 | «Mindre» portalavvik bør være ≤15 % soft | Claude A1 | Konflikt med egen hard-limit-anbefaling | Tvetydigheten er reell; terskelen vilkårlig | Portalgrensen er hard for leverbart svar |
| C2 | Top-80-avrunding må defineres | Claude A2 | Allerede identifisert | Riktig hovedpoeng; intern matematisk konflikt | Revider primærregel til nearest-count + sensitivitet |
| C3 | `notes.md`-override og freeze er usynkronisert | Claude A3 | Subsumert av identity/deliverables/freeze-redesign | Riktig i original P0.8 | Notes kan aldri endre identitet etter ingest; helst aldri være authority for kanal |
| C4 | `used_evidence_refs`: `skal` versus `kan` | Claude A4 | Ny | Reell normativ konflikt | Oppdatering er obligatorisk ved evidensendring |
| C5 | Terra clustering-preflight bryter modellrollelogikken | Claude B1 | Ny | Reell, selv om stien er optional | Fjern fra first-run scope eller bruk strategimodell |
| C6 | Testsuiten bør tieres før/etter pilot | Claude B2 | Egen rapport endrer bølgerekkefølge, men ikke eksplisitt testtiers | Nyttig presisering | Innfør Tier 0/1/2 etter beslutningsverdi |
| C7 | RERUN mangler modell/effort | Claude B3 | Ny | Reelt kontrakthull | Sol Max i første pilot/batch; senere separat A/B |
| C8 | Ingen kryss-klynge-homogenitetskontroll | Claude B4 | Ny i batchbred form | Reell | Konsolider med G5; menneskelig batch-stikkprøve |
| C9 | Stage 3 reviewer sitt eget produkt | Claude C1 | Allerede eksplisitt i egen §5.5 | Redundant, men korrekt | Behold egen tolkning: queue calibration, ikke uavhengig QA |
| C10 | Creditlogging er ikke operasjonalisert | Claude C2 | Egen rapport definerer header; P0.8 har allerede header | Premisset delvis feil | Ny residual: logg chat-level cost separat; ikke fabrikker per-jobb-cost |
| C11 | Priority A/B mangler tolkningsregel ved mismatch mot Top-80 | Claude C3 | Egen rapport dekker confounding | Delvis nytt | Legg eksplisitt post-pilot decision rule |
| C12 | Grove mekaniske bounds for headline/profile | Claude 2.2 | Allerede dekket av egen hard/soft-matrise | Redundant og nyttig bekreftelse | Ingen ny hovedendring |

---

# 3. Nye funn som bør innarbeides

## 3.1 Full replacement må være eksplisitt i CV-mergekontrakten

### Nytt signal

Gemini peker på et lite, men viktig spørsmål: Hvis baseline har fire bullets og en override leverer én, er resultatet én bullet eller fire bullets med én posisjonelt endret?

P0.8s mergealgoritme sier «replace bullets» og det eksterne reviewet sier tilsvarende at baselinebullets beholdes bare når ingen override finnes. Dette impliserer full replacement, men implementeringsmodellen bør ikke måtte utlede det.

### Integrert normativ regel

> Når `employment_overrides` inneholder et objekt for en `employment_id`, erstatter objektets `bullets` hele `default_bullets`-arrayet for dette arbeidsforholdet. Det finnes ingen posisjonell merge, append eller delvis fallback. Hvis ingen override finnes, brukes hele baseline-arrayet. `bullets` må inneholde 1–5 elementer; tomt array er invalid.

### Konsekvenser

- En override med én bullet gir nøyaktig én synlig bullet.
- En modell som vil beholde en baselinebullet må eksplisitt skrive den som del av replacement-arrayet.
- Silent fallback er fortsatt forbudt.
- Eldre overrides skal ikke droppes for å redde sideantall; de rendres og kan utløse `PAGE_BUDGET`.

### Test

- baseline 4 + override 1 → rendret 1;
- baseline 4 + ingen override → rendret 4;
- override 0 → schemafeil;
- override 6 → schemafeil;
- eldre override → synlig tekst eller hard renderfeil, aldri silent fallback.

## 3.2 Evidence-sporbarhet må få én modalitet

### Nytt signal

Claude identifiserer en reell ordlydskonflikt:

- Stage 3-delen sier at nye refs **skal** registreres ved strategibytte;
- artefaktdelen sier at listen **kan** endres av Stage 3.

Det siste kan tolkes som at oppdateringen er valgfri.

### Integrert normativ regel

> `used_evidence_refs` MÅ representere den evidensen finalpakken faktisk bygger sine hovedpåstander på. Stage 3 MÅ legge til nye refs når den innfører eller bytter hoved-/støtteevidens, og MÅ fjerne refs som ikke lenger er brukt dersom de ellers ville være misvisende. Feltet KAN forbli uendret når evidensgrunnlaget ikke endres.

### Viktig grense

Dette er **sporbarhet**, ikke en deterministisk sannhetsbevisning. Validatoren kan kontrollere at en ref finnes i frozen authorities/context snapshot. Den kan ikke bevise at formuleringen er semantisk korrekt.

## 3.3 RERUN bør ha en eksplisitt standardrute

### Nytt signal

P0.8 definerer RERUN-prosessen, men ikke hvilken modell/effort som brukes. Dette skaper variasjon i den mest krevende haleoperasjonen.

### Integrert beslutning

> RERUN-default for P0.8-piloten er GPT-5.6 Sol ved Max effort, én jobb per separat chat. RERUN er ikke en fjerde standardstage, men en out-of-band gjentakelse av sluttforfatteransvaret for en pakke som krever ny sammenhengende strategi/tekst.

### Hvorfor Max

- RERUN skal bare brukes når lokal CHECK-redigering ikke er nok.
- Problemene er typisk kandidatidentitet, evidence pair, motivasjonslogikk eller channel backbone — Sol-domener med stor nedstrømseffekt.
- Det forventede volumet er begrenset til halen; dette er riktig sted å bruke høy marginal compute.

### Senere test

Sol XHigh kan testes etter at minst noen reelle RERUN-caser finnes. Ikke bruk normale READY-jobber som proxy for RERUN-arbeid.

## 3.4 Reviewgrensen bør uttrykkes som reparasjonsomfang

Gemini vil gjøre bestemte kategorier til tvungne RERUN-triggere. Intuisjonen er riktig — statusene trenger operativ boundary — men kategorier alene blir feil:

- generisk motivasjon kan være én lokal setningsendring eller et symptom på feil kandidatbackbone;
- en uklar identitet kan noen ganger løses med headline/profile-patch, andre ganger kreve full rewrite;
- en claim-strength-feil kan være ett verb eller et dypt evidence problem.

### Bedre normativ beslutningsregel

| Status | Reparasjonsomfang | Tillatt strategisk endring etter human review |
|---|---|---|
| `READY` | ingen identifisert materiell endring | skim/mikropolish |
| `CHECK` | én til tre isolerte, lokalt reparerbare issues | ingen ny backbone, ingen nytt evidence pair, ingen bred kanalomskriving |
| `RERUN` | minst ett issue krever ny sammenhengende vurdering | identitet, evidence pair, motivasjonslogikk, channel backbone eller flere sammenhengende avsnitt må rekonstrueres |

`READY` skal alltid ha tom reasons-array. `CHECK` og `RERUN` skal ha 1–3 konkrete reasons.

### Truth boundary

Hvis Stage 3 oppdager en faktisk unsupported claim, skal den først **reparere finalpakken**. `RERUN` er ikke tillatelse til å levere en kjent usann påstand videre. Statusen beskriver gjenværende kvalitets-/arbeidsbehov etter beste sannferdige final, ikke et sted å parkere bevisste truth violations.

## 3.5 LibreOffice-startkost bør reduseres på jobb-nivå, ikke med en ny service

### Nytt signal og faktisk P0.7-belegg

Gemini peker på at `soffice`-start per dokument kan bli treg. P0.7s `convert_to_pdf()` oppretter en ny LibreOffice-profil og starter en ny subprocess for hver DOCX. En jobb med både CV og søknad gir derfor to prosessstarter.

P0.8s `--job`-modus gjør at en enkelt rerender ikke trenger å prosessere hele batchen, så Geminis «mange minutter for én jobb» er overdrevet. Men for 40 jobber kan 40–80 prosessstarter bli reell operatørfriksjon.

### Integrert, avgrenset forbedring

Per jobb:

1. rendrer alle påkrevde DOCX-filer til samme jobblokale tempmappe;
2. kaller LibreOffice én gang med alle jobbens DOCX-paths;
3. bruker én isolert profile/tempkontekst for jobben;
4. validerer hver forventet PDF individuelt;
5. promoterer jobben atomisk først når alle påkrevde outputs er gyldige.

Dette halverer prosessstarter for `CV_APPLICATION` uten en persistent UNO-server, bakgrunnsdaemon eller ny avhengighet.

### Måling før mer optimalisering

Logg eller rapporter minst:

- `render_wall_seconds` per jobb;
- antall konverterte dokumenter;
- converter timeout/failure;
- total render time for 2-jobbers smoke og 8-jobbers pilot.

**Aktiveringskriterium for videre arbeid:** optimaliser på tvers av jobber eller vurder persistent converter først dersom målt render-/rerendertid blir en merkbar del av menneskets faktiske workflow. Ikke bygg en LibreOffice-service spekulativt.

## 3.6 Batch-bred frasekonvergens må kontrolleres, men ikke mekaniseres for tidlig

### Konsolidert nytt signal fra begge rapporter

P0.8 har:

- rekkefølgespredning innen Priority A/B;
- `cluster_notes.md` med phrase/convergence-risk;
- Stage 3 cross-job-gjenbrukskontroll innen samme chat/cluster.

Det har ikke en mekanisme for å se at klynge 1 og klynge 4 bruker samme åpning, headline-struktur eller motivasjonsbro. Separate chatter har ingen delt minne om tidligere sluttprosa.

### Hvorfor Geminis 5-gram-løsning ikke bør brukes

En 5-gram-skanner vil:

- flagge legitime uttrykk, stillingstitler, tekniske navn og norsk standardprosa;
- ikke fange semantisk identiske setninger med små ordendringer;
- gjøre `finalize.py` til en stilvurderer, i konflikt med «kode eier mekanikk, modeller/mennesket eier semantikk»;
- introdusere en mini-similarity-engine som preferanseprofilen eksplisitt utsetter uten målt behov;
- kunne skyve sterke formuleringer mot kunstig variasjon.

### Riktig MVP-tiltak

Legg til en human batchkontroll etter at alle klynger er rendret:

> Kryss-klynge-stikkprøve: sammenlign headline, første profilsetning og søknadsåpning for minst 2–3 READY-pakker fra forskjellige klynger. Se etter faktisk gjenbrukt sluttprosa, samme retoriske åpning og motivasjon som kunne flyttes uten endring. Behold sterke parallelle faktaformuleringer når likheten er naturlig.

Dette kan inngå i `START_HERE.md` og full-batch-sjekklisten, ikke i per-jobb `review.json`.

### Aktiveringskriterium for kode

Hvis piloten/full batch viser minst to materielle kryss-klynge-kollisjoner som mennesket faktisk ville redigert, kan neste revisjon vurdere en **ikke-blokkerende diagnostikk**. Start i så fall med eksakte duplikate hele setninger over en minimumslengde, ikke 5-grams og ikke hard failure.

## 3.7 Clustering-preflighten bør ikke være en implementeringsforpliktelse

### Nytt signal

Claude peker på en intern modellrolleinkonsistens:

- Sol eier ikke-lineære valg med stor nedstrømseffekt;
- clustering kriteriene er employer problem, candidate identity, evidence pool og selection regime;
- likevel er optional preflight satt til Terra XHigh.

Dette er en reell spenning. At outputen er ikke-autoritativ reduserer risikoen, men eliminerer ikke operatorarbeidet ved et dårlig forslag.

### Integrert beslutning

Den enkleste og mest konsistente løsningen er:

- manuell clustering forblir eneste `FIRST_RUN_READY`-krav;
- optional preflight fjernes fra implementeringens DoD, testsuite og mandatory repository artefacts;
- operatoren kan ved behov bruke en ad hoc clusteringprompt uten at dette blir en produksjonsstage;
- hvis en standardmodell senere låses, bør oppgaven rutes gjennom gjeldende strategimodell, normalt Sol XHigh, ikke Writer-modellen.

Dette er et **scope-kutt** og reduserer Sol-implementeringstokens. Det opprettholder likevel muligheten til modellstøtte uten å bygge en funksjon før den brukes.

## 3.8 Testsuiten bør organiseres etter tidspunktet den reduserer risiko

### Nytt signal

Claude bruker filantall som bevis på testvekst. Filantall alene er et svakt kompleksitetsmål; dekomponerte testfiler kan være enklere enn én stor testfil. Det reelle poenget er likevel godt: implementeringsmodellen bør ikke bruke stor innsats på releasepolish og syntetiske edge cases før en vertikal mekanisk flyt er bevist.

### Integrert testtier

#### Tier 0 — MÅ før første reelle modelloutput

Beskytter sannhet, identitet, privatliv og grunnleggende renderbarhet:

- schema parse + representative positive/negative fixtures;
- batchplan/job identity/freeze/hash-crosscheck;
- baseline parse, unique employment IDs og full chronology;
- full replacement semantics for employment bullets;
- required deliverables og hard portal limits;
- unknown employment ID;
- private leakage med høy-presisjonsmønstre;
- template tag contract;
- én-jobbs vertical slice til DOCX/PDF/portal;
- selectable PDF og visuell inspeksjon av minst sparse/normal fixture.

#### Tier 1 — MÅ før åttejobbers produktpilot

Beskytter normal operasjon og recovery:

- expected-job reconciliation;
- partial success;
- `--job` rerender og rollback-safe `--force`;
- no-letter/portal/older override;
- progress set-reconciliation og continuation;
- Stage 1/2/3 critical contract validation;
- normal/dense rendering og full side-for-side visuell QA;
- converter timeout/failure isolation;
- review queue sortering og alle statusklasser.

#### Tier 2 — KAN ferdigstilles etter developer-smoke, men før full 40-jobbers release

Release- og vedlikeholdskvalitet som ikke bør blokkere tidlig læring:

- full manifest-polish og deterministic ZIP tooling;
- exhaustive metadata cleanup;
- brede repository-absence checks som bare beskytter filantall/nomenklatur;
- mindre fixturevarianter uten direkte truth-/outputrisiko;
- omfattende dokumentasjonskonsistenssjekker;
- golden regression jobs etter menneskelig godkjent pilot.

### Viktig avgrensning

Dette er ikke et argument for å hoppe over mekanisk QA. Det er en argumentasjon for å få **den høyeste risikoen først** og utsette lavmarginal releasepolish til etter en faktisk vertikal kjøring.

## 3.9 Creditmålingen trenger riktig regnskapsenhet

### Korreksjon av Claude

P0.8 §40.1 definerer allerede:

- stage models/efforts;
- predicted review;
- human score;
- submit-ready;
- edit minutes;
- bottom-20/tail fields;
- input/output/total credits.

Det er derfor feil at CSV-feltene ikke er spesifisert.

### Den reelle, nye målefeilen

Produksjonsenheten er en **cluster-stage-chat**, mens pilotloggen er én rad per jobb. Plattformen kan gi credits/tokens per chat eller per turn, ikke nødvendigvis per jobb. Å kopiere samme clusterkost til åtte jobbrader vil åttedoble totalsummen; å dele likt gir falsk presisjon fordi jobbene kan ha ulik lengde og continuationbruk.

### Integrert løsning: separat run-ledger

Opprett eller spesifiser en enkel `docs/PILOT_RUN_LOG.csv` med én rad per faktisk chat/continuation:

```text
run_id;batch_id;cluster_id;stage;model;effort;started_at;ended_at;
jobs_planned;jobs_completed;continuation_of;platform_input_credits;
platform_output_credits;platform_total_credits;measurement_source;notes
```

`PILOT_LOG.csv` beholder én rad per jobb og trenger ikke late som eksakt per-jobb credit finnes. Dersom en estimert allokering brukes, må den ha eksplisitt metode og `estimated=true`.

### Korrekt metrikk

```text
cluster_credits_per_ready = sum(all actual stage/chat credits for cluster)
                            / number of submit-ready jobs in cluster
```

Batchmetrikk beregnes tilsvarende. Per-jobb cost brukes bare når plattformen faktisk eksponerer jobbnær måling eller når et eksplisitt estimat er ønsket.

## 3.10 Priority A/B trenger en forhåndsdefinert miscalibration-regel

### Ny residual utover egen rapport

Min hovedrapport beskrev konfunderingsproblemet: A er både en prediksjon og en behandling. Claude tilfører et nyttig operatørspørsmål: Hva gjør systemet hvis B-jobber ender i Top-80 og A-jobber havner i halen?

### Integrert tolkningsregel

Et enkelt 8-jobbers avvik skal **ikke** automatisk føre til at A/B fjernes eller kriteriene skrives om. Gjør i stedet følgende:

1. registrer hvilke B-jobber som scoret høyt og hvilke A-jobber som scoret lavt;
2. vurder om forskjellen skyldtes feil Stage 1-prioritet, vanskeligere jobbmix, prosesseringsposisjon, microvariation eller Stage 3-rewrite;
3. se etter systematikk på minst to klynger eller i en liten counterbalanced test;
4. endre bare én av følgende av gangen:
   - prioriteringskriteriene;
   - process order;
   - microvariation policy;
   - A/B-mekanismen som helhet.

### Beslutningssignal

- **B lykkes uten ekstra compute:** mulig at A/B-prediksjonen er svak eller unødvendig.
- **A lykkes, men bare med microvariation/early position:** policyen kan virke, men dette beviser ikke prediksjonskvalitet.
- **A og B er like, reviewtid lik:** vurder å fjerne A/B for enklere drift.
- **B dominerer gjentatte ganger:** Stage 1s kriterier eller antakelsen om «high-upside first» er feilkalibrert.

## 3.11 Top-80-regelen bør endres fra min tidligere anbefaling

### Konflikten

- Min rapport foreslo `n_top = ceil(0.8*n)`, altså top 7 ved n=8.
- Claude diskuterer floor/ceil inkonsistent, men peker riktig på at valg av én eller to halejobber kan endre pilotkonklusjonen.
- P0.8 sier språklig at de laveste 20 % tas ut.

### Revidert primærregel

Bruk nærmeste heltallsrepresentasjon av bunn-20 % med eksplisitt half-up-regel:

```text
bottom_k = max(1, floor(0.20 * n + 0.5))
top_k = n - bottom_k
Top80Mean = mean(top_k highest human scores)
```

Resultat:

- n=8 → bottom_k=2, top_k=6;
- n=10 → bottom_k=2, top_k=8;
- n=40 → bottom_k=8, top_k=32.

For n=8 er 25 % ekskludert nærmere 20 % enn 12,5 % ekskludert. Dette er likevel en grov diskret approksimasjon.

### Obligatorisk sensitivitet for liten n

Rapporter også:

- Top6 mean;
- Top7 mean;
- all-8 mean;
- rå scoreliste og median.

`Q_happy` fra én 8-jobbers klynge er en observasjonsindikator, ikke et presist estimat av full-batch-utility og ikke et tilstrekkelig grunnlag alene for Max→XHigh-routing.

---

# 4. Konflikter og endelig avgjørelse

## 4.1 Portalgrenser: hard versus 15 % soft

### Pos A — egen rapport/preferanseprofil

- Portalsvaret må kunne limes inn og aksepteres.
- «Innen limits» er eksplisitt suksesskriterium.
- Et over-limit svar er ikke en komplett employer-facing leveranse.

### Pos B — Claude

- Tillat opptil 15 % som soft avvik; over dette hard failure.

### Vurdering

15 % er ikke avledet fra portaladferd, brukerpreferanse eller empiriske data. En portal med 1500-tegnsgrense aksepterer ikke 1725 tegn fordi overskridelsen anses «mindre». Toleransen ville dessuten gjøre READY/CHECK-data avhengig av en arbitrær systemregel fremfor arbeidsgiverens faktiske tekniske kontrakt.

### Endelig beslutning

**Behold hard portalgrense.** Dersom man vil bevare en lengre privat formulering, må den ligge i et eksplisitt ikke-leverbart felt eller arbeidsnotat. Den kan aldri gjøre den faktiske `answer`-verdien gyldig.

## 4.2 YAML-frontmatter: strukturgevinst versus redundant truth surface

### Pos A — Gemini

- maskinlesbar frontmatter reduserer Stage 2-tolkning;
- kritiske felt blir enklere å finne.

### Pos B — P0.8/egen rapport/preferanseprofil

- strategy har allerede eksakte headings og evidence blocks;
- Stage 2 er en LLM, ikke en deterministisk parser;
- duplicate state og ekstra schema øker drift;
- semantic artifacts bør forbli modellvennlige og smale.

### Endelig beslutning

**Ikke innfør YAML-frontmatter i P0.8.** Høst bare kjerneideen:

- bruk eksakte key/value-linjer i eksisterende headings;
- gjør evidence blockformatet obligatorisk;
- valider at kritiske headings/labels finnes;
- ikke kopier identity/headline/evidence/priority til et andre autoritativt feltsett.

Hvis developer-smoken viser at Terra faktisk misleser strategyen, kan et senere eksperiment gjøre et **enkelt** strukturert control block autoritativt og samtidig fjerne den tilsvarende duplikasjonen fra proseksjonene.

## 4.3 Auto-fit: sidebesparelse versus skjult layoutmutasjon

### Pos A — Gemini

- reduser spacing/line-height 5–10 % når dokumentet nesten blir tre sider.

### Pos B — prosjektkontrakten

- sidebudsjett er soft;
- layout skal være profesjonell og konsistent;
- kode skal ikke ta semantiske/estetiske beslutninger uten dokumentert behov;
- masterne skal tilpasses kirurgisk og visuelt verifiseres.

### Risiko ved auto-fit

- karakter-/linjeestimat er ikke pålitelig proxy for Word/LibreOffice-layout;
- dokumenter får inkonsistent typografi;
- skjult mutation gjør visuell QA vanskeligere;
- spacing kan bli dårligere enn en 3-siders CV;
- output avhenger av heuristiske terskler og renderer.

### Endelig beslutning

**DEFERRED.** Først design masteren godt og mål reell overflow. Dersom «2 sider + 3 linjer» skjer gjentatte ganger, vurder én forhåndsgodkjent `COMPACT`-mastervariant eller renderprofil med eksplisitt logging — aldri kontinuerlig, skjult per-dokument spacingjustering.

## 4.4 N-gram-sentinel versus minimal mekanikk

### Pos A — Gemini

- 5-gram-duplikater gir `LANGUAGE_POLISH`.

### Pos B — Claude/preferanseprofil/egen vurdering

- automatisert similarity engine er deferred;
- common phrases skaper falske positiver;
- sterk formulering skal ikke svekkes for kunstig variasjon;
- human spot-check er riktig skala.

### Endelig beslutning

**Ikke implementer i finalizer.** Bruk batch-stikkprøve og konkret aktiveringskriterium.

## 4.5 State fingerprint: jobbnivå versus batchnivå

### Pos A — Gemini

- kopier tre authority-hashes til hver `job_identity.json`.

### Pos B — egen rapport

- opprett ett `context_snapshot.json` ved freeze med authority, baseline, schema, writing standard, calibration og template hashes.

### Vurdering

Jobbnivå gir 40 duplikate truth surfaces og gjør job identity til en blanding av jobbmetadata og global run provenance. Batchnivå matcher den faktiske konsistensen som skal beskyttes.

### Endelig beslutning

**Bruk batch-level context snapshot.** `job_identity.json` kan eventuelt inneholde `context_snapshot_id` eller hashreferanse, men ikke kopiere hele hashsettet.

---

# 5. Forslag som eksplisitt ikke tilfører nytt signal

## 5.1 Eksplisitt headline

P0.8 gjør allerede:

- headline required i package;
- 15–140 som soft skriveintervall;
- renderer bruker headline direkte;
- ingen concat av competencies;
- Stage 1, 2 og 3 har eksplisitt headlineansvar.

Geminis forslag er derfor allerede implementert på spesifikasjonsnivå.

## 5.2 Stage 3 som selvreviewer

Dette er allerede analysert i egen rapport. Nyrapportene bekrefter, men endrer ikke konklusjonen:

- `review.json` er queue prediction/calibration;
- human action/score er fasit;
- høy TailRecall uten presisjon kan bety overflagging;
- ingen fjerde reviewer-stage før målt behov.

## 5.3 Mekaniske headline-/profile-bounds

Claude foreslår grove sanity bounds. Egen rapport har allerede en samlet target-versus-absolute-bound-matrise. Den bør beholdes; det er ingen ny arkitekturendring.

## 5.4 Stage schema-validering

P0.8 krever mekanisk sluttkontroll, og egen rapport foreslår en standard validatorhelper. Det nye er bare å gjøre exit 0 til en eksplisitt completion-betingelse. Ingen `_DONE.md` skal gjeninnføres.

---

# 6. Konsolidert addendum-patchliste

Denne listen inneholder bare endringer som ikke allerede var fullt dekket i hovedrapporten, eller som nå er revidert etter kryss-review.

## 6.1 MÅ inn før implementering

| ID | Endring | Hvorfor | Berørte kontrakter |
|---|---|---|---|
| ADD-01 | Presiser full replacement av `default_bullets` ved `employment_override` | fjerner mergeambiguity | §22, §26, package tests |
| ADD-02 | Gjør oppdatering av `used_evidence_refs` obligatorisk ved evidensendring | fjerner `skal`/`kan`-konflikt | §15.7, §22.7 |
| ADD-03 | Definer RERUN-default som Sol Max, én jobb | lukker modell-/efforthull | §8.1, §17, MODEL_ROUTING |
| ADD-04 | Definer reviewstatus etter reparasjonsomfang | bedre TailRecall/queue-kalibrering | §15.10–15.11, review policy |
| ADD-05 | Revider Top-80 heltallsregel og krev liten-n-sensitivitet | gjør pilotmåling eksplisitt | §2.1, §43.3, §46.4 |
| ADD-06 | Definer chat-/stage-level credit ledger og forby falsk per-jobb-presisjon | gjør credits/ready beregnbar | §40.1, §46 |
| ADD-07 | Fjern optional clustering-preflight fra first-run DoD eller rute strategisk | reduserer scope og modellrollebrudd | §7.4, §8.1, §44 |
| ADD-08 | Tier tests etter pre-live, pre-pilot og pre-full-release | bruker implementeringstokens på høyeste risiko først | §§38–39, §42 |

## 6.2 BØR inn som lavrisiko implementasjonsoptimering

| ID | Endring | Begrensning |
|---|---|---|
| ADD-09 | Én LibreOffice conversion-call per jobb for alle jobbens dokumenter | behold per-jobb transaction og isolasjon |
| ADD-10 | Logg render wall time i smoke/pilot | ingen performanceplattform; enkel måling |
| ADD-11 | Legg kryss-klynge-stikkprøve i full-batch human review | ingen automatic similarity gate |
| ADD-12 | Stage completion krever standard validator exit 0 | ingen ad hoc one-liners; ingen `_DONE` |
| ADD-13 | Eksakte key/value labels i kritiske strategy-seksjoner | ingen YAML-duplikat |
| ADD-14 | Post-pilot action rule for Priority A/B-miscalibration | ingen policyendring fra én liten klynge |

## 6.3 DEFERRED / ikke implementer nå

| Forslag | Beslutning | Aktiveringskriterium |
|---|---|---|
| YAML-frontmatter/machine block | ikke nå | dokumentert Stage 2-mislesing i developer-smoke/pilot |
| Typografisk auto-fit | ikke nå | gjentatt near-miss overflow som faktisk gir menneskelig arbeid |
| 5-gram phrase sentinel | ikke nå | minst to materielle batch-kollisjoner som mennesket korrigerer |
| Persistent LibreOffice service/UNO | ikke nå | målt conversion overhead dominerer workflow |
| Egen similarity engine | ikke nå | manuell spot-check skalerer ikke eller tail issue gjentar seg |
| Authority hashes per job | forkast plassering | bruk batch snapshot |
| 15 % portal tolerance | forkast | bare employer-/portalspesifikk dokumentert toleranse kan endre dette |

---

# 7. Forslag til eksakt normativ tekst

## 7.1 Bullet replacement

> **Employment override semantics:** Presence of an `employment_override` for an `employment_id` replaces the complete `default_bullets` array for that employment. Merge-by-position, append, implicit retention and partial fallback are prohibited. Absence of an override retains the complete baseline array. An override must contain 1–5 bullets.

## 7.2 Evidence refs

> Stage 3 MUST update `used_evidence_refs` whenever the final package introduces, removes or replaces material evidence. The final list must reflect the evidence actually used in the final employer-facing package. Existence validation does not constitute semantic claim validation.

## 7.3 RERUN route

> **Pilot RERUN default:** GPT-5.6 Sol at Max effort, one job per separate chat. RERUN is an out-of-band final-writer revision, not a fourth standard stage and not an automatic retry.

## 7.4 Review boundary

> `CHECK` is used only when all remaining issues are isolated and locally repairable without changing the package backbone, main evidence pair or cross-channel structure. `RERUN` is required when the remaining issue requires a new coherent identity/evidence/motivation/channel decision or a multi-section rewrite. Stage 3 must repair any known unsupported claim before writing either status.

## 7.5 Top-80 small-n rule

> `bottom_k = max(1, floor(0.20*n + 0.5))`; `top_k = n - bottom_k`. For pilots with fewer than 20 packages, report raw scores and sensitivity using the adjacent feasible cut-offs. Small-n `Q_happy` is observational and must not alone determine model-routing changes.

## 7.6 Credit accounting

> Credits are recorded at the unit exposed by the platform. Cluster-stage chat costs must be logged once in `PILOT_RUN_LOG.csv` and must not be copied into every per-job row. `credits_per_ready` is computed from actual cluster/batch credits divided by submit-ready jobs. Any per-job allocation must be labeled estimated and document its allocation method.

## 7.7 Converter batching

> Finalizer must render all required DOCX files for one job before PDF conversion and should pass all of that job’s DOCX paths to a single isolated LibreOffice conversion invocation. Output remains transactional per job. Cross-job converter services are deferred until measured runtime justifies them.

## 7.8 Cross-cluster review

> After all production clusters are finalized, the operator performs a brief cross-cluster spot-check of CV headlines, profile openings and application openings from multiple READY packages. The check targets actual reusable prose and rhetorical convergence, not legitimate repetition of facts, titles or technical terms.

---

# 8. Revidert implementeringskonsekvens

Disse addendumendringene bør ikke utløse en ny full omskriving av P0.8-spesifikasjonen. De kan innarbeides som en smal P0.8.1-diff sammen med hovedrapportens kontraktshardening.

Den beste implementeringsrekkefølgen blir nå:

1. **Lås hovedrapportens P0-kontrakter** — identity input, deliverables, portal hard limit, cluster schema, freeze, expected set, truth classes, render source map, Stage 1/3 order og pilotmatematikk.
2. **Legg inn addendumets mikro-kontrakter** — bullet replacement, evidence-ref modalitet, RERUN-rute, review boundary, credit unit og testtiers.
3. **Bygg dataschemas og mekanisk vertical slice.**
4. **Tilpass master/rendering og implementer én LibreOffice-call per jobb.**
5. **Kjør Tier 0.**
6. **Kjør to-jobbers developer-smoke.**
7. **Bygg/reparer Tier 1 ut fra faktisk flyt.**
8. **Kjør åttejobbers produktpilot.**
9. **Utfør kryss-klynge-kontroll først når mer enn én klynge finnes.**
10. **Fullfør Tier 2/releasepolish før 40-jobbers produksjonsbatch.**

Dette beskytter den viktigste ressursen i den kommende Sol Max-implementeringen: ikke bare tokens, men **tokens brukt på riktig rekkefølge av usikkerheter**. Først må systemet bevise at én jobb kan gå korrekt gjennom de virkelige datakontraktene og dokumentmalene; deretter at to jobber ikke forurenser hverandre; deretter at en klynge produserer høy pakkeverdi; først til slutt bør releasepolish og hypotetiske edge cases få full oppmerksomhet.

---

# 9. Endelig integrert vurdering

De nye rapportene styrker konklusjonen om at en siste spesifikasjonsrunde er legitim **bare dersom den er en avgrenset kontraktdiff**. De mest verdifulle tilleggene er små:

- én setning om bullet replacement;
- én modalitetsretting for evidence refs;
- én RERUN-rad i modelltabellen;
- én klarere reviewboundary;
- én revidert avrundingsregel;
- én riktig credit-regnskapsenhet;
- én testsuite-tiering;
- én batch-bred menneskelig frasestikkprøve;
- én lavrisiko converteroptimering.

Det er nettopp denne typen endringer som har høy forventet verdi før en kostbar implementering: de reduserer konkrete tolkningstap uten å legge til en ny produktidé.

Forslagene om YAML-frontmatter, typografisk auto-fit og n-gram-sentinel bør ikke snike seg inn fordi de høres teknisk sofistikerte ut. De gjeninnfører mønsteret prosjektet eksplisitt har forsøkt å komme bort fra: ekstra maskineri som lover «garanti», men som skaper nye kontrollflater, heuristikker og vedlikeholdsbehov før en reell pakke har bevist at problemet finnes.

## Stopping rule

Denne addendumrunden er ferdig når:

- de åtte MÅ-endringene i §6.1 er enten innarbeidet eller eksplisitt forkastet med begrunnelse;
- implementeringsprompten peker på både hovedrapportens P0-register og dette addendumets delta-register;
- ingen av de deferred forslagene bygges uten sitt aktiveringskriterium;
- spesifikasjonen ikke lenger inneholder uklarhet om replacement, evidence refs, RERUN-model, Top-80-count eller credit accounting;
- implementeringen kan starte med en vertical slice uten ny arkitekturdiskusjon.

Etter dette er den høyeste forventede informasjonsverdien i kode, faktiske DOCX/PDF-er og reelle søknadspakker — ikke en ny generell reviewrapport.

---

# Appendiks A — kildekritiske merknader

## A.1 Gemini-rapporten

**Bevar signalet:**

- handoffstruktur;
- bullet replacement;
- LibreOffice-startkost;
- phrase drift;
- stage-time validator;
- mid-run source drift.

**Ikke importer ukritisk:**

- stale `_DONE`-mønster;
- `experience_overrides`-navnet;
- feil authority-filnavn;
- headline som «manglende»;
- udefinert rolle-ID-ontologi;
- garantiprosenter;
- auto-fit og 5-gram-motor uten pilotbevis.

## A.2 Claude-rapporten

**Bevar signalet:**

- used-evidence modalitet;
- clustering-model role;
- RERUN-routing;
- cross-cluster review;
- testtiering;
- eksplisitt pilot interpretation rule.

**Korriger:**

- §40.1 har allerede creditkolonner;
- 15 % portal tolerance er ikke begrunnet;
- floor/ceil-eksempelet er selvmotsigende;
- filantall alene beviser ikke overtesting.

## A.3 Egen rapport — eksplisitt revisjon

Jeg endrer bare én tidligere substansiell anbefaling:

- **Tidligere:** `n_top = ceil(0.8*n)`, top 7 av 8.
- **Nå:** `bottom_k = round_half_up(0.2*n)`, bottom 2/top 6 av 8, med obligatorisk top6/top7-sensitivitet.

Begrunnelsen er at P0.8 definerer metrikken som eksklusjon av bunn-20 %, og 2/8 ligger nærmere 20 % enn 1/8. Den viktigere læringen er fortsatt at n=8 er for lite til å bruke `Q_happy` som en presis routingdom.
