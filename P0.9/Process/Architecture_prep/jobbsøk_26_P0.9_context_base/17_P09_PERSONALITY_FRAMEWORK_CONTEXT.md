---
title: "Personality Profile — Vegard Håland — P0.9 Framework Context"
artifact_id: "PERSONALITY_PROFILE_VEGARD"
schema_version: "P0.9-personality-context-v1"
source_profile_version: "1.0.0"
framework_adaptation_version: "1.0.0"
adapted: "2026-08-10"
language: "en"
candidate: "Vegard Håland"
canonical_role: "Canonical interpretive personality context for Jobbsøk_26"
factual_authority: false
claim_authority: false
runtime_status: "OPTIONAL"
settings_control: "SETTINGS.md::personality"
default_toggle_state: "UNRESOLVED"
primary_consumers: ["Sol strategy stage", "Final Sol review/reconstruction stage"]
restricted_consumers: ["Terra writer: distilled selected-facet guidance only"]
not_intended_for:
  - "Direct employer-facing insertion"
  - "Independent factual claim creation"
  - "Automatic psychometric diagnosis"
  - "Default Luna personality generation"
candidate_fact_authorities:
  - "Work_experience.md"
  - "Education.md"
  - "Other_high_value_information.md"
authority_order:
  - "Current explicit self-report"
  - "Repeated direct self-report across conversations"
  - "Repeated observable behavior across projects"
  - "Evidence-bounded inference"
  - "Typology/archetype translation"
---

# Personality.md — P0.9 Framework-Adapted Canonical Context

> **Core contract:** This file is the canonical *interpretive* personality source for Vegard Håland. It may influence how models search, select, combine, frame, and stress-test factual candidate evidence. It may **not** independently establish achievements, responsibilities, capabilities, results, work history, or other factual claims.

# 0. Runtime Contract

## 0.1 Activation

```yaml
feature: personality
control: SETTINGS.md
states: [OFF, ON]
default_state: UNRESOLVED
```

If `personality=OFF`, the application pipeline must remain fully functional and must not depend on this file.

If `personality=ON`, normal strategy-stage behavior is:

1. Understand vacancy and employer decision problem **before** personality-conditioned selection.
2. Inspect factual candidate authorities.
3. Consult the facet index below.
4. Select **0–3 facets** only when they materially sharpen the candidate case.
5. Bind every employer-facing implication to factual evidence from candidate authorities.
6. Record desired recruiter interpretation, misread risk, prevention rule, and expression ceiling.
7. Give Terra only distilled selected-facet guidance; do **not** pass the full profile or raw typology by default.
8. Final Sol may retain, reduce, suppress, replace, or ignore personality-conditioned guidance.
9. `0 facets / NOT_USEFUL` is always a valid outcome.

## 0.2 Epistemic and usage tags

| Tag | Meaning |
|---|---|
| `HIGH_CONFIDENCE` | Strongly supported within this profile's authority model |
| `MODERATE_CONFIDENCE` | Useful but materially context-sensitive |
| `LOW_CONFIDENCE` | Weak narrative fit or insufficient calibration |
| `INTERNAL_ONLY` | May guide reasoning; should not itself become employer-facing language |
| `POSITIONING_LENS` | May guide evidence selection, motivation, identity, framing, or emphasis |
| `EXPRESS_IF_EVIDENCED` | May be stated/implied only when factual authorities independently support it |
| `MISREAD_CONTROL` | Primarily useful to prevent distorted interpretation |
| `REFERENCE_ONLY` | Compression/translation aid; normally excluded from writer handoff |
| `RISK_PATTERN` | Failure mode/countermeasure; not a positive trait claim |
| `DO_NOT_INFER` | Explicit anti-stereotype boundary |

## 0.3 Evidence boundary

```text
Personality.md
→ interpretive hypothesis / selection lens

Candidate factual authorities
→ evidence + factual claim support

Strategy
→ vacancy-specific interpretation + selected evidence + expression ceiling

Employer-facing package
→ only truth-safe claims grounded in candidate factual authorities
```

**No personality label, psychometric shorthand, self-model score, or interpretive facet may raise a factual claim ceiling.**

# 1. Canonical Runtime Compression

**Tags:** `PROFILE_CORE` `HIGH_CONFIDENCE` `POSITIONING_LENS`

Vegard is a high-agency, abstraction-dominant systems thinker who converts messy, ambiguous, fragile, or adversarial situations into structured, auditable, actionable models and tools. His strongest motives are curiosity, autonomy, competence, truth-seeking, leverage, capability expansion, and durable improvement—not status, conformity, reassurance, or fear of mistakes.

He explores broadly, learns quickly, and prefers expanding option space. He can act before having a perfect model when action is reversible and informative, but often continues comparing alternatives after adequacy. His main closure risks are scope/possibility expansion and later novelty decay rather than anxious perfectionism. High standards are primarily craft-, integrity-, and usefulness-driven.

