# Codex — Final MaxAll Master-Plan Synthesis (from scratch)

Reasoning effort: **MAXIMUM**.

You have full access to the repository at `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`, and to the following supplied materials:

- your own earlier plan (`Initial_ED_plan_codex.md`);
- the earlier Claude plan (`Initial_ED_plan_Claude.md`);
- `CLAUDE_MAXALL_REVIEW_OF_CODEX_PLAN.md`;
- `all_extreme_value_context_from_claude_instance.md`;
- `Neutral_Cross_Plan_Comparison_and_MaxAll_Review_Catalyst.md`;
- the research/review attachments (deep-research reports from both models, the post-research synthesis, the interview-conversion audit).

**This is a from-scratch synthesis, not a revision of your previous plan.** Do not patch `Initial_ED_plan_codex.md`. Start from the problem and the repository and build the final master plan anew. Your previous plan is one input among several and carries no privileged status; neither does Claude's.

Treat every plan and attachment as a **hypothesis**. The live repository and the actual run artifacts decide all factual disputes. Where an attachment and the repo disagree, the repo wins — and say so explicitly when it happens.

---

## 0. Governing rules

### MaxAll
Maximum reasoning depth. Read every supplied document completely. Independently re-verify every material premise you rely on against the actual repo and artifacts — including premises asserted in the Claude review, which are repo-checked but should not be taken on trust. Reason over causal mechanisms rather than labels (density, entropy, AI-feel, individuality, polish, anchoring). Consider multivariate and higher-order interactions. Preserve useful contradictions instead of averaging them. Distinguish evidence, inference, design judgment and uncertainty. Optimize for **actual interview probability**, not for the elegance of the planning documents. Continue until another pass stops yielding material improvement.

### ED-1 — Happy-path optimization, minimal defensive scaffolding
Assume the intended mechanism works. Do **not** design: speculative failure handling, migration, compatibility layers, generalized recovery, security hardening unrelated to the semantic treatment, QA frameworks, new validation subsystems, monitoring, approval gates, schema machinery added merely to make a concept auditable, permanent regression infrastructure, defensive abstractions, observability, or elaborate tests.

Only validation the implementer itself needs to know the happy path runs and produces inspectable artifacts.

**Critical default:** if a semantic objective can be achieved by stronger instructions, better routing, changed selection logic, or existing fields — do that instead of adding schema, state or QA machinery.

Clean, coherent, correctly wired implementation is still required. "Experimental" means low defensive overhead, never sloppy.

### ED-2 — Strong treatment, not incrementalism
Do not choose the smallest safe delta. Ask: *assuming the mechanisms behave as intended, what is the strongest plausibly excellent version we can viably run now?* Explore the S+ frontier. Prefer substantial coordinated changes where the causal mechanism crosses stages. Do not dilute a promising mechanism because a gentler version is easier to defend. If it overshoots, it will be scaled back after observation.

### ED-3 — Extreme implementation productivity
Coherent implementation clusters. Minimal ceremony. No TDD, no test-every-edit, no repeated full-suite runs. Minimal end-of-cluster sanity checks. One integrated happy-path exercise near the end. Then STOP for human evaluation.

### MVP-KISS overlay
**Semantically aggressive, mechanically simple.** The ideal treatment may deeply rewrite objectives, stage instructions, routing, evidence priorities, document roles and language behaviour while adding almost no new machinery.

---

## 1. Scope note

Do not implement in this turn. Produce the planning package only. Do not modify `P0.9/Build/`.

---

## 2. Required process — follow in exactly this conceptual order

### Step 1 — Atomic synthesis and fresh repo revalidation

