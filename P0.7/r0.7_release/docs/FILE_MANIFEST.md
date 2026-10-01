# Jobbsøk_26 P0.7 — filmanifest

Dette manifestet dekker nøyaktig 52 releasefiler før ZIP-bygg. Paths er
relative til Jobbsok_26_P0.7/.

| Path | Status | Rolle |
|---|---|---|
| .gitignore | KEEP | Holder cache, venv og runtime-output utenfor release |
| AGENTS.md | MODIFY | Universelle P0.7-grenser |
| MODEL_ROUTING.md | ADD | Låst standardruting og selektiv eskalering |
| START_HERE.md | MODIFY | Installasjon, preflight, stages, continuation og kommandoer |
| requirements.txt | KEEP | Pinned Python-avhengigheter |
| context/CV_BASELINE.md | MODIFY | Verifisert P0.7 dynamisk-CV-baseline |
| context/Education.md | KEEP | Kandidatmyndighet for utdanning |
| context/NORWEGIAN_APPLICATION_CORE.md | MODIFY | Norsk runtimekjerne med batchvariasjon |
| context/Other_high_value_information.md | KEEP | Kandidatmyndighet for identitet/støttefakta |
| context/PACKAGE_CONTRACT.md | MODIFY | P0.7 package schema og finalizerkontroller |
| context/PERSUASION_CALIBRATION.md | MODIFY | P0.7 eksplisitt kalibrering |
| context/Work_experience.md | KEEP | Kandidatmyndighet for arbeidserfaring |
| context/templates/APPLICATION_MASTER.docx | KEEP | Original A4 søknadsmaster |
| context/templates/CV_MASTER.docx | KEEP | Original A4 CV-master |
| context/templates/EXAMPLE_FINAL_PACKAGE.json | MODIFY | Gyldig P0.7 eksempelpackage |
| docs/FILE_MANIFEST.md | MODIFY | Dette fullstendige manifestet |
| docs/HYBRID_PILOT_LOG.csv | ADD | Minimal operatorlogg for kalibreringspilot |
| docs/IMPLEMENTATION_REPORT.md | MODIFY | Migration, hardening og begrensninger |
| docs/TEST_REPORT.md | MODIFY | PASS/FAIL/BLOCKED/NOT RUN-bevis |
| output/.gitkeep | KEEP | Tom final output-root |
| scripts/advance.ps1 | MODIFY | Autoritativ Stage 2 → Stage 3-gate |
| scripts/finalize.py | MODIFY | P0.7 validering og originalmaster-rendering |
| scripts/ingest.py | MODIFY | P0.7 input/ID-/lesbarhetskontroll |
| stg1_analyze/AGENTS.md | MODIFY | Kandidatblind Terra Max-kontrakt |
| stg1_analyze/input/.gitkeep | KEEP | Tom Stage 1 input |
| stg1_analyze/output/.gitkeep | KEEP | Tom Stage 1 output |
| stg2_strategy/AGENTS.md | MODIFY | Sol Max evidence lanes og blueprints |
| stg2_strategy/input/.gitkeep | KEEP | Tom Stage 2 input |
| stg2_strategy/output/.gitkeep | KEEP | Tom Stage 2 output |
| stg3_write/AGENTS.md | MODIFY | Terra Extra High drafting-kontrakt |
| stg3_write/input/.gitkeep | KEEP | Tom Stage 3 input |
| stg3_write/output/.gitkeep | KEEP | Tom Stage 3 output |
| stg4_mirror/AGENTS.md | MODIFY | Sol Extra High non-veto Mirror-kontrakt |
| stg4_mirror/input/.gitkeep | KEEP | Tom Stage 4 input |
| stg4_mirror/output/.gitkeep | KEEP | Tom Stage 4 output |
| tests/__init__.py | MODIFY | P0.7 testsuite-markør |
| tests/support.py | MODIFY | Kontrollerte P0.7 fixture-hjelpere |
| tests/test_contracts.py | MODIFY | Hash, kontrakt, routing og template-tester |
| tests/test_ingest.py | MODIFY | Positive/negative P0.7 ingest-tester |
| tests/test_advance.py | MODIFY | Statisk og conditional PowerShell-test |
| tests/test_finalize.py | MODIFY | P0.6.1-hardening, rendering og negative gates |
| tests/test_e2e.py | MODIFY | Kontrollert P0.7 E2E-fixture |
| tests/test_stage_artifacts.py | MODIFY | Stageartifact-kontrakter |
| tests/fixtures/stage_artifacts/BATCH_STATUS.md | MODIFY | Full Wave 1/midpoint/Wave 2-statusfixture |
| tests/fixtures/stage_artifacts/BLOCKED.md | KEEP | Blockerfixture |
| tests/fixtures/stage_artifacts/CLUSTER_EVIDENCE_BASE.md | MODIFY | Evidence lanes-fixture |
| tests/fixtures/stage_artifacts/MINICLUSTER_SPLIT.json | KEEP | Splitfixture |
| tests/fixtures/stage_artifacts/_DONE.md | KEEP | Completion-fixture |
| tests/fixtures/stage_artifacts/job_identity.json | ADD | P0.7 identity-anchor fixture |
| tests/fixtures/stage_artifacts/package_blueprint.md | KEEP | Blueprint-fixture |
| tests/fixtures/stage_artifacts/review_flags.md | KEEP | Privat review-fixture |
| tests/fixtures/stage_artifacts/vacancy_analysis.md | MODIFY | Stage 1 explicit-facts fixture |

## Ekskludert fra release

- P0.6 og eldre releaser/historikk.
- Pre-final-test-backupen.
- Alle testgenererte DOCX/PDF/PNG-er, LibreOffice-profiler og Python-cache.
- Tomme production input-/output-mapper utover deres .gitkeep-markører.

## Pakkelås

Releasefolderen inneholder 52 filer. Jobbsok_26_P0.7_Release.zip inneholder
samme 52 medlemmer i sortert, deterministisk rekkefølge; CRC er gyldig og to
uavhengige bygg var byteidentiske. Endelig SHA-256 står i den separate
releaseverifikasjonen og i leveringsmeldingen etter at manifestet er frosset.
