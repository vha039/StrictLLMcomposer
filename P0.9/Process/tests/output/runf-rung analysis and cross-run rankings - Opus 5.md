# Batches `runf` and `rung` — package review, cross-run rankings and a revised optimisation plan

**Runs:**
- `r20260914-211650-5d3516` (`runf`, 4 jobs)
- `r20260914-211651-5dbd38` (`rung`, 4 jobs)

Both are P0.9.3 two-stage runs, frozen one second apart and run in parallel. `r20260914-210959-66cf95` (`rune`, the same 8 jobs as one cluster) was frozen seven minutes earlier and abandoned before Stage 1.

**Models:** both new ledgers record `stage1 = SOL_CLASS = "Codex / GPT-6 Astra (High)"` and `stage3 = TERRA_CLASS = "Claude Opus (High)"`. The operator says the ledger is wrong. This report therefore treats `runf` and `rung` as two blind arms and never infers which model wrote what.

**Compared against:**
- `rund` (`r20260913-205507-247618`, 12 jobs; operator-stated Terra xhigh on Stage 1 and Opus 5 medium on Stage 3);
- the earlier Avinor/Huseierne corpus (0.9.0–0.9.3, including branches);
- the nine-package ranking, the curated package and its interview model;
- the previous report, `rund batch analysis - r20260913-205507-247618 - Opus 5.md`.

**Prepared:** 2026-09-15. Nothing in `P0.9/Build` was modified.

---

## 0. TL;DR

1. **This is a clean experiment.**
   - Every one of the 26 frozen inputs is byte-identical to `rund` except `settings.toml`, which differs only in the stage role label and the model mapping. That covers the stage instructions, all three writing policies, the authorities, masters, template map, evidence index and baseline map.
   - None of the previous report's edits (E-1…E-11) had been applied.
   - What changed is therefore the model and effort, the chat size (4 jobs instead of 12) and the vacancy mix.
2. **The packages are clearly better.**
   - On the six vacancies both runs share, the new packages beat `rund` by **+6.9 percentage points** on the interview-odds index (nominal scores, 30.2 against 23.3). The Monte Carlo, which also samples the size of the tail-only CV penalty, puts the gain at +8.3 points (90% interval [+6.1, +10.5]), positive in 100% of 4 000 draws.
   - The letter moved most: its calibration sub-score rose by **+27 points** on average.
   - **0 of 8** letters volunteer a limitation (`rund`: 10 of 12), and 0 carry the self-disqualification knock-out cue (`rund`: 8 of 12).
   - Truth held everywhere. A targeted truth pass found no fabrication and one ownership-verb slip.
3. **This corrects my previous report.**
   - With identical policy text, stronger models did not write gap sentences. They also kept gaps out of `top_employer_problems` (0 of 8, against 11 of 12) and recovered cross-cutting recall.
   - Volunteered limitations (T1) and the recall collapse (T2/T3) were therefore **mainly cheap-model effects**, not effects of K rule 5, the content lock or the Stage-3 asymmetry.
   - E-1, E-5 and E-10 become cheap-tier guardrails.
   - E-4 must be **reworded, not applied**. The "overclaim is worse" guard did real work here: Stage 3 caught four Stage-1 overstatements.
4. **The new top defect is CV capacity.**
   - 3 of 4 `runf` CVs render to three pages (522–533 words of profile and bullets). Page 3 holds only KURS and REFERANSER, two to four lines.
   - Under the interview model this costs about a quarter of the odds, and it takes about 30 seconds to fix.
   - Fixed, `runf` is the strongest arm on the index (32.6).
5. **Arm league table (execution index, which ignores how well the candidate fits each vacancy):**
   - `rung` **30.9**: zero knock-out cues and the cleanest mechanics.
   - `runf` **27.2**: the richest CVs and the best letters (mean 82.9), pulled down by the page overruns.
   - Earlier Avinor corpus (9 packages): **25.5**.
   - `rund` **23.2**.
   - The human-curated package scores **33.2**.
   - `rung` versus `runf` is not a robust difference (P = 0.75).
6. **Rankings:**
   - Best execution: `rund` BI 35.5, `runf` Tieto 34.1, `rung` EIE 33.2, `rund` Statnett 33.0.
   - Best by expected interview chance, adjusted for fit: `rund` Statnett 38.1, `rung` Abacus 32.9, `rung` EIE 32.1, `rund` BI 31.9.
   - Head-to-head, the new package wins 5 of 6 shared vacancies. BearingPoint goes to `rund` until the `runf` CV is compacted; after that `runf` wins.
7. **Residue that persists across all three arms is harness-, source- or template-shaped:**
   - READY 20 of 20, with apply/no-apply nudges.
   - An invitation close in every letter.
   - "Jeg søker … fordi" in 18 of 20 letters.
   - A new transfer-bridge formula ("Den … vil jeg ta med inn i …") in 8 of 8. This is K's *positiv overføringsbro* made literal, and the content lock protects it.
   - Status sentences verbatim in both documents, bold support sections, CV bullets ending on "avviklet", and headline wraps (5 of 8).
8. **Five harness defects found this time:**
   - **FORFATTERSTEMME's own example «Jeg moderniserte verktøyet»** models the ownership claim that WORK §4.3's ceiling forbids ("sole ownership of the complete modernization"). The verb recurs as "Moderniserte …" (`runf` Tieto CV, `rund` KPMG CV) and "har modernisert" (`rung` Norwegian Stage 1).
   - **The WORK §0.3 BAR digest row** reads as if Vegard quality-assured others. The source says Vegard's own work was quality-assured at first. `runf`'s Stage 3 caught this in 4 of 4 jobs.
   - **Documentation voice from the authority** ("avhang av økonomilederens kapasitet") leaked into the Stortinget package in both `rund` and `rung`.
   - **No rule on grammatical person in the CV:** two `rung` profiles are written in the first person.
   - **Triage is set before render, and the queue does not surface page warnings.** Renaming the PDFs also turned three jobs into `render: FAILED` in the queue.
9. **Operator notes:**
   - The ledger is wrong again, and the stage-3 role label was changed. That alters the Stage-3 policy fingerprint although the Stage-3 text is identical.
   - The Norwegian ad is in English and was run as CORE; settings say non-Bokmål vacancies are EXCEPTION. Norwegian and Visma both take a CV upload only.
   - The Stortinget deadline was 14.09.
   - Five CV PDFs were renamed after render. They are byte-identical to the receipts.
10. **Plan:**
    - **Now:** compact the three CV tails, fix the ownership verb, trim headlines, choose the version to send per vacancy (§5.7).
    - **Before any policy edit:** run a **2×2 branch test**, crossing the Stage-1 strategies with the Stage-3 models on 3–4 shared jobs, to find which stage carried T1.
    - **Cheap fixes:** deterministic changes (tail compaction, un-bolding, page warnings in the queue); source maintenance (the §0.3 row and the BAR phrase); the V example swap; variation and bridge wording; a CV person rule.
    - **Keep 4-job chats, and record the true model mapping at freeze.**

---

## 1. Run anatomy

### 1.1 Batches and timeline

All eight jobs are CORE and HIGH. Times are local, measured from handoff creation to the last return file, so they include operator latency.

**`runf` (`5d3516`, frozen 23:16:50)**

| # | Job | Stage 1 | Stage 3 | Render | Pages CV/letter |
|---|---|---|---|---|---|
| 1 | Tieto Tech Consulting, Prosjektleder & Endringsleder | 23:19→23:30 (11.2 min) | 23:39→23:47 (7.5) | OK | 2/1 |
| 2 | BearingPoint, Konsulent forretning/teknologi | 23:31→23:37 (5.9) | 23:47→23:52 (4.9) | OK | **3**/1 |
| 3 | Amesto Accounthouse, AI Team Lead Transformasjon | 23:37→23:43 (6.3) | 23:53→23:57 (3.7) | OK | **3**/1 |
| 4 | Visma Enterprise, Product Manager | 23:44→23:50 (6.0) | 23:57→00:00 (2.8) | OK | **3**/1 |

**`rung` (`5dbd38`, frozen 23:16:51)**

| # | Job | Stage 1 | Stage 3 | Render | Pages CV/letter |
|---|---|---|---|---|---|
| 1 | Stortinget, seniorrådgiver/rådgiver (deadline **14.09**) | 23:21→23:25 (3.9) | 23:33→23:40 (7.0) | OK | 2/1 |
| 2 | Norwegian Air Shuttle, Senior Manager Digital Governance Operations | 23:25→23:28 (3.0) | 23:41→23:45 (4.0) | OK | 2/1 |
| 3 | EIE eiendomsmegling, Systemkoordinator | 23:29→23:34 (4.9) | 23:45→23:48 (2.7) | OK | 2/1 |
| 4 | Abacus IT, ERP-rådgiver | 23:34→23:36 (2.6) | 23:48→23:51 (2.2) | OK | 2/1 |

**Throughput**

| Arm | Stage 1 per job | Stage 3 per job | Total per job | Relative to `rund` |
|---|---:|---:|---:|---:|
| `rund` | ≈1.1 min (after job 1) | ≈2.3 min | ≈3.4 min | 1.0× |
| `runf` | 7.4 min (6.1 after job 1) | 4.7 min | ≈12.1 min | ≈3.6× |
| `rung` | 3.6 min | 4.0 min | ≈7.6 min | ≈2.2× |

**Observations**

- **The two chats ran side by side.** Stage 1 ran in both chats between 23:19 and 23:50. Stage 3 overlapped between 23:39 and 00:00. Renders interleaved, and Word COM completed all 16 documents without a collision.
- **Stage-3 time falls steadily inside each chat.** `runf` went 7.5 → 4.9 → 3.7 → 2.8 minutes; `rung` went 7.0 → 4.0 → 2.7 → 2.2. Later jobs reuse the context of earlier ones. That makes them cheaper, and it is also the mechanism behind within-chat formula convergence (§6.3, N2).
- **Stage-1 time stays flat inside each chat.** Strategy size does not shrink with sequence either: `runf` 44 → 40 → 41 → 37 KB; `rung` 20 → 22 → 17 → 19 KB. The monotone decay seen in the 12-job `rund` chat (17 → 9 KB) is absent.
- **`rune` was replaced by the segmentation my previous report recommended.**
  - `rune` froze the same 8 jobs as one cluster at 23:09:59. Its folder holds only the derived vacancy views.
  - Seven minutes later the same jobs were frozen as two 4-job clusters and run in parallel.
  - The split is not random. `runf` got the consultancies and the product role (Tieto, BearingPoint, Amesto, Visma). `rung` got the staff, operations, systems, ERP and governance roles (Stortinget, Norwegian, EIE, Abacus). **`runf` versus `rung` is therefore confounded with vacancy type**, and the clean comparisons are the paired ones against `rund`.

### 1.2 Provenance: what the frozen inputs prove

**Frozen-input diff (26 entries; `rund` → `runf`/`rung`)**

| Input | `rund` | `runf` | `rung` |
|---|---|---|---|
| Stage instructions, writing policies (D, K, V) | identical | identical | identical |
| Authorities, CV_BASELINE `c52b1631`, personality profile and facets | identical | identical | identical |
| Evidence index `bd151997`, baseline map `a73fefbc`, template map `84a069c3`, masters, schemas | identical | identical | identical |
| `settings.toml` | `28b78a74` | `969b04bb` | `969b04bb` |

**The whole `settings.toml` diff:**
```
- stage3 = "SOL_CLASS"    # Elastic Final Writer
+ stage3 = "TERRA_CLASS"  # Elastic Final Writer
- SOL_CLASS = "Codex / GPT-5.6 Sol"
+ SOL_CLASS = "Codex / GPT-6 Astra (High)"
+ TERRA_CLASS = "Claude Opus (High)"
```

**Why the label change matters**

- The file's own comment calls the stage entries "frozen capability roles, not volatile commercial model names". The mapping below them is the part expected to change.
- `runf` and `rung` changed the Stage-3 *role* as well as the mapping.
- `configured_model` is folded into `stage_policy_sha256`. The Stage-3 fingerprints of `runf` and `rung` therefore differ from `rund`'s, although the Stage-3 text is identical.
- Any tooling or review that reads a fingerprint change as "policy changed" will misread this pair of runs.

**What to do about it (§7.3)**

- The ledger is still the only durable record of which model produced a run, and the operator says it is wrong here too.
- Record the actual model and effort per stage before freezing.
- If the two stages ran different models, a two-role split is legitimate. It then has to be true.

### 1.3 Vacancy set

**Overlap with `rund`.** Six of the eight vacancies were also in `rund`: Tieto, BearingPoint, Amesto, Stortinget, EIE and Abacus. That gives six matched pairs.

**Two new vacancies:**

| Vacancy | What the ad asks for | What it means for the package |
|---|---|---|
| **Visma Enterprise, Product Manager** (5 positions) | 3–5 years as a Product Manager, continuous discovery, outcome ownership, commercial understanding, AI in products. Domain experience in ERP, payroll, finance or workforce management is an advantage. The ad says outright that no letter is required: upload a full CV and answer form questions. Final deadline 30.09. | The candidate misses a hard requirement. **The CV is the whole application.** |
| **Norwegian Air Shuttle, Senior Manager Digital Governance Operations** | A newly established group function covering GDPR, NIS2, the EU AI Act, third-party governance and EASA Part-IS. Operational lead: requirements into roadmaps, loosely defined matters into next steps, dashboards and decision support, escalation and incidents. The ad is **in English**, working languages are English and Norwegian, and it asks for a CV upload through the recruitment system. | The level and regulatory domain are both stretches. **The CV is the only uploaded document, and it arrives in Bokmål.** |

**Batch data**

- `unit` and `reference` are empty for all eight jobs again.
- The Visma deadline was left empty; the ad says 30.09.
- The Norwegian ad was classed CORE. `settings.toml` states that non-Bokmål vacancies are EXCEPTION.
- The harness deliberately has no letter-required or channel switch (DEC-01/02/04). Both Stage 1 and Stage 3 handled Visma well: a short, optional letter and a CV written to stand alone. The Norwegian review noted that no English version had been produced.

### 1.4 Deliverable hygiene

- **Render and warnings.** All eight renders are OK. There were three page warnings, all on `runf` CVs: BearingPoint, Amesto and Visma. `render_report.json` records each as `CV rendered to 3 pages; editorial target is <=2. Review signal only.`
- **Five CV PDFs were renamed after render.**

  | Job | File on disk |
  |---|---|
  | `runf` BearingPoint | `CV_Tech_Konsulent.pdf` |
  | `runf` Amesto | `CV_AI_Transformasjon.pdf` |
  | `runf` Visma | `CV_Product_Manager.pdf` |
  | `rung` Stortinget | `CV_radgiver.pdf` |
  | `rung` Abacus | `CV_IT_radgiver.pdf` |

  - All five are **byte-identical to the SHA-256 in their render receipts**, so the content is untouched. The DOCX files keep their canonical names and match their receipts.
  - The canonical PDF paths no longer exist. The derived queue views therefore report `render: FAILED` with the action *"Rerender from the current eligible semantic final"* for BearingPoint and Amesto (`runf`) and Stortinget (`rung`), the three that had already been renamed when the views were generated.
- **Word lock files.** `~$…docx` owner files sit in the `out/` folders of `runf` Tieto and `rung` Stortinget, the first job of each chat. Their letters were open in Word while later jobs rendered. Render succeeded anyway.
- **Template residue is unchanged.**
  - PDF spans confirm Tillitsverv, Språk, Kurs and Referanser items still render in `Calibri-Bold`.
  - Headlines are all-caps. At the current size about 62–65 characters fit on one line.

---

## 2. The experiment these runs create

**Held constant:** every semantic input. That means the stage instructions, D, K, V, the authorities, the digests, the evidence index, the masters and the template map.

**Varied:**
- the models and effort at both stages (the mapping is unknown, and the two new arms may differ from each other);
- chat size, 4 jobs per chat instead of 12;
- job order and vacancy mix;
- parallel execution;
- the settings label.

**What the design can support**
- A behaviour present in `rund` and absent from both new arms is not caused by the frozen policy text alone. At minimum it needs the cheaper model or the 12-job chat.
- A behaviour present in all three arms is shaped by the harness, the source or the template, or is common to every model tried so far.
- The six shared vacancies allow paired comparisons without a vacancy confound.

**What it cannot separate**
- **Which stage caused a change.** Both stages changed together.
- **Model versus chat size** for effects that live inside a chat (T3 decay, T4 convergence).
- **Arm `runf` versus arm `rung`**, which is confounded with vacancy type (§1.1).

The 2×2 branch test in §7.2 resolves the first point for the price of about eight Stage-3 runs.

**How I read it.** Everything was read in full:
- the 8 finals, 8 reviews and 8 strategies;
- the rendered PDF text for all 16 documents;
- all 8 vacancy views, checked against the source PDFs for the two new ads;
- the 12 `rund` letters and CV tops again, for the head-to-heads.

A targeted truth pass then checked every claim `rund` did not already make against the frozen WORK and OTHER authorities (appendix D). Scores use the nine-package ranking's rubrics unchanged, plus the curated-package interview model's compound, knock-out cues and odds scale (§5.1), so the new tables are comparable with the earlier corpus.

---

## 3. Verdict

### 3.1 Headline findings

**1. The same harness produced much better packages once the models improved.**
- On the six matched vacancies:
  - mean letter score 71.7 → 80.8;
  - mean package score 80.0 → 83.0;
  - mean interview-odds index 23.3 → 30.2.
- Most of the gain sits in one behaviour. The new letters argue with what is documented and leave missing requirements to the chronology and the review.
- **Truth architecture held again:** no fabrication in eight packages written by two different chats.

**2. The strongest content is not the strongest artefact.**
- `runf` wrote the richest strategies (34–41 KB, 7 evidence units, 3 personality facets), the richest CVs (17–21 evidence refs) and the best letters.
- Its CVs also ran to three pages in 3 of 4 jobs.
- `rung` wrote half-size strategies and tighter CVs, and every document stayed within its page budget.
- This is the curated-package lesson again, from the other side: *more evidence is the road to page three*. The harness gives the writer no capacity signal before render (§6.3, N1).

**3. The previous report over-attributed to policy text.**
- It traced volunteered limitations through Stage-1 field semantics, the Stage-3 asymmetry, K rule 5 and the content lock.
- All four were unchanged here, yet no new letter volunteers a gap.
- The chain was real in `rund`, but its trigger was the cheap models, not the wording.
- What survives across all three arms is a much shorter list, and that list is where harness edits still pay (§6.2).

**4. The stronger Stage 1 introduced a new failure, and the harness caught it.**
- New Stage-1 overstatements appeared in 4 of 8 jobs:
  - "har modernisert" budsjetteringsverktøyet;
  - "om lag 3,5 år med funksjonelt eierskap";
  - "besvarer KI-henvendelser";
  - a causal link between onboarding and the tool's value.
- Stage 3 removed every one and recorded it in `upstream_claim_repaired`.
- The elastic Stage 3 and its overclaim guard are doing exactly what 0.9.3 built them for. Weakening that guard to fix cheap-tier disclosure would now be a mistake (§7.1, E-4).

