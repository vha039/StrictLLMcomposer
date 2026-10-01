---
document: "Jobbsøk_26 — Bounded architecture-optimization review (P0.8.1 control vs Brainstorm_Brief option space)"
artifact_role: "decision basis for a later frontier-model architecture-selection step"
status: "NON_NORMATIVE — no architecture selected"
language: "en"
inputs:
  - "Jobbsok_26_P0.8_architecture_and_specification.md (normative baseline)"
  - "Jobbsok_26_P0.8_1_review_refinement.md (CR-01..CR-25 hardening; NON_NORMATIVE_UNTIL_ADOPTED)"
  - "Brainstorm_Brief.md (~29.6k words; exploratory, not adopted)"
  - "prior conversation corrections, incl. verified Luna pricing (30 Jul 2026)"
objective: "net expected final framework value; truth as hard constraint"
---

# 0. Read contract

## 0.1 Epistemic labels

| Label | Meaning |
|---|---|
| `[OBS]` | Observation grounded in a supplied document or a verified conversation correction |
| `[INF]` | Inference / hypothesis from analysis; not verified |
| `[TEST]` | Claim that requires local evidence before it can drive an irreversible choice |
| `[NEW]` | Mechanism originated in this review, not present in BB or P0.8.1 |
| `[REPAIR]` | BB mechanism whose value depends materially on a modification introduced here — provenance split noted |

## 0.2 Disposition vocabulary

`PRESERVE` = serious survivor · `SALVAGE` = full proposal loses, named component survives · `FLAG` = no standalone survival, one named material interaction · `PRUNE` = insufficient on all three.
A `FLAG` is **not** a survivor. Reactivation requires: counterpart survived + interaction still material + could change a bundle.

## 0.3 ID normalization (required before any later model reuses BB identifiers)

`[OBS]` **BB contains an ID collision.** §8 numbers its context-centric mechanisms `Idea C-01 … C-32`; §19.6 independently numbers a different register `C-01 … C-15`. They are not the same series. Example: §8 `C-04` = global evidence indexing; §19.6 `C-04` = Source Escape Protocol.

**Normalization used throughout this document:**

- `CC-01 … CC-32` = §8 context-centric rough-draft ideas.
- `C-01 … C-15` = §19.6 context-architecture register (unchanged).
- All other series (`A-`, `P-`, `S-`, `F-`, `L-`, `V-`, `R-`, `O-`, `T-`, `B-`, `E-`, `DP-`, `A-FAM-`, `S-FMT-`) are unambiguous and retained.

`[OBS]` §19.6 is already a partial de-duplication of §8. Verified mapping (used to demonstrate coverage without re-analysing the same mechanism twice):

| §8 | Absorbed by | §8 | Absorbed by |
|---|---|---|---|
| CC-01 | L-02 | CC-17 | L-11 |
| CC-02, CC-03 | L-03 | CC-18 | L-12 |
| CC-04 | C-01 | CC-19 | L-13 |
| CC-05 | L-01 / F-07 | CC-20 | L-14 |
| CC-06 | C-14 | CC-21 | (own row) |
| CC-07 | (own row, late-binding) | CC-22 | T-3 |
| CC-08 | (own row, audit-of-model) | CC-23 | C-02 + ownership question |
| CC-09 | L-04 | CC-24 | (own row, `memory.md`) |
| CC-10 | L-06 | CC-25 | C-07 |
| CC-11 | L-05 | CC-26 | (own row, writer delta) |
| CC-12 | C-02 | CC-27 | C-12 |
| CC-13 | L-08 | CC-28 | T-4 / T-5 |
| CC-14 | C-13 | CC-29 | C-05 |
| CC-15 | L-09 | CC-30 | P-15 / C-30-equivalent |
| CC-16 | L-10 | CC-31 | T-5 |
| | | CC-32 | C-04 (inverse) |

Rows marked "own row" are dispositioned individually in §2.6.

---

# 1. Independent re-examination of P0.8.1 (before BB framing)

`[OBS]` P0.8.1 is a strong contract-hardening pass. CR-01..CR-25 correctly target the interfaces rather than the topology, and the four verified P0.7 defects are all addressed. Nothing below argues for topology redesign. What follows are **remaining optimization surfaces** found by reading P0.8+P0.8.1 on their own terms.

## OS-1 — `strategy.md` serves four consumers with one format and no schema

`[OBS]` The strategy artifact is simultaneously: (a) machine handoff to Terra; (b) human-inspectable design record; (c) decision ledger for final Sol; (d) evidence-provenance record feeding `used_evidence_refs`.

`[INF]` The recurring "Markdown vs JSON" debate (BB §12.7, Gemini, deep-research report) is a **symptom**, not the defect. The defect is that four consumers with different tolerance for ambiguity share one unvalidated surface. P0.8.1 §10.2 correctly rejects YAML frontmatter (duplicate truth), and correctly proposes stable labels + presence validator — but a presence validator does not resolve which consumer wins when a label is ambiguous.

`[INF]` The consumer-split reframing changes what a good answer looks like: the *decision core* (identity, headline hypothesis, evidence refs with claim ceiling + channel role, priority, elasticity band, counterfactual reserve) is machine-consumed and benefits from structure; the *employer decision model* is Sol-consumed reasoning and benefits from prose. A single artifact can hold both **only if one format is canonical** — hence S-FMT-2 or S-FMT-4, never S-FMT-3. This is the highest-value unresolved contract in the whole corpus. → `E-01`, §8.

## OS-2 — Freeze granularity is chosen on file-count aesthetics, not blast radius

`[OBS]` P0.8.1 CR-03 specifies one batch-level `context_snapshot.json` and explicitly rejects per-job authority hashes (§20.4) on redundancy grounds. BB F-11 proposes merging it into one `run_manifest.json`. BB F-19 separately proposes dependency-scoped invalidation.

`[INF]` Both documents debate *where the hashes live*. Neither resolves *what a hash change invalidates*. A single snapshot with an undifferentiated hash set forces a binary: blanket `RUN_CONTEXT_CHANGED` (P0.8.1's rule) or runtime dependency logic (F-19's risk of a state engine). → resolved by `N-01`, §5.

## OS-3 — CR-04 hardens a contract BB proposes deleting

`[OBS]` P0.8.1 CR-04 (P0) mandates `cluster_plan.schema.json` with exact set-equality. `cluster_plan.json` carries exactly two payloads: Priority A/B and processing order. BB F-05 proposes removing A/B; BB F-08 proposes human-fixed order.

`[INF]` If both BB proposals are adopted, `cluster_plan.json` carries nothing not already in `batch_plan.json`, and CR-04's schema work is wasted. **This cross-document dependency is stated in neither source.** CR-04 is therefore *conditional*, not unconditional-P0. Sequencing consequence: DC-6 (§3) must be decided **before** the builder implements CR-04.

## OS-4 — The 8-job pilot is being asked to be both baseline and experiment

`[OBS]` P0.8.1 §17.2 warns against using one 8-job `Q_happy` for routing decisions. BB §12.11 lists nine variables one pilot cannot cleanly separate. Both nevertheless frame the 8-job cluster as the primary learning event.

`[INF]` These are two different instruments. The 8-job run is a **product-viability observation** with n too small for inference. Anything introduced *into* it (personality layer, Luna prep, strategy JSON) destroys its value as the clean baseline against which everything later is compared. Therefore variables must be resolved by paired 2-job tests **before** the pilot, not after. This partially inverts BB §12.11's ordering. → §8.

## OS-5 — Portal contract cost is concentrated and severable

`[OBS]` P0.8.1 spends CR-08 + §8.2 resolving the portal hard/soft conflict. Portal logic additionally occupies: a `channel` enum branch, `portal_required`, question-ID uniqueness validation, word/char limit validation, portal output rendering, `PORTAL_ANSWER` review code, portal fixtures and tests, and portal constraints in all three stage instructions.

`[INF]` This is the single largest severable contract surface in the system, and CR-08's entire conflict is an artifact of coupling portal answers to the core package. Underweighted in BB relative to the Luna debate. → DC-1, §3.

## OS-6 — No metric attributes anchoring, and every proposed context mechanism claims to affect it

`[OBS]` P0.8.1 §11 correctly downgrades "candidate-blind" from isolation to a debiasing read-order protocol, and §11.3 proposes measuring it indirectly (strategy deltas, early/late, repeated openings). BB adds C-06 (Context Loss Budget) with eight sub-measures.

`[INF]` Eight sub-measures will not be recorded by hand during a manual chat workflow. A metric nobody logs is not a metric. → `N-02`, §5.

## OS-7 — Small residual contract ambiguities in P0.8.1 itself

| ID | Ambiguity | Consequence |
|---|---|---|
| OS-7a | `required_outputs` (CR-02) normalizes deliverable state, but P0.8.1 does not state whether `cv_overrides` remains mandatory when `CV ∉ required_outputs` | builder must guess; interacts with DC-1 |
| OS-7b | CR-13 defines READY/CHECK/RERUN by repair scope, but a package with a *known unsupported claim repaired by Stage 3* has no recorded trace | fact-correction rate becomes unmeasurable; `fact_correction_required` in §25.1 has no producer |
| OS-7c | CR-23 requires validator exit 0 before `completed`, but does not say what the model does on exit≠0 within the same chat (repair, skip, or fail the job) | recovery behaviour undefined at the most common failure point |

`[INF]` OS-7c is the highest-frequency of the three: schema failures on manually-produced JSON are expected to be the most common runtime event in the entire system.

---

# 2. Univariate disposition of BB

Depth is allocated by decision value. Terse rows are terse because the mechanism is dominated, already adopted in P0.8.1, or has no material bundle effect — not because it was skipped.

## 2.1 A — architecture and process philosophy

