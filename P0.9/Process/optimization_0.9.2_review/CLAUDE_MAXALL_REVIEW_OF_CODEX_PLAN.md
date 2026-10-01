# MaxAll Review of the Codex Experimental Optimization Plan

**Status:** Review material for Codex's final from-scratch master-plan synthesis. Not an implementation plan.
**Authority:** The live repository decides factual disputes. Both plans are hypotheses.
**Date:** 2026-09-05. Repo state: `P0.9/Build` control files match those frozen in `r20260902-210926-0d1af3`.

---

## 0. Executive position

The Codex plan is **causally sound at the level it operates on, and operating one level too high.** Its objective hierarchy (category-first diagnostic individuality), its rejection of quotas/ledgers/validators, and its "substitution loss, not compression" diagnosis are all correct and should survive into the master plan largely intact.

But its failure model stops at *Stage 3 has a bad substitution incentive*. The repository shows something stricter and more useful: **the deletion of the judgment evidence is triple-determined by the architecture, and every stage behaved correctly when it happened.** Fixing Stage 3's incentive alone will not reliably fix it, because two of the three determinants sit upstream of Stage 3 and one of them is a doctrine Codex proposes to keep.

My own prior plan was wrong in a different way — it blamed lifecycle ranking alone, proposed a schema field that the repo shows would not have helped, and rested on an A/B framing that Codex correctly refutes. I retract all three below.

The strongest available treatment is neither plan's. It is a **single structural move — fuse judgment into the carrying case rather than letting it compete as a third case** — which simultaneously resolves the information loss, the user's fewer-arguments target, and the pretension target, and which requires no schema, no ledger, no validator and no new machinery. §7 develops it.

---

## 1. Repo-verified premises

Everything below was checked directly against artifacts, not against any attachment's description.

| # | Premise | Verdict | Evidence |
|---|---|---|---|
| P1 | `EV:WORK#025` (the proxy-model judgment) was written into the letter by Stage 2 and deleted by Stage 3 in **all three runs** | **Confirmed** | `used_evidence_refs` deltas, `r20260828`, `r20260902-155301`, `r20260902-210926` |
| P2 | It is the only `lifecycle: CONCEPT` item in the Avinor evidence plan, in every run | **Confirmed** | `strategy.json` `evidence_plan[].lifecycle` |
| P3 | Stage 1 framed it as `"Støttebevis…"` and told the writer to use it **`kort som støtte`** (0828/155301) / **`ikke som et tredje hovedcase`** (210926) — in every run | **Confirmed** | `evidence_plan[].role`, `application_direction.structure_guidance` |
| P4 | Codex: the voice-file change invalidated **every** stage, so the runs are not a controlled voice-only test | **Confirmed — Codex is right, I was wrong** | `manifest.py::stage_policy_sha256` includes `writing_policy` for all stages; Stage 1 headline, thesis, `writer_guidance`, evidence ordering and facet selection all differ 155301→210926 (Avinor facets `PF-19,01,11` → `PF-01,08,19`) |
| P5 | The new voice policy **improved** evidence retention | **Confirmed** | Avinor Stage 3 drops: 3-of-9 (0828, 155301) → 1-of-10 (210926); final refs 7 → 11 |
| P6 | `cli.py` distils personality to label + two restrictions, discarding `vacancy_relevance`, `intended_employer_interpretation`, `misread_risk`, `evidence_refs` | **Confirmed** | `runtime/jobbsok/cli.py:1043-1049` |
| P7 | Stage 3 is told `"Nobody will compare your final against the strategy… There is no comparator and there will never be one."` | **Confirmed** | `policy/stages/stage3_final_writer_review.md:85-86` |
| P8 | The "form your own thesis before reading upstream" instruction is **duplicated inside the Stage 3 file** (lines 36-40 and 55-58) | **Confirmed** | Same file. Codex is right that it is duplicated; it is duplicated within the stage instruction, not between prompt and instruction — `STAGE3_PROMPT.md` carries no such language |
| P9 | 100 policy bullets are routed identically to all three stages; Stage 2 alone has no named-section routing table | **Confirmed** | `WRITING_DOCTRINE` 59 + `PERSUASION_CALIBRATION` 19 + `FORFATTERSTEMME` 22; `cli.py` passes `writing_policy` as a flat list to every stage; Stage 1 and Stage 3 instructions carry section tables, Stage 2's does not |
| P10 | The T15 test asserts `set(facet) <= {3 keys}`, so Codex's `cli.py` expansion **will** break it | **Confirmed — Codex is right to schedule the edit** | `runtime/tests/test_t13_t15_merge_leakage_personality.py:355` |
| P11 | Codex: `Process/operator_prompts/v2` is "historical… intentionally not synchronized" | **Refuted** | All three files are **byte-identical** to `Build/prompts`. Editing only `Build/prompts` desynchronizes them for the first time |
| P12 | `"rapportert i bruk"` → `"fortsatt i bruk"` is claim drift | **Refuted (my earlier audit was wrong)** | `PERSUASION_CALIBRATION.md:42-49` gives that exact pattern as `riktig`. It is prescribed, operator-approved calibration |
| P13 | `additionalProperties: false` on every artifact schema; `semantic_fields()` derives from schema properties | **Confirmed** | `schemas/*.schema.json`, `artifacts.py:286-290`. A new field is declarable and flows automatically — but see §4 for why that does not make it worth adding |

