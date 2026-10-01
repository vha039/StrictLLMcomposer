# Extreme-value context handoff — Claude instance → Codex

Compressed. Repo-verified unless marked. No narrative.

## Repo facts that change the design

- **`EV:WORK#025` (proxy-model judgment) deleted by Stage 3 in 3/3 runs.** `r20260828`, `r20260902-155301`, `r20260902-210926`. Only `lifecycle: CONCEPT` item in the Avinor plan. Survived two voice policies and three independently regenerated Stage 1 strategies. Structural, not stochastic.
- **The deletion is triple-determined. Every stage complied.**
  - D1 `WRITING_DOCTRINE § Single Backbone`: "normalt to hovedbevis… høyst én kontrollert differensiator". Judgment is a *third* case by construction.
  - D2 Stage 1 wrote `"Støttebevis…"` + `structure_guidance` = `kort som støtte` (0828/155301) / `ikke som et tredje hovedcase` (210926). **In every run.**
  - D3 `lifecycle: CONCEPT` = weakest maturity rank. Stage 3 review states the reason: *"fordi innføringsstatusen er svakere."*
  - Fixing only Stage 3's incentive leaves D1 and D2 firing.
- **`manifest.py::stage_policy_sha256` folds `writing_policy` into EVERY stage hash.** The voice-file edit regenerated Stage 1 too (headline, thesis, `writer_guidance`, evidence order, facets `PF-19,01,11`→`PF-01,08,19`). The two runs are **not** a controlled voice-only A/B. Codex is right; my earlier framing was wrong.
- **The new voice policy IMPROVED retention.** Avinor Stage 3 drops 3-of-9 → 1-of-10; final refs 7 → 11. Do not roll it back.
- **`cli.py:1043-1049` sends personality downstream as brakes only** — `plain_language_label` + `expression_ceiling` + `expression_guardrail`. Discards `vacancy_relevance`, `intended_employer_interpretation`, `misread_risk`, `evidence_refs`. Stages 2/3 can suppress personality, never express it.
- **`stage3_final_writer_review.md:85-86`**: *"Nobody will compare your final against the strategy… There is no comparator and there will never be one."* Plus the "form your own thesis before reading upstream" rule stated **twice** (lines 36-40 and 55-58).
- **Constraint load: 100 policy bullets routed identically to all 3 stages.** Doctrine 59 / Persuasion 19 / Voice 22. Stages 1 and 3 have named-section routing tables. **Stage 2 has none** — the most saturated stage is the one that writes the first full realization.
- **T15 asserts `set(facet) <= {3 keys}`** (`test_t13_t15_merge_leakage_personality.py:355`). Any `cli.py` field expansion breaks it. One-line edit; ED-legitimate.
- **`Build/prompts/*` and `Process/operator_prompts/v2/*` are byte-identical today.** Codex's plan asserts they are unsynchronized provenance. False.
- `additionalProperties: false` everywhere; `semantic_fields()` derives from schema properties, so a new field flows automatically — irrelevant, see landmines.

## Landmines / disproven premises

- **`"rapportert i bruk"` → `"fortsatt i bruk"` is NOT claim drift.** `PERSUASION_CALIBRATION.md:42-49` gives that exact pattern as `riktig`. Operator-approved. My earlier audit and the GPT review were both wrong. Do not "fix" it.
- **A `decision_signal` schema field would not have helped.** Stage 1 already wrote the signal in plain prose in `evidence_plan[].role`: *"kandidaten **avviste falsk presisjon**"* / *"**erstattet falsk presisjon** med en transparent, vektet proxymodell"*. Explicit, unmistakable, deleted anyway — 3/3. **The problem is not representational.** I withdraw my own approved schema proposal.
- **`krav_framing` enum likewise unnecessary.** `importance: MINIMUM` + `relation: GAP` + `objections[].reframe` + `honesty_note` already carry it, and both runs classified R02/R04 correctly. The system knows and has no instruction about what to *do*. Instruction gap, not representation gap.
- **Discard log / proposition-survival check: dead end.** Both deep-research reports independently conclude self-reported logs don't work (IBM: explanations *eroded* IF rate); ED-1 forbids the external verifier that would replace them. Only exit is fixing the ranking. Both plans reached this; don't reopen.
- Lix as a target invites deleting exactly the technical vocabulary that carries credibility. Diagnostic only.

## The synthesis neither plan has

**Fuse judgment into the carrying case. Do not let it compete as a separate case.**

