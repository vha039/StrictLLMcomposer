# Identified framework enhancements — recommendations for adjudication

Prepared 2026-09-06. **Recommendations only.** Nothing here is approved, scheduled or implemented. The finalizing model adjudicates each item and folds the accepted ones into the final plans.

Companion: `User clarifications, optimizations, expansions, decisions and other user-work.md` holds the content-side decisions that are the user's to make. This file holds the engineering side.

**Adjudication standard.** Every item below must satisfy ED-1 (happy path, no defensive scaffolding), ED-2 (coordinated, not a micro-patch), ED-3 (large clusters, minimal batched validation) and MVP-KISS (semantically aggressive, mechanically simple), and must earn its place against the optimization order in root `AGENTS.md`: truthful package quality ≫ low human effort > simple robust implementation > model cost > reversibility. Where an item trades one against another, the trade is stated.

**Measured baseline.** Static input per two-job run is approximately **556,000 tokens** (Stage 1 ≈ 103.5k, Stage 2 ≈ 86.4k, Stage 3 ≈ 88.3k per job). Savings below are against that figure.

---

## Ranked summary

| ID | Enhancement | Saving / effect | Risk | Verdict |
|---|---|---:|---|---|
| FE-01 | Slim evidence-index view in the context bundle | ~114k tokens/run | Low | **Strongly recommend** |
| FE-02 | Read-§0-then-open-sections instruction for authorities | ~30–60k/run, behavioural | Low | **Recommend** |
| FE-03 | Stage-filtered writing policy and governing-hash scope | ~6k/run + removes forced Stage-1 regeneration | Medium | **Recommend, with care** |
| FE-04 | Deterministic vacancy page rendering for scanned sources | Operator effort | Low | **Recommend** |
| FE-05 | Slim baseline-map view | ~4k/run | Low | Recommend if FE-01 is taken |
| FE-06 | Evidence-digest section inside each authority | ~20–40k/run | Low | Recommend, pairs with FE-02 |
| FE-07 | Code authoring semantic fields | — | High | **Reject, with reasoning** |
| FE-08 | Knowledge graph over the authorities | — | High | **Reject, with reasoning** |
| FE-09 | Decision cache / job-archetype memory | — | High | **Reject as posed; safe variant is FE-06** |

---

## FE-01 — Emit a slim evidence-index view in the context bundle

**Strongly recommend.** This is the single largest token saving available anywhere in the framework, and it is pure transport.

**Observation.** `generated/evidence_index.json` is 75,431 characters (~22,900 tokens) across 144 entries, averaging 524 characters each. Every stage bundle points at it (`cli.py` `read.evidence_index`), so every stage of every job reads all of it. Per two-job run that is 137,400 tokens.

Each entry carries `evidence_id`, `source_id`, `kind`, `heading_path`, `line_start`, `line_end`, `content_sha256` and `source_stated_ids`. A writing model uses exactly two of those: the id, so it can cite correctly, and the heading path, so it knows what the id refers to. `content_sha256` alone is 64 characters × 144 = 9,216 characters of data the model can do nothing with.

**Proposal.** `cli.py` writes a slim projection alongside the existing bundle and points `read.evidence_index` at it — id plus heading path only, roughly 90 characters per entry:

~~~text
EV:WORK#023-4-4-prj-04-sykehusdekkende-rammeverk-for
  Arbeidserfaring > 4. Detaljert prosjektevidens > 4.4 PRJ-04 — Sykehusdekkende rammeverk for gevinstrealisering
~~~

The full index stays frozen, hashed and authoritative. `validate.py`'s reference resolution is unchanged and still reads the real file. Add `read.evidence_index_full` pointing at the frozen original so a model that needs line ranges can still open it.

**Effect.** ~19,000 tokens saved per stage per job. **~114,000 per two-job run, about 20% of total static input.**

**Risk.** Low. No schema change, no authority change, no instruction change, no validator change. The projection is derived, disposable and regenerated per bundle — the same category as the handoff.

**Adjudication notes.** The one question is whether the slim view should be written into `generated/` per run or emitted inline in the bundle JSON. Inline is simpler and avoids another disposable file; 13,000 characters inline is acceptable in a bundle that already carries paths and field lists. Recommend inline.

---

## FE-02 — Instruct stages to read authority §0 first and open detail sections on demand

**Recommend.** Zero machinery; an instruction change only.