---

## 2. Three corrections to my own prior plan

Stated first, because the review's credibility depends on symmetry of scrutiny.

**2.1 My "controlled A/B" framing was wrong.** I asserted that `r20260902-210926` differed from its predecessor by exactly one frozen input and was therefore a clean voice-policy A/B. P4 refutes this: `stage_policy_sha256` folds `writing_policy` into every stage's handoff hash, so Stage 1 was fully regenerated. The strategies differ in thesis, headline, evidence ordering and facet selection. Codex caught this; I did not.

**But the correction strengthens the finding it was attached to.** P1 now holds across two voice policies, three independently regenerated Stage 1 strategies, three different facet selections and three different Stage 2 drafts. An invariant that survives a complete upstream re-roll is far stronger evidence of a structural cause than one observed under a single controlled variable. Codex's methodological correction should be adopted *and* the conclusion it corrects should be promoted, not demoted.

**2.2 My `decision_signal` schema field should be withdrawn.** The user approved it; the repo says it would not have worked. Stage 1 already wrote the decision signal in plain prose, in the exact field Codex proposes to rely on: *"kandidaten **avviste falsk presisjon** og utformet en transparent, justerbar proxyarkitektur"* (210926), *"**erstattet falsk presisjon** med en transparent, vektet proxymodell med synlige antakelser og kontrollpunkter"* (0828/155301). The information was present, explicit, and unmistakable. Stage 3 deleted it anyway, three times.

A field that re-encodes information the model already had, in a form the model already read, does not change behaviour. **The problem was never representational.** Codex's "use existing fields" instinct is correct on this point and my schema proposal should be rejected — by me. What is missing is not a slot; it is a *ranking and structural-position rule*. §7.

**2.3 My `krav_framing` enum should also be withdrawn, but the objective retained.** Same argument, plus the neutral catalyst's §11 question is decisive: `importance: MINIMUM` + `relation: GAP` + `objections[].reframe` + `honesty_note` already express everything the enum would. Both runs already classified R02/R04 correctly as MINIMUM/GAP. The system *knows*. It simply has no instruction about what to *do*. That is an instruction gap, not a representation gap. Keep the behavioural rule; drop the enum.

---

## 3. What the Codex plan gets right and should keep

These are load-bearing and I would fight to preserve them.