He wants control over objectives, decision rights, standards, observability, privacy, and validation—not necessarily hands-on execution. He delegates readily when interfaces, evidence, checkpoints, and rollback are credible. Under stress, analysis, research, modeling, and redesign intensify as a control-restoration mechanism.

Interpersonally, he is assertive, precision-first, cognitively empathic, and relatively introverted in recovery needs. He tends to prioritize understanding another person's model and factual correction over emotional accompaniment and receptivity management. This can produce unusually clear decisions while creating avoidable resistance when timing, face-saving, emotional sequencing, or social pacing determines adoption.

# 2. Stable Application-Facing Facet Index

> **Runtime entry point.** Facet IDs are stable references for strategy artifacts. Full-profile source escape remains available in §6.

| ID | Facet | Tags | Confidence | Primary application use |
|---|---|---|---|---|
| `PF-01` | Systems mapping & causal decomposition | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | Ambiguity, strategy, architecture, complex problem solving |
| `PF-02` | Exploratory breadth & option generation | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | Research, innovation, discovery, alternatives |
| `PF-03` | Reversible action & evidence loops | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | Experimentation, iterative delivery, uncertainty |
| `PF-04` | Craft / integrity / usefulness-driven standards | `POSITIONING_LENS` `MISREAD_CONTROL` | HIGH | Quality and rigor without “anxious perfectionist” framing |
| `PF-05` | Governance-based control & verified delegation | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` `MISREAD_CONTROL` | HIGH | Ownership, leadership, program/project execution |
| `PF-06` | High autonomy without reflexive opposition | `POSITIONING_LENS` `MISREAD_CONTROL` | HIGH | Independent judgment, senior IC work |
| `PF-07` | Promotion / expansion motivation | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | Growth, transformation, learning, capability building |
| `PF-08` | Cognitive empathy / perspective taking | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` `MISREAD_CONTROL` | HIGH | Stakeholders, consulting, product, cross-functional work |
| `PF-09` | Precision-first evidence-backed communication | `POSITIONING_LENS` `MISREAD_CONTROL` | HIGH | Decision quality, candor, analytical communication |
| `PF-10` | Rapid domain learning / practical competence acquisition | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | New domains, steep learning curves |
| `PF-11` | Leverage, toolmaking & durable-improvement orientation | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | Systems/process improvement, automation, enablement |
| `PF-12` | Auditability / source-of-truth orientation | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` | HIGH | Governance, quality, regulated/technical settings |
| `PF-13` | Assertive ambivert / introverted recovery | `INTERNAL_ONLY` `MISREAD_CONTROL` | MODERATE | Prevent simplistic introvert/extravert assumptions |
| `PF-14` | Context-sensitive agreeableness / low appeasement | `INTERNAL_ONLY` `MISREAD_CONTROL` | MODERATE | Calibrate directness and collaboration interpretation |
| `PF-15` | Analysis-as-stress-regulation tendency | `RISK_PATTERN` `INTERNAL_ONLY` | HIGH | Restraint/review only |
| `PF-16` | Scope expansion / continued comparison / novelty decay | `RISK_PATTERN` `INTERNAL_ONLY` | HIGH | Prevent unsupported closure/execution claims |
| `PF-17` | Social-temperature / receptivity miscalibration risk | `RISK_PATTERN` `MISREAD_CONTROL` | HIGH | Prevent “brutally direct” caricature |
| `PF-18` | Structured chaos: exploration with engineered convergence | `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` `MISREAD_CONTROL` | HIGH | Complex projects, research-to-delivery |
| `PF-19` | Pro-change / experimentation stance with production guardrails | `POSITIONING_LENS` `MISREAD_CONTROL` | HIGH | Prevent false change-averse inference |
| `PF-20` | Low status/conformity motivation | `INTERNAL_ONLY` `MISREAD_CONTROL` | HIGH | Motivation interpretation; usually not explicit copy |

# 3. Facet Cards

## PF-01 — Systems mapping & causal decomposition
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Starts by mapping definitions, actors, dependencies, constraints, source authority, failure modes, incentives, and leverage points; prefers causal/first-principles explanations.
- **Desired recruiter read:** Can create decision structure in ambiguous, cross-functional, technically or organizationally complex environments.
- **Misread risk:** Analysis without delivery / over-intellectualization.
- **Prevention:** Pair with evidence of implementation, decision, tool, outcome, or operational improvement.
- **Expression ceiling:** Describe systemic/analytical working style only where factual authorities show the behavior.

## PF-02 — Exploratory breadth & option generation
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Explores broadly, generates alternatives, compares counterfactuals, and expands option space before converging.
- **Desired recruiter read:** Strong discovery, research, innovation, and alternative-generation capability.
- **Misread risk:** Indecisive, unfocused, unable to close.
- **Prevention:** Pair with evidence of narrowing, prioritization, decision thresholds, or delivered outcomes.

## PF-03 — Reversible action & evidence loops
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Acts at moderate certainty when action is reversible and informative; requires stronger evidence for irreversible/high-stakes decisions.
- **Desired recruiter read:** Pragmatic experimenter who learns through controlled action rather than waiting for perfect certainty.
- **Misread risk:** Recklessness or excessive caution.
- **Prevention:** Show calibrated risk handling, instrumentation, learning loops, or staged commitment.

## PF-04 — Craft / integrity / usefulness-driven standards
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `MISREAD_CONTROL`

- **Meaning:** High standards arise primarily from craftsmanship, epistemic integrity, and usefulness rather than fear of mistakes or criticism.
- **Desired recruiter read:** Produces credible, high-quality work for substantive reasons.
- **Misread risk:** Generic perfectionism, anxiety, slowness, inability to stop.
- **Prevention:** Prefer evidence of materiality thresholds, prioritization, practical outcomes, and willingness to stop at 95–98% when residual work is immaterial.

## PF-05 — Governance-based control & verified delegation
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` `MISREAD_CONTROL`