**5. The remaining residue is cosmetic in each package but systematic across the corpus.**
- Invitation closes, formula openings and transfer bridges are harmless in any single letter. They are exactly what makes a batch sound machine-made.
- Knock-out mechanics (page count) and interview-reopening triage are not cosmetic.
- Both have cheap deterministic or text fixes.

### 3.2 Property scorecard

Counts are per package unless stated. For D, the earlier 12-job counts from the previous report were re-checked with the broader patterns in appendix B.

**Truth and attribution**

| Property | `rund` (12) | `runf` (4) | `rung` (4) | Reading | Main owner |
|---|---|---|---|---|---|
| Fabrications / unsupported facts | 0 | 0 | 0 | = | Authorities + K + S3 |
| Ownership-verb slips ("Moderniserte …") | 1 (KPMG CV) | 1 (Tieto CV) | 0 in finals (1 caught in S1) | = | V example + ceiling (§6.3 N3) |

**Mechanics**

| Property | `rund` (12) | `runf` (4) | `rung` (4) | Reading | Main owner |
|---|---|---|---|---|---|
| Page budget met (CV 2 / letter 1) | 11/11 | **1/4** | 4/4 | `runf` ↓↓ | No capacity feedback |
| CV words, profile + bullets (mean) | 181–441 (355) | 422–533 (500) | 374–450 (401) | `runf` ↑ | S1 depth → S3 fill |
| Headline wraps to 2 lines | 8/11 | 3/4 | 2/4 | ↑ slightly | Soft doctrine, no feedback |
| Three-item list headlines | 11/12 | 0/4 | 0/4 | ↑↑ | Model |
| First-person CV profile | 0/12 | 0/4 | 2/4 | `rung` ↓ | No rule |

**Stage 1**

| Property | `rund` (12) | `runf` (4) | `rung` (4) | Reading | Main owner |
|---|---|---|---|---|---|
| Strategy size / evidence units / requirements / facets | 8–16 KB / 2–3 / 6–10 / 0 in 11 | 34–41 KB / 5–7 / 12–17 / 3 | 15–20 KB / 5–6 / 11–14 / 1 | ↑↑ | S1 model |
| SUPPORTED share of requirement relations | 37% | 39% | 49% | ≈ | Not the driver of T1 |
| Candidate gaps written into `top_employer_problems` | 11/12 | **0/4** | **0/4** | ↑↑ | S1 model |
| Strategies citing §2.2/§5.x/§6.x/OTHER §2.5 | 0/12 | 4/4 | 4/4 | ↑↑ | S1 model |

**Stage 3**

| Property | `rund` (12) | `runf` (4) | `rung` (4) | Reading | Main owner |
|---|---|---|---|---|---|
| Stage-3 `used_evidence_refs` that include those sections | 1/12 | 2/4 | 2/4 | ↑ (still sparse) | Digest surface (E-6) |
| §5.2 notes/summaries written into the documents | 0/12 | 0/4 | 1/4 (Stortinget CV) | ↑ small | S3 recall + surface |
| Evidence refs per package | 9–15 (12.7) | 17–21 (20.0) | 10–15 (13.5) | `runf` ↑ | S1 depth |
| Understatement repairs of Stage 1 | 10/12 | 1/4 | 1/4 | ↑↑ | S1 model |
| Overstatement repairs of Stage 1 | 0/12 | 2/4 | 2/4 | New, caught | S1 model + S3 guard |
| Digest ambiguity detected (WORK §0.3 BAR row) | 0 | 4/4 | 0 (source followed silently) | — | Source maintenance |
| Triage | READY 12/12 | READY 4/4 | READY 4/4 | = | S3 triage table |
| Apply/no-apply nudges in review | 3/12 | 2/4 | 1/4 (soft) | = | S3 + prompt |

**Letter**

| Property | `rund` (12) | `runf` (4) | `rung` (4) | Reading | Main owner |
|---|---|---|---|---|---|
| Letters volunteering a limitation | 10/12 | **0/4** | **0/4** (1 mild learning line) | ↑↑ | Model |
| Self-disqualification knock-out cue | 8/12 | 0/4 | 0/4 | ↑↑ | Model |
| Stock close "Jeg forteller gjerne mer i en samtale" | 11/12 | 1/4 | 1/4 | ↑ | Model + chat |
| Any "gjerne … samtale/prat" invitation close | 12/12 | 4/4 | 4/4 | = | V M06 wording |
| Cleft motive "Det som … , er …" | 10/12 | 0/4 | 0/4 | ↑↑ | Model |
| "Jeg søker … fordi" / "Derfor søker jeg" | 12/12 | 3/4 | 3/4 | = | Universal |
| Identity-formula opening ("Jeg er samfunnsøkonom …") | 5/12 | **4/4** | 0/4 | Chat-local | Chat convergence |
| Opening restates the title ("søker stillingen som …") | 7/12 | 1/4 | **4/4** | Chat-local | Chat convergence |
| Transfer-bridge formula ("… vil jeg ta med / bidra med …") | 6/12 | **4/4** | **4/4** (7 in total) | ↓ | K *overføringsbro* + lock |
| Conflict framing ("gjennomføringsleder valgte …") | 4/12 | 3/4 | 1/4 | = | V register (partial) |

**Pair and cost**

| Property | `rund` (12) | `runf` (4) | `rung` (4) | Reading | Main owner |
|---|---|---|---|---|---|
| Bullet or paragraph ending on "avviklet" | 5/12 | 3/4 | 1/4 | = | No rule (E-7 part 2) |
| Documentation voice from the source (Stortinget) | yes | — | yes | = | Source phrase |
| Letter 5-grams also in the CV (mean share) | .10 | .065 | .045 | ↑ | M02 partly effective |
| Max letter sentences ≥0.6 similar to a CV sentence | 7 | 7 | 4 | = | M02 partial |
| Wall-clock per job (Stage 1 + Stage 3) | ≈3.4 min | ≈12.1 min | ≈7.6 min | — | Budget |

---

## 4. Package-by-package review

Each package was read in full: the final JSON, the rendered PDF text, the review and the strategy. The vacancy essences for the six shared jobs are in the previous report (§4.5, 4.6, 4.8, 4.10, 4.11, 4.12) and are only recapped here. Every claim new to this pair of runs was checked against the frozen authorities (appendix D). Suggested wording is supported by the cited sections, but Vegard owns the final Norwegian.

**How to read the scores.** Each package lists CV, letter and package rubric scores, then the knock-out cues, then:
- the **interview-odds index (IOI)**, which rates execution independently of fit;
- the **expected interview chance**, which applies a vacancy-fit factor.

The model is in §5.1. Verdict scale as before: *light edit* under 10 minutes, *targeted edit* 10–30 minutes, *rework* means re-running Stage 3.

### 4.1 `runf` — Tieto Tech Consulting, Prosjektleder & Endringsleder

**Vacancy.** Change and project-lead consultants for client digitalisation. Adoption, anchoring and benefit realisation; KI-supported work processes. A **minimum of five years** as change, process or project lead. Public-sector or large private experience is a strength, and certifications are a plus.

**Route**
- **Stage 1** (44 KB, 17 requirements, 7 evidence units, 3 facets):
  - Chose a functional adoption route: PRJ-03, then PRJ-04, with KI as a short separate proof.
  - Marked R01 MINIMUM/GAP but kept the gap out of every positive field.
  - Its writer guidance says the minimum is handled "gjennom presise påstander og korrekt kronologi, ikke gjennom unnskyldning".
- **Stage 3** kept the route and made three changes:
  - lifted PRJ-06 into the benefits paragraph (rejected false precision; no core VBA, so the controllers could own the model);
  - added the 2027 round;
  - moved observed user tests into the CV.
- **Stage 3 also repaired three things:**
  - the §0.3 BAR digest ambiguity;
  - Stage 1's causal link between onboarding and the tool's value;
  - Stage 1's under-use of the 2027 modernisation.

**Against `rund`.**
- Both of `rund`'s costliest sentences are gone:
  - the opening "Jeg har ikke vært endringsleder eller prosjektleder i fem år. Jeg søker likevel …";
  - the closing "Erfaringen min er fra offentlig sektor, og jeg har ikke jobbet som konsulent."
- The consulting shift is now a positive paragraph: *"Til nå har jeg gjort dette fra innsiden av én stor virksomhet … Hos dere vil jeg bruke den samme arbeidsformen hos flere virksomheter, i et fagmiljø der endringsledelse er hovedfaget."*
- The IOI more than doubles: 15.9 → **34.1**.

**Strengths**
- **The best handling of the constrained refactor in the corpus.** After *"Gjennomføringslederen ville ha en smal refaktorering, funksjon for funksjon, og det var den jeg gjennomførte"* the paragraph turns the disagreement into a consulting skill: *"Jeg regner med at mye av arbeidet i kundeoppdrag foregår på samme måte: innenfor rammer kunden eier, og uten at driften kan stoppe."*
- **Method and judgement side by side, each with its own status.** The benefits paragraph pairs PRJ-04 (four people, standard, still in use after 2.5 years) with PRJ-06: *"I stedet for å gi tallene en presisjon de ikke hadde, utformet jeg en vektet modell med synlige forutsetninger."*
- **The KI paragraph states where delegation stops:** *"der konsekvensene er store, ligger beslutningen hos et menneske"*.
- **The CV headline gets the altitude right without claiming a title:** "Samfunnsøkonom og rådgiver | Innføring av nye løsninger og gevinstarbeid".
- **Evidence breadth.** 17 evidence refs. Stage 1 cited §2.2, §5.2, §6.6 and OTHER §2.5.

**Defects**
- **Ownership verb in CV bullet 1:** *"Moderniserte sykehusets om lag 20 år gamle budsjetteringsverktøy …"*.
  - WORK §4.3's ceiling says "Never claim … sole ownership of the complete modernization".
  - The next sentence restores the boundary ("I praksis eneste kodende utvikler i en bred prosess med om lag 50 deltakere"), and the letter is correct. So this is a calibration slip, not a fabrication.
  - `rung`'s Norwegian Stage 3 repaired the same verb out of its own Stage 1 (§6.3, N3).
- **Formula opening:** *"Jeg er samfunnsøkonom og har siden 2023 vært rådgiver …"*. All four `runf` letters open this way.
- **The ad quoted as a paragraph opener:** *"Dere skriver at investeringene skal gi faktisk verdi."* The paragraph works without it.
- **Stock close:** *"Jeg forteller gjerne mer om dette i en samtale."*
- **Headline wrap.** In caps the headline wraps, leaving "GEVINSTARBEID" alone on line 2.
- **"Avviklet" ending.** The dashboard bullet ends "… til avviklingen rundt februar 2026."
- **Status sentences in both documents:** still in use after 2.5 years, "ferdigstilt og overlevert", and the superuser sentence.
- **Review nudge:** *"Vurder ved godkjenning om søknaden skal sendes med dette kjente gapet."* This reopens the apply decision (DEC-31), again on Tieto.

**Truth check: verified.**
- The 2027 round with "vesentlig større frihet", and current use in "den pågående budsjettprosessen" (WORK §4.3 delivered status, confirmed 2026-09-06).
- "Bevisst uten kjerne-VBA" (§4.6).
- The superuser role for about three years in a Teams channel (§0.3).
- One slip, the ownership verb above.

**Scores:** CV **85.1** · Letter **81.6** · Package **83.3** · no knock-out cue · IOI **34.1** (2nd of 20) · expected chance **18.9** (fit 0.45, because the five-year minimum is unmet).

**Verdict: send after light edit.**
1. **CV bullet 1:** "Var i praksis eneste kodende utvikler da sykehusets om lag 20 år gamle budsjetteringsverktøy i Excel/VBA ble modernisert, slik at ansatt-, ansettelses- og bemanningsdata ble integrert i stedet for å kopieres manuelt. Bred prosess med om lag 50 deltakere; laget onboarding- og presentasjonsmateriell for controllere. Brukt sykehusdekkende i budsjettprosessene for 2026 og 2027."
2. **Headline:** "Samfunnsøkonom og rådgiver | Innføring og gevinstarbeid" (55 characters, one line).
3. **Body 2:** delete the ad-quote sentence.
4. **Dashboard bullet:** "… eier av løsningen og den månedlige driften mens den var i bruk, fra om lag august 2025 til februar 2026."
5. **Close (optional):** replace the stock sentence with a topic, e.g. "Jeg tar gjerne en samtale om hvordan dere arbeider med innføring og gevinster i kundeoppdragene."
6. **Review:** ignore the apply/no-apply nudge.

### 4.2 `runf` — BearingPoint, Konsulent forretning- og teknologirådgivning

**Vacancy.**
- Requirements: 2–4 years' experience, preferably as a consultant, and a master's degree.
- Scope: technology and AI for business value, digital transformation, new governance models and ways of working, change and AI adoption, procurement and IT-partner selection.
- Style: work close to leadership and challenge established truths.

**Route**
- **Stage 1** (40 KB, 16 requirements, 7 units):
  - Chose a judgement-and-technology-choice angle: PRJ-06, then PRJ-03, with KI as practice.
  - The formal filter is visible early, and the consulting gap is handled in the motivation.
  - Tone instruction: "faglig trygg, ikke senior".
- **Stage 3:**
  - rebuilt the KI proof so it also carries the challenge to the forecast target;
  - opened on a documented work pattern (separating the underlying need from the requested solution);
  - moved the learning-speed evidence into the motivation;
  - repaired the digest ambiguity, and kept the technology appraisal separate from the implementation lead's decision.

**Against `rund`.**
- `rund`'s closing concession, *"Jeg har ikke jobbet som konsulent, og anskaffelser og valg av IT-partnere blir nytt for meg"*, is replaced by the positive frame my previous report proposed: *"Nye fagområder har jeg satt meg inn i før. I klinikken hadde jeg overtatt hele den tildelte månedsoppgjørsflyten innen om lag tre måneder, og VBA lærte jeg fra grunnen da jeg laget konverteringsverktøyene."*
- The letter gains 6.7 points.
- The CV gains content but runs to three pages, so the IOI dips slightly (27.4 → 25.7). Compacted, it is **33.1**.

**Strengths**
- **The profile answers the formal filter outright:** *"om lag 3,5 års erfaring som rådgiver i økonomi og IKT"*.
- **Two competencies meet the ad's own vocabulary without overclaiming:**
  - "Styringsmodeller og arbeidsformer: gevinstrealisering, Scrum/Kanban og WIP" answers *nye styringsmodeller og arbeidsformer*;
  - "Vurdering av teknologialternativer mot driftsrisiko og vedlikehold" is the defensible neighbour of IT-partner selection.
- **Body 1 ends on a real transfer:** *"Hos kunder som står foran et investeringsvalg, vil jeg gjøre det samme: vise hva tallene bærer, og hva som er antakelser."*
- **The most direct evidence anywhere for *utfordre etablerte sannheter*:** *"utfordret jeg hvordan prognosemålet var definert, og krevde tidsriktig validering mot referanseprognoser"*.
- **Breadth without concession:** 21 evidence refs and no concession sentence.

**Defects**
- **Three-page CV** (522 words). Page 3 holds KURS and REFERANSER, four lines. This is a knock-out cue.
- **Duplication:** dup60 = 7. The STE model and PRJ-03 appear at near-equal detail in CV bullets 1–2 and letter bodies 1–2. Shortening those two CV bullets fixes the page count and the duplication together.
- **Headline wrap:** "TEKNOLOGI" alone on line 2. The letter also opens with the formula.
- **Mild conflict framing with no transfer:** *"mens gjennomføringslederen valgte en smal refaktorering"*. Tieto converts the same contrast (§4.1); this letter does not.
- **In-chat carry-over:**
  - the bridge formula *"Den kombinasjonen av bruk og kontroll vil jeg ta med når kunder skal ta i bruk AI"*;
  - the bolt-on *"Jeg er også registrert KI-superbruker ved OUS og tar et masterprogram i kunstig intelligens …"*, identical in `runf` Amesto.
- **Mixed terms:** "AI" and "KI" in the same letter.
- **"Avviklet" inside the dashboard bullet.**

**Truth check: verified.**
- PRJ-06 as decision support for choices about storage, equipment, automation and investments (§4.6: "Warehouse, equipment, automation, feature and investment choices").
- "Defined and challenged the operational forecast target" (§4.5).
- The option appraisal (§4.3).
- "Om lag 3,5 år" is derived from the chronology (March 2023 to September 2026) and is correct. The inflated variant, "3,5 år med funksjonelt eierskap", belonged to the Visma Stage 1 and was not used anywhere.

**Scores:** CV **83.9** · Letter **83.2** · Package **80.7** · knock-out cue: CV three pages · IOI **25.7** (33.1 once compacted) · expected chance **23.7** (30.8 compacted).

**Verdict: targeted edit, about 10 minutes, mechanical.**
1. **CV to two pages.**
   - Cut bullet 2 (PRJ-03, 72 words) to scope, sole coder, controls and use; the option appraisal stays in the letter.
   - Cut bullet 1 (PRJ-06) to about 30 words.
   - If it still spills, drop the REFERANSER section.
2. **Headline:** "Samfunnsøkonom | Rådgiver i virksomhet og teknologi".
3. **Terminology:** use KI throughout the letter.
4. **Optional:** "Gjennomføringslederen valgte en smal refaktorering, og den gjennomførte jeg funksjon for funksjon …" (drops the *mens* contrast).

### 4.3 `runf` — Amesto Accounthouse, AI Team Lead – Transformasjon

**Vacancy.**
- A small transformation team with a big mandate: automation in accounting and payroll from idea to delivery.
- Data warehouses, APIs, AI pilots made to work for many customers.
- Not a developer, but able to discuss architecture.
- Accounting or payroll experience is "interesting"; personnel responsibility may come later.

**Route**
- **Stage 1:** BAR first (learn the process, then automate it), PRJ-03 for technology choice, PRJ-05 for architecture and KI with distributed authorship. Translate health vocabulary; do not address the team-lead title.
- **Stage 3:**
  - kept that route;
  - added the STE model's no-VBA decision as a consequence of technology choices;
  - added PRJ-05's separation of local validation from live runs as a concrete KI control;
  - moved the founding of Analyseavdelingen into the motivation;
  - repaired only the digest ambiguity.

**Against `rund`.**
- `rund`'s closing *"Lønn, regnskapsbyrå og løsninger for mange eksterne kunder har jeg ikke jobbet med, og jeg har ikke ledet et team"* is gone.
- In its place is the positive functional route: *"Fra Analyseavdelingen har jeg også erfaring med å starte noe nytt: jeg var med i gruppen på fire som etablerte avdelingen …"*. That answers *lite team med stort mandat*.
- The letter gains 9.7 points. IOI 25.1 → 26.2, or **33.7** with a two-page CV.

**Strengths**
- **The best thesis-in-the-opening of the eight letters:** *"Automatisering har jeg lært fra to sider: først som den som gjennomførte en regnskapsnær prosess, deretter som den som bygget verktøyene andre brukte i den."*
- **Every paragraph converts to Amesto's work:**
  - *"Å kjenne prosessen før jeg automatiserer den, er den rekkefølgen jeg vil ta med inn i regnskaps- og lønnsleveransene deres."*
  - *"I driftskritiske prosesser som regnskap og lønn er det den typen kontroll jeg vil bygge inn når KI tas i bruk."*
