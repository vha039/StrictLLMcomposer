# Policy for stage 3 (EDITOR)

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

---
document: Jobbsøk_26 P0.9 forfatterstemme
version: 0.9.3
language: nb-NO
owner: Vegard Håland
artifact_role: CONTROL_PLANE
authority_domain: employer_facing_expression_only
factual_authority: false
claim_authority: false
strategy_authority: false
qualification_authority: false
primary_consumer: Stage 3
secondary_consumers: []
non_consumer: "Stage 1 (filen er ikke del av denne fasens writing_policy-rute)"
status: ACTIVE
---

# Forfatterstemme

Denne filen fastsetter et uttrykksregister for kandidatens arbeidsgiverrettede
tekst: hvordan et seriøst, evidensforankret faglig argument skal lyde når det er
tydelig, naturlig og hans eget i tonefall.

Den er ikke en «humanizer», ikke et forsøk på å etterligne chat-språk, og ikke
en instruks om å vise personlighet. Den er en generativ prior for uttrykk.

## Rangorden

1. Sannhet og evidensgrenser.
2. Arbeidsgiverens overtalelse og lesbarhet.
3. Stemme.

Stemme kan aldri endre en påstand, et claim-tak, en lifecycle-tilstand, et
forbehold eller et evidensvalg. Den kan forme lokal setnings- og leddrekkefølge,
rytme og formulering av allerede valgt stoff. Den velger ikke bevis, ikke
argumenter og ikke fordelingen mellom CV og søknad, og den flytter aldri en
grense.

## Målinntrykk

Målet er at en norsk ansettende leder som legger fra seg pakken, sitter igjen
med et inntrykk av en person som er kompetent, jordnær, nyttig, interessant,
troverdig og lett å samarbeide med.

Ikke imponeringssøkende, ikke intens, ikke selvbevisst. Forskjellen ligger nesten
alltid i hvor mye teksten tolker seg selv, ikke i hvor sterkt den hevder noe.

## Argumentvaner

- Sett den bærende påstanden først, begrunnelsen etter.
- Forklar mekanisme og årsak i stedet for å bruke adjektiver. Skriv hvordan noe
  virker, ikke at det er strategisk, innovativt eller spennende.
- Bevar de skillene som endrer kandidatens påstand, arbeidsgiverens beslutning
  eller leserens forståelse. Ikke glatt dem ut for å få en penere setning, og
  ikke ta med skiller som bare viser at resonnementet kunne vært mer detaljert.
- Bruk konkrete verb og konkret omfang der evidensen bærer det.
- Skriv om oppførsel og resultat, ikke om gunstige egenskaper ved deg selv.
- Ta en spesifikk faglig vurdering framfor en allment akseptabel plattityde.
- Skriv med verb og konkrete subjekter der nominalisering ellers ville samlet
  handlingen i et substantiv. «Bussen kom tjue minutter for sent» framfor «det
  oppstod en forsinkelse på tjue minutter i bussens ankomst». Eksempelet er
  bevisst hentet utenfor kandidatens egen historie: et førstepersonseksempel
  ville samtidig ha foreslått en påstand kildene setter tak på.
- Ikke overforklar relevans. Én tydelig kobling er nok; leseren trenger ikke få
  den samme broen bygget to ganger.
- Bruk stemmen til å gjøre argumentet klarere, aldri til å gjøre teksten mer
  særpreget enn stillingen og evidensen tilsier.

## Sosial temperatur

Direkte, men profesjonell. Samarbeidsvillig uten ritualhøflighet. Ikke
karikert kontant, ikke kald, ikke konfronterende. Presisjon er høflighet her.
Vis moderat varme gjennom den konkrete, allerede evidensstøttede nytten
argumentet viser for mottakeren, ikke gjennom ros, smiger eller påtatt
entusiasme.

## Setningsarkitektur

- Høy tetthet av relevant signal. Korthet er ikke et mål i seg selv, og
  fullstendighet skal ikke ofres for stramhet — men ingen setning skal bære mer
  forklaring enn argumentet trenger.
- Sterk makrostruktur, mindre lakkerte overganger. En tekst kan være godt
  ordnet uten at hvert avsnitt starter med en brolegging.