**Observation.** All three stages read all 27,900 tokens of `Work_experience.md`, 9,600 of `Other_high_value_information.md` and 7,700 of `Education.md` for every job — 135,600 tokens per two-job run for `Work` alone. Each file already has a `§0 Runtime-kjerne` that functions as a decision surface: `Work §0.3` is a fourteen-row evidence-bridge table, `Other §0.2` is the route thesis, `Education §0.5` is the finance/process bridge.

**Proposal.** Add to each stage instruction's input rules: read `§0` in full, plus `Work §8` (approved metrics) and `§10` (forbidden and unresolved) always; open a project or course section only for records actually under consideration. Stage 3 additionally opens the sections behind every proposition it retains, which is the verification it must do anyway.

**Effect.** Behavioural, so not guaranteed, but plausibly 30–60k tokens per run. The larger benefit is attentional: a model ranking from a fourteen-row bridge table makes a cleaner selection than one scanning 1,085 lines.

**Risk.** Low, with one caveat the finalizing model must weigh: a stage that under-reads may miss a ceiling. Mitigated by making `§8` and `§10` mandatory reads, since those are where the ceilings live.

**Dependency.** Pairs with FE-06 and with the user's `§3`/`§4` cuts. If those cuts land, `§0` becomes a better digest and this instruction becomes more effective.

---

## FE-03 — Stage-filter the writing policy, and scope the governing hash to what each stage consumes

**Recommend, with care.** Small token saving, large workflow saving, and it repairs a known experimental-design defect.

**Observation, two parts.**

First: `FORFATTERSTEMME.md` declares `non_consumer: "Stage 1 (filen følger writing_policy-ruten, men strategi-instruksen peker ikke til den)"` in its own front matter. `manifest.py:221-223` collects all three writing policies by glob and hands the list to every stage. Stage 1 therefore reads 2,900 tokens it is explicitly told not to consume.

Second, and much more expensive: `manifest.py::stage_policy_sha256` folds **all** writing-policy records into **every** stage's governing hash, and `branch.py`'s `CONTENT_GOVERNING` lists `("writing_policy",)` for `strategy`, `draft_package`, `final_package` and `review` alike. A voice-only edit therefore invalidates Stage 1 and forces regeneration of strategy → draft → final on every job. This is documented as the reason the September runs were never a controlled voice-only A/B, and it makes every future voice iteration cost a complete three-stage rerun.

**Proposal.** Two coupled changes:

1. `cli.py` filters `read.writing_policy` by stage — Stage 1 receives doctrine and persuasion; Stages 2 and 3 receive all three.
2. `CONTENT_GOVERNING["strategy"]` references only the policies Stage 1 consumes, rather than the whole `writing_policy` list. `stage_policy_sha256` follows the same scoping.

**Effect.** ~5,800 tokens per two-job run directly. Indirectly, a voice-only change stops invalidating Stage 1, which avoids ~200k tokens of needless Stage-1 and Stage-2 rework per iteration and makes voice-only A/B testing possible for the first time.

**Risk.** Medium, and the finalizing model should weigh it properly. This changes manifest and branch semantics, which are load-bearing for reproducibility. Two specific considerations:

- The current over-broad hash is *conservative* — it never under-invalidates. Narrowing it is correct only if Stage 1 genuinely does not consume voice, which the file asserts and the Stage-1 instruction's routing table confirms. That assertion should be verified against the post-P0.9.3 Stage-1 instruction before implementing, because the base plan adds routing rows.
- Existing runs' hashes stay valid; this affects future freezes and branches only.

**Do not** implement this in the same cluster as the P0.9.3 semantic edits. It is independent and should be validated on its own.

---

## FE-04 — Deterministic page rendering for scanned vacancy sources

**Recommend.** Small, contained, uses an already-installed dependency, and removes a real operator burden.

**Observation.** Both `runb` vacancy PDFs yield zero extractable characters and are flagged `requires_source_inspection` with reasons naming the scanned pages. `vacancy.py` already detects this correctly. But the model must then render the pages itself to read them — in the last treatment run this meant writing ad-hoc PyMuPDF code inside the stage task. PyMuPDF is already a dependency (`.venv/Scripts/pymupdf.exe` is present and `render`/`pdf.py` use it).

**Proposal.** When `context` prepares a bundle for a job with `requires_source_inspection`, render the source PDF's pages to PNG under the run's existing `derived/` directory and list them in the bundle as `read.vacancy_pages`. Roughly fifteen lines in `cli.py` or `vacancy.py`.

