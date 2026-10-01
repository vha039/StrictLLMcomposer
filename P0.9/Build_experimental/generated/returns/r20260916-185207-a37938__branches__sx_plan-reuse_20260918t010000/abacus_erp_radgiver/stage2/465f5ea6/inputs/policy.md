# Policy for stage 2 (ADVOCATE)

---
document: Jobbsøk_26 P0.9 persuasion calibration
version: 0.9.3
owner: Vegard Håland
artifact_role: CONTROL_PLANE
status: ACTIVE_MINIMAL
---

# Persuasion calibration

Bare eksplisitte, gjenbrukbare korreksjoner fra Vegard skal legges til her.
Filen kan kalibrere styrke, bidragsnivå, bevisfunksjon og kravhåndtering, men
kan aldri opprette eller endre kandidatfakta.

Fire domener, én eier hver:

| Domene | Spørsmål den svarer på |
|---|---|
| `CLAIM_STRENGTH` | Hvor sterkt kan dette sies? |
| `CONTRIBUTION_AND_TEAM` | Hvem gjorde det, og innenfor hvilken ramme? |
| `PROOF_FUNCTION_LIFECYCLE` | Hva kan dette beviset brukes til? |
| `MATERIAL_REQUIREMENTS_AND_GAPS` | Hva gjør vi med et krav som ikke er oppfylt? |

# CLAIM_STRENGTH

Godkjent styrke:

- Flytt styrken fra selvkarakteristikk til dokumentert arbeid, ansvar, omfang,
  faglig skjønn, implementering og konsekvens.
- Bruk sterke, presise arbeidsverb uten å kalle kandidaten eksepsjonell,
  overlegen eller unikt kvalifisert.
- Dokumentert faglig skjønn er selvstendig sterk evidens: en beslutning, en
  begrunnet avvisning, en avveining eller en kontroll teller på egne premisser,
  på sitt eget claim-tak. Det er ikke en svakere variant av et leveransebevis,
  og det skal ikke rangeres ned fordi det ikke er en leveranse.
- En sterk, kildestøttet og intervjuforsvarlig formulering kan beholdes med
  en presis merknad om et avgrenset bekreftelsesbehov. En merknad gjør ikke
  en kjent udokumentert påstand tillatt.

Kildestøtte gjelder hele den historiske påstanden, også handlingen,
mottakeren, årsaken og sammenligningen. Et støttet case eller en gyldig
evidensreferanse gir ikke støtte til et nytt forbindelsesledd.
Brukertesting dokumenterer ikke hva som endret løsningen mest; innføring
av en metode dokumenterer ikke at kandidaten holdt workshops om metoden.

Behold det dokumenterte arbeidet med full styrke. Du kan forkorte, omordne,
syntetisere forenlige erfaringer, tilpasse terminologi og forklare relevans.
En begrunnet slutning om hva erfaringen kan bety for en ny arbeidsgiver
er noe annet enn en ny påstand om hva som skjedde, hvem som gjorde det
eller hva som forårsaket resultatet. Marker dette skillet i formuleringen,
uten å gjøre støttede fakta nølende eller generiske.

For svakt:

- Ikke erstatt støttede verb med «bidro litt», «fikk anledning til» eller
  generelle forbehold.
- Ikke gjør sannhetsgrensen til defensiv prosa om ikke-diskvalifiserende gap.
- Ikke bær kildefilenes dokumentasjonsstemme inn i kandidatens egen tekst. Når
  myndigheten sier at kandidaten «oppgir X», er X kandidatens egen opplysning og
  kan sies direkte av ham. Bevar reelle grenser som omtrentlighet,
  observasjonstidspunkt, lifecycle-tilstand og fravær av måling; fjern bare
  avstanden som oppstår fordi kilden er skrevet *om* kandidaten. Kjent sannhet
  skal låte kjent.

Verbene skal følge den dokumenterte handlingen, ikke statusprestisje:
«utformet en modell» sier utforming; «avviste direkte fordeling fordi
datagrunnlaget ikke bar den» sier en dokumentert faglig beslutning;
«gjennomførte kodeendringene» sier egen gjennomføring. Ingen av dem skal
automatisk bli «bidro til» fordi kandidaten manglet linje- eller
programmyndighet. Bruk «bidro til» eller «medutviklet» når det er den presise
beskrivelsen av et delt arbeid. Dette er eksempler på styrkekalibrering, ikke
påbud om bestemte verb.

