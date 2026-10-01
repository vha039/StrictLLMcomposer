# 00 — Overview · final pilot-learned optimization pass

**Status:** planning package. Not authority.
**Produced:** 2026-09-01, against run `r20260828-213932-7f13b4` (cluster `pilot_live_smoke`).
**Scope of this package:** analysis and planning only. Nothing in `P0.9/Build`, no architecture file
and no pilot artifact was modified to produce it.

This file is the map into the package. Read §1–§4 for the verdict and the shape of the change set;
§7 is the index into every other file.

---

## 1. Executive verdict

The pilot succeeded. Two real vacancies produced two current `READY` packages with materially
different strategies, correct claim ceilings, honest limitations moved to review rather than to the
employer, and valid DOCX output. **This is a writing-quality and typography pass, not a redesign.**

Three findings determine the shape of the change set, and all three correct or extend what the prior
handoffs said:

1. **The pilot ran the exact policy now in force.** All 15 frozen inputs are byte-identical to live,
   including both Word masters and the generated baseline map. Stale-policy drift is ruled out, so
   every defect is either non-compliance with an in-force rule, a rule not routed to the stage that
   needed it, or a genuine coverage gap. Exactly one is the third kind.
2. **Typography is inline, not style-driven.** `docxfill._set_paragraph_text` deep-copies the template
   run including its `w:rPr`, so generated CV text takes the master's **inline** `w:sz`. A prior
   report concluded the opposite; acting on it would have changed almost nothing in the CV. Reading
   the run properties also exposed a defect no report had recorded: two *content* zones are formatted
   as *record titles* — bold navy — while carrying the least important content on the page.
3. **No prohibited dash is model-generated.** Both final packages contain zero en dashes and zero em
   dashes. Every dash that reaches an employer-facing page comes from deterministic code, the
   baseline, or static master text. Outcome D is almost entirely a code-and-assets fix.

Two mechanical defects were also reproduced. The pilot output files carry a protected DACL owned by
`vhaala\CodexSandboxOnline`, while their parent `out/` directory inherits `vhaala\veggi`
FullControl; the current sandbox can read them as owner, but the human account is absent from the
file DACL. Python 3.14.3's creator-only `tempfile.mkdtemp(..., 0o700)` plus same-volume promotion is
the direct mechanism. Two tests are also hard-coupled to a production configuration value, so the
suite is **not** green today.

**Verdict: proceed.** Twenty-one implementation-controlled file changes plus human pilot-log data,
no architecture amendment, no schema change, no new command or state. Every change traces to a
mandatory outcome or a reproduced defect.

---

## 2. Target state

| Dimension | Now | After |
|---|---|---|
| CV body text | 9 pt | **12 pt**, headings 14, subordinate 10, name 24 |
| Letter body text | 10.5 pt | **12 pt** |
| Size set | `{8, 8.5, 9, 9.5, 10, 10.5, 24.5}` | **`{8, 10, 12, 14, 24}`** — no half-points |
| CV page 2 | ~15 % full | ~50 % full, a genuine two-page CV |
| Subordinate CV zones | bold navy, styled as titles | plain, clearly subordinate |
| En/em dashes on the page | 16 en + 4 em | **0** |
| Motivation | employer slogan promoted to the letter's climax, and scored as passing the employer-swap test | grounded in the work; purpose language allowed when it is a causal feature of the work, never as evidence of specificity |
| Durability claim | `var rapportert i bruk` | `var fortsatt i bruk`, with `om lag` and the observation horizon intact |
| Voice | polished generic application prose | a candidate-specific author voice owned by Stage 3 |
| Output files | human account absent from protected file DACL | openable directly from `out/` |
| Suite | 251 tests, **2 failing** | **256 / 0 / 0** |

---

## 3. Principal weaknesses found

Fifteen validated issues plus one merged. Full entries in `03_…md`; evidence in `04_…md`.

**The three with the greatest employer-facing impact:**

1. **CV typography and hierarchy (ISS-01–04, HIGH/MEDIUM).** All substantive CV prose is 9 pt, the
   letter is 10.5, three half-point sizes are in use, and two subordinate content zones are formatted
   as titles. This affects every recruiter scan before any wording quality can matter.
