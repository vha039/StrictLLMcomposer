---
document: Jobbsøk_26 P0.7 static CV rendering baseline
baseline_version: 0.7.0
status: DERIVED_VERIFIED
verified_as_of: 2026-07-31
---

# CV baseline

> DERIVED CV RENDERING BASELINE.
> The three candidate authority files remain authoritative.

Denne filen gir `finalize.py` komplett, stabil CV-struktur. Den kan ikke
opprette kandidatfakta. Ved konflikt gjelder:

1. `Work_experience.md`
2. `Education.md`
3. `Other_high_value_information.md`

Kildehashene som ble brukt til denne baselineversjonen:

| Authority | SHA-256 |
|---|---|
| `Work_experience.md` | `03ebb948b03bb1f9c81b992ed748ca76dfad96308272f4d4de47804384ac2710` |
| `Education.md` | `d384ff8328da7127f79868e4eb49cfafd8bcde246457741c655456aa4104ae8f` |
| `Other_high_value_information.md` | `0739f2a4c815c6dab9436816f1648c0346497f25414bea2760b1b4d2bb48c40a` |

`employment_group_period` brukes bare for den samlede OUS-overskriften i den
profesjonelle Word-masteren. `authority_anchor` og `include_in_cv` er
validerings-/renderingsmetadata, ikke nye fakta.