- **Two documented decisions answer *konsekvensene av teknologiske valg*:** the option appraisal, and the model deliberately built without core VBA so the controllers could own it.
- **A precise distributed-authorship statement:** *"En kollega laget den opprinnelige modellen og mye av datavaskingen."* It sits next to a real control, local validation kept separate from unvalidated live runs.
- **The headline fits on one line:** "Rådgiver i økonomi og IKT | Automatisering av økonomiprosesser".

**Defects**
- **Three-page CV** (523 words) for the sake of **two lines**, "REFERANSER / Oppgis ved forespørsel." It is the cheapest fix in the corpus.
- **Long first bullet:** CV bullet 1 is 84 words.
- **English term:** "features" in CV bullet 2 and in letter body 3 (`rund` Amesto had it too).
- **Bridge formula used twice**, plus the superuser/master bolt-on shared with BearingPoint.
- **"Avviklet" ending** on the dashboard bullet; the opening sentence is the identity formula, placed before the thesis; dup60 = 7.

**Truth check: verified.**
- "Separation of local/synthetic validation from unvalidated live-database/model execution" (OTHER §4.3).
- The coworker created the original XGBoost model, many features and much of the data cleaning (WORK §4.5).
- The BAR bullet follows §1.1 ("arbeid som ble kvalitetssikret av andre"), not the ambiguous digest.

**Scores:** CV **83.6** · Letter **84.7** (the best letter of the 20) · Package **80.6** · knock-out cue: CV three pages · IOI **26.2** (33.7 compacted) · expected chance **19.9** (26.2 compacted).

**Verdict: targeted edit, about 5 minutes, mechanical.**
1. **CV to two pages.** Delete REFERANSER, or better, cut bullet 1 to about 55 words; the option appraisal is already in the letter.
2. **Terminology:** "features" → "variabler" in both documents.
3. **Opening:** start on the thesis sentence. The identity sentence can go, since the CV carries it.
4. **Body 3:** delete the superuser/master bolt-on, since the CV carries it.

### 4.4 `runf` — Visma Enterprise, Product Manager (CV-only instrument)

**Vacancy:** see §1.3.

**Route**
- **Stage 1** (37 KB, 12 requirements):
  - Chose domain strength, user proximity and data discipline.
  - Explicitly "ikke kles ut som PM".
  - The letter optional and short, and the CV built to stand alone.
- **Stage 3:**
  - kept that route;
  - added PRJ-10's section-level DRG estimates as planning-domain evidence, without the one-month hit observation;
  - used the forecast-target challenge in the letter.
- **Repairs:** Stage 1's objection reframed the experience as *"om lag 3,5 år med funksjonelt eierskap"*. Stage 3 identified this as inflated ownership and did not use it.

**Strengths**
- **The CV shows product-manager behaviour without the title.** Its competencies include:
  - "Brukerinsikt: observerte brukertester, behovsavklaring og kravarbeid";
  - "Prioritering og iterativ forbedring innenfor tekniske og operative rammer";
  - "Data og validering: måldefinisjon, referanseprognoser og akseptansekriterier";
  - "Domene: økonomi, budsjett, bemanning, aktivitet og kapasitet i helseforetak".
- **Bullet 1 carries two product decisions:** *"Valgte stjerneskjema etter å ha vurdert alternativer, og skilte en større modellmodernisering fra løpende videreutvikling da modellgrensene ga leveranserisiko."*
- **The domain argument is real.** Visma builds ERP and workforce management for *kommuner og helseforetak*: *"Manuelt arbeid i økonomi og bemanning kjenner jeg dermed både fra plassen til den som gjør det, og fra plassen til den som endrer verktøyet."*
- **The best close of the eight:** *"Jeg tar gjerne en samtale om hvor erfaringen passer best, i ERP eller Workforce Management."* It picks up the ad's own "sammen kan vi finne ut hvor erfaringen og interessene dine passer best".
- **The review gets the channel right:** upload the CV, use the letter only if the form allows, and answer the form questions by hand.

**Defects**
- **Three-page CV, and the CV is the whole application.** 533 words; a 103-word profile; page 3 holds KURS and REFERANSER.
- **Headline wraps** at 84 characters.
- **The profile repeats the competency block** ("Stiller krav til mål, referanser og akseptansekriterier …").
- **Review nudge:** *"Vurder ved godkjenning om søknaden skal sendes med dette kjente gapet."*
- **Fit:** three to five years as a PM is a hard requirement the package cannot change.

**Truth check: verified.**
- Star schema chosen after evaluating alternatives (§4.1).
- Staffing, UTA and on-call controls (§6.1).
- The DRG estimates (§4.10), without the hit observation.
- The forecast target defined and challenged (§4.5).

**Scores:** CV **81.4** · Letter 82.2 (not counted; not requested) · Package **78.8** · knock-out cue: CV three pages · IOI **22.6** (29.4 compacted) · expected chance **9.3** (12.7 compacted).

**Verdict: targeted edit.** The CV has to be two pages, because it is the application.
1. **Profile** down to about 60 words: drop the "Stiller krav …" sentence, which repeats competency 3.
2. **Headline:** "Samfunnsøkonom | Brukernære løsninger for økonomi og bemanning" (61 characters).
3. **Bullet 1** (81 words): keep the two decisions, the user tests and the ownership period; cut the rest.
4. **Form questions:** use letter body 3 as the motivation answer.
5. **Batch data:** add the 30.09 deadline.

### 4.5 `rung` — Stortinget, seniorrådgiver/rådgiver, forvaltningsavdelingens stab (deadline 14.09)

**Vacancy.**
- A central staff role close to the department head and management group.
- The work: planning and follow-up structures (Decisions/Planner), gatherings, cross-cutting coordination, notes and decision support, investigations, and new digital and KI working methods.
- Advantages: M365, guidance and continuity/preparedness. HEMMELIG clearance is required.

**Route**
- **Stage 1** (20 KB, 14 requirements, 5 units, 1 facet):
  - Chose routine leader deliveries in BAR and PRJ-08 structuring ahead of the more prestigious analysis projects, with PRJ-03 as proof of a delivered improvement.
  - Kept economic leader support separate from administrative secretariat work.
  - Labelled staff experience ADJACENT.
- **Stage 3:**
  - Repaired that label: both OUS placements are formal staff units, and independent sign-off and dispatch of monthly reports is documented. This is the same understatement `rund`'s Stage 3 repaired.
  - Gave the KI superuser role its own paragraph.
  - Added the intake forms as a bridge to case follow-up.
  - Kept PRJ-04 in the CV.

**Against `rund`.**
- **`rund`'s biggest single miss is repaired in the CV.** Bullet 1 is now *"Utarbeider beslutningsgrunnlag, notater og korte sammendrag om økonomi, bemanning og aktivitet for ledere, controllere og fagmiljøer"*, and one competency reads "Beslutningsgrunnlag, notater og sammendrag".
- **KI no longer leads the CV.**
- **The headline shrank** from 99 to 63 characters and fits on one line.
- **Package 75.5 → 84.8; IOI 19.0 → 30.9.**

**Strengths**
- **The opening anchors in the staff units and states what the work was:** *"Begge steder har jobben vært å levere underlag som ledere kan bruke, og å gjøre arbeidet rundt dem mer ordnet."*
- **Economic leader support becomes the staff role without inflation:** *"Stillingen hos dere har et annet innhold, men den samme kjernen: faste leveranser til ledelsen og mange større og mindre saker som skal følges helt i mål."*
- **Decisions and Planner appear only as future contribution**, which is correct under the ceiling.
- **The CV names the ad's own advantages:** "Microsoft 365: Teams, Loop, Forms, Excel og PowerPoint", "Workshops, veiledning og opplæring", "Strukturering av oppgaver, prioritering og oppfølging".
- **Letter and CV overlap less than in any other package** (shared 5-grams .03).
- **HEMMELIG and the five-year preference are left to the review**, which is correct.

**Defects**
- **Documentation voice again, in both documents.**
  - Letter: *"prosjektøkonomiske saker, som ble fordelt etter behov og etter hva økonomileder hadde kapasitet til"*.
  - CV: *"etter behov og økonomileders kapasitet"*.
  - This is the same defect as in `rund`, written by a different model from the same source phrase, CLM-BAR-004 *"avhang av økonomilederens kapasitet"*. It is source-driven (§6.3, N7).
- **First-person CV profile:** *"Fra klinikkstaben … har jeg erfaring med …"*, *"I dag arbeider jeg med …"*.
- **Notes and summaries appear only in the CV.** The letter's answer to the writing tasks is "underlag som ledere kan bruke".
- **Formula opening and close.**
  - The opening restates the title: *"… og søker stillingen som seniorrådgiver/rådgiver i forvaltningsavdelingens stab."*
  - The close stacks three formulas: "Jeg søker fordi …", a meaning sentence ("gjør det meningsfullt for meg") and the stock close.
- **Bolt-ons:** two transfer bridges and three "også / I tillegg" additions in 461 words.
- **Little judgement shown.** The letter describes structures rather than decisions.
- **Nine competencies**, above settings' soft maximum of 8. The render report shows no warning.

**Truth check: verified.**
- "Sammen med avdelingsleder og to kolleger" (WORK §0.2).
- Decision notes and executive summaries (§5.2).
- Workshops planned and facilitated (§4.8).
- Decisions/Planner are future contribution only.

**Scores:** CV **83.4** · Letter **76.7** · Package **84.8** · no knock-out cue · IOI **30.9** · expected chance **28.7** (fit 0.90).

**Verdict: light edit, but the deadline was 14.09.** If the application has not been sent, check whether late applications are still considered. The same edits apply to reuse in other staff roles:
1. **Letter body 1:** delete "og etter hva økonomileder hadde kapasitet til". **CV:** "Håndterte prosjektøkonomiske saker etter behov, blant annet …".
2. **CV profile without first person:** "Erfaring fra klinikkstaben i Barne- og ungdomsklinikken med selvstendig månedsoppgjør og månedlig rapportering til ledere. Arbeider i dag med beslutningsgrunnlag, struktur for oppgaver og samarbeid, og forbedring av digitale arbeidsverktøy."
3. **Letter body 2**, add: "Til ledere, controllere og fagmiljøer skriver jeg beslutningsgrunnlag, notater og korte sammendrag, med detaljnivå etter hvem som skal bruke dem." (§5.2)
4. **Opening:** cut the title clause. **Close:** keep one of the two motive sentences and end on the offer.

### 4.6 `rung` — Norwegian Air Shuttle, Senior Manager Digital Governance Operations (CV-only instrument; English ad)

**Vacancy:** see §1.3.

**Route**
- **Stage 1** (22 KB, 12 requirements):
  - Took the ad's alternative entry: advisory, transformation or business operations in a regulated organisation.
  - Carrying evidence: PRJ-03 for controlled implementation, PRJ-04 for shared methodology, PRJ-06 as judgement.
  - Named regulations, authority contact and incident handling stay material gaps, recorded in the review only.
- **Stage 3:**
  - made the STE trade-off the first carrying case (loosely defined matter, verifiability, less dependence on key people);
  - moved PRJ-04 to the CV;
  - added the intake forms and the KI superuser role;
  - used the founding of Analyseavdelingen as the motivation.
- **Repair:** Stage 1's *"har modernisert"* was replaced by sole coder under the implementation lead's constraints.

**Strengths**
- **The letter maps onto the ad's bullets without echoing them.**
  - *"reduce reliance on key individuals"* is answered by *"slik at controllerne skulle kunne kontrollere og endre forutsetningene uten å være varig avhengige av en utvikler"*.
  - *"bringing together the right specialists … agreed actions are followed up"* is answered by *"slik at spesialistene får de riktige spørsmålene tidlig, ansvaret er tydelig og avtalte tiltak blir fulgt opp"*.
- **It opens on a work pattern, not an identity formula:** *"Mye av arbeidet mitt ved Oslo universitetssykehus begynner med en bestilling som er for bred eller for løst formulert til å gjennomføres slik den står."*
- **The motivation is a true parallel.** The candidate helped found a new department, and the ad describes a newly established group function.
- **The CV competencies use the ad's verbs:** "Strukturering av løst definerte saker og beslutningsbehov", "Dashbord og ledelsesrapportering", "Prosessforbedring, standardisering og automatisering".
- **A privacy control without a GDPR claim:** *"kontrollerer kode og notatbøker for sensitive data"*.
- **No over-reach.** No regulation is named, and no authority contact or incident work is implied.

**Defects**
- **Language and channel.**
  - The ad is in English and asks for a CV upload only. That CV is in Bokmål.
  - The job was classed CORE, although the settings class non-Bokmål vacancies as EXCEPTION.
  - The review noted that no English version was produced. The queue did not.
- **The package's best writing never reaches the reader**, because the letter cannot be uploaded.
- **First-person CV profile:** *"der jeg gjør bredt formulerte behov om …"*.
- **Formula opening and close.** The opening restates the title. The close uses *"den viktigste grunnen til at jeg søker"* and *"Jeg tar gjerne en prat om hvordan jeg kan bidra."*
- **Level gap.** The role is a senior operational lead and escalation point; the package honestly presents an operational adviser. That is fit, not execution.
- **Soft apply/no-apply nudge in the review:** *"Vurder nivåspranget i godkjenningen."*

**Truth check: verified.**
- About 80–90% of the dashboard DAX: a self-reported share (§8), bounded here by "backend".
- The sensitive-data checks (§4.5).
- The intake forms (§4.9).
- The implementation lead's narrow refactor (§4.3).

**Scores:** CV **79.5** · Letter 83.5 (not counted; cannot be uploaded) · Package **80.8** · no knock-out cue · IOI **28.6** · expected chance **12.3** (fit 0.35).

**Verdict: fix the channel, not the content.**
1. **Produce an English CV**, either through an EXCEPTION run or by careful manual translation of this one. The content transfers.
2. **CV profile without first person.**
3. **Reuse the letter text:** paste bodies 1 and 3 into any free-text field the recruitment system offers.
4. **Review:** ignore the level nudge.

### 4.7 `rung` — EIE eiendomsmegling, Systemkoordinator

**Vacancy.**
- Broker-facing system support: inquiries, fixes and follow-up.
- Work with Brokio on tool testing; a large KI share of the job.
- Guides people actually read; training online and at gatherings; office set-ups with vendors; Core/EIE 365.
- Background: estate agent, or economics/IT, plus systems work and **close customer dialogue**.
- A two-year temporary post.

**Route**
- **Stage 1** (17 KB, 11 requirements):
  - Chose user-facing technical advice plus practical KI.
  - Carrying evidence: PRJ-01 for troubleshooting and testing; PRJ-02 and PRJ-03 for guidance and onboarding.
  - Kept the gaps in real estate, Core/EIE 365 and vendor set-up.
- **Stage 3:**
  - promoted the REGERP tools to the first carrying case (help during a system transition, used across clinics);
  - added PRJ-07 early access for tool testing;
  - surfaced the UiA KI master.
- **Repair:** Stage 1's "KI-henvendelser" became "tekniske henvendelser", the source's wording.

**Against `rund`.**
- `rund`'s closing learning line (*"Meglerbransjen, Core og EIE 365 må jeg lære …"*) is gone.
- `rund` also had a Sector Alarm customer-dialogue sentence; `rung` leaves customer dialogue to the chronology.
- IOI 31.5 → 33.2, a small gain. `rund`'s EIE was already one of its best packages.

**Strengths**
- **Every paragraph lands in EIE's world:**
  - new tools and offices: *"Når nye verktøy tas i bruk eller nye kontorer skal i gang hos EIE …"*;
  - guides: *"Veiledninger og opplæring for meglerne vil jeg bygge på samme måte, med utgangspunkt i hvor folk faktisk står fast"*;
  - Brokio: *"finne ut sammen med meglerne hvor KI kan forenkle arbeidsdagen, prøve det ut i praksis og gjøre det som fungerer, lett å ta i bruk"*.
- **The most concrete user-support evidence in the corpus.** The dashboard paragraph covers monthly operation and *"var den som feilsøkte når noe ikke virket"*, then: *"Der jeg så at de ble usikre eller misforsto noe, samlet jeg innspillene og tok dem i korte, avgrensede forbedringsrunder."*
- **The most scannable competency block of the eight** (8 items, 37 words), mirroring the ad's tasks.
- **Opening on the KI superuser role** suits an ad where KI is a large part of the day.

**Defects**
- **Close customer dialogue, a stated requirement, is answered only by the Sector Alarm line in the chronology.** `rund` covered it in one letter sentence.
- **Three transfer bridges with the same frame** in a 377-word letter. V says "Én tydelig kobling er nok".
- **Headline wraps** at 77 characters.
- **A generic CV bullet:** *"Utvikler beslutningsstøtte for økonomi, bemanning og aktivitet med Power BI, Excel/VBA, SQL og R/Python etter behov."*
- **Formula opening and close.** The opening restates the title; the close is "Jeg søker fordi …" followed by "Jeg tar gjerne en prat om stillingen."

**Truth check: verified.**
- Primary technical troubleshooting, observed confusing interactions, collected feedback and focused improvement sprints (§4.1).
- PRJ-07 early access including Python (§4.7).

**Scores:** CV **82.6** · Letter **81.1** · Package **84.9** · no knock-out cue · IOI **33.2** (3rd of 20) · expected chance **32.1**.

**Verdict: light edit.**
1. **Customer dialogue**, in the letter or the profile: "Tett kundedialog har jeg fra Sector Alarm, der jeg avklarte behov, laget pristilbud og solgte direkte til kunder." (WORK §1.2, as `rund` used it.)
2. **Keep one bridge.** Cut "er det denne typen praktisk hjelp jeg vil bidra med" and let the Brokio sentence carry the transfer.
3. **Headline:** "Rådgiver økonomi og IKT | Systemforbedring og brukerveiledning" (62 characters).
4. **CV:** delete the generic "Utvikler beslutningsstøtte …" bullet.

### 4.8 `rung` — Abacus IT, ERP-rådgiver (the ad covers junior and senior)

**Vacancy.**
- BNXT by Visma implementations for customers.
- ERP-rådgiver (junior track): 1–2 years of ERP, economics, logistics, system implementation or similar, plus process understanding in finance or logistics.
- Senior: solid ERP delivery.

**Route**
- **Stage 1** (19 KB, 12 requirements):
  - Chose the ERP-rådgiver track in finance.
  - Carrying evidence: BAR and the REGERP tools, with PRJ-03 for controlled change.
  - Its structure guidance ends: *"Avslutt på BNXT-læring og bidrag i Abacus' prosjektmiljø uten defensiv katalog over mangler."*
- **Stage 3:**
  - kept the route;
  - opened on the REGERP transition seen from the user side;
  - gave the REGERP tools their own argument;
  - added the intake forms and the STE model to the CV;
  - found nothing to repair.

