# Jobbsok_26 Final Pilot-Learned Perfection Pass
## Non-Authoritative Considerations for Implementing Models

**Status:** deliberation input only.  
**Authority:** NONE. This file is intentionally non-authoritative. It records reasoning, observed pilot issues, design possibilities, trade-offs, and tentative recommendations developed during review of the first two real vacancies. The implementing model must validate every repository-specific statement against the actual current repository, frozen architecture, run artifacts, rendered documents, and current user instruction before accepting it.

**Do not treat this file as a specification, implementation plan, architecture amendment, or instruction to preserve any particular mechanism.** The implementing model owns the final implementation decisions. Where this file conflicts with current explicit user instruction, the frozen architecture, or actual repository state, this file loses.

---

# 1. Why this pass exists

The first two real pilot vacancies demonstrated that Jobbsok_26 is already capable of producing materially tailored, truthful, professional application packages. The value of the pilot is therefore no longer to prove that the framework can mechanically run. It is to identify the gap between a strong package and the best package the framework can reasonably produce without abandoning MVP-KISS discipline.

The current pass should be understood as a **pilot-learned optimization pass**, not a return to speculative architecture construction.

The core optimization order remains:

1. Employer-facing package quality and chance of interview.
2. Truth and evidence integrity.
3. Authentic candidate representation.
4. Low human handling and low operator friction.
5. Pipeline coherence and predictable recoverability.
6. Simple and robust implementation.
7. Auditability where materially useful.
8. Cost and optionality.

The pass may accept small increases in implementation complexity where the expected quality gain is material and well supported by the pilot, but each expansion should be bounded to the smallest surface that can realistically deliver the intended effect.

---

# 2. Pilot context to inspect directly

The implementing model should reconstruct the actual current run from disk rather than relying on this summary.

Known pilot identity from the conversation:

```text
run_id:  r20260828-213932-7f13b4
cluster: pilot_live_smoke

jobs:
  huseierne_strategi_maalstyring
  avinor_digital_transformasjon
```

The first two real pilot jobs were:

- Huseiernes Landsforbund - Strategi- og malstyringsradgiver.
- Avinor AS - Seniorradgiver Digital Transformasjon.

Both completed Stage 1 and Stage 2 without mechanical refusal or recovery. Stage 3 produced final packages and rendered documents. The final DOCX files were structurally valid and opened normally after being copied outside the Codex-generated output directory. The original output directory exhibited a Windows access/ACL problem. That environment issue should be investigated separately from semantic package quality and should not be allowed to contaminate the writing analysis.

The implementing model should inspect, where present, at minimum:

- frozen vacancy source for each job;
- normalized vacancy/source-inspection artifacts;
- manifest and frozen settings;
- Stage 1 handoff and `strategy.json`;
- Stage 2 handoff and `draft_package.json`;
- Stage 3 handoff, `final_package.json`, and `review.json`;
- all failure/currentness/render receipts;
- `render_report.json`;
- final DOCX and PDF outputs;
- page counts and page warnings;
- the actual Word templates and style definitions;
- writing doctrine and persuasion policy;
- stage instructions;
- `PERSONALITY_PROFILE.md` and any distilled personality handoff;
- candidate factual authorities and evidence index;
- any current GATE/report evidence that bears on the pilot.

The cross-stage lineage is especially important. For every observed final-package weakness, identify **where the weakness first entered the pipeline** and whether a later stage had both the information and authority to repair it.

---

# 3. Four user-set behavioral outcomes

The implementation mechanism for each rule is deliberately left open. The final behavioral outcomes are not.

## 3.1 Readability over fit-to-page

The current pilot CVs used approximately Calibri 9 for most body text, and the application letters approximately Calibri 10.5. The pilot review found this unnecessarily small, particularly because the second CV page was sparsely populated. The system was sacrificing readability without receiving a corresponding information-density benefit.

Desired behavior:

- Main employer-facing body text should default to **12 pt**.
- If a document exceeds its desired page target, **edit/compress content before shrinking normal prose**.
- Smaller text is reserved for content that is intentionally subordinate, such as metadata or compact secondary labels.
- Avoid micro-tuning typography through half-point sizes merely to make text fit.
- Prefer a discrete human-readable size scale. The user preference is 8, 9, 10, 11, 12 and then even-numbered sizes above 12 where useful.
- The rule is a readability constraint, not an instruction that every character in a CV must be 12 pt.

Questions for implementation:

- Is this best enforced entirely in the Word masters/style map?
- Do current templates contain several body styles that must be normalized?
- Does 12 pt require content-allocation changes to preserve the two-page CV target?
- Should the letter remain one page, and if so what content-compression policy should precede any font reduction?
- Do existing page-target warnings need recalibration after typography changes?
- Does the current page-2 whitespace indicate a content-layout defect independent of font size?

A key multivariate effect is expected: larger body text interacts directly with CV length, page balance, content selection, section density, template spacing, and page warning behavior. It would be a mistake to change font size in isolation and then respond to resulting overflow by shrinking other dimensions mechanically.