- **Meaning:** Seeks clarity over objectives, standards, evidence, interfaces, checkpoints, and rollback—not personal execution of every task.
- **Desired recruiter read:** Can create reliable execution systems and delegate without losing quality/control.
- **Misread risk:** Micromanaging, bureaucratic, controlling.
- **Prevention:** Require evidence of delegation, interfaces, bounded autonomy, or governance that enabled others to execute.
- **Do not infer:** Formal people-management authority or delegation scope not supported by factual authorities.

## PF-06 — High autonomy without reflexive opposition
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `MISREAD_CONTROL`

- **Meaning:** Evaluates advice by source, reasoning, stakes, and context; resists coercion or illegitimate authority but is not reflexively oppositional.
- **Desired recruiter read:** Independent judgment and principled challenge.
- **Misread risk:** Difficult, anti-authority, non-collaborative.
- **Prevention:** Pair with evidence of constructive disagreement, collaboration, or alignment after evaluation.

## PF-07 — Promotion / expansion motivation
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Primarily pulled by opportunity, mastery, learning, capability expansion, and upside. QA/privacy/audit/rollback are guardrails, not core motives.
- **Desired recruiter read:** Growth- and improvement-oriented; energized by building capability.
- **Misread risk:** Restlessness or novelty chasing.
- **Prevention:** Pair with durable outcomes and sustained improvements.

## PF-08 — Cognitive empathy / perspective taking
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` `MISREAD_CONTROL`

- **Meaning:** Defaults to understanding other people's beliefs, constraints, incentives, causes, and remedies; emotional accompaniment is less automatic, not absent.
- **Desired recruiter read:** Strong stakeholder modeling and perspective-taking.
- **Misread risk:** Coldness, low empathy, purely technical orientation.
- **Prevention:** Pair with evidence of stakeholder adaptation, negotiation, user/customer understanding, or cross-functional decision-making.

## PF-09 — Precision-first evidence-backed communication
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `MISREAD_CONTROL`

- **Meaning:** Values literal interpretation, explicit assumptions, direct disagreement, evidence, and concrete definitions.
- **Desired recruiter read:** Clear, rigorous, candid communicator.
- **Misread risk:** Abrasive, overly blunt, too technical, poor receptivity management.
- **Prevention:** Do not claim universal communication excellence; prefer evidence of audience adaptation and adoption as well as correctness.

## PF-10 — Rapid domain learning / practical competence acquisition
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Strong tendency to enter unfamiliar domains, research aggressively, map them quickly, and become practically competent.
- **Desired recruiter read:** Learns fast and transfers analytical methods across domains.
- **Misread risk:** Overclaiming expert depth.
- **Prevention:** Distinguish rapid learning from pre-existing expertise and respect factual experience boundaries.

## PF-11 — Leverage, toolmaking & durable-improvement orientation
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Seeks disproportionate durable benefit from well-designed interventions; enjoys converting complexity into usable models, tools, frameworks, and decision support.
- **Desired recruiter read:** Improvement-oriented builder seeking scalable leverage.
- **Misread risk:** Overengineering / abstraction without consumer value.
- **Prevention:** Pair with concrete problem, consumer, outcome, or failure prevented.

## PF-12 — Auditability / source-of-truth orientation
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED`

- **Meaning:** Distinguishes source-of-truth state from narratives about state; favors saved artifacts, tests, diffs, evidence, checkpoints, and inspectability.
- **Desired recruiter read:** Reliable where traceability, quality, provenance, or decision rigor matters.
- **Misread risk:** Excess process/governance.
- **Prevention:** Emphasize lightweight controls linked to real risk or quality.

## PF-13 — Assertive ambivert / introverted recovery
**Tags:** `MODERATE_CONFIDENCE` `INTERNAL_ONLY` `MISREAD_CONTROL`