1. **Category-first ordering.** Objective #2 (occupational/qualification legibility before differentiation) is the single best idea in either plan. It is supported by the strongest counter-literature in both deep-research reports (Zuckerman typecasting; Leung incremental-progression), it directly addresses the candidate's real exposure as an economist→analysis→methodology→tooling spanner, and — non-obviously — it is also the strongest available *anti-pretension* mechanism. §6.1.
2. **Refusal of the ledger/quota/validator family.** Correct, and correct for the right reason. Both deep-research reports independently conclude that self-reported discard logs do not work (IBM: explanations *eroded* instruction-following), and ED-1 forbids the external verifier that would replace them. Codex's resolution — fix the incentive instead — is the only exit from that deadlock, and it is the same conclusion I reached independently.
3. **"Substitution loss, not compression."** The word counts prove it: the deleted Avinor proxy paragraph was ~75 words; its replacement was 57 words of modal adviser prose. Nothing was saved. Codex names this precisely.
4. **Rejecting Lix/word/numeral/paragraph targets.** I used a Lix comparison in my own verification section. Codex is right that it invites a bad local optimum — a scalar that can be improved by deleting exactly the technical vocabulary that carries credibility. Drop it as a target; keep it only as a post-hoc diagnostic the human may glance at.
5. **No public/private regime branch.** Both deep-research reports push hard for `legal_selection_regime` branching. Codex declines, and is right for this experiment: the branch depends on a fact the user can obtain with one phone call (both reports rank that call as highest-value), and hard-coding a taxonomy on two observed vacancies would fit noise. Defer, don't reject.
6. **Cluster/verification architecture.** The five-cluster shape, the child-run via `branch`, the refusal to debug the Word-COM PDF degradation, and forced-preference human comparison over aggregate scoring are all well-judged and ED-compliant.

---

## 4. Where the Codex plan is incomplete, too weak, or internally conflicting

### 4.1 The failure model stops one level short — the deletion is triple-determined

Codex's model (its §"Reconstructed failure model", steps 3–7) attributes the loss to Stage 3 forming its thesis early, receiving broad suppression permission, and substituting abstractions under smoothness pressure. All true. But the repo shows three *independent, individually sufficient* reasons the judgment evidence dies, and Codex's plan only addresses one:

| Determinant | Where it lives | Codex's plan addresses it? |
|---|---|---|
| **D1 — Case-count cap.** `WRITING_DOCTRINE § Single Backbone`: "normalt to hovedbevis; høyst én kontrollert differensiator… Bruk størstedelen av søknadens argumentkapasitet på én eller to avgjørende beslutningstester." | Writing doctrine | **No** — Codex revises `Single Backbone` for ranking dimensions but keeps the two-case cap. The judgment evidence is a *third* case by construction. |
| **D2 — Subordinate role framing.** Stage 1 wrote `"Støttebevis…"` and `structure_guidance` said `kort som støtte` / `ikke som et tredje hovedcase` — in all three runs. | Stage 1 output, caused by D1 | Partially — Codex adds ranking dimensions to Stage 1 but does not stop it from classifying judgment as support. |
| **D3 — Lifecycle as value.** `lifecycle: CONCEPT` is the weakest rank on the only maturity ladder in the system. Stage 3's own review says it cut the design *"fordi innføringsstatusen er svakere."* | Doctrine + schema semantics | Partially — Codex adds `JUDGMENT_EVIDENCE` to `APPROVED_STRONG`, which helps, but does not state that lifecycle bounds phrasing rather than ranking selection. |

Under D1+D2+D3, Stage 3 deleting `#025` is not a defect. **It is compliance.** Any plan that leaves the two-case cap intact while asking Stage 3 to preserve judgment is issuing two conflicting instructions and will get the stronger, older, more-repeated one.

This is the most important gap in the Codex plan.

### 4.2 The deletion hierarchy is necessary but not sufficient

Codex's ordered deletion list (ad restatement → interchangeable bridges → CV/letter duplication → low-diagnostic detail → only then a diagnostic proposition) is a genuine improvement and should be kept. But it governs *what Stage 3 cuts when it needs space*. It does not govern *what Stage 2 built*, and the repo shows the problem is upstream of the cut: Stage 2 produced a 4-case letter against a 2-case doctrine. Stage 3 was handed an over-full letter and a rule saying which two cases matter. The hierarchy fires too late.

Add an allocation rule at Stage 2 — or better, remove the need for one via §7.

### 4.3 Stage 2's constraint exposure is identified nowhere in the Codex plan

P9 is, I think, the largest un-adopted finding available. Stage 2 receives all 100 policy bullets with no routing table, while Stages 1 and 3 both have one. Under the constraint-saturation evidence both deep-research reports cite (FollowBench: consecutive satisfaction ~3; IF rate 0.88→0.66 from 2→10 constraints; soft-conflict scores 0.24→2.03), Stage 2 is the stage operating furthest into the degraded regime — and it is the stage that writes the first full realization.

