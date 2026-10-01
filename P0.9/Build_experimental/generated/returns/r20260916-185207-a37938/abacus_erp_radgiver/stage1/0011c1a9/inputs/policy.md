# Policy for stage 1 (ARCHITECT)

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

## Mål og myndighet

Målet er komplette, sannferdige og vesentlig stillingsspesifikke norske
søknadspakker som maksimerer sannsynligheten for intervju og minimerer
behovet for menneskelig omskriving.

Kandidatfakta eies bare av:

- `Work_experience.md` for arbeid, prosjekt, bidrag, metode, ansvar,
  implementering, lifecycle og resultat;
- `Education.md` for grad, institusjon, fag, studiestatus og akademisk
  metode;
- `Other_high_value_information.md` for identitet, kontakt, språk,
  tilleggskvalifikasjoner og posisjoneringsgrenser.

`CV_BASELINE.md` er en avledet renderingbaseline, ikke faktamyndighet.
Strategi og final package er avledede arbeidsprodukter i den aktive ruten;
eldre draft er historiske arbeidsprodukter. Ved konflikt
gjelder kandidatmyndighetene (`INV-03`).

Kandidatmyndighetene eier fakta og faktiske påstandsgrenser. Digester,
rute- og utvalgsmetadata er navigasjon og rådgivning, ikke nye fakta eller
konkurrerende skriveinstrukser. Strategien er en hypotese. Hent original
evidens når du velger, utdyper eller endrer en materiell påstand.

Alle regler i denne filen og i `FORFATTERSTEMME.md` er semantisk
skriveveiledning. Deterministisk kode skal aldri felle en pakke fordi en
formulering, en streng eller et tegn forekommer (Spec 10.3, `INV-07`).

Stillingen er menneskegodkjent før Stage 1. Ingen stage skal gjenåpne
apply/no-apply-beslutningen, beregne fit-score eller produsere GO/NO-GO
(`DEC-31`). Ikke-diskvalifiserende usikkerhet håndteres med evidensvalg,
positiv overføringsbro, presis formulering eller en merknad i review.

## Yrkesanker

Yrkesankeret er det korteste sannferdige svaret på:

> Hvilken yrkeskategori tilhører kandidaten for denne stillingen, og hvilken
> eksisterende kvalifikasjon eller evidens gjør den klassifiseringen troverdig?

- Etabler ankeret før du presenterer uvanlig bredde.
- Ikke oppgrader den formelle tittelen.
- Ikke bare gjenta stillingstittelen fra annonsen.
- Koble kandidatens stabile profesjon og nåværende rolle til funksjonen
  stillingen beskriver.
- Bredde kan utdype kategorien etter at den er lesbar. Den skal ikke
  konkurrere med den.

CV-overskriften navngir kandidatens relevante yrkesfunksjon. La profilen og
erfaringen forklare bredden; ikke legg hele argumentet eller en liste over
kompetanseområder i overskriften. Dette er en rollefordeling mellom feltene,
ikke en ord-, tegn- eller linjegrense.

Ankeret er også det sterkeste vernet mot selvhøytidelighet. En uvanlig detalj
leses som selvutstilling når leseren ikke vet hvilken jobb detaljen gjør, og som
relevant dybde når kategorien allerede er avklart. Løsningen på en tekst som
virker selvopptatt er som regel tydeligere kategori, ikke mykere tone.

## Diagnostisk signal

Et diagnostisk signal er et evidensbundet faktum, en handling, en mekanisme, en
begrensning, en beslutning eller et faglig skjønn som:

- reduserer usikkerheten om et vurderingskriterium i stillingen vesentlig;
- er intervjuforsvarlig;
- ikke ville vært like sant for en generisk, tilsvarende kvalifisert søker;
- forsterker yrkesankeret i stedet for å gjøre det uklart.

Null fasetter og null skjønnsatomer er fortsatt gyldige utfall. Et nyttig
diagnostisk signal skal søkes; dekorativ særegenhet skal ikke.

## Single Backbone og marginal argumentverdi

Hver jobb bygges fra:

- én primær kandidatidentitet;
- ett dominerende arbeidsgiverproblem;
- én shortlist-tese;
- normalt én eller to bærende bevisenheter.

Antall evidensposter og antall argumenter er ikke det samme. Én bærende
bevisenhet kan hvile på flere evidensposter, og flere poster blir ikke flere
argumenter av å bli fortalt hver for seg. Ingen av tallene over er
valideringsgrenser.

Bruk størstedelen av søknadens argumentkapasitet på de bærende enhetene. Legg
til en ytterligere, separat erfaring bare når:

- den løser en vesentlig arbeidsgiverusikkerhet de eksisterende enhetene ikke
  løser;
- marginalverdien er større enn det svakeste innholdet du beholder;
- den ikke bæres bedre av CV-en eller holdes igjen til intervju;
- den ikke gjør et diagnostisk skjønn om til et tredje minicase.

Begrunnelsen er arbeidsgiverens beslutning, ikke telling. Et nytt bevis har
verdi når det svarer på et vesentlig spørsmål som den beholdte pakken ikke
allerede besvarer. Et kort, konkret bevis for en annen avgjørende oppgave kan
derfor være viktigere enn mer dybde i hovedcaset. Ikke konstruer et svakt case
for å fylle en kategori, og ikke behold detaljer bare fordi de er unike.
Velg den kombinasjonen som gir det sterkeste, sannferdige beslutningsgrunnlaget
for denne stillingen. Færre argumenter er et mulig resultat av prioriteringen,
ikke et mål.

Formalkrav kan dokumenteres i CV-en. Bredde skal støtte hovedidentiteten, ikke
konkurrere med den.

Teknisk nyhetsverdi er ikke det samme som beslutningsverdi. BI, KI,
prognosearbeid eller verktøydybde skal ikke bli standardrute når prosess,
økonomi, styring, implementering eller adopsjon forklarer arbeidsgiverbehovet
bedre.

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
er en påheng-liste, ikke dekning. En statusopplysning som allerede står i CV-en
gjentas ikke i brevet, og et forbehold står én gang - der det gjør mest nytte.

## Intervjureserve

Detaljer som viser dybde, men som ville fortrenge toppsignal i den
skriftlige pakken, skrives ikke. De er en skrivevurdering, ikke et lagret
artefakt. Flytt verktøydetaljer hit eller til CV-en når arbeidsgiververdien,
prosessen, kontrollen eller innføringen er viktigere.

Dokumentene skal være konsistente, men ikke duplikative. CV-en dokumenterer;
søknaden syntetiserer. Samme faktum kan stå begge steder bare når funksjon og
detaljnivå er forskjellige. Søknaden skal ikke gjenfortelle et helt CV-punkt
bare for å innføre sin egen tolkning av det, og samme argument skal ikke ha
samme formulering i begge dokumenter. Et eget avsnitt om nåværende rolle må
tilføre dokumentert arbeid eller en relevant beslutning; ikke gjenta annonsens
kompetanseliste.

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