| ID | Disposition | Assessment |
|---|---|---|
| A-01 fresh build vs patch | PRESERVE (already P0.8.1) | `[OBS]` Consistent with P0.8.1 Wave A. No delta. |
| A-02 divergence–convergence | PRESERVE (meta) | Governs process, not architecture. This document is its convergence step. |
| A-03 compare untested designs on merit | PRESERVE (meta) | Correct posture; the brief's own instruction that absent pilot data affects confidence not veto is sound. |
| A-04 separate brainstorm from integration | PRESERVE (meta) | Explicit user requirement; respected here. |
| A-05 manual distinct chats | PRESERVE | Stable preference, unchallenged by any BB mechanism. |
| A-06 no hidden orchestrator/retry | PRESERVE | Hard boundary. Note: several BB mechanisms (F-19, C-03) drift toward it — see §6.3. |
| A-07 one job transaction at a time | PRESERVE | Highest-leverage single rule in the system; protects partial success, recovery and cross-job leakage simultaneously. |
| A-08 one cluster per stage chat | PRESERVE as empirical parameter | `[TEST]` Cluster size is the parameter, not the topology. |
| A-09 human irreversible boundary | PRESERVE | Non-negotiable. |
| A-10 real pilot over scaffolding | PRESERVE | Reinforced by OS-4. |

**Cluster verdict:** no A-series mechanism changes the architecture question. All are already P0.8.1-consistent. Zero pruned — this series is doctrine, not options.

## 2.2 P — personality / me-nizer

`[OBS]` This is the only BB domain with a **direct employer-facing quality theory** rather than an efficiency or hygiene theory. It therefore deserves the deepest univariate treatment.

**Core assessment.** `[INF]` The second-order convergence premise (§4.1) is plausible and unverified: skilled LLM users may converge on a shared "evidence-driven polished employer-specific" style, so first-order tailoring no longer differentiates. If true, personality-conditioned selection is one of the few remaining differentiation levers that does not require fabricating facts. If false, the layer adds context, risk and evaluation burden for nothing.

`[INF]` **The structural problem no BB section states: the personality layer is the only proposed mechanism whose failure mode is invisible to every existing metric.** Truth violations are caught by human review. Weak strategy surfaces as RERUN. Bad Norwegian surfaces as edit minutes. But "subtly performative / slightly cringe / trying too hard" produces a *lower human quality score with no attributable cause* — the operator scores 6 instead of 8 and cannot say why, because there is no counterfactual package to compare against. **Consequence: personality cannot be evaluated by observation; it can only be evaluated by paired comparison on identical jobs.** This is a hard constraint on when it may be introduced (§8, E-05).

| ID | Disposition | Assessment |
|---|---|---|
| P-01 `PERSONALITY.md` | PRESERVE | Vehicle for the whole cluster. Value is entirely conditional on P-02 + P-05 + P-07 holding. |
| P-02 not fact authority | PRESERVE — mandatory precondition | Without an explicit precedence line, a personality profile is a latent second candidate-fact surface. Non-optional if P-01 is adopted. |
| P-03 strategy-stage selection | PRESERVE | `[INF]` Correct placement argument: late enough to be vacancy-conditioned, early enough to be consequential. Superior to the "final-stage flavor" alternative it replaced. |
| P-04 2–4 facets | PRESERVE as parameter | `[TEST]` Number is arbitrary; the binding constraint is *expressed* facets (P-11), not *considered* facets. |
| P-05 evidence anchoring | PRESERVE — mandatory precondition | `[OBS]` BB itself names the failure: retrospective fitting (any evidence can be read as proving any facet). BB's control ("state what the evidence does not prove") is the right shape. |
| P-06 misread-risk mapping | PRESERVE, conditional | `[INF]` Genuinely novel and defensible for a Norwegian audience — but only where a real role-relevant downside exists. Applied universally it produces defensive prose. BB's own conditional framing (§4.6) is the correct form. |
| P-07 no jargon in output | PRESERVE — mandatory precondition | Trivial cost, prevents the worst failure mode (typology cosplay). |
| P-08 me-nizer framing | PRESERVE (conceptual) | Not a mechanism; the framing that keeps the cluster away from "humanizer"/anti-detection, which BB §12.13 confirms is not a useful target. |
| P-09 interest spark | PRESERVE | `[INF]` Highest variance item in the corpus: largest upside on recruiter memorability, largest downside on cringe. Its definition (§4.8) is unusually disciplined — employer problem + characteristic approach + real evidence + future usefulness — which is what separates it from an opening gimmick. |
| P-10 1–3 spark candidates | PRESERVE as parameter | Exploration count, not output count. → E-06. |
| P-11 one primary + ≤1 support | PRESERVE — mandatory constraint | Directly protects Single Backbone. Should be a hard writing rule, not a setting. |
| P-12 Stage 3 spark override | PRESERVE | Already consistent with P0.8.1 §2.4 Stage 3 freedom; costs nothing extra. |
| P-13 anti-convergence question | PRESERVE | One qualitative question at final stage; near-zero cost. Explicitly not an automated similarity check. |
| P-14 intensity setting | FLAG → S-01 | Only meaningful if a settings file exists. Not independently justified. |
| P-15 full profile on escape to final Sol | SALVAGE (component: escape access) | `[INF]` The general Source Escape Protocol (C-04) already covers this. A personality-specific escape is redundant with a general one. Salvage: *personality is in the escape-eligible set*. |

**Cluster verdict:** P-01/02/05/07/11 form an **indivisible minimum bundle** — adopting P-01 without any one of them converts an authenticity mechanism into an unsupported-claim generator. P-03/06/09/13 are the value-adding layer. P-04/10/14 are parameters. P-12 is free. P-15 collapses into C-04.

## 2.3 S — settings and compilation

| ID | Disposition | Assessment |
|---|---|---|
| S-01 `SETTINGS.md` | PRESERVE (minimal form) | `[INF]` Justified only if ≥2 settings genuinely need to vary during the experiment programme. Under the §8 experiment plan, exactly three do: context-prep on/off, personality on/off, strategy elasticity. A 3-key file is defensible; a 7-key file is knob-proliferation. |
| S-02 discrete labels | PRESERVE | Correct; avoids pseudo-precision. |
| S-03 evidence aperture | FLAG → L-01 / C-02 | Meaningless without a retrieval-breadth mechanism to control. |
| S-04 strategy elasticity | PRESERVE | `[INF]` The most consequential single setting: it directly parameterizes how much Stage 3 may reconstruct, which is P0.8's central quality bet. Deserves a real value even if all other settings are dropped. |
| S-05 spark count | FLAG → P-09/P-10 | |
| S-06 `PRIME_ROLE` toggle | PRUNE | `[OBS]` BB itself identifies this as Priority A/B under a new name (§5.2). Reintroduces the exact prediction/treatment confounding that F-05 exists to remove. Dominated. |
| S-07 one owner per setting | PRESERVE (design rule) | Cheap governance rule; prevents divergent interpretation across three stages. |
| S-08 model-compiled instructions | PRUNE for first release | `[INF]` Compilation frequency is very low (settings change between runs, not within them). BB §5.8 concedes the value is consistency not cost. A model compiler introduces drift-from-source risk, a cache-validity problem (S-09/S-12) and a version dependency to solve a problem that a static table solves. |
| S-09 deterministic hash/cache | FLAG → S-08 | Only needed if compilation exists. Falls with S-08. |
| S-10 Luna as settings compiler | PRUNE | Falls with S-08. |
| S-11 deterministic templating | SALVAGE → replaces S-08 | `[REPAIR]` The surviving component of the whole compilation idea: a static enum→instruction-fragment table, resolved at read time by the stage model reading `SETTINGS.md` alongside its stage instruction. No artifact, no cache, no compiler, no invalidation. |
| S-12 composite invalidation key | FLAG → S-08 | Falls with S-08. |

**Cluster verdict:** the settings *concept* survives in minimal form (S-01 + S-02 + S-04 + S-07 + S-11). The *compilation* sub-architecture (S-08/09/10/12) is pruned entirely — it is machinery to make a rarely-used file efficient.

## 2.4 F — product simplification

`[OBS]` Highest aggregate complexity-reduction density in the BB, and `[INF]` systematically underweighted relative to the Luna debate in BB's own conditional-merit summary (§34).