**Against `rund`.**
- `rund`'s body 3 (*"BNXT og Visma kjenner jeg ikke fra før, og jeg har ikke jobbet med ERP-implementering for kunder. Derfor søker jeg rådgiverrollen og ikke seniorrollen."*) is replaced by a positive track choice, *"Jeg søker stillingen som ERP-rådgiver innen finans"*, and one forward-framed learning line.
- **Letter 68.3 → 77.5; IOI 20.8 → 30.9.**

**Strengths**
- **The best first sentence of the eight:** *"Jeg har opplevd et ERP-skifte fra brukersiden."*
- **The process paragraph uses exactly the month-close vocabulary an ERP finance consultant works in** (prosjektnulling, periodisering, reversering, avsetninger, bilagsflyt, avstemming, resultatforklaring). It converts it: *"Det har gitt meg et konkret bilde av hva økonomibrukerne trenger at et system gjør riktig hver måned, og det bildet vil jeg ta med inn i behovsanalysene hos kundene."*
- **CV competencies read like an ERP finance profile:** "Datakonvertering og validering ved ERP-overgang", "Brukererfaring og dataflyt i REGERP, ADI og GAT".
- **The close names the customer's processes and the product:** *"forstå hvordan kunden gjør oppgjør, fakturering og prosjektoppfølging, og være med på å få det riktig inn i BNXT."*

**Defects**
- **One learning line survives from the Stage-1 instruction:** *"Selve produktet skal jeg lære, og rådgiversporet med erfarne kolleger gir en god ramme for det."*
  - It is forward-framed and much cheaper than `rund`'s version.
  - It is also the one place where a Stage-1 learning instruction still reached a stronger writer (§6.2, T1).
- **Little judgement shown.** The letter contains no decision, and the intake-form evidence for *behovsanalyse og løsningsdesign* is only in the CV.
- **Headline wraps** at 92 characters.
- **The thinnest of the eight:** 10 evidence refs and a 340-word letter.
- **"Avviklet" ending:** the dashboard bullet ends "… til den ble avviklet rundt februar 2026."

**Truth check: verified.**
- A substantial contribution to a first component of an operations report (§0.3, PRJ-02).
- Buy-outs, audit costs and overhead (CLM-BAR-004).
- Tools that checked project and account codes (§1.1 tools).

**Scores:** CV **83.3** · Letter **77.5** · Package **83.8** · no knock-out cue · IOI **30.9** · expected chance **32.9** (fit 1.10; second-best chance of the 20).

**Verdict: light edit.**
1. **Headline:** "Samfunnsøkonom | Økonomiprosesser og systemendring" (50 characters).
2. **Add the analysis step to the letter:** "Før noe bygges, har jeg utformet skjemaer for arbeidsinntak som får fram formål, brukere, beslutningsbehov og akseptansekriterier." (WORK §4.9)
3. **Delete** "Selve produktet skal jeg lære …". The junior track already assumes learning.
4. **Reorder the dashboard bullet** so it does not end on "avviklet".

### 4.9 Across the eight: same evidence, different writing

**1. The same three records carry almost every letter; what differs is the conversion sentence.**
- PRJ-03 (the budget tool) is in all eight letters. PRJ-06 (the STE model) is in four, and in two more CVs. BAR and the REGERP tools are in six.
- That is correct: they are the strongest records. What makes a letter vacancy-specific is the sentence that turns the record into the employer's problem:

  | Package | PRJ-03, PRJ-06 or BAR becomes … |
  |---|---|
  | Tieto | working inside frames the client owns |
  | BearingPoint | showing what the numbers carry |
  | Amesto | knowing a process before automating it |
  | Visma | knowing manual work from both chairs |
  | Stortinget | fixed deliveries to leadership |
  | Norwegian | traceability without key-person dependency |
  | EIE | help at a system transition |
  | Abacus | the ERP change from the user side |

- The new arms write this sentence consistently; `rund` did it in about half its letters.

**2. Both new arms handle a missing requirement the same way: silence plus a positive substitute.**

| Vacancy | Missing in the record | Positive substitute |
|---|---|---|
| Tieto | Five years as lead | "fra innsiden av én stor virksomhet … hos flere virksomheter" |
| BearingPoint | Consulting | Learning speed with two pieces of evidence |
| Amesto | Team lead | Founding group of a new unit |
| Visma | PM title | User research, prioritisation and validation behaviour |
| Abacus | BNXT | The track choice |
| Norwegian | Regulatory domain | Operational translation and traceability |

- Every gap is recorded in `review.json`. This is the behaviour E-1 was meant to force; stronger models do it unprompted.

**3. Each chat converges on its own formulas.**
- `runf`: 4 of 4 identity openings, and a verbatim bolt-on shared between BearingPoint and Amesto (*"Jeg er også registrert KI-superbruker ved OUS og tar (et) masterprogram i kunstig intelligens ved Universitetet i Agder"*).
- `rung`: 4 of 4 openings that restate the title, and 7 transfer bridges across 4 letters.
- Letter-pair 4-gram similarity is highest for adjacent jobs in the same chat: `runf` BearingPoint–Amesto .105, `rung` Norwegian–Abacus .062. Cross-chat pairs are mostly .01–.03.
- `rund`'s highest pair was also its adjacent BearingPoint–Amesto (.14).
- **Shorter chats reduce convergence but do not remove it.**

**4. The two arms write in two styles.**

| | `runf` | `rung` |
|---|---|---|
| Letter length and density | Longer (mean 429 words), denser | Shorter |
| Conversions | Explicit | More bridges and "også" bolt-ons |
| Judgement shown | More | Less |
| CV headlines | "Anchor \| function" pipe form, 3 of 4 wrap | Prose form, 2 of 4 wrap |
| CV length | 522–533 words in three of four | 374–450 words, 2 pages |

Neither style is better in every respect. The best achievable package combines `runf`'s letter conversions with `rung`'s CV discipline.