Codex's plan edits Stage 2's instruction to *add* the two-layer sequence, positive gap handling and document-role allocation. That is three more constraints onto the most saturated stage. **The neutral catalyst's §6 question is the right one and Codex does not answer it:** a correct new rule that becomes the 101st low-salience bullet may be worse than replacing twenty old bullets with one dominant objective. The master plan should subtract at least as aggressively as it adds, and Stage 2 is where subtraction pays most.

### 4.4 Voice `Rangorden` change is the one place Codex may be too aggressive

Codex proposes: *"Replace the blanket prohibition on voice affecting evidence choice with the narrower rule that voice cannot originate evidence but can influence salience among eligible propositions,"* and *"Remove the unconditional 'readability beats visible personality' formulation."*

I understand the motive and I think the first half is defensible. But this is the single change with the clearest path to a *new* failure mode, and it interacts badly with target 5.1. `FORFATTERSTEMME § Anti-karikatur` currently ends with "Arbeidsgiverens overtalelse og lesbarhet slår alltid synlig personlighet." That clause is the only hard brake on voice-driven self-display in the entire corpus. Removing it while simultaneously telling voice it may influence salience gives the model licence to foreground what *sounds* characteristic. The observed Avinor letter is already over-indexed on self-framing (§6.1: 7 meta markers, incl. "Det tydeligste gjennomføringsbeviset **mitt**"). Loosening the brake in that direction is the wrong-signed change for this candidate's actual failure mode.

**Recommendation:** keep the salience clarification; replace the removed clause with a *directional* one rather than deleting it — e.g. "employer inference beats visible personality" — so the ordering survives while the anti-diagnostic reading of it does not. Codex's proposed replacement text ("diagnostic employer value beats personality display") already says this; the plan should be explicit that the brake is *reworded, not removed*.

### 4.5 Two smaller factual/scope items

- **P11:** the plan's assumption that `Process/operator_prompts/v2` is desynchronized provenance material is false; the files are byte-identical today. Either mirror the edits or state explicitly that divergence is intended, but do not assert a divergence that does not yet exist.
- **Codex edits `make_fixtures.py` + T15.** Correct and necessary (P10) — an existing test that would otherwise fail is happy-path wiring, not new scaffolding. This is ED-compliant and my plan wrongly omitted it. Adopt Codex's item verbatim.

---

## 5. Items from my plan: integrate, transform, or leave rejected

| Item | Disposition | Reason |
|---|---|---|
| **`cli.py` personality routing repair** | **Integrate — both plans have it; it is the highest leverage-per-line change available** | P6. Codex passes 6 fields; I proposed also passing `evidence_refs`. **Adjudication: Codex's 6 fields, not mine.** Forwarding `evidence_refs` couples personality to evidence selection and risks making the facet a second evidence authority (catalyst §5). `vacancy_relevance` + `intended_employer_interpretation` + `misread_risk` convert the packet from brakes to target without that coupling. Codex wins this one. |
| **Delete the "no comparator ever" clause** | **Integrate, and strengthen** | P7. Codex softens it to "the neutral architectural fact that no strategy-compliance comparator exists." Good. But the sentence should not merely be neutralized — the same edit should say what upstream *is*: discovered option value. Deleting a claim leaves a vacuum; replacing it sets the frame. |
| **De-duplicate the doubled "independent thesis" instruction** | **Integrate** | P8. Codex has this; it is correct and cheap. |
| **Stage 2 named-section routing table** | **Integrate — Codex lacks it entirely** | §4.3. This is my plan's strongest unadopted item. |
| **Corpus subtraction / dedupe of repeated invariants** | **Integrate and intensify** | §4.3, catalyst §6, and the post-research synthesis §8 attractor-risk argument. Neither plan treats subtraction as *part of the treatment*. It should be. |
| **CV/letter capacity allocation** | **Transform** | My "at least one letter paragraph must carry judgment the CV cannot" hard-codes the current 4-paragraph shape and is a quota in disguise — the catalyst (§8) is right to challenge it. Replace with the §7 fusion rule, which achieves the effect without a count. |
| **`decision_signal` schema field** | **Rejected — by me** | §2.2. |
| **`krav_framing` schema enum** | **Rejected — by me; behavioural rule retained** | §2.3. |
| **Lix in the verification section** | **Rejected — by me** | §3.4. Codex is right. |
| **Krav-coverage behaviour** | **Integrate as instruction only** | The user selected "include a krav-coverage rule." Implement it as Stage 1 classification in existing `note`/`objections` fields + a Stage 3 positive-engagement rule. No enum. §6.3. |