2. **Generic, performative author voice (ISS-05, 09–11, HIGH/MEDIUM).** Huseierne's mission slogan is
   amplified into a dedicated motivation paragraph and then rewarded by the review; Stage 3 also
   introduces consultant-form openings, both strategies prescribe the same letter skeleton, and both
   finals retain a stock closing. The packages are polished but less plausibly written by this
   candidate than the strongest pilot sentence proves they can be.
3. **Truth attenuation on the strongest durability claim (ISS-06, HIGH).** The authority's
   third-person provenance word is carried into first-person prose, and Stage 3 removes the
   `fortsatt` Stage 2 had added. The result sounds less certain than the candidate's own documented
   knowledge while the genuine approximation and observation horizon remain necessary.

Then: the em dash the renderer injects (ISS-07), 16 en dashes from the baseline and masters (ISS-08),
consultant-form openings Stage 3 introduced (ISS-09), a letter skeleton both strategies prescribed
(ISS-10), a stock closing that survived reconstruction in both jobs (ISS-11), one clause hyphen
(ISS-12), the output ACL problem (ISS-13), the test coupling (ISS-14), and the pilot log that was
never written (ISS-15).

---

## 4. Major changes and why

| Outcome | Change | Why this and not something else |
|---|---|---|
| **A** readability | Declarative, idempotent typography table in `prepare_masters`, five tiers, both masters; `styles.xml Normal` for the letter | The CV needs inline runs rewritten; the letter needs `styles.xml`. Doing only one silently does nothing. `prepare_masters` is the only auditable route to a master edit in a repository with no version control, and it already verifies the 17/7 control contract before writing. Headings go to **14**, not 12, so the change does not flatten a hierarchy that already exists. |
| **A** page policy | One doctrine paragraph: page targets are met by editorial compression | Draws the distinction that matters — **per-document shrinking is prohibited; canonical template design is legitimate**. No validator, no hard limit. |
| **B** motivation | Keep the existing Norwegian doctrine unchanged; route `motivation_bridge` to `Begrunnet motivasjon`, make Stage 3 apply it before triage, and prevent text it rejects from serving as swap-test pass evidence | Coverage already exists. The defect is routing and salience, not policy. A categorical mission ban was rejected: Avinor's societal framing is a causal operating condition and must survive. |
| **C** leverage | Add one provenance-voice bullet to existing `TOO_WEAK`; route `Rolig faglig tyngde`/`TOO_WEAK` to Stage 1 and Stage 3; make Stage 3's repair duty symmetric | The clarification removes third-person source distance without stripping real uncertainty. No new leverage rubric and no authority edit. |
| **D** punctuation | Fix the deterministic sources and add a short canonical `Tegnsetting` section | No en/em dash is model-generated. No validator, normalizer or runtime warning is added; generated clause punctuation remains semantic guidance and human acceptance. |
| **E** voice | New expression-only `policy/writing/FORFATTERSTEMME.md`; Stage 3 primary, Stage 2 light, Stage 1 non-consumer | The existing writing-policy collection freezes and hashes it without new plumbing. It contains no motives, facts, facets, claim authority or strategy authority. Stage 3 forms an independent thesis/opening/order/register before reading upstream, preventing the draft from becoming a prose template. |
| — | Inheritance-preserving staging beside `out_dir` | A parent-path move alone would fail under Python 3.14's special `0o700` directory mode. An opt-in transaction mode preserves destination ACL inheritance and same-volume atomic promotion; rollback staging stays private. |
| — | Fixture-owned role mapping | Restores configuration independence and **increases** coverage: the test now proves the mapping flows through the public handoff, which the deleted assertion never did. |

---

## 5. Expected employer-facing gains

- A CV a recruiter can read at a glance, with a real hierarchy and a populated second page instead of
  a dense first page and a near-empty second.
- The candidate's strongest durability evidence stated on his own authority rather than as a
  second-hand report — while the approximation and the observation horizon that *are* genuine survive.
- A motivation paragraph that explains why this work is a meaningful next use of his experience,
  instead of quoting the employer's slogan back to them.
- Plain human punctuation throughout, removing the most recognisable machine-typography signature.
- A letter that reads as written by this person: claim first, mechanism over adjective, distinctions
  preserved, confident inside the evidence boundary, low ceremony.
