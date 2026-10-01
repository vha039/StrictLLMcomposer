# P0.9 Desired Final State

## 0. Purpose and boundary

This document defines the observable properties of the mechanically finalized Jobbsøk_26 P0.9 baseline.

`[HARD]` Every `DFS-*` property in this document is a required outcome. It specifies **what must be true**, not the internal implementation mechanism used to make it true. Class names, helper structure, token formats, local algorithms and test-fixture design belong elsewhere unless they are themselves required by an approved architecture rule.

`FINAL_EXECUTION_PLAN.md` is the preferred route to this state. If direct implementation evidence supports a smaller or safer mechanism that still satisfies this document and `DEFINITION_OF_DONE.md`, the route may change deliberately under the roadmap guidance.

The terminal engineering state of this roadmap is `GO_FOR_TWO_JOB_SMOKE`. Executing the real semantic smoke is outside this document’s scope.

## 1. Product and architecture preservation

### DFS-00 — Core product remains intact

Mechanical finalization must preserve the central P0.9 product architecture:

- every core job yields a tailored Bokmål CV and application letter;
- the CV and letter remain complementary employer-facing documents;
- the semantic workflow remains three manually initiated stages;
- Stage 3 remains truth-bounded and elastic rather than a strategy-compliance checker;
- candidate facts remain bounded by the factual authorities;
- human beings retain factual approval, final package judgment and irreversible submission authority;
- deterministic runtime does not call semantic models, contact employers, submit applications or publish externally;
- no runtime semantic quality/fit judge or hidden semantic retry/orchestration engine is introduced;
- PDF/render degradation remains distinct from semantic package validity.

Mechanical repair must not recreate superseded P0.7 machinery merely to make the implementation look more conventionally “complete.”

## 2. DFS-01 — Frozen-run immutability

Once a run is frozen, every run-bound read capable of changing semantic eligibility, validation, context, rendering or employer-visible output must derive from that run’s immutable frozen state or from an explicitly defined immutable derivative of it.

Editing maintained/root authorities, schemas, settings, policies, templates, mappings, personality material or inbox inputs after freeze must not silently change the behavior or output of an existing run.

Maintained/root inputs remain valid sources for future freezes or explicitly created child runs; they are not live dependencies of an already frozen run.

Tampering with the run’s own frozen governing bytes must be detected and diagnosed rather than silently consumed.

## 3. DFS-02 — Deterministic ownership of mechanical metadata

Semantic models own semantic judgment and content.

Deterministic tooling owns or deterministically verifies metadata whose correct value is mechanically derivable from repository/run state, including lineage/current-upstream information and other predetermined envelope fields.

A human or semantic model must not be required to manually derive canonical hashes or mechanically predetermined identifiers that tooling already knows.

The implementation may choose the smallest safe representation for this contract; the desired state does not mandate a specific token, envelope class or serialization mechanism.

## 4. DFS-03 — Semantic artifacts are current at birth

A semantic candidate may become the current artifact only after the runtime has verified that it was produced for the correct current run/job/stage/mode and against the exact governing inputs/upstream state required for that stage.

A stale, incorrectly bound or mechanically inconsistent candidate must be refused **before** it archives, replaces or hides valid current work.

Successful acceptance must not immediately produce a state that the same runtime derives as stale.

A refused candidate that leaves a valid current artifact untouched must not demote that valid artifact merely because an attempted submission failed.

## 5. DFS-04 — Currentness is an action boundary

Actions that consume “current” semantic work must use one coherent definition of eligibility/currentness.

In particular, context preparation, continuation routing, semantic finalization and authoritative rendering must not consume stale, integrity-compromised or otherwise ineligible semantic artifacts.

Read-only diagnostic commands may inspect and report invalid state, but mutating/action commands must not convert known-invalid state into current employer output.

Triage outcomes such as READY/CHECK/RERUN remain orthogonal to mechanical currentness unless the governing architecture explicitly states otherwise.

## 6. DFS-05 — Stage-3 completion and interrupted recovery

Stage 3 owns the completed final semantic package and its review/triage record.

The normal Stage-3 path must support producing the required final/review result coherently.

If a valid current final exists but review is missing or invalid because work was interrupted, the system must be able to resume the remaining Stage-3 work from disk state without forcing unnecessary semantic regeneration.

Continuation commands must reflect the actual remaining Stage-3 work rather than treating “final exists” as equivalent to “Stage 3 complete.”

## 7. DFS-06 — Failure scope and continuation

Failure handling must reflect the scope of the failure rather than merely the Python exception class.

A job-local malformed artifact, operator mistake or job-specific processing error must not unnecessarily abort or hide independent healthy jobs when safe continuation is still established.

