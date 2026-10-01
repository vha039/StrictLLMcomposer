# P0.9 Finalization Execution Ledger

> Mutable execution checkpoint. This file **reports** state; it does not define requirements.
> Repository evidence outranks this ledger whenever they disagree.

---

## 0. STATE REGISTER — read this first after any interruption or compaction

Keep this block under ~25 lines. It is the minimum needed to resume at the correct semantic point.

```text
GOAL:      P0.9 mechanical finalization to GO_FOR_TWO_JOB_SMOKE
SCOPE:     Roadmap package at P0.9/Process/goal_prep/Implementation_Roadmap/
PHASE:     Terminal reconciliation after P8
PROGRESS:  P0-P8 deterministic/public work complete; user gates remain
FACTS:     Full suite 236 passed / 10 target-Word skipped; fresh slice 21/0
FACTS:     Architecture stays 0.9.0; no real job or model chat consumed
REJECTED:  Blanket 0.9.1 bump; amendments A-01..A-04 (existing frozen rules suffice)
NEXT:      User closes target Word/visual/account gates, then fresh independent review
STOP:      GO_FOR_TWO_JOB_SMOKE | BLOCKED_USER | BLOCKED_HARD_CONSTRAINT
RULE:      Repository state outranks this register. Correct it before continuing.
```

**Update cadence.** Rewrite this block only after a *stable conclusion*: a phase exit, a recorded `DEV-*`/`DISC-*`, a durable fact worth surviving compaction, or a rejected route. Do not update it after every edit, and never paste tool output into it.

**`REJECTED` matters.** After compaction the most expensive failure is re-litigating a decision that was already investigated and closed. One line each: what was tried, why it was rejected.

---

## 1. Current checkpoint

- **Roadmap status:** `TERMINAL_BLOCKED_USER`
- **Current phase:** Terminal reconciliation after P8
- **Current task:** Await the four explicitly user-owned closures in §7
- **Last completed phase:** `P8` evidence regeneration and hygiene
- **Last verified checkpoint:** Full suite `236 passed, 10 skipped`; fresh slice `21 expected, 0 unexpected`
- **Current blocker:** Target Word/visual execution and actual account facts are unavailable in this session
- **Next action:** Run the listed target checks from an unlocked interactive session and supply Gate-10 facts
- **Working-tree state:** No usable Git metadata; nested `Build.zip` removed; local venv/cache paths ignored
- **Last full-suite result:** Canonical current tree, 2026-08-24: `236 passed, 10 skipped` in 69.41 s; every skip requires target Word COM

## 2. DFS / DOD status

| DFS | DOD | Status | Evidence / note |
|---|---|---|---|
| DFS-00 | DOD-00 | PASS | Core architecture and hard boundaries remain intact; terminal GO is tracked separately below |
| DFS-01 | DOD-01 | PASS | Public CLI validation/render unchanged after edits across all five maintained roots; frozen-byte tamper refused |
| DFS-02 | DOD-02 | PASS | Context/submission tooling owns every fixed field; model returns semantic fields only |
| DFS-03 | DOD-03 | PASS | Stale/wrong handoffs refuse before mutation; accepted artifacts derive current immediately |
| DFS-04 | DOD-05 | PASS | Shared semantic_state gates status/next/context/finalize/render |
| DFS-05 | DOD-06 | PASS | Public Stage-3 pair is prevalidated; review-only recovery leaves final untouched |
| DFS-06 | DOD-08 | PASS | Malformed one-job JSON and unmodelled render fault contained; frozen global fault aborts |
| DFS-07 | DOD-09 | PASS | Production failure wiring, correction/retry distinction and BLOCKED_MANUAL proven |
| DFS-08 | DOD-11 | PASS | Receipt verification binds exact semantic final/date/consumed frozen inputs/config and current output bytes |
| DFS-09 | DOD-12 | PASS | Full staged DOCX generation precedes promotion; PDF siblings cannot advance across a held/failed DOCX generation |
| DFS-10 | DOD-12 | PASS | Human/foreign files are no-clobber protected; pipeline ownership is retained across failed/recovered conversion |
| DFS-11 | DOD-13 | PASS | Public write resolver refuses traversal/protected/reparse escapes; explicit external exports remain non-authoritative |
| DFS-12 | DOD-14 | PASS | Parent compromise/refusal, unchanged reuse, bounded invalidation and interrupted exposure proven; P5 suite 40 passed |
| DFS-13 | DOD-16 | `BLOCKED_USER` | Short-path staging and honest timeout diagnostics pass; interactive Word/long-name/human-session proof skipped |
| DFS-14 | DOD-17 | `BLOCKED_USER` | Exact frozen master/hash/control and repair checks pass; target Word font/glyph/open subcheck unavailable |
| DFS-15 | DOD-18 | `BLOCKED_USER` | Forced break removed reproducibly; sparse/normal/dense target artifacts and human visual judgment unavailable |
| DFS-16 | DOD-04 / DOD-19 | `BLOCKED_USER` | Public context/status and actionable handoff pass; actual role surfaces/file access/account facts absent |
| DFS-17 | DOD-21 / DOD-22 / DOD-24 | PASS | Fresh replacement slice 21/0, regenerated scoped reports, ignored/cleaned residue and no nested archive |
| DFS-18 | DOD-19 / DOD-20 | `BLOCKED_USER` | Pilot scaffold and synthetic role mapping pass; actual account preflight and real pilot remain user/next-phase work |
| DFS-19 | DOD-15 | PASS | No amendment or revision change; exact 0.9.0 authority remains untouched |

