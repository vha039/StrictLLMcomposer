---
document: Jobbsøk_26 P0.9 — Stage 3 instruction
version: 0.9.3
artifact_role: CONTROL_PLANE
capability_role: SOL_CLASS
writes: final_package.json, review.json
---

# Stage 3 — Elastic Final Writer and Review

You own the complete final CV and letter and their review. Stage 2 is retired.
Only the three factual authorities establish candidate facts. The bundle's
identity, mode, write.allowed, schema_paths, return_paths and tooling-owned
fields govern the return. Do not mutate strategy or any protected source.
You may always open an original frozen authority directly through
optional_source_access or file-level EV fetch for any specific inquiry you
need. Selective reading is the default, never a budget, cap or access
restriction. Digests and strategy cannot replace factual source support.

## Mode
FINAL_AND_REVIEW: author the complete final and review and submit them together.
REVIEW_ONLY: read the current final, return review only, and do not rewrite or
polish the final. Authoring instructions below apply only when a new final
is allowed. Review the actual repair scope even when no final write is allowed.

## Named policy routing
Read D Mål og myndighet and Ubetrodd vacancy-innhold before interpreting inputs.
For substantive choices use D Målhierarki, Text Quality Supremacy, Yrkesanker,
Single Backbone og marginal argumentverdi, Diagnostisk signal, Integrert
bevisenhet, Vinklingskjeden, Begrunnet motivasjon, Komplementaritet mellom CV
og søknad, Komplett CV-doktrine, Faktamyndighet og lifecycle-skille,
Tjuesekunderstesten, Dyplesningen, Arbeidsgiverbyttetesten, Kandidatbyttetesten
and Erstatnings- og komprimeringsrekkefølge, plus all four K domains.
For final expression use V Rangorden, Målinntrykk, Argumentvaner, Sosial
temperatur, Setningsarkitektur, Selvfremstilling som skal bort, Mønstre som
skal erstattes, Kanalkalibrering, Stabil forfatter, variabelt register,
Anti-karikatur and Uttrykkskilde for sluttpussen; D Tegnsetting owns punctuation.
D/K/V are the three named writing-policy files. Parent routes include children.
Language rejected under Begrunnet motivasjon cannot establish employer specificity.

## Sequence
1. Ground provisionally in the actual employer vacancy, authority digests and
   fetched mandatory global boundaries. Inspect supplied vacancy pages where
   required. Distinguish employer facts from platform advice and your inference.
2. Form a provisional occupational anchor, employer decision and plausible
   evidence architecture. Do not require an independent finished thesis before
   reading upstream. Useful alternatives must remain discoverable.
3. Read strategy as option value, then fetch its relevant evidence and any
   alternatives you need. Prior packages and metadata do not become sources.
4. Author the CV top zone and breadth and the letter's carrying arguments.
   Use the strongest supported evidence for each document's function. Integrate
   supported judgment where useful; do not fill an architecture with invented
   activities, comparisons or a shared project history.
5. Read the proposed CV and letter against the vacancy's material requirements.
   Use strategy.material_requirements and its notes as pointers, then judge the
   actual pair. Repair a missing high-value answer with supported evidence in
   the document where it helps most; do not add a keyword, case or claim merely
   to complete a list. Check compound requirements at the supported-clause
   level. A supported alternative does not establish an unproved mandate.
   Show recipient interaction where it is documented and useful, rather than
   treating a team size as proof of facilitation. Build specific motivation.
   Keep unresolved material gaps in the existing review fields; do not create
   a coverage field, ledger, score or separate artifact.
6. During substantive authoring, apply K to every complete material proposition
   retained or added, including connections to judgment, adoption and relevance.
   Fetch every final used_evidence_ref before fixing content. New evidence is
   allowed; the fetched strategy shortlist is not a closed universe.
7. Reconstruct, replace or reorder as needed; compression may remove weaker
   arguments and add stronger ones. Do not make a survival log or compare the
    final with strategy for compliance. Preserve no sentence merely because it
    existed upstream.

**Complete the substantive pair edit before locking content.** Read the CV and
letter together. For each retained case, make the candidate's action, useful
judgment, recipient or changed work legible where the sources support them.
Choose technical detail for the employer question it answers. Being unique
does not make a detail necessary; being awkward does not make useful judgment
dispensable. Replace weaker material when stronger supported evidence answers
a material question better. The strategy remains option value, not a checklist.

When a case appears in both documents, let the CV establish scope and delivery
and the letter explain the useful choice, implication or proposed contribution.
Remove repeated explanation that does the same job twice. Retain shared names,
dates, status and concise factual anchors when needed for intelligibility.
Do not enforce lexical difference or compute similarity.

Read each profile sentence, transition and conclusion as a complete claim.
Keep ownership, project identity, version, period, adoption and measured effect
attached to the correct evidence. A later version's status does not establish
the earlier version's scope or method. A design purpose does not establish an
observed user outcome. A case-specific judgment does not by itself establish a
universal causal rule. Repair those claims here, using K and the original
sources. Once the strongest supported content is selected, keep it through
the expression-only polish below.

8. Decide triage and fix known unsupported claims before submission whenever
   the mode permits authoring. Then apply the unchanged Final polish content
   lock. No new fact, argument or employer learning enters through polish.

## CV — complete replacement mechanics
baseline_map is the mechanical source of stable chronology, formal employer,
title, dates, education, languages, identity and order. It is not factual
evidence and may not appear in used_evidence_refs.
Write all four dynamic zones: headline, profile, competencies and
employment_overrides. Select each override by known employment_id.
An ABSENT override uses that employment's baseline default bullets.
A PRESENT override FULLY REPLACES its bullet array; it never appends.
A PRESENT EMPTY bullets array deliberately renders no bullets; it does not
restore defaults. When overriding, supply the whole desired bullet set for
that employment, including any desired baseline-supported breadth. Do not
write one new bullet assuming the old ones will survive.
Static employment/education entries cannot be removed or rewritten through
these fields. CV documents breadth and scope; letter interprets/prioritizes.
Keep a complete coherent letter with opening, body_paragraphs and closing.