**5. What no arm did.**
- No letter asks the employer a real question about its work. Visma's close comes nearest.
- No letter names an employer fact and converts it, as the curated notes recommended (b5104f's "43 lufthavner … kontroller er det som gjør endring mulig"). Norwegian's "ny konsernfunksjon" parallel and Visma's "kommuner og helseforetak" come closest.
- That move is the largest remaining gap between these letters and the best Avinor letter, and no policy text currently asks for it by function.

---

## 5. Rankings and scores

Package labels in the tables: `D·` = `rund`, `F·` = `runf`, `G·` = `rung`. IOI and expected chance are on a percentage scale; differences between them are in percentage points.

### 5.1 The scoring model

**Layer 1: document rubrics.** These are the nine-package ranking's rubrics, weights unchanged.

| Document | Formula |
|---|---|
| CV | .26 coverage (K) + .20 evidence (E) + .18 mechanics (M) + .14 altitude (A) + .12 calibration (C) + .10 Norwegian (N) |
| Letter | .22 specificity (S) + .20 judgement (J) + .18 conversion (K) + .16 architecture (A) + .14 calibration (C) + .10 prose (N) |
| Package | .26 combined coverage (G) + .22 division of labour (R) + .20 set mechanics (M) + .16 consistency (X) + .16 credibility posture (Z) |

- **One convention is added for cross-vacancy use.** Every sub-score is judged against the best package the frozen authorities could support *for that vacancy*.
- A package for a stretch vacancy can therefore score high if it is well executed.
- Fit enters only in layer 4. All sub-scores are in appendix E.

**Layer 2: compound.**
- The compound is a weighted geometric mean: CV .35 · letter .35 · package .30, the same weighting the curated-package interview model uses for its gates. A weak document cannot be averaged away.
- For **CV-only instruments** (Visma, Norwegian) the letter is excluded: CV .65 · package .35.

**Layer 3: interview-odds index (IOI).**
- A logistic maps the compound to a percentage scale calibrated to the curated-package notes' four anchors:
  - b5104f 39.8%;
  - the curated package 31.8%;
  - an average package about 22%;
  - an excellent one about 45%.
- The fitted formula is `IOI = 1 / (1 + exp(−0.0769 × (compound − 91.86)))`. Run on the published document scores, it returns b5104f **42.2** and the curated package **33.2**, within 2.5 points of the gate model.
- Knock-out cues then multiply the odds, as in that model:

  | Cue | Multiplier |
  |---|---|
  | CV over two pages | ×0.70 |
  | Letter over one page | ×0.75 |
  | Self-disqualifying statement on an advertised requirement | ×0.85 |
  | Employer-blind letter | ×0.85 |

- The `runf` overruns are **tail-only**, two to four lines on page 3. The nominal tables still apply ×0.70, and the Monte Carlo samples ×0.70–0.90.

**Layer 4: expected interview chance.**
- The IOI's odds are multiplied by a **vacancy-fit factor**, with Avinor = 1.0 by definition.
- The factor captures what execution cannot change: unmet minimums, missing domains and level.
- Treat it as an editorial judgement and read the resulting column as a send-priority signal.

| Vacancy | Fit | Why |
|---|---:|---|
| Statnett, prosjektcontroller | 1.25 | Economics master plus month close, budget, forecasts and project economics: the ad's core |
| Abacus, ERP-rådgiver track | 1.10 | Junior-track minimum met through economics and systems work; finance-process vocabulary is direct |
| EIE, systemkoordinator | 0.95 | Economics/IT entry accepted; KI superuser and user support are direct; no real-estate systems; temporary post |
| Stortinget, stab | 0.90 | Two staff units; administrative leader-group support, Decisions/Planner and HEMMELIG undocumented; five years preferred for senior |
| BearingPoint | 0.90 | Master and 2–4 years met; consulting preferred; procurement undocumented |
| BI Digital, Business Designer | 0.85 | Process, data and cost-benefit design documented; no business-design title (the ad says titles do not matter) |
| ECIT, Solution Manager | 0.85 | Lifecycle ownership documented; CRM, web, e-signing and vendor follow-up not |
| Amesto, AI Team Lead | 0.70 | Strong automation and data evidence; team-lead title, payroll and API/data-warehouse work undocumented |
| Digdir, NOBID | 0.65 | Multi-actor coordination documented; eID and Nordic domain absent |
| Nasjonalmuseet | 0.55 | Method and analysis documented; audience and commercial domain absent |
| KPMG | 0.55 | Strategic work in a large organisation is accepted; consulting, restructuring and sales absent |
| Tieto | 0.45 | The five-year minimum as change or project lead is unmet |
| Norwegian | 0.35 | Senior-manager level; regulatory domains absent; English ad |
| Visma | 0.35 | Three to five years as Product Manager required |

**Earlier corpus.**
- The nine Avinor packages and the curated package enter with their **published** CV, letter and package totals and the cues recorded in the curated-package notes.
- The notes say only b5104f and 6d65bd have no cue, but do not name 93c621's cue. It is entered as ×0.85.

**Monte Carlo (4 000 draws).** Each draw varies every uncertain element at once:

| Element | How it varies |
|---|---|
| Sub-scores | N(0, 3) each; published Avinor totals N(0, 2.5) |
| Rubric weights | Dirichlet (α = 80·w) |
| Compound weights | Dirichlet (α = 60·w) |
| Logistic | Slope U(0.065, 0.09), midpoint U(90, 93.5) |
| Cue sizes | Self-disqualification 0.80–0.90; CV overrun 0.65–0.75; tail-only overrun 0.70–0.90; two-page letter 0.70–0.80; employer-blind 0.80–0.90 |
| Fit factors | × lognormal (σ 0.25) |
| Model structure | 50/50 between the document compound and the gate model with a tone score. Gates: G1 = .40K + .30A + .20M + .10E; G2 = .30S + .25J + .20K + .15A + .10N; G3 = .35 tone + .25Z + .20R + .20X |

**How to read the numbers.**
- **Ordering and gap sizes are the robust part.** Absolute percentages inherit the Avinor applicant-pool assumptions.
- **Monte Carlo means can sit above the nominal values for `runf`.** The sampled tail penalty averages ×0.80 against the nominal ×0.70.

### 5.2 Master ranking: all 20 current-harness packages (execution; independent of fit)

| # | Package | Run | Vacancy | CV | Letter | Package | Compound | Knock-out cues | **IOI** | IOI if cues fixed | MC median rank [P10–P90] | P(top 3) |
|---:|---|---|---|---:|---:|---:|---:|---|---:|---:|---|---:|
| 1 | **D·BI** | rund | BI Digital | 84.5 | 83.4 | 84.5 | 84.1 | none | **35.5** | 35.5 | 1 [1–3] | 0.92 |
| 2 | **F·Tieto** | runf | Tieto | 85.1 | 81.6 | 83.3 | 83.3 | none | **34.1** | 34.1 | 2 [1–4] | 0.80 |
| 3 | **G·EIE** | rung | EIE | 82.6 | 81.1 | 84.9 | 82.8 | none | **33.2** | 33.2 | 3 [1–6] | 0.58 |
| 4 | **D·Statnett** | rund | Statnett | 85.5 | 79.1 | 83.6 | 82.6 | none | **33.0** | 33.0 | 4 [2–7] | 0.36 |
| 5 | **D·EIE** | rund | EIE | 82.9 | 78.4 | 84.4 | 81.7 | none | **31.5** | 31.5 | 6 [3–8] | 0.11 |
| 6 | **G·Abacus** | rung | Abacus | 83.3 | 77.5 | 83.8 | 81.4 | none | **30.9** | 30.9 | 7 [4–9] | 0.06 |
| 7 | **G·Stortinget** | rung | Stortinget | 83.4 | 76.7 | 84.8 | 81.4 | none | **30.9** | 30.9 | 7 [4–10] | 0.05 |
| 8 | **G·Norwegian** | rung | Norwegian (CV-only) | 79.5 | 83.5† | 80.8 | 80.0 | none | **28.6** | 28.6 | 9 [6–11] | 0.02 |
| 9 | **D·BearingPoint** | rund | BearingPoint | 85.0 | 76.5 | 83.0 | 81.3 | self-disq. ×0.85 | **27.4** | 30.8 | 11 [8–13] | 0.00 |
| 10 | **F·Amesto** | runf | Amesto | 83.6 | 84.7 | 80.6 | 83.1 | CV 3 pages (tail) ×0.70 | **26.2** | 33.7 | 8 [4–11] | 0.08 |
| 11 | **F·BearingPoint** | runf | BearingPoint | 83.9 | 83.2 | 80.7 | 82.7 | CV 3 pages (tail) ×0.70 | **25.7** | 33.1 | 9 [6–11] | 0.02 |
| 12 | **D·Amesto** | rund | Amesto | 83.5 | 75.0 | 81.0 | 79.7 | self-disq. ×0.85 | **25.1** | 28.2 | 13 [11–14] | 0.00 |
| 13 | **D·ECIT** | rund | ECIT | 82.0 | 75.8 | 81.7 | 79.7 | self-disq. ×0.85 | **25.0** | 28.1 | 13 [11–14] | 0.00 |
| 14 | **F·Visma** | runf | Visma (CV-only) | 81.4 | 82.2† | 78.8 | 80.5 | CV 3 pages (tail) ×0.70 | **22.6** | 29.4 | 12 [10–14] | 0.00 |
| 15 | **D·Abacus** | rund | Abacus | 82.5 | 68.3 | 80.3 | 76.6 | self-disq. ×0.85 | **20.8** | 23.6 | 15 [15–16] | 0.00 |
| 16 | **D·Stortinget** | rund | Stortinget | 73.7 | 70.2 | 75.5 | 73.0 | none | **19.0** | 19.0 | 16 [15–18] | 0.00 |
| 17 | **D·Nasjonalmuseet** | rund | Nasjonalmuseet | 80.5 | 67.6 | 76.4 | 74.5 | self-disq. ×0.85 | **18.3** | 20.9 | 17 [16–18] | 0.00 |
| 18 | **D·Digdir** | rund | Digdir | 79.8 | 65.6 | 79.0 | 74.3 | self-disq. ×0.85 | **18.1** | 20.6 | 17 [16–18] | 0.00 |
| 19 | **D·Tieto** | rund | Tieto | 81.4 | 61.7 | 75.9 | 72.3 | self-disq. ×0.85 | **15.9** | 18.2 | 19 [18–19] | 0.00 |
| 20 | **D·KPMG** | rund | KPMG | 63.6 | 62.8 | 66.9 | 64.3 | self-disq. ×0.85 | **9.3** | 10.7 | 20 [20–20] | 0.00 |

† Letter shown but excluded from the compound: the channel takes a CV only.

**Reading the table**
- **The top four are within 2.5 points, and their Monte Carlo ranks overlap.** P(top 3): `rund` BI 0.92, `runf` Tieto 0.80, `rung` EIE 0.58, `rund` Statnett 0.36. Treat them as a group.
- **The bottom is robust.** `rund` KPMG is 20th in at least 90% of draws, and `rund` Tieto is 18th or 19th in at least 80%.
- **The knock-out cues reorder the middle.**
  - `runf` Amesto and BearingPoint have the 1st and 3rd best letters, yet sit 10th and 11th nominally because of two to four lines on page 3.
  - With two-page CVs they would be 3rd and 5th.
  - Every `rund` package from 9th to 19th that carries a cue carries the self-disqualification cue.
- **`rund` spans the whole table.** Two of its packages are top 4; the bottom six are all `rund`. The cheap tier's weakness was variance more than average quality.

### 5.3 Expected interview chance (fit-adjusted): the send-priority list

| # | Package | Vacancy | Fit factor | IOI (execution) | **Expected interview chance** | If cues fixed | MC median rank [P10–P90] |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | **D·Statnett** | Statnett | 1.25 | 33.0 | **38.1** | 38.1 | 2 [1–5] |
| 2 | **G·Abacus** | Abacus | 1.10 | 30.9 | **32.9** | 32.9 | 4 [1–7] |
| 3 | **G·EIE** | EIE | 0.95 | 33.2 | **32.1** | 32.1 | 4 [1–8] |
| 4 | **D·BI** | BI Digital | 0.85 | 35.5 | **31.9** | 31.9 | 4 [1–8] |
| 5 | **D·EIE** | EIE | 0.95 | 31.5 | **30.4** | 30.4 | 5 [2–9] |
| 6 | **G·Stortinget** | Stortinget | 0.90 | 30.9 | **28.7** | 28.7 | 6 [2–10] |
| 7 | **D·BearingPoint** | BearingPoint | 0.90 | 27.4 | **25.4** | 28.6 | 8 [4–12] |
| 8 | **F·BearingPoint** | BearingPoint | 0.90 | 25.7 | **23.7** | 30.8 | 7 [3–11] |
| 9 | **D·Abacus** | Abacus | 1.10 | 20.8 | **22.4** | 25.4 | 10 [6–13] |
| 10 | **D·ECIT** | ECIT | 0.85 | 25.0 | **22.1** | 25.0 | 10 [6–13] |
| 11 | **F·Amesto** | Amesto | 0.70 | 26.2 | **19.9** | 26.2 | 10 [5–13] |
| 12 | **D·Amesto** | Amesto | 0.70 | 25.1 | **19.0** | 21.6 | 12 [8–15] |
| 13 | **F·Tieto** | Tieto | 0.45 | 34.1 | **18.9** | 18.9 | 12 [8–15] |
| 14 | **D·Stortinget** | Stortinget | 0.90 | 19.0 | **17.4** | 17.4 | 13 [10–16] |
| 15 | **D·Digdir** | Digdir | 0.65 | 18.1 | **12.5** | 14.4 | 16 [14–18] |
| 16 | **G·Norwegian** | Norwegian | 0.35 | 28.6 | **12.3** | 12.3 | 16 [13–18] |
| 17 | **D·Nasjonalmuseet** | Nasjonalmuseet | 0.55 | 18.3 | **11.0** | 12.7 | 17 [15–19] |
| 18 | **F·Visma** | Visma | 0.35 | 22.6 | **9.3** | 12.7 | 17 [15–19] |
| 19 | **D·Tieto** | Tieto | 0.45 | 15.9 | **7.9** | 9.1 | 19 [17–20] |
| 20 | **D·KPMG** | KPMG | 0.55 | 9.3 | **5.3** | 6.2 | 20 [19–20] |

**Deadlines change what this list means in practice.**
- Statnett, BI, Digdir and Nasjonalmuseet closed 13.09, and Stortinget closed 14.09.
- **Still open, in order of expected chance:**
  1. `rung` Abacus
  2. `rung` EIE
  3. BearingPoint (`runf`, once compacted)
  4. ECIT (`rund`, after its edit)
  5. Amesto (`runf`, once compacted)
  6. Tieto (`runf`)
  7. Norwegian (`rung`, in English)
  8. Visma (`runf`, compacted; closes 30.09)
  9. KPMG (rework)

### 5.4 Same-vacancy head-to-heads (the clean comparison)

| Vacancy | Old (rund) | New | CV old → new | Letter old → new | Package old → new | IOI old → new | Δ IOI | Expected chance old → new | Winner |
|---|---|---|---|---|---|---|---:|---|---|
| Tieto | D·Tieto | F·Tieto | 81.4 → 85.1 | 61.7 → 81.6 | 75.9 → 83.3 | 15.9 → 34.1 | +18.2 | 7.9 → 18.9 | **F·Tieto** |
| BearingPoint | D·BearingPoint | F·BearingPoint | 85.0 → 83.9 | 76.5 → 83.2 | 83.0 → 80.7 | 27.4 → 25.7 | -1.8 | 25.4 → 23.7 | **D·BearingPoint** |
| Amesto | D·Amesto | F·Amesto | 83.5 → 83.6 | 75.0 → 84.7 | 81.0 → 80.6 | 25.1 → 26.2 | +1.2 | 19.0 → 19.9 | **F·Amesto** |
| Stortinget | D·Stortinget | G·Stortinget | 73.7 → 83.4 | 70.2 → 76.7 | 75.5 → 84.8 | 19.0 → 30.9 | +11.9 | 17.4 → 28.7 | **G·Stortinget** |
| EIE | D·EIE | G·EIE | 82.9 → 82.6 | 78.4 → 81.1 | 84.4 → 84.9 | 31.5 → 33.2 | +1.8 | 30.4 → 32.1 | **G·EIE** |
| Abacus | D·Abacus | G·Abacus | 82.5 → 83.3 | 68.3 → 77.5 | 80.3 → 83.8 | 20.8 → 30.9 | +10.1 | 22.4 → 32.9 | **G·Abacus** |

**Sub-score movement, new minus `rund`, per matched pair:**

| Vacancy | CV K | CV E | CV M | CV A | CV C | CV N | L S | L J | L K | L A | **L C** | L N | P G | P R | P M | P X | **P Z** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Tieto (F) | +6 | +6 | +2 | +6 | -6 | +4 | +14 | +16 | +8 | +26 | +53 | +6 | +8 | +4 | -2 | -2 | +32 |
| BearingPoint (F) | +8 | +6 | -28 | +2 | +2 | +2 | +6 | +4 | +4 | +0 | +26 | +2 | +6 | -6 | -24 | +0 | +14 |
| Amesto (F) | +4 | +4 | -18 | +4 | +4 | +4 | +8 | +6 | +2 | +4 | +38 | +4 | +4 | -6 | -20 | +0 | +24 |
| Stortinget (G) | +16 | +8 | +12 | +14 | +2 | -4 | +10 | +4 | +10 | +4 | +6 | +2 | +12 | +18 | +6 | +0 | +6 |
| EIE (G) | +0 | -4 | +0 | +2 | +2 | +0 | +6 | -6 | +0 | +4 | +14 | +0 | -2 | +2 | +0 | +0 | +4 |
| Abacus (G) | +2 | -4 | +2 | +2 | +2 | +2 | +10 | -4 | +2 | +20 | +26 | +6 | +0 | +6 | +0 | +0 | +14 |
| **Mean** | **+6.0** | **+2.7** | **-5.0** | **+5.0** | **+1.0** | **+1.3** | **+9.0** | **+3.3** | **+4.3** | **+9.7** | **+27.2** | **+3.3** | **+4.7** | **+3.0** | **-6.7** | **-0.3** | **+15.7** |

**Where the movement is**
- **The largest movement by far is letter calibration (+27.2).** That is the volunteered-limitation defect disappearing.
- **Package credibility posture (+15.7) follows from it.**
- **Letter architecture (+9.7) and employer specificity (+9.0)** come next: better openings and conversions.
- **Mechanics is the only dimension that went backwards** (CV −5.0, set −6.7), entirely because of the three `runf` overruns.
- **Stortinget moved the most in the CV (+16 coverage).** That is the §5.2 notes line plus KI demoted from the lead.

**The one reversal is BearingPoint.**
- `rund`'s version still carries a closing concession (×0.85).
- `runf`'s carries a three-page CV (×0.70).
- The mechanical defect costs more than the rhetorical one. Compacting the `runf` CV takes about 10 minutes and gives the best BearingPoint package in the corpus (IOI 33.1).

### 5.5 Arm league table

| Arm | n | Mean CV | Mean letter | Mean package | Mean compound | Packages with a knock-out cue | **Mean IOI** | Mean IOI if cues fixed | MC mean IOI [5–95%] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| rung | 4 | 82.2 | 79.7 | 83.6 | 81.4 | 0/4 | **30.9** | 30.9 | 30.6 [26.2–34.7] |
| runf | 4 | 83.5 | 82.9 | 80.9 | 82.4 | 3/4 | **27.2** | 32.6 | 29.3 [25.0–33.5] |
| Avinor 0.9.x | 9 | 80.3 | 80.2 | 80.1 | 80.2 | 7/9 | **25.5** | 29.3 | 25.6 [21.9–29.2] |
| rund | 12 | 80.4 | 72.0 | 79.3 | 77.0 | 8/12 | **23.2** | 25.0 | 22.7 [18.6–26.7] |
| curated (human, Avinor) | 1 | 84.0 | 79.0 | 86.0 | 82.8 | 0/1 | **33.2** | 33.2 | — |

**Monte Carlo contrasts:**

| Contrast (execution IOI, percentage points) | Mean | 90% interval | P(> 0) |
|---|---:|---|---:|
| F3 minus D3 | +8.5 | [+4.9, +11.8] | 1.00 |
| G3 minus D3 | +8.1 | [+6.2, +10.2] | 1.00 |
| New6 minus D6 | +8.3 | [+6.1, +10.5] | 1.00 |
| G mean minus F mean | +1.3 | [-1.6, +4.2] | 0.75 |
| D mean minus Avinor-9 mean | -2.9 | [-5.0, -0.8] | 0.01 |
| G mean minus Avinor-9 mean | +5.0 | [+2.8, +7.2] | 1.00 |
| F mean minus Avinor-9 mean | +3.7 | [+1.0, +6.5] | 0.99 |

**Reading the contrasts**
- **The matched contrasts are robust.** Both new arms beat `rund` on their three shared vacancies in every draw, by similar amounts.
- **`rung` versus `runf` is not robust** (P = 0.75), and it is confounded with vacancy type anyway.
  - If a tail-only spill costs ×0.90 rather than ×0.70, `runf`'s mean rises to about 30.9 and ties `rung`.
  - Compacted, `runf` leads (32.6).
- **Arm against the earlier Avinor corpus.**
  - `rund` sits slightly below the nine high-budget Avinor packages on execution (−2.9, P(>0) = 0.01).
  - Both new arms sit above them (+3.7 and +5.0).
  - Different vacancies and a different reviewer's published scores make this the least certain row. What it supports: moderate budgets with 4-job chats reach at least the execution level of the near-unlimited-budget corpus.
- **The human-curated package (33.2) is above every arm mean** but below the best individual packages: `rund` BI 35.5, `runf` Tieto 34.1, `rung` EIE 33.2.

### 5.6 Cross-corpus ranking: 30 packages on one scale

| # | Package | Run family | Vacancy | CV | Letter | Package | Compound | Knock-out cues | **IOI** | IOI if cues fixed | MC median rank [P10–P90] |
|---:|---|---|---|---:|---:|---:|---:|---|---:|---:|---|
| 1 | b5104f | Avinor 0.9.x | Avinor | 88 | 90 | 85 | 87.8 | none | **42.2** | 42.2 | 1 [1–1] |
| 2 | D·BI | rund | BI Digital | 84 | 83 | 84 | 84.1 | none | **35.5** | 35.5 | 3 [2–5] |
| 3 | F·Tieto | runf | Tieto | 85 | 82 | 83 | 83.3 | none | **34.1** | 34.1 | 4 [2–6] |
| 4 | Curated (cherry-picked) | curated | Avinor | 84 | 79 | 86 | 82.8 | none | **33.2** | 33.2 | 4 [2–9] |
| 5 | G·EIE | rung | EIE | 83 | 81 | 85 | 82.8 | none | **33.2** | 33.2 | 5 [3–8] |
| 6 | D·Statnett | rund | Statnett | 86 | 79 | 84 | 82.6 | none | **33.0** | 33.0 | 6 [3–9] |
| 7 | D·EIE | rund | EIE | 83 | 78 | 84 | 81.7 | none | **31.5** | 31.5 | 8 [5–11] |
| 8 | G·Abacus | rung | Abacus | 83 | 77 | 84 | 81.4 | none | **30.9** | 30.9 | 9 [6–12] |
| 9 | G·Stortinget | rung | Stortinget | 83 | 77 | 85 | 81.4 | none | **30.9** | 30.9 | 9 [6–13] |
| 10 | G·Norwegian | rung | Norwegian | 80 | 84 | 81 | 80.0 | none | **28.6** | 28.6 | 12 [8–16] |
| 11 | D·BearingPoint | rund | BearingPoint | 85 | 77 | 83 | 81.3 | self-disq. ×0.85 | **27.4** | 30.8 | 15 [11–18] |
| 12 | 3eeb10 | Avinor 0.9.x | Avinor | 82 | 79 | 82 | 80.9 | employer-blind ×0.85 | **26.8** | 30.2 | 15 [9–19] |
| 13 | 0fa53b-opusx | Avinor 0.9.x | Avinor | 85 | 81 | 81 | 82.4 | letter 2 pages ×0.75 | **26.6** | 32.5 | 15 [10–19] |
| 14 | 3eeb10-stage1 | Avinor 0.9.x | Avinor | 80 | 86 | 84 | 83.3 | CV 3 pages ×0.70 | **26.5** | 34.0 | 15 [9–20] |
| 15 | F·Amesto | runf | Amesto | 84 | 85 | 81 | 83.1 | CV 3 pages (tail) ×0.70 | **26.2** | 33.7 | 10 [6–15] |
| 16 | 6d65bd | Avinor 0.9.x | Avinor | 78 | 77 | 80 | 78.2 | none | **26.0** | 26.0 | 16 [11–20] |
| 17 | F·BearingPoint | runf | BearingPoint | 84 | 83 | 81 | 82.7 | CV 3 pages (tail) ×0.70 | **25.7** | 33.1 | 12 [8–16] |
| 18 | D·Amesto | rund | Amesto | 84 | 75 | 81 | 79.7 | self-disq. ×0.85 | **25.1** | 28.2 | 19 [15–21] |
| 19 | D·ECIT | rund | ECIT | 82 | 76 | 82 | 79.7 | self-disq. ×0.85 | **25.0** | 28.1 | 18 [15–20] |
| 20 | F·Visma | runf | Visma | 81 | 82 | 79 | 80.5 | CV 3 pages (tail) ×0.70 | **22.6** | 29.4 | 17 [13–21] |
| 21 | 0fa53b-solxh | Avinor 0.9.x | Avinor | 80 | 76 | 75 | 77.1 | self-disq. ×0.85 | **21.4** | 24.3 | 22 [19–25] |
| 22 | D·Abacus | rund | Abacus | 83 | 68 | 80 | 76.6 | self-disq. ×0.85 | **20.8** | 23.6 | 23 [21–25] |
| 23 | 0fa53b-solmed | Avinor 0.9.x | Avinor | 77 | 74 | 78 | 76.2 | self-disq. ×0.85 | **20.4** | 23.1 | 23 [21–26] |
| 24 | 93c621 | Avinor 0.9.x | Avinor | 76 | 75 | 77 | 75.9 | self-disq. ×0.85 | **20.0** | 22.7 | 23 [21–26] |
| 25 | 0fa53b | Avinor 0.9.x | Avinor | 77 | 84 | 79 | 80.0 | CV 3 pages ×0.70, self-disq. ×0.85 | **19.3** | 28.6 | 24 [21–28] |
| 26 | D·Stortinget | rund | Stortinget | 74 | 70 | 76 | 73.0 | none | **19.0** | 19.0 | 26 [23–28] |
| 27 | D·Nasjonalmuseet | rund | Nasjonalmuseet | 80 | 68 | 76 | 74.5 | self-disq. ×0.85 | **18.3** | 20.9 | 27 [25–28] |
| 28 | D·Digdir | rund | Digdir | 80 | 66 | 79 | 74.3 | self-disq. ×0.85 | **18.1** | 20.6 | 27 [25–28] |
| 29 | D·Tieto | rund | Tieto | 81 | 62 | 76 | 72.3 | self-disq. ×0.85 | **15.9** | 18.2 | 29 [28–29] |
| 30 | D·KPMG | rund | KPMG | 64 | 63 | 67 | 64.3 | self-disq. ×0.85 | **9.3** | 10.7 | 30 [30–30] |

**Reading the table**
- **b5104f stays first in at least 90% of draws.** It is still the only package with a converted employer fact and a question-shaped close.
- **Four of the top six are current-harness packages** (`rund` BI and Statnett, `runf` Tieto, `rung` EIE), written in about 3 (`rund`) to 19 (`runf` Tieto) wall-clock minutes per job across both stages.
- **The two high-budget Avinor packages that lost a quarter to a third of their odds to a single page-length cue** sit directly beside `runf` Amesto (#15) and BearingPoint (#17), for the same kind of reason: `0fa53b-opusx` (two-page letter, #13) and `3eeb10-stage1` (three-page CV, #14). `0fa53b` carries a three-page CV *and* a self-disqualification cue, so it falls to #25. The defect class is budget-independent.

### 5.7 Best package per vacancy across all runs

| Vacancy | Fit factor | Best package to send | Its expected chance | Alternative | Alternative's chance | Best after cheap fixes |
|---|---:|---|---:|---|---:|---|
| Statnett | 1.25 | **D·Statnett** | 38.1 | — | — | D·Statnett 38.1 |
| Abacus | 1.10 | **G·Abacus** | 32.9 | D·Abacus | 22.4 | G·Abacus 32.9 |
| EIE | 0.95 | **G·EIE** | 32.1 | D·EIE | 30.4 | G·EIE 32.1 |
| BI Digital | 0.85 | **D·BI** | 31.9 | — | — | D·BI 31.9 |
| Stortinget | 0.90 | **G·Stortinget** | 28.7 | D·Stortinget | 17.4 | G·Stortinget 28.7 |
| BearingPoint | 0.90 | **D·BearingPoint** | 25.4 | F·BearingPoint | 23.7 | F·BearingPoint 30.8 |
| ECIT | 0.85 | **D·ECIT** | 22.1 | — | — | D·ECIT 25.0 |
| Amesto | 0.70 | **F·Amesto** | 19.9 | D·Amesto | 19.0 | F·Amesto 26.2 |
| Tieto | 0.45 | **F·Tieto** | 18.9 | D·Tieto | 7.9 | F·Tieto 18.9 |
| Digdir | 0.65 | **D·Digdir** | 12.5 | — | — | D·Digdir 14.4 |
| Norwegian | 0.35 | **G·Norwegian** | 12.3 | — | — | G·Norwegian 12.3 |
| Nasjonalmuseet | 0.55 | **D·Nasjonalmuseet** | 11.0 | — | — | D·Nasjonalmuseet 12.7 |
| Visma | 0.35 | **F·Visma** | 9.3 | — | — | F·Visma 12.7 |
| KPMG | 0.55 | **D·KPMG** | 5.3 | — | — | D·KPMG 6.2 |

**Hybrids worth considering.**
- **EIE:** the `rung` package plus `rund`'s Sector Alarm sentence.
- **Stortinget:** the `rung` package plus a §5.2 notes sentence in the letter.
- **BearingPoint:** the `runf` letter with a CV compacted to two pages.

### 5.8 Stage-level scorecards

The stages are scored separately so that the model-versus-harness reasoning in §6 has numbers under it. Criterion scores are editorial judgements drawn from the strategies, overrides and reviews already cited.

**Stage 1 (Decision Architecture)**

| Criterion (weight) | What it measures | `rund` | `runf` | `rung` |
|---|---|---:|---:|---:|
| Recall breadth (.25) | Cross-cutting sections and project coverage cited where the ad needs them | 35 | 85 | 65 |
| Field hygiene (.20) | Gaps kept out of `top_employer_problems`, `backbone` and `structure_guidance` | 30 | 95 | 85 |
| Requirement labelling (.15) | Either/or handled; ADJACENT and SUPPORTED accurate | 50 | 60 | 70 |
| Route quality (.20) | A carrying pair Stage 3 could keep | 60 | 85 | 78 |
| Restraint (.10) | No overstatement in thesis, objections or bridge | 90 | 70 | 70 |
| Depth (.10) | Ceilings, units and facets Stage 3 can use | 45 | 95 | 60 |
| **Stage-1 score** | | **47.8** | **82.8** | **72.4** |

**Stage 3 (Elastic Final Writer)**

| Criterion (weight) | What it measures | `rund` | `runf` | `rung` |
|---|---|---:|---:|---:|
| Elastic repair (.15) | Catches Stage-1 errors in both directions, and source ambiguity | 85 | 90 | 80 |
| Selection and conversion (.20) | Evidence turned into the employer's problem | 78 | 90 | 85 |
| Letter calibration (.20) | No volunteered limitation; hedges placed cheaply | 35 | 92 | 88 |
| CV discipline (.15) | Pages, headline, person, bullet length | 85 | 45 | 80 |
| Formula resistance (.10) | Openings, closes and bridges varied inside the chat | 40 | 55 | 50 |
| Source fidelity (.10) | Ceilings, status, attribution; no documentation voice | 85 | 86 | 84 |
| Triage and review use (.10) | CHECK used when warranted; no apply/no-apply advice | 35 | 45 | 55 |
| **Stage-3 score** | | **64.1** | **75.3** | **77.5** |

**Budget lens, matched vacancies, wall-clock as a proxy**

| Arm | IOI gain over `rund` | Extra minutes per job | Gain per extra minute |
|---|---:|---:|---:|
| `rung` | +8.0 | +4.2 | **≈1.9** |
| `runf` | +5.9 | +8.7 | ≈0.7 (≈1.2 once the CVs are compacted) |

`rung`'s allocation bought about twice the improvement per extra minute that `runf`'s did. Most of `runf`'s extra Stage-1 depth did not reach the reader: it reached page 3.

---

## 6. How the latest changes manifested: model versus harness

### 6.1 The core inference

`rund`, `runf` and `rung` ran on identical frozen policy. Each behaviour therefore falls into one of three kinds:

1. **Present in `rund`, absent from both new arms.** The policy text allows it but does not produce it. It needs a cheaper model, a 12-job chat, or both.
2. **Present in all three arms.** It is shaped by the harness, the source or the template, or it is common to every model tried so far. That is where edits to policy, source or template still pay.
3. **Present in one new arm only.** It is a chat-local or model-specific style, and it will recur in some other form in the next chat.

A fourth kind comes from the stronger models themselves: **behaviour absent from `rund` that appears in the new arms**, such as Stage-1 overreach and page overruns.

### 6.2 Tendency-by-tendency re-attribution

| # | Tendency (previous report) | `rund` | `runf` | `rung` | Verdict | Confidence | Consequence for the plan |
|---|---|---|---|---|---|---|---|
| T1 | Volunteered limitations in the letter | 10/12 | 0/4 | 0/4 (+1 mild learning line) | **Model-driven** (one or both stages). The policy permits it but does not produce it | High | E-1, E-10 → cheap-tier guardrails; E-5 kept; **2×2 test first** |
| T1a | Gaps written into Stage-1 positive fields | 11/12 | 0/4 | 0/4 (1 learning instruction in SG) | Model-driven; the field semantics still propagate when present | High | E-5 kept as a guardrail |
| T2 | Cross-cutting evidence does not reach the documents | S1 0/12; S3 1/12 | S1 4/4; S3 2/4 | S1 4/4; S3 2/4 | **Split.** Stage-1 recall is model-driven; Stage-3 under-use is a surface problem | High / medium | E-6 kept (the surface) |
| T3 | Thin, decaying Stage 1 | 17 → 9 KB; 10/12 understatement repairs | Flat ~40 KB; 1/4 | Flat ~19 KB; 1/4 | **Model plus chat length** | Medium | Keep 4-job chats |
| T4 | Homogenisation inside a chat | Stock close 11/12; cleft 10/12 | Identity opening 4/4; bridge 4/4 | Title restatement 4/4; bridge 4/4 | **Convergence is chat-level at every tier.** The formula is model-specific. Two families are policy-shaped: the invitation close (V) and the transfer bridge (K + lock) | High | E-7 reworded to function level; new bridge text (E-18) |
| T5 | CV and letter do the same work | shared5 .10 | .065 | .045 | Partly model (better), partly harness (anchor licence) | Medium | E-8 kept, low priority |
| T6 | Bolt-on coverage sentences | 5/12 | 2/4 | 4/4 (7 markers) | Present in all arms; step-5 add-on reading | Medium | E-9 kept, low |
| T7a | Three-item list headlines | 11/12 | 0/4 | 0/4 | Model-driven | High | E-11 text demoted |
| T7b | Headline wraps | 8/11 | 3/4 | 2/4 | **Harness**: all-caps headline, no feedback | High | Render warning (E-11 companion) kept |
| T7c | "Avviklet" as the last word | 5/12 | 3/4 | 1/4 | **Harness**: no rule | High | E-7 part 2 kept |
| T7d | Moral and lesson sentences | 5/12 | Replaced by bridges | Replaced by bridges | Migrated, not removed | Medium | See T4 |
| T8 | Triage without signal; apply/no-apply nudges | READY 12/12; 3 nudges | READY; 2 nudges | READY; 1 soft nudge | **Harness** (triage table, prompt), tier-independent | High | E-3 kept **high**; post-render flag added |
| T9 | Template residue (bold support sections, metadata) | Yes | Yes | Yes | **Template**, deterministic | High | §7.4 unchanged |
| T10 | Process and provenance | Wrong ledger | Wrong ledger, relabelled role, renamed PDFs | Same | **Operator** | High | §7.5 checklist |

**T1: the chain re-examined.** The previous report traced six links. This is where each one stands now.

1. **Stage 1 writing gaps into positive fields.**
   - It happened in 11 of 12 `rund` strategies and 0 of 8 new ones.
   - `rung` Abacus still shows the link can transmit. Stage 1's `structure_guidance` said "Avslutt på BNXT-læring", and a stronger Stage 3 wrote "Selve produktet skal jeg lære". The line was softened but still transmitted.
   - **The field semantics matter at every tier. Cheap models simply trigger them far more often.**
2. **The M01 sentence "retain the gap".** It was not misread by stronger Stage-1 models. No evidence it harms them.
3. **The Stage-3 and prompt asymmetry ("overclaim is the worse failure").** Unchanged, and it produced no gap sentences in the new arms. It did produce four correct overstatement repairs. **It is an asset, not a cause** (§6.3, N4).
4. **K rule 5 ("behold et uttrykkelig forbehold …").** Unchanged, and no forbehold in any new letter. Stronger writers read it as the narrow licence it is.
5. **The content lock protecting caveats.** Unchanged and inert, because nothing needed protecting.
6. **Triage blind to persuasion.** Unchanged, and still blind (T8).

**What is left unidentified.** Both stages changed together, so these runs cannot say whether a strong Stage 3 alone would have suppressed the gap sentences Terra's strategies invited. That is the most valuable open question for budget design, and it is cheap to answer (§7.2).

### 6.3 New tendencies

**N1: CV capacity overrun, `runf` 3/4.**

*How it happens*
- A deep Stage 1 (7 evidence units, 17–21 references) feeds a Stage 3 licensed to use what helps.
- Nothing tells the writer how much two pages hold.
- The render warning arrives after finalize and is not shown in the queue.

*Empirical capacity with the current masters and baseline tail*

| CV words (profile + bullets) | Packages | Rendered |
|---|---|---|
| 322–450 | every `rund` and `rung` CV, plus `runf` Tieto | 2 pages |
| 522–533 | `runf` BearingPoint, Amesto, Visma | 3 pages; page 3 holds only the tail |

- The tail on page 3 is REFERANSER (Amesto) or KURS plus REFERANSER (BearingPoint, Visma).
- **Practical capacity is therefore about 480–500 words**, and a compacted tail would add about 20–30 words.

*Why it matters*
- The curated-package notes warned that "adding evidence is exactly how that happens".
- The nine-package ranking named the other half: "the framework has a compression order and no compression budget".
- `rund` (at most 441 words) never needed one. `runf` did.

**N2: formula convergence survives 4-job chats.**
- Each chat settled on its own opening family and a shared bridge frame (T4).
- Adjacent jobs share more wording than distant ones.
- Stage-3 time per job fell by 60–70% across each chat. Later letters are written largely from the earlier ones in context.

**N3: the V example primes an ownership overclaim.**
- **The example.** FORFATTERSTEMME line 60, under the verb-and-subject guidance: *«Jeg moderniserte verktøyet» framfor «moderniseringen av verktøyet ble gjennomført»*.
- **The source record it collides with.** The only "verktøy" in the corpus that was modernised is PRJ-03. Its ceiling (WORK §4.3) says: *"Never claim … sole ownership of the complete modernization"*; §0.3 adds *"ingen eierskap til hele moderniseringen"*.
- **Occurrences:**
  - `rund` KPMG CV: *"Moderniserte et arvet, virksomhetskritisk Excel/VBA-verktøy"*;
  - `runf` Tieto CV: *"Moderniserte sykehusets om lag 20 år gamle budsjetteringsverktøy"*;
  - `rung` Norwegian Stage 1: *"har modernisert et virksomhetskritisk arbeidsverktøy"*, repaired by its Stage 3.
- **Status.** The priming is inference, not proof. The example is nonetheless the only place in the policy that models this exact claim in the first person, and it costs one line to replace.

**N4: Stage-1 overreach at stronger tiers, caught every time.**

| Overstatement in Stage 1 | Job |
|---|---|
| "har modernisert" | `rung` Norwegian |
| "om lag 3,5 år med funksjonelt eierskap" | `runf` Visma |
| "besvarer KI-henvendelser" | `rung` EIE |
| Onboarding as the cause of the tool's value | `runf` Tieto |

- All four were written into positive fields (thesis, objection response, bridge), and Stage 3 removed all four.
- This is the design working. It also means a cheaper or weaker Stage 3 paired with a strong Stage 1 is the one untested combination with a known new risk.

**N5: an ambiguous digest row, caught by `runf` and silently avoided by `rung`.**
- WORK §0.3 row *OUS — tidlig BAR-arbeid*: *"gikk fra kvalitetssikring av andre til selvstendig gjennomføring"*.
- WORK §1.1: *"Arbeidet ble kvalitetssikret av andre i starten"*.
- The digest is what Stage 3 reads first. A writer that trusts it would claim that Vegard quality-assured others in the first months.
- No package made that claim. It is a latent trap for any Stage 3 that does not open §1.1.

**N6: documentation voice is a property of the source phrase.**
- CLM-BAR-004: *"Fordelingen av saker var etterspørselsstyrt og avhang av økonomilederens kapasitet."*
- Two different models, `rund` and `rung`, wrote it into the Stortinget letter and CV as *"etter hva økonomileder hadde kapasitet til"*.
- K already says not to carry the source's documentation voice. The phrase is a boundary note that reads like an evidence atom, so move it to the boundary column.

**N7: first person in the CV.**
- Two `rung` profiles use *jeg*. No policy sentence sets the CV's grammatical person, and every other generated and curated CV uses the implied subject.

**N8: channel and language.**
- CV-only instruments (Visma, Norwegian) were handled well inside the packages: optional letters and advice to answer the form questions.
- The English ad was not handled outside them. It was run as CORE, and only the review mentions the missing English version.
- The harness deliberately has no channel or language switch (DEC-01/02/04), so the remedy belongs in operator practice and the EXCEPTION class.

**N9: review, render and queue are out of step.**
- Triage is decided before render, so no review can see a page overrun.
- The queue view lists triage and render state but not the render warnings.
- Renaming a PDF after render makes the queue report `render: FAILED` and advise a re-render, although the file is intact.

### 6.4 What M01–M06 did under stronger models

| Plan item | Observed in `rund` (cheap) | Observed in `runf` and `rung` (stronger) | Revised reading |
|---|---|---|---|
| **M01** material-question allocation | Coverage bolted on; "retain the gap" read as "surface the gap" | Coverage broad (10–21 refs); gaps retained in review and objections; fewer bolt-ons in `runf`, more in `rung` | **Works with capable models.** The misreading is a cheap-tier artefact (guardrail E-5) |
| **M02** substantive pair edit | Joins right, duplication unchanged | Shared 5-grams down (.10 → .055); status sentences still in both documents | **Partly effective**; the anchor licence still lets status sentences through (E-8) |
| **M03** K correction | "ikke innført" fixed; gap clauses worse | "ikke innført" 0; gap clauses 0; strong verbs kept, once too strong ("Moderniserte") | **Worked.** The gap clauses were never M03's doing |
| **M06** defensible fit, headline role, ordinary close | Forced uniqueness gone; headlines unchanged; stock close 11/12 | Forced uniqueness gone; list headlines gone (0/8) but 5/8 wrap; stock sentence 2/8, but an invitation close 8/8 | **Headline sentence works for capable models but needs render feedback.** The close wording yields invitation formulas at every tier |
| **M04** register dial level 2 | Small; conflict framing 4/12 | Conflict framing 4/8 (2 turned into a skill); no self-ranking; documentation voice survives | **Small effect**; cannot see source-phrase leakage |
| **M05** masters and consumers | Competence block and title fixed; support sections bold | Same | **Deterministic**; the un-bolding item is still open |

### 6.5 What the previous report got wrong, and what it got right

**Wrong or overstated**

1. **It put policy text at the centre of T1.**
   - The evidence then was consistent with that. The evidence now shows the texts do not generate gap sentences in capable models.
   - The previous report's own confidence labels ("high confidence on 1–4") were too high for links 3–5.
2. **It ranked E-1 first.**
   - For capable tiers E-1 is inert. It remains a cheap guardrail for cheap tiers, so it should be demoted, not dropped.
3. **E-4 would have weakened the most valuable Stage-3 behaviour at stronger tiers.**
   - It proposed replacing "overclaim is the worse of the two failures" with symmetry.
   - Stage 3's overclaim guard caught four Stage-1 overstatements here. The new drift bullet stays; the replacement sentence goes.
4. **It said "Stage 1's cheap-model value is recall, not judgement" and advised spending on Stage 3.**
   - Stronger Stage-1 models also improved field hygiene, labelling and route stability. Understatement repairs fell from 10 of 12 to 2 of 8.
   - At `rung`'s size, Stage-1 spend had the best return in this dataset (§5.8).
5. **"Buying back Stage-1 capability is not recommended before E-5/E-6" was too categorical.**
   - Capable Stage-1 models restored recall with no text change at all. The cheapest route to that quality is now an empirical question (§7.2).

**Right, and confirmed**

- Segmentation to four jobs or fewer: flat Stage-1 curves and no end-of-chat dip.
- Triage has lost its signal (E-3): persists at every tier.
- The retrieval surface (E-6): Stage 3 still under-uses cross-cutting evidence that Stage 1 cites.
- Template and metadata residue (§8.2): unchanged.
- Record the real model mapping: the ledger is still wrong.
- The curated notes' warning that more evidence leads to page three is now observed in three packages.

### 6.6 What this means for budget design

**Where extra spend paid**
- Stage-1 recall and field hygiene: both new arms, every job.
- Stage-3 calibration and conversion: both new arms.
- Together these removed the self-disqualification cue from 8 of 12 packages to none, and doubled the IOI on the hardest shared vacancy (Tieto 15.9 → 34.1).

**Where it did not**
- `runf`'s additional Stage-1 depth beyond `rung`'s level: 40 KB against 19 KB, and 7 evidence units against 5.
- It produced more references and a better letter, but mainly longer CVs, three of which overran.
- Per extra minute, `rung`'s allocation returned about twice as much (§5.8).

**The cheapest configuration that reaches `rung`-level quality is still unknown.** Two cheap experiments decide it, and they are cheaper than any further policy editing:

| If a strong Stage 3 on Terra strategies already removes the gap sentences | Then |
|---|---|
| Yes | Terra Stage 1 with the E-5/E-6 guardrails and a strong Stage 3 is the budget sweet spot |
| No | `rung`-size Stage-1 capability is the floor |

---

## 7. Revised optimisation plan

The ordering is by expected interview value per unit of effort, given what these runs show about tiers. The constitution still applies:
- no detectors, similarity checks or numeric judges;
- no schema growth;
- counts and pages are editorial signals only;
- K edits need **[Vegard accepts]**;
- candidate facts change only by Vegard.

Hash boundaries are noted where they matter.

### 7.0 Now (these batches)

**1. Send order for the vacancies that are still open**

| # | Package | What to do first |
|---|---|---|
| 1 | `rung` **Abacus** | Headline; add the intake-form sentence (§4.8) |
| 2 | `rung` **EIE** | Add the Sector Alarm sentence; keep one bridge; headline (§4.7) |
| 3 | `runf` **BearingPoint** | Compact the CV to two pages; headline (§4.2) |
| 4 | `rund` **ECIT** | Apply the previous report's §4.7 edits |
| 5 | `runf` **Amesto** | Compact the CV; change "features" (§4.3) |
| 6 | `runf` **Tieto** | Ownership verb; headline; quote sentence (§4.1) |
| 7 | `rung` **Norwegian** | English CV (§4.6) |
| 8 | `runf` **Visma** | Two-page CV; form answers; by 30.09 (§4.4) |
| 9 | `rund` **KPMG** | Rework as in the previous report |

**2. Closed deadlines.**
- Statnett, BI, Digdir and Nasjonalmuseet closed 13.09, and Stortinget closed 14.09.
- If any is unsent, check whether late applications are still considered.
- For Stortinget, send the `rung` package with the §4.5 edits.

**3. File hygiene.**
- Do not rename canonical outputs. Use `render --dest <folder>` or copy the files, so receipts and the queue stay valid. The three `render: FAILED` entries clear once the canonical names exist again.
- Delete the two `~$…docx` owner files once Word is closed.

**4. Pilot log.** Add a `pilot/PILOT_LOG.csv` row per submitted package, with edit minutes. That turns three arms into a cost-per-package series.

### 7.1 Status of the previous plan (E-1…E-11)

| Item | Previous claim | New evidence | New status |
|---|---|---|---|
| **E-1** Letter gap rule (S3) | #1 fix for T1 | Capable models already comply; the text is inert for them | **Demote → cheap-tier guardrail.** Shorten to its last two sentences plus "keep the gap in review" |
| **E-2** Content-lock clarification | Unlocks deletion of gaps and morals | Nothing to delete in the new arms; extra bridges now need it | **Keep, merged with E-18** (the lock protects the *only* bridge, not the third) |
| **E-3** Triage hook | READY has no signal | READY 8/8; 3 apply/no-apply nudges | **Keep, high.** Add the post-render companion (E-14) |
| **E-4** Prompt symmetry | Remove "overclaim is worse" | The overclaim guard caught 4 Stage-1 overstatements | **Reword: keep the sentence**, add only the disclosure drift bullet (text below) |
| **E-5** Gap-free positive fields + recall breadth (S1) | T1/T2/T3 | Capable models comply; the Abacus learning instruction still propagated; new overreach in positive fields | **Keep as guardrail, extended** with the qualifier clause (text below) |
| **E-6** Retrieval surface | T2 | Stage 3 still under-uses §2.2/§5.x/§6.x that Stage 1 cites; §5.2 in 1 of 8 | **Keep, medium-high** |
| **E-7** Close and opening variation + "avviklet" ending | T4, T7 | Stock close gone, but formulas migrate per chat; "avviklet" endings 4/8 | **Reword to function level** plus a prompt companion; keep part 2 unchanged |
| **E-8** Status sentences once | T5 | Improved but still verbatim | **Keep, low** |
| **E-9** Integrate coverage | T6 | Bolt-ons persist (`rung` 7 markers in 4 letters) | **Keep, low** |
| **E-10** K rule 5 scope **[Vegard accepts]** | Removes the competing licence | Rule 5 unchanged and inert for capable models | **Park** until the 2×2 test shows Stage 3 carries T1 |
| **E-11** Headline role (D) | Three-item headlines | List headlines 0/8, but 5/8 wrap in caps | **Demote the text; keep the render warning** |

**E-4 revised (STAGE3_PROMPT.md, "Where this stage drifts"; hash-free).** Leave *"over-correcting into an overclaim is the worse of the two failures"* as it is, and add:

> **Into disclosure.** A missing requirement belongs in the review. If a letter sentence says the candidate lacks, has not done or must learn something the vacancy asks for, replace it with the nearest documented evidence or delete it. A domain the reader can see is new may be named once, only when the same sentence turns it into the argument.

**E-5 extension (S1 instruction, § Encode the actual decisions; S1 hash).** Append:

> shortlist_thesis, objections and motivation_bridge carry the qualifiers of the ceilings they cite: team boundary, period, status and whose decision it was. Never compress "effectively sole coder in a broad process" into "modernised", or a bounded ownership period into years of ownership.

### 7.2 First, identify which stage carried T1: the 2×2 branch test

This is the highest information value for the least cost, and it should come **before** any E-1/E-5/E-10 editing.

**Design**

| | Stage 3 = the new, stronger Stage 3 | Stage 3 = the `rund` Stage 3 (Opus 5 medium) |
|---|---|---|
| **Stage 1 = `rund` Terra strategies** | **Cell B**: branch `rund --from-stage 3`, new Stage-3 model | Cell A: observed (`rund`) |
| **Stage 1 = new strategies** | Cell D: observed (`runf`/`rung`) | **Cell C**: branch `runf`/`rung --from-stage 3`, the `rund` Stage-3 model |

**Setup**
- **Jobs:** Tieto, BearingPoint, Amesto and Abacus. All four carried the self-disqualification cue in `rund` and none in the new runs. Use one fresh chat per cell, four jobs.
- **Cost:** eight Stage-3 runs, about 30–40 wall-clock minutes. No Stage 1.
- **Hold every policy edit until both cells are done.** `branch` uses the live governing inputs.
- **Precondition: the Stage-1 role and its mapping string must be byte-identical to the parent's, or the strategies are regenerated.**
  - `_same_governing_inputs` (`runtime/jobbsok/branch.py:164-172`) reuses a strategy only when the child's `stage1` role *and* `role_mapping[that role]` equal the parent manifest's recorded values.
  - This holds even when the recorded string is wrong. A mismatch sets the strategy to REGENERATE_REQUIRED, and the final package with it, so Cell B would silently become a fresh Stage-1 run.
  - The live settings already break Cell B. `rund` recorded `SOL_CLASS = "Codex / GPT-5.6 Sol"`, while the live `settings.toml` says `"Codex / GPT-6 Astra (High)"`. Cell C (parents `runf`/`rung`) matches the live settings as they stand.
- **Settings per cell** (roles are limited to `SOL_CLASS` and `TERRA_CLASS`):
  - **Cell B:** `stage1 = "SOL_CLASS"` with `SOL_CLASS = "Codex / GPT-5.6 Sol"` restored verbatim; `stage3 = "TERRA_CLASS"` with `TERRA_CLASS` set to the true new Stage-3 model.
  - **Cell C:** `stage1 = "SOL_CLASS"` with `SOL_CLASS = "Codex / GPT-6 Astra (High)"` kept verbatim; `stage3 = "TERRA_CLASS"` with `TERRA_CLASS` set to the `rund` Stage-3 model. Do not reuse `SOL_CLASS` for Stage 3 as `rund` did; relabelling it would break reuse.
- **Record the truth where it cannot break reuse:** set the Stage-3 mapping truthfully, pass `--model-tag`, and note the real Stage-1 model beside each run ID. The Stage-3 fingerprint changing is intended here.
- **Check the disposition before spending a Stage-3 run.** `branch` prints each job's disposition, for example `strategy=REUSED, final_package=REGENERATE_REQUIRED, review=REGENERATE_REQUIRED`. Anything other than REUSED means the settings are wrong; delete nothing, fix the settings and branch again.
- **Verification level:** confirmed by reading the code; no branch was run, because this analysis may not write under `P0.9/Build`.

**Read the cells by hand, with no detector:**
- letter sentences stating an unmet listed requirement;
- the self-disqualification cue;
- CV pages;
- overstatement repairs;
- the letter rubric.

| Outcome | Meaning | Budget consequence |
|---|---|---|
| B ≈ 0 gap sentences, C ≈ 0 | **Stage 3 carries T1** | Terra-class Stage 1 plus a strong Stage 3 plus E-6/E-12/E-13 is the economy tier. E-5 stays a guardrail |
| B ≈ 0, C high | Stage 3 carries it strongly | Never pair a cheap Stage 3 with any Stage 1. Consider E-1 and E-10 only for cheap Stage-3 tiers |
| B high, C ≈ 0 | **Stage 1 carries T1** via field semantics | E-5 becomes essential for cheap Stage 1; `rung`-size Stage 1 is the floor otherwise |
| B high, C high | Both | Keep both guardrails; the economy tier is not viable without E-1 and E-5 |

### 7.3 New pitches

#### E-12 CV capacity signal (WRITING_DOCTRINE § CV, or S3 step 5; editorial, not a limit) — targets N1

Add:
> Med gjeldende maler rommer to CV-sider omtrent 480 ord i profil og punkter sammen med de faste avsnittene. Dette er redaksjonell kapasitet, ikke en grense. Når utkastet er lengre, bruk komprimeringsrekkefølgen på det CV-en og brevet sier likt før du fjerner noe som bare står ett sted.

- **Why it is allowed.** Counts are permitted as editorial signals. This one tells the writer what the render will do, instead of discovering it after finalize.
- **Why it works with E-8.** It points compression at duplicated content first. Two of the three overruns had seven letter sentences that closely duplicate a CV sentence.
- **Hash:** D affects both stages; the S3 instruction affects Stage 3 only.

#### E-13 Tail compaction and un-bolding (CV_MASTER / CV_BASELINE; deterministic) — targets N1, T9

- **Compact the tail.** Render KURS and REFERANSER as one line each, label and content on the same line, or drop "Referanser: Oppgis ved forespørsel", which Norwegian CVs commonly omit.
  - That line is **all** of `runf` Amesto's page 3, and half of BearingPoint's and Visma's.
  - The content decision is Vegard's (CV_BASELINE); the layout change belongs to the template (`prepare_masters.py`, GATE-02 note, registry refresh).
- **Un-bold the support content.** Remove `<w:b/>` from the prototypes for Tillitsverv, Språk, Kurs and Referanser (the previous report's item 8.2.1). Still open, and verified again in these PDFs.

#### E-14 Show render warnings where decisions are made (queue view; deterministic) — targets N9, T8

- Print each job's render warnings next to its triage line in `queue.md` and `status.json`, for example `render: OK · warnings: CV 3 pages`, and list them under "Ready — skim and approve".
- Optionally warn when the rendered headline takes two lines. `render.py` already reads PDF text.
- **No semantic change:** READY stays READY. The operator sees the one mechanical defect review cannot see.
- **Companion (operator):** never rename canonical outputs; use `render --dest`.

#### E-15 Replace the ownership example in FORFATTERSTEMME (line 60) — targets N3

Replace:
> «Jeg moderniserte verktøyet» framfor «moderniseringen av verktøyet ble gjennomført».

with an example whose subject is not the candidate:
> «Bussen kom tjue minutter for sent» framfor «det oppstod en forsinkelse på tjue minutter i bussens ankomst».

- **Why not a first-person work example.** Any candidate action in the example can prime a capped claim. Even «Jeg avstemte kontoene» reads as *all* accounts, while CLM-BAR-001 bounds reconciliation to the candidate's own assigned clinic flow («ikke hele OUS») and WORK §10.1 forbids claiming month-end close for all of OUS.
- **What the example still teaches.** It keeps what the rule is about: a verb and a concrete subject instead of a nominalisation. It gives the writer nothing in the corpus to inflate.
- **Hash:** V, so Stage 3. Confirm whether Stage 1 folds V at the next freeze.

#### E-16 Source maintenance **[Vegard]** — targets N5, N6

**(a)** WORK §0.3, row *OUS — tidlig BAR-arbeid*.

Replace:
> gikk fra kvalitetssikring av andre til selvstendig gjennomføring, kontroll og lederrapportering

with:
> gikk fra å få eget arbeid kvalitetssikret av andre til selvstendig gjennomføring, kvalitetssikring og lederrapportering

**(b)** CLM-BAR-004. Move the phrase *"Fordelingen av saker var etterspørselsstyrt og avhang av økonomilederens kapasitet"* from the claim text to the Ceiling column, reworded as a boundary: *"Etterspørselsstyrt tildeling; ikke fast ansvar for en prosjektportefølje."*

**Cost:** WORK changes both stage hashes; re-attest CV_BASELINE at freeze. **No new fact.**

#### E-17 CV grammatical person (WRITING_DOCTRINE § CV) — targets N7

Add:
> CV-profil og CV-punkter skrives uten første person; subjektet er underforstått, som i CV_BASELINE.

#### E-18 The transfer bridge is a function, not a formula (FORFATTERSTEMME § Mønstre + S3 final polish) — targets T4, T6, T7d

**V**, add to the pattern list:
> Overføringsbro som refreng: Flere avsnitt ender med samme «Den [erfaringen/arbeidsformen/strukturen] vil jeg ta med inn i …»-setning. Én overføring er nok; legg den helst i avslutningen eller inn i beviset den gjelder. Gjentatte broer er utskiftbare relevansbroer (WRITING_DOCTRINE, komprimeringsrekkefølge 4).

**S3 final polish**, after "Never delete the only employer bridge …", add:
> A second or third bridge with the same function is not protected.

#### E-7 revised: variation by function, with a prompt companion — targets T4, N2

**V § Mønstre**, replacing the previous E-7 part 1:
> Samme åpningsgrep i flere brev i samme klynge: identitetsformel («Jeg er samfunnsøkonom og …»), tittelgjentakelse («… og søker stillingen som …») eller «Jeg søker … fordi». Mønsteret gjelder grepet, ikke ordene. Første setning bruker ikke plassen på det emnelinjen allerede sier. Avslutt etter funksjon: det konkrete bidraget, et tema du gjerne utdyper, eller et spørsmål om arbeidet deres.

Part 2 is unchanged: no "avviklet" as the last word of a bullet or paragraph.

**Prompt companion (STAGE3_PROMPT.md; hash-free):**
> Before drafting each letter after the first in a chat, look at the opening move, the motivation frame and the closing move you already used, and choose different ones.

#### E-19 Convert one employer fact (optional; test on a branch before adopting) — targets §4.9 point 5

This is the one move that separates b5104f from every letter here. Add, as an option rather than a requirement, to WRITING_DOCTRINE § Arbeidsgiverspesifisitet:
> Når annonsen gir et konkret faktum om arbeidsgiverens drift, skala eller oppdrag, kan brevet bruke det én gang og straks omsette det til en arbeidsbetingelse kandidatens dokumenterte arbeid svarer på.

**Risk:** the relaxed name-swap test (M06) removed forced uniqueness that produced strained closes (C09). Test it on the 2×2 branches' letters before freezing.

### 7.4 Operating model for reduced and moderate budgets

| Tier | Stage 1 | Stage 3 | Chats | Required text and template items | Evidence so far |
|---|---|---|---|---|---|
| **Economy** | Terra-class, about 1 min/job | Decided by the 2×2 test | ≤4 jobs, fresh chat per cluster | E-5 extended, E-6, E-12, E-13, E-14, E-15; E-1 if Stage 3 is cheap | `rund`: IOI 23.2, 8/12 self-disqualification cues |
| **Standard** (`rung`-like) | Mid-capability, 3–5 min/job | Strong, about 4 min/job | ≤4 | E-12, E-13, E-14, E-15, E-3, E-18 | IOI 30.9, zero cues, best gain per minute |
| **Rich** (`runf`-like) | High-capability, 6–11 min/job | Strong, 3–7 min/job | ≤4 | **E-12 and E-13 essential**, plus E-3, E-18 | IOI 27.2 as rendered; 32.6 once the CVs fit |

**General rules**
1. **Keep chats at four jobs or fewer; parallel chats are fine.** Two render streams interleaved without a COM failure.
2. **Put the best available Stage 3 behind any Stage 1 that writes positive fields ambitiously.** The overreach risk rises with Stage-1 capability (N4).
3. **Record the real mapping at freeze and keep role labels stable.** For example: `stage1 = "SOL_CLASS"`, `stage3 = "SOL_CLASS"`, and put the truth in `role_mapping`. Use two roles only when two models actually ran. Pass `--model-tag` on branches.
   - **Exception for branches that reuse a strategy:** keep the parent's Stage-1 role and mapping string verbatim, even if it is wrong (§7.2 precondition). Record the truth in the Stage-3 mapping, the model tag and the run notes.
4. **Class non-Bokmål ads as EXCEPTION.** Note CV-only channels in the approval step. Fill `deadline`, `unit` and `reference`.
5. **Close Word before render** where possible. It worked this time; COM failures cost `rund` a PDF set.

### 7.5 Next-run signals (human-observed; no detector)

| # | Check | Target |
|---|---|---|
| 1 | Letters stating an unmet listed requirement | 0 |
| 2 | Gaps or learning instructions in Stage-1 positive fields or structure guidance | 0 |
| 3 | CV pages / letter pages | 2 / 1 |
| 4 | Rendered headline lines | 1 |
| 5 | Ownership verbs beyond a ceiling ("Moderniserte …", "har modernisert") in finals | 0 |
| 6 | Stage-1 overstatements recorded as repaired | Allowed; unrepaired 0 |
| 7 | Same opening move or bridge frame in ≥3 letters of a chat | No |
| 8 | §5.2 notes and summaries where the ad asks for writing or decision support | Yes |
| 9 | First person in a CV | 0 |
| 10 | CHECK when a known persuasion or mechanical defect remains; apply/no-apply advice in reviews | Yes; 0 |
| 11 | Canonical PDF names intact; no `render: FAILED` on an OK render | Yes |
| 12 | Model mapping recorded truthfully at freeze | Yes |
| 13 | Pilot-log edit minutes per package | Falling |

### 7.6 Deliberately not recommended

- **A detector, similarity check or word-count gate** for capacity, formulas or gap sentences. The constitution excludes them, and E-12, E-13 and E-14 reach the cause without one.
- **Applying E-4 as originally written.** It would weaken the Stage-3 guard that caught every Stage-1 overstatement in these runs.
- **Editing K rule 5 (E-10) before the 2×2 test.** There is no evidence it matters at capable tiers.
- **A channel, language or letter-required switch.** DEC-01/02/04 exclude it, and the EXCEPTION class and operator practice cover the need.
- **Reinstating unique-close pressure.** C09 showed it strains closes; E-7 revised asks for varied function instead.
- **Buying `runf`-level Stage-1 depth by default.** Beyond `rung`'s level, the extra depth mostly reached page 3. Buy it for high-fit, high-stakes vacancies, and only with E-12 and E-13 in place.
- **Treating the arm league table as a model ranking.** The mapping is unknown, the arms saw different vacancy types, and `rung` versus `runf` is not robust.

---

## Appendix A — Package metrics (all 20 current-harness packages)

**Column definitions**
- `dup60`: letter sentences with ≥0.60 SequenceMatcher similarity to a CV sentence.
- `shared5`: the share of letter 5-grams also found in the CV.
- **Pages** come from `render_report.json`. **Headline lines** were read from the rendered PDF text; they were measured for the new runs only (`rund`: 8 of 11 wrap, per the previous report).
- **S1 reqs** gives the count of material requirements, with SUPPORTED and GAP relations in brackets.
- **Minutes** are wall-clock from handoff to the last return file.

| Package | Headline chars / lines | Comps | Bullets | CV words | Letter words | Avg sent. len | jeg /100w | dup60 | shared5 | Refs | Pages CV/L | S1 KB | S1 units | S1 reqs (SUPPORTED/GAP) | Facets | Minutes S1 / S3 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---:|---|
| F·Amesto | 62 / 1 | 7 | 11 | 523 | 470 | 20.4 | 4.9 | 7 | 0.08 | 21 | 3/1 | 37.4 | 7 | 17 (10/1) | 3 | 6.3 / 3.7 |
| F·BearingPoint | 75 / 2 | 8 | 11 | 522 | 440 | 17.6 | 4.5 | 7 | 0.07 | 21 | 3/1 | 36.4 | 7 | 16 (7/2) | 3 | 5.9 / 4.9 |
| F·Tieto | 72 / 2 | 8 | 10 | 422 | 496 | 18.4 | 3.8 | 3 | 0.06 | 17 | 2/1 | 40.9 | 7 | 17 (4/2) | 3 | 11.2 / 7.5 |
| F·Visma | 84 / 2 | 8 | 12 | 533 | 311 | 23.9 | 4.2 | 3 | 0.05 | 21 | 3/1 | 33.9 | 5 | 12 (3/2) | 3 | 6.0 / 2.8 |
| G·Abacus | 92 / 2 | 8 | 11 | 405 | 333 | 18.5 | 5.1 | 4 | 0.05 | 10 | 2/1 | 16.8 | 5 | 12 (5/1) | 1 | 2.6 / 2.2 |
| G·EIE | 77 / 2 | 8 | 11 | 374 | 373 | 20.7 | 5.1 | 2 | 0.06 | 14 | 2/1 | 15.4 | 5 | 11 (6/1) | 1 | 4.9 / 2.7 |
| G·Norwegian | 65 / 1 | 8 | 12 | 450 | 445 | 22.2 | 3.1 | 4 | 0.04 | 15 | 2/1 | 19.7 | 6 | 12 (6/1) | 1 | 3.0 / 4.0 |
| G·Stortinget | 63 / 1 | 9 | 12 | 374 | 457 | 20.8 | 4.6 | 3 | 0.03 | 15 | 2/1 | 18.4 | 5 | 14 (7/1) | 1 | 3.9 / 7.0 |
| D·Abacus | 94 / – | 8 | 11 | 353 | 312 | 19.5 | 5.4 | 4 | 0.11 | 11 | 2/1 | 8.0 | 2 | 6 (1/3) | 0 | ≈1 / ≈2 |
| D·Amesto | 72 / – | 8 | 12 | 425 | 386 | 22.7 | 4.9 | 2 | 0.09 | 15 | 2/1 | 9.4 | 2 | 7 (2/2) | 0 | ≈1 / ≈2 |
| D·BearingPoint | 62 / – | 8 | 10 | 367 | 372 | 20.7 | 4.0 | 4 | 0.09 | 15 | 2/1 | 8.3 | 2 | 7 (3/2) | 0 | ≈1 / ≈2 |
| D·BI | 82 / – | 8 | 11 | 441 | 484 | 21.0 | 3.5 | 2 | 0.09 | 13 | 2/1 | 12.9 | 3 | 8 (3/2) | 2 | ≈1 / ≈2 |
| D·Digdir | 79 / – | 8 | 10 | 362 | 360 | 21.2 | 5.0 | 2 | 0.1 | 13 | 2/1 | 10.1 | 3 | 7 (2/2) | 0 | ≈1 / ≈2 |
| D·ECIT | 85 / – | 8 | 10 | 376 | 361 | 18.1 | 5.3 | 3 | 0.09 | 11 | 2/1 | 9.4 | 2 | 8 (3/2) | 0 | ≈1 / ≈2 |
| D·EIE | 74 / – | 8 | 9 | 322 | 356 | 22.2 | 5.3 | 2 | 0.05 | 15 | 2/1 | 9.7 | 2 | 8 (3/2) | 0 | ≈1 / ≈2 |
| D·KPMG | 59 / – | 6 | 4 | 181 | 319 | 17.7 | 3.4 | 4 | 0.09 | 9 | –/– | 8.4 | 2 | 7 (2/3) | 0 | ≈1 / ≈2 |
| D·Nasjonalmuseet | 65 / – | 8 | 10 | 350 | 372 | 21.9 | 3.8 | 7 | 0.12 | 13 | 2/1 | 10.5 | 3 | 8 (3/2) | 0 | ≈1 / ≈2 |
| D·Statnett | 57 / – | 8 | 10 | 380 | 415 | 18.9 | 3.4 | 7 | 0.08 | 10 | 2/1 | 16.0 | 3 | 10 (5/2) | 0 | ≈1 / ≈2 |
| D·Stortinget | 99 / – | 8 | 11 | 344 | 326 | 20.4 | 4.9 | 7 | 0.15 | 13 | 2/1 | 10.8 | 2 | 8 (5/0) | 0 | ≈1 / ≈2 |
| D·Tieto | 87 / – | 8 | 10 | 355 | 390 | 17.7 | 4.9 | 4 | 0.1 | 14 | 2/1 | 8.7 | 2 | 7 (2/3) | 0 | ≈1 / ≈2 |

---

## Appendix B — Pattern scan

**How the counts were made**
- Regular expressions over the final letter text, validated by hand for the new runs.
- Opening and closing columns look only at the opening or closing paragraph. Other columns count occurrences.
- "Repair direction" for the new runs was classified by hand from `upstream_claim_repaired`.

**Which `rund` counts are floors**
- `rund`'s "S1 gaps in `top_employer_problems`" column (marked `*`) is the regex floor. The hand-validated count in the previous report is 11 of 12.
- "Apply nudge" counts explicit apply/no-apply advice. "Soft" means a level or approval nudge without the word *sendes*.

| Package | Identity opening | Title restated | «søker … fordi» | Cleft | Transfer bridges | Bolt-on markers | Invitation close | Stock close | Conflict framing | «avviklet» ending | Doc. voice | 1st person CV | Ownership verb | S1 gaps in TEP | Repair direction | Apply nudge | Triage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|
| F·Amesto | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | – | 0 | 0/4 | digest | – | READY |
| F·BearingPoint | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | – | 0 | 0/4 | digest | – | READY |
| F·Tieto | 1 | 1 | 1 | 0 | 2 | 0 | 1 | 1 | 1 | 1 | 0 | – | 1 | 0/4 | digest; over (causal onboarding); under (2027) | yes | READY |
| F·Visma | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | – | 0 | 0/4 | over (3,5 år eierskap) | yes | READY |
| G·Abacus | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | – | 0 | 0/3 | none | – | READY |
| G·EIE | 0 | 1 | 1 | 0 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | – | 0 | 0/3 | over (KI-henvendelser) | – | READY |
| G·Norwegian | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | yes | 0 | 0/3 | over (har modernisert) | soft | READY |
| G·Stortinget | 0 | 1 | 1 | 0 | 2 | 3 | 1 | 1 | 0 | 0 | 1 | yes | 0 | 0/3 | under (staff units) | – | READY |
| D·Abacus | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | – | 0 | 1/3* | under | – | READY |
| D·Amesto | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | – | 0 | 1/3* | under | – | READY |
| D·BearingPoint | 1 | 1 | 1 | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 0 | – | 0 | 0/3* | none | – | READY |
| D·BI | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | – | 0 | 0/3* | under | – | READY |
| D·Digdir | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | – | 0 | 1/3* | under | yes | READY |
| D·ECIT | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | – | 0 | 1/3* | under | – | READY |
| D·EIE | 0 | 0 | 1 | 1 | 3 | 1 | 1 | 1 | 0 | 0 | 0 | – | 0 | 1/3* | under | – | READY |
| D·KPMG | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | – | 1 | 1/3* | none | – | READY |
| D·Nasjonalmuseet | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | – | 0 | 1/3* | under | yes | READY |
| D·Statnett | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | – | 0 | 1/3* | under | – | READY |
| D·Stortinget | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | – | 0 | 1/3* | under | – | READY |
| D·Tieto | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | – | 0 | 1/3* | under | yes | READY |

---

## Appendix C — Evidence reaching the letter (L) or only the CV (c), new runs

| Package | PRJ-03 budget tool | PRJ-06 STE | PRJ-04 benefits | BAR month close | REGERP tools | PRJ-01 dashboard | PRJ-05 forecasting | KI superuser | PRJ-08 founding / work model | PRJ-09 intake | PRJ-02 teaching | PRJ-10 DRG | PRJ-07 pilots | Sector Alarm | UiA KI master | §5.2 notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F·Tieto | L | L | L | c | c | c | L | L | c | . | c | . | . | . | . | . |
| F·BearingPoint | L | L | c | L | L | c | L | L | c | c | c | . | c | . | L | . |
| F·Amesto | L | L | c | L | L | c | L | L | L | c | . | . | c | . | L | . |
| F·Visma | L | c | c | L | c | L | L | c | c | c | . | c | . | . | c | . |
| G·Stortinget | L | . | c | L | c | L | . | L | L | L | c | . | . | . | . | c |
| G·Norwegian | L | L | c | c | c | c | c | L | L | L | . | . | . | . | . | . |
| G·EIE | L | . | . | c | L | L | . | L | . | c | c | . | L | c | L | . |
| G·Abacus | L | c | . | L | L | c | . | . | . | c | c | . | . | c | . | . |

**What the table shows**
- **§5.2 (decision notes, summaries, adapting to the reader) reaches one CV and no letter.** That is so although WORK#032 is cited in 5 of 8 new strategies (1 of 4 in `runf`, 4 of 4 in `rung`). This is the E-6 surface problem.
- **Sector Alarm, the only external customer-dialogue evidence, never reaches a letter.** That includes EIE, where close customer dialogue is a stated requirement.

---

## Appendix D — Truth-pass ledger (claims new relative to `rund`)

Section references are to the frozen `Work_experience.md` (WORK) and `Other_high_value_information.md` (OTHER) of `r20260914-211651-5dbd38`, which are identical in all three runs.

| Package | Claim (abridged) | Source | Verdict |
|---|---|---|---|
| F·Tieto CV | "Moderniserte sykehusets … budsjetteringsverktøy" | WORK §4.3 ceiling; §0.3 live ceiling | **Slip**: exceeds "no sole ownership of the complete modernization"; the adjacent sentence restores the boundary |
| F·Tieto L | "I 2027-runden hadde jeg vesentlig større frihet … nå i bruk i den pågående budsjettprosessen" | §4.3 delivered status (confirmed 2026-09-06) | Supported |
| F·Tieto / BP / Amesto, G·Norwegian L | "bevisst uten kjerne-VBA … uten å være varig avhengige av en utvikler" | §4.6 | Supported |
| F·BearingPoint CV/L | "om lag 3,5 års erfaring" | §1.1 chronology (from March 2023) | Derived; correct |
| F·BearingPoint CV/L | STE as decision support for "lager, utstyr, automatisering og investeringer" | §4.6 ("Warehouse, equipment, automation, feature and investment choices") | Supported |
| F·BearingPoint, F·Visma | "utfordret hvordan prognosemålet var definert … tidsriktig validering mot referanseprognoser" | §4.5 ("Defined and challenged the operational forecast target"; time-aware holdouts, baselines) | Supported |
| F·Amesto L | "En kollega laget den opprinnelige modellen og mye av datavaskingen" | §4.5 status register and claim atoms | Supported |
| F·Amesto L | "holder lokal validering atskilt fra kjøringer mot levende data som ikke er validert" | OTHER §4.3 | Supported |
| F·Amesto CV | "Gikk fra arbeid som ble kvalitetssikret av andre til selvstendig gjennomføring" | §1.1 (not the §0.3 digest) | Supported |
| F·Visma CV | "Valgte stjerneskjema etter å ha vurdert alternativer" | §4.1 | Supported |
| F·Visma CV | "skilte en større modellmodernisering fra løpende videreutvikling da modellgrensene ga leveranserisiko" | §4.1 | Supported |
| F·Visma CV/L | "kvalitetssikret bemannings-, UTA- og vaktgrunnlag" | §6.1; BAR budget contribution | Supported |
| F·Visma CV | "seksjonsvise DRG-estimater med Stata, R og Power Query" | §4.10 (the hit observation omitted) | Supported |
| F·Visma, G·Norwegian, G·EIE CV | "Hovedutvikler for/av backend" or "av datamodellen" / "om lag 80 til 90 prosent av DAX" | §4.1; §8 (self-reported share) | Supported |
| G·EIE L/CV | "var den som feilsøkte når noe ikke virket"; "observerte hvor de ble usikre" | §4.1 (primary technical troubleshooting; observed confusing interactions) | Supported |
| G·EIE CV | "tidlig tilgang og utprøving … Fabric, Power Platform, dbt, Pega og Python" | §4.7 | Supported |
| G·Stortinget L | "en av fire i etableringsgruppen sammen med avdelingslederen" | §0.2 | Supported |
| G·Stortinget CV | "Utarbeider beslutningsgrunnlag, notater og korte sammendrag …" | §5.2 (pattern-level) | Supported |
| G·Stortinget L | "Decisions og Planner" | Vacancy | Future contribution only; correct |
| G·Norwegian CV | "kontrollerer kode og notatbøker for sensitive data" | §4.5 | Supported |
| G·Abacus CV | "bidro vesentlig til en første komponent i en driftsrapport" | §0.3 PRJ-02 | Supported |
| G·Abacus CV | "frikjøp, revisjonskostnader, overhead" | CLM-BAR-004 | Supported |
| G·Abacus L | tools that checked "prosjekt og konto" | §9.3 story map (project/account validation) | Supported |
| `runf` S1 Visma | "om lag 3,5 år med funksjonelt eierskap" | §8 (owner Aug. 2025–Feb. 2026) | **Overstatement**; not used by Stage 3 |
| `rung` S1 Norwegian | "har modernisert" | §4.3 ceiling | **Overstatement**; repaired by Stage 3 |
| `rung` S1 EIE | "besvarer KI-henvendelser" | §0.3 ("tekniske svar i en Teams-kanal") | **Overstatement**; repaired |
| `runf` S1 Tieto | Onboarding as the cause of the tool's value | K (no borrowed causality) | **Overstatement**; repaired |

---

## Appendix E — Scoring sheet

These are the sub-scores behind every table in §5. G1, G2 and G3 are the gate-model values used in the Monte Carlo's structural alternative. Letter scores for Visma and Norwegian are shown but excluded from their compounds.

| Package | K .26 | E .20 | M .18 | A .14 | C .12 | N .10 | **CV** | S .22 | J .20 | K .18 | A .16 | C .14 | N .10 | **Letter** | G .26 | R .22 | M .20 | X .16 | Z .16 | **Package** | Tone | G1 | G2 | G3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| D·Abacus | 86 | 84 | 78 | 80 | 86 | 78 | **82.5** | 66 | 66 | 84 | 62 | 58 | 74 | **68.3** | 86 | 72 | 84 | 88 | 70 | **80.3** | 68 | 82.4 | 69.8 | 73.3 |
| D·Amesto | 86 | 88 | 80 | 82 | 84 | 76 | **83.5** | 74 | 82 | 84 | 76 | 52 | 78 | **75.0** | 86 | 78 | 86 | 88 | 64 | **81.0** | 68 | 83.8 | 78.7 | 73.0 |
| D·BI | 86 | 86 | 80 | 86 | 84 | 84 | **84.5** | 78 | 90 | 86 | 84 | 78 | 84 | **83.4** | 88 | 80 | 84 | 88 | 82 | **84.5** | 76 | 84.8 | 84.1 | 80.7 |
| D·BearingPoint | 84 | 86 | 88 | 84 | 86 | 80 | **85.0** | 72 | 84 | 82 | 76 | 64 | 80 | **76.5** | 86 | 76 | 90 | 88 | 74 | **83.0** | 74 | 85.0 | 78.4 | 77.2 |
| D·Digdir | 80 | 76 | 84 | 76 | 84 | 80 | **79.8** | 66 | 62 | 76 | 62 | 55 | 74 | **65.6** | 80 | 76 | 86 | 86 | 66 | **79.0** | 66 | 79.2 | 67.2 | 72.0 |
| D·ECIT | 82 | 84 | 80 | 84 | 84 | 76 | **82.0** | 72 | 86 | 82 | 72 | 62 | 78 | **75.8** | 84 | 76 | 86 | 88 | 74 | **81.7** | 74 | 82.4 | 78.1 | 77.2 |
| D·EIE | 84 | 84 | 82 | 80 | 86 | 80 | **82.9** | 80 | 76 | 84 | 74 | 76 | 80 | **78.4** | 86 | 80 | 86 | 88 | 82 | **84.4** | 80 | 82.4 | 78.9 | 82.1 |
| D·KPMG | 58 | 58 | 60 | 72 | 74 | 72 | **63.6** | 58 | 76 | 66 | 56 | 50 | 70 | **62.8** | 66 | 70 | 58 | 82 | 60 | **66.9** | 60 | 62.6 | 65.0 | 66.4 |
| D·Nasjonalmuseet | 76 | 78 | 88 | 80 | 84 | 80 | **80.5** | 62 | 72 | 72 | 66 | 60 | 76 | **67.6** | 76 | 62 | 90 | 86 | 70 | **76.4** | 68 | 79.8 | 68.5 | 70.9 |
| D·Statnett | 88 | 80 | 88 | 86 | 88 | 82 | **85.5** | 72 | 80 | 86 | 70 | 90 | 80 | **79.1** | 88 | 66 | 90 | 88 | 88 | **83.6** | 80 | 86.6 | 77.3 | 80.8 |
| D·Stortinget | 72 | 72 | 74 | 70 | 82 | 76 | **73.7** | 70 | 60 | 74 | 68 | 80 | 74 | **70.2** | 74 | 62 | 82 | 86 | 78 | **75.5** | 70 | 71.8 | 68.4 | 73.6 |
| D·Tieto | 82 | 82 | 80 | 80 | 86 | 78 | **81.4** | 62 | 70 | 78 | 48 | 35 | 74 | **61.7** | 80 | 72 | 86 | 86 | 52 | **75.9** | 56 | 81.0 | 66.3 | 64.2 |
| F·Amesto | 90 | 92 | 62 | 86 | 88 | 80 | **83.6** | 82 | 88 | 86 | 80 | 90 | 82 | **84.7** | 90 | 72 | 66 | 88 | 88 | **80.6** | 84 | 83.4 | 84.0 | 83.4 |
| F·BearingPoint | 92 | 92 | 60 | 86 | 88 | 82 | **83.9** | 78 | 88 | 86 | 76 | 90 | 82 | **83.2** | 92 | 70 | 66 | 88 | 88 | **80.7** | 82 | 83.8 | 82.2 | 82.3 |
| F·Tieto | 88 | 88 | 82 | 86 | 80 | 82 | **85.1** | 76 | 86 | 86 | 74 | 88 | 80 | **81.6** | 88 | 76 | 84 | 84 | 84 | **83.3** | 82 | 86.2 | 80.6 | 81.7 |
| F·Visma | 86 | 92 | 58 | 80 | 90 | 82 | **81.4** | 84 | 76 | 78 | 84 | 90 | 84 | **82.2** | 84 | 78 | 60 | 88 | 86 | **78.8** | 84 | 79.2 | 80.8 | 84.1 |
| G·Abacus | 88 | 80 | 80 | 82 | 88 | 80 | **83.3** | 76 | 62 | 86 | 82 | 84 | 80 | **77.5** | 86 | 78 | 84 | 88 | 84 | **83.8** | 82 | 83.8 | 75.8 | 82.9 |
| G·EIE | 84 | 80 | 82 | 82 | 88 | 80 | **82.6** | 86 | 70 | 84 | 78 | 90 | 80 | **81.1** | 84 | 82 | 86 | 88 | 86 | **84.9** | 84 | 82.6 | 79.8 | 84.9 |
| G·Norwegian | 80 | 86 | 72 | 76 | 86 | 76 | **79.5** | 84 | 84 | 84 | 80 | 88 | 80 | **83.5** | 82 | 80 | 70 | 88 | 86 | **80.8** | 82 | 77.8 | 83.0 | 83.8 |
| G·Stortinget | 88 | 80 | 86 | 84 | 84 | 72 | **83.4** | 80 | 64 | 84 | 72 | 86 | 76 | **76.7** | 86 | 80 | 88 | 86 | 84 | **84.8** | 76 | 85.6 | 75.2 | 80.8 |

**Anchors for the earlier corpus** (published totals, not re-scored):

| Package | CV | Letter | Package | Cues entered |
|---|---:|---:|---:|---|
| b5104f | 88 | 90 | 85 | none |
| 0fa53b-opusx | 85 | 81 | 81 | letter two pages |
| 3eeb10-stage1 | 80 | 86 | 84 | CV three pages |
| 3eeb10 | 82 | 79 | 82 | employer-blind letter |
| 6d65bd | 78 | 77 | 80 | none |
| 0fa53b | 77 | 84 | 79 | CV three pages; self-negation |
| 0fa53b-solxh | 80 | 76 | 75 | self-negation |
| 0fa53b-solmed | 77 | 74 | 78 | self-negation |
| 93c621 | 76 | 75 | 77 | one cue (type not restated in the notes; entered as ×0.85) |
| Curated (cherry-picked) | 84 | 79 | 86 | none |

---

## Appendix F — Method, sources and limits

**Read in full**
- The 8 new finals, reviews and strategies, and the rendered PDF text of all 16 documents.
- The 8 vacancy views; the Visma and Norwegian source PDFs checked against their derived views.
- The 12 `rund` letters and CV tops, for the head-to-heads.
- Both manifests and all three batch CSVs; the handoff and return timestamps; the render reports and derived queue views.
- The frozen WORK and OTHER sections behind every claim in appendix D.
- FORFATTERSTEMME, WRITING_DOCTRINE, PERSUASION_CALIBRATION, the Stage-3 instruction and STAGE3_PROMPT, at the passages quoted.
- The previous report, the nine-package ranking (§4) and the curated-package notes (§0–1).

**Diffed**
- All 26 frozen inputs across `rund`, `runf` and `rung`, by SHA-256.
- `settings.toml` line by line.
- The PDFs on disk against their render receipts, by SHA-256.

**Computed**
- Metrics and pattern scans (appendices A and B).
- Pairwise letter similarity.
- PDF span fonts for the support sections.
- The scoring model and a 4 000-draw Monte Carlo (`scratchpad/score/score.py`, `tables.py`, `appendix.py`).

**Limits**
1. **The model mapping is unknown.** Arm-level statements describe behaviour, not models.
2. **Arms differ in vacancy type.** Only the six matched pairs support a clean old-versus-new comparison.
3. **The rubric scores are one reviewer's editorial judgements.** The Monte Carlo covers score noise, weights, cue sizes, fit and model structure, but not a systematic reviewer bias. The earlier corpus uses published scores from a different review pass.
4. **Absolute interview percentages inherit the Avinor applicant-pool assumptions.** Ordering and gap sizes are the robust part.
5. **Wall-clock time includes operator latency** and is a proxy, not a token count.
6. **Patterns are counted, not detected.** Every count that drives a conclusion was checked by hand in the text.