Additional criteria without a one-to-one DFS row (`DOD-07`, `DOD-10`, `DOD-23`, `DOD-25`) are audited at their owning phase and at final completion.

## 3. Phase status

| Phase | Status | Last evidence |
|---|---|---|
| P0 Governance / revision | PASS | Existing frozen IDs support the required implementation; no revision change |
| P1 Frozen assets | PASS | Shared frozen resolver owns schemas/settings/maps/masters; two public CLI proofs pass |
| P2 Handoff / currentness | PASS | Public three-stage/review-only and stale-at-birth proofs pass |
| P3 Failure / continuation | PASS | Focused regression `86 passed`; two-job containment proven |
| P4 Render / output / write safety | PASS | Receipt mutations, review orthogonality, staged promotion and write-boundary suite pass |
| P5 Branch | PASS | Lifecycle/branch regression `40 passed`; public child currentness and invalidation proven |
| P6 Word / template / visual | `BLOCKED_USER` | Code/static checks complete; 10 target-Word tests accurately skipped; visual-human proof pending |
| P7 Operator / pilot readiness | `BLOCKED_USER` | Public operator/context behavior and pilot log pass; actual account facts pending |
| P8 Evidence regeneration | PASS | Fresh slice 21/0; current gate, traceability, AR and builder reports; hygiene complete |

## 4. Deliberate plan deviations

### DISC-001 — Phase-1 DOD cross-reference mismatch

- Finding: `FINAL_EXECUTION_PLAN.md` names `DOD-17` as a P1 primary criterion, while the authoritative DOD owner table assigns template-contract integrity to P6 and assigns old-run root metamorphism to `DOD-01`.
- Scope decision: DEFER_DISCOVERED
- Reason (cite the scope-admission rule): The owner table resolves execution unambiguously; editing stable roadmap control documents would not improve the build or smoke trustworthiness.
- Affected DFS/DOD if admitted: None; P1 was judged against `DOD-01`, and `DOD-17` remains owned by P6.
- Status: Recorded; no product change.

```text
### DEV-###
- Original route:
- Chosen route:
- Why / evidence:
- Affected DFS/DOD:
- Regression check:
- Status:
```

### DEV-002 — Final review route in a non-Git, execution-restricted checkout

- Original route: run the Codex `/review` command over a final diff.
- Chosen route: inspect the changed active-tree trust boundaries directly, compile the runtime/tools/tests and execute the three static anti-orchestration/network/redesign guards; reserve a fresh independent `/review` for the post-blocker GO decision.
- Why / evidence: this checkout has no usable Git metadata and the installed `codex review` executable was denied at process launch; active-tree review found no new material defect, compilation passed and the three guards passed.
- Affected DFS/DOD: DFS-17 / DOD-25.
- Regression check: full current-tree suite `236 passed, 10 target-Word skips`; evidence hashes independently recomputed.
- Status: Complete for the present `BLOCKED_USER` terminal; not represented as an independent `/review` PASS.

## 5. Newly discovered issues

### DISC-002 — Full handoff digest made a valid long-root workflow unusable