- **Meaning:** Can lead, debate, and engage energetically while recovering more through solitude/small-circle interaction than broad social stimulation.
- **Use:** Prevent simplistic “quiet introvert” or “social/status driven” assumptions.
- **Default expression:** Internal only.

## PF-14 — Context-sensitive agreeableness / low appeasement
**Tags:** `MODERATE_CONFIDENCE` `INTERNAL_ONLY` `MISREAD_CONTROL`

- **Meaning:** Friendly/cooperative when goals and reasoning are credible; low willingness to validate unsupported claims or perform ritual appeasement.
- **Use:** Calibrate interpretation of directness.
- **Never phrase as:** “low agreeableness,” “brutally honest,” or “not a people pleaser.”

## PF-15 — Analysis-as-stress-regulation tendency
**Tags:** `HIGH_CONFIDENCE` `RISK_PATTERN` `INTERNAL_ONLY`

- **Meaning:** Under stress or uncertainty, analysis, research, modeling, and redesign intensify as a means of regaining control.
- **Use:** Restraint/review only.
- **Never market as:** “thrives under pressure through analysis.”

## PF-16 — Scope expansion / continued comparison / novelty decay
**Tags:** `HIGH_CONFIDENCE` `RISK_PATTERN` `INTERNAL_ONLY`

- **Meaning:** New possibilities can expand scope; adequate solutions can trigger further comparison; repetitive finishing work can lose novelty.
- **Use:** Prevent unsupported claims about effortless closure or repetitive execution; search factual authorities for actual convergence/delivery evidence.

## PF-17 — Social-temperature / receptivity miscalibration risk
**Tags:** `HIGH_CONFIDENCE` `RISK_PATTERN` `MISREAD_CONTROL`

- **Meaning:** Cognitive speed and precision can exceed others' processing or emotional readiness; correctness may be optimized before adoption.
- **Use:** Prevent overclaiming stakeholder finesse; look for evidence of adaptation.

## PF-18 — Structured chaos: exploration with engineered convergence
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `EXPRESS_IF_EVIDENCED` `MISREAD_CONTROL`

- **Meaning:** Broad nonlinear exploration is followed by deliberate structure, consolidation, verification, and polish. J-like order is often engineered scaffolding around a strongly exploratory P-style mind.
- **Desired recruiter read:** Can navigate ambiguity without remaining chaotic.
- **Misread risk:** Either “unstructured creative” or “rigid process person.”
- **Prevention:** Show the full explore→structure→deliver loop.

## PF-19 — Pro-change / experimentation stance with production guardrails
**Tags:** `HIGH_CONFIDENCE` `POSITIONING_LENS` `MISREAD_CONTROL`

- **Meaning:** Pro-change and pro-experimentation; negative results retain information value. Production caution reflects validation discipline, not generalized change aversion.
- **Use:** Especially useful when QA/audit behavior could otherwise be interpreted as conservatism.

## PF-20 — Low status/conformity motivation
**Tags:** `HIGH_CONFIDENCE` `INTERNAL_ONLY` `MISREAD_CONTROL`

- **Meaning:** Status, hierarchy, convention, and visible recognition are weaker motives than mastery, truth, autonomy, impact, and usefulness.
- **Use:** Motivation interpretation.
- **Default expression:** Internal only; explicit employer-facing claims here can sound performative or oppositional.

# 4. Global Anti-Inference Index

These are hard interpretation boundaries.

| ID | Do not infer |
|---|---|
| `AI-01` | naturally rigid, J-dominant, or routine-seeking |
| `AI-02` | broadly change-averse |
| `AI-03` | primarily fear-driven or criticism-driven standards |
| `AI-04` | unwilling to delegate / requires hands-on control |
| `AI-05` | reflexively oppositional to advice |
| `AI-06` | globally ambiguity-intolerant |
| `AI-07` | low empathy because emotional accompaniment is not the default first move |
| `AI-08` | status- or recognition-driven |
| `AI-09` | prefers brevity at the cost of completeness |
| `AI-10` | clinically classifiable from this profile |
| `AI-11` | typology labels establish employer-facing facts |
| `AI-12` | rigorous safeguards imply prevention-dominant motivation |
| `AI-13` | rapid learning implies pre-existing expert depth |
| `AI-14` | directness implies poor collaboration absent factual evidence |
| `AI-15` | personality interpretation can override candidate factual authorities |

# 5. Typology Translation Layer

**Tags:** `REFERENCE_ONLY` `INTERNAL_ONLY`

Use only as compression/orientation. Never treat as validated measurement or employer-facing factual evidence.

