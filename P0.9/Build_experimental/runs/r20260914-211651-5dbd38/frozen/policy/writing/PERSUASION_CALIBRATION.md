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
5. Behold et uttrykkelig forbehold når den konkrete teksten ellers ville villede
   vesentlig. Ikke flytt en nødvendig opplysning til review for å få en sterkere
   søknad. Ukjent bruk eller effekt skal heller ikke omskrives til kjent fravær.
6. Hold det uløste materialgapet synlig i eksisterende felter i review.json.
   Et kjent gap alene tvinger ikke CHECK når ingen faktabekreftelse eller lokal
   reparasjon gjenstår.

Den positive overføringsbroen sier hva kandidaten faktisk har gjort og hvordan
det kan brukes. Den skal verken blåse opp erfaringen eller gjøre et
ikke-diskvalifiserende fravær til et nytt argument mot kandidaten.
