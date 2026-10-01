# Anti-regression audit — 2026-08-25

| ID | Status | Protected property and current evidence |
|---|---|---|
| AR-01 | PASS (target session 2026-08-25) | Word COM remains the configured baseline and produces verified PDFs on target; full suite 246 passed, 0 skipped. |
| AR-02 | PASS | Master repair remains reproducible/idempotent with exact 17/7 control inventory. |
| AR-03 | PASS (target session 2026-08-25) | Norwegian glyphs survive into the target PDF (`test_t19_norwegian_glyphs_survive_to_the_pdf`). Sparse/normal/dense *visual* judgement remains `DOD-18`. |
| AR-04 | PASS | `artifact_hash` excludes only finalization; date stales render, not semantic review identity. |
| AR-05 | PASS | Norwegian filename folding remains readable and tested. |
| AR-06 | PASS | Active runs resolve every maintained input through verified `FrozenRunAssets`; staged copies verify before exposure. |
| AR-07 | PASS | `EV:` factual and `BL:` mechanical namespaces remain distinct. |
| AR-08 | PASS | Exactly three manually invoked semantic stages remain. |
| AR-09 | PASS | Stage 3 remains truth-bounded/elastic; no strategy or quality judge. |
| AR-10 | PASS | PDF failure remains render degradation, never semantic failure or a product branch. |
| AR-11 | PASS | Foreign DOCX remains no-clobber; held owned DOCX restores exactly; lock text never recommends force as a remedy. |
| AR-12 | PASS | No production network/model/contact/submission surface. |
| AR-13 | PASS | Malformed/unmodelled local failures preserve peers; shared exhaustion aborts only after rollback. |
| AR-14 | PASS | Density/page/cardinality signals remain warnings. |
| AR-15 | PASS | Recovery remains bounded/manual; no orchestrator, scheduler or retry engine. |
| AR-16 | PASS (target session 2026-08-25) | Stdlib OOXML, root-tag/package preservation and one-shot read-only macro-disabled COM remain; target Word opens and exports the generated documents. |
| AR-17 | PASS | Active runs do not reread `inbox/` or maintained roots. |
| AR-18 | PASS | Warnings remain non-failing; stale/current gates act directly. |
| AR-19 | PASS | Baseline↔authority conflict continues to block freeze/branch. |
| AR-20 | PASS (target session 2026-08-25) | Ownership is resolved from the document window handle after `Documents.Open` and rechecked as `WINWORD.EXE`. Forced timeout with a human Word session open terminated only automation PID 24508 and left the human session and every pre-existing process untouched; unresolved ownership terminates nothing. |

Legacy/orphan outputs remain invisible; branching remains parent-immutable and
topological; repeated explicit export remains non-authoritative. The lock and
foreign-edit diagnostics are mutually exclusive.

Result: every executable deterministic anti-regression check passes. DOD-23
remains `BLOCKED_USER` only for target-session evidence.
