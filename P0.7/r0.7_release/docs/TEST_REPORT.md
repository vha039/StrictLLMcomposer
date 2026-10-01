# Jobbsøk_26 P0.7 — testrapport

Testdato: 2026-08-01  
Mål for bevisløypen: P0.7-arbeidskopien, ikke reell Terra/Sol-produksjon.

## Sammendrag

| Status | Antall | Betydning |
|---|---:|---|
| PASS | 32 automatiske tester | Kjørte og bestått |
| BLOCKED | 2 PowerShell-runtime-tester | Skippet fordi pwsh/Windows PowerShell mangler |
| FAIL | 0 | Ingen |
| NOT RUN | 2 produksjonsaktiviteter | Reelle modellstager og reell vacancy-pilot |

P0.6-baselinen ble kjørt før migrering: 30 PASS og 3 PowerShell-avhengige
skips. P0.7s fulle suite er den gjeldende releaseporten.

## Utførte tester

| Testområde | Kommando/metode | Status | Faktisk bevis |
|---|---|---|---|
| Python compile/import | primary-runtime Python, py_compile og unittest-import | PASS | ingest.py, finalize.py og hele testsuiten importerte |
| Kandidat-/masterintegritet | SHA-256 mot frosne verdier | PASS | Tre myndigheter og to originale DOCX-mastere er byteidentiske |
| JSON, schema og baseline | Marker parsing, Draft 2020-12/fallback og eksempelpackage | PASS | P0.7 schema, baseline 0.7.0 og job_identity.json validert |
| Aktiv arkitektur | Statisk kontraktstest | PASS | Fire stages, kun tre scripts og ingen API-/orchestratorrest |
| Ingest positiv | PDF-ekstraksjon, hash/page-markører og Markdown-gjenbruk | PASS | Exit 0 og korrekt stdout |
| Ingest negativ | Kort Markdown, svak/dominert PDF, invalid/duplikat/prefiks-ID | PASS | Jobblocker eller konfigurasjonsfeil uten stille fallback |
| Advance statisk | Guard- og forbudsinspeksjon | PASS | Krever Stage 2-artifacts, identity, done, blocker, status og split |
| Advance runtime positiv/negativ | Conditional PowerShell-tester | BLOCKED | Ingen PowerShell-runtime i miljøet |
| Finalizer positiv | Letter, no-letter, portal, expected/completed, identity og review | PASS | Check-only returnerte 0 for komplett fixture |
| Finalizer negativ | Manglende package/done/flag/identity-anchor, blocker, mismatch, limits, tags, timeout | PASS | Returnerte job-feil/exit 1 eller config exit 2 |
| CV-overstyringer | Eldre EMP_TKS_HEIS-overstyring | PASS | Synlig rendret i to-siders CV |
| Rendering | LibreOffice, originalmastere og PDF-validering | PASS | Tett CV 2s, sparsom CV 2s, søknad 1s |
| Controlled E2E | Syntetisk vacancy → ingest → Stage 1/2/3/4 fixtures → check-only → DOCX/PDF | PASS | To pakker rendret; ingen modellchat påstått |
| Fysisk CLI-smoke | ingest.py og finalize.py --check-only | PASS | Begge kommandoer exit 0 mot kontrollert fixture |
| Visuell DOCX QA | documents render_docx.py | PASS | 5/5 sider inspisert |
| Visuell PDF QA | pdftoppm fra finalizer-PDF | PASS | 5/5 sider inspisert |
| Private/offentlige skiller | Renderte DOCX/PDF og portalfil | PASS | Ingen control tags, interne IDs eller review-flagg i arbeidsgiverfiler |

Den fulle automatiske kommandoen var:

~~~powershell
python -m unittest discover -s tests -p "test_*.py" -v
~~~

Resultat: 34 tester kjørt, 32 bestått, 2 skippet som BLOCKED.

## Visuell QA

Følgende kontrollerte fixtures ble rendret og inspisert side for side både som
DOCX-renderinger og som finalizerens PDF:

| Fixture | Sider | Kontrollert |
|---|---:|---|
| Tett CV med eldre employment-overstyring | 2 | A4, kronologi, override, ingen klipping eller blankfeilark |
| Sparsom CV | 2 | A4, komplett CV, balansert tosidig layout |
| Package med søknadsbrev, unit/reference og portalsvar | 1 brevside | A4, avslutning/signatur, unit/reference, ingen privat lekkasje |
| Package uten søknadsbrev | 0 brevside | Kun CV; ingen Application-filer |
| Portal | 1 Markdown-fil | Eksakt spørsmål/svar og hard grensekontroll |

Selektiv tekst ble validert i alle PDF-er. CV-sidegrensen er 2 og
søknadssidegrensen er 1; overskridelse har egen negativtest.

## BLOCKED og NOT RUN

### BLOCKED

PowerShell-runtime finnes ikke i Linux-miljøet. Følgende er ikke beskrevet som
runtime-PASS:

~~~powershell
pwsh -NoProfile -File .\scripts\advance.ps1 -Cluster B01_C01_process_digitalization -Root .
python -m unittest tests\test_advance.py -v
~~~

Den statiske advance-kontrakten og alle fixturebaserte guards er PASS. På en
Windows/PowerShell-maskin skal begge kommandoene kjøres før produksjonsbruk.

### NOT RUN

- Reelle Terra-/Sol-chatter for Stage 1–4.
- Reell vacancy-pilot.

Ingen godkjent reell vacancy og ingen separate manuelle stagechatter var
tilgjengelig. Kontrollert fixture-E2E er derfor bevis for systemet, ikke
påstand om produksjonsmodelloutput.

### BLOCKED_ASSET

Ingen. Alle kandidatmyndigheter og begge originale Word-mastere var
tilgjengelige og hashverifiserte.

## Releasearkiv

- ZIP-medlemmer: 52, én per manifestfil.
- CRC: gyldig (zipfile.testzip() returnerte ingen feil).
- Medlemsrekkefølge og -sett: identisk med releasefolderen; ingen duplikater.
- Deterministisk dobbeltbygg: byteidentisk.
- Endelig SHA-256 er registrert i den separate releaseverifikasjonen og i
  leveringsmeldingen etter at disse rapportene er frosset.