## 3.2 Earned motivation only

The pilot demonstrated a difference between credible employer-specific motivation and performative mission rhetoric.

Avinor's societal and operational importance is plausibly relevant to the candidate's motivation because the role concerns safety-critical national infrastructure, regulated operations, digital transformation, and continuity. Huseierne's member mission was used in a sentence equivalent to:

> Better business governance at Huseierne supports the mission of making it safer and easier to own a home, and this particularly motivates me.

The user found this performative and inauthentic.

Desired behavior:

- Motivation should first be grounded in the **actual work**, problem, responsibility, operating environment, learning opportunity, leverage, autonomy, capability expansion, or type of contribution.
- Employer mission or societal importance should be used only when it is genuinely consequential **and** credibly motivating for this candidate.
- When in doubt, omit mission-based enthusiasm rather than manufacture it.
- Employer-specific motivation is still valuable, but specificity must not be confused with ceremonial praise.
- The system should not feel obliged to produce a dedicated "mission motivation" paragraph.

Potential general hierarchy for motivation, to be adjudicated by the implementing model:

1. Actual work and decision problem.
2. Responsibility and contribution shape.
3. Operating environment and organizational setting.
4. Learning, leverage, capability building, or transformation opportunity.
5. Employer-specific subject matter.
6. Societal/mission importance only when genuinely earned.

This rule is probably partly universal writing doctrine and partly reinforced by the candidate's personality profile, which describes motivation as much more strongly tied to mastery, truth, leverage, autonomy, capability expansion, and durable improvement than to status, conformity, or ritual signaling.

## 3.3 Maximum truthful leverage

This is the strongest refinement of the existing claim-ceiling philosophy.

The current framework has correctly optimized against overclaiming. The pilot revealed the opposite failure mode: the model can sometimes attenuate known truth through unnecessary hedging.

Example from the pilot:

- Better: `Rammeverket ... er fortsatt i bruk om lag 2,5 ar senere.`
- Worse: `Rammeverket ... var rapportert i bruk om lag 2,5 ar senere.`

Assuming the evidence authority establishes that the framework is in fact still in use, the second formulation introduces epistemic distance and uncertainty that the evidence does not contain. It therefore reduces persuasive value and alters the epistemic proposition in the wrong direction.

Desired behavior:

> **Facts are immutable. Their employer-relevant articulation should be maximally effective.**

More explicitly:

1. Nothing may exceed the factual authority.
2. Once a proposition clears the truth bar, the model should use the strongest accurate verb, attribution, specificity, emphasis, placement, consequence, and employer-relevant framing that the evidence can defend.
3. The model must not add uncertainty, distancing language, passive attribution, or hedges that are absent from the evidence.
4. Known truth should sound known.
5. If the evidence itself is qualified, approximate, contested, historical, or uncertain, that qualification remains part of the ground truth and must be preserved.
6. The model may reframe a known fact for employer relevance, but may not change the underlying proposition or invent a causal consequence.
7. Understatement that materially reduces interview value should be treated as a quality defect just as unsupported inflation is.

This creates both a **truth ceiling** and a **leverage floor**.

Examples:

```text
evidence: "sto for hoveddelen av kodeendringene"
acceptable high-leverage wording: "sto for hoveddelen av kodeendringene"
under-leveraged: "bidro med kodeendringer"
unsupported inflation: "ledet hele utviklingen"
```

```text
evidence: "arbeidet i et firepersonsteam"
acceptable: preserve team contribution and own substantiated role
unsupported: imply sole ownership or formal leadership
```

The candidate accepts responsibility for keeping factual authority files current. The semantic stages should treat those authorities as the most established ground truth available. If the model cannot rely on those authorities with appropriate confidence, the entire evidence architecture loses value.

Important implementation boundary:

- This is **not** permission to infer new achievements from plausible consequences.
- It **is** permission and obligation to articulate the known achievement at its strongest defensible persuasive level.

## 3.4 Plain human punctuation, with a hard no-en-dash/no-em-dash rule

The pilot reinforced a user preference that also reduces a common polished-LLM signature.

Desired behavior:

- En dash `–` and em dash `—` are **strongly prohibited** in employer-facing text.
- This should be treated as close to a hard style rule, but it does not necessarily justify introducing a dedicated Python validator.
- Ordinary hyphen `-` remains allowed where normal human writing genuinely calls for it, including compounds, dates, ranges, and similar structural uses.
- Do not use a hyphen merely as clause punctuation when a comma, period, colon, or parentheses can do the same job.
- Prefer ordinary punctuation: `.`, `,`, `:`, `()`, `?`, `!`, and quotation marks where natural.
- Semicolon is permitted but should be uncommon.
- `|` remains appropriate as a structural divider in headings/titles.

The exact mechanism is open:

- writing doctrine;
- professional voice profile;
- Stage 3 instruction;
- template normalization;
- lightweight final review instruction;
- or some combination.