<!-- CV_BASELINE_DATA_START -->
```json
{
  "baseline_version": "0.7.0",
  "candidate": {
    "full_name": "Vegard Håland",
    "phone": "+47 905 26 886",
    "email": "vegard-haaland@outlook.com",
    "location": "Oslo",
    "linkedin": null
  },
  "employment": [
    {
      "employment_id": "EMP_OUS_ANALYSE",
      "sort_order": 1,
      "employer": "Oslo universitetssykehus HF",
      "formal_title": "Rådgiver Økonomi og IKT",
      "unit": "Direktørens stab, Analyseavdelingen",
      "location": "Oslo",
      "period": "12.2023-d.d.",
      "employment_group_period": "03.2023-d.d.",
      "default_bullets": [
        "Utvikler og forbedrer beslutningsstøtte for økonomi, bemanning, aktivitet/DRG og pasientflyt ved hjelp av Power BI, DAX, Power Query, Excel/VBA, SQL og prosjektavhengig R/Python.",
        "Omsetter brede behov til avgrensede løsningsarkitekturer, kontroller, dokumentasjon og brukbare leveranser for ledere, controllere, fagmiljøer og tekniske samarbeidspartnere.",
        "Bidrar til strukturering av leveranser, workshops, onboarding og kompetanseoverføring i tverrfaglige oppdrag."
      ],
      "always_include": true,
      "authority_anchor": "EMP-OUS-001"
    },
    {
      "employment_id": "EMP_OUS_BAR",
      "sort_order": 2,
      "employer": "Oslo universitetssykehus HF",
      "formal_title": "Rådgiver Økonomi og IKT",
      "unit": "Barne- og ungdomsklinikken, Stab",
      "location": "Oslo",
      "period": "03.2023-11.2023",
      "default_bullets": [
        "Overtok etter opplæring den tildelte månedsoppgjørsflyten med periodisering, reversering, avstemming, kvalitetssikring, resultatforklaring og rapportering til ledere.",
        "Utviklet Excel/VBA-verktøy for konvertering og validering ved overgangen til REGERP og bidro i budsjett, prosjektøkonomi og klinikkens økonomi-/aktivitetsrapportering."
      ],
      "always_include": true,
      "authority_anchor": "CLM-BAR-001"
    },
    {
      "employment_id": "EMP_TKS_HEIS",
      "sort_order": 3,
      "employer": "TKS Heis",
      "formal_title": "Hjelpearbeider",
      "unit": null,
      "location": null,
      "period": "07.2015-08.2021",
      "default_bullets": [
        "Sesong- og heltidsarbeid sammen med heismontører under studiene, i et praktisk og sikkerhetssensitivt arbeidsmiljø."
      ],
      "always_include": true,
      "authority_anchor": "July 2015–August 2021"
    },
    {
      "employment_id": "EMP_AHLSELL",
      "sort_order": 4,
      "employer": "Ahlsell",
      "formal_title": "Butikkmedarbeider/vikar",
      "unit": "Auglendsmyra",
      "location": "Stavanger",
      "period": "02.2015-04.2015",
      "default_bullets": [
        "Arbeidet med varemottak, lager, bestilling, salg og kundekontakt."
      ],
      "always_include": true,
      "authority_anchor": "February–April 2015"
    },
    {
      "employment_id": "EMP_LUFTFORSVARET",
      "sort_order": 5,
      "employer": "Luftforsvaret",
      "formal_title": "Vakt- og sikringssoldat",
      "unit": "Sola",
      "location": "Sola",
      "period": "03.2014-02.2015",
      "default_bullets": [
        "Utførte vakthold, adgangskontroll og alarmrespons med tydelige prosedyrer og ansvar."
      ],
      "always_include": true,
      "authority_anchor": "March 2014–February 2015"
    },
    {
      "employment_id": "EMP_SECTOR_ALARM",
      "sort_order": 6,
      "employer": "Sector Alarm",
      "formal_title": "Sikkerhetskonsulent",
      "unit": null,
      "location": "Stavanger",
      "period": "10.2013-03.2014",
      "default_bullets": [
        "Gjennomførte behovsavklaring, pristilbud, direkte salg og kundedialog."
      ],
      "always_include": true,
      "authority_anchor": "October 2013–March 2014"
    }
  ],
  "education": [
    {
      "education_id": "EDU_UIA_AI",
      "sort_order": 1,
      "institution": "Universitetet i Agder",
      "qualification": "Masterprogram i kunstig intelligens",
      "field": "Kunstig intelligens",
      "period": "2024-d.d.",
      "status": "Pågående",
      "details": [],
      "include_in_cv": true,
      "authority_anchor": "EDU-001"
    },
    {
      "education_id": "EDU_NTNU_ECON",
      "sort_order": 2,
      "institution": "NTNU",
      "qualification": "Master i samfunnsøkonomi",
      "field": "Samfunnsøkonomi",
      "period": "2020-2022",
      "status": "Fullført",
      "details": [
        "Relevante fag: videregående og anvendt økonometri, anvendt tidsserieøkonometri og videregående matematisk analyse."
      ],
      "include_in_cv": true,
      "authority_anchor": "EDU-002"
    },
    {
      "education_id": "EDU_UIB_ECON",
      "sort_order": 3,
      "institution": "Universitetet i Bergen",
      "qualification": "Bachelor i samfunnsøkonomi",
      "field": "Samfunnsøkonomi",
      "period": "2017-2020",
      "status": "Fullført",
      "details": [
        "Bred økonomifaglig bakgrunn, blant annet statistikk og økonometri, offentlig økonomi, arbeidsmarked, konkurranse, finans og bedriftsøkonomi."
      ],
      "include_in_cv": true,
      "authority_anchor": "EDU-003"
    },
    {
      "education_id": "EDU_CALGARY",
      "sort_order": 4,
      "institution": "Ernest Manning High School, Calgary",
      "qualification": "Videregående utdanning",
      "field": "Naturfag og avansert matematikk",
      "period": "2011-2013",
      "status": "",
      "details": [],
      "include_in_cv": false,
      "authority_anchor": "EDU-004"
    }
  ],
  "languages": [
    {
      "language": "Norsk",
      "level": "Morsmål"
    },
    {
      "language": "Engelsk",
      "level": "Flytende skriftlig og muntlig"
    }
  ],
  "other_sections": [
    {
      "section_id": "OTHER_TRUST",
      "heading": "Tillitsverv",
      "items": [
        "Styremedlem/beboerrepresentant, Solheimslien studentboliger, 10.2017-01.2019.",
        "Økonomiansvarlig og nestleder, 01.2019-01.2020.",
        "Styreleder og økonomiansvarlig, 01.2020-08.2020."
      ]
    },
    {
      "section_id": "OTHER_COURSES",
      "heading": "Kurs",
      "items": [
        "Sanitet nivå 2, 04.2014."
      ]
    }
  ],
  "references_text": "Oppgis ved forespørsel."
}
```
<!-- CV_BASELINE_DATA_END -->
