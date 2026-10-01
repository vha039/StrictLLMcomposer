# Jobbsøk_26 P0.7 package contract

Denne kontrakten er felles for Stage 3, Stage 4,
`templates/EXAMPLE_FINAL_PACKAGE.json` og `scripts/finalize.py`.

- Stage 3 bruker `source_stage: STAGE3_DRAFT`.
- Stage 4 bruker `source_stage: STAGE4_FINAL`.
- `contract_version` er `0.7`.
- Pakken inneholder bare dynamiske CV-soner; kontakt, formell kronologi,
  utdanning, språk og referanser kommer fra `CV_BASELINE.md`.
- `application` er `null` når brev ikke skal produseres.
- Portalgrenser er harde og valideres både i schema og Python.
- Ukjente toppfelt eller nested felt avvises.

<!-- PACKAGE_SCHEMA_START -->
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Jobbsok26DynamicApplicationPackage",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "contract_version",
    "source_stage",
    "job",
    "cv_overrides",
    "application",
    "portal_answers"
  ],
  "properties": {
    "contract_version": {
      "const": "0.7"
    },
    "source_stage": {
      "enum": [
        "STAGE3_DRAFT",
        "STAGE4_FINAL"
      ]
    },
    "job": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "job_id",
        "batch_id",
        "macro_cluster_id",
        "mini_cluster_id",
        "employer",
        "title",
        "language",
        "letter_required"
      ],
      "properties": {
        "job_id": {
          "type": "string",
          "pattern": "^B[0-9]{2}_J[0-9]{3}_[a-z0-9_]+$",
          "maxLength": 120
        },
        "batch_id": {
          "type": "string",
          "pattern": "^B[0-9]{2}$"
        },
        "macro_cluster_id": {
          "type": "string",
          "pattern": "^B[0-9]{2}_C[0-9]{2}_[a-z0-9_]+$",
          "maxLength": 100
        },
        "mini_cluster_id": {
          "type": "string",
          "pattern": "^B[0-9]{2}_C[0-9]{2}[AB]_[a-z0-9_]+$",
          "maxLength": 101
        },
        "employer": {
          "type": "string",
          "minLength": 2,
          "maxLength": 200
        },
        "title": {
          "type": "string",
          "minLength": 2,
          "maxLength": 200
        },
        "unit": {
          "type": [
            "string",
            "null"
          ],
          "maxLength": 200
        },
        "reference": {
          "type": [
            "string",
            "null"
          ],
          "maxLength": 200
        },
        "language": {
          "const": "nb-NO"
        },
        "letter_required": {
          "type": "boolean"
        }
      }
    },
    "cv_overrides": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "baseline_version",
        "profile",
        "key_competencies",
        "experience_overrides"
      ],
      "properties": {
        "baseline_version": {
          "type": "string",
          "minLength": 1
        },
        "profile": {
          "type": "string",
          "minLength": 80,
          "maxLength": 1400
        },
        "key_competencies": {
          "type": "array",
          "minItems": 4,
          "maxItems": 8,
          "uniqueItems": true,
          "items": {
            "type": "string",
            "minLength": 3,
            "maxLength": 180
          }
        },
        "experience_overrides": {
          "type": "array",
          "minItems": 1,
          "maxItems": 4,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "employment_id",
              "bullets"
            ],
            "properties": {
              "employment_id": {
                "type": "string",
                "pattern": "^[A-Z0-9_]+$"
              },
              "bullets": {
                "type": "array",
                "minItems": 1,
                "maxItems": 5,
                "items": {
                  "type": "string",
                  "minLength": 20,
                  "maxLength": 550
                }
              }
            }
          }
        }
      }
    },
    "application": {
      "oneOf": [
        {
          "type": "null"
        },
        {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "opening",
            "body_paragraphs",
            "closing"
          ],
          "properties": {
            "opening": {
              "type": "string",
              "minLength": 40,
              "maxLength": 800
            },
            "body_paragraphs": {
              "type": "array",
              "minItems": 1,
              "maxItems": 5,
              "items": {
                "type": "string",
                "minLength": 60,
                "maxLength": 1500
              }
            },
            "closing": {
              "type": "string",
              "minLength": 30,
              "maxLength": 600
            }
          }
        }
      ]
    },
    "portal_answers": {
      "type": "array",
      "maxItems": 20,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "question_id",
          "question",
          "answer",
          "max_words",
          "max_chars"
        ],
        "properties": {
          "question_id": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100
          },
          "question": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1000
          },
          "answer": {
            "type": "string",
            "minLength": 1
          },
          "max_words": {
            "type": [
              "integer",
              "null"
            ],
            "minimum": 1
          },
          "max_chars": {
            "type": [
              "integer",
              "null"
            ],
            "minimum": 1
          }
        }
      }
    }
  }
}
```
<!-- PACKAGE_SCHEMA_END -->

## Tilleggskontroller i finalizer

`finalize.py` skal i tillegg kreve:

- finalisering bare fra `STAGE4_FINAL`;
- baselineversjon lik `CV_BASELINE.md`;
- komplett forventet/ferdigstilt jobbmengde: `stg4_mirror/input` definerer
  forventede jobber og `stg4_mirror/output` definerer ferdigstilte pakker;
- `job_identity.json`, pakke, mappe, batch-prefiks, makro-/miniklynge,
  arbeidsgiver og tittel er konsistente;
- korrekt `STAGE4_FINAL`-kilde, Stage 4-`_DONE.md` og ingen aktiv
  `BLOCKED.md` før en jobb kan godkjennes eller rendres;
- brevobjekt når `letter_required=true`;
- `application=null` når `letter_required=false`;
- portalgrenser overholdt;
- alle employment-ID-er kjent og uten duplikater;
- alle `always_include`-poster rendret og alle schema-tillatte
  employment-overstyringer enten synlig rendret eller eksplisitt avvist;
- CV på høyst to A4-sider og søknadsbrev på høyst én A4-side;
- `unit` og `reference` rendres når de finnes;
- obligatoriske private review-flagg har korrekt heading-struktur;
- ingen placeholder eller intern strategi-/evidensterminologi i
  arbeidsgivertekst;
- identisk jobbidentitet og baselineversjon i draft/final;
- finalens employment-ID-er er samme sett eller et subset av draftens;
- ingen overskriving uten `--force`.

Finalizer skriver aldri `FINALIZE_REPORT.md`, `output/INDEX.md` eller en
syntetisk global PASS-rapport. Exit-kode og stdout uttrykker kun den faktiske
kjøringen.

Employer-facing tekst skal aldri inneholde lokale evidens-ID-er, `decision
test`, `review flag`, `single backbone`, `shortlist thesis`,
`CLUSTER_EVIDENCE_BASE`, `package_blueprint`, template-tags eller private
flagg.