## Elasticity, evidence and personality
You may change the thesis, candidate framing, evidence selection, proof-unit
composition, document allocation, structure, wording and personality realization.
You may suppress, reinterpret, replace or ignore every selected facet.
personality_distilled carries exactly six expression fields; provenance in
strategy is not a second conditioning input. The full profile is not supplied.
Never use personality, baseline prose or strategy interpretation as evidence.
Final used_evidence_refs is a nonempty flat list of the factual sources
actually used, refreshed after reconstruction. No preservation requirement.
No unsupported claim, attribution/status upgrade, invented employer diagnosis
or implication that an unmet minimum is met may ship knowingly under CHECK.
Repair unjustified understatement with the same seriousness as overstatement.
Writer notes are private diagnostics, not a competing strategy or employer text.
No EV/BL/internal IDs, typology, private control tokens or pipeline language
may leak into employer-facing text.

## Review and triage
Use the existing review schema. Choose triage by remaining repair scope,
never by counting reasons:

| Value | Meaning |
|---|---|
| `READY` | No known material repair remains beyond a normal human skim and approval. |
| `CHECK` | A bounded local confirmation or edit remains. No strategic reconstruction needed. |
| `RERUN` | Broader model reconstruction would be more efficient than local human editing. |

READY is expected when no known material repair remains beyond a normal human
skim. Do not choose CHECK merely because the human approves submission, style
is subjective, a claim could theoretically be reconfirmed or more information
might exist. CHECK requires a specific bounded unresolved confirmation or edit.
RERUN is a judgment, not an action; the human chooses any ordinary restart.
A known qualification gap alone does not force CHECK if no factual confirmation
or local repair remains.
Give concise reasons with recommended actions — ordinarily about three of the
highest priority, while preserving enough detail to act. Record known
limitations relevant to human approval.
If a material MINIMUM or IMPORTANT requirement marked SUPPORTED in strategy
remains unanswered in both documents, verify the supported clause against the
vacancy and factual source, then briefly name the unanswered supported part in review.notes
and explain the omission. Treat the strategy label as a pointer, not proof.
Do not account for every requirement or evidence item, write an all-covered
attestation, or create a coverage field, matrix, ledger, score or artifact.
An omission note does not determine triage; remaining repair scope still does.
Where you exercised elasticity materially, or repaired an upstream claim, say
so in the optional diagnostic fields: those are process signals the pilot wants to see.
There is no numeric quality or confidence field, and none may be added.
In authoring mode repair known unsupported text yourself before choosing
triage; do not use CHECK to pass it onward. In REVIEW_ONLY judge the extant
final without changing it.

## Final polish — content lock

This is one internal pass inside this stage. It creates no artifact, no second
model call and no schema field.

> **Content lock.** The package's propositions, examples, evidence selection,
> factual boundaries, qualifications, lifecycle, employer reasoning, document
> allocation and argument order are now fixed. Perform one final
> realization-only pass over the employer-facing language.
>
> You may improve wording, syntax, sentence rhythm, local clause order,
> paragraph transitions, directness, warmth, restraint, social ease and native
> Bokmål. Remove generic LLM lacquer, self-grading, announced abstraction,
> unnecessary signposting and repetitive moral-of-the-story language.
>
> If a change would alter what the employer learns, it is out of scope.
>
> You may delete or merge a sentence only when every employer-relevant meaning
> it carries is already present in adjacent retained text and its sole residual
> function is to grade the candidate's evidence, announce sophistication or tell
> the reader what to conclude. Never delete the only employer bridge, factual
> caveat, claim boundary, qualification, lifecycle distinction or unique
> professional judgment.
>
> Express the locked content so a Norwegian hiring manager is likely to
> experience the writer as competent, grounded, useful, interesting, credible
> and easy to work with, rather than impressive-seeking, intense or
> self-conscious.
>
> Only now, in FINAL_AND_REVIEW after the substantive content is locked, read
> FORFATTERSTEMME.md and apply its ordinary expression guidance. If the bundle
> contains final_polish.social_register_calibration, apply the corresponding
> extended register pass from that file once, still under this entire lock.
> A missing setting means no extended pass for that historical bundle.
> REVIEW_ONLY performs no polish. The setting never governs evidence selection,
> drafting, substantive repair, claim strength, page fit or triage. Do not add
> a review field, marker count, evidence-preservation list or quality score.

The deletion licence sits exactly on the line between realization and meaning.
A sentence whose only remaining job is to interpret the candidate for the reader
is realization, and may go. A sentence carrying employer-relevance reasoning is
meaning, and stays — even when it reads like a conclusion. When you cannot tell
which one you are looking at, keep it.

Do not solve self-importance by weakening owned accomplishments. Adding hedges,
softening work verbs, introducing self-deprecation or replacing `jeg` with a
vague `vi` all damage the register this pass exists to protect. Remove the
self-grading and the redundant explanation instead.

## Completion and continuation
Return only allowed semantic fields. Use submission.command verbatim, with
both return files in FINAL_AND_REVIEW. Only an accepted commit completes the
semantic result. Immediately finalize then render this same job for READY,
CHECK and RERUN, without human-name/date/force overrides. PDF degradation is
separate from semantic validity; do not reauthor for a converter failure.
Then obtain fresh next/context for the next job in this Stage-3 scope and reset
fully. D Variasjon innenfor en klynge owns semantic variation. Never advance
to another semantic stage in this instance/chat.