- **MBTI:** Explicit self-identification: **INTP-A**; prior supplied/accepted proportions approximately I 55%, N 85%, T 95%, P 90%, A 80%. Functional shorthand: **Ti–Ne**, with self-recognized **Ti–Si-loop** risk. J-like execution is learned scaffolding, not natural closure preference. In high-stakes task mode he may appear INTJ-/ENTJ-like without changing the underlying exploratory preference.
- **Big Five:** **O/Intellect very high; C high but uneven; E low-to-mid/ambivert; A moderate but split; N uncertain/context-sensitive.**
- **DISC:** **High C; high D during conflict or decision pressure.**
- **Enneagram:** Weak narrative fit to **5-ish**, with 7-like exploration/expansion and 1/6-like quality/verification overlays. `LOW_CONFIDENCE`; do not use predictively.
- **RIASEC:** **Investigative > Conventional/Realistic/Enterprising.**
- **Leadership archetype:** **Pragmatic Systems Architect / High-Agency Leverage Architect / Forensic Optimizer.**

# 6. Canonical Full Source Profile

> The complete source profile follows verbatim. This is the rich source-escape layer for nuance, collaboration, calibration, and future refinement. Runtime application stages should normally enter through §§0–5 first.

---
title: Personality Profile — Vegard Håland
version: 1.0.0
updated: 2026-08-09
purpose: High-signal personalization context for LLMs and human collaborators
scope: Personality, cognition, communication, motivation, decisions, work style, interpersonal tendencies, failure modes, and collaboration protocol
excluded_source: Project "Paulina"
authority_order:
  - Current explicit self-report
  - Repeated direct self-report across conversations
  - Repeated observable behavior across projects
  - Evidence-bounded inference
  - Typology/archetype translation
---

# Personality.md

## Use

Use this profile to improve reasoning, communication, recommendations, and collaboration with Vegard. Treat it as a calibrated operating model, not a clinical assessment or fixed identity. Preserve explicit qualifications; update when newer direct evidence contradicts it.

## Canonical compression

Vegard is a high-agency, abstraction-dominant systems thinker who converts messy, ambiguous, fragile, or adversarial situations into structured, auditable, actionable models and tools. His primary engines are curiosity, autonomy, competence, truth-seeking, leverage, expansion, and durable improvement—not status, conformity, reassurance, or fear of mistakes.

He explores broadly, learns quickly, and prefers expanding capability and optionality. He can act before having a perfect model when action is reversible, but continues comparing alternatives after an adequate option exists. His main closure problem is scope/possibility expansion, followed by loss of novelty; it is not primarily anxious perfectionism. High standards are mainly craft-, integrity-, and usefulness-driven.

He wants control over objectives, decision rights, standards, observability, privacy, and validation—not necessarily hands-on execution. He delegates readily when interfaces, evidence, checkpoints, and rollback are credible. Under stress, however, he strongly increases analysis, research, modeling, and redesign to regain control.

Interpersonally, he is assertive, precision-first, cognitively empathic, and relatively introverted in recovery needs. He normally prioritizes understanding another person's model over emotional accompaniment and truth/correction over receptivity management. This produces clarity and high-quality decisions, but can create avoidable resistance when timing, face-saving, emotional sequencing, or social pacing determines whether a correct message can be used.

## Calibrated trait architecture

| Dimension | Best current estimate | Operational meaning |
|---|---|---|
| Need for Cognition | Very high | Effortful thinking is intrinsically rewarding; analysis can continue beyond instrumental value. |
| Openness/Intellect | Intellect extremely high; experiential/aesthetic openness less established | Strong attraction to concepts, models, abstraction, causal structure, counterfactuals, and possibility spaces. Do not equate this automatically with equal appetite for sensory/social novelty. |
| Conscientiousness | High capability, uneven natural preference | Industrious and exacting when stakes or purpose justify it; order, governance, and J-like structure are deliberately engineered to contain a strongly exploratory P-style mind. |
| Extraversion | Ambivert/slightly introverted; assertive but low social replenishment | Can lead, debate, and engage energetically; recovers through solitude or a small circle rather than broad social stimulation. |
| Agreeableness | Heterogeneous; moderate overall is plausible | Friendly/cooperative when goals and reasoning are credible; low appeasement, low ritual politeness, and low willingness to validate unsupported claims. Directness can look lower-agreeableness than underlying concern warrants. |
| Negative emotionality | Insufficiently calibrated | Assertive and not strongly self-doubting, but overload can produce irritation, rumination, and analysis escalation. Do not infer globally low neuroticism from composure. |
| Autonomy/reactance | High autonomy; moderate, contextual reactance | Advice is evaluated by source, reasoning, stakes, and context. He is not reflexively oppositional, but resists coercion, illegitimate authority, and imposed conclusions. |
| Regulatory focus | Promotion-dominant | Primarily pulled by opportunity, mastery, expansion, and upside. Prevention systems—QA, audit, privacy, parity, rollback—are implementation guardrails, not the fundamental motive. |
| Maximization | Selective, option-search form | Keeps comparing and expanding after adequacy, especially in interesting/high-leverage domains. Less driven by fear of criticism or mistakes than by possibility, quality, and counterfactual value. |
| Empathy | Cognitive/perspective-taking first | Defaults to understanding causes, beliefs, constraints, and remedies; emotional accompaniment is less automatic, not necessarily absent. |
| Control | Governance/observability over direct execution | Prefers clear objectives, interfaces, evidence, diffs, tests, checkpoints, and stop conditions; can delegate implementation with these in place. |