---

## 6. The three new output-quality targets

### 6.1 Target 5.1 — killing the "this person may be A LOT" signal

**Measured, not asserted.** In the current Avinor final letter (309 words, 6 paragraphs):

- **7 self-framing / meta-reasoning markers**: `"Det tydeligste gjennomføringsbeviset mitt"`, `"på metodenivå"`, `"har lært meg at"`, `"Det er denne erfaringen"`, `"Erfaringen viste hvordan"`, `"arbeidsformen"`, `"tydeligste"`. Huseierne's letter has 2. The Avinor letter is measurably the more self-impressed of the two.
- **4 body paragraphs of near-identical mass** (47–68 words), each **4 sentences**, each following `claim → mechanism → outcome → lesson`.
- First-person density 3.6% — *not* high. **Self-importance here is not caused by "I".**

**The diagnosis is structural and rhetorical, not lexical.** Three mechanisms, in descending order of impact:

1. **The moral-of-the-story sentence.** Every single body paragraph closes by telling the reader what to conclude: *"Arbeidet krevde at forbedringstakten ble styrt sammen med kompatibilitet…"*, *"Erfaringen viste hvordan en felles modell kan…"*, *"Slik kan jeg bidra i samspillet mellom Avinors ledere…"*. The candidate never lets a fact stand on its own. Four consecutive distilled lessons is what produces *"is this person going to be a lot?"* — it reads as someone who cannot stop explaining. It is also the least Jante-compatible move available, because it presumes the reader needs interpretation. **Removing or thinning the lesson sentence is the single highest-value tone intervention, and it simultaneously shortens the letter, reduces AI-modal symmetry, and raises perceived seniority — senior people state the fact and trust the reader.**
2. **Self-grading of one's own portfolio.** `"Det tydeligste gjennomføringsbeviset mitt er…"` is the candidate ranking his own evidence for the employer. This is the most self-impressed phrase in either letter. The fix is not humility — it is simply *stating the case*: "Jeg moderniserte et virksomhetskritisk budsjetteringsverktøy…". The evidence carries the ranking.
3. **Announced abstraction level.** `"Jeg har også arbeidet med verdistyring **på metodenivå**"` tells the reader the work was meta. That is intellectual self-positioning. The work itself already proves it.

**Non-obvious interaction — the strongest anti-pretension lever is category anchoring, not tone softening.** The catalyst (§4, §9) asks whether stronger category anchoring could permit *more* individuality with *less* perceived pretension. The repo supports yes, and the mechanism is specific: an unusual detail reads as *self-display* when the reader cannot see its job function, and as *relevant depth* when they can. Four separate impressive-sounding cases with no established category produce "look at everything I've done." The same four facts, arriving *after* the reader has classified the candidate, read as evidence for a claim already made. **Category-first is therefore doing double duty: it is Codex's objective #2 and it is the primary treatment for 5.1.** Codex has the mechanism but has not connected it to the pretension target; the master plan should.

**Explicitly do not:** add hedges, weaken work verbs, add self-deprecation, or reduce first-person usage. All four would damage `Rolig faglig tyngde` and the GPT deep-research finding that factual ownership ("jeg utviklet", "jeg valgte") is both more informative and *less* culturally risky than adjectival self-description. The problem is the interpreting, not the claiming.

### 6.2 Target 5.2 — the Stage-3 final polish sub-pass

I think this mechanism is **stronger than the catalyst credits it**, for a reason neither plan states: it changes what the *substantive* pass is allowed to optimize for.

Today Stage 3 is doing substance and register simultaneously under one objective. That is precisely the condition under which "reads better" silently outranks "says more" — the two objectives are fungible inside one generation. Splitting them means the substantive pass **no longer has to buy smoothness with signal**, because a later pass will supply smoothness for free. This is the same logic as the deletion hierarchy, applied to the generation order rather than the cut order, and it is the cheapest available protection against substitution loss.