- Read all supplied materials completely.
- Explicitly reason over **every material element** of both prior plans and the Claude review — not just headline ideas.
- For each idea independently decide: **retain / merge / modify / replace / intensify / simplify / reject**, with a reason. Do not preserve an idea because two documents repeat it; do not reject one because a model disagreed with it.
- Eliminate redundancies; reconcile conflicts explicitly.
- Independently inspect and revalidate the actual repo and the latest artifacts. Reconstruct the Stage 1 → Stage 2 → Stage 3 transformation yourself from `strategy.json` / `draft_package.json` / `final_package.json` / `review.json` across `r20260828-213932-7f13b4`, `r20260902-155301-2120b3` and `r20260902-210926-0d1af3`.
- Search for further optimizations neither prior model found.
- Obey MaxAll + ED + MVP-KISS throughout.
- **Fully integrate the three new output-quality targets** (§3).

Specific claims you must personally re-verify before relying on them, in either direction:

1. Whether `EV:WORK#025` is deleted by Stage 3 in all three runs, and how Stage 1 framed it each time (`evidence_plan[].role`, `application_direction.structure_guidance`, `lifecycle`).
2. Whether `manifest.py::stage_policy_sha256` folds `writing_policy` into every stage's hash, and therefore whether the last two runs are a controlled comparison.
3. What `runtime/jobbsok/cli.py` actually forwards in `personality_distilled`.
4. The exact wording and location of the Stage 3 no-comparator clause and the duplicated independent-thesis instruction.
5. Whether `Build/prompts/*` and `Process/operator_prompts/v2/*` are currently identical.
6. Whether `PERSUASION_CALIBRATION.md` prescribes the `"fortsatt i bruk"` phrasing.
7. Whether the two-case cap in `WRITING_DOCTRINE § Single Backbone` conflicts with any judgment-preservation rule you intend to write.

### Step 2 — Design the master plan's layout before writing it

Produce an explicit layout plan first:

- complete section/chapter/header hierarchy;
- the purpose of every section;
- which decisions and which evidence belong in each;
- priority and depth allocation per section;
- dependencies and ordering between sections;
- how duplication between sections will be prevented;
- how the document stays implementation-ready rather than becoming an essay.

### Step 3 — Adversarially critique and optimize the layout while planning its content

Before filling anything, review your own proposed layout against the content you intend to place in it:

- identify missing, duplicated or misordered sections;
- optimize the information architecture;
- decide the argument/content priority within each section;
- **map every retained mechanism and decision to exactly one authoritative home**;
- ensure the result will be exhaustive but maximally navigable and non-redundant.

Then revise the layout.

### Step 4 — Fill the master plan, MaxAll style

Write the complete master plan containing at least:

- full failure model, causally traced to repo artifacts;
- target-state objective hierarchy;
- the final selected S+ treatment and the tiers rejected above and below it;
- exact stage-by-stage behaviour for Stages 1, 2 and 3;
- policy / voice / personality / routing changes, including every instruction **removed or superseded**;
- multivariate interactions and any new local optima created;
- complete implementation surface (every file and section touched);
- implementation clusters, ordering and boundaries;
- direct step-by-step implementation instructions;
- explicit ED non-goals;
- minimal experimental sanity validation;
- the final happy-path run and the human comparison protocol.

**No unresolved design forks.** The implementing agent must have no substantive design decisions left.

### Step 5 — MaxAll self-review until convergence

Repeatedly review and improve the filled plan for: causal correctness; completeness; internal consistency; unnecessary machinery; insufficient treatment strength; instruction saturation; redundancy; stage conflict; output-quality implications; Janteloven / social-calibration risk; pretension and self-impression risk; argument overload; whether the Stage-3 polish boundary is exact; whether ED has been weakened by safety instincts; and whether any stronger-but-simpler mechanism remains undiscovered.

Continue until a further pass yields no material improvement.

---

## 3. Mandatory output-quality targets — first-class requirements

### 3.1 Kill the "pretentious / self-impressed / this person may be A LOT" signal