- An operator who can open the deliverable where the system says it is.

None of this is proven by any test. Three of the five mandatory outcomes are provable only by human
judgement, which `07_…md` schedules as an explicit acceptance step rather than leaving to chance.

---

## 6. Architecture and scope summary

**No normative amendment is required for any change.** The full argument is `01_…md`; the short form:

- Typography is **explicit builder freedom** — Spec §22.2 grants *"template layout changes proven by
  target-machine gates"*, and `DEC-24` already treats typography as an editorial signal.
- Doctrine changes are refinements of existing named sections in the canonical Norwegian source; Spec
  §4.5 already classes writing guidance as advisory control plane.
- Stage-instruction changes are stage-responsibility clarifications. No stage gains or loses an
  artifact, an authority or a write permission; `INV-09` is untouched.
- The voice file is a writing rule in the control plane (Contract §3), carries **no facets, facet IDs,
  typology or trait claims**, and therefore does not touch the frozen personality interface (Spec
  §22.1, §10; Contract §12, §22).
- `F1` increases conformance with `DEC-21` rather than deviating from it; it changes neither
  no-clobber ownership checks nor rollback privacy.

**Scope: 21 implementation-controlled files plus human log data** — 7 control plane (1 new), 2
authority/derived outputs, 2 regenerated binaries, 4 runtime, 4 tests/fixtures, 2 version/ledger.
`evidence_index.json` is regenerated byte-identical and excluded from the final diff. Zero schema
edits, zero new commands, zero new state axes, zero new dependencies, zero architecture edits.

**Frozen-run semantics:** existing runs keep their frozen inputs. `render_job` refuses to render a run
whose live master no longer matches its frozen record, so **the pilot cannot be re-rendered with the
new typography by design** — which is why verification needs new runs.

---

## 7. Index to the package

| File | What it answers | Read it when |
|---|---|---|
| **`00_OVERVIEW.md`** *(this file)* | What is wrong, what changes, what it costs, where everything is | first |
| **`01_CHANGE_ARCHITECTURE_SPECIFICATION.md`** | Does any of this need an architecture amendment? Explicit diff against frozen P0.9, every change classified, frozen-run and backward-compatibility semantics, and the five objections a hostile reviewer would raise | before approving the change set |
| **`02_IMPLEMENTATION_DESCRIPTIONS_INSTRUCTIONS_AND_DEFINITIONS.md`** | Exactly what to do. The 35-row CV and 8-row letter typography tables with anchors and targets, canonical-section routing, the complete expression-only `FORFATTERSTEMME.md` draft, the `MECHANICAL_FIELDS` replay recipe, implementation order with dependencies, named tests, rollback and stop conditions | during implementation — this is the executable file |
| **`03_ISSUE_REGISTRY_MITIGATION_AND_FIX_LOGIC.md`** | Why each change exists. One atomic entry per validated issue with evidence, causal chain, confidence, severity, recurrence, scope boundary, non-target surfaces, alternatives, interactions and acceptance. Plus the reproduced-but-**not**-defective register | when questioning whether a change is justified, or whether something else should have been changed |
| **`04_PILOT_FORENSIC_AUDIT.md`** | What the pilot actually did. Stage-by-stage lineage for both vacancies, verbatim quotes, the escalation chains for outcomes B and C, cross-job comparison, and the limitations register — what this audit could **not** see | when checking whether a claim in the other files is evidenced |
| **`05_DECISION_LOG_AND_ALTERNATIVES.md`** | Why this design and not another. Every major decision with rejected alternatives — and, first, the **eleven decisions reversed** during adversarial re-evaluation of the first draft | when reopening a settled design question |
| **`06_CHANGE_IMPACT_AND_TRACEABILITY_MATRIX.md`** | What else this touches. Change → issue → outcome → file → test → acceptance; the full framework impact sweep; architecture-clause traceability; the prohibited-redesign checklist; and the explicit unchanged-surface list | during the final scope gate |
| **`07_VERIFICATION_ACCEPTANCE_AND_STOPPING_PLAN.md`** | How to know it worked, and when to stop. Test arithmetic, the hash-equal B0 snapshot plus one projected A1 replay, human acceptance steps, property-based Run B criteria, the representative-cluster gate, and the stopping rule | before and after implementation |

