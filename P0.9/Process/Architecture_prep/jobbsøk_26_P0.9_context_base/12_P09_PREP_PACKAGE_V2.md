---
document: "Jobbsøk_26 P0.9 — pre-architecture uncertainty reduction package"
role: "inputs to the final architecture-definition step; not an architecture"
contents: "user questionnaire · external research prompt · other preparatory work · personality.md sidebar"
---

# 0. Prioritization logic

Only items passing this filter are included: *if the answer flipped, would a consequential P0.9 architecture decision change?*

The five decisions that are currently blocked or under-informed, in descending order of consequence:

| Rank | Blocked decision | Blocked by |
|---|---|---|
| 1 | **Product boundary** (DC-1: portal in core vs detached; CV-only possible; language scope) | facts about the real 40-vacancy batch — user-supplied |
| 2 | **Scale and human-load envelope** (cluster count/size, how much CHECK/RERUN load is tolerable, whether 40 is realistic at all) | user's actual time budget and deadline pressure — never stated anywhere in the corpus |
| 3 | **Whether the experiment programme is executable** (gates DC-2 personality, DC-4 strategy format) | user's willingness to run paired/blinded tests + existence of a quality anchor |
| 4 | **CV template and rendering constraints** (whether content-control-heavy Word masters survive Norwegian ATS parsing; whether multi-doc LibreOffice conversion works on the target box) | external research + a local spike |
| 5 | **Generality budget** (one-shot for these 40 vs reusable framework) — determines how much reversibility and abstraction is worth paying for | user-supplied, single question |

Everything below serves one of these five. Items that would merely satisfy curiosity, restate a known risk, or refine a parameter that should stay configurable are excluded.

**Highest single-value item in the whole package:** a one-row-per-vacancy inventory of the actual batch (§3, item W-1). It simultaneously answers decision 1, informs decision 2, and *is* the seed for `batch_plan.json`. Nothing else in this document comes close.

---

# 1. Questionnaire — information only you can supply

24 items. Pre-filled with my best estimate; correct rather than compose. `→` marks my assumed answer.

## Interactivity assessment (brief)

The lowest-cost genuinely interactive option available right now is a **single self-contained HTML artifact** rendered in this chat: native checkboxes, radio groups, `<input type=range>` 1–10 sliders, editable textareas, and one "copy all answers as Markdown" button. No storage, no backend, ~200 lines, one turn to produce. That is the right level — say the word and I'll generate it.

Two things I'd advise against: building a hosted form (disproportionate), and using a slider for anything that isn't genuinely continuous (radio buttons carry more information per click for the questions below — only Q C5 and Q D3 warrant scales).

Fallback with zero build cost: answer inline by editing the `→` lines.

---

## Section A — The real batch (unblocks DC-1, the highest-value cluster)

**A1.** Are the ~40 vacancies already identified and collected?
→ *Partially — some collected, batch not complete*
`[ ] Yes, all 40 collected  [x] Partially  [ ] No, none yet  [ ] The "40" is an estimate, actual count differs`

**A2.** If the count differs from 40, what is the realistic number for the first full batch? (short text)
→ *`____`*

**A3.** Roughly what share of your vacancies require answering questions in a web form (portal) *in addition to* uploading CV + letter?
→ *25–50%*
`[ ] 0%  [ ] under 25%  [x] 25–50%  [ ] 50–75%  [ ] over 75%  [ ] don't know yet`

**A4.** Do any require **CV only**, with no application letter?
→ *No*  `[ ] Yes  [x] No  [ ] Don't know`

**A5.** Do any accept **only** portal form answers, with no CV/letter upload at all?
→ *No*  `[ ] Yes  [x] No  [ ] Don't know`

**A6.** What shape do the portal questions typically take? *(multi-select — combinations are meaningful; "several short fields" + "structured checkboxes" implies detachment is nearly free, whereas "long essay fields" implies the detached tool needs real writing quality)*
→ *single short motivation box; structured yes/no + qualification checkboxes*
```
[x] One short free-text motivation box
[ ] Several short free-text fields (2–5)
[ ] One or more long essay fields (200+ words)
[x] Structured yes/no or qualification checkboxes
[ ] Salary expectation / availability fields only
[ ] Don't know yet
```