Avoid overengineering a character-level lint subsystem unless the repository already contains a natural and essentially free enforcement point.

---

# 4. The current personality mechanism and the newly identified missing channel

The pilot exposed an important distinction between **personality as positioning** and **personality as professional voice**.

## 4.1 What the existing personality mechanism appears designed to do

The current `PERSONALITY_PROFILE.md` defines personality as an interpretive source, not factual authority. Stage 1 may select 0-3 vacancy-relevant facets and bind them to factual evidence. The selected facets can shape:

- evidence selection;
- candidate framing;
- desired recruiter interpretation;
- misread prevention;
- motivation interpretation;
- expression ceilings.

This is valuable and should not be discarded merely because the pilot revealed a different unmet need.

The current mechanism answers roughly:

> **What about this candidate should matter for this vacancy, and how should the evidence be interpreted?**

## 4.2 The missing function

The pilot question was not whether the application contains personality-consistent facts. The candidate's work naturally reflects his personality, so many factually grounded passages will align with personality even if the personality mechanism contributes nothing.

The more diagnostic question is:

> **How would a person with this personality construct and express a professional argument?**

The profile predicts a distinctive professional writing fingerprint, including tendencies such as:

- claim/recommendation first, rationale second;
- causal and mechanistic language over decorative adjective language;
- explicit preservation of meaningful distinctions rather than smoothing them away;
- high information density without forced brevity;
- narrow/local qualifications with strong confidence inside the supported boundary;
- behavior/mechanism rather than favorable personality labels;
- specific judgments rather than universally agreeable professional platitudes;
- motivation grounded in work content, mastery, leverage, learning, autonomy, and useful improvement rather than ritual employer praise;
- relatively low social lubrication, while remaining professional and cooperative;
- strong macro-structure with more natural, less lacquered local prose;
- precision and directness without caricatured bluntness;
- simple punctuation and limited stylistic ornament;
- a tendency to explain how/why something works rather than merely label it as strategic, innovative, exciting, or important.

This layer should not imitate chat quirks or make every paragraph sound analytical. It should make the package plausibly written by this particular person in a professional context.

The desired effect can be summarized as a **ME-anizer**, not a generic humanizer.

## 4.3 Evidence from the pilot

Some passages already show traces of this voice.

A particularly strong Avinor example was equivalent to:

> Expectations must be verifiable, responsibility and assumptions must be visible, and the method must work for the people who use it.

This has a distinctive claim -> criteria -> auditability -> user-practicality structure.

Other passages preserve tensions such as improvement versus operational continuity and dependencies, which fits the candidate's tendency to preserve causal distinctions.

However, large portions of both letters still use generic polished application rhetoric:

- rhetorical employer-problem opening formulas;
- ceremonial closing language;
- generic `I want to contribute...` constructions;
- mission-motivation language that feels borrowed from employer branding;
- highly symmetrical application structure;
- polished transitions that could plausibly occur in many LLM-generated applications.

The Huseierne package showed this more strongly than Avinor.

The current personality system therefore appears more effective at deciding **what to say** than at making the final output sound like **the person who is saying it**.

---

# 5. Architectural options for the professional-voice function

The implementing model should independently adjudicate these. The following ranking is tentative only.

## Option A - Dedicated frozen professional-voice context, primary consumer Stage 3

Concept:

```text
Stage 1:
  vacancy + evidence + existing Personality.md positioning lens
  -> strategy

Stage 2:
  strategy + evidence + writing doctrine + distilled positioning guidance
  -> strong native factual draft

Stage 3:
  vacancy + evidence + strategy + draft + writing doctrine
  + candidate-specific PROFESSIONAL_VOICE context
  -> final package + review
```

The new context would be candidate-specific but would have:

```text
factual_authority = false
claim_authority = false
strategy_authority = false
qualification_authority = false
```

It would influence only professional expression and rhetorical construction.

Possible content:

- argument posture;
- sentence architecture;
- local syntax;
- degree and location of qualification;
- causal/mechanistic preference;
- motivation language;
- social-temperature calibration;
- lexical preferences;
- punctuation preferences;
- anti-caricature rules;
- different conditioning levels for CV and application.

Potential advantages:

- clean separation of concerns;
- voice remains always available even when Stage 1 selects zero personality facets;
- no pollution of `strategy.json`;
- no need for a new semantic stage or artifact;
- candidate voice can evolve independently from generic writing doctrine;
- exact voice file can be frozen/hashed for provenance;
- easy A/B testing against existing pilot outputs;
- Stage 3 already owns final reconstruction.

Potential disadvantages:

- Stage 3 must be willing to reconstruct rather than merely polish;
- a generic Stage 2 draft may anchor Stage 3 more than desired;
- introduces one additional frozen context surface and corresponding plumbing/tests.

Tentative ranking: **#1**.

## Option B - Dedicated professional-voice context supplied to both Stage 2 and Stage 3