**Design, under ED (no new stage, no new artifact, no new field):**

- **Placement:** the final section of the Stage 3 instruction, framed as the last thing done before writing the return — not a separate prompt, not a separate model call, not a schema surface.
- **Precondition, stated as a lock:** "The package's content is now fixed. Every proposition, example, evidence choice, claim ceiling, document allocation and argument order in front of you is final."
- **Authority — positive list only** (per the compliance-gap evidence: substitution is easier than suppression): wording, syntax, sentence rhythm, paragraph transitions, directness, warmth, restraint, social ease, native Bokmål idiom, and the removal of self-framing, lesson-drawing, announced abstraction and modal-LLM lacquer.
- **Boundary — the one hard prohibition worth spending:** "If a change would alter what the employer learns, it is out of scope." That single sentence is a better boundary than an enumerated forbidden-list, because it is checkable by the model against its own edit and does not require it to hold seven prohibitions in working memory.
- **Objective sentence** (this is the whole mechanism, and it should be quoted close to verbatim in the instruction): *"Given that this content is already chosen, express it so a Norwegian hiring manager thinks: kompetent, jordnær, nyttig, troverdig og grei å jobbe med — not imponerende, intens eller selvbevisst."*
- **Explicit permission to shorten:** the pass may delete a sentence whose only function was to tell the reader what to conclude. That is not content — it is interpretation of content — and naming this as *in scope* is what makes the pass able to fix 6.1.

The last bullet is the subtle one, and I would put it in front of Codex as a genuine design question rather than a settled call: it is the one place where the boundary is soft, because a lesson sentence sits exactly on the line between realization and meaning. My position is that it belongs in scope, because the observed lesson sentences carry no evidence — they restate the inference the evidence already licenses — and because leaving them out of scope would neuter the sub-pass against the primary pretension mechanism. But it must be worded so it licenses removing *redundant interpretation*, not removing *employer-relevance reasoning*.

### 6.3 Target 5.3 — fewer arguments, more depth

**Do not implement as a count.** Both deep-research reports converge on the Presenter's Paradox (evaluators average rather than add; adding moderately favourable material to strongly favourable material lowers the overall judgment across seven studies) — which is the real reason fewer-and-deeper wins, and it is a *ranking* argument, not a *counting* argument. A quota of "three body paragraphs" would be satisfied by merging the two weakest.

**The correct mechanism is §7's fusion rule**, which produces the reduction as a consequence rather than a target: when judgment rides inside a carrying case, four thin cases become two deep ones, and the freed capacity goes to interpretation and employer usefulness rather than to a further example. The reduction is then *caused by* the depth increase rather than traded against it — which is exactly the "less crammed but more senior, not simply shorter" outcome the user specified.

Secondary support, both cheap: the deletion hierarchy already ranks duplication and interchangeable bridges above evidence, and the Presenter's-Paradox logic should be stated once in `WRITING_DOCTRINE § Single Backbone` as the *reason* for the case cap — currently the cap is asserted without a rationale, which is why Stage 2 overrides it.

---

## 7. The synthesis neither plan contains: fuse judgment into the carrying case

**The problem restated precisely.** The system has exactly one way to carry a professional judgment: as its own case, competing for a slot in a two-slot backbone. It therefore always ranks third, is always labelled `Støttebevis`, always carries the weakest lifecycle, and is always the marginal cut. Three runs, three deletions, three different strategies.

**The move.** Stop treating judgment as an *exhibit* and start treating it as the *interpretation layer of a carrying case*.

Concretely — the current Avinor structure:

> p1: budget modernization (case 1, IN_USE) → lesson
> p2: benefits framework (case 2, IN_USE) → lesson
> p3: current-role process description (generic, replaced the deleted judgment)
> p4: Avinor relevance → lesson

The fused structure:

> p1: budget modernization, **including the judgment made while doing it** — why the improvement pace was subordinated to compatibility and operational risk, as a decision he took
> p2: benefits framework, **including why it lasted** — because expectations were made testable and assumptions visible rather than given more precision than the data carried
> p3: Avinor relevance + contribution