| ID | Disposition | Assessment |
|---|---|---|
| F-01 CV+application invariant core | PRESERVE (strong) | `[INF]` Invariance removes conditional branching from schema, stage instructions, finalizer, fixtures and tests simultaneously. The generality lost is generality the pilot was never going to exercise. |
| F-02 detached portal tool | PRESERVE (strongest single simplification) | See OS-5. `[INF]` Additional under-argued benefit: portal answers written *from an approved final package* are strictly better-grounded than answers written in parallel with the package, because the approved text is the source. Detachment is a quality argument, not only a scope argument. |
| F-03 remove channel enum | PRESERVE, dependent on F-01+F-02 | Supersedes P0.8.1 CR-02 rather than contradicting it: CR-02 normalizes to one `required_outputs` representation; F-03 observes that under invariance the representation is a constant. |
| F-04 `nb-NO` only | PRESERVE | Removes an enum branch and an unvalidated English style system. Reversible by explicit extension. |
| F-05 remove Priority A/B | PRESERVE (contested) | `[OBS]` P0.8.1 CR-18 keeps A/B and marks it confounded. BB proposes removal. `[INF]` The two positions are reconcilable: A/B's *ordering* function has value (distinct jobs early, similar jobs separated); its *differentiated-treatment* function creates the confound. Split them — see DC-6. |
| F-06 remove mandatory microvariation | PRESERVE | `[INF]` Duplicates spark exploration (interaction 11.5) and adds hidden treatment variance to the A/B confound. Weakly justified as a permanent rule; fine as a writer discretion. |
| F-07 human clustering standard | PRESERVE | Converges with P0.8.1 CR-24. Settled. |
| F-08 remove model cluster order | PRESERVE, conditional | Interacts with CR-04 (OS-3) and F-05. Decide together. |
| F-09 reduce cluster notes | PRESERVE | `[OBS]` BB §6.8 names the real risk: an unbounded "shared evidence surface" recreates P0.7's deleted `CLUSTER_EVIDENCE_BASE`. Content-limited form (convergence risks, terms that must stay distinct, outliers) is correct. |
| F-10 derive progress | SALVAGE (component: derive `remaining`) | `[INF]` `remaining` and `next` are derivable; `completed` and `failed` are not cheaply re-derivable without re-validating every artifact. Full derivation trades a small state risk for a per-continuation validation cost. Salvage the reduction, not the removal. |
| F-11 one run manifest | PRESERVE with modification | See `N-01`. The god-object risk BB names is real; the fix is field partitioning, not file splitting. |
| F-12 job-centric tree | PRESERVE | `[INF]` Aligns physical layout with the actual transaction and rerun unit (A-07). BB's stated cost — stage write boundaries become conventions — is already true in P0.8: stage isolation is enforced by instruction, not by filesystem permission. So the cost is largely notional. |
| F-13 atomic `final_result.json` | PRUNE (weak) | `[INF]` BB's own counter is decisive: package and review have different consumers and different update lifecycles (finalizer appends mechanical soft reasons to the queue without rewriting canonical review). Merging couples them for a file-count gain. |
| F-14 derived review queue | PRESERVE | Already P0.8 behaviour; BB correctly hardens "derived, never state". |
| F-15 trim release governance | PRESERVE | Converges with P0.8.1 Tier-2 deferral. Deterministic ZIP/member-count are release theatre before a product exists. |
| F-16 public CLIs + internal modules | PRESERVE | Identical to CR-21. Settled. |
| F-17 fixed dynamic CV surface | PRESERVE | `[INF]` Each additional dynamic zone multiplies render-source mapping, schema, page-balance risk and visual QA. Four zones is the right pilot surface. Directly protects CR-09's template source map from growing. |
| F-18 frozen document date | PRESERVE | `[INF]` Strong: a pure rerender must not silently change employer-facing content. Resolves BB §12.15 against the deep-research report's conversion-time proposal. |
| F-19 dependency-scoped invalidation | SALVAGE → `N-01` | Value is real (avoids both silent drift and blanket invalidation); BB's own risk ("becomes a state engine") is real. Salvageable only in static-table form. |

**Cluster verdict:** F is the highest-yield cluster. F-01/02/03/04/17 form a coherent **product-invariance package** whose combined effect is larger than any Luna configuration. Two prunes (F-13), two salvages (F-10, F-19).

## 2.5 L — Luna and context preparation

`[OBS]` **Verified pricing correction (30 Jul 2026):** Luna $0.20/M in, $1.20/M out; Terra $2.00/M in, $12.00/M out. Luna is ~10× cheaper than Terra on both axes.

`[INF]` **Explicit correction to my own prior-turn assessment.** In an earlier turn I argued against a Luna-heavy context-centric chain partly on the grounds that it "costs more tokens, not fewer." On dollar cost that was wrong: at these prices a cluster prep pass is cents. My other objections — anchoring, irreversible early filtering, weaker models determining what stronger models may later see, and model-role misallocation — are unaffected by price and remain the operative concerns. The binding constraint on Luna is **not money**; it is the 5-prompt user-load cap and the context/attention budget of downstream models.

`[INF]` **The decisive structural insight for this cluster:** BB §8.3 states the asymmetry (false inclusion = attention cost; false exclusion = decisive evidence unreachable) and uses it to argue for reversible tiers. It does not follow the asymmetry to its conclusion. If false exclusion is the expensive error, then **the optimal first-pilot prep output is a pure index with no relevance judgment at all** — an index has zero false-exclusion risk and near-zero anchoring risk, whereas tiers have both. And a lossless index over *stable* candidate authorities is deterministic: it can be built in code, once, and reused across every batch. **The highest-value component of the entire Luna proposal may require no model pass at all.** Only the *vacancy-conditioned* annotations genuinely need a model. → `N-03`.

| ID | Disposition | Assessment |
|---|---|---|
| L-01 five cluster Luna prompts | PRESERVE as toggleable experiment, not default | `[TEST]` Fits the 5-prompt cap exactly. Value unproven. Must be on/off-able (C-15) or it contaminates the baseline. |
| L-02 global Luna pass | PRUNE | `[OBS]` Costs a 6th prompt or distorts clustering to 4; duplicates PDF+extracted context at portfolio scale; BB itself rates it advisory/deferred. Dominated by `N-03` (deterministic index) for indexing and by F-07 (human) for clustering. |
| L-03 selective PDF cross-check | PRESERVE (triggered only) | `[INF]` Strong precisely because it is *triggered by deterministic extraction heuristics*, not run over all 40 vacancies. Verifies what the vacancy says; does not interpret. Low anchoring, high catch value for the one failure mode (silent extraction loss) that is otherwise invisible. |
| L-04 verbatim requirement map | PRESERVE, with BB's own caveat | `[INF]` Genuine clerical offload. Risk is context bloat via literal quotation — faithful compact normalization beats verbatim copying. Highest value for public-sector `kvalifikasjonsprinsippet` coverage. |
| L-05 candidate-source navigation | PRESERVE (highest-merit Luna task) | `[INF]` Robust for exactly the reason BB states: even a wrong Luna interpretation is harmless because Sol opens the source. Failure mode is bounded. But see `N-03` — much of this is deterministic. |
| L-06 linear evidence map | PRESERVE with caps | DIRECT/PARTIAL/ADJACENT/WEAK labelling; Luna maps, Sol ranks. Needs a hard row cap or it becomes the clutter it is meant to prevent. |
| L-07 obvious non-starter filtering | SALVAGE (component: label, never delete) | `[INF]` This is the mechanism the false-exclusion asymmetry most directly condemns. Survives only as `DUPLICATE`/`SUPERSEDED`/`OBJECTIVELY_INVALID` — objective, verifiable classes. Any relevance-based exclusion is pruned. |
| L-08 cross-source bridge matrix | PRESERVE, bounded | Vacancy/cluster-conditioned tables only. BB correctly flags the creep path to a claim graph. |
| L-09 claim-ceiling map | PRESERVE, Sol-reviewable | `[INF]` Directly serves the hard truth constraint — but note the asymmetric failure: a too-conservative ceiling causes *underselling*, which is a real quality loss the system has no metric for. Must be advisory. |
| L-10 lifecycle map | PRESERVE | Cheap, mechanical, directly prevents the pilot→production and proposed→delivered upgrades in the forbidden list. |
| L-11 actor/contribution map | PRESERVE | Supports `jeg`/`vi` calibration, which is a named Norwegian quality requirement. |
| L-12 contradiction register | PRESERVE, small | Focused fact-check surface; risk is false conflicts creating unnecessary caution. |
| L-13 cluster collision map | PRESERVE | Qualitative anti-convergence; the correct alternative to a similarity engine (R-19). |
| L-14 gap/uncertainty register | PRESERVE, paired with reframe | Must be paired with constructive objection/reframe or it becomes a pessimism checklist that suppresses persuasion. |
| L-15 personality candidates from Luna | PRUNE for first adoption | `[INF]` Compounds two unvalidated layers and makes attribution impossible (BB B-4 admits this). Also the highest stereotyping risk in the corpus. If personality is adopted, Sol selects. |
| L-16 spark seeds from Luna | PRUNE for first adoption | Same reasoning; additionally, a cheap model generating "memorable angles" is the most likely single source of gimmick output. |
| L-17 fail-open prep | PRESERVE — mandatory if any Luna | Non-negotiable precondition: prep must never become an availability dependency. |
| L-18 no direct Luna→employer prose | PRESERVE — mandatory if any Luna | Non-negotiable precondition. |
| L-19 Sol vacancy-first read order | PRESERVE — mandatory if any Luna | The primary anchoring control. Note `[INF]`: this is a *protocol*, not enforceable isolation — same epistemic status P0.8.1 §11 correctly assigned to candidate-blindness. Should be labelled identically. |
| L-20 Terra does not read raw prep | PRESERVE, with escape | Prevents prep bypassing Sol's filter; escape preserves recovery. |
| L-21 Luna writer test | PRESERVE as deferred experiment | `[TEST]` Legitimate later paired test (E-08). Not a first-release option: natural Bokmål is the named quality core. |
| L-22 Luna portal tool | PRESERVE — pairs with F-02 | `[INF]` Strong synergy: the detached portal task is bounded, direct, mechanically countable and sourced from approved text — exactly the L-05 role-selection profile. This is the *best* Luna use in the corpus and it lives outside the core. |
| L-23 Luna implementation worker | PRESERVE (out of product scope) | `[INF]` Materially relevant to the user's stated token-cost concern: after Sol Max fixes contracts, routine module/fixture/test generation is a strong Luna candidate. Affects build economics, not architecture. |
| L-24 Luna pilot summarizer | PRUNE (low value) | Post-hoc storytelling risk over a dataset of 8 rows. |
| L-25 bounded employer research | PRUNE for this release | Explicit opt-in only; scope/security expansion; no observed need. |