Concept:

```text
Stage 1 -> strategy
Stage 2 + voice -> first complete authored package
Stage 3 + same voice -> reconstruct/finalize while preserving candidate authorship
```

Potential advantages:

- voice enters at original composition rather than being retrofitted;
- reduces generic Stage 2 anchoring;
- potentially highest absolute writing quality if both stages use the same source coherently.

Potential disadvantages:

- duplicated responsibility;
- more context and cognitive load in two stages;
- harder causal diagnosis if voice degrades;
- Stage 2 may spend effort on voice instead of strategy execution/content completeness;
- greater risk of overconditioning/cosplay;
- Stage 3 still needs full voice responsibility because it may reconstruct everything.

Tentative ranking: **#2**, especially as an escalation if Stage-3-only voice conditioning proves insufficient in testing.

## Option C - Professional voice as a dedicated subsection/translation inside `PERSONALITY_PROFILE.md`, consumed by Stage 3

Potential advantages:

- one candidate personality/voice source;
- reduced risk that personality and voice drift conceptually;
- fewer top-level context files.

Potential disadvantages:

- the existing personality file is large and contains internal-only typology, failure modes, misread controls, and collaboration guidance irrelevant to final copy;
- passing the full file to Stage 3 may increase cosplay and context noise;
- current distillation boundaries appear deliberately intended to avoid giving writers the whole personality model;
- extracting only a subsection may itself create a small routing mechanic.

Tentative ranking: **#3**.

## Other options considered

### Put voice directly into Stage 1 / `strategy.json`

Generally unattractive because voice is mostly candidate-invariant while strategy is vacancy-specific. It conflates `what to say` with `how this person says it`, and could make voice disappear when Stage 1 legitimately selects zero personality facets.

### Put candidate voice directly into `WRITING_DOCTRINE.md`

Very cheap, but conceptually muddy. Generic good Norwegian application writing and candidate-specific professional expression are different sources of truth. A candidate-specific voice rule should not silently become universal writing doctrine.

### Stage 2 only

Likely insufficient because Stage 3 is the final reconstructive writer and can wash out Stage 2 voice.

### Add Stage 4 / Stage 3.5

Conceptually clean but operationally expensive and likely contrary to MVP-KISS. It would create questions about artifact ownership, state, render eligibility, recovery, context modes, and final authority merely to perform work Stage 3 already owns.

### Dynamic per-vacancy voice generated by Stage 1

Likely unnecessary stochastic drift. Candidate voice should be canonical; employer-specific register adaptation belongs to the writer.

### Deterministic humanizer/linting subsystem or LLM judge

Strongly disfavored. The objective is generative candidate-specific authorship, not cosmetic anti-AI entropy or a numeric `sounds like Vegard` score.

---

# 6. Where the professional-voice layer should act if Stage 3 owns it

If the implementing model lands on Stage 3 as primary owner, the important distinction is:

> **Do not describe it as cosmetic final polish. Treat it as final authorship.**

A useful conceptual order is:

1. Vacancy: what does the employer actually need?
2. Facts/evidence: what is established?
3. Independent final judgment: what should the package actually say?
4. Strategy/draft: what upstream material is useful?
5. Writing/persuasion doctrine: is this a strong application?
6. Professional voice: how would this candidate naturally construct and express this exact argument?
7. Final reconstruction: write the integrated package.
8. Final tests: truth, maximum leverage, employer specificity, readability, voice authenticity, complementarity.
9. Triage.

Voice should be applied **after factual and strategic grounding** to prevent personality cosplay.

The layer may influence:

- argument posture;
- paragraph order;
- sentence architecture;
- opening style;
- motivation framing;
- local certainty calibration;
- degree of social lubrication;
- lexical choice;
- punctuation;
- information density and rhythm.

It may not independently change:

- factual truth;
- qualification status;
- evidence authority;
- responsibility scope;
- outcomes;
- claim ceilings;
- job-fit classification.

It may restructure presentation of already-supported propositions because voice is not merely vocabulary.

---

# 7. Voice calibration: moderate, not cosplay

The target is not to imitate informal chat.

The target is also not to maximize visible personality signals.

A useful qualitative target is:

- predominantly clean professional application prose;
- enough candidate-specific cognitive/rhetorical fingerprint that the output does not read like generic over-perfected LLM copy.

Do not encode fake precision such as `voice_strength = 0.25` unless the actual current framework already has an elegant mechanism that genuinely benefits from such a setting.

Positive voice features should generally be tendencies, not quotas.

Bad approach:

```text
[ ] exactly one causal statement per paragraph
[ ] two explicit distinctions
[ ] maximum three adjectives
[ ] one personality phrase
```

Better approach:

> Use these tendencies as a generative prior. Preserve naturalness, employer readability, and persuasion. Do not perform the personality.

Hard prohibitions, such as no en/em dash, may reasonably be stronger than positive stylistic tendencies.

---

# 8. Employer adaptation versus stable voice