Two cases, not four. The judgment is now:
- **structurally unremovable** — cutting it guts the main case's explanation;
- **lifecycle-immune** — it rides on `IN_USE` evidence, so D3 cannot fire;
- **not `Støttebevis`** — it is part of the `hovedbevis`, so D2 cannot fire;
- **not a third case** — so D1 cannot fire.

All three determinants are disarmed by one structural change, with **no schema, no ledger, no validator, no preservation rule and no new instruction load.**

**And it satisfies the other two targets simultaneously:**
- 5.3: four arguments → two, with the freed capacity spent on depth per case. Exactly the specified direction, achieved without a quota.
- 5.1: two lesson-sentences disappear because the lesson has become the case's own explanation rather than an appended moral; the symmetric 4×4-sentence rhythm breaks; and the candidate stops grading his own portfolio because there are only two items to grade.

**Note the honest caveat.** The 0828 Stage 2 draft *co-located* the judgment with the benefits case in one paragraph and Stage 3 still cut it. That is not a counter-example — inspect the text: it was appended as a distinct second exhibit (*"Når et annet prosjekt manglet tilstrekkelig datagrunnlag…"*), a separate project with its own subject. Co-location is not fusion. Fusion requires the judgment to be **about the carrying case itself** — the reason *that* work succeeded or was constrained. This distinction is the whole mechanism and the master plan must state it explicitly, because "put them in the same paragraph" is the failure mode that already happened.

**Where it lives:**
- `WRITING_DOCTRINE § Single Backbone` / `Vinklingskjeden`: a carrying case is narrated with the decision that shaped it. Judgment is not a separate case type.
- Stage 1: stop emitting `Støttebevis`-framed judgment items and `kort som støtte` guidance; instead bind the judgment to the carrying evidence it explains, inside that item's `role`.
- Stage 3: the deletion hierarchy then needs no special judgment clause, because judgment is no longer separately deletable.

This is the aggressive, mechanically simple treatment ED-2 and MVP-KISS jointly ask for.

---

## 8. Multivariate interactions worth designing around

1. **Category anchoring × individuality × pretension.** Positive three-way. Anchoring first makes unusual detail read as relevant depth rather than display (§6.1). Codex has the first two connected; the third is free and unclaimed.
2. **Fusion × case count × capacity × duplication.** Fusing judgment into carrying cases reduces case count, which frees letter capacity, which removes the pressure that caused CV/letter duplication in the first place. One change, four objectives. This is why §7 dominates a capacity quota.
3. **Voice-brake removal × pretension target.** Negative. §4.4 — Codex's `Anti-karikatur` loosening is the one proposed change that pushes *toward* the "A LOT" signal. Reword rather than remove.
4. **Adding Stage 2 constraints × Stage 2 saturation.** Negative. §4.3 — Codex adds three obligations to the most saturated, least-routed stage. Net effect may be negative even if each rule is correct.
5. **Polish sub-pass × substantive pass.** Positive, and under-exploited. §6.2 — the sub-pass should be used as *permission for the substantive pass to be less smooth*, not merely as a finishing step. The master plan should say this explicitly in the Stage 3 instruction, or the substantive pass will keep trading signal for smoothness out of habit.
6. **Fusion × the two-case cap.** Watch for a new local optimum: if judgment must ride inside a carrying case and there are only two carrying cases, a genuinely important third judgment has nowhere to go. Acceptable for this experiment — the letter should carry fewer arguments anyway — but the master plan should name it as a known, deliberate constraint rather than discover it in output.

---

## 9. ED / MVP-KISS scorecard

| Proposal | Machinery cost | Semantic aggression | Verdict |
|---|---|---|---|
| §7 fusion rule | Zero | Very high | **Adopt — best ratio in either plan** |
| Category-first objective (Codex) | Zero | High | Adopt |
| `cli.py` 6-field routing (Codex) | ~6 lines + 1 test edit | High | Adopt |
| Deletion hierarchy (Codex) | Zero | Medium | Adopt |
| Polish sub-pass (user 5.2) | Zero | High | Adopt |
| Stage 2 routing table + corpus subtraction (mine) | Zero (net negative tokens) | Medium-high | Adopt |
| Krav engagement as instruction | Zero | Medium | Adopt |
| `decision_signal` field (mine) | Schema + spec revision | Low — info already present | **Reject** |
| `krav_framing` enum (mine) | Schema | Low | **Reject** |
| Proposition ledger / survival check (both research reports) | High | Medium | Reject under ED-1 |
| Regime branching (both research reports) | Medium | Medium | Defer — resolve by phone call first |

