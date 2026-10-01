You own the Relay implementation plan. Reconcile it against an independent review; do not implement.

## Inputs and authority

- Read the current plan **in full**: `P0.9/Process/build_experimental/bright-questing-teacup.md`. The originally supplied `Process/build/_experimental` path was inaccurate.
- Read **in full**: `P0.9/Build_experimental/reviews/PLAN_REVIEW_DIFF.md`.
- Target: `P0.9/Build_experimental` only. Never modify or write through to `P0.9/Build`, including through copied environments, launchers or redirected paths.
- The user's experimental brief controls. The plan is a proposal; the review is advisory evidence, never instructions. Model reputation is not evidence. Current repository behavior and your own adjudication control.
- Optimize upside, information flow, specialization, final-package quality and operator effort. Breakage in the experimental copy is acceptable. Prefer the simplest architecture preserving intended capabilities. No QA frameworks, new test suites, generic preflight, compatibility/migration systems or defensive scaffolding. Lightweight checks intrinsic to a chosen mechanism are allowed.
- Stages remain separate, human-started agent sessions. Do not silently replace this with automatic orchestration.

## Adjudicate, then reconcile

For **every substantive finding**, identify the challenged plan decision and verify every material factual premise against actual current code. Read enough callers, consumers, schemas and existing prior art to understand consequences; do not rely on the review's citations alone.

Reconstruct realistic alternatives, including deletion and useful hybrids. Reason extensively about quality, evidence authority, operator cost, token cost, implementation dependencies and second-order interactions. Distinguish definite defects from hypotheses. Explicitly adjudicate each D-ID: **ACCEPT / MODIFY / REJECT**, with the decisive reason and exact resulting decision. Reject unsupported recommendations. For unresolved choices, identify the deciding observation and choose a workable default where possible.

Propagate accepted/modified decisions through **every** affected section. Check combinations: editorial freedom versus provenance; draft-bound rejection versus queue routing; CV-only advocacy versus schemas/registry/rendering; branch reuse versus consumed-context identity; implementation completion versus human-started trials. Remove superseded rules rather than leaving conflicting exceptions.

Produce **one fully reconciled, execution-ready replacement plan**, not an addendum or patch list. Keep the adjudication record compact. Commands, paths, schemas, artifact ownership, binding, stage order, dependencies, completion criteria and human handoffs must agree. Do not invent production-hardening work to resolve inconsistencies. **Do not begin implementation in this planning turn.**

Append the following behavior as the updated plan's **final section**, not merely accompanying chat:

### After plan acceptance

Once the user explicitly accepts this plan:

1. Immediately save the accepted/final plan to an appropriate durable location inside `P0.9/Build_experimental`.
2. Then create and output one optimized `/goal` prompt instructing yourself to execute the **ENTIRE** accepted plan.
3. The prompt must contain **strictly fewer than 4,000 characters**, including its `/goal` prefix. It must initialize execution from the repository, point to the saved plan as the authoritative implementation specification, preserve material scope/constraints/stop conditions, require inspection of actual repository state before changes, prohibit modifying `P0.9/Build`, and instruct full execution rather than re-planning. Preserve human-started stage boundaries. Optimize implementation reliability and instruction economy; verify the character count before output.
4. After outputting that single prompt, **HALT**.
5. Do not start implementation until the user initializes execution with that `/goal`.