- Finding: a 64-character digest in every handoff filename pushed an otherwise valid public-command path over the Windows path boundary under the long-root target fixture.
- Scope decision: ADMIT
- Reason (cite the scope-admission rule): Operator-blocking and smoke-contaminating public-path defect discovered while closing DOD-16.
- Affected DFS/DOD if admitted: DFS-03/DOD-03 and DFS-13/DOD-16.
- Status: Fixed with a 16-character filename prefix while acceptance still recomputes and verifies the complete canonical envelope.

```text
### DISC-###
- Finding:
- Scope decision: ADMIT | DEFER_DISCOVERED
- Reason (cite the scope-admission rule):
- Affected DFS/DOD if admitted:
- Status:
```

## 6. Durable execution facts

### P0-01 — No architecture amendment or revision change

- `INV-09`, Spec §7.2, `DEC-07`, `DEC-21`, `DEC-27`, `DEC-42`, Spec §16.6 and §22.2 already permit deterministic mechanical metadata, receipt verification, three-axis failure ownership, safe alternate destinations and the required implementation choices.
- Explicit human export is treated as a per-invocation human-approved generated destination and remains non-authoritative; this does not legalize protected-root, traversal or reparse escape.
- `SPEC_REVISION`, `SCHEMA_REVISION` and manifest const pins remain `0.9.0`; unrelated `map_version` and `index_version` remain unchanged.

### P0-02 — Baseline test/environment fact

- Current packaged source and canonical readable files matched at 175/175 entries; four protected rendered outputs could not be read by the sandbox.
- The original scratch baseline was `206 passed, 1 failed, 1 skipped`; final current-tree evidence is `236 passed, 10 target-Word skips` in 69.41 s.
- Repository root has no usable Git metadata, so execution uses explicit hashes/inventories rather than clean-tree claims.

### P1-01 — Frozen run asset boundary

- `FrozenRunAssets` in `runtime/jobbsok/manifest.py` is the single run-bound resolver for frozen schemas, settings, maps and template masters; live roots remain used by preflight/new freeze/source maintenance.
- `RunContext` and all public run commands now take soft thresholds from the frozen settings file; authoritative render opens the frozen master selected by the frozen template map.
- Targeted public CLI proof: `2 passed`; post-freeze mutations across authorities/context/policy/schemas/templates did not alter validation or DOCX production, while a frozen stage-policy mutation made integrity and validation exit `2` before work.

### P2-01 — Tool-owned closed-loop handoff

- `context` writes one content-addressed, re-derivable handoff under `generated/handoffs/` and prints the exact submission action; models return semantic fields only.
- `stage-submit` recomputes the current envelope, rejects stale/wrong returns before mutation, stamps canonical metadata, validates, then commits. Stage 3 validates both candidates before replacing either and supports `REVIEW_ONLY`.
- Stage-2 policy now states that strategy ceilings are advisory/correctable and source authorities remain the claim ceiling.

### P3-01 — Failure scopes and bounded recovery

- Public status/validate/next contain malformed job-local JSON while preserving healthy-job diagnosis; frozen-input uncertainty aborts at run scope.
- Unexpected document-build exceptions are caught inside the job render workspace; prior output survives and later jobs continue.
- Semantic-stage validation failures persist the current production failure; one same-session mechanical correction and the separately counted manual semantic retry remain distinct. Success clears the record; exhaustion reaches `BLOCKED_MANUAL`.
- Focused P1-P3 regression checkpoint: `86 passed`.

### P4-01 — Verified render reality and coherent promotion

- `verify_receipt` validates the frozen report schema and exact run/job/final/date/baseline/template/map/config/output path/hash/size identity before status exposes any output.
- A complete staged DOCX generation must be promotable before either component advances; a PDF advances only with its accepted DOCX. Failed recovery retains prior pipeline ownership evidence and retires only proven pipeline bytes.
- Explicit external exports are non-authoritative and do not mutate canonical receipt state; relative traversal, protected roots and reparse escapes refuse.
- Deterministic render/security regression: `23 passed`; combined no-Word regression: `27 passed`. Word-dependent target proof remains P6.

### P5-01 — Fully staged bounded branch rebind

