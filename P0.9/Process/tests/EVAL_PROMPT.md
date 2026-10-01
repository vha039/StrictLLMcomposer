# TASK: Comparative evaluation of 11 CV + application packages for one vacancy

You are acting in two roles at once, and you must keep them distinct in your reasoning:

1. **The hiring manager for Avinor AS, Digital Transformasjon** — the person who actually decides who gets called in. You care about one thing: does this package make you want to interview this candidate, over the other ten versions of the same candidate?
2. **A document-quality assessor** — you judge structure, prose, precision, Norwegian language quality, evidence density, and internal consistency.

## Inputs

Working directory: `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Process\tests`

- `avinor_digital_transformasjon.md` (and `.pdf`) — the vacancy text. This is the ground truth for what the role requires. Read it first, in full, before opening any candidate document.
- `cv/` — 11 CVs (.docx)
- `soknad/` — 11 application letters (.docx, Norwegian "søknad")

**All 22 documents describe the same real person applying to the same vacancy.** They are 11 generated variants from an automated pipeline. The underlying facts (employers, dates, degrees) are essentially fixed; what varies is selection, framing, ordering, emphasis, wording, and how much of the vacancy's language the document absorbs. Your discrimination therefore has to come from those dimensions — do not fall back on "candidate A has more experience than candidate B", because there is only one candidate.

## Pairing rule (read carefully — the naive rule is wrong)

Each package = one CV + one application letter. Pair them by the **full filename stem with the `CV_` / `Soknad_` token removed** — the two names are otherwise identical.

The **leading 6 hex characters** identify the pipeline run the package came from. That prefix is **not unique**: `0fa53b` has four packages and `3eeb10` has two (later stage/variant suffixes). Treat every one of those as a **separate package**, but note the shared lineage — variants from the same run are the most informative comparisons you have, because they isolate a single change. Build and print the pairing table as step zero and confirm you have 11 clean pairs and 22 files before you analyse anything.

Give each package a short stable ID you use consistently in every table (e.g. `0fa53b-base`, `0fa53b-opusx`, `0fa53b-solmed`, `0fa53b-solxh`, `3eeb10-base`, `3eeb10-stage1`, `0d1af3`, `2120b3`, `6d65bd`, `93c621`, `b5104f`). Print the ID → filename mapping once.

## Rubric — you define it, but you define it *first*

Before you score anything, design and publish three rubrics:

- **A. CV rubric** — your own categories (aim for 5–8), each with: a name, a one-sentence definition of what it measures, its weight, and concrete anchors describing what a low, middle, and top score looks like *for this specific vacancy*.
- **B. Application-letter rubric** — a separate set of categories. Do not just reuse the CV categories; a letter is a different instrument and should be judged on different things.
- **C. Package rubric** — categories that only exist at the pair level and cannot be seen in either document alone (see Phase 4).

State the weighting function explicitly (e.g. `0.25·Fit + 0.20·Evidence + …`) on a 0–100 scale. You may set the **final score independently of the weighted sum** — mathematical equivalence is not required — but whenever the final score deviates from the computed sum by more than a few points, add a one-line justification for the override. Publish all three rubrics before any document scores appear.

Categories are your call, but the rubric should be able to see at least: fit against the vacancy's actual responsibilities and requirements; evidence and specificity (numbers, named systems, named outcomes) versus generic consultant-speak; credibility and non-inflation; structure and scannability for a recruiter giving it 45 seconds; Norwegian bokmål language quality and register; and distinctiveness — whether the document sounds like this person or like a template. Add whatever else you think matters.

## Work in phases, and show the work at each phase

**Phase 0 — Inventory.** Pairing table, package IDs, confirmation that all 22 files were opened and read in full. Never score a document you did not read end to end.

**Phase 1 — Rubrics.** As above, all three, published up front.

**Phase 2 — CVs.** First a short per-CV analysis (2–5 sentences: what this version does differently, its strongest and its weakest move). Then compare all 11 head-to-head — explicitly name what separates adjacent ranks. Then the **CV rank table**.

**Phase 3 — Application letters.** Same structure: per-letter analysis, head-to-head comparison, then the **application rank table**.

**Phase 4 — Packages.** Open each CV together with its paired letter and read them as a recruiter would, in sequence. Judge what only becomes visible as a pair:

- Do they contradict each other (dates, titles, scope, framing of the same episode)?
- Redundancy vs complementarity — does the letter just narrate the CV, or does it add the reasoning, motivation and judgement the CV cannot carry?
- Combined coverage of the vacancy's requirements: which requirements does the *set* leave uncovered, and does the pair double-cover the same ones?
- Consistency of voice and register across the two documents.
- The 45-second recruiter test applied to the set.

Then cross-compare all 11 packages against each other, and produce the **package rank table**.

**Phase 5 — The three tables.** Return all three tables together in one place at the end, even though they already appeared in their phases: CV rank, application rank, package rank. Each table: rank, package ID, final score, the sub-scores, and a one-line reason. Force a strict total order — no tied ranks. If two are genuinely near-indistinguishable, still order them and say so in the reason line.

**Phase 6 — The strongest set.** Independently of the packages as delivered, pick the single strongest CV and the single strongest application letter across the whole corpus — **they may come from different runs**. Then:

- Check that the mixed pair actually holds together: any contradictions, duplications, or tonal clashes introduced by the mix?
- Score the hybrid against the package rubric.
- Say plainly whether the hybrid beats the best intact package, and by how much.
- List the concrete edits (specific and quotable — "cut the second paragraph under Erfaring", not "tighten the prose") needed to make the mixed set coherent.

## Rules of engagement

- **Evidence or it did not happen.** Every score claim gets at least one short verbatim quote from the document, with the package ID. Quote the Norwegian as written; do not translate inside the quote.
- **Hunt for fabrication.** You have 11 renderings of one factual base. A claim, number, title, or achievement that appears in only one or two packages is a candidate hallucination from the generator. Flag every such claim in a dedicated section with the package ID and the exact wording, and penalise it under credibility. Cross-check against the facts that appear consistently across the corpus.
- **Penalise vacancy-parroting.** Reusing the ad's phrasing is cheap; converting a requirement into concrete evidence from the candidate's own history is what should score.
- **Name the deltas.** After the tables, add a short section: which specific, transferable moves separate the top packages from the bottom ones? This is the actionable part.
- **Be decisive, be honest.** State uncertainty where you have it, but do not hedge every ranking into mush. If the whole corpus is weak on some dimension, say so rather than grading on a curve.
- Write the report in English; keep all quoted source text in Norwegian.