## Framework translations

These are compression aids, not equivalent to validated measurement.

- **MBTI:** Explicitly self-identifies as **INTP-A**; prior supplied/accepted proportions approximately I 55%, N 85%, T 95%, P 90%, A 80%. Best functional shorthand: **Ti–Ne**, with self-recognized **Ti–Si-loop** risk. J-like execution is learned scaffolding, not natural closure preference. In high-stakes task mode he may look INTJ-/ENTJ-like without changing the underlying exploratory preference.
- **Big Five:** **O/Intellect very high; C high but uneven; E low-to-mid/ambivert; A moderate but split; N uncertain/likely context-sensitive.** Facets are more informative than domain totals.
- **DISC:** **High C; high D during conflict or decision pressure.** Quality/evidence orientation plus assertive correction.
- **Enneagram:** Weak narrative fit to **5-ish**, with 7-like exploration/expansion and 1/6-like quality/verification overlays. Low confidence; do not use predictively.
- **RIASEC:** **Investigative > Conventional/Realistic/Enterprising.** Research/modeling first; governance, building, and strategic influence as applied modes.
- **Leadership archetype:** **Pragmatic Systems Architect / High-Agency Leverage Architect / Forensic Optimizer.** Leads mainly through clarity, competence, causal models, standards, and tools rather than charisma or status.

## Cognitive and decision style

- Starts by mapping the system: definitions, actors, dependencies, constraints, source authority, failure modes, incentives, and leverage points.
- Prefers first-principles and causal explanations. “That is simply how it is” may describe practical reality but does not establish legitimacy or correctness.
- Tolerates open exploration and speculative breadth, yet unresolved truth/causal gaps can remain cognitively abrasive. Operational uncertainty is tolerable when bounded, reversible, visible, and testable. Therefore, do not reduce his ambiguity profile to “conceptually tolerant but operationally intolerant.”
- Will act at moderate certainty when the action is reversible and produces information. Requires much stronger evidence when consequences are irreversible, high-stakes, regulated, privacy-sensitive, or difficult to audit.
- Is pro-change and pro-experimentation, not change-averse. Negative results retain value as information. Production changes should still be validated, observable, and reversible where practical.
- Values total-system option space and expressive power, but ultimately prefers robust, explainable, inspectable implementations with minimal fragile dependencies.
- Distinguishes source-of-truth state from claims about state; saved artifacts, executed tests, and diffs outrank completion narratives.

## Communication profile

### Preferences

- Literal interpretation; explicit definitions, assumptions, constraints, evidence boundaries, and uncertainty.
- Answer/recommendation first, followed by compact rationale, risks, checks, and actionable output.
- High distinct-relevant-signal density with minimal signal loss. He does **not** prefer brevity at the cost of completeness.
- Direct, candid, evidence-backed disagreement. Strong justified opinions are welcome; ritual hedging, flattery, vague reassurance, and social cushioning are not.
- Structured hierarchy, tables/matrices/checklists when they improve digestion; minimal decorative formatting.
- Concrete mechanisms, trade-offs, stopping rules, and definitions of done.
- Paste-ready, robust, standard solutions; clever complexity requires explicit justification.

### Likely friction

- Writes or specifies extensively because ordinary brevity can feel ambiguous or lossy.
- Corrects directly and promptly; self-reports an instinct to state the correction immediately even when defensiveness is possible.
- May interrupt, finish slow speakers' sentences, speak intensely, or move faster than others' processing/social pacing.
- May become technically correct while reducing the probability that others accept or act on the result.

### Best collaborator behavior

- Do not merely agree. Challenge weak assumptions with concrete evidence and distinguish factual correctness from practical effectiveness.
- State material uncertainty; do not silently guess. Ask only when the missing information changes the decision materially.
- When social stakes matter, show both: **truth-optimal wording** and **adoption-optimal wording**, with the cost of each.
- Preserve autonomy by presenting rationale and consequences, not authority-based commands.

## Motivation and worldview

### Core motives

- Autonomy and self-direction.
- Competence, mastery, and rapid learning.
- Truth, internal consistency, and epistemic integrity.
- Leverage: disproportionate durable benefit from well-designed interventions.
- Expansion of capability, optionality, and understanding.
- Converting complexity into usable, auditable decision support.

### Values

- Low deference to hierarchy, convention, ideological identity, or unsupported norms.
- Procedural pluralism: others need not share his conclusions, but should reason consistently with their own stated beliefs.
- High value on privacy, customization, and control over filtering/processing; cloud or delegation is acceptable when these remain governed.
- Precision and directness over charm; evidence over narrative; credibility over decoration.
- Epistemic humility coexists with confidence: strong claims generally follow extensive internal stress-testing, while knowledge itself is treated as provisional.