A professional voice profile should distinguish stable authorial invariants from vacancy-dependent register.

Potential invariants:

- precision;
- causal structure;
- low performativity;
- confidence inside evidence boundaries;
- explicit distinctions where material;
- preference for concrete mechanisms;
- relatively low ceremonial rhetoric;
- dense useful signal.

Potential variables:

- warmth;
- formal register;
- technical depth;
- sentence length;
- degree of abstraction;
- explanation density;
- assertiveness;
- vocabulary domain.

The output for Avinor should not sound identical to the output for Huseierne, but both should plausibly have the same author.

---

# 9. Pilot issues already observed, to trace rather than assume

These are **observations to investigate**, not pre-adjudicated defects.

## OBS-01 - CV body typography appears too small

Observed approximately Calibri 9 body text in the pilot CVs.

Potential causes:

- template style definitions;
- original desire to force two pages;
- static layout choices;
- no readability floor in writing/template policy.

Potential interactions:

- page targets;
- section spacing;
- amount of content;
- second-page underutilization.

## OBS-02 - Application body typography appears unnecessarily small/oddly tuned

Observed approximately Calibri 10.5.

Potential causes/interactions similar to OBS-01.

## OBS-03 - CV page 2 substantially underutilized

Both pilot CVs appeared dense on page 1 and sparse on page 2.

Potential causes:

- static section/page break behavior;
- content partitioning;
- template layout;
- insufficient use of relevant evidence;
- fixed ordering that pushes only low-value historical material to page 2;
- mismatch between font sizing and section allocation.

This issue should be analyzed jointly with typography rather than independently.

## OBS-04 - Some openings feel rhetorically performative

The Avinor opening was strategically useful but polished in a recognizable `When employer X does Y, it must achieve Z without sacrificing Q` consultant/LLM form.

The Huseierne opening more strongly resembled an external consultant restating the employer's business situation back to the employer.

Potential root causes:

- persuasion doctrine rewarding employer-problem framing too literally;
- Stage 2 stock opening patterns;
- Stage 3 insufficient reconstructive voice conditioning;
- employer-specificity test accidentally rewarding explicit vacancy-summary language.

The fix should not ban employer-problem openings. It should distinguish openings that genuinely create a useful candidate bridge from openings that merely demonstrate vacancy comprehension.

## OBS-05 - Huseierne motivation feels borrowed/performative

Mission language about making it safer/easier to own a home felt inauthentic relative to the candidate's actual motivation profile.

Trace:

- Did Stage 1 specify this motivation?
- Did Stage 2 invent it?
- Did Stage 3 retain or strengthen it?
- Did personality guidance contain enough information to prevent it?

Potential root causes:

- generic application-writing prior;
- persuasion doctrine over-rewarding employer mission specificity;
- personality system focused on positioning rather than motivation/voice;
- Stage 3 lacking full/appropriate candidate motivation context.

## OBS-06 - Truth attenuation: `var rapportert i bruk`

One package weakened a fact that another package stated correctly as current continued use.

Trace exactly where the hedge first appeared.

Potential root causes:

- claim ceiling interpreted as `always hedge`;
- model uncertainty about evidence authority;
- strategy expression ceiling too conservative;
- Stage 2 hedging;
- Stage 3 failure to maximize truthful leverage;
- evidence phrasing itself may differ from recollection and must be verified.

This issue has high importance because it indicates a systemic truth-calibration asymmetry rather than mere style.

## OBS-07 - En/em-dash and dash-like punctuation contributes to LLM voice

Distinguish:

- text generated by semantic stages;
- dashes already present in static template content;
- date/range typography;
- headings.

The new rule is specifically a hard prohibition on `–` and `—` in employer-facing text, while ordinary `-` remains legitimate.

## OBS-08 - Letters share a strong common structural skeleton

Both letters followed a similar sequence and similar length:

```text
employer problem
proof case 1
proof case 2
current role/collaboration
employer-specific motivation
polite close
```

This may be a good reusable argument structure, or it may be excessive formulaicity.

Do not infer defect merely from similarity. Evaluate whether the structure is the optimal argument for each vacancy and whether Stage 3 is sufficiently free to choose different shapes.

## OBS-09 - Current personality mechanism has limited visible authorial effect

Positioning/evidence selection appear personality-consistent, but the final writing often still sounds like generic polished application prose.

Potential root cause is not necessarily that personality is weak. The current mechanism may simply be designed for a different channel: evidence interpretation and recruiter framing rather than syntax/rhetoric/authorship.

## OBS-10 - Objection handling may be too implicit

Huseierne included explicit fit gaps such as five years of experience and practical OKR experience. The package avoided false claims, but did not necessarily make the strongest truthful transfer argument or explicit objection handling.

Potential interaction with maximum truthful leverage: avoiding overclaiming should not imply avoiding strong argumentation around adjacent evidence.

## OBS-11 - Some employer-facing language is over-polished rather than candidate-specific