Norwegian hiring social calibration matters. The target is **not** self-deprecation and **not** weakening real accomplishments. It is: grounded competence; low ego-display; calm seniority; restrained confidence; specific evidence carrying the status; practical usefulness over intellectual exhibition; employer orientation over autobiographical fascination; socially easy, cooperative, credible professionalism. "Clearly capable and interesting" without "trying hard to seem impressive."

Determine what currently creates the impression and remove it without flattening individuality or truthful persuasive force. Consider whether the cause is lexical, structural, selection-based, rhetorical or multivariate; whether there are too many arguments, too much explicit meta-reasoning, too many abstract distinctions, too much consultant register, too much self-attribution, too much polished causal architecture in too little space; and whether stronger category anchoring plus fewer, deeper examples makes the candidate read as **both more senior and less self-impressed**.

### 3.2 Final Stage-3 language/tone/persona polish sub-pass

After Stage 3 has completed all substantive work — strategy, evidence inclusion, argument selection, CV/letter allocation, claim ceilings, final content and overall structure — perform one final polish sub-pass **inside** Stage 3. Not a new stage.

At that point content and substantive structure are locked. The pass may optimize only realization: wording, syntax, rhythm, transitions, directness, warmth, restraint, social ease, native Bokmål, perceived writer persona, removal of pretentiousness and self-importance, removal of generic LLM lacquer, recruiter-friendliness.

It must not: add or drop arguments or examples; change evidence selection; change factual propositions; change qualifications or lifecycle; alter employer reasoning; change strategic meaning; or re-open document allocation.

Objective: *given that this exact content has already been selected, express it in the language most likely to make a Norwegian hirer think: competent, grounded, useful, interesting, credible and easy to work with.*

Design the strongest clean implementation of this as a Stage-3 internal sub-pass under ED. Decide and state the exact authority boundary. Decide explicitly whether the pass may delete a sentence whose only function is to tell the reader what to conclude, and justify the call.

### 3.3 Bias the letter toward fewer arguments and more depth

Prefer roughly one fewer separate argument/example/experience than the current style — plausibly two fewer where the material supports it — spending the freed capacity on insight, seniority, employer usefulness, prioritization and applicant-fit inference.

**Approximate directional target, not automatically a mechanical quota.** Determine the best semantic mechanism (argument budget, selection hierarchy, letter-role allocation, deletion order, deep-read reward objective, paragraph-function model, or another). The result must read **less crammed but more senior**, not merely shorter or less informative.

---

## 4. Tensions requiring deep adjudication

Use the neutral comparison file as a catalyst; verify and extend it independently.

1. **Category-first legibility vs diagnostic individuality.** How to make the candidate instantly legible as qualified before differentiating, so unusual breadth reads as relevant seniority rather than occupational incoherence or self-display — without producing vacancy-language mimicry.
2. **Lifecycle vs judgment value.** Concept-stage work can be weak outcome evidence and excellent judgment evidence. Make the distinction first-class in model reasoning while staying ED/MVP-KISS. Do not assume a schema field is needed; do not assume existing fields suffice. Decide from the repo and from observed model behaviour.
3. **Personality routing.** What downstream writers actually need for selected personality guidance to become an expression target rather than a set of brakes. Adjudicate which fields flow. Protect the boundary: personality/voice must never become factual authority.
4. **Constraint saturation and policy routing.** Whether the system has accumulated too many overlapping instructions. Inspect Stage 2's exposure specifically. Decide whether the redesign should **subtract and consolidate at least as aggressively as it adds** — a correct new rule that becomes the 101st low-salience bullet may be worse than replacing twenty old bullets with one dominant objective.
5. **Stage 3 reconstruction vs signal preservation.** Find the optimum between genuine independent authorship, exploiting upstream discovery as option value, avoiding regression to modal professional prose, and avoiding a hidden strategy-compliance regime. Question whether preservation needs any explicit machinery once ranking and replacement incentives are corrected.
6. **CV/letter capacity and document roles.** Treat attention and space as scarce. Determine whether duplicate case narration displaces judgment, insight, fit reasoning or seniority signal. Prefer functional allocation over quotas unless a bounded argument budget is clearly stronger.
7. **Unmet material requirements.** How to positively engage real minimum/gap issues without defensive "I lack X" prose, without overclaiming, and preferably without new schema machinery.

