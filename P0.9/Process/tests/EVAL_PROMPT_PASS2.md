# TASK: Framework post-mortem and final ranking, from 9 generated Avinor packages

You are reviewing the output of a document-generation framework against the vacancy it was aimed at, and then tracing every weakness you find back into the framework's own source — prompts, policy, context, authorities, templates, weighting, code — so it can be fixed.

Work the five parts below in order. Parts 1–2 must be completed on your own reading of the documents, **before** you open the two prior reports in Part 3; do not let another model's ranking seed your own.

## Material

Repo root: `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`
Framework proper: `…\P0.9\Build\` (skip `.venv`)
Test material: `…\P0.9\Process\tests\`

- `avinor_digital_transformasjon.md` — the vacancy. Ground truth for what the role requires.
- `cv/` and `soknad/` — 11 CVs and 11 letters, one package per matching filename stem (`CV_` / `Soknad_` token removed). The leading 6 hex characters mark the pipeline run; `0fa53b` has four packages and `3eeb10` two, so same-prefix variants are distinct packages that isolate a single change.
- **Exclude `0d1af3` and `2120b3` entirely from Parts 1 and 2.** Nine packages remain.
- `output/` — two prior evaluation reports (Part 3).

All 22 documents describe the same person. The facts are fixed; what varies is selection, framing, ordering, emphasis and wording. Every quality difference you observe is therefore a framework difference, which is exactly what makes it traceable.

Surfaces most likely to carry causation, though not an exhaustive list — go where the evidence leads:
`prompts/STAGE1_PROMPT.md`, `prompts/STAGE3_PROMPT.md`, `policy/stages/stage1_decision_architecture.md`, `policy/stages/stage3_final_writer_review.md`, `policy/writing/WRITING_DOCTRINE.md`, `policy/writing/FORFATTERSTEMME.md`, `policy/writing/PERSUASION_CALIBRATION.md`, `policy/personality_facets.json`, `policy/settings.toml`, `authorities/`, `context/PERSONALITY_PROFILE.md`, `templates/`, `schemas/`, `runtime/jobbsok/`.

---

## Part 1 — Weaknesses, and what in the framework causes them

Read the nine CVs and nine letters against the vacancy and against each other, and catalogue **every weak aspect** you can find: weak against the vacancy's actual requirements, weak as recruiter-facing documents, weak as Norwegian prose, weak in evidence density, credibility, structure, distinctiveness, or coherence.

For each weakness, trace it into the repository and name the **causing element**. Causation runs two ways and you must look for both:

- **A negative contribution that exists** — an instruction, constraint, example, weighting, schema field, template slot, or code path that actively produces the flaw.
- **A positive contribution that is absent** — the instruction, context, evidence, calibration or constraint that would have prevented it and is simply not there anywhere in the framework.

"Contribution" is anything that shapes the output: prompt wording, policy doctrine, personality facets, authority files, weighting and ordering, schema shape, template structure, defaults in `settings.toml`, or logic in `runtime/jobbsok/`.

Cite the causing element by `path:line` (or by the specific key/field) and quote the offending — or conspicuously missing — text. Where a weakness appears in some packages but not others, use the variant lineage to isolate which change caused it; that is your strongest causal evidence. Where you can only reach a hypothesis, label it a hypothesis and say what in the repo would confirm or kill it.

Output: an ordered catalogue, worst first, each entry = weakness → evidence in the documents (short verbatim Norwegian quotes, with package ID) → causing element in the repo → confidence.

## Part 2 — Optimization plan pitch

Take the catalogue from Part 1 and analyse each item in depth against the full repository — including what else depends on the surface you would change, and what a change would break or shift elsewhere.

Then produce the **optimization plan pitch**: the specific optimizations and tweaks you recommend implementing into the framework to mitigate these weaknesses. It must be immensely specific, highly detailed and directly actionable. For every proposed change:

- the exact file and location to change,
- the current text or behaviour, and the replacement text or behaviour, written out in full — not described,
- which catalogue items it mitigates, and why that mechanism works,
- what it costs: side effects, interactions with other surfaces, what gets worse,
- how you would know from the next run's output whether it worked.

Order the plan by expected effect per unit of change, and say plainly which items you would ship first and which you would not ship at all.

## Part 3 — The two prior reports

Now open the two reports in `…\P0.9\Process\tests\output\`. They are two models' answers to the same earlier evaluation prompt. (If the two files turn out to be byte-identical, say so and treat them as one.)

Read both extensively, cross-reference them against each other and against the documents themselves, and reflect on where they agree, where they diverge, where either is unsupported by the source text, and where either has judged on something other than the documents.

Then take every package that either report placed in the **top 5 for CVs, top 5 for letters, or top 5 as a package**, and analyse each of those packages deeply and directly — CV, letter, and the pair.

## Part 4 — Your own top-5 tables

Through your own analysis, extensive reasoning, and cross-referencing against the repository, determine the top 5 CVs, the top 5 letters, and the top 5 packages. Critically review the two models' rankings as you go — adopt what is well-founded, reject what is not, and say which is which and why. The two reports are input to your judgement, not authority over it.

Return three tables — CV top 5, letter top 5, package top 5 — each with rank, package ID, score, and full reasoning. Alongside them, state the ranking foundation you used: the categories, what each measures, their weighting, and why that weighting fits this vacancy. Add whatever further insight the corpus gives up — patterns across the lineage, what the strongest packages do that the others do not, anything the prior reports missed.

## Part 5 — Deliverables

Write two files into `…\P0.9\Process\tests\output\`:

1. `final optimization plan based on FW test-runs against Avinor.md` — Parts 1 and 2.
2. `finalized rankings, package review, with resoning and comments.md` — Parts 3 and 4.

Then give me, in chat, a short TL;DR of each file — focused on the diffs: what changes you are proposing, and where your ranking departs from the two prior reports. Keep both summaries brief; the detail belongs in the files.