Examples include generic ceremonial closings, `I want to contribute...`, mission rhetoric, symmetrical paragraph transitions, and stock professional phrases.

This is the primary observed surface symptom motivating the professional-voice layer.

## OBS-12 - Original rendered output directory had a Windows access/ACL problem

The generated DOCX could be copied to the user's Documents folder and opened normally there, while Word could not open it in the original run output directory and normal PowerShell could not read its ACL.

This appears orthogonal to document semantics but is real operator friction and should be root-caused if still present.

Do not allow this issue to trigger unrelated semantic changes.

---

# 10. Required style of root-cause analysis

For every identified issue, the implementing model should establish a causal chain rather than jump from symptom to fix.

Example format:

```text
Observed final symptom
  -> first stage/artifact where symptom appears
  -> upstream input or policy that encouraged it
  -> why later stage did/did not repair it
  -> whether template/runtime amplified it
  -> exact boundary of affected behavior
  -> smallest surface capable of fixing the root cause
```

The model should explicitly distinguish:

- direct cause;
- contributing cause;
- enabling condition;
- downstream failure to repair;
- unrelated correlated observation.

A multivariate root cause is acceptable and expected where supported.

For example, generic final voice could plausibly arise from:

```text
Stage 2 generic drafting prior
+ limited downstream personality context
+ Stage 3 anchoring on a good-enough draft
+ writing doctrine rewarding polished employer specificity
= polished but weakly candidate-specific final prose
```

Do not force a single-cause explanation where the evidence shows interaction.

---

# 11. Boundary discipline to prevent over-refactoring

For every issue, define **what is actually suboptimal and what is not**.

Example:

Bad scope statement:

> The rendering/template system needs redesign because the CV typography is too small.

Better:

> The normal body styles used by dynamic CV prose are below the desired readability target. Page 2 is simultaneously underutilized. Investigate body style sizing, section allocation, and page-break behavior. Do not modify render provenance, converter semantics, or artifact ownership unless direct evidence shows they cause the layout problem.

Likewise:

Bad:

> Personality needs redesign.

Better:

> Existing vacancy-specific personality positioning may remain valid. The observed deficiency is that final professional syntax/rhetoric is weakly candidate-specific. Introduce or strengthen only the expression channel necessary to address that deficiency.

Every fix proposal should name explicit **non-target surfaces**.

---

# 12. Multivariate interactions that deserve special attention

The implementing model should search for additional interactions, but at minimum reason about the following.

## 12.1 Typography x page target x content selection x page balance

12 pt body text may create overflow. The intended response is not automatic shrinkage. The system may need better content compression, section allocation, or template balance.

The current sparse second page suggests the layout problem is not merely `too much content`.

## 12.2 Maximum truthful leverage x evidence authority x claim ceiling

Strengthening articulation increases interview value but can increase overclaim risk if the model blurs the line between:

- fact;
- defensible framing;
- inference;
- causal consequence.

The final design must strengthen confidence **inside** the evidence boundary, not move the boundary.

## 12.3 Professional voice x earned motivation

A good voice layer should naturally suppress generic mission rhetoric because the candidate's motivation model is strongly grounded in mastery, leverage, truth, autonomy, learning, and durable improvement.

Avoid implementing the same correction redundantly in two places unless each serves a distinct function.

## 12.4 Professional voice x generic writing doctrine

Writing doctrine should answer `what makes a good application`. Candidate voice should answer `how this candidate professionally expresses it`.

If both carry the same rules, drift and duplication result.

## 12.5 Professional voice x existing personality positioning

The two mechanisms should reinforce one another without becoming a feedback loop.

Positioning may select candidate characteristics because they matter to the vacancy. Voice should not then search for facts merely because they sound personality-consistent.

## 12.6 Professional voice x Stage 2 anchoring

If Stage 3 receives voice only at the end, a strong generic Stage 2 draft may anchor structure and language. Determine empirically whether Stage 3's reconstructive authority is sufficient.

This is the main argument for the Stage-2+Stage-3 alternative.

## 12.7 Voice/directness x employer register

Candidate-specific precision/directness must still adapt to public-sector, private-sector, technical, executive, and collaborative contexts.

Authenticity does not mean identical register across employers.

## 12.8 No-en/em-dash x template typography

The semantic model may comply while static templates still contain prohibited characters. The final desired state is employer-facing output compliance, not merely generated-prose compliance.

## 12.9 Earned motivation x employer specificity test

An overly literal employer-swap test can unintentionally reward borrowed mission language because mission text is highly employer-specific.

The final policy should distinguish **specificity** from **authentic relevance**.

## 12.10 Maximum truthful leverage x objection handling

The system should not respond to explicit fit gaps merely by becoming quiet. It should search factual authorities for the strongest legitimate transfer argument while preserving the actual gap.

## 12.11 Voice x letter formulaicity

A candidate-specific voice layer may reduce stock wording while leaving a stock macro-structure intact. Evaluate both syntax and argument architecture.

