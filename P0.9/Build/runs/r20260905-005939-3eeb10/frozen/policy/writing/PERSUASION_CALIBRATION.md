---
document: Jobbsøk_26 P0.9 persuasion calibration
version: 0.9.2
owner: Vegard Håland
artifact_role: CONTROL_PLANE
status: ACTIVE_MINIMAL
provenance: >
  Carried over from P0.7 context/PERSUASION_CALIBRATION.md. The WRONG_CHANNEL
  entry was dropped because the portal channel is outside the P0.9 core
  (DEC-02), so complementarity is CV vs letter. Reorganisert i 0.9.2 fra tolv
  feiltaksonomi-overskrifter til fire kalibreringsdomener. Rutevalg,
  dokumentrolle, teknisk nivå og arbeidsgiververdi eies nå av
  WRITING_DOCTRINE.md, og naturlig norsk av FORFATTERSTEMME.md. Ingen
  godkjent kalibrering er fjernet, bare flyttet til én eier.
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
- En sterk, rimelig og intervjuforsvarlig formulering kan beholdes i
  arbeidsgiverteksten med en presis merknad i review.

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

Mønstereksempel, med generisk innhold. Kilden sier at noe «ble innført som
Y-standard» og er «oppgitt aktivt om lag N år senere»:

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

# MATERIAL_REQUIREMENTS_AND_GAPS

Bruk eksisterende felter: `importance`, `relation`, `note`, `evidence_refs` og
`objections[].reframe` / `honesty_note`.

1. Antyd aldri at et uoppfylt minstekrav er oppfylt.
2. Si positivt hva den nærliggende, overførbare evidensen faktisk er, når den
   reduserer arbeidsgiverens usikkerhet.
3. Bruk arbeidsgiverens substansielle vokabular bare der det er dekket.
4. Unngå et defensivt «jeg mangler X»-avsnitt med mindre taushet ville villede
   vesentlig.
5. Hold det uløste gapet synlig i `review.json` for mennesket.
6. Et kjent gap alene tvinger ikke `CHECK` når ingen faktabekreftelse eller
   lokal reparasjon gjenstår.

Den positive overføringsbroen er en formulering om det kandidaten faktisk har
gjort, ikke en omskrivning av det han mangler.
