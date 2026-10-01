# Jobbsøk_26 P0.7 — implementeringsrapport

## Status

P0.7 er implementert som en ren, manuelt operert firestage-release. Den aktive
flyten inneholder ingen API-/SDK-orchestrator, modellrunner, retry-motor,
database, cache, automatisk research eller innsending. P0.6 er ikke endret.

- Release: Jobbsok_26_P0.7/
- Pre-final-test-backup: Jobbsok_26_P0.7_pre_final_test_backup/
- Baseline som ble migrert: Jobbsok_26_P0.6/
- Originalasset-backup kontrollert mot: _backups/P0.6_source_assets/

## Inventory og migreringsklassifisering

| Område | Klassifisering | P0.7-resultat |
|---|---|---|
| Tre kandidatmyndigheter | KEEP | Byteidentiske, hash-låste og fortsatt eneste faktamyndigheter |
| Originale CV-/søknadsmastere | KEEP | Byteidentiske content-control-mastere, brukt av finalizer |
| P0.6 fysisk stage-struktur | MODIFY | Beholdt fire isolerte stages, oppgradert til P0.7-bølger og Phase A/B |
| P0.6 ingest | MODIFY | Meningsfull Markdown/PDF, batch-/ID-kontroll og proporsjonal svaksiderutine |
| P0.6 advance | MODIFY | Autoritativ Stage 2-gate med identity, done, blocker og statuskrav |
| P0.6 finalizer | MODIFY | Forventet/ferdigstilt sammenlikning, cross-stage identity, sidegrenser og timeout |
| P0.6 package schema/baseline | MODIFY | Versjon 0.7, batch_id, unit/reference og dynamisk CV-overstyring |
| Root/stage-instrukser | MODIFY | 12-prompt topologi, modellruting, 10+10/5+5 og recovery |
| P0.6 tests/fixtures | MODIFY | P0.7 positive, negative, E2E- og renderingfixturer |
| Historisk P0.5.x API-runner | REMOVE_FROM_ACTIVE_PATH | Ble ikke kopiert inn i aktiv release; historikk står utenfor |
| Historiske output/reporter | ARCHIVE | P0.6-historikk beholdt utenfor aktiv drift |
| P0.7 routing/pilotlogg/identitetsfixture | ADD | MODEL_ROUTING.md, HYBRID_PILOT_LOG.csv, job_identity.json og nye kontrakter |
| Manglende originalasset | BLOCKED_ASSET | Ingen |

Aktive scripts er nøyaktig ingest.py, advance.ps1 og finalize.py.

## Implementert måltilstand

- Fire manuelt startede og fysisk isolerte stages, én modellprompt per
  stage-instans og intern Phase A → midpoint/checkpoint → Phase B
  source-first self-audit.
- To XL-makroklynger à omtrent 20 jobber, to evidence lanes per makroklynge,
  fire miniklynger à omtrent 10 jobber, 10+10- og 5+5-arbeidsbølger og
  12-prompt HappyPath.
- Modellruting: Terra Max (Stage 1), Sol Max (Stage 2), Terra Extra High med
  selektiv Max (Stage 3), Sol Extra High med selektiv Max (Stage 4).
- Kandidatblind Stage 1 med job_identity.json; Sol-eid retrieval og
  CLUSTER_EVIDENCE_BASE.md/MINICLUSTER_SPLIT.json i Stage 2; Terra-drafting i
  Stage 3; konstruktiv, non-veto Sol Mirror i Stage 4.
- job_identity.json kryssvalideres mot package, batchprefiks,
  makro-/miniklynge, mappesti, employer og title.
- Originalmasterbasert DOCX/PDF-rendering, A4-validering, selekterbar PDF-tekst
  og privat separasjon av review-flagg.

## P0.6.1-hardening

| Gate | Status |
|---|---|
| Alle schema-tillatte employment-overstyringer rendres, også eldre roller | Implementert og testet med EMP_TKS_HEIS |
| Forventede vs. ferdigstilte jobber; ingen falsk global PASS | Implementert og negativtestet |
| Identity/path/batch/cluster/employer/title-kryssvalidering | Implementert og negativtestet |
| Stage 2 completeness, _DONE.md, BLOCKED.md og status før advance | Implementert; runtime-test er miljøblokkert |
| Meningsfull Markdown/PDF, IDs, prefiks og samlet lesbarhet ved ingest | Implementert og testet |
| CV ≤2 sider, brev ≤1 side, unit/reference og converter-timeout | Implementert og render-testet |
| Stage 4 source, _DONE.md, aktiv blocker og review-headinger | Implementert og negativtestet |
| Ingen private tags/IDs/placeholders i employer-facing filer | Implementert og testet |
| Ingen FINALIZE_REPORT.md eller output/INDEX.md | Implementert og testet |

## Originalassets brukt

| Asset | SHA-256 |
|---|---|
| context/Work_experience.md | 0b39a5105f0d809d1bc9a917665bc69c619eb059253a779079b37304b49a2f9d |
| context/Education.md | 75e238890215cbc02c3bc59cdaaeb43f467ae7d512e9b5a9c4723ccc0c4580f8 |
| context/Other_high_value_information.md | 58a8f88f9eb627847152d684b19d7938c42da7d173a57a7fff58728a25ae5bf8 |
| context/templates/CV_MASTER.docx | c3809748fe26dd5a7ae0a146d940a15e1b3326036ae5f7fac9fd2be02292e8c5 |
| context/templates/APPLICATION_MASTER.docx | dfd24125f921863da23932b8be3255df51cc8a4ee9a97c6a602a33dedb241409 |

## Små, dokumenterte kompatibilitetstilpasninger

| Tilpasning | Begrunnelse | Bevis |
|---|---|---|
| Bounded JSON-schema fallback når jsonschema ikke kan importeres | Holder schemaet kjørbart i begrensede runtime-miljøer uten å utvide arkitekturen | Kontrakt- og schema-tester passerer; normal installasjon pinner jsonschema |
| Kort enkeltsides-PDF kan aksepteres fra 120 tegn med eksplisitt varsel | Hindrer urimelig blokkering av legitim kort vacancy; dokument dominert av svake sider blokkeres fortsatt | Positiv og negativ ingest-test |

Ingen utsatt P0.7-systemflate ble introdusert.

## Begrensninger og utsatt arbeid

- BLOCKED_ASSET: ingen.
- BLOCKED: faktisk PowerShell-kjøring av advance.ps1; pwsh/Windows PowerShell
  er ikke installert i dette miljøet.
- NOT RUN: reelle Terra/Sol-stager og reell vacancy-pilot. Bare kontrollerte
  fixtures ble brukt; ingen modellchat ble fabrikkert som gjennomført.
- Bevisst utenfor P0.7: API-/SDK-runner, codex exec, session resume, retry,
  working-lag, database/state-machine, semantic cache/embeddings, Luna/Ultra
  som standardrute, subagents, LLM-judge, automatisk arbeidsgiverresearch og
  innsending. Den dokumenterte, ikke-standard Luna-økonomitesten kan først
  vurderes etter første makroklynge.

## Første kommando

~~~powershell
python scripts\ingest.py stg1_analyze\input
~~~