A genuinely run-global, shared-infrastructure or environment-global failure may abort broader work when continuing would make state uncertain or risk corruption.

After interruption or failure, disk state and diagnostics must be sufficient to determine what remains valid, what failed and what action comes next.

Unexpected failures must not leave misleading partially current employer output.

## 8. DFS-07 — Production-state and render-state ownership remain distinct

Persistent semantic production failure/blocking represents failed semantic-production attempt/recovery state.

Read-only diagnostics do not automatically become current production failure.

DOCX/PDF conversion, rendering and render-receipt failures remain on the render axis and do not by themselves make an otherwise valid semantic package semantically failed.

A repair must not collapse the system’s independent semantic-currentness, production-failure and render-currentness concepts into one state machine.

## 9. DFS-08 — Render currentness is verified from reality

Employer-facing output is current only when its render evidence can be verified against the current eligible semantic final, the governing document date, the actual immutable inputs/configuration consumed by rendering, and the actual bytes that are present.

A render record is evidence/receipt, not a semantic artifact and not an infallible state marker.

Unreceipted, mismatched, missing or byte-divergent output must not be surfaced as current merely because files or an old report exist.

A change that only affects review/triage metadata must not invalidate unchanged employer-document bytes: review content is not part of render identity. A current valid review **is** required before an authoritative render may be initiated. Both halves are existing frozen semantics — see `D-03` in `FINAL_EXECUTION_PLAN.md` for the governing citations.

## 10. DFS-09 — Employer-output generations remain coherent

The current DOCX/PDF representation of one logical document component must not silently combine different semantic generations.

If regeneration cannot safely replace one member of a DOCX/PDF component pair, a newly generated sibling must not advance in a way that makes the pair look mutually current when they represent different semantic state.

Prior pipeline-owned output may be retired from current presentation only when ownership is safely established.

A stale pipeline-owned PDF must not remain visually/currently authoritative merely because a later PDF conversion failed.

## 11. DFS-10 — Human-edited output is protected

Human-edited employer deliverables must not be silently overwritten by deterministic rerendering.

Ownership/currentness logic must preserve the existing hash-based no-clobber principle while still allowing the pipeline to recover from its own degraded or interrupted prior attempts.

The operator must not be trained by false ownership diagnostics to use destructive force options routinely.

## 12. DFS-11 — Write boundaries are explicit and safe

Canonical production/model-controlled writes must resolve only inside approved writable roots for the active operation.

Path traversal, symlink/junction/reparse escape and writes into protected factual/control-plane roots must be refused.

An explicitly human-requested export may target a resolved path outside the repository when allowed by the approved architecture, but such exported bytes are non-authoritative unless separately and deliberately adopted.

These production boundaries must not accidentally prohibit explicit human-invoked **source-maintenance tooling** whose purpose is to update maintained templates or other source assets between runs. Maintenance actions and run-production actions must remain distinguishable.

## 13. DFS-12 — Branching preserves parent immutability and produces coherent children

A branch operation must fully verify the parent inputs/state required for safe branching before exposing child side effects.

The parent run must remain byte-for-byte unaffected by child creation.

A canonical child must not become visible while its current semantic chain still contains placeholder or internally inconsistent lineage/binding state.

When governing semantic inputs are unchanged, legitimately reusable semantic content should remain current in the child without unnecessary regeneration.

When governing inputs change, only the correct earliest affected stage and its descendants become non-current; the system must not pretend unchanged descendants are current under changed inputs.

No generic lineage engine, event-sourcing system or dependency framework is required merely to achieve these properties.

## 14. DFS-13 — Target-Windows document rendering is operationally reliable

The normal target-machine Word path must handle realistic long Norwegian employer/title combinations without losing expected PDFs merely because internal temporary/staging paths are unnecessarily long.

Timeout and process-cleanup diagnostics must truthfully describe what was and was not terminated.

Automated cleanup must never risk terminating unrelated user Word work merely to appear “stronger.”

The existing proven one-document/one-automation-instance posture and target Word rendering path must remain safe unless direct evidence supports a superior alternative.

## 15. DFS-14 — Template and document integrity are enforced at point of use

Rendering must verify that the immutable master actually consumed still satisfies the expected template/control contract before producing employer documents.

Unknown, missing or duplicate controls that would create unsafe or leaked employer output must fail locally rather than being silently unwrapped/shipped.

Mechanical finalization must preserve the target-Word compatibility properties established by the repaired masters, including byte-safe handling of untouched OOXML package parts where relevant.

