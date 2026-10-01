# Finalization traceability — 2026-08-25

The executing registry in `runtime/tests/test_traceability.py` prevents named
coverage from disappearing; it does not promote helper tests to public or
target evidence.

## Material trust boundaries

| Boundary | Strongest current evidence | Result |
|---|---|---|
| Maintained-root independence | existing public metamorphism + frozen tamper suite | PASS `PUBLIC_CLI` |
| Freeze staged-copy coherence | disposable copy-mutation public command | PASS `PUBLIC_CLI_FAULT_PROBE` |
| Handoff and Stage-3 completion | emitted commands executed in all four modes | PASS `PUBLIC_CLI` |
| Stage-3 pair preservation | injected second current-write failure | PASS `PUBLIC_CLI_FAULT_PROBE` |
| Finalize only after review | missing-review finalize/status/context probe | PASS `PUBLIC_CLI` |
| Held render destination | normal and `--force` two-job probes with changed final | PASS `PUBLIC_CLI_FAULT_PROBE` |
| Local versus shared failure | malformed receipt/unmodelled promotion; ENOSPC promotion/receipt | PASS `PUBLIC_CLI_FAULT_PROBE` |
| Receipt-bound output bytes | existing mutation matrix + receipt-write rollback | PASS deterministic/public fault |
| Repeated external export | two exports to one directory; canonical hashes unchanged | PASS `PUBLIC_CLI` |
| Locked read-only status | live canonical locked DOCX | PASS `PUBLIC_CLI`; render marked unverifiable |
| Parent-safe branch | existing public reuse/invalidation + staged copy mutation | PASS public/fault |
| Declared formats | 20 retained typed artifacts; direct invalid date/time probes | PASS deterministic |
| Template point-of-use | existing public mutations + preparation check | PASS public/static |
| Target Word long name/PDF/glyph | target `test_t19_*` group | PASS (target session 2026-08-25); all 10 executed |
| Human Word survives forced timeout | live forced timeout with human session open | PASS (target session 2026-08-25); owned PID 24508 terminated, human session untouched |
| Sparse/normal/dense usability | `VISUAL_HUMAN` | `BLOCKED_USER` |
| Actual surface/file/privacy facts | `USER_ACCOUNT` | `BLOCKED_USER` |
| Independent repaired-byte review | installed `codex.exe` | `BLOCKED_USER` (access denied) |
| Fresh deterministic slice | retained `slice_evidence.json` and hashes | PASS `PUBLIC_CLI` |

## Acceptance summary

| IDs | Scope/result |
|---|---|
| ACC-01–11, ACC-13–19 | PASS at the deterministic/public scope named by the suite and probes. |
| ACC-12 | Both retained DOCX outputs pass; target Word PDF portion remains `BLOCKED_USER`. |
| ACC-20 | Not mechanical; real-job pilot and human scoring not run. |

Full-suite evidence: `236 passed, 10 target-Word skips` in 79.83 seconds.
Retained slice: 21 expected command outcomes, 0 unexpected. Fault probes are
disposable and not represented as new committed tests or a harness.