**A7.** Any vacancies where the application must be written in English or another non-Norwegian language?
→ *No*  `[ ] Yes  [x] No  [ ] Don't know`

**A8.** Do the vacancies carry real application deadlines that constrain when the framework must be finished?
→ *Some within 4–8 weeks*
`[ ] No, I control timing entirely  [ ] Some within 2–4 weeks  [x] Some within 4–8 weeks  [ ] Most are rolling/open-ended`

**A9.** Roughly how many are **public sector** (stat/kommune/helseforetak)?
→ *Majority (over half)*
`[ ] None  [ ] A few  [x] Majority  [ ] Almost all`

---

## Section B — Human-load envelope (unblocks scale/cluster decisions; currently absent from the entire corpus)

`[OBS from your own doctrine]` Your cost hierarchy puts Human Effort above everything. No document states what that budget actually *is*, so every cluster-size and review-load decision so far has been made without a constraint.

**B10.** Realistic hours per week you can spend on reviewing + submitting?
→ *5–10 h/week*  `[ ] under 2  [ ] 2–5  [x] 5–10  [ ] over 10`

**B11.** Calendar window in which you want the full batch submitted?
→ *1–2 months*  `[ ] 2 weeks  [ ] 1 month  [x] 1–2 months  [ ] 2–3 months  [ ] open`

**B12.** Maximum acceptable *total* human minutes per submitted package (review + edits + portal work + submission), for it to feel worth it?
→ *10–20 min*  `[ ] under 10  [x] 10–20  [ ] 20–40  [ ] over 40`

**B13.** Forced choice: which do you actually prefer?
→ *~30 strong packages, weakest ones dropped rather than rescued*
```
[ ] 40 decent packages
[x] ~30 strong packages, weakest dropped rather than rescued
[ ] ~15 excellent packages, rest abandoned
```

**B14.** Is this framework intended for **repeat use** on future batches, or essentially one-shot for this batch?
→ *Repeat use — expect at least 2–3 more batches*
`[ ] One-shot  [x] Repeat use, 2–3 more batches  [ ] Long-term, indefinite reuse`
*(This one question sets the price you should be willing to pay for generality, reversibility and abstraction. One-shot → take K-1 lean everywhere. Long-term → some of the pruned generality becomes worth keeping.)*

---

## Section C — Whether the experiment programme is executable (gates personality + strategy-format decisions)

**C15.** Willing to run 2-job paired pre-pilot tests (≈6 extra prompts total) *before* the 8-job pilot?
→ *Yes*  `[x] Yes  [ ] Only one of them  [ ] No — decide by judgment instead`

**C16.** If yes, can you score packages **blind to condition**?
→ *Self-blinded: shuffle + score after a delay, without checking which variant is which*
```
[ ] Yes, fully blinded (another person shuffles/labels)
[x] Self-blinded (shuffle, delay, score before checking labels)
[ ] No, unblinded only
```
*(If "no": the personality layer becomes unmeasurable in principle and should be built as an off-by-default toggle rather than adopted.)*

**C17.** Do you have 2–3 past applications you would score 8+/10, usable as calibration anchors for the 1–10 scale?
→ *Yes, at least 2*  `[x] Yes  [ ] One  [ ] No  [ ] Yes but they predate my current experience and would need updating`

**C18.** Do you know your current interview-conversion baseline (interviews per application)?
→ *Roughly, not precisely*
`[ ] Yes, precisely: ____  [x] Roughly: ____  [ ] No idea`
*(This is the only true outcome metric in the system. Even a rough number lets the architecture model calibrate how much quality gain is worth how much complexity.)*