- La den lokale formen følge den informasjonelle funksjonen. Et avsnitt som
  bærer en avveining, tåler en lengre setning; et avsnitt som slår fast noe,
  skal være kort. Ulik funksjon skal gi ulik form.
- Ikke bygg parallelle bevisblokker fordi symmetrien ser ryddig ut. Like lange
  avsnitt med lik indre rytme er et tegn på at formen kom fra malen og ikke fra
  argumentet.
- En lengre setning er i orden når et forbehold faktisk krever det; del den når
  detaljen ellers blir vanskelig å lese.
- La avsnittsformen følge argumentet i denne stillingen. To jobber kan gjerne
  få samme form når begge trenger den, men formen skal komme fra jobben og
  ikke fra en mal.

## Selvfremstilling som skal bort

Dette er de konkrete mønstrene som gjør en ellers sannferdig og godt begrunnet
tekst selvhøytidelig. De er observert i faktisk produksjon.

1. **Den avsluttende lærdommen.** En setning på slutten av et avsnitt som
   forteller leseren hva han skal konkludere med, og som ikke tilfører noe
   utover det avsnittet allerede har vist. Flere slike på rad leser som en
   person som er mye å ha med å gjøre. Skriv beviset, og la slutningen være
   leserens.
2. **Selv-rangering av egen evidens.** Å rangere sine egne bevis på
   arbeidsgiverens vegne — «det tydeligste beviset mitt er …», «min sterkeste
   erfaring er …». Rekkefølgen i teksten sier allerede hva som veier tyngst.
3. **Annonsert abstraksjonsnivå.** Å kunngjøre hvor prinsipielt eller
   metodisk man har arbeidet — «på metodenivå», «på et strukturelt plan»,
   «prinsipielt sett». Vis arbeidet; nivået framgår av det.

Videre bort:

- konsulentregisterets prosesskaskader;
- serielle påstander om at hver eneste aktivitet demonstrerer nettopp den
  kompetansen stillingen etterspør;
- oversatt amerikansk søknadsretorikk, `brenner for` og managementsjargong;
- mekanisk symmetri og overforklarte relevanssetninger.

**Motsatt grøft, like alvorlig.** Løsningen er aldri å legge til forbehold,
svekke et dokumentert eierskap, innføre selvironi eller bytte `jeg` mot et
diffust `vi`. Feilen ligger i tolkningen, ikke i påstanden. Fjern
egenvurderingen og den overflødige forklaringen; behold det sterke verbet og
det konkrete ansvaret.

## Mønstre som skal erstattes

Disse er observert i faktisk produksjon og gjenkjennes som generisk
søknadsspråk. De er mønstre å erstatte, ikke forbudte strenger.
Om en formulering er akseptabel avhenger
av fortsettelsen: det er den generiske bruken som skal bort, ikke ordene i
seg selv.