Mønstereksempelet viser bare forskjellen mellom kandidatstemme,
dokumentasjonsstemme og en for sterk tidsangivelse. Det er ikke en
setningsmal som skal gjenbrukes. Behold kildens faktiske status og tidspunkt,
men la formuleringen følge argumentet i den aktuelle teksten. Kilden i dette
generiske eksempelet sier at noe «ble innført som Y-standard» og er «oppgitt
aktivt om lag N år senere»:

```text
riktig:      «… ble innført som Y-standard og var fortsatt i bruk om lag N år senere.»
for svakt:   «… var rapportert i bruk om lag N år senere.»
for sterkt:  «… er fortsatt i bruk i dag.»   (kilden gjelder N år senere, ikke i dag)
```

For sterkt:

- Ingen selv-rangering, superlativer, titteloppgradering, formelt mandat,
  personalansvar eller resultatnivå uten kandidatmyndighet.

Harde faktagrenser:

- Arbeidsgiver, formell tittel, dato, grad, institusjon, tall, personalansvar,
  mandat og lifecycle skal komme fra riktig kandidatmyndighet.
- Ingen jobbspesifikk prosa, spekulativ regel eller modellpreferanse lagres som
  varig kalibrering uten eksplisitt godkjenning fra Vegard.

# CONTRIBUTION_AND_TEAM

- Bevar skillet mellom personlig arbeid, hovedansvar i team, samskaping,
  bidrag og observasjon.
- Bruk `jeg` for dokumentert personlig bidrag og teamkontekst for kollektiv
  leveranse. Kombiner når begge er sanne. Når både teamkontekst og personlig
  hovedansvar er dokumentert, er mønsteret «I et tverrfaglig team hadde jeg
  hovedansvar for …» godkjent.
- Ikke skjul et dokumentert hovedansvar i et diffust «vi». Ikke tilskriv
  kandidaten hele teamets leveranse.
- Legg teamrammen nær den sterke personlige påstanden, ikke som en generell
  reservasjon et annet sted i teksten.
- Funksjonell eller teknisk ledelse kan beskrives gjennom konkrete handlinger:
  prioritering, oppgavenedbryting, koordinering, arkitektur, workshops,
  integrasjon, kontroll og overlevering. Den skal ikke oppgraderes til
  personalansvar, linjeledelse eller formell prosjekt- eller produkteierrolle
  uten kilde (`INV-03`, Spec 4.1).

# PROOF_FUNCTION_LIFECYCLE

Lifecycle avgjør hva et bevis kan brukes til, ikke hvor godt beviset er.

- Planlagt, utforskende, pilot, aktiv utvikling, implementert, i bruk, fullført
  og avviklet er ulike tilstander. Bruk verb som samsvarer.
- Implementert og i bruk er sterkere for leveranse, adopsjon og varighet.
- Konseptarbeid kan være førsterangs bevis for en dokumentert beslutning, en
  avveining eller en faglig avvisning. At artefaktet er på konseptstadiet
  rangerer ikke skjønnet ned; det avgrenser bare hva skjønnet kan sies å ha
  levert.
- Konseptevidens kan aldri låne implementerings-, adopsjons- eller
  resultatstatus, verken fra seg selv eller fra en annen post.
- Når to poster står i samme argument, beholder hver sin egen tilstand. En
  beslutning i én post er aldri årsaken til en annen posts varighet eller bruk.
- Uavklart eller ikke dokumentert status betyr ikke at noe ikke har skjedd.
  Når kilden bare fastslår utforming, kan teksten si hva kandidaten utformet.
  Den kan ikke derfor si «ikke innført». Et uttrykkelig negativt statusutsagn
  krever støtte for fraværet, på samme måte som et positivt utsagn krever støtte
  for gjennomføringen.
- Hold artefaktets ferdigstillelse, overlevering, organisatoriske bruk og
  målte effekt fra hverandre. Bevar også skillet mellom versjoner og perioder;
  senere bekreftet bruk endrer ikke automatisk beskrivelsen av tidligere arbeid.

# MATERIAL_REQUIREMENTS_AND_GAPS

Bruk eksisterende felter: `importance`, `relation`, `note`, `evidence_refs` og
`objections[].reframe` / `honesty_note`.

1. Antyd aldri at et uoppfylt minstekrav er oppfylt.
2. Si positivt hva den nærliggende, overførbare evidensen faktisk er, når den
   reduserer arbeidsgiverens usikkerhet. Behold det sterkeste støttede
   arbeidsverbet og riktig personlig bidrag.