---

## 5. Search beyond both plans

Do not limit yourself to reconciling known proposals. Actively hunt for: instructions individually sensible but collectively producing the wrong objective; upstream signal that repeatedly disappears downstream; generic application-writing priors surviving despite policy; places where readability is bought by deleting texture instead of improving prioritization; evidence repeated rather than interpreted; weak occupational anchoring; excess abstraction or nominalization; over-explicit self-positioning; missing social/reader calibration; systematic argument-shape convergence across vacancies; bad interaction between voice and category clarity; policy duplication; and opportunities to make the treatment **more extreme semantically while simpler mechanically**.

Ask repeatedly: *assuming the happy path works exactly as intended, what change would most improve the actual employer response?*

---

## 6. Required outputs

### 6.1 The final master experimental optimization plan
A complete `.md` artifact written to an appropriate planning directory outside `P0.9/Build/`. Also surface the decisive structure and conclusions in chat.

### 6.2 Iteration TL;DR
A short summary of every major internal step: synthesis, layout v1, layout critique, revised layout, fill, self-review changes, convergence.

### 6.3 `all_extreme_value_context_from_codex_instance.md`
Short, dense, non-bloated. Only high-value context the future implementing Claude instance would otherwise miss. Extreme signal-to-token ratio. No narrative history, no generic advice, no restatement of the master plan.

### 6.4 The fresh-Claude `/Plan` prompt
A complete, copy-paste-ready, self-contained initialization prompt for a **fresh Claude Code Opus Max instance with full project-folder access**. It must instruct that instance to:

- produce the complete, uncompromising implementation/execution plan for the final master design;
- verify the current repo anchors itself before planning;
- remain ED + MVP-KISS throughout;
- **not redesign the approved target** — the design is settled; it plans execution.

### 6.5 The queued `/GOAL` prompt
A complete, copy-paste-ready prompt to send to that **same** Claude implementation instance after its first implementation pass. It must strongly require Claude to:

- complete **every** approved implementation item rather than reporting 80–90% completion;
- revisit all central semantic instruction surfaces — stage instructions, writing policy, voice/personality guidance, operator prompts, context/handoff text — and make them internally optimized **as one system** wherever the final plan calls for it;
- preserve ED: no production-hardening detour, no speculative QA, no new scaffolding unless intrinsic to the approved happy-path mechanism;
- preserve MVP-KISS: aggressive semantic treatment, simplest viable mechanics;
- work in large coherent implementation clusters;
- batch only minimal validation;
- continue until the complete experimental happy path exists and is ready for the user's manual test;
- **STOP** before inventing post-experiment hardening or scale-back.

Both prompts must be self-contained enough for a fresh instance with no conversation history.

---

## 7. Final discipline check before returning

- Did you genuinely start from scratch rather than patching your previous plan?
- Did you re-verify the repo claims yourself, including the ones the Claude review says it verified?
- Did you challenge the Claude review as hard as your own prior plan?
- Did you resolve the two-case-cap / judgment-preservation conflict explicitly, one way or the other?
- Did you decide the schema question on repo evidence rather than on either plan's preference?
- Did you treat instruction **subtraction** as part of the treatment?
- Did ED survive, or did safety instincts reintroduce schemas, validators, tests or gates?
- Did you fully integrate the pretension target, the polish sub-pass and the fewer-arguments target — as designed mechanisms, not mentions?
- Is every mechanism in exactly one authoritative home?
- Are there any unresolved design decisions left for the implementer?
- Is this plausibly one of the strongest treatments we could viably test now?

If any answer is unsatisfactory, improve the package before returning.
