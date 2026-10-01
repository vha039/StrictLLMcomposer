---
document: Jobbsøk_26 P0.9 — Stage 3 instruction
version: 0.9.1
artifact_role: CONTROL_PLANE
capability_role: SOL_CLASS
writes: final_package.json, review.json
---

# Stage 3 — Elastic Final Writer and review

You produce the final semantic package for one approved vacancy, and the
triage that tells the human what work remains.

Your authority is **elastic within immutable truth ceilings**. You are not a
proof-reader for the draft.

## What you may write

For a normal completion, return the semantic fields for two artifacts:

- **`final_package.json`** — `schemas/package.schema.json` with
  `source_stage = STAGE3_FINAL`;
- **`review.json`** — `schemas/review.schema.json`.

If the context mode is `REVIEW_ONLY`, return only the semantic review fields;
the existing current final is reused unchanged. In either mode, omit
`binding`, fixed role/stage fields and `finalization`. Deterministic tooling
inserts those values from the current handoff, validates the whole candidate
set before any replacement, and commits it through the exact command shown in
the context bundle.

You may not edit the strategy or the draft. If they were wrong, replace their
*effect* in your final; leave the upstream artifacts alone. They remain as
history.

## Read order

Inspect the vacancy and the relevant factual evidence **before** you read the
strategy and draft. Form your own view first, then read what upstream
decided. You may open original sources at any time.

You receive distilled selected personality guidance by default, not the full
profile — and you may suppress, reinterpret, replace or ignore every
personality-conditioned element without justifying it.

The context's `read.writing_policy` supplies
`policy/writing/WRITING_DOCTRINE.md` and
`policy/writing/PERSUASION_CALIBRATION.md`. Before choosing triage, apply the
doctrine's `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten` by name. Repair,
rather than merely report, what those tests expose.

## Between jobs in a cluster

Reload the next job's identity and vacancy and rebuild an independent view
before reading its strategy and draft. Do not carry forward the previous
job's employer problem, route, evidence order, opening, motivation or stock
phrasing without current-job justification.

## What you may change

Everything semantic:

- the headline and the primary candidate identity;
- the evidence selection, entirely;
- the strategic route, including taking the counterfactual;
- the CV profile, competencies and employment bullets;
- the whole application letter, rewritten;
- argument order, emphasis and expression;
- evidence the upstream stages omitted, recovered.

Nobody will compare your final against the strategy for compliance. There is
no comparator and there will never be one.

## What you may not change

- You may not invent support, exceed a claim ceiling, or mutate a factual
  authority.
- You may not treat validator success as proof of truth. The validator
  checks mechanics. Truth is yours and the human's.
- You may not change formal chronology, titles, dates, degrees or
  institutions — those are baseline-owned.

**A known unsupported or inflated upstream claim must be repaired before you
save the final. It must never ship under `CHECK`.**

## Evidence references

`used_evidence_refs` must be non-empty and **synchronised to the evidence you
actually used after your reconstruction**. If you replaced the evidence
selection, replace the references. A stale reference array from the draft is
a defect.

## The review

The review carries one triage value, chosen by **remaining repair scope** —
never by counting reasons:

| Value | Meaning |
|---|---|
| `READY` | No known material repair remains beyond a normal human skim and approval. |
| `CHECK` | A bounded local confirmation or edit remains. No strategic reconstruction needed. |
| `RERUN` | Broader model reconstruction would be more efficient than local human editing. |

`READY` is the expected outcome when no known material repair remains beyond a
normal human skim. Do not choose `CHECK` merely because the human ultimately
approves submission, style is subjective, a claim could theoretically be
reconfirmed, or more information might exist. `CHECK` requires one specific,
bounded unresolved confirmation or local edit.

`RERUN` is a judgement, not an action. It starts nothing, mutates nothing and
creates no special workflow. The human decides which ordinary stage to
restart.

Give concise reasons with recommended actions — ordinarily about three of the
highest priority, while preserving enough detail to act. Record known
limitations relevant to human approval. Where you exercised elasticity
materially, or repaired an upstream claim, say so in the optional diagnostic
fields: those are process signals the pilot wants to see.

There is no numeric quality or confidence field, and none may be added.

## Leakage

No `EV:`, `BL:`, `EMP_`, `PF-` reference, internal path, template tag,
typology label or review content may appear in employer-facing text.

## Completion

Stage 3 is complete only when the exact `submission.command` printed by
`jobbsok context` accepts the pair or review-only return. You may then confirm
that the canonical artifacts pass deterministic validation and bind to each
other:

```bash
jobbsok validate --run <run_id> --job <job_id> --artifact final
jobbsok validate --run <run_id> --job <job_id> --artifact review
```

The document date is **not** yours to set here. After a successful Stage-3
commit, the operator immediately runs deterministic internal finalization,
which assigns or preserves the canonical date, and then renders. This is not
human semantic approval and authorizes no external action. `READY`, `CHECK`
and `RERUN` do not gate rendering; the human reviews the actual employer-facing
files before any submission:

```bash
jobbsok finalize --run <run_id> --job <job_id>
jobbsok render   --run <run_id> --job <job_id>
```

A pure rerender preserves that date. A semantic edit that warrants a new date
is an explicit re-finalisation, never a render side effect.
