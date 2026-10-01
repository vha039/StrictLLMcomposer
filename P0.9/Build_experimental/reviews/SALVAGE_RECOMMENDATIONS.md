# What to keep from the Relay experiment

Every change in `Build_experimental` against the stable `Build` core, judged on
whether it earned its place in the four-package test. Nothing here modifies
`Build`; this is the pitch for what to port.

## The one finding that explains the rest

| | old `strategy.json` | new `brief.json` |
|---|---|---|
| Stortinget | 14 material requirements, **13 evidenced** | 2 units + 6 stances (scout found 21 requirements) |
| Norwegian | 12, **11 evidenced** | 2 units + 7 stances (20 found) |
| EIE | 11, **9 evidenced** | 2 units + 5 stances (15 found) |
| Abacus | 12, **11 evidenced** | 2 units + 6 stances (18 found) |

`brief.stances` only covers requirements the candidate is **weak** on —
PARTIAL, GAP, ADJACENT. A requirement rated STRONG gets no stance, so nothing
in the brief guarantees it is answered.

Stortinget's ad asks for «arbeidsprosesser basert på potensialet i digitale
verktøy og kunstig intelligens» (scout Q06, TASK/**STRONG**). The scout put the
AI evidence in *reserve*; Stage 1 retrieved it anyway
(`outside_scout_refs: EV:OTHER#026-4-2-repeterbar-ki-arbeidsmodell`) and
attached it to no unit and no stance. The delivered package contains **no AI
mention at all**, CV or letter. The old package answers the requirement.

The "brief ≤8 KB, no requirement ledger" decision was mine, justified by lean
briefs producing tight packages. The tightness was real. The cost was coverage,
and coverage is what a screener checks. **Do not port the brief shape.**

Downstream evidence of the same narrowing, across all four jobs:

| | old → new |
|---|---|
| CV employment-bullet words | 308→190, 374→209, 304→204, 343→188 (**−38–45%**) |
| CV preamble words (headline+profile+competencies+tools) | 118→162, 126→184, 115→180, 112→160 (**+37–57%**) |
| «i praksis eneste kodende utvikler» (documented, confirmed) | 4/4 → **0/4** |
| AI superuser role | 4/4 → 1/4 |
| Hospital-wide benefits framework | 2/4 → 0/4 |

New CV totals are 351–395 dynamic words against a two-page boundary measured
above 605 — roughly **210–250 words of headroom went unused while documented
evidence was deleted**. This was not a length tradeoff. It was selection.

---

## KEEP — port as-is

### K1 · Drop REFERANSER, fold KURS into «SPRÅK OG KURS» · **highest value**
`templates/template_map.json`: `CV_SUPPORT_SECTION_1` and `_2` → `none`;
`CV_OPTIONAL_LANGUAGES` → source `baseline.languages_and_courses`, heading
«SPRÅK OG KURS» (needs the matching branch in `render.resolve_control`).

**Why:** the previous corpus shipped three-page CVs whose page 3 held four
lines of KURS and REFERANSER. A CV over two pages is a ×0.70 knock-out — the
largest single multiplier in the scoring model. Re-rendering the eight
14 September packages through the new template put **all eight on two pages**,
including the three that overflowed (588, 591, 605 dynamic words).

**Implementation:** four keys in the map plus one branch in `render.py`.
`CV_BASELINE` hashes the three authorities, not itself, so no hash blocker.
Frozen runs keep their own copies; re-freeze only affects new runs.

**Benefit:** removes the knock-out cue that cost `runf` three of four packages.

### K2 · `signals.py` — the formula-tic scanner
Drop-in module, ~90 lines, no dependencies. Eight patterns drawn from the
actual corpus: stock close, «søker … fordi», cleft motive, identity opening,
title restated in the opening, paragraph ending «avviklet», bolt-on marker,
first person in the CV. Plus `cv_dynamic_words`, `letter_words`, `letter_text`,
`first_sentence`, `last_sentence`.

**Why, measured:** `signals.scan` over the eight packages — old corpus **16
tics** (title restated 4/4, bolt-on 4/4, «søker … fordi» 3/4, first person in
CV 2/4); new corpus **0**.

**Implementation:** copy the module; call `scan()` in `status` and print the
names as soft signals. No gate.

**Benefit:** the writer sees its own formulas before submitting. Cheap.
Note these are *not* knock-outs — they are writing-quality tells, and I
over-weighted them in my first verdict.

### K3 · `preview` — render the work in progress and measure it
Renders the in-progress package to `%TEMP%\jbprev\` with an injected
FINALIZED date, no receipt, then reports pages per document, headline line
count (page-1 spans ≥13 pt), tail headings past the target page, word counts
and tics.

**Why:** five of eight CVs in the previous corpus had two-line headlines and
three ran to three pages, because stages estimated instead of looking. The new
corpus has one-line headlines 4/4 and two-page CVs 4/4.

**Implementation:** simpler in `Build` than here. Build's Stage 3 writes the
whole package, so `preview` can render the current `final_package.json`
directly — it does not need `assemble.py` or the layer machinery. Reuse
`render.render_job(..., destination=...)` in export mode and the pymupdf
analysis verbatim. Word COM absence prints `pages UNKNOWN` plus word counts.

**Benefit:** eliminates the guessed page count, which is the only defect class
that carries a knock-out multiplier.

### K4 · `FORFATTERSTEMME` — tic list, one-bridge rule, variation by function
The policy half of K2: the named worn-out formulas, "one transfer bridge per
letter, in the closing or inside the evidence it belongs to", and the point
that variation is about the **move** (converted employer fact / judgment case /
result case / track choice / problem / direct motive; question / contribution /
next step / motive echo / plain), not the words.

**Implementation:** copy the two hunks into `policy/writing/FORFATTERSTEMME.md`.
Pure text.

### K5 · `FORFATTERSTEMME` nominalisation example
«Bussen kom tjue minutter for sent» replacing «Jeg moderniserte verktøyet».

**Why:** the old example re-primed a claim the sources cap — it taught the
first-person form of a sentence the ceilings forbid. Pure correctness fix,
zero cost.

### K6 · `WRITING_DOCTRINE` — convert one employer fact
"When the ad gives a concrete fact about the employer's operations, scale,
systems or mandate, the letter may use it once and must immediately convert it
into a working condition the documented work answers. A name or number merely
repeated is not employer-specific."

**Why, measured:** employer-fact conversion went from roughly 1 of 4 to **4 of
4** — Stortinget's «ivareta og fornye», Norwegian's newly created function,
EIE's service mix, Abacus's ISO certification. This is the change a single
reader most reliably notices.

### K7 · `WRITING_DOCTRINE` — CV: no first person, one-line headline
**Why, measured:** `first person in CV` fired on 2 of 4 old packages — a
standing doctrine violation nobody had caught. New: 0 of 4. Old headlines run
to 93 characters and three of four open "Samfunnsøkonom og rådgiver…"; new are
44–55 characters, functional and distinct.

### K8 · `WRITING_DOCTRINE` — selective repetition (repeal, not addition)
The stable core says «En statusopplysning som allerede står i CV-en gjentas
ikke i brevet». Replace with: a status or qualifier **may** be repeated when it
carries the letter's argument, **must** be when the letter would otherwise
mislead, each document independently truthful; decorative repetition stays
prohibited.

**Why:** that one sentence is a measured evidence suppressor. The Relay CVs
carry hospital-wide use in 3 of 4 jobs and the letters omit it — the letters
obeyed the rule. This repeal is worth having **independently of everything else
here**, and it applies to the stable core unchanged.

---

## MODIFY, then keep

### M1 · `[capacity]` — make it two-sided
Ported as-is, `cv_dynamic_words = 600` was read as a target. Result: 351–395
words used, 210–250 wasted, documented evidence cut to fit a number nobody set.

**Change:** `preview` warns **under** as well as over — "CV uses 356 of ~600
available dynamic words; 240 unused. Check what the brief demoted." Same for
the letter.

**Benefit:** turns the capacity figure from a compression target into what it
was meant to be — a budget the writer should spend.

### M2 · Tools line — move it or drop it
`CV_TOOLS_METHODS` → `package.cv.tools_line`, prefix «VERKTØY  ».

**Problem:** it contributes 20–28 of the 44–58 added preamble words, sitting
*before* the employment evidence. Competency inflation (+18–28 words) accounts
for most of the rest.

**Change:** keep the field — pulling tool lists out of bullets is right — but
render it **after** the employment section, not in the header block. And cap
competencies at six, which the doctrine already says and nobody enforced.

**Benefit:** keeps the bullets clean without pushing evidence further down the
page.

### M3 · `PERSUASION_CALIBRATION` NAME_ONCE exception — add placement
The exception is right: a threshold the screener will see anyway may be named
**once**, in a sentence that converts it into the argument, never as a list or
a parenthetical apology.

**Missing:** where. The Relay's Abacus letter opens on the BNXT gap. The
independent review's objection is sound — the old letter handles the same
threshold better by establishing the qualification first and naming the gap
after. Add: "never in the opening; place it after the evidence that makes the
gap survivable."

### M4 · Evidence cards (`cards.py`) — keep the mechanism, not the default pack
The good part: `cards --ids/--search` returns a section **with its digest row
(`Lifecycle | Can prove | Live ceilings`) and every boundary line naming it**.
Facts travel with their ceilings. All four briefs quoted ceilings verbatim and
no letter exceeded one — the Relay has zero overstatement defects, which is a
real gain over a corpus where the final stage repaired an overstatement in
every job.

The bad part: a bounded default pack plus a ≤3-unit brief is how evidence gets
demoted out of the package. Retrieval was never blocked — Stage 1 *did* fetch
the AI card — but nothing required it to be used.

**Change for `Build`:** add `cards` as a retrieval command Stage 1 and Stage 3
can call, and keep the strategy's `evidence_plan[].claim_ceiling` as the
binding ceiling. Do **not** replace full-authority reading with a default pack
until requirement coverage is enforced.

**Benefit:** ceilings that travel with facts, without the narrowing.

---

## DISCARD

| Change | Why |
|---|---|
| **Four stages** (Scout / Architect / Advocate / Editor) | Higher operator load, higher cost, no measured quality gain. Nothing observed requires four sessions that two could not do. |
| **`brief.json` replacing `strategy.json`** | The active harm. 2 units + weak-requirement stances against 11–14 evidenced material requirements. This is the mechanism behind every evidence loss measured. |
| **Layers + `assemble.py`** | Only meaningful with two writing stages. Build's Stage 3 owns the whole package; the layer merge buys nothing and costs a merge semantics nobody needs. |
| **`pipeline.py` registry, dual fingerprints, `artifact_fingerprint`, the rebuilt `branch`** | Infrastructure churn with no observed output effect. Build's handoff envelope already does the job. Several defects I fixed in the experiment (the `--reject` gate, `binding_for` filtering inputs) were introduced by the rewrite and do not exist in Build. |
| **`register --cluster` as a variation check** | No employer sees the cluster. It prevents *your own corpus* looking formulaic, which matters only if one recruiter sees two applications. Keep the command if you like reading it; do not spend writer attention on it. |
| **Delivery choice / `form_answers`** | Untested — the one genuine CV-only instrument (Visma) is in the cluster that never ran. Revisit only if a CV-only vacancy comes up. |

---

## Landing order in `Build`

1. **K5, K6, K7, K8, K4, M3** — policy text only. Copy the hunks into
   `policy/writing/`. No code, no re-freeze needed for existing runs.
2. **K1 + M2** — `template_map.json`, one branch in `render.resolve_control`,
   the un-bold step already reproducible in
   `runtime/tools/prepare_masters.py::unbold_support_blocks`. Re-freeze for new
   runs.
3. **K2** — copy `signals.py`, call `scan()` from `status`.
4. **K3 + M1** — `preview`, built directly on the current `final_package.json`.
   Ship the two-sided capacity warning with it, or M1's lesson is lost.
5. **M4** — `cards` as a retrieval command, only after 1–4 are in and measured.

Steps 1–3 are a few hours and carry most of the measured benefit. Step 4 is the
one that removes a knock-out multiplier. Step 5 is optional.

## What this does not establish

The experiment changed the stage count, the writing policy, the CV template and
the model mapping at once. "Four stages is worse than two" is **not** shown by
this data — what is shown is that the brief shape lost requirement coverage and
the template change removed a knock-out cue. Those two findings are independent
of the stage count and portable on their own.