**Cluster verdict:** the Luna *layer* is a legitimate `[TEST]` candidate in one narrow configuration (L-01 + L-03..L-14 minus L-07's exclusion power, with L-17/18/19/20 as mandatory preconditions). The Luna *creative* extensions (L-15/16) and the Luna *global* pass (L-02) are pruned. Two out-of-core Luna uses (L-22, L-23) are strong and independent of the architecture decision.

## 2.6 CC — §8 context-centric rough draft (rows not absorbed by §19 registers)

| ID | Disposition | Assessment |
|---|---|---|
| CC-07 exclude personality/writing doctrine from early prep | PRESERVE (late-binding principle) | `[INF]` Strong and generalizable beyond Luna: literal extraction contaminated by a desired final story is worse than no extraction. Should be a stated principle even in a no-Luna architecture (it constrains Sol's own Phase A read order). |
| CC-08 second pass audits first pass | PRUNE | `[OBS]` BB's own critique is decisive: if the earlier pass is deterministic and non-destructive there is nothing semantic to audit. Model-review-of-model-summary is the anti-pattern the whole corpus warns against. |
| CC-21 evidence complementarity candidates | SALVAGE → folds into L-06/L-08 | Serves the "two proofs must demonstrate different things" rule; not a separate mechanism. |
| CC-24 `memory.md` exclusion filters | PRUNE (hard) | `[OBS]` No `memory.md` contract exists; archetype memory was explicitly parked by the user. This idea would reintroduce it *indirectly through filtering machinery* — the exact re-entry path BB warns about. |
| CC-26 writer delta | PRESERVE, minimal | `[INF]` Legitimate: the writer is the only actor that discovers whether a strategy is *realizable in prose*. Absent-by-default, ~200–300 words, only when writing exposes a strategic defect. Risk is essay creep; cap is the control. |
| CC-31/CC-28 Terra owns strategy+writing | PRUNE as default → see T-4/T-5 | Removes Sol from the highest-leverage decision point and converts final Sol into a repair model. Legitimate later economy experiment only. |

## 2.7 C — context architecture (§19.6)

| ID | Disposition | Assessment |
|---|---|---|
| C-01 lossless deterministic index | PRESERVE (strong) → `N-03` | `[INF]` The single best idea in the context cluster, and it needs no model. See §5. |
| C-02 reversible relevance tiers | PRESERVE, weakened | `[INF]` Survives only if tiers are *navigation recommendations with zero permission semantics* and the models are told so. BB's own risk statement — "downstream models may still treat labels as authority even when instructed otherwise" — is the crux, and it is unfalsifiable without a test. → E-02 must measure how often decisive evidence came from outside CORE. |
| C-03 Progressive Evidence Aperture | SALVAGE → collapses into `N-02` | `[INF]` The four-level status lifecycle (Luna tiers → Sol roles → Terra usage → final Sol disposition) is a state system for an auditing benefit obtainable from one field. See §5. |
| C-04 Source Escape Protocol | PRESERVE — mandatory for any filtering design | `[INF]` The single control that makes any context-reduction scheme safe. Elevates from "good idea" to *precondition*: no filtering mechanism may be adopted without it. Also absorbs P-15 and CC-32. |
| C-05 Counterfactual Reserve | PRESERVE | `[INF]` High value/low cost: one alternative route + trigger + reason-it-is-secondary. Gives Stage 3 a *bounded* reconstruction path instead of either blind acceptance or open-ended re-derivation. Directly operationalizes strategy elasticity (S-04). |
| C-06 Context Loss Budget | SALVAGE → `N-02` | Eight sub-measures will not be hand-logged in a manual workflow (OS-6). One field can carry the signal. |
| C-07 delta-only communication | PRESERVE (doctrine) | `[INF]` The correct answer to CC-25's cumulative-rewriting failure. Each stage writes only its unique contribution; no stage rewrites prior artifacts. |
| C-08 question-aware ordering | PRESERVE, low cost | Ordering context by decision function rather than source chronology is free if prep exists; meaningless if it does not. |
| C-09 non-authority header | PRESERVE — mandatory if any advisory artifact | 5 lines. Cheapest guardrail in the corpus. |
| C-10 job-local prep slices | PRESERVE | `[INF]` Resolves the real tension correctly via BB's own principle: *minimize authoritative objects, not disposable job-local views*. More files, smaller active context — and the file count is on derived, disposable artifacts. Synergises with F-12. |
| C-11 short cluster context | PRESERVE, capped | Same content-limit discipline as F-09. |
| C-12 no summary-of-summary | PRESERVE (doctrine) | `[INF]` The most important single doctrine for protecting truth in any multi-stage design. Should be stated in root instructions regardless of which bundle is chosen. |
| C-13 improved vacancy representation | PRESERVE, conditional | `[INF]` Only safe if canonical `vacancy.md` is unchanged and inference is *visibly* separated from quotation. Otherwise Luna's theory of the role silently replaces the employer's words. |
| C-14 global semantic labels | FLAG → C-01/`N-03` | Descriptive labelling without deletion; folds into the index. |
| C-15 context-prep toggle | PRESERVE — mandatory if Luna adopted | Without an OFF state there is no baseline and the Luna question can never be answered. |

## 2.8 V — artifact and validation

| ID | Disposition | Assessment |
|---|---|---|
| V-01 canonical strategy Markdown | PRESERVE (control arm) | Current P0.8.1 position. |
| V-02 canonical strategy JSON | PRESERVE (challenger) | See OS-1. `[TEST]` E-01 is the deciding test. Note `[INF]`: BB's strongest counter — schema encourages generic field-filling — is testable and is the thing E-01 must actually measure, not just parse-success. |
| V-03 generated Markdown view from JSON | PRESERVE if V-02 wins | Deterministic rendering, no model-written duplicate. Avoids the S-FMT-3 dual-truth trap. |
| V-04 standard artifact validator | PRESERVE | = CR-23/CR-21. Settled. |
| V-05 completion requires exit 0 | PRESERVE | = CR-23. Settled — but see OS-7c: the *repair* behaviour on exit≠0 is undefined. |
| V-06 mandatory current evidence refs | PRESERVE | = CR-12. Settled. |
| V-07 full bullet replacement | PRESERVE | = CR-11. Settled. |
| V-08 separate package/review | PRESERVE | Beats V-09; see F-13. |
| V-09 atomic final result | PRUNE | See F-13. |
| V-10 derived job context view | PRESERVE if manifest adopted | Good hybrid: canonical manifest + regenerable job-local view. |
| V-11 advisory Markdown context validator | PRESERVE if Luna adopted | Ref-existence, size, prohibited-content, job-ID. Explicitly not semantic. |
| V-12 dependency stale-state validator | SALVAGE → `N-01` | Same as F-19. |

## 2.9 R — rendering, security, testing

| ID | Disposition | Assessment |
|---|---|---|
| R-01 template spike before finalizer | PRESERVE (strong) | `[INF]` Sequencing insight underrated in P0.8.1: the Word master's real tag contract is discoverable only by opening it. Writing the finalizer first and discovering the template contract second guarantees rework. Should precede CR-09's source map being finalized. |
| R-02 one LO invocation per job | PRESERVE | = CR-19. `[TEST]` Q91: multi-document single invocation must be verified on the target Windows environment. |
| R-03 no persistent UNO | PRESERVE | Settled. |
| R-04 font/locale preflight | PRESERVE | `[INF]` Cheap and catches the one render failure class that is environment-dependent and otherwise silent (missing glyphs, wrong hyphenation). Not in P0.8.1 — genuine BB addition. |
| R-05 high-precision leakage scan | PRESERVE | = CR-07 Class A. Settled. |
| R-06 input safety envelope | PRESERVE (strong) | `[OBS]` Vacancy PDFs are untrusted external content. `[INF]` The layered form (file safety → fixed source wrapper → capability restriction → advisory flag → human boundary) is right, and the wrapper text is essentially free. P0.8 has "vacancy as untrusted data" as a principle; BB makes it operational. Genuine gap-fill. |
| R-07 advisory suspicious-content scan | PRESERVE as advisory only | `[OBS]` BB correctly rejects regex-as-classifier. Flag, never rewrite or block. |
| R-08 safe paths / no symlinks | PRESERVE | Implementation hygiene. |
| R-09 transactional output | PRESERVE | Settled. |
| R-10 soft page budgets | PRESERVE | Settled. |
| R-11 no auto-fit | PRESERVE | = P0.8.1 §9.4 DEFERRED. Settled. |
| R-12 visual QA | PRESERVE | Non-substitutable. |
| R-13 test tiers | PRESERVE | = CR-20. Settled. |
| R-14 one-job vertical slice | PRESERVE | = CR-20. Settled. |
| R-15 two-job smoke | PRESERVE | Settled. |
| R-16 eight-job pilot | PRESERVE, reframed | See OS-4: observation, not experiment. |
| R-17 paired one-variable A/B | PRESERVE (strong) | `[INF]` Elevated by OS-4: paired tests must *precede* the pilot for any variable that would contaminate it. |
| R-18 cross-cluster human spot-check | PRESERVE | = CR-22. Settled. |
| R-19 no n-gram hard gate | PRESERVE | Settled. |
| R-20 no semantic truth validator | PRESERVE | = CR-07 Class B. Settled. |

## 2.10 O / T / A-FAM / S-FMT — combinations, topologies, artifact families, strategy formats

| ID | Disposition | Assessment |
|---|---|---|
| O-0 no context model | PRESERVE — this is the control | Clean causal baseline, zero added prompts. |
| O-1 Luna Context Compiler Lite | PRESERVE | The only serious Luna configuration; exactly 5 prompts. |
| O-2 O-1 + personality/spark candidates | PRUNE | Confounds two unvalidated layers (= L-15/L-16). |
| O-3 global + cluster Luna | PRUNE | 6th prompt or distorted clustering; = L-02. |
| O-4 Luna + Terra hypothesis lab | PRUNE | +10 prompts, role overlap, anchoring, attribution loss. |
| O-5 Luna → Terra strategy+writer → Sol | PRUNE as default | Removes Sol from the initial backbone; later economy experiment only. |
| O-6 full context funnel | PRUNE | `[OBS]` BB itself rates it a weak standard-MVP candidate. Cascading filters, authority ambiguity, Sol arrives last. This is the configuration my prior-turn analysis argued against; that argument stands on non-cost grounds. |
| O-7 deterministic index + job-local Luna slices | PRESERVE (strongest Luna variant) | `[INF]` Superior to O-1: gets portfolio indexing with no global semantic model, keeps the 5-prompt cap, and reduces active context per job. → basis for `N-03` + C-10. |
| O-8 Luna as toggle only | PRESERVE (methodological) | = C-15. The correct adoption *procedure* for O-1/O-7, not a rival configuration. |
| T-0 Sol→Terra→Sol | PRESERVE — control topology | |
| T-1 Luna→Sol→Terra→Sol | PRESERVE | = O-1/O-7. |
| T-2 global+cluster Luna→S→T→S | PRUNE | = O-3. |
| T-3 Luna→Terra alternatives→S→T→S | PRUNE | = O-4/CC-22. |
| T-4 Luna→Terra strategy/writer→Sol | PRUNE as default | = O-5/CC-28. Deferred experiment. |
| T-5 Sol strategy+writer→Sol final | PRUNE | Loses Terra's output-heavy strength and doubles Sol cost with no quality theory. |
| T-6 Luna writer experiment | PRESERVE as deferred | = L-21/E-08. |
| A-FAM-1 current P0.8 | PRESERVE (control) | |
| A-FAM-2 lean manifest-centered | PRESERVE | With `N-01` partitioning. |
| A-FAM-3 context-augmented P0.8 | PRUNE | `[INF]` Adds files without removing old state — strictly worse than A-FAM-2 or A-FAM-4 on every complexity dimension. Dominated. |
| A-FAM-4 job-centric P0.9 | PRESERVE | = F-12 + C-10 + F-11. |
| S-FMT-1 canonical Markdown | PRESERVE (control) | |
| S-FMT-2 canonical JSON | PRESERVE (challenger) | |
| S-FMT-3 JSON core + MD rationale | PRUNE | Dual truth surface; the exact defect P0.8.1 §10.2 rejected YAML for. |
| S-FMT-4 JSON + generated MD view | PRESERVE if S-FMT-2 wins | = V-03. |

## 2.11 §28 parked register

`[OBS]` All sixteen §28 entries are already `DEFERRED` or `REJECTED` in P0.8.1 §20/§27 with matching rationale. **Convergence is complete; no disagreement exists.** Dispositioned as a block: 28.1 YAML (PRUNE, = P0.8.1 §20.1), 28.2 auto-fit (DEFERRED), 28.3 n-gram (REJECTED), 28.4 best-of-N (DEFERRED), 28.5 separate reviewer stage (REJECTED), 28.6 automatic semantic claim verification (REJECTED, = CR-07 Class B), 28.7 provenance platform/claim graph (REJECTED), 28.8 vector DB (REJECTED), 28.9 archetype memory (REJECTED), 28.10 outcome learning (REJECTED), 28.11 automatic employer research (DEFERRED), 28.12 auto rerun (REJECTED), 28.13 persistent LO service (DEFERRED), 28.14 render-aware semantic repair loop (REJECTED), 28.15 AI detector (REJECTED — BB §12.13 confirms detectors are not a useful target), 28.16 enterprise release platform (REJECTED).

`[INF]` One note worth carrying forward: 28.5 (separate reviewer stage) is the *only* rejected item whose activation criterion is plausibly reachable from pilot data — if Stage 3 shows systematic overconfidence (many READY, low human scores), the rejection deserves re-examination. Keep its activation trigger live.

## 2.12 DP-1..DP-7 decision packets

`[OBS]` BB's decision packets map cleanly onto the design-choice clusters below and are used as navigation rather than re-analysed: DP-1→DC-1, DP-2→DC-2, DP-3→DC-3, DP-4→DC-4, DP-5→DC-5, DP-6→DC-6, DP-7→DC-7.

---

# 3. Design-choice clusters

Each cluster is a set of mutually-constraining choices that must be decided together. Options are listed post-optimization (each optimized before judgement, per the brief).

## DC-1 — Product boundary

| Option | Content | Verdict |
|---|---|---|
| **1a** | CV + application invariant; portal detached (`L-22` tool); `nb-NO` only; no channel enum | **PRESERVE — strongest** |
| 1b | Keep portal in core with CR-08 hard-limit rule; keep channel enum | PRESERVE (control) |
| 1c | Keep portal, drop `nb-NO` multi-language | PRUNE — half-measure, keeps the expensive branch and drops the cheap one |

`[INF]` 1a dominates 1b on contract surface (removes ~8 distinct mechanisms), on OS-5's quality argument, and on CR-08's conflict evaporating. Its only real cost is that portal answers require a second workflow invocation — which the operator performs anyway, after approving the package. **Open risk:** `[TEST]` whether any approved vacancy in the actual 40 genuinely needs CV-only or portal-only. This is answerable today by inspecting the batch, not by a pilot. Resolving OS-7a depends on this.

## DC-2 — Authenticity layer

| Option | Content | Verdict |
|---|---|---|
| **2a** | No personality layer (control) | PRESERVE |
| **2b** | `PERSONALITY.md` + minimum bundle (P-01/02/05/07/11) + P-03 strategy-stage selection + P-09 spark, one primary | PRESERVE |
| 2c | 2b + P-06 misread mapping (conditional only) + P-13 anti-convergence check | PRESERVE |
| 2d | 2c + Luna-generated facet/spark candidates (L-15/16) | PRUNE — confounds two unvalidated layers |
| 2e | Full profile to all three stages (P-C) | PRUNE — three independent personality strategies; BB's own worst case |

`[INF]` 2b/2c cannot be introduced into the 8-job baseline pilot without destroying it (§2.2). They require a paired test (E-05) on identical jobs with blinded scoring.

## DC-3 — Context preparation

| Option | Content | Verdict |
|---|---|---|
| **3a** | None; Sol retrieves directly (control) | PRESERVE |
| **3b** | `N-03` deterministic index only — **no model pass, no added prompts** | PRESERVE — new dominant low-risk option |
| **3c** | 3b + O-7 Luna cluster prompt writing job-local slices (C-10), literal tasks only (L-03/04/05/06/08..14), tiers advisory (C-02), preconditions L-17/18/19/20 + C-04 + C-09 + C-15 mandatory | PRESERVE |
| 3d | O-1 single cluster prep file, no index | PRUNE — dominated by 3c on active-context grounds |
| 3e | O-3/O-6 global + cascading filters | PRUNE — see O-3/O-6 |

`[INF]` **3b is a new option not present in BB's combination space** and it changes the shape of the decision: BB frames context prep as "Luna or nothing." A deterministic index is strictly better than nothing at zero prompt cost and zero anchoring risk, which means 3a is no longer the right control for the Luna question — 3b is. Testing 3c against 3b (not against 3a) isolates *what the model adds beyond deterministic navigation*, which is the actual open question.

## DC-4 — Strategy artifact

| Option | Content | Verdict |
|---|---|---|
| **4a** | S-FMT-1 canonical Markdown, stable labels, presence validator (P0.8.1 position) | PRESERVE (control) |
| **4b** | S-FMT-2 canonical JSON with multiline prose fields + `C-05` counterfactual reserve + `S-04` elasticity band as fields | PRESERVE |
| 4c | S-FMT-4 = 4b + deterministically generated MD view | PRESERVE if 4b wins |
| 4d | S-FMT-3 JSON + model-written MD | PRUNE — dual truth |
| 4e | YAML frontmatter in MD | PRUNE — = P0.8.1 §20.1 |

`[INF]` The compression question (BB §6.17: 900–1400 → 400–1000 words) is **orthogonal to format and independently valuable**. A 1400-word strategy × 8 jobs = >10k words of strategy per cluster competing for downstream attention. Compression should be adopted in whichever format wins.

## DC-5 — State, provenance and runtime tree

| Option | Content | Verdict |
|---|---|---|
| **5a** | P0.8.1: `job_identity.json` + `context_snapshot.json` + 3× `progress.json`, stage-centric tree | PRESERVE (control) |
| **5b** | `N-01` partitioned manifest + job-centric tree (F-12) + derived job view (V-10) + reduced progress (F-10 salvage) | PRESERVE |
| 5c | 5b + full artifact-derived state, no progress files | PRUNE — trades small state risk for per-continuation revalidation cost |
| 5d | Unpartitioned single manifest | PRUNE — forces blanket invalidation or runtime dependency logic |

## DC-6 — Priority, order and cluster plan *(resolves OS-3)*

| Option | Content | Verdict |
|---|---|---|
| 6a | Keep A/B + model-generated order + `cluster_plan.schema.json` (P0.8.1 CR-04 + CR-18) | PRESERVE (control) |
| **6b** | **Split prediction from treatment:** keep ordering (distinct jobs early, similar jobs separated), remove differentiated treatment (no microvariation-for-A, no extra compute); A/B recorded as a *pure prediction label* for evaluation only | PRESERVE — **new hybrid** |
| 6c | Remove A/B and model order entirely; human-fixed order; delete `cluster_plan.json` and CR-04 | PRESERVE |
| 6d | Keep A/B treatment, randomize order | PRUNE — sacrifices operational convenience for a causal cleanliness the pilot's n cannot exploit anyway |

`[INF]` 6b is the reconciliation of P0.8.1 CR-18 and BB F-05/F-06: it retains the genuinely useful function (ordering reduces convergence and front-loads distinctness) while eliminating the confound (differentiated treatment). Under 6b, A/B becomes *falsifiable*: if predicted-A does not dominate the human top-80 when treatment is equal, the prediction is worthless and can be dropped. Under 6a it can never be falsified. Under 6c the question is never asked.

## DC-7 — Implementation sequence

`[OBS]` P0.8.1 §16.2/§23.3 (Wave A–H, vertical slice first, test tiers) and BB §33 converge almost completely. `[INF]` Two deltas from this review: **R-01 (template spike) should precede finalizer implementation**, and **paired experiments precede the 8-job pilot** for any variable that would contaminate it (OS-4).

---

# 4. Salvaged components and live interaction flags

## 4.1 Salvaged components (parent proposal pruned or weakened)

| From | Component retained | Recombined into |
|---|---|---|
| L-07 | Objective exclusion classes only (`DUPLICATE`/`SUPERSEDED`/`OBJECTIVELY_INVALID`) — never relevance-based | DC-3 (3c), `N-03` |
| S-08/09/10/12 | Static enum→instruction-fragment mapping (S-11), read at stage time | DC-2/DC-3 settings, no artifact |
| C-03 | Single "evidence used from outside prep" signal | `N-02` |
| C-06 | Same signal | `N-02` |
| F-10 | Derive `remaining`/`next`; retain `completed`/`failed` | DC-5 (5b) |
| F-19 / V-12 | Static invalidation-class table | `N-01` |
| P-15 | Personality is escape-eligible under the general protocol | C-04 |
| CC-21 | Complementarity check folded into evidence mapping | L-06/L-08 |
| L-02 | Portfolio-level indexing intent, delivered deterministically | `N-03` |
| CC-22/CC-26 | Writer-discovered strategy defects reported as a capped delta | CC-26 minimal form |

## 4.2 Live interaction flags (counterpart survived — reactivation warranted)

| Flag | Named interaction | Reactivate if |
|---|---|---|
| S-03 evidence aperture × DC-3 | Aperture is only meaningful if 3c adopted; under 3b it has no mechanism to control | DC-3 = 3c |
| P-14 intensity × S-01 | Only meaningful if both personality and a settings file are adopted | DC-2 ∈ {2b,2c} ∧ S-01 adopted |
| S-05 spark count × P-09/P-10 | Exploration parameter for spark generation | DC-2 ∈ {2b,2c} |
| C-14 global labels × `N-03` | Descriptive labels fold into the deterministic index rather than a model pass | DC-3 ∈ {3b,3c} |
| V-10 derived job view × F-11 | Only needed if manifest is canonical | DC-5 = 5b |
| V-11 context validator × DC-3 | Only needed if advisory prep artifacts exist | DC-3 = 3c |
| V-03 MD view × V-02 | Only if JSON becomes canonical | DC-4 ∈ {4b,4c} |
| 28.5 reviewer stage × Stage-3 calibration | Only if pilot shows systematic READY overconfidence | pilot signal |

## 4.3 Flags deliberately not retained

`[OBS]` Per the brief's instruction against vague speculative interactions: no flag is retained for L-15/L-16 (personality×Luna), O-2, O-4, T-3, T-5, A-FAM-3, S-FMT-3, S-06, F-13, CC-08 or CC-24. Each was pruned on standalone grounds *and* its only named interactions run to mechanisms that are themselves pruned or that gain nothing from the pairing.

---

# 5. Newly derived mechanisms

`[NEW]` These originate in this review. Where they repair a BB idea, the split is stated.

## N-01 — Invalidation-class partitioning inside a single freeze object

**Problem:** OS-2 / DC-5. One undifferentiated hash set forces blanket invalidation; per-dependency runtime logic (F-19) becomes a state engine.

**Mechanism:** keep exactly one canonical freeze object. Partition its hash fields into four **static classes**, and fix a table mapping class → stale scope:

| Class | Members | Stale scope on change |
|---|---|---|
| `SOURCE_TRUTH` | three candidate authorities, `CV_BASELINE`, vacancy hashes | all semantic outputs for affected jobs |
| `WRITING_POLICY` | writing standard, calibration, personality, stage instructions, settings | draft + final (strategy only if the policy contains strategy rules) |
| `RENDER_ASSET` | Word masters, font/locale environment | rendered files only |
| `SCHEMA` | schema files, spec version | validation only; no semantic rerun |

**Why this is not a state engine:** the mapping is a **constant table in the validator**, not runtime dependency inference. Output is a report (`VALID` / `STALE_JOB` / `STALE_CLUSTER` / `RERENDER_REQUIRED`), never an automatic action. No new file, no new stored state.

**Provenance:** F-11 (single object) + F-19/V-12 (scoped staleness) are BB; the static-class partition that makes them coexist without a state engine is new.

**Cost:** ~4 constants and one lookup. **Benefit:** a writing-standard tweak or a font change stops invalidating a whole batch's strategy work — the single most likely cause of avoidable rework in a multi-day manual run.

## N-02 — `evidence_outside_prep` — one field replacing an entire measurement subsystem

**Problem:** OS-6. C-03's four-level status lifecycle and C-06's eight sub-measures both try to answer one question: *did context reduction cost us decisive evidence?*

**Mechanism:** add to the final package one integer and one array:

```
evidence_outside_prep_count : int
evidence_outside_prep_refs  : [ref]     # refs used in the final package that
                                        # no upstream handoff surfaced
```

Since `used_evidence_refs` is already mandatory (CR-12) and prep/strategy refs are already recorded, this is a set difference the model can state honestly.

**What it measures simultaneously:** prep recall / false-exclusion rate (DC-3), tier aggressiveness (C-02), anchoring severity (L-19), Stage 3 independence (P0.8.1 §11.2), strategy elasticity realization (S-04), and the entire Context Loss Budget signal. Six BB concerns, one field.

**Limits:** `[INF]` self-reported, so it measures what the model *believes* it reopened; it is a diagnostic trend signal, not a proof. Still strictly better than eight unlogged sub-measures.

**Provenance:** repairs C-03 + C-06; the consolidation onto an already-mandatory object is new.

## N-03 — Deterministic candidate-evidence index (code, not model)

**Problem:** the highest-value Luna tasks (L-05 source navigation, L-02 indexing, C-01 lossless index, C-14 labels) are largely *deterministic over stable inputs*.

`[OBS]` The three candidate authorities change only through a deliberate fact-maintenance process. They are stable across an entire batch and across batches.

**Mechanism:** `ingest.py` (or a build-time step) emits one generated index over the authorities:

```
evidence_id | source_file | heading_path | section_hash | approx_size
            | lifecycle_label (if present in source) | claim-ceiling marker (if present)
```

No relevance judgement, no vacancy conditioning, no semantic annotation. Regenerated when `SOURCE_TRUTH` class changes (`N-01`).

**Consequences:**
- False-exclusion risk: **zero** (nothing is excluded).
- Anchoring risk: **near-zero** (no interpretation to anchor on).
- Prompt cost: **zero**.
- It gives every stage a stable addressing scheme for `used_evidence_refs`, which currently falls back to `source_file#heading` string matching — a known fragility in P0.8 §10.6.
- It converts the Luna question from "prep or no prep" into the sharper "**what does a model add beyond deterministic navigation?**"

**Provenance:** C-01/L-05/L-02 are BB (as *Luna* tasks); relocating the deterministic subset to code, and the resulting reframing of the Luna control condition, is new.

## N-04 — Stage-validator failure protocol *(resolves OS-7c)*

**Mechanism:** define the model's behaviour on validator exit≠0 explicitly, since this is the most frequent expected runtime event:

```
exit≠0 → read error → repair the artifact in the same chat → revalidate
       → max 2 repair attempts
       → on 3rd failure: record job in `failed` with the validator's error code,
         do NOT mark completed, continue to the next independent job
```

`[INF]` Bounded, visible, model-side repair. This is *not* the rejected automatic retry engine (28.12 / P0.8.1 §20.9): there is no hidden loop, no code-initiated retry, no orchestrator — it is an instruction to the model about what to do with an error it can already see. Without it, the most common failure has undefined behaviour.

## N-05 — Fact-correction trace *(resolves OS-7b)*

**Mechanism:** CR-13 requires Stage 3 to repair known unsupported claims before saving. Add one boolean to the review object: `upstream_claim_repaired: bool` (+ optional one-line note).

`[INF]` Without it, `fact_correction_required` in the pilot log (P0.8.1 §25.1) has no producer, and the single most safety-relevant Stage-3 behaviour — how often the draft contained an unsupported claim — is invisible. One boolean; also the natural activation signal for tightening Stage 2 instructions.

## N-06 — Explicit protocol-not-isolation labelling, generalized

`[OBS]` P0.8.1 §11 correctly relabels Stage 1 candidate-blindness and Stage 3 independent-view as *debiasing read-order protocols*, not isolation.

`[INF]` The same epistemic status applies to three BB mechanisms that are currently described in stronger terms: L-19 (Sol vacancy-first before prep), L-20 (Terra does not read raw prep), C-09 (non-authority header), and C-02 (tiers are navigation not permission). All four are *instructions the model may fail to follow*, unverifiable from the filesystem.

**Mechanism:** a single stated convention — any control of this class is labelled `PROTOCOL` (behavioural, measured indirectly) rather than `BOUNDARY` (mechanically enforced). Prevents the builder from writing tests that assert an unenforceable property, which is the same class of error as P0.7's `_DONE.md` substring check and BB/P0.8.1's shared warning about "keyword theatre" in stage-contract tests.

---

# 6. Multivariate analysis of survivors

## 6.1 Reinforcing sets (super-additive)

**M-1 · Product invariance stack (F-01+F-02+F-03+F-04+F-17):** compounding rather than additive. Invariance removes conditional branches from schema *and* stage instructions *and* finalizer *and* fixtures *and* the template source map simultaneously; F-17 then prevents the dynamic surface from regrowing. `[INF]` This is the largest net complexity reduction available and it carries no quality-loss theory — the removed capability is deferred, not lost.

**M-2 · Job-centric runtime (F-12 + C-10 + V-10 + N-01):** the job folder becomes the transaction unit, the rerun unit, the context-loading unit, the backup unit and the detached-portal-tool input unit at once. `[INF]` File count rises; *cognitive* complexity falls, because each added file is derived, disposable and job-local — exactly BB's principle "minimize authoritative objects, not disposable views."

**M-3 · Safe-reduction quartet (C-04 + C-09 + C-12 + N-03):** any context-reduction mechanism is safe only with all four. Source escape provides recovery; the non-authority header sets status; no-summary-of-summary prevents grounding drift; the deterministic index guarantees the primary sources remain addressable. `[INF]` **Adopting any filtering mechanism without all four is the single highest-risk move available in this option space** — it is precisely "weaker models determining what stronger models may later see."

**M-4 · Falsifiable priority (DC-6 6b + N-02 + pilot log):** separating prediction from treatment makes A/B testable within the pilot at zero added cost, converting an unfalsifiable policy into a decidable one.

**M-5 · Strategy handoff (DC-4 4b + C-05 + S-04):** if the strategy becomes structured, the counterfactual reserve and the elasticity band become *fields* rather than prose the writer may miss. `[INF]` This is the strongest argument for V-02 that BB does not make: JSON's value is not parse-safety, it is that it makes strategy elasticity and the alternative route mechanically present rather than rhetorically present.

## 6.2 Interference and redundancy

**X-1 · Sparks × microvariation (BB 11.5):** both generate alternative openings. Running both duplicates exploration and blurs attribution. `[INF]` Resolution: strategy owns *angle* candidates (P-09/P-10), writer owns *expression* only. F-06's removal of mandatory microvariation is therefore reinforced if DC-2 ∈ {2b,2c}.

**X-2 · Luna prep × strategy elasticity (BB 11.3):** the stated interaction is real and under-drawn. `[INF]` The failure mode: *tight* elasticity + prep filtering = prep errors become uncorrectable downstream, because Stage 3 is told to preserve strategy and Stage 1's strategy was built on a filtered view. **Constraint: DC-3=3c must not be combined with `elasticity=TIGHT`.** This is a genuine co-implementation hazard, not an additive cost.

**X-3 · Personality × Luna candidates (L-15/16):** confounds attribution completely — a lower human score cannot be assigned to the personality layer or to the cheap model's stereotyping. Already pruned; noted because BB B-4 proposes exactly this pairing.

**X-4 · Manifest × dependency invalidation (BB 11.7):** genuine tension; `N-01` resolves it by making the dependency mapping static.

**X-5 · Strategy JSON × final Sol reconstruction (BB Q56/Q number in §20.5):** `[INF]` under-analysed and potentially serious. A validated JSON strategy may *increase* Stage 3's reluctance to reconstruct, because a schema-valid object reads as an authoritative contract in a way prose does not. This directly opposes P0.8's central bet (Stage 3 free final authority). **E-01 must measure Stage-3 strategy-change rate, not only Terra's parse fidelity.** Under-measuring this is the most likely way E-01 gives a confidently wrong answer.

**X-6 · Compression × elasticity:** a compressed 400–700-word strategy carries less rationale; combined with elastic settings, Stage 3 has more freedom and less basis. `[INF]` C-05 (counterfactual reserve) is what makes compression safe — it preserves the decision basis that compression removes. Adopt together.

## 6.3 Drift-toward-forbidden-scope watch

`[INF]` Three surviving mechanisms have a credible path into explicitly-rejected territory. Each needs a stated stop line in whatever architecture is chosen:

| Mechanism | Drift path | Stop line |
|---|---|---|
| `N-01` invalidation classes | → runtime dependency inference → state machine (28.16 / A-06) | static table only; report-only, never triggers action |
| C-03/`N-02` evidence tracking | → evidence lifecycle platform → claim graph (28.7) | one count + one ref array; no per-claim provenance |
| L-08 cross-source bridges | → knowledge graph (28.7) | vacancy/cluster-conditioned tables only; not persisted across batches |

---

# 7. Candidate integration bundles

All bundles retain: Sol→Terra→Sol topology, three candidate authorities, dynamic CV merge, original Word masters, manual submission, human final semantic authority, no orchestrator/retry/vector-DB/judge. These are not in play.

**All bundles are options. None is a recommendation.**

## K-0 — Optimized P0.8.1 control

`[OBS]` Given equal optimization effort per the brief. This is **not** raw P0.8.1: it includes the P0.8.1 deltas *plus* the OS-fixes that require no new architecture.

- P0.8.1 CR-01..CR-25 as specified.
- **+** `N-04` validator failure protocol (OS-7c).
- **+** `N-05` fact-correction trace (OS-7b).
- **+** `N-06` PROTOCOL/BOUNDARY labelling convention.
- **+** `N-03` deterministic evidence index (no prompts, no model, stabilizes `used_evidence_refs`).
- **+** R-04 font/locale preflight; R-06 input-safety envelope + fixed untrusted-source wrapper.
- **+** R-01 template spike before finalizer.
- **+** strategy compression target (400–1000 words) without format change.
- **+** OS-7a resolved (state `cv_overrides` obligation explicitly).

**Material changes vs P0.8.1:** eight additions, all contract-level or sequencing; zero new stages, artifacts-of-authority or model passes. **Quality effect:** `[INF]` small positive (compression, index-stabilized refs). **Human load:** unchanged. **Implementation cost:** marginal over P0.8.1. **Failure modes:** unchanged from P0.8.1. **Reversibility:** full. **Uncertainty:** low — nothing here is speculative.

`[INF]` K-0 is a genuinely strong control. Several BB bundles do not beat it.

## K-1 — Lean product (K-0 + DC-1 1a)

Adds F-01/02/03/04/17 + L-22 detached portal tool + OS-5 resolution.

**Changes:** portal removed from core package, schema, stage instructions, finalizer, review codes, fixtures, tests; channel enum removed; `nb-NO` fixed; dynamic CV surface frozen at four zones. CR-08's hard/soft portal conflict disappears rather than being resolved.
**Quality:** `[INF]` neutral-to-positive — portal answers derived from approved final text are better grounded (OS-5).
**Human load:** one additional workflow invocation per job that actually has a portal; offset by a materially simpler core.
**Implementation:** **negative cost** — this is the only bundle that reduces build scope relative to the control.
**Failure modes:** a vacancy needing CV-only or portal-only is unhandled by the invariant core.
**Reversibility:** high — deferred capability, not deleted design.
**Uncertainty:** `[TEST]` answerable today by inspecting the real 40-vacancy batch, not by pilot.

## K-2 — Lean product + state consolidation (K-1 + DC-5 5b + DC-6 6b)

Adds `N-01` partitioned manifest, job-centric tree (F-12), derived job view (V-10), reduced progress (F-10 salvage), split prediction/treatment priority (6b), F-09 capped cluster notes; resolves OS-3 by deciding `cluster_plan`'s fate explicitly.

**Quality:** `[INF]` indirect — via less rework from over-broad invalidation and cleaner rerun.
**Human load:** lower per continuation and per rerun; one-time relearning of the tree.
**Implementation:** moderate — a fresh runtime layout inside an already-large build. This is the real cost.
**Failure modes:** manifest as god object (mitigated by `N-01`'s facts-and-fingerprints-only rule); stage write boundaries become conventional (already effectively true).
**Reversibility:** medium — tree layout is expensive to change after fixtures and tests exist.
**Uncertainty:** medium. → E-12 is a cheap implementation spike that de-risks this before commitment.

## K-3 — Deterministic-context bundle (K-1 + DC-3 3b + `N-02` + M-3 quartet)

Adds the deterministic index as an actively used navigation layer, the outside-prep signal, and the safe-reduction quartet (C-04 escape, C-09 header, C-12 no-summary-of-summary, plus `N-03`) — **with no model prep pass and no added prompts**.

**Quality:** `[INF]` plausible small positive (less Sol time on retrieval mechanics); genuinely unknown.
**Human load:** unchanged. **Prompts:** unchanged at 15.
**Implementation:** low — one generator + one field.
**Failure modes:** index goes stale (handled by `N-01` SOURCE_TRUTH class); index unused by models (measurable via `N-02`).
**Reversibility:** very high — a generated artifact nobody is forced to read.
**Uncertainty:** low risk, unknown benefit. `[INF]` This is the best risk-adjusted position on the context question and it is **not** in BB's combination space.

## K-4 — Context-prep experimental (K-3 + DC-3 3c, toggled)

Adds one Luna cluster prompt per cluster (+5 prompts, at the cap) producing job-local slices, literal tasks only, advisory tiers; L-17/18/19/20 + C-15 mandatory; constrained by X-2 (never with `elasticity=TIGHT`).

**Quality:** `[TEST]` unknown; both directions plausible.
**Human load:** +5 prompts; no new approval steps (L-17).
**Implementation:** moderate — prep contract, V-11 advisory validator, slice-writing rules, toggle.
**Failure modes:** anchoring; context bloat; false exclusion via tiers; prep duplicating Sol's work.
**Reversibility:** high **if and only if** C-15 toggle is built in from the start.
**Uncertainty:** highest of any bundle. → E-02, run against **K-3 as control**, not K-0.

## K-5 — Authenticity bundle (K-1 + DC-2 2c)

Adds `PERSONALITY.md` + minimum bundle + strategy-stage resonance + conditional misread mapping + one primary spark + anti-convergence check + minimal S-01 (intensity, elasticity).

**Quality:** `[TEST]` the only bundle with a *direct* employer-facing quality theory; also the only one whose failure is invisible to existing metrics (§2.2).
**Human load:** unchanged mechanically; higher review subtlety.
**Implementation:** low mechanically (one context file + stage-instruction sections); high in *evaluation* design.
**Failure modes:** cosplay; retrospective evidence fitting; defensive prose from over-applied misread control; personality becoming a latent fact surface.
**Reversibility:** high — remove the file and the instruction sections.
**Uncertainty:** high but **cheaply testable** via E-05 paired/blinded.

## K-6 — Structured strategy (K-1 + DC-4 4b/4c + C-05 + S-04 + compression)

**Quality:** `[INF]` ambiguous — plausible handoff gain vs the X-5 risk that a validated object suppresses Stage-3 reconstruction, which would attack P0.8's central quality bet.
**Implementation:** moderate — one schema, one validator, possible MD renderer.
**Reversibility:** medium — stage instructions and fixtures embed the format.
**Uncertainty:** high, and **E-01 is unusually cheap** (two jobs).

## Pruned bundles

| Bundle | Reason |
|---|---|
| BB B-9 full stack | `[OBS]` BB concedes it is untestable and un-attributable. Ten simultaneous changes. |
| BB B-2 settings-only | Knobs with nothing to control; without DC-2/DC-3 there are no settings worth having. |
| BB B-4 Luna+personality candidates | X-3 attribution collapse. |
| Any bundle containing O-3/O-4/O-6 | See §2.10. |
| A-FAM-3 context-augmented P0.8 | Adds without removing; dominated. |

## Bundle comparison

| | Prompts | Build cost vs K-0 | Quality theory | Reversibility | Decision-blocking uncertainty |
|---|---|---|---|---|---|
| K-0 control | 15 | — | indirect | full | none |
| K-1 lean | 15 | **lower** | neutral/positive | high | does the real batch need CV-only? |
| K-2 +state | 15 | higher | indirect | medium | E-12 spike |
| K-3 det. context | 15 | slightly higher | plausible | very high | none blocking |
| K-4 Luna prep | 20 | higher | unknown | high (if toggled) | E-02 |
| K-5 authenticity | 15 | low mech. / high eval | **direct** | high | E-05 |
| K-6 strategy JSON | 15 | moderate | ambiguous | medium | E-01 |

`[INF]` K-1 and K-3 are additive to each other and to K-5/K-6 and can be sequenced. K-4 should not be adopted before K-3 exists as its control. K-5 and K-6 should not enter the same pilot as each other.

---

# 8. Triaged uncertainty and minimal experiments

BB's 110 questions are consolidated by decision value. Superseded and low-materiality questions are disposed of as blocks rather than individually reproduced.

## 8.1 Must resolve before architecture selection (not by pilot)

| # | Question | Resolvable by |
|---|---|---|
| Q5, Q1 | Does any vacancy in the real 40 require CV-only or portal-only? | **Inspect the actual batch today.** Blocks DC-1 and OS-7a. |
| Q2 | Is portal detachment pilot-only or permanent? | Decision, not evidence. Blocks DC-1. |
| Q70/Q108 (partial) | Should A/B be prediction, treatment, both or neither? | Design decision (DC-6 6b makes it testable rather than resolving it). |
| Q71/Q76 | Does one manifest / job-centric tree simplify implementation? | **E-12 spike** — cheap, no models. Blocks DC-5. |
| Q83 | Validator as third CLI or subcommand? | Decision; CR-21 already implies subcommand/module. |
| Q84 | Same-chat repair after validator failure? | **`N-04` decides it by contract.** Resolved here. |
| Q21 | Which settings must exist before the first pilot? | Falls out of DC-2/DC-3: exactly the toggles the chosen experiments need. |

## 8.2 Best resolved by the smallest controlled test

| Exp | Question | Design | Decision it changes |
|---|---|---|---|
| **E-01** | Strategy format | 2 jobs, `strategy.md` vs `strategy.json`, identical Sol/Terra/Sol. Measure: format errors, **generic field-filling**, strategy length, Terra fidelity, **Stage-3 strategy-change rate (X-5)**, final quality | DC-4 |
| **E-05** | Personality layer | 2–3 jobs, paired, **blinded scoring**, same strategy inputs. Measure: authenticity, interest, cringe/overexpression, evidence defensibility, edit minutes | DC-2 |
| **E-02** | Model context prep | 2 jobs, **K-3 as control** (not K-0). Measure: `N-02` outside-prep count, Sol source openings, evidence recall, added context, final quality | DC-3 (3c vs 3b) |
| **E-12** | Manifest/tree spike | Implementation only, no models. Measure: code complexity, validation clarity, chat ergonomics, stale-state behaviour | DC-5 |
| **E-09** | Cluster size/order | **After** baseline exists. 8 vs 10, position effects | A-08 parameter |

`[INF]` **Sequencing constraint from OS-4:** E-01, E-05 and E-02 must run *before* the 8-job pilot, because each introduces a variable that would otherwise contaminate the only clean baseline available. They are 2-job tests; the cost is small relative to the value of an uncontaminated pilot.

## 8.3 Configurable / parameterizable — do not resolve by argument

Q9, Q14, Q16 (facet and spark counts), Q22 (aperture location), Q33 (prep size), Q45 (Luna effort), Q61–Q64 (cluster size), Q55 (elasticity encoding), Q96 (page overflow → CHECK). `[INF]` Each is a value in a small enum, not an architecture choice. Fixing them by argument now is negative-value.

## 8.4 Superseded or answered by newer evidence

| Questions | Status |
|---|---|
| Q25, Q105 | Superseded — model/effort/credits are `[VOLATILE]` per P0.8 §52; verified Luna pricing supersedes BB's own earlier figures |
| Q43, Q44 | Answered by pruning L-02/O-3 (6th prompt or distorted clustering) |
| Q26–Q30 | Answered by pruning S-08 (no compilation → no cache, no invalidation, no split) |
| Q10, Q35 | Answered by pruning L-15/L-16 (Luna does not see or generate personality) |
| Q37 | Answered by L-07 salvage: only objective classes qualify |
| Q86, Q87 | Answered by R-06/R-07: never rewrite vacancy text; no OCR in MVP |
| Q98 | Answered by F-18: ingest-frozen date |
| Q77 | Answered by F-13 prune: package and review stay separate |
| Q106 | Answerable mechanically once `N-02` + strategy-delta logging exist |
| Q110 | `[INF]` Out of scope — removing the final Sol stage is not in any surviving bundle |

## 8.5 Safely deferrable

Q3, Q6, Q109 (portal tool routing, employer research, Luna-as-writer); Q78/Q79 (`N-01` defers the state-engine question by construction); Q88 (product-surface permission enforcement); Q92–Q95 (render micro-optimizations beyond R-02/R-04); Q100–Q104 (pilot instrumentation detail, decidable when the pilot is scheduled).

## 8.6 Low materiality — dispositioned as a block

Q8 (framework internal consistency of the personality report), Q17–Q20 (spark judging philosophy), Q23, Q24 (answered by pruning S-06), Q34, Q39–Q42, Q46, Q47, Q50–Q54, Q57–Q60, Q65–Q69, Q72–Q75, Q80–Q82, Q85, Q89–Q91, Q97, Q107. `[INF]` These are either downstream of a cluster decision, restatements of a preserved mechanism's known risk, or questions whose answers do not change any bundle.

---

# 9. Completeness check

| Check | Result |
|---|---|
| Every materially distinct BB mechanism dispositioned directly or via explicit cluster mapping | **Yes.** Registers A(10), P(15), S(12), F(19), L(25), C(15), V(12), R(20) = 128 IDs individually dispositioned in §2.1–2.9. §8's CC-01..CC-32 covered via the §0.3 mapping table (26 absorbed) plus 6 individual rows in §2.6. O-0..O-8, T-0..T-6, A-FAM-1..4, S-FMT-1..4 in §2.10. §28's 16 parked items as a convergence block in §2.11 with one live activation trigger noted. DP-1..DP-7 mapped to DC-1..DC-7 in §2.12. B-0..B-9 addressed via §7 bundles and the pruned-bundle table. E-01..E-12 in §8.2 and §8.4. §11's ten interactions in §6. |
| No reactivation-worthy interaction silently lost when its counterpart survived | **Checked.** Eight live flags retained in §4.2 with explicit reactivation conditions; §4.3 states why no flag is kept for the eleven pruned mechanisms. X-2 (prep × tight elasticity) and X-5 (JSON × Stage-3 reconstruction) are surfaced as co-implementation hazards rather than left as flags, because both could change a bundle outcome. |
| Useful components from rejected proposals retained | **Yes** — ten salvages tabulated in §4.1; four of them (C-03, C-06, F-19, L-02) are load-bearing inputs to `N-01`/`N-02`/`N-03`. |
| P0.8.1 control received fair treatment | **Yes.** §1 examines P0.8.1 independently *before* BB framing and produces seven optimization surfaces of which four (`N-04`, `N-05`, `N-06`, OS-7a) are folded into K-0. K-0 is explicitly an *optimized* control, and §7 records that several BB bundles do not beat it. |
| Source proposals, repaired interpretations and new mechanisms distinguishable | **Yes** — `[REPAIR]` and `[NEW]` labels; every `N-` mechanism carries an explicit provenance line separating the BB contribution from the modification. §2.5 additionally records a correction to my own earlier-turn claim. |
| Bundles remain options, not an implicit decision | **Yes.** No bundle is recommended; the comparison table reports trade-offs without a ranking column; sequencing constraints are stated as constraints (K-4 needs K-3 as control; K-5 and K-6 not in one pilot), not as a plan. |
| Material epistemic distinctions preserved | **Yes** — `[OBS]`/`[INF]`/`[TEST]` applied where the distinction affects a decision. Notably: Luna pricing is `[OBS]`; every Luna *benefit* claim is `[TEST]`. |
| Later architecture-selection model need not reprocess BB | **Yes** for disposition, rationale, clusters, interactions, bundles and triage. **Exception to re-open only if needed:** BB §23 (Norwegian writing doctrine) and §24 (external-evidence ledger) are *content* rather than architecture options; they are unchanged from P0.8's `WRITING_STANDARD` inputs and were not re-litigated here. |

---

# 10. What this analysis does not settle

`[INF]` Stated plainly so the next step is not over-read:

1. **No bundle is selected.** K-0 through K-6 are options with different risk shapes.
2. **The Luna question remains open** — but its shape changed: `N-03` makes "deterministic navigation" the right control, not "nothing."
3. **Personality remains the highest-variance and least-measurable proposal.** Its adoption question is inseparable from its evaluation design.
4. **Strategy format remains genuinely undecided**, and X-5 identifies a way E-01 could give a confidently wrong answer if it measures only parse fidelity.
5. **Every quality claim in this document about an unbuilt mechanism is `[INF]` or `[TEST]`.** No pilot has run. The largest single reduction in uncertainty available is still the first real cluster, and nothing here changes that.