Template repair/tuning must preserve the intended control capital and remain reproducible through maintained tooling rather than one-off opaque manual edits.

## 16. DFS-15 — Employer documents are visually and textually usable

Sparse, normal and dense representative fixtures must render without known deterministic layout defects that would contaminate the semantic-quality smoke.

At minimum:
- no known forced blank/near-empty page caused by the current master logic;
- no clipping, missing glyphs or unintended blank pages;
- reasonable heading/section flow;
- employer-facing text remains parseable and correctly identified;
- Norwegian glyphs and filenames remain correct.

Mechanical finalization must not introduce hard semantic/page caps or auto-fit logic merely to make fixtures visually uniform.

## 17. DFS-16 — Human/model handoff is closed-loop and low-friction

For each semantic stage, the operator/model handoff must expose the exact current inputs, role/surface information available for the run, output contract and submission action needed to complete that stage.

Completing the documented Stage-1/2/3 workflow must not require the human or model to manually compute canonical hashes or reverse-engineer internal binding rules.

The runtime must reject stale or mechanically inconsistent returned work before it displaces good current state.

Operator surfaces should expose enough current reason/limitation/next-action information that routine recovery does not require manually inspecting multiple internal JSON files.

## 18. DFS-17 — Evidence and reports are re-derivable and truthful

Test names, helper-level checks and historical reports must not be treated as proof of public production-path behavior they do not exercise.

Material mechanical invariants must have evidence at the scope claimed.

Synthetic vertical-slice evidence, gate reports, traceability material and builder/finalization reports must reference artifacts/runs that actually exist or deliberately retained immutable evidence sufficient for independent reproduction.

No report may claim a stronger test/gate status than the evidence actually supports.

Obsolete/orphaned evidence may be removed or clearly superseded only after replacement evidence is verified.

## 19. DFS-18 — Pilot readiness is mechanically prepared without pre-solving pilot questions

Before real candidate data is used:
- the operational model/surface/file-access/privacy mapping required by GATE-10 must be resolvable and truthfully recorded at the scope actually known;
- the human-owned pilot log scaffold must exist;
- queue/context surfaces must support practical continuation;
- known mechanical/render/layout defects that would confound the semantic smoke must be closed.

Volatile provider facts remain operational evidence, not frozen product architecture.

Questions such as strategy filler, model-writing quality, personality usefulness, source-inspection false positives and READY/CHECK calibration remain pilot questions unless direct implementation evidence converts them into mechanical defects.

## 20. DFS-19 — Architecture and revision semantics remain coherent

Any architecture amendment made during finalization must be explicit, human-authorized, mapped to affected governing IDs and synchronized across the required architecture/adoption records.

No old frozen run may be silently interpreted under materially changed normative semantics.

If a new architecture/schema revision is introduced, the repository must preserve enough exact prior authority to explain older frozen runs, and runtime behavior toward unsupported older revisions must be explicit and safe rather than accidental.

The desired state does not prescribe whether the final mechanism is labeled `0.9.1` or implemented through another coherent revision strategy; that choice belongs to the finalized execution plan.

## 21. Explicit non-goals and deferred uncertainties

Mechanical finalization must not expand into:
- execution of the two-real-job semantic smoke;
- representative-cluster product experiments;
- personality-catalogue redesign without package evidence;
- speculative source-inspection tuning;
- speculative Stage-1 schema simplification;
- generic OOXML support not required by current masters;
- automatic semantic model routing/retry;
- runtime semantic quality scoring;
- event sourcing, dependency/lineage engines or generic transaction frameworks;
- portal/channel/language machinery;
- automated submission;
- broad “cleanup” whose only justification is style or theoretical future use.

Such discoveries are recorded as `DEFER_DISCOVERED` under the scope-admission rule (`GUIDANCE_INSTRUCTIONS_AND_RULES.md` §6) rather than silently admitted into the baseline.

## 22. Terminal engineering state — `GO_FOR_TWO_JOB_SMOKE`

The system may be classified `GO_FOR_TWO_JOB_SMOKE` only when:

- every mechanically applicable desired-state property above is demonstrated by the approved Definition of Done;
- no known material baseline correctness, integrity, containment, render/document or operator-blocking defect remains inside this roadmap’s scope;
- all accepted anti-regression properties remain intact;
- evidence/report claims have been regenerated or corrected to match reality;
- any genuinely user-owned/account-specific prerequisite is identified explicitly rather than guessed;
- remaining unknowns are deliberately semantic/pilot questions, not known mechanical defects.

`GO_FOR_TWO_JOB_SMOKE` authorizes the **next** human/model phase to begin. It does not itself execute or certify the semantic smoke.