## 12.12 Readability x ATS/machine parsing

Any template change must preserve machine-readable structure and the existing template/control contract.

## 12.13 Layout x render determinism

Changing font/style/spacing may affect page counts and output stability. Preserve deterministic render semantics unless directly implicated.

## 12.14 Pilot-learned fixes x representative cluster throughput

A fix that produces excellent two-job output but materially increases per-job cognitive complexity, failure rates, or human review burden may be a net regression at cluster scale.

---

# 13. Suggested professional-voice content model if a distinct source is chosen

This is illustrative, not prescriptive.

A compact candidate-specific voice source could contain:

## Purpose

Write employer-facing material as this candidate would plausibly write when making a serious professional argument. Do not imitate informal chat or manufacture quirks.

## Professional argument habits

- State the material proposition early.
- Explain mechanisms and causal links rather than relying on adjectives.
- Preserve distinctions that matter to the conclusion.
- Prefer concrete evidence and precise verbs.
- Keep qualifications narrow and local.
- Use strong certainty where facts are established.
- Avoid ornamental consensus language and empty professional enthusiasm.

## Motivation register

- Work/problem fit first.
- Mastery, leverage, learning, autonomy, capability expansion, and useful improvement are credible motives.
- Mission language only when genuinely consequential and plausibly motivating.

## Social temperature

- Direct but professional.
- Cooperative without excessive ritual politeness.
- Do not caricature bluntness or low warmth.

## Syntax/rhythm

- High information density while preserving readability.
- Strong macro-structure.
- Natural local prose rather than perfectly lacquered transitions.
- Occasional longer sentence where qualification genuinely requires it.

## Punctuation

- No en dash or em dash.
- Ordinary hyphen where human orthography/notation calls for it.
- Prefer periods and commas.
- Semicolon rare.

## Anti-caricature

- Do not make every paragraph analytical.
- Do not force systems jargon.
- Do not insert personality labels.
- Do not imitate casual/chat punctuation or slang.
- Do not make the candidate sound combative.
- Do not repeat an identical rhetorical skeleton across vacancies without current-job justification.
- Employer persuasion and readability outrank visible personality signaling.

## Channel calibration

- CV: light voice conditioning, especially profile/headline/core bullets.
- Letter: moderate voice conditioning, especially opening, argument structure, motivation, certainty, and closing.

---

# 14. Shadow-test concept before or during implementation

A high-value validation design would compare the existing final packages with voice-conditioned alternatives while holding factual content constant.

Possible experiment:

```text
existing final package
+ exact vacancy
+ factual authorities
+ candidate professional-voice source
-> shadow Stage-3 rewrite
```

Evaluate side-by-side:

- stronger/weaker employer persuasion;
- truth preservation;
- factual certainty calibration;
- candidate-specific voice;
- generic LLM residue;
- performativity;
- motivation authenticity;
- readability;
- structural naturalness;
- recruiter scan value;
- cross-job differentiation;
- whether the output sounds like a professional version of the same person across both jobs.

The experiment should not become a permanent new stage merely because it is useful for validation.

---

# 15. What should probably remain unchanged unless evidence says otherwise

This list is deliberately conservative.

- Existing three semantic stages.
- Vacancy-atomic artifact ownership.
- Stage 1's vacancy-first/evidence-first decision architecture.
- Existing personality-as-positioning concept.
- Stage 2 as complete native package writer.
- Stage 3 as elastic final writer/reviewer.
- Human-only external submission.
- Truth/evidence authority boundaries.
- Render/finalization state separation.
- Frozen-run provenance model.
- Bounded recovery model.
- No LLM-as-judge quality score.
- No automatic submission.
- No deterministic content truncation to satisfy page targets.

Any change to these surfaces needs direct causal evidence from the pilot or from the interaction of accepted fixes.

---

# 16. Potential additional issues the implementing model should actively search for

Do not assume the above registry is complete. The model should search for at least:

- Stage 1 route errors or avoidable weak route choices.
- Evidence omitted despite high employer value.
- Evidence included despite low employer value.
- Claim ceiling too high or too low.
- Objections detected but not mitigated.
- Personality facets selected but not expressed usefully.
- Personality guidance causing overfitting/cosplay.
- Stage 2 generic filler or CV/letter repetition.
- Stage 2 evidence order that Stage 3 should have changed but did not.
- Stage 3 failure to reconstruct weak upstream material.
- Stage 3 defensive `CHECK`/`RERUN` behavior.
- Triage calibration against the actual human review.
- Employer-swap-test false positives/false negatives.
- Readability/typography/spacing inconsistencies.
- Page balance.
- Section order.
- Low-value historical content occupying valuable CV space.
- Unnecessary headings, duplicated title lines, boilerplate closings.
- Norwegian phrasing that is grammatically valid but not native/natural.
- Translated-American application rhetoric.
- Overuse of `jeg` sentence starts.
- Unnecessary abstractions or consultant language.
- Excessive technicality.
- Missing commercial/organizational bridge where relevant.
- Unnecessary repetition across CV and letter.
- Cross-job phrase leakage or formulaic reuse.
- Unsupported or attenuated certainty.
- Template style anomalies.
- Render warnings that fail to route attention effectively.
- Output filename/path/operator-friction defects.
- Any pilot instrumentation that failed to capture a high-value human observation.