1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …`
   som generisk avslutning. En kort, naturlig invitasjon til samtale er
   tilstrekkelig når bidrag og motivasjon allerede er tydelige. Behold et
   stillingsspesifikt poeng når det tilfører noe; ikke finn på et nytt poeng
   bare for å gjøre avslutningen særegen. I innholdslåst puss beholdes alt
   materielt innhold også når avslutningen omformuleres.
2. `Jeg ønsker å bidra …` som frittstående motivasjonssetning. Si hva du vil
   gjøre, og la det følge av arbeidet.
3. `Det som særlig motiverer meg, er …` fulgt av arbeidsgiverens formål eller
   slagord.
4. `Når <arbeidsgiver> skal <X>, må <Y> …` som standardåpning. En åpning som
   bare refererer arbeidsgiverens egen situasjon tilbake til dem, bruker den
   viktigste setningen i brevet på noe leseren allerede vet.
5. En fast åpning–to bevis–motivasjon–avslutning-form eller speilvendte
   bevisblokker på tvers av jobber. La strukturen følge argumentet.
6. Overføringsbro som refreng: flere avsnitt som ender med samme «den
   erfaringen tar jeg med inn i …»-bevegelse. Én overføring er nok; legg den i
   avslutningen eller inne i beviset den gjelder. Gjentatte broer er
   utskiftbare relevansbroer (`Erstatnings- og komprimeringsrekkefølge`, punkt
   4).
7. Faste vendinger som har slitt seg ut i denne klyngen: «Jeg forteller gjerne
   mer om dette i en samtale», «søker … fordi», kløyvd motivsetning («Det som
   særlig motiverer meg, er …»), identitetsåpning («Jeg er samfunnsøkonom og
   …»), tittelgjentakelse i første setning, og avsnitt som ender på
   «avviklet».

Variasjon gjelder **grepet**, ikke bare ordene. Åpning og avslutning velges
etter funksjon - omsatt arbeidsgiverfaktum, vurderingscase, resultatcase,
sporvalg, problem, direkte motiv; avslutning som spørsmål, konkret bidrag,
neste steg eller ren avrunding. Klyngens register (`register.md`) viser hvilke
grep de andre brevene allerede bruker.

## Kanalkalibrering

- **CV:** lett. Profil, nøkkelkompetanser og bullets skal være dokumenterende
  og skannbare. Stemme viser seg her som presisjon og konkret omfang, ikke som
  stil.
- **Søknad:** moderat. Stemmen former ordlyd, lokal rytme og sosial temperatur
  i den valgte åpningen, motivasjonen og avslutningen. Den velger ikke
  argumentrekkefølge, nytt innhold eller en annen påstandsstyrke.

## Stabil forfatter, variabelt register

Invariant på tvers av arbeidsgivere: presisjon, årsaksstruktur, lav
performativitet, sikkerhet innenfor evidensgrensen, eksplisitte skiller der de
betyr noe, konkrete mekanismer, lite seremoniell retorikk.

Variabelt: varme, formalitet, setningslengde og ordforråd. Gjør det valgte
faglige innholdet tilgjengelig uten å endre hva arbeidsgiveren får vite.
Valg om argument, teknisk dybde og forklaring tas før innholdslåsen.

To pakker til to ulike arbeidsgivere skal ikke være like. De skal ha samme
forfatter.

## Anti-karikatur

- Ikke gjør hvert avsnitt analytisk.
- Ikke bruk stemmen til å overforklare, vise fram metode eller presse inn en
  personlig signatur der enkel språkføring er bedre.
- Ikke press inn systemspråk, rammeverksjargong eller metaspråk om metode.
- Ingen personlighetsetiketter, ingen typologi, ingen selvkarakteristikk.
- Ikke etterlign uformell tone eller chat-tegnsetting.
- Ikke gjør kandidaten kranglete eller belærende.
- Arbeidsgiverens slutning, lesbarhet og sosiale letthet slår alltid synlig
  personlighet.
- Ingen fakta oppstår her. Stemme er uttrykk, ikke evidens.

## Uttrykkskilde for sluttpussen

Denne filen er uttrykkskilden for den avsluttende, innholdslåste pussen i
Stage 3. Når innholdet er låst, er det seksjonene over — målinntrykk,
argumentvaner, sosial temperatur, setningsarkitektur og selvfremstilling — som
avgjør hvordan det låste innholdet skal lyde.

Den pussen kan endre hvordan noe sies. Den kan aldri endre hva arbeidsgiveren
får vite.

### Operatørstyrt sosialregister i siste puss

Denne mekanikken brukes bare i den siste, innholdslåste pussen i Stage 3
FINAL_AND_REVIEW. Den skal ikke leses eller brukes til utvalg, strategi,
utkast eller substansiell omskriving. REVIEW_ONLY utfører ingen registerpuss.
Nivået kommer fra final_polish.social_register_calibration i den fryste
Stage-3-bundelen, med kilde i [voice] i policy/settings.toml. Operatøren velger
heltall fra 0 til 3. Mangler feltet i en eldre fryst bunt, brukes ikke denne
utvidede registerpussen.

Alle nivåer har samme gulv: Behold hver materiell opplysning, personlig handling,
faglig vurdering, mottaker, kvalifikasjon, eierskapsgrense, status, periode,
arbeidsgiverbegrunnelse og argumentrekkefølge. Behold sterke støttede verb.
Ikke legg til ydmykhetsfraser, forbehold, svakere eierskap eller et diffust «vi».
Ikke fjern et case, kort ned for å nå et sidetall eller bytt ut dokumentert
skjønn med generelle kompetanseord. Nivået er et redaksjonelt valg, ikke en
kvalitetsskår eller en grad av påstått kompetanse.

Mønstrene nedenfor gjelder bare når de kan omformes uten å endre det låste
innholdet. De er ikke forbudte ord eller strenger:
- Forelesningspreg: Leseren får egen virksomhet forklart med en autoritet som
  det konkrete kandidatbidraget ikke trenger.
- Selvrangering eller eksakt-passform: En innramming annonserer hvor godt
  kandidaten passer, fremfor å la det allerede beskrevne arbeidet vise det.
- Gjentatt egenposisjonering: En relevansbro eller metakommentar sier på nytt
  det samme som den nærmeste teksten allerede gjør.
- Seiers- eller konfliktpreg: Måten et dokumentert valg presenteres på gjør
  samarbeidet til en rangering av personer. Behold selve valget, rammen,
  begrunnelsen og nødvendig attribusjon.
- Unødvendig avstand: Abstrakt innpakning, gjentatt setningsstart eller
  dokumentasjonsspråk gjør en allerede konkret handling vanskeligere å lese.

Nivå 0: Hopp over denne utvidede registerpussen. Den ordinære innholdslåste
stemmepussen gjelder fortsatt.

Nivå 1: Omform tydelig forelesningspreg, selvrangering og eksakt-passform der
endringen bare gjelder innramming eller allerede overflødig metatekst.

Nivå 2: Gjør nivå 1 og omform også gjentatt egenposisjonering og seiers- eller
konfliktpreg. Behold en spørsmålstilling eller metakommentar når den faktisk
bærer en egen del av argumentet. Annonsert abstraksjon er ingen automatisk
slettegrunn.

Nivå 3: Gjør nivå 2 og arbeid mer med lokal setningsrytme, subjektplassering
og avstand til leseren. Varier bare når samme handling og samme aktør fortsatt
er like tydelige. Et nødvendig «jeg» skal ikke bli et uklart passiv eller «vi».

Nivåene angir hvilke mønsterfamilier operatøren ønsker prioritert; de garanterer
ikke at to enkeltutkast blir forskjellige. Nivå 2 er et startpunkt, ikke et
målt optimum. Nivå 3 er høyeste nivå; det finnes ikke et eget innsatsnivå 4.

På alle aktive nivåer kan et faguttrykk få en betydningslik, mer lesbar
formulering. Forklar ikke en teknisk virkemåte som den låste teksten ikke
allerede fastslår. En term som må beholdes for presisjon, beholdes.

Gjør én sammenhengende puss, ikke en serie poengstyrte gjennomløp. Når en
foreslått endring ville endre en materiell opplysning, la den formuleringen
stå. Registerpussen kan ikke reparere en ustøttet påstand eller flytte en
nødvendig avgrensning til review. Håndter eventuelle slike funn etter de
eksisterende innholds- og triagereglene, uten å bruke registeret som grunnlag
for ny utvelgelse. Ingen telling av markører, ord eller evidensreferanser
avgjør om pussen er god.

## Tegnsetting

Følg `WRITING_DOCTRINE.md § Tegnsetting`. Ingen egne regler her.

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

# Dyplesningen

Fortsatt oppmerksomhet skal gi leseren:

- personlig bidrag;
- rammer og avveininger;
- mekanisme og kontroll;
- faglig skjønn;
- lifecycle og resultat;
- troverdig nytte for denne arbeidsgiveren.

De to lesningene er ikke to tekster. Førstelesningen skal ikke tømmes for
innhold for å bli rask, og dyplesningen skal ikke bli en lengre versjon av det
samme.

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

# Variasjon innenfor en klynge

Innenfor én menneskeoppsatt klynge kan fakta gjenbrukes når den enkelte
jobbens strategi støtter det. Delte fakta er legitimt; gjentatt generisk
ordlyd, arbeidsgiverproblem eller motivasjon er det ikke.

Les stageinstruksen på nytt underveis i en lang klynge, og varier
bevisrekkefølge, åpningsvinkel og dokumentrolle når vacancy-analysen gir
grunnlag for det. Konvergens mellom jobber observeres av mennesket
(`EXP-07`); det finnes ingen automatisk likhetsdetektor i baseline, og det
skal ikke bygges en (Spec 3, Contract 22). `jobbsok register --cluster` lister
hva de andre jobbene i klyngen faktisk valgte - spor, åpningsgrep,
avslutningsgrep, motiv, arbeidsgiverfaktum og første/siste setning. Det er en
opptelling av valg, ikke en likhetsmåling, og den leses før neste brev
skrives.

# Komplett CV-doktrine

CV-en skal være en komplett, omvendt kronologisk A4-CV, ikke en tynn
profilflate.

Den skal alltid inneholde:

- kontakt og identitet fra baseline;
- stillingstilpasset profil;
- prioriterte nøkkelkompetanser;
- full baseline-arbeidskronologi;
- alle `always_include`-ansettelser;
- stillingsspissede bullets for kjente employment-ID-er når verdifullt;
- høyere utdanning og pågående studium med korrekt status;
- språk;
- relevante stabile støtteseksjoner;
- referanseopplysning når masteren bruker den.

Formelle arbeidsgivere, titler, enheter, perioder, rekkefølge, utdanning,
kontakt og språk genereres aldri av en modellstage. De kommer fra baseline
(`DEC-23`). Hvis en employment-ID ikke overstyres, brukes baselinepunktene.
En overstyring som er til stede, erstatter baselinepunktene fullstendig — det
finnes ingen tillegging eller posisjonsfletting.

CV-toppen skal endres materielt med stillingen. Profil og nøkkelkompetanser
skal gjøre kandidatens yrkesanker og rute tydelig: en leser skal kunne plassere
kandidaten i riktig yrkeskategori på første skanning. De tre sterkeste signalene
skal være synlige før sekundær bredde. Verktøy skal stå der de dokumenterer
gjennomføring, ikke som dekorativ beholdning.

Eldre roller kan være kompakte, men kronologien skal ikke forsvinne. Ingen
foto, alder, fødselsdato eller gateadresse som standard. Bruk selekterbar
tekst, enkel leserekkefølge og masterens rolige skandinaviske hierarki.

## Myke redaksjonelle utgangspunkt

Følgende er utgangspunkt for skjønn, ikke grenser. Deterministisk validering
skal aldri felle en pakke for å avvike fra dem (`DEC-24`, `DEC-33`):

- omtrent fire til åtte nøkkelkompetanser;
- CV normalt to sider; en tynn CV kan være én. Med gjeldende maler rommer to
  sider omtrent kapasitetstallet i `[capacity]` i settings - overskrift,
  profil, nøkkelkompetanser, bullets og verktøylinje til sammen. Dette er
  redaksjonell kapasitet, ikke en grense: `jobbsok preview` måler den faktiske
  sideflyten, og komprimeringsrekkefølgen starter med det CV og brev sier likt;
- CV-profil og CV-punkter skrives uten første person; subjektet er
  underforstått, som i CV_BASELINE;
- overskriften navngir en funksjon og skal rendre på én linje;
- verktøy- og metodelister hører hjemme på verktøylinjen, ikke i punktene;
- søknad normalt én side;
- normalt to til fem avsnitt i brevets hoveddel.

Et dokument feiler mekanisk bare når det er ubrukelig, korrupt, avklippet
eller bryter en verifisert teknisk grense.

Sidemål nås ved redaksjonell komprimering, aldri ved å krympe brødteksten. En
stage skal aldri bytte skriftstørrelse eller linjeavstand mot plass i en enkelt
pakke; typografi er ikke en variabel i det semantiske arbeidet. Malenes
typografi og avstander settes én gang, av mennesket, i masterfilene, og er like
for alle jobber. Når et dokument blir for langt, komprimer eller prioriter
innhold. Mindre skrift er forbeholdt bevisst underordnet informasjon:
kontaktlinje, enhets- og periodelinjer, fagdetaljer, støtteseksjoner og løpende
topp-/bunntekst. Sidetall er fortsatt et redaksjonelt signal, ikke en
valideringsgrense (`DEC-24`).

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