**C19.** 1–10: how consistent do you think your own package scoring would be if you re-scored the same package a week later, without seeing the old score?
→ *6*  `Score: __/10`
*(Low self-consistency is not a problem to fix — it's a number the architecture model needs, because it sets the minimum effect size any experiment can detect.)*

---

## Section D — Design values and risk posture (mostly confirmations)

**D20.** Default strategy elasticity — how much may Stage 3 reconstruct?
→ *ELASTIC — strategy is a strong hypothesis, final writer may rebuild it within truth bounds*
`[ ] TIGHT  [ ] BALANCED  [x] ELASTIC`

**D21.** Personality layer posture for the first release?
→ *Build as an off-by-default toggle, validate via paired test, adopt only if it wins*
```
[ ] Don't build it at all yet
[x] Build as off-by-default toggle, adopt only after paired test
[ ] Build it in as default — I'm confident enough in the theory
```

**D22.** Detach portal answers from the core package (core = tailored CV + tailored letter; portal handled by a separate small tool run from the approved package)?
→ *Yes*  `[x] Yes  [ ] No, keep in core  [ ] Depends on my A3–A6 answers — you decide`

**D23.** Rank what the architecture model should optimize when options conflict. *(1 = highest)*
→ *1 final package quality · 2 human minutes per package · 3 reversibility/optionality · 4 build cost and calendar time*
```
__ Final package quality (interview effect)
__ Human minutes per submitted package
__ Reversibility / ability to change course later
__ Build cost and calendar time to first submission
```

**D24.** Accept these three scope cuts for the first release? *(multi-select — check the ones you accept)*
```
[x] nb-NO only; English deferred to an explicit later extension
[x] Fixed dynamic CV surface (headline, profile, competencies, employment bullets) — no dynamic education/support sections
[x] Job-centric runtime folders (all of one job's artifacts in one directory) instead of stage-centric folders
```

---

## Section E — Environment and source facts

**E25.** Codex app on your machine: verified able to run local Python *and* invoke LibreOffice headless?
→ *Python yes; LibreOffice believed but not verified*
```
[ ] Both verified working
[x] Python verified, LibreOffice unverified
[ ] Neither verified
[ ] LibreOffice not installed
```

**E26.** Are `Work_experience.md`, `Education.md`, `Other_high_value_information.md` current as of now?
→ *Minor updates needed*
`[ ] Current  [x] Minor updates needed  [ ] Material updates needed  [ ] Not sure`

**E27.** Your personality report — what is it?
→ *Composite of several instruments, self-assembled into one report*
```
[ ] Single validated instrument, professionally administered
[x] Composite of several instruments, self-assembled
[ ] Self-assessment / self-written
[ ] Includes third-party observations (manager, colleagues, 360)
```
*(Affects only one thing: how much interpretive weight the file may carry. Composite/self-assembled → strictly interpretive, no exceptions.)*

**E28.** Hard ceiling on standard model prompts for a 40-job batch?
→ *20*  `[ ] 15  [x] 20  [ ] 25  [ ] over 25`

---

# 2. External research — Deep Research prompt

Copy the block below verbatim into a capable research model. This is the consolidated version — merged with an independently-drafted external prompt for the same task, combining that version's stronger evidence-tagging, track structure, and architecture-decision guardrails with this document's more concrete technical specificity and actionable template-rule output.

```
# DEEP RESEARCH BRIEF — Jobbsøk_26 P0.9 external evidence gathering

## Objective

Produce a decision-critical external evidence report for a later model that will
define the final P0.9 architecture: a private, manually initiated, file-based
workflow producing truthful, tailored Norwegian CVs and application letters via
GPT-5.6 Sol/Terra/Luna model chats, rendered from Word templates through headless
LibreOffice, with human review and manual submission.

Do NOT design or select the architecture. Do NOT recommend a final architecture.
Research only facts capable of materially changing one of:

- model/stage allocation and effort routing;
- context-loading design (what a model reads, in what order, at what size);
- manual-chat interactive feasibility (what a model can reliably do inside one
  chat turn without an orchestrator);
- structured-handoff assumptions (Markdown vs schema-validated JSON between stages);
- Norwegian application/ATS boundaries (what the product must produce);
- DOCX/PDF template and rendering constraints;
- minimal security/runtime controls for untrusted input documents.

If a question is better answered by inspecting the real vacancy set or by a cheap
local/two-job test than by web research, write `LOCAL TEST DOMINATES WEB RESEARCH`,
say in one line what the test would be, and move on — do not speculate further.

## Model-family note

GPT-5.6 Sol, Terra, and Luna are real, currently-documented OpenAI capability tiers
(Sol = flagship/highest cost, Terra = balanced, Luna = fastest/cheapest), generally
available since 9 July 2026, with a Terra/Luna price reduction on 30 July 2026.
Verify current facts directly — do not assume the figures above are still current.

## Inputs available to you

If attached, use: P0.8 architecture/specification; P0.8.1 review/hardening;
Brainstorm_Brief.md; brainstorm_review.md (design-choice clusters DC-1..DC-7,
mechanisms N-01..N-06, bundles K-0..K-6); the actual vacancy inventory, if produced.
If the vacancy inventory is not attached, use the platform fallback list in Track C.

Current working assumptions you should treat as context, not as settled fact to
defend: manually initiated cluster chats (one cluster per chat, several jobs per
cluster), one job transaction completed before the next, local deterministic
ingest/finalize scripts, three immutable candidate-authority files as sole fact
source, human final review and manual submission, no automatic orchestrator/retry.

---

## Track A — Current OpenAI execution facts [highest priority]

Official OpenAI sources only.

1. Current availability, and reasoning/effort control options, for Sol, Terra, and
   Luna in ChatGPT Work, Codex, Desktop, and the API.
2. Context window and maximum-output limits per tier.
3. Current published pricing per million input/output tokens, per tier.
4. File-upload / file-context behavior relevant to long multi-file, multi-turn chats
   (how many files, what size, whether earlier files remain "readable" late in a
   long conversation).
5. What local repository, code-execution, and process/tool access Codex (and Work,
   if relevant) currently grants an agent operating on a local Windows repository.
6. **Whether a model can, within one interactive chat turn, run a validator against
   its own output, read the error, repair the artifact, and re-validate — without a
   second prompt or external orchestration.** (Resolves `N-04`.)
7. Which JSON-Schema / Structured-Output validity guarantees are API-only versus
   actually available/enforceable in manual ChatGPT Work/Codex use. (Resolves the
   `strategy.json` vs `strategy.md` question, `DC-4`.)
8. Any materially relevant privacy/retention controls for uploaded candidate files.

Separate documented fact from workflow inference throughout.

## Track B — Long-context behavior and context preparation

Recent primary research / provider technical reports only.

Research evidence relevant to:

- multi-document "lost in the middle" effects;
- degradation across sequential jobs processed in one long conversation
  (position/order effects — early vs late job quality);
- job-local context slices vs one large shared context file;
- information loss from summarization/compression chains;
- a weaker/cheaper model preparing context that a stronger model then decides from;
- anchoring effects from preliminary summaries or relevance labels on a later,
  more capable model's independent judgment;
- delayed-context or independent-read-first protocols as an anchoring mitigation;
- reversible ranking/annotation of source material vs destructive filtering.

**Frame findings against this specific three-way comparison** (the live P0.9
alternatives, `DC-3` in `brainstorm_review.md`):

  (3a) no context-preparation layer — the stronger model retrieves directly;
  (3b) a deterministic, lossless, non-semantic index over stable source material
       (no model pass, no relevance judgment);
  (3c) 3b plus a cheap model's vacancy-conditioned preparation pass (advisory tiers,
       source-linked navigation) read by the stronger model before it decides.

Do not generalize an exact optimal cluster size (jobs per chat) from unrelated
benchmarks — that parameter is local-test territory. If direct evidence for
structured-strategy anchoring, or for this project's other specific hypotheses,
does not exist, say so plainly rather than extrapolating from adjacent findings.

## Track C — Norwegian application platforms and public-sector requirements

Prioritize platforms actually present in the real vacancy inventory if attached.
Otherwise examine: Jobbnorge, Webcruiter, Talentech/ReachMee, EasyCruit, Varbi, and
relevant finn.no application flows. Vendor, Norwegian-government, and other
first-party sources preferred. Actual vacancy facts always override market averages
where the two conflict.

Determine, where publicly documented:

1. Accepted CV/application document formats, and any size/page limits.
2. Whether the platform performs automated CV parsing/data extraction, and whether
   the candidate must also manually re-enter data.
3. Formatting known to impair parsing: multi-column layout, tables, text boxes,
   headers/footers, graphics, unusual fonts, or Word content controls (SDT).
4. Whether application letters are handled as upload, free-text field, or either;
   and the number, length, and any enforced word/character limits on free-text
   portal question fields.
5. Norwegian public-sector qualification-principle (`kvalifikasjonsprinsippet`)
   implications for explicit, itemized requirement/evidence coverage in the
   application text itself.
6. Mandatory or conventional attachments (vitnemål, attester, transcripts,
   references) that belong outside the core CV/application package.
7. Whether any platform is known to reject or degrade LibreOffice-produced (as
   opposed to Microsoft Word-produced) documents.

**Required technical depth:** report exact limits, field counts, and format rules
where documented — avoid summarizing at the level of "generally, PDFs are accepted."
Where a limit is set per-employer rather than per-platform, say so explicitly; that
distinction is itself architecturally relevant (it determines whether limits can be
hardcoded or must be read from each vacancy).

## Track D — Word/LibreOffice rendering mechanics and minimal security controls

Official LibreOffice/Microsoft/OpenAI sources and primary technical evidence
preferred.

1. Headless LibreOffice on Windows converting multiple DOCX files: reliability of a
   single `soffice --headless --convert-to pdf` invocation given several input
   files; the `-env:UserInstallation` profile-isolation pattern and why it matters;
   documented failure modes, exit codes, and partial-success behavior.
2. Word content-control (SDT) fidelity through DOCX→PDF conversion in LibreOffice —
   known issues with unwrapping, placeholder-text leakage, or empty paragraphs left
   behind by removed conditional content.
3. Font substitution and Norwegian glyph handling (æ, ø, å) in headless conversion
   on Windows; safe font families; how substitution could be detected
   programmatically. Whether Norwegian locale settings affect line-breaking or
   hyphenation.
4. Known pitfalls filling or removing Word content controls from Python
   (python-docx or direct OOXML manipulation).
5. Prompt injection risk from untrusted vacancy PDFs/documents feeding into model
   chats: current guidance on instruction/data separation, least-privilege file
   access, and human-confirmation boundaries; why a regex/"AI firewall" content
   filter should or should not be relied on as the primary control.

Where behavior is version- or template-specific rather than general, say so
explicitly rather than generalizing.

---

## Exclude — do not spend meaningful effort on

Generic CV/cover-letter writing advice; interview psychology; AI-detection tools or
evasion; vector databases/RAG frameworks; agent-orchestration frameworks;
persistent/long-term memory systems; automatic submission; general model benchmark
leaderboards; best-of-N generation; generic employer research; commercial
application-generator products; exact cluster sizes or effort-level defaults (local
test territory); ATS markets outside Norway except where a vendor also serves
Norway.

## Evidence handling

Tag every consequential claim with exactly one of:
`[FACT-FIRST-PARTY]` `[RESEARCH]` `[COMMUNITY]` `[INFERENCE]` `[VOLATILE]`
`[LOCAL-TEST]` `[NO-EVIDENCE]`

For conflicts: show both claims, date them, distinguish product/version/surface
differences, prefer current primary evidence for volatile product facts, and state
plainly what remains unresolved. Never turn missing evidence into an estimate —
`[NO-EVIDENCE]` is a valid and useful answer. Date every material claim; flag
anything likely to have changed in the last 12 months.

---

## Required output structure

Start directly at section 1. No narrative introduction, no Norwegian-labour-market
background, no general commentary.

**1. Decision-impact summary** — max 12–15 bullets. Only findings capable of
changing a P0.9 design decision. Lead with anything that would invalidate a current
project assumption.

**2. Current OpenAI capability matrix**
`| Capability | Surface/model | Current fact | Source/date | Confidence | Architectural relevance |`

**3. Decision-critical findings** — one block per material finding:
`Claim / Evidence+tag / Applicability to Jobbsøk_26 / Potentially affected decisions
(cite DC-x or N-x where applicable) / What it does NOT establish / Residual
uncertainty / Best next evidence: external, local test, or user decision`

**4. Norwegian platform/template matrix** — one row per platform; "not documented"
rather than a blank cell.

**5. Template design rules** — one consolidated, concrete DO / DO-NOT list for the
Word CV and letter masters, derived from Tracks C and D. This is the single most
directly actionable output — write it as rules an implementer applies, not as
prose.

**6. Evidence map to open P0.9 mechanisms**
`| Mechanism/decision (DC-x / N-x) | Evidence supporting | Evidence cautioning |
Evidential status | Local test still needed? |`
No recommendation column — status and next-evidence type only.

**7. Local tests that dominate further research** — ranked, with the smallest
adequate test stated for each.

**8. Conflicts / superseded project assumptions** — any statement in the supplied
project documents that newer evidence contradicts.

**9. Source register** — load-bearing sources only.

**10. What external research cannot decide** — split explicitly into: requires user
policy decision / requires real vacancy or file inspection / requires local
technical test.

Do not provide a final P0.9 architecture.
```

# 3. Other high-value preparatory work

Ordered by expected impact per unit of effort. Five items only.

## W-1 — Batch inventory *(highest-value single artifact in this whole package)*

One row per vacancy, in a spreadsheet or CSV:

```
job_id_slug | employer | title | sector (stat/kommune/helseforetak/privat)
| platform (Webcruiter/Jobbnorge/…) | CV required? | letter required?
| portal questions? (count + rough length) | language | deadline
| your gut priority 1-10 | notes
```

Why this outranks everything else:
- It *is* the answer to A3–A9, with real data instead of estimate.
- It resolves DC-1 (product boundary) definitively — the single decision with the largest effect on build scope.
- It becomes the seed for `batch_plan.json`, so the effort is not throwaway.
- It lets the architecture model see the real distribution of channels and platforms rather than designing for a hypothetical one.
- Combined with W-2's research findings, it tells you which template constraints actually bind.

Even a partial inventory (10–15 rows) is enough to answer the boundary question. Do this before answering Section A if you can.

## W-2 — Template spike on `CV_MASTER.docx` and `APPLICATION_MASTER.docx`

No models, no code beyond unzipping. Open the P0.7 masters and produce a factual inventory:

- every content-control tag that actually exists, with exact name and occurrence count;
- which ones P0.7's `finalize.py` actually fills, and which are orphans;
- the actual layout mechanics (columns? text boxes? tables? headers?);
- where the CV physically breaks across pages with sparse vs dense content.

Why: P0.8.1 CR-09 mandates a package→template source map, and BB R-01 argues the spike must precede finalizer work. Both are right, and **the map cannot be written correctly from the specification alone** — it has to be written from the file. Discovering the real tag contract after the finalizer is built guarantees rework at exactly the point where rework is most expensive. This also produces the input the research prompt's section 4 output needs to be checked against.

## W-3 — Environment preflight script

~30 lines, run once on the target Windows box, output pasted into the architecture handoff:

```
python --version; platform info
soffice path + version; test single-file convert; test multi-file single invocation
presence of the fonts the masters actually use
current path length of C:\Codex\Jobbsok_26_P0.9\... at deepest expected nesting
locale settings; UTF-8 handling
```

Why: this resolves E25 with fact rather than belief, and directly answers the research prompt's P3.1 for *your* machine, which is the only machine that matters. It also converts P0.7's two permanently-skipped PowerShell tests into either a pass or a known constraint.

## W-4 — Quality anchor set

Pick 2–3 past applications you'd score 8+/10 and one you'd score ~5. For each, write 3–5 lines: what makes it good/weak, and what a recruiter would notice first.

Why: the entire evaluation architecture rests on your 1–10 score, and an uncalibrated scale cannot detect the effect sizes any of the experiments are looking for. Written anchors also become legitimate style-calibration input for `PERSUASION_CALIBRATION.md` — which is the one place the corpus already permits approved historical applications.

## W-5 — Precedence and conflict table for the architecture model

The corpus is now six-plus documents with overlapping authority and at least one known ID collision. Before the architecture step, produce one page:

- document precedence order (which wins on what);
- the list of conflicts already resolved and their resolution (P0.8.1 §0.2 has some; the C-series ID collision, CR-04's conditionality on DC-6, and the portal hard/soft history are others);
- explicit "do not reintroduce" list.

Why: cheap, and it prevents the architecture model from re-litigating settled questions or inheriting a stale position. Much of this already exists across P0.8.1 §0.2/§21/§27 and my review's §0.3/§2.11 — this is consolidation, not new analysis.

## Decisions you can safely resolve now, without more input

`[INF]` These have converged across every source and need no further evidence — closing them shrinks the architecture model's search space at zero risk:

- frozen document date at ingest (not conversion time);
- package and review stay separate files (no `final_result.json` merge);
- no settings-compilation model, no compiled-instructions artifact, no cache (static enum→instruction mapping instead);
- no global portfolio-wide model pass;
- manual clustering only; drop the model clustering preflight from release scope;
- Luna never produces employer-facing prose, and never sees the personality file;
- validator exit 0 required before a job is marked complete, with a bounded 2-attempt same-chat repair rule.

## Explicitly *not* worth doing before the architecture step

Building the `strategy.json` schema, drafting stage instructions, writing any test, or prototyping the Luna prep contract. All four depend on decisions the questionnaire and W-1 will change, and all four are cheap to write once the boundary is fixed.

---

# 4. Sidebar — `personality.md` draft recommendations

Short by design; we'll do this properly separately.

## Role

**One job: help the strategy stage decide which of the candidate's already-supported patterns are worth surfacing for a specific vacancy, and how each could be misread.** It is interpretive context. It answers "what should be emphasized and how should it be framed" — never "what is true about the candidate."

It sits in the `WRITING_POLICY` invalidation class, not `SOURCE_TRUTH`. A change to it invalidates drafts and finals, not facts.

## Structure — facet blocks

One block per facet. Nothing else in the file except a short header and the negative section.

```markdown
## Facet: <plain professional description, no instrument language>

Looks like:        <1–2 lines: how this shows up in actual work>
Evidence anchors:  <Work_experience.md#Exact heading>, <Education.md#…>
Likely misread:    <the specific negative interpretation a recruiter may form>
Prevention:        <what the package must show to pre-empt that misread>
Expression ceiling: <the strongest claim this facet supports — and what it does NOT support>
Not for:           <role types or selection regimes where this should stay invisible>
```

## Hard rules

**Must not contain:**
- typology names, letter codes, percentiles, instrument names, archetype labels — not even in internal fields, because leakage risk into employer-facing text is the worst failure mode;
- any achievement, responsibility, result or capability claim (those live in the three authority files);
- comparative superiority ("better than most at…", "unusually strong…");
- behavioural guarantees ("reliably delivers under pressure");
- any facet without at least one evidence anchor.

**Must contain:**
- the misread column, from the first draft. It's the genuinely novel part of the concept and it is very hard to retrofit — writing it later produces generic "could be seen as too detail-oriented" filler.
- an explicit **negative section**: facets that are true but should not be surfaced, and why. `[INF]` This is where the file earns most of its value: telling the model what *not* to do is higher-signal than another positive facet, and it's information no model can derive from your work history.

## Five high-leverage principles

1. **No anchor, no facet.** If you can't point to a specific section of an authority file, delete the facet. This single rule is what separates the file from self-description, and it's the rule that makes the whole layer defensible in an interview.
2. **Write it before looking at any specific vacancy.** Facets written while thinking about a particular role are retrofitted, and retrofitting is the failure mode the concept is most vulnerable to.
3. **Cap it at 8–12 facets.** More means the strategy stage picks badly and expresses too many. A long personality file is worse than a short one, not richer.
4. **Employer-legible language throughout.** Write each facet as you'd want a recruiter to understand it. If a line would embarrass you if the file leaked, rewrite the line — that discomfort is a reliable detector of unsupported or performative content.
5. **Separate stable traits from current preferences.** Traits belong in the file; "currently interested in X" goes stale within months and belongs nowhere near it. Version and date the file.

## One thing to decide while drafting

`[INF]` Whether a facet's expression ceiling can ever be *raised* by evidence. My recommendation: no. The ceiling is set by the authority files; the personality file may only say "this facet is relevant here and could be misread this way." If the file can raise a ceiling, it has become a fact authority, which is the boundary the whole design depends on.
