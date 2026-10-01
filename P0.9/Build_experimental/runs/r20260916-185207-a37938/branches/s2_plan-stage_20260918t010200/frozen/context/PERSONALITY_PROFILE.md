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
runtime_status: "ACTIVE"
settings_control: "policy/settings.toml::[personality]"
default_toggle_state: "ON"
primary_consumers: ["Stage 1 decision architecture", "Stage 3 final writer and review"]
restricted_consumers: ["Stage 2 (ADVOCATE) writer: distilled selected-facet guidance only"]
not_intended_for:
  - "Direct employer-facing insertion"
  - "Independent factual claim creation"
  - "Automatic psychometric diagnosis"
  - "Automatic personality generation by any preparation pass"
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
control: policy/settings.toml [personality]
state: ON
max_facets: 3
```

Personality is ON in the P0.9 baseline (`DEC-35`). There is no OFF switch:
the valid null outcome is Stage 1 selecting **zero** facets, which step 9
below already permits. Normal Stage-1 behavior is:

1. Understand vacancy and employer decision problem **before** personality-conditioned selection.
2. Inspect factual candidate authorities.
3. Consult the facet index below.
4. Select **0–3 facets** only when they materially sharpen the candidate case.
5. Bind every employer-facing implication to factual evidence from candidate authorities.
6. Record desired recruiter interpretation, misread risk, prevention rule, and expression ceiling.
7. Give the Stage-2 writer only distilled selected-facet guidance; do **not** pass the full profile or raw typology by default.
8. The Stage-3 final writer may retain, reduce, suppress, replace, or ignore personality-conditioned guidance.
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

# 3. Facet Cards

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

# 6. Canonical Full Source Profile

# 7. Framework Handoff Contract

When personality materially contributes to a vacancy strategy, reference stable facet IDs from `policy/personality_facets.json` rather than copying profile prose. That file is the canonical closed facet set; the former prose index and facet cards are retired.

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
- Do not pass MBTI/DISC/Enneagram/RIASEC labels to the Stage-2 writer by default.
- Do not copy failure-mode labels into employer-facing prose.
- Do not let personality create a claim that the factual authorities cannot support.
- The Stage-3 final writer may remove all personality-conditioned material if it weakens credibility, naturalness, persuasion, or truth safety.

# 8. Retrieval / Context Index

# 9. Compact Machine-Oriented Shorthand

# 10. Human-Readable Canonical Shorthand