**Effect.** No token saving; a genuine reduction in operator and model effort, which is priority 2 in the optimization order. It also removes a place where a stage writes ad-hoc code, which is a small correctness win.

**Risk.** Low. `derived/` is already model-writable run output. The pages are disposable and regenerated per bundle. Rendering failure must be non-fatal — fall back to the current behaviour of naming `read.vacancy_original`.

**Adjudication note.** Reject if the finalizing model judges that adding an image-producing side effect to `context` is scope creep. The counter-argument is that `context` already writes handoffs and return directories, and the alternative is every scanned-source stage reinventing the same code.

---

## FE-05 — Slim baseline-map view

**Recommend if FE-01 is accepted; otherwise marginal.**

`generated/baseline_map.json` is 6,972 characters (~2,100 tokens), read by Stages 2 and 3. Same pattern as FE-01 at one-tenth the scale: it carries hashes and structural metadata alongside the employment/education/language content the writer needs. A slim projection saves roughly 4,000 tokens per two-job run.

Worth doing as part of the same change as FE-01, since it is the same mechanism. Not worth a separate cluster.

---

## FE-06 — An evidence digest inside each authority, replacing the retrieval indexes

**Recommend.** This is the safe, non-prescriptive answer to the caching question, and it costs no machinery.

**Observation.** The user asked whether the framework should cache a "job archetype → strategy-stage evidence selected" mapping so that the relevant nuggets enter attention first. The goal is right; the proposed mechanism is not (see FE-09). What actually produces the effect is a compact, complete, decision-free view of *what evidence exists and what each record can prove* — read before the detail, not instead of it.

**Proposal.** Replace `Work §0.4`, `Other §0.4` and `Education §0.4` — the keyword retrieval indexes, which serve a retrieval system that does not exist — with a digest table in the same position:

~~~text
| Record | Lifecycle | What it can prove | Hardest ceiling | EV id |
|---|---|---|---|---|
| PRJ-03 | IN_USE | controlled modernisation to actual use under continuity constraints | not original author; no savings or quantified effect | EV:WORK#022-… |
| PRJ-04 | IN_USE | shared method adopted org-wide and still in use ~2.5 yrs later | one of four; no ownership, no measured effect | EV:WORK#023-… |
| PRJ-06 | CONCEPT | documented refusal of false precision; transparent proxy design | designed only; no implementation, adoption or ROI | EV:WORK#025-… |
~~~

Ten rows for `Work`, correspondingly fewer elsewhere. It is descriptive, contains no decisions and no history, and is derivable from content the files already carry — so it can be human-maintained or, if the finalizing model prefers, generated.

**Effect.** Combined with FE-02, plausibly 20–40k tokens per run, and a materially better ranking surface for Stage 1. It also puts `lifecycle` and the hardest ceiling adjacent to the id, which is exactly where the two observed defects went wrong.

**Risk.** Low. One caution: the digest must never become a substitute source for the letter. The `Do not copy` discipline that governs `Work §9` applies here and should be stated in the digest's own preamble.

---

## FE-07 — Code authoring semantic fields: **reject**

The user asked whether Python could take a nugget and write it verbatim into `strategy.json`, to save tokens and credits. I recommend rejecting this, and the reasoning matters because a weaker version of the idea will recur.

**Why it fails on architecture.** `paths.py::STAGE_WRITE_MAP` restricts each stage to its own artifact and the module comment states that widening it "is an architecture change, not a refactor." `INV-09` makes stage-scoped write ownership normative. Deterministic tooling authoring semantic content also crosses the mechanical/semantic boundary the specification draws.

**Why it fails on quality, which matters more.** The candidate fields are not quotations:

- `evidence_plan[].role` is a judgment about what a record proves *for this vacancy*. Two different vacancies produce two different `role` values from the same record. There is no verbatim source to copy.
- `claim_ceiling` looks copyable — the authority states ceilings — but it is a *per-vacancy* selection of which boundaries are live. Copying the authority's full ceiling text would create a second source of truth for ceilings and make the strategy's ceiling look authoritative when it is derived.
- `lifecycle` is the one field that looks genuinely mechanical. But a deterministic check that the model transcribed it correctly is a validator, and validators over semantic content are explicitly excluded.

**The adjacent thing that does work** is FE-06: put the lifecycle and the hardest ceiling next to the id in a digest, so the model reads them at the moment it decides rather than reconstructing them from prose. That captures the intent — correct values, less scanning — without deterministic authorship.