3. Bruk arbeidsgiverens substansielle vokabular bare der det er dekket.
4. Avgrens først selve påstanden: arbeidsverb, eierskap, omfang, periode,
   leveransestatus og resultat. Når dette gir riktig forståelse, skal teksten
   ikke i tillegg bære en generell liste over mandat eller erfaring kandidaten
   ikke har. Dette gjelder også en innskutt leddsetning eller kontrast, ikke
   bare et eget «jeg mangler X»-avsnitt.
   Unntaket er et terskelkrav skjermleseren uansett ser - år, nivå, et navngitt
   system. Da kan teksten nevne det **én gang**, i en setning som gjør det om
   til argumentet: «Selve produktet skal jeg lære, og rådgiversporet med
   erfarne kolleger gir en god ramme for det.» Aldri som liste, aldri som
   innskutt unnskyldning, og aldri mer enn én slik setning i et brev.
5. Behold et uttrykkelig forbehold når den konkrete teksten ellers ville villede
   vesentlig. Ikke flytt en nødvendig opplysning til review for å få en sterkere
   søknad. Ukjent bruk eller effekt skal heller ikke omskrives til kjent fravær.
6. Hold det uløste materialgapet synlig i eksisterende felter i review.json.
   Et kjent gap alene tvinger ikke CHECK når ingen faktabekreftelse eller lokal
   reparasjon gjenstår.

Den positive overføringsbroen sier hva kandidaten faktisk har gjort og hvordan
det kan brukes. Den skal verken blåse opp erfaringen eller gjøre et
ikke-diskvalifiserende fravær til et nytt argument mot kandidaten.

## Integrert bevisenhet

En bærende bevisenhet er ett arbeidsgiverbeslutningsargument. Den kan bygge
på ett case eller flere klart atskilte erfaringer som belyser samme
beslutning. Antall avsnitt eller evidensposter avgjør ikke antall argumenter.

Bygg med kildestøttet arbeid, personlig bidrag og teamramme, relevant
lifecycle og resultat. En dokumentert beslutning, mekanisme, avveining
eller kontroll kan vise skjønn inne i argumentet. Dette er mulige
bestanddeler, ikke plasser som må fylles. Leveranse eller varighet kan
bære argumentet uten et særskilt skjønnsatom.

PERSUASION_CALIBRATION.md § CLAIM_STRENGTH eier påstandsstøtten;
§ CONTRIBUTION_AND_TEAM eier attribusjonen; § PROOF_FUNCTION_LIFECYCLE
eier hva hver tilstand kan bevise.

Skjønn fra samme evidenspost kan skrives direkte inn når den dokumenterte
relasjonen forklarer arbeidet. Samme post er ikke bevis for en ny sammenheng.

Skjønn fra en annen post kan brukes når det gir mer beslutningsverdi enn
innholdet det fortrenger. Presenter det som en separat dokumentert beslutning,
eller som en faglig regel begrunnet i den beslutningen. Begge kilder skal
inngå i used_evidence_refs. Hver erfaring beholder sin kontekst, handling,
attribusjon, lifecycle og sitt påstandstak.

Integrasjonen ligger i den felles arbeidsgiverrelevansen, ikke i en
konstruert felles prosjekthistorie. Ingen erfaring låner årsak, innføring,
varighet eller resultat fra en annen. Samlokalisering alene er ikke
integrasjon: vis hvilken beslutning erfaringene belyser. Hvis koblingen
ikke tilfører verdi, bruk det sterkere innholdet alene. Behold nødvendig
arbeidsgiverrelevans; stryk en avsluttende lærdom som bare gjentar poenget.

## Vinklingskjeden

For hver bærende bevisenhet kobler modellen internt:

`råfaktum -> arbeidsgiverbehov -> strategisk vinkel -> CV eller søknad ->
naturlig norsk formulering`

Bruk Integrert bevisenhet, de fire kalibreringsdomenene og dokumentrollene
på påstanden.

Kjeden skal endre mening og prioritet, ikke skape formelprosa. Unngå
gjentatte «Dette er relevant fordi …», identiske problem–handling–resultat-
avsnitt og dramatisk risikospråk.

## Jeg, vi og funksjonell ledelse

Dokumentarkitektonisk konsekvens: personlig bidrag og teamgrense hører hjemme
inne i den bærende bevisenheten, nær den sterke påstanden, ikke som en generell
reservasjon et annet sted i teksten.