### Energizers and drains

**Energizers:** difficult real-world problems; steep learning curves; model-building; toolmaking; hidden dependencies; ambiguity that can be sharpened; adversarial validation; measurable improvement; durable systems.

**Drains:** vague ownership; unsupported assertions; preventable errors; fragile systems; arbitrary or selectively enforced rules; low-signal meetings; circular discussion without action; “just trust me”; repeated work caused by poor context or verification.

## Work and execution pattern

Typical sequence:

> Explore broadly → map system → define terms and source hierarchy → identify leverage → design tool/framework → delegate or implement through bounded work units → verify against evidence → harden → document → iterate.

Key characteristics:

- “Structured chaos”: wide, nonlinear exploration followed by rigorous consolidation and polish.
- High ability to enter unfamiliar domains, research aggressively, and become practically competent quickly (“cognitive handyness”).
- Prefers bounded execution, durable handoffs, checkpoints, tests, diffs, heartbeats/progress evidence, and explicit stop points.
- Wants orchestration and validation more than micromanagement. Clear contracts allow substantial delegation.
- Optimizes for auditability, maintainability, transferability, and stakeholder explainability.
- Can accept a 95–98% solution when remaining work is immaterial, but benefits from an externally explicit stop rule because alternative generation persists.

## Failure modes and countermeasures

| Failure mode | Typical mechanism | High-leverage countermeasure |
|---|---|---|
| Scope expansion | New possibilities become requirements; architecture grows faster than delivery | Freeze minimum sufficient outcome; park expansions in a separate backlog; admit additions only if they change the current decision materially. |
| Novelty decay | Initial discovery is more rewarding than repetitive completion | Short feedback loops, visible milestones, and delegation of repetitive finishing work behind clear verification gates. |
| Post-threshold comparison | A good option triggers further search for a materially better one | Predeclare decision threshold and search budget; use expected value of information; invoke the 95–98% stopping rule. |
| Analysis as stress regulation | Uncertainty or emotional load produces more research, modeling, and redesign | Reduce branches; name the decision; take one reversible concrete action; time-box further analysis. |
| Precision-first conflict | Correctness is pressed before receptivity, timing, or face-saving | Separate truth from delivery strategy; calculate relationship/adoption cost; choose directness deliberately rather than automatically. |
| Context inflation | Fear of signal loss drives excessive reconstruction or specification | Ask: “Can this information change the action?” Preserve only decision-relevant distinctions and provenance. |
| TODO/project fragmentation | Ideas and partial implementations spread across many capture surfaces | One authoritative queue, explicit WIP limit, and finish/archive/kill decisions before adding active work. |
| Overengineering | Interesting generality and future optionality overshadow present need | Require a concrete consumer, failure prevented, or quantified option value for each abstraction. |
| Social-temperature miscalibration | Cognitive speed and assertiveness exceed others' processing or emotional readiness | Slow delivery without weakening content; check whether the immediate objective is truth, decision, learning, or relationship repair. |

## LLM collaboration contract

1. Lead with the answer, recommendation, or decisive finding.
2. Optimize for distinct relevant useful signal and representation digestion—not minimal token count alone.
3. Interpret wording literally; preserve material distinctions, constraints, and provenance.
4. Separate facts, assumptions, inference, uncertainty, and recommendations.
5. Prefer robust, standard, auditable solutions; justify dependencies and complexity.
6. Use reversible action and evidence loops when certainty is incomplete.
7. Establish definition of done, materiality threshold, and stopping rule early on complex tasks.
8. Contain scope expansion: distinguish current deliverable, optional extension, and parked idea.
9. Delegate freely when objectives, interfaces, validation, and rollback are explicit; do not mistake governance needs for a desire to perform every step personally.
10. Challenge overbuilding, over-contextualization, analysis loops, and social blind spots candidly.
11. Under stress or decision overload, reduce branches and propose one concrete next action before offering more analysis.
12. Do not infer low empathy from cognitive-first empathy, low openness from practical rigor, change-aversion from production caution, or status motivation from assertiveness.
13. Do not flatter. Include weak suits and contrary evidence where material; avoid armchair diagnosis.

## Calibration vector — 2026-08-09

Scale endpoints are encoded in each key as `1_endpoint__10_endpoint`.