Pre-existing attachments in this directory are **not** part of the package and were not modified:
`FINAL_PERFECTION_PLAN_PROMPT.md` (governing process), `Claude_handoff.md` and `Codex_handoff.md`
(priors, re-verified), `NON_AUTHORITATIVE_CONSIDERATIONS.md` (deliberation material).

No ninth file was added; each required file is distinct and none is redundant with another.

---

## 8. Handoff disagreements resolved by the repository

The two handoffs conflict in one material place, and the wrapper asked for the disagreement itself to
be recorded.

| Claim | Resolution |
|---|---|
| `Claude_handoff.md` §3: full suite **251 passed / 0 skipped / 0 failed** | **Stale.** Two tests are hard-coupled to production role mapping and must fail now — confirmed by source inspection at `test_t05_t08_ownership_schema_failure.py:178` and `:250`. The 251/0/0 measurement predates GATE-10 populating `settings.toml`. |
| `Codex_handoff.md` §8: **239 passed / 2 failed / 10 skipped**, both failures test-only | **Correct.** The repository decides. |
| `Claude_handoff.md` §5.4: typography is style-map driven | **Materially wrong** — the governing values are inline runs in `document.xml`. Corrected in `04_…md` §4.1. |
| `Claude_handoff.md` §7: output ACL issue not reproduced or root-caused | **Superseded by current bytes.** The pilot file DACL is protected and sandbox-owned while `out/` inherits human FullControl; Python 3.14.3's `mkdtemp(..., 0o700)` and same-volume promotion explain the identity-specific failure. |
| `NON_AUTHORITATIVE_CONSIDERATIONS.md` OBS-06: one package hedged, the other stated it correctly | **Refuted.** Both packages carry the identical hedge; the stronger form exists only in the Stage-2 drafts. |
| `NON_AUTHORITATIVE_CONSIDERATIONS.md` OBS-03: page 2 underutilized as an independent defect | **Reclassified** — no page break exists in the master; page 2 is pure overflow, and outcome A resolves it. Merged, not separately fixed. |

`Claude_handoff.md` §5.1 (the pilot froze the current policy), §5.3 (zero dashes in semantic output)
and the single clause-hyphen count were all **confirmed** and, in the first case, widened from the
stage instructions and writing policy to all 15 frozen inputs.

---

## 9. Open uncertainty that implementation cannot resolve

Stated so it is not mistaken for something the plan overlooked.

1. **Whether 12 pt keeps the CV at two pages** is modelled, not measured — ≈1.5 pages. No page count
   has ever been produced for the pilot, because its PDF conversion failed. Discharged by Run A1; the
   3-page decision rule is compression, never type reduction.
2. **Whether the voice file produces authentic authorship or mannered prose** is only answerable by
   the blind A/B. The guard is explicit: if Run B reads as *more* performed than the pilot, soften the
   file rather than reverting the change set.
3. **Whether the provenance clarification is over-applied.** Stripping a real qualification would be
   worse than the understatement being fixed. The inserted bullet names the limits that must survive,
   and Run B is checked in both attenuation and inflation directions.
4. **Whether the inheritance-preserving F1 path behaves identically in the implementation session.**
   The current bytes and Python 3.14 source establish the old mechanism: private `0o700` staging and a
   protected promoted-file DACL. The new mode still needs target-machine DACL inspection and a direct
   open under `vhaala\veggi`; a structural unit test cannot substitute for that identity boundary.
5. **Whether the change set holds at cluster scale.** Two jobs cannot show cross-job convergence
   (`EXP-07`) or triage calibration against real edits (`EXP-06`). Deferred to the representative
   cluster, with a `PILOT_LOG.csv` row per job — the instrument the pilot never used.

---

## 10. Stopping rule

This is the **final pilot-informed optimization pass**. Implement the change set, recover B0, run the
projected A1 verification and fresh Run B, then one representative cluster. At that point framework iteration
stops.

Iteration resumes only on **repeated real-production evidence** of a material blocker that also beats
the smallest local remedy. A single stylistic preference, a one-off model output, or a defect cheaper
to fix by hand than to engineer away does not qualify.

> The goal is not theoretical perfection. It is a stable production system whose remaining
> imperfections are cheaper to handle manually than to engineer away.