Note the pattern: **every item worth adopting costs zero machinery.** That is not a coincidence; it is what the repo evidence implies, because every failure traced back to an instruction or a structural position, never to a missing representation.

---

## 10. What I would challenge Codex to rethink before writing the final master plan

1. **You kept the two-case cap while asking Stage 3 to preserve judgment.** Those instructions conflict, and the repo shows which one wins — three times. Either raise the cap, or make judgment ride inside a case (§7). Do not ship both rules unreconciled.
2. **Your fix is entirely downstream of where the classification happens.** Stage 1 labelled the judgment `Støttebevis` and said `kort som støtte` in every run, including the run whose strategy you praise. Stage 3 obeyed. Adding ranking dimensions to Stage 1 does not stop it emitting a subordinate role; changing what a judgment *is* structurally does.
3. **You add three constraints to Stage 2 and subtract none, from the only stage with no routing table.** Justify this against the constraint-saturation evidence you cite elsewhere, or subtract. Consider whether Stage 2's whole policy exposure should be a named-section table plus one dominant objective.
4. **Your `Anti-karikatur` loosening is the wrong sign for this candidate.** The measured problem is 7 self-framing markers and a self-graded portfolio, not insufficient personality. Reword the brake; do not remove it.
5. **You assert `Process/operator_prompts/v2` is unsynchronized. It is byte-identical today.** Decide deliberately whether to mirror or diverge.
6. **Say what the polish sub-pass licenses upstream.** If it is only a finishing pass, it is worth little. If it is permission for the substantive pass to stop buying smoothness with signal, it is worth a great deal — but only if you write that down where the substantive pass reads it.

---

## 11. Strongest plausible synthesis if we ignore implementation risk and optimize the happy path

One objective, four coordinated edits, zero new machinery.

**Objective (replaces the current implicit one, stated once, at the top of `WRITING_DOCTRINE`):**

> Make the reader classify the candidate as a qualified member of this role's category within twenty seconds; then, in the same document, give that classified candidate two pieces of work narrated deeply enough that the decisions inside them are visible. Truth and claim ceilings bound everything. Where capacity is scarce, spend it on making one case deeper rather than adding another.

**Edit 1 — Doctrine (`WRITING_DOCTRINE`, `PERSUASION_CALIBRATION`).** Category anchoring before differentiation. Judgment is narrated inside a carrying case, never as a competing case (§7). Lifecycle bounds phrasing, not selection value. State the Presenter's-Paradox rationale for the case cap so downstream stages stop overriding it. Delete the invariants duplicated across all three writing files. Reword — do not remove — the personality brake as "employer inference beats personality display."

**Edit 2 — Stage 1.** Category anchor first; bind judgment to the carrying evidence it explains rather than emitting `Støttebevis` items; populate the facet interpretation fields concretely; classify each MINIMUM as bar-or-wish in the existing `note`; zero facets stays valid.

**Edit 3 — Stage 2.** Named-section routing table (its first). Two-layer realization. Positive-transfer gap handling. Net constraint count should *fall*.

**Edit 4 — Stage 3.** Delete the no-comparator clause and replace it with upstream-as-option-value; de-duplicate the doubled thesis instruction; adopt the deletion hierarchy; positively engage unmet MINIMUMs without defensive prose; then the **final polish sub-pass** (§6.2) with the content-lock, the positive authority list, the single boundary sentence, and explicit licence to delete redundant interpretation.

**Plus:** `cli.py` six-field personality routing + the one T15 assertion edit.

**Predicted output shape:** Avinor letter of roughly two deep body paragraphs plus opening and close; no `"det tydeligste beviset mitt"`; no paragraph-terminal morals; the proxy-model judgment present *inside* the benefits or budget case rather than as a third exhibit; CV top zone naming the category and the employer; Huseierne engaging the objectives-and-measures requirement in its own vocabulary without naming the gap.

If that package does not read as more senior, more grounded and less effortful than `r20260902-210926`, the hypothesis is wrong in a way worth knowing — which is the point of running it.