---

## FE-08 — Knowledge graph over the authorities: **reject**

The user asked whether the context files should be graphed. I recommend no.

The selection problem Stage 1 solves is *which evidence most reduces this employer's uncertainty*. That is a judgment about fit, not a traversal over relations. A graph would add a build step, a schema, a generator, a validator and a new class of staleness, and neither observed defect (`D1`, an invented activity; `D2`, an invented comparison) is a retrieval failure — both cite records that genuinely exist and are correctly resolved.

The genuinely graph-shaped information in the corpus — which record supports which requirement, and which records may be combined — is already expressed where it belongs: in `material_requirements[].evidence_refs` and in the cross-record integration rule. Those are per-vacancy, which is precisely why a static graph would not carry them.

Fails ED-1 and MVP-KISS. Not recommended at any point before P1.0.

---

## FE-09 — Job-archetype decision cache: **reject as posed**

The proposed mechanism — a central file recording "job archetype → strategy-stage evidence selected", read early so those nuggets enter attention first — should not be built, for four reasons that compound:

1. **It becomes a de-facto authority.** Anything read early and framed as prior success is treated as a prior. `Other §0.3` already forbids exactly this: *"bruk arbeidsgiverresearch, tidligere søknader, modellprosa eller minne som kandidatbevis."*
2. **It induces the convergence the framework is built to prevent.** `WRITING_DOCTRINE.md § Variasjon innenfor en klynge` and the employer-swap test exist because repeated generic wording and repeated evidence pairs are the observed failure mode. A cache optimises directly for repetition.
3. **The sample cannot support it.** Two vacancies do not define an archetype. Fitting a taxonomy to them would encode noise, and the same objection already caused public/private regime branching to be deferred.
4. **It re-creates the defect this pass is fixing.** The D1/D2 lesson is that pre-written prose entering a later stage gets treated as source. A decision cache is pre-written prose by design.

**What survives from the idea:** the goal of getting the right nuggets into attention early, which FE-06 delivers descriptively and without history. If the user still wants run-to-run memory after ten or more real vacancies, the safe form would be a **human-owned, read-after-selection divergence check** — the model selects independently, then compares against prior selections to notice unintended convergence. That is a different artifact with a different purpose and should not be built now.

---

## Interaction with the P0.9.3 plans

| Item | Interaction | Sequencing |
|---|---|---|
| FE-01, FE-05 | None. Pure transport, touches no policy or instruction. | Any time. Safe before the semantic clusters. |
| FE-02 | Adds input rules to the stage instructions the base plan is already rewriting. | **Fold into the base plan's Cluster 1**, so the instructions are edited once. |
| FE-03 | Touches `cli.py`, `manifest.py`, `branch.py`. Independent of semantics. | After the semantic clusters. Validate alone. |
| FE-04 | Touches `cli.py`/`vacancy.py`. Independent. | Any time. |
| FE-06 | Requires the user's `§3` cuts to have landed, since it replaces the retrieval indexes. | After the user's authority maintenance. |
| FE-07, FE-08, FE-09 | Rejections. No work. | — |

**One warning for the finalizing model.** FE-02 and FE-06 change what a stage reads. The base P0.9.3 plan specifies a two-job treatment from `T` whose purpose is to test the semantic correction. Changing the input surface in the same pass makes that a multi-variable test. Either fold FE-02 into the treatment deliberately and say so, or hold FE-06 until after the comparison. Do not let it happen by accident.

---

## Combined effect if all recommended items are accepted

| Source | ≈ Tokens saved per two-job run |
|---|---:|
| FE-01 slim evidence index | 114,000 |
| FE-06 + FE-02 authority digest and selective reading | 30,000–60,000 |
| User-approved context cuts (`§3`/`§4` of the user work package) | 40,000–55,000 |
| Instruction compression at the selective register | 35,000–45,000 |
| FE-03 stage-filtered policy | 5,800 |
| FE-05 slim baseline map | 4,000 |
| **Total** | **~230,000–285,000 of ~556,000** |

A 40–50% reduction in static input per run, with the largest single component being a transport change that touches no instruction, no schema and no authority.

The quality argument is separate and, by the optimization order, more important: a Stage 1 that ranks from a fourteen-row evidence digest with lifecycle and ceiling adjacent to each id is making a better-posed decision than one scanning 1,085 lines of mixed fact, routing metadata and retired prescription. The token saving is the second-order benefit.