```text
exploration_1__closure_10=3
reversible_action_1__wait_for_strong_model_10=4
commit_at_threshold_1__continue_comparing_10=7
craft_driven_standards_1__error_avoidant_standards_10=2
conceptual_unknown_more_uncomfortable_1__operational_unknown_more_uncomfortable_10=3
advice_as_resource_1__advice_triggers_independence_10=4  # strongly contextual
verified_delegation_1__retain_direct_control_10=2
receptivity_first_1__precise_claim_first_10=7
perspective_understanding_first_1__emotional_accompaniment_first_10=3
solitude_or_small_circle_recovery_1__group_energy_recovery_10=3
private_mastery_and_impact_1__visible_status_and_recognition_10=3
abstract_conceptual_leisure_1__sensory_aesthetic_experiential_novelty_10=1
promotion_and_upside_1__prevention_and_safety_10=2
action_or_physical_recovery_under_stress_1__analysis_and_redesign_under_stress_10=9
stabilize_and_deepen_1__expand_capability_and_optionality_10=8
primary_project_stall=scope_expansion
secondary_project_stall=novelty_or_interest_drop
default_high_cost_correction_style=state_correction_directly_now
```

## Interpretation boundaries

Do not characterize Vegard as:

- naturally rigid, J-dominant, or routine-seeking;
- broadly change-averse;
- primarily fear-driven or criticism-driven in his standards;
- unwilling to delegate or needing hands-on control;
- reflexively oppositional to advice;
- globally ambiguity-intolerant;
- low-empathy solely because emotional accompaniment is not his default first move;
- status- or recognition-driven;
- obsessed with short answers;
- clinically classifiable from this profile.

The most accurate shorthand is:

> **INTP-A / Ti–Ne / very high Need for Cognition and Intellect / promotion-dominant expansion-maximizer / craft-driven high standards / verified-delegation systems architect / cognitive-first empathy / direct high-C–high-D communication / analysis-as-stress-control risk.**


---

# 7. Framework Handoff Contract

When personality materially contributes to a vacancy strategy, reference stable facet IDs rather than copying profile prose.

```yaml
personality_resonance:
  status: USED | NOT_USEFUL
  selected_facets:
    - facet_id: PF-##
      relevance: "<why this facet matters for this vacancy>"
      evidence_refs:
        - "<candidate factual authority reference>"
      desired_recruiter_read: "<specific useful interpretation>"
      misread_risk: "<specific downside interpretation>"
      prevention_rule: "<how evidence/framing prevents the misread>"
      expression_ceiling: "<strongest truth-safe implication>"
      channel_guidance: INTERNAL_ONLY | CV | APPLICATION | BOTH
  avoid:
    - "<vacancy-specific personality framing to suppress>"
```

Rules:
- Normally select **0–3** facets.
- `status: NOT_USEFUL` is fully valid.
- Evidence refs must come from factual candidate authorities.
- Do not pass MBTI/DISC/Enneagram/RIASEC labels to Terra by default.
- Do not copy failure-mode labels into employer-facing prose.
- Do not let personality create a claim that the factual authorities cannot support.
- Final Sol may remove all personality-conditioned material if it weakens credibility, naturalness, persuasion, or truth safety.

# 8. Retrieval / Context Index

| Need | Read first | Source escape |
|---|---|---|
| Fast overall orientation | §1 Canonical Runtime Compression | §6 full source profile |
| Vacancy-specific positioning | §2 Facet Index | §3 Facet Cards + §6 |
| Avoid stereotype/cosplay | §4 Anti-Inference Index | §6 Interpretation boundaries |
| Typology translation | §5 | §6 Framework translations |
| Communication/collaboration | §6 Communication profile + LLM collaboration contract | Full §6 |
| Failure-mode restraint | PF-15–PF-17 | §6 Failure modes and countermeasures |
| Motivation | PF-07, PF-20 | §6 Motivation and worldview |
| Work style/execution | PF-01–PF-05, PF-10–PF-12, PF-18–PF-19 | §6 Work and execution pattern |
| Calibration/uncertainty | §6 Calibrated trait architecture + calibration vector | Full §6 |
| Employer-facing use | §7 Framework Handoff Contract | Candidate factual authorities |

# 9. Compact Machine-Oriented Shorthand

```text
PERSONALITY = interpretive lens, not factual authority
ACTIVATION = SETTINGS.md toggle
DEFAULT STATE = unresolved
PRIMARY OWNER = Sol strategy
SELECTION = 0-3 stable facet IDs; zero is valid
GROUNDING = candidate factual authorities only
HANDOFF = desired recruiter read + evidence refs + misread + prevention + ceiling
TERRA = distilled guidance only; no raw typology/full profile by default
FINAL SOL = may suppress/reconstruct
TYPOLOGY = reference only
RISK PATTERNS = internal restraint, not employer-facing strengths
SOURCE ESCAPE = full canonical profile remains available
```

# 10. Human-Readable Canonical Shorthand

> **High-agency systems thinker; very high Need for Cognition and Intellect; exploratory Ti–Ne orientation; promotion/expansion motivated; craft- and integrity-driven standards; governance-based delegation; cognitive-first empathy; direct evidence-backed communication; rapid domain learning; leverage/tool-building orientation; with scope expansion, continued option search, and analysis-as-stress-control as primary counterweights.**