Each new finding should be traced to root cause and classified by recurrence likelihood before it is admitted to the final change set.

---

# 17. Suggested classification for every issue

A useful issue registry could contain:

```text
ID
Title
Observed artifact(s)
Job(s)
Stage first introduced
Stage(s) that could have repaired it
Expected behavior
Actual behavior
Employer-facing consequence
Human-review consequence
Severity
Recurrence likelihood
Systemic vs local
Root cause(s)
Contributing factors
Confidence in root-cause attribution
Scope boundary
Proposed fix
Why that surface is the correct fix surface
Top alternatives
Why alternatives lose
Interactions with other proposed fixes
Architecture impact
Implementation cost/risk
Verification method
Pilot/cluster acceptance criterion
Non-target surfaces
```

This makes it difficult to smuggle speculative redesign into a local quality issue.

---

# 18. Architecture-change posture

The implementing model should produce an explicit architecture diff, even if the correct result is `no frozen architecture amendment required` for some or all changes.

For each proposed change, classify it as one of:

- implementation-only correction;
- policy/writing-doctrine refinement;
- template configuration change;
- context/frozen-input addition;
- stage-responsibility clarification;
- actual architecture amendment.

Architecture amendments should be used only when the intended behavior cannot truthfully be represented within the existing architecture. If an amendment is needed, define the smallest normative diff and all downstream consequences explicitly.

Do not silently reinterpret frozen architecture merely to avoid the word `amendment`.

Likewise, do not amend architecture simply because a new concept has been given a name.

---

# 19. Final-plan quality bar

The final plan should leave the implementing agent with essentially zero design work.

It should specify:

- exact files to inspect/change;
- exact intended behavioral changes;
- exact functions/sections/styles/schemas if applicable;
- exact invariants to preserve;
- exact dependencies between changes;
- exact order of implementation;
- exact TDD/red-green tests where failures could be silent or expensive;
- exact public-command/end-to-end verification;
- exact two-pilot regression/re-render procedure;
- exact representative-cluster acceptance gate;
- exact changed-file/scope gate;
- explicit rollback/stop conditions;
- explicit `do not change` surfaces.

Where the repo makes a proposed change unnecessary, the plan should say so and remove it.

Where two fixes overlap, the plan should consolidate rather than layer redundant mechanisms.

Where an observed issue is sufficiently mitigated by another accepted change, the issue registry should record that rather than invent an additional fix.

---

# 20. Stopping rule

This pass is intended to be the final pilot-informed optimization pass before representative-cluster use.

The stopping principle should be approximately:

> Implement the smallest coherent set of changes that can reasonably remove the observed material suboptimalities and realize the high-value trade-offs identified by the two-job pilot. Permit small complexity increases when the expected employer-facing value is material. Do not expand the patch beyond the surfaces necessary to realize those gains and preserve pipeline coherence.

After implementation and verification:

1. Re-run/re-render the two pilot jobs through the changed surfaces as necessary.
2. Compare against the original pilot outputs.
3. Require no material regression in truth, tailoring, render stability, workflow, or handling.
4. Require the targeted quality defects to be materially improved.
5. Run one representative cluster.
6. Only observed material blockers may justify another framework change cycle.

The goal is not theoretical perfection. The goal is a stable production system whose remaining imperfections are cheaper to handle manually than to engineer away.

---

# 21. Compact decision summary from the preceding discussion

These are **tentative considerations, not implementation instructions**:

1. The existing personality mechanism should probably remain focused on vacancy-specific positioning/evidence interpretation.
2. A second professional-voice mechanism has a distinct purpose and should not be forced through the same 0-3-facet path.
3. Stage 3 is the strongest candidate for primary voice ownership because it already owns final reconstruction and is the point where generic polished LLM residue is observed.
4. A compact, candidate-specific, frozen professional-voice source exposed to Stage 3 appears to offer the cleanest separation of concerns.
5. Stage 2 + Stage 3 voice conditioning is the strongest alternative if Stage-3-only conditioning proves too anchored by generic upstream prose.
6. Full `PERSONALITY_PROFILE.md` exposure to Stage 3 is a plausible but context-heavy third option.
7. A new semantic Stage 4, voice state, voice score, dynamic per-vacancy voice artifact, deterministic humanizer, or LLM voice judge appear low-value relative to their complexity.
8. Body typography, earned motivation, maximum truthful leverage, and punctuation should be adjudicated individually before their combined interaction is designed.
9. The two pilot runs must be forensically traced end to end before root causes are accepted.
10. The final patch should be pilot-driven, not a pretext for reopening the whole framework.