The judgment becomes the explanation of why *that* carrying case succeeded or was constrained — not a second exhibit. Then it is: not `Støttebevis` (D2 dead), riding on `IN_USE` evidence (D3 dead), not a third case (D1 dead). Unremovable without gutting the main case. **Zero machinery.**

Simultaneously delivers the user's other two targets:
- 5.3 fewer-arguments: 4 thin cases → 2 deep ones, as a *consequence* not a quota. Presenter's Paradox (evaluators average, not add) is the real rationale — a ranking argument, never a counting one.
- 5.1 pretension: two paragraph-terminal morals disappear; the symmetric 4×4-sentence rhythm breaks; only two items left to grade.

**Critical distinction:** co-location ≠ fusion. The 0828 draft put both in one paragraph (*"Når et annet prosjekt manglet tilstrekkelig datagrunnlag…"* — separate project, own subject) and Stage 3 still cut it. Fusion means the judgment is **about the carrying case itself**. State this explicitly or the known failure mode repeats.

## Pretension (target 5.1) — measured diagnosis

Avinor final letter, 309 words: **7 self-framing/meta markers** (Huseierne: 2). First-person density only 3.6% — **"I" is not the problem.** Three mechanisms, ranked:

1. **The moral-of-the-story sentence.** Every body paragraph ends telling the reader what to conclude. Four consecutive distilled lessons = "is this person going to be a lot?". Highest-value single fix; also shortens, de-symmetrizes, and raises seniority.
2. **Self-grading the portfolio.** `"Det tydeligste gjennomføringsbeviset mitt er…"` — candidate ranks his own evidence for the employer. Worst phrase in either letter.
3. **Announced abstraction level.** `"…arbeidet med verdistyring på metodenivå."`

**Non-obvious:** the strongest anti-pretension lever is **category anchoring**, not tone softening. Unusual detail reads as self-display when its job function is invisible, as relevant depth when the reader has already classified the candidate. Codex has category-first as objective #2 but never connects it to the pretension target. Connect it.

**Do NOT:** add hedges, weaken work verbs, add self-deprecation, or cut first-person. All damage `Rolig faglig tyngde`, and GPT's report shows factual ownership ("jeg valgte") is *less* culturally risky than adjectival self-description. The problem is the interpreting, not the claiming.

## Polish sub-pass (5.2) — the point Codex will miss

Its real value is **not** finishing. It is that splitting substance from register **removes the substantive pass's need to buy smoothness with signal**. Today one objective covers both, which is exactly when "reads better" silently outranks "says more". Write that permission where the substantive pass reads it, or it changes nothing.

Design: last section of the Stage 3 instruction. Content-lock precondition. **Positive authority list only** (substitution beats suppression). One hard boundary sentence — *"If a change would alter what the employer learns, it is out of scope"* — beats an enumerated prohibition list. Explicit licence to delete a sentence whose only function was telling the reader what to conclude; that is interpretation, not content, and without it the pass cannot touch pretension mechanism #1. **Open design question worth Codex's judgment:** that licence sits exactly on the realization/meaning line — word it to permit removing redundant interpretation without permitting removal of employer-relevance reasoning.

## Adjudications already settled

- Personality packet: **Codex's 6 fields, not my 7.** Forwarding `evidence_refs` couples personality to evidence selection and risks a second evidence authority.
- Regime branching (both research reports push it): **defer.** Depends on one phone call the user can make; hard-coding a taxonomy on two vacancies fits noise.
- My CV/letter "one paragraph must carry judgment" rule: **withdrawn** — a quota in disguise, hard-codes the current 4-paragraph shape. §7 fusion achieves it without a count.

## What I most want Codex to think about

1. You kept the two-case cap **and** asked Stage 3 to preserve judgment. Those conflict; the repo shows which wins, 3/3. Reconcile or fuse.
2. Your fix is entirely downstream of where the subordination happens (Stage 1's `Støttebevis`).
3. You add 3 constraints to Stage 2 and subtract none — from the only stage with no routing table. **Subtraction is part of the treatment, not cleanup.**
4. Your `Anti-karikatur` loosening ("remove *readability beats visible personality*") is the wrong sign for a candidate whose measured defect is 7 self-framing markers. Reword the brake to "employer inference beats personality display" — don't delete it.
5. Every item worth adopting in either plan costs **zero machinery**. Not a coincidence — every traced failure was an instruction or a structural position, never a missing representation. Let that discipline the master plan.