- Parent frozen and vacancy integrity is required before staging; the full parent tree is hash-compared before exposure.
- The child manifest and final bindings exist in staging before a single rename exposes the child. No placeholder state or post-publication repair remains.
- Reuse is a fixed four-artifact topological rebind, not a lineage engine: only parent-current artifacts with identical governing inputs and reused predecessors are rebound and child-validated.
- The optional semantic-hash identity exclusion was rejected: the bounded fixed rebind is smaller and preserves existing hash-consumer semantics.
- Public parent-compromise, unchanged-currentness and stage-specific invalidation proofs plus interrupted-exposure probe: `40 passed`.

### P6-01 — Honest target boundary and reproducible master repair

- Word conversion remains one isolated, macro-disabled, read-only automation instance per document; no generic Word process kill was added.
- Timeout reporting now states only that the PowerShell invocation stopped. Current COM activation fails with Windows `80070520`, so ten target tests are skipped and target success is not claimed.
- The maintained master tool removes the exact single unconditional CV page-break paragraph, refuses ambiguity, preserves all 17/7 controls and is idempotent. Current target-Word open/export and visual review remain user-owned.

### P7-01 — Actionable operator handoff without invented account facts

- Public `context` exposes the complete submission bundle and exact semantic-only handoff; status exposes the first three current reason/action pairs plus all known limitations.
- A synthetic nonempty role mapping proves the mechanical public path. Actual SOL/TERRA surfaces, file access and privacy/retention/training settings remain unknown and are not guessed.
- `pilot/PILOT_LOG.csv` is a human-owned semicolon-delimited scaffold; no product-quality result is inferred from it.

### P8-01 — Replacement evidence and source hygiene

- The fresh vertical slice uses its own absolute input and current public handoff contract: 21 expected outcomes, zero unexpected, healthy job usable, poisoned peer contained, exactly two current DOCX artifacts and no inherited PDF.
- Gate, traceability, anti-regression and builder reports now distinguish deterministic/public, target Windows, human visual and user-account scopes.
- The nested `Build.zip` residue and finalization scratch/bytecode directories were removed; `.venv` and `.pytest_cache` remain local ignored paths, not distribution evidence.

Record only conclusions that must survive compaction: a measured threshold, a confirmed consumer inventory, an environment fact, a decision made and its reason. Not narrative, not tool transcripts.

## 7. Current user-owned blockers

1. **DOD-16 / AR-01,03,16,20:** run the target-Word group from an unlocked interactive Windows session, including realistic long names and a forced conversion timeout while a human Word document remains open; confirm the document/session survives.
2. **DOD-18:** generate sparse, normal and dense current-tree DOCX/PDF fixtures through target Word and record human visual checks for clipping, blank pages, glyphs, section flow and balance.
3. **DOD-19 / Gate-10:** provide the intended `SOL_CLASS` and `TERRA_CLASS` surfaces, how each receives/reads the frozen files, and the relevant account privacy, retention and training facts.
4. **DOD-25:** after the target/account gates close, run a fresh independent `/review`; the installed CLI executable was access-denied here and the completed active-tree self-review is not counted as independent evidence.

If a blocker appears, record the exact missing user fact or action and the affected `DOD-*` criterion.

## 8. Completion checkpoint

- **Final status:** `BLOCKED_USER`; deterministic/public implementation work is exhausted, but `GO_FOR_TWO_JOB_SMOKE` is not authorized.
- **Full suite:** `236 passed, 10 target-Word skips` in 69.41 s.
- **Fresh public slice:** `21 expected, 0 unexpected`; exactly two current DOCX outputs; healthy peer usable and poisoned peer isolated.
- **Evidence roots:** `P0.9/Build/evidence/finalization/` (including `DOD_AUDIT.md`), `evidence/gates/GATE_REPORTS.md`, `evidence/vertical_slice/`, and `BUILDER_REPORT.md`.
- **Final review:** active-tree self-review/compile/static guards passed; installed `codex review` could not launch (`Access is denied`) and is explicitly not counted as independent review evidence.
- **Remaining `DEFER_PILOT`:** real-job semantic quality, cluster metrics and human-scored product questions only.
- **Remaining `DEFER_DISCOVERED`:** DISC-001 roadmap cross-reference typo; no implementation effect.
- **Next-phase pointer:** close §7, then and only then run the two-real-job semantic smoke. No real job was consumed here.
- **Roadmap lifecycle state:** terminal `BLOCKED_USER`; resume only when the listed user facts/actions are available.