Den detaljerte kalibreringen av `jeg`, `vi`, hovedansvar og funksjonell ledelse
eies av `PERSUASION_CALIBRATION.md § CONTRIBUTION_AND_TEAM`. Ikke gjenta den her.

## Begrunnet motivasjon

Motivasjon skal være forankret i:

- en konkret oppgave eller et reelt virksomhetsproblem;
- hvorfor arbeidet er faglig, operativt eller samfunnsmessig meningsfullt;
- en troverdig kobling til kandidatens erfaring;
- et kontrollert bilde av bidraget kandidaten ønsker å gi.

Unngå generisk virksomhetsros, kopierte verdier, prestisjemotivasjon,
`brenner for` og entusiasme uten substans. Motivasjon skal forklare hvorfor
akkurat dette arbeidet er en meningsfull neste bruk av kandidatens erfaring.

Avslutt normalt med det konkrete bidraget og en naturlig invitasjon til samtale.
Unngå standardseremoni og faste avslutningsfraser.

> Merk: `brenner for` er semantisk skriveveiledning, ikke en forbudt streng.

Når annonsen gir et konkret faktum om arbeidsgiverens drift, skala, systemer
eller oppdrag, kan brevet bruke det én gang og straks omsette det til en
arbeidsbetingelse kandidatens dokumenterte arbeid svarer på. Et navn eller et
tall som bare gjentas er ikke arbeidsgiverspesifikt (`Arbeidsgiverbyttetesten`).

# Komplementaritet mellom CV og søknad

Kjernen produserer nøyaktig to arbeidsgiverdokumenter for hver `CORE`-jobb:
én CV og ett søknadsbrev, begge på bokmål (`DEC-01`, `DEC-04`). Det finnes
ingen portal-, kanal- eller språkgren i kjernen. Portalspørsmål håndteres
eventuelt manuelt etterpå og er ikke en forutsetning for at pakken er
komplett (`DEC-02`).

## CV

CV-en eier:

- fullstendig kronologi og formelle kvalifikasjoner;
- ansettelsesomfang og lifecycle;
- konkrete ansvarsområder, verktøy og metoder;
- bredden i relevant evidens;
- skannbare bevis og støttet skala;
- terminologi som kan leses av en utenforstående.

Toppsonen og prioriterte erfaringsbullets skal være vesentlig
stillingsspesifikke.

## Søknad

Søknaden eier:

- shortlist-tesen;
- prioriteringen mellom bevisene;
- de integrerte bevisenhetene;
- hvordan kandidaten resonnerer og gjennomfører;
- hvorfor evidensen betyr noe for denne arbeidsgiveren;
- begrunnet motivasjon og kontrollert fremtidig bidrag.

Dekning integreres i argumentene. Et eget avsnitt som lister gjenstående krav
er en påheng-liste, ikke dekning. En statusopplysning eller avgrensning kan
gjentas fra CV-en når den bærer brevets argument, og skal gjentas når brevet
ellers ville bli misvisende. Hvert dokument skal være selvstendig sannferdig:
en avgrensning som bestemmer påstandens omfang, følger påstanden i hvert
dokument som fremsetter den. Dekorativ gjentakelse er fortsatt utelukket:
CV-innhold skal ikke gjenfortelles uten å gjøre arbeid i argumentet.

## Intervjureserve

Detaljer som viser dybde, men som ville fortrenge toppsignal i den
skriftlige pakken, skrives ikke. De er en skrivevurdering, ikke et lagret
artefakt. Flytt verktøydetaljer hit eller til CV-en når arbeidsgiververdien,
prosessen, kontrollen eller innføringen er viktigere.

Dokumentene skal være konsistente, men ikke duplikative. CV-en dokumenterer;
søknaden syntetiserer. Samme faktum kan stå begge steder når det bærer
argumentet eller er nødvendig for riktig avgrensning. Søknaden skal ikke gjenfortelle et helt CV-punkt
bare for å innføre sin egen tolkning av det, og samme argument skal ikke ha
samme formulering i begge dokumenter. Et eget avsnitt om nåværende rolle må
tilføre dokumentert arbeid eller en relevant beslutning; ikke gjenta annonsens
kompetanseliste.

# Tjuesekunderstesten

Før Stage 3 lagrer en final, vurder om en rekrutterer på omtrent tjue
sekunder kan gjengi:

1. kandidatens troverdige yrkeskategori;
2. relevant formell utdanning og nåværende rolle;
3. arbeidsgiverproblemet kandidaten er posisjonert for;
4. de sterkeste én eller to bevisene;
5. en grunn til å lese videre.

Hvis svaret er nei, reparer rekkefølge, toppsone, åpning, signalstyrke eller
teknisk overlast. Ikke løs problemet med mer tekst med mindre et konkret
bevis mangler.

# Arbeidsgiverbyttetesten

Bytt arbeidsgivernavn og tittel mentalt med en annen jobb i klyngen. Undersøk
om pakken begrunner hvorfor kandidatens dokumenterte arbeid er relevant for
den konkrete oppgaven, beslutningssituasjonen eller gjennomføringsformen.

Et navn, en verdi eller et virksomhetstall gjør ikke begrunnelsen spesifikk.
Samtidig kan en god begrunnelse være relevant for flere arbeidsgivere med
lignende behov. Navnebyttet er et redaksjonelt spørsmål, ikke et krav om at
hver setning bare kan passe én arbeidsgiver.

Reparer en generell pakke med et støttet arbeid og en tydelig anvendelse i
rollen. Skill mellom hva kandidaten har gjort, hva annonsen faktisk oppgir,
og hva kandidaten foreslår å bidra med. En funksjonell parallell kan begrunne
overførbarhet; den beviser ikke at to virksomheter har samme modell, problemer
eller beslutningsprosess. Ikke legg til en arbeidsgiverpåstand for å gjøre
koblingen mer særegen.

CV-toppen skal gjøre det relevante kandidattilbudet raskt forståelig. Den
trenger ikke gjenta arbeidsgivernavnet eller annonsens formuleringer. Brevet
skal gi en konkret grunn til å søke og et begrunnet fremtidig bidrag.

# Kandidatbyttetesten

Bytt kandidaten mentalt med en generisk, tilsvarende kvalifisert søker.

Pakken feiler testen når teksten fortsatt ville vært sann. Da beskriver den en
rolle, ikke denne kandidatens arbeid. Reparer med dokumentert handling,
beslutning, mekanisme eller faglig skjønn, ikke med særegenhet for
særegenhetens skyld. Signalet må fortsatt være relevant for stillingen; en
detalj som bare gjør kandidaten gjenkjennelig, men ikke mer aktuell, består
ikke testen.

De to byttetestene virker sammen. Arbeidsgiverbyttetesten fanger generisk
tilpasning; kandidatbyttetesten fanger en utbyttbar kandidat.

# Erstatnings- og komprimeringsrekkefølge

Når kapasitet eller klarhet krever at noe fjernes, ta det i denne rekkefølgen:

1. gjengivelse av annonsen som ikke kobles til kandidatens arbeid, og generisk
   ros. Behold arbeidsgiverens faglige begreper når de presist navngir støttet
   erfaring eller et begrunnet fremtidig bidrag; et dekket krav er ikke
   annonseekko bare fordi samme begrep står i annonsen;
2. selv-rangering, annonsert abstraksjonsnivå og overflødige lærdomssetninger;
3. kronologi eller casedetalj som allerede står i CV-en;
4. utskiftbare relevansbroer;
5. generisk kompetanse- og prosesspråk;
6. det svakeste støttende eksempelet;
7. først deretter en diagnostisk mekanisme eller et faglig skjønn, og bare når
   en annen beholdt kombinasjon gir større arbeidsgiverbeslutningsverdi.

En glattere eller mer annonselik erstatning er ikke «sterkere» fordi den er
lettere å kategorisere. Byttes en setning mot en som sier mindre, er det et tap
selv om teksten leser bedre.

# Tegnsetting

Bruk vanlig norsk tegnsetting. Tankestrek (`–`) og lang tankestrek (`—`) skal
ikke forekomme i arbeidsgivertekst. Vanlig bindestrek `-` brukes der
rettskrivingen krever det: sammensetninger (`Barne- og ungdomsklinikken`,
`Vakt- og sikringssoldat`), datoer og intervaller. Ikke bruk bindestrek bare for
å dele en setning når punktum, komma, kolon eller parentes gjør samme jobb.
Foretrekk `.`, `,`, `:`, `()`, `?`, `!` og anførselstegn. Semikolon er tillatt,
men bør være uvanlig. `|` er et strukturelt skilletegn i overskrifter og titler
og er fortsatt i orden.

> Merk: dette er semantisk skriveveiledning.
