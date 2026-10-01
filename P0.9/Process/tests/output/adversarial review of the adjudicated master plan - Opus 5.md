# Adversarial review of the adjudicated master optimisation plan

Reviewer: Opus 5. Date: 2026-09-12. Target: `adjudicated master optimization plan.md` (1555 lines)
and `implementation guidance.md` (1831 lines), both dated 2026-09-11.

This document is written to be **iterated through item by item**. Every finding has a stable ID, a
verdict I am asking for, and enough evidence to accept or reject it without re-deriving anything.
Nothing here is a request to restore my original plan. Where the adjudication overruled me and was
right, I say so first and in detail, so that none of it is re-litigated.

**Everything below was verified against the live repository on 2026-09-12.** Where I assert a fact
about the tree, I ran the check. Where I could not verify, the item says so explicitly.

---

## 0. Overall assessment

The adjudication is substantially better than the plan it replaced. Three things in particular:

- **The verification pass is the right instrument and it worked.** 225 citation locators plus 41
  claim rulings caught four material errors of mine that would otherwise have shipped into policy.
  I confirmed the most consequential ones independently; they hold.
- **E08's reframing of the lifecycle problem is better than my P5.** I proposed a channel rule
  (send `Limit` cells to review). Astra proposed an inference rule (*"Uavklart eller ikke
  dokumentert status betyr ikke at noe ikke har skjedd"*). The inference rule is correct where mine
  was crude: it fixes the reasoning error rather than hiding the input. Adopt it, drop mine.
- **E14's placement is better than my P14b's.** I proposed inserting the register section between
  `§ Selvfremstilling som skal bort` and `§ Mønstre som skal erstattes`. Astra placed it inside
  `§ Uttrykkskilde for sluttpussen`. That section is already named in the Stage-3 routing list
  (`stage3_final_writer_review.md:34-37`), and the instruction states *"Parent routes include
  children"* — so the new subsection inherits routing with **no edit to the routing list at all**.
  That is a strictly cheaper and more robust placement than mine.

E14's content is also a faithful and improved realisation of P14: the invariant floor survives at
every level, the marker IDs are replaced by five named pattern families (less mechanical, harder to
game), and page fit is correctly excluded from the register pass. I am not asking for any of it back.

My findings concentrate in three places: **four defects in shipped edit payloads**, **one structural
gap where the highest-value fix has no mechanism of action**, and **four specification ambiguities**
in a document that promises the implementing model will never have to make a design decision.

---

## 1. Concessions — where the adjudication overruled me and was right

Listed first so the planner does not spend effort re-arguing these. I have verified each against the
repository. **No action required on any of them** beyond not reopening them.

### K1 · "15 ark og 78 globale navn" is not a Gen-B-only fact (V31)

My companion ranking document attributed this detail to the Gen B authority refresh. Verified false:

```
runs/r20260905-005939-3eeb10/frozen/authorities/Work_experience.md:427
  "The FY-2025 workbook is supported at approximately 15 worksheets and 78 global named ranges."
runs/r20260905-005939-3eeb10/frozen/authorities/Work_experience.md:982
  "| Approximately 15 worksheets and 78 global names | Budget-workbook architecture scale | ..."
```

Present in Gen A. My generation attribution was wrong; V31 is correct.

### K2 · The demand-side retrieval index was never removed (V07)

My W14 claimed the authority's index was "flipped from demand-side routing to supply-side ceilings"
and proposed restoring it (P13). Verified false. `authorities/Work_experience.md § 0.4
Gjenfinningsindeks` is live and routes vacancy signals to evidence sections, including the rows this
corpus most needed:

```
| `stakeholder`, `communication`, `training`, `workshop`, `rådgivning`        | §§4.2, 5.2, 6.9 |
| `endringsledelse`, `forankring`, `etterlevelse`, `opplæring`, `adopsjon`    | §§2.2, 4.1–4.4, 4.8, 5.2, 6.7, 6.9 |
```

`§ 3.1 Standard utvalgsruter` additionally maps six named routes to lead and supporting evidence,
including `BENEFITS_STRATEGY_GOVERNANCE` and `ENABLEMENT_ADOPTION`. I compared a *different* pair of
tables across the generations and mislabelled the change. **P13 is correctly struck.**

One residue that is not a proposal: the PRJ-09 coverage asymmetry I observed (Gen A 3/3, Gen B 2/6)
is real and now has no explanation. It should be recorded as an open observation, not carried as a
cause.

### K3 · The letter master's second header row is not empty (V13)

I claimed the right-hand cell of row 2 was `<w:p />`. Verified false — it owns a control:

```
row0 cell0: tags=['APP_EMPLOYER','APP_UNIT_OPTIONAL']   row0 cell1: tags=['APP_DATE']
row1 cell0: tags=['APP_JOB_TITLE']                      row1 cell1: tags=['APP_REFERENCE_OPTIONAL']
```

The `<w:p />` I saw was in a **generated** letter, where `job.reference` was null, the control
resolved empty and `unwrap_content_controls` had already run. I read the output and described the
master. That is a methodological error on my part and V13's correction is exactly right — it also
means my P1 would have deleted a supported control.

### K4 · The page-budget evidence — my largest error

V17 says an empty `warnings` array cannot establish a page count, because
`render.py:296-305` returns `None` when `page_count is None`. Correct, and the consequence is larger
than the adjudication states. Verified from the `pdf`-format entries of each run's
`render_report.json`:

| Package | PDF state | CV pages | Letter pages |
|---|---|---:|---:|
| `3eeb10` | OK | 2 | 1 |
| `3eeb10-stage1` | OK | **3** | 1 |
| `b5104f` | OK | 2 | 1 |
| `0fa53b` | OK | **3** | 1 |
| `0fa53b-opusx` | OK | 2 | **2** |
| `93c621` | **DEGRADED** | null | null |
| `6d65bd` | **DEGRADED** | null | null |
| `0fa53b-solxh` | **DEGRADED** | null | null |
| `0fa53b-solmed` | **DEGRADED** | null | null |

V18's measured set — "A 3/1, AO 2/2, C 2/1, B 2/1 and CX 3/1" — is exactly right.

**Four of nine packages were never measured.** My plan's identification table recorded "≤2 / 1" for
those four, and my ranking tables scored them on it: CV `M` of 90/88/84/82 and package `M` of
94/92/88/92 for `solxh`, `solmed`, `6d65bd` and `93c621` respectively. Those sub-scores are partly
built on a null. The effect is concentrated in the socially-weighted package table, where
`solmed` rose to 4th on an `M` of 92 that was never measured. The top of all three tables is
unaffected — every top-five entry has a measured count — but the mid-table ordering should not be
relied on. This correction belongs in the rankings document, not in the plan, and I will make it
there.

### K5 · "Authority-mandated" was the wrong epistemology (V30)

I wrote that Gen A's *"Modellen er utformet, ikke innført"* was mandated by its frozen authority.
The frozen text says implementation and adoption are **unresolved**, which licenses silence, not a
negative assertion. V30's distinction — inability to claim an event versus evidence it did not
occur — is correct, and E08 is the right repair. My P5 (channel-marking the `Limit` column) is
inferior and should stay struck.

### K6 · `write_filled_document` does not exist (V21)

Actual name is `write_filled_docx`, `docxfill.py:316`, and `document_date` is not a parameter. My P3
patch named a function that is not there. V21 is correct; P3 is correctly dropped for this pass.

### K7 · The strong-verb floor was not missing (V09)

I claimed no surface owned confidence level after the Gen A→B refactor. Verified present:
`PERSUASION_CALIBRATION.md:53-63`, `WRITING_DOCTRINE.md:120-124`,
`stage3_final_writer_review.md:101`, `STAGE3_PROMPT.md:150-152`. What was removed was the concrete
verb *ladder*, not the floor. V09's split — verified removal of examples, wrong claim that the floor
disappeared — is right, and E11's optional status follows correctly.

---

## 2. Findings

Severity key. **A** = will produce a wrong or broken result if shipped as written. **B** = the
proposal will not achieve its stated purpose. **C** = specification ambiguity in a document that
promises none. **D** = worth considering; I would not block on it.

---

### R01 · [A] The register dial is the only unvalidated setting in the file, and E13 can crash Stage 3

**The claim.** `E12` adds `[voice].social_register_calibration` with no validation, and `E13` reads
it with a direct key access. Both of the two most likely hand-edit mistakes produce bad outcomes,
and this is a setting that exists *specifically* to be hand-edited.

**Evidence.** `settings.py::_check` validates every other tunable in the file, without exception:

| Setting | Validation in `_check` |
|---|---|
| `[product].language` | must equal `"nb-NO"` |
| `[personality].max_selected_facets` | must equal `3` |
| `[stages].stage1` / `.stage3` | must be in `ROLES` |
| `[stages].stage2` (legacy) | must be in `ROLES` when present |
| `[recovery].retry_start_stages` | list, members in `1..3` |
| `[recovery].mechanical_correction_attempts` | non-negative int |
| `[render].converter` | must be in `CONVERTERS` |
| `[render].invocation_granularity` | must be in `GRANULARITIES` |
| `[render].converter_timeout_seconds` | positive int |
| **`[voice].social_register_calibration`** | **none** |

E13 as written:

```python
    if stage == 3:
        voice = context.assets.settings.get("voice")
        if voice is not None:
            bundle["final_polish"] = {
                "social_register_calibration": voice["social_register_calibration"]
            }
```

**Reasoning.** The `voice is not None` guard handles the historical-run case correctly — I verified
`_check` uses `.get()` throughout and does **not** reject unknown tables, so a pre-`[voice]` frozen
settings file loads fine and the guard skips. That part is right. What is unguarded is the key. An
operator who writes `[voice]` with a mistyped key, or who comments the key out while testing level 0
by deletion, gets an unhandled `KeyError` inside `cmd_context` — which is the command every Stage-3
job begins with, so Stage 3 dies for the whole run with a traceback rather than a diagnostic. And an
operator who writes `7`, or `"2"`, or `2.5`, passes silently into a bundle whose consuming document
defines only levels 0–4.

Tuning by hand between child runs is the entire interaction design of this feature. The expected
user action is exactly the one that breaks it.

**Proposed fix.** Nine lines in `settings.py::_check`, in the file's own idiom, placed after the
`[personality]` block:

```python
    voice = data.get("voice")
    if voice is not None:
        level = voice.get("social_register_calibration")
        if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 4:
            raise ConfigurationError(
                f"{path.name}: [voice].social_register_calibration must be an "
                f"integer 0..4. FORFATTERSTEMME.md defines exactly those levels. "
                f"Found {level!r}."
            )
```

With that in place, E13's direct key access becomes safe and needs no change. If the planner prefers
not to touch `settings.py`, the minimum alternative is `voice.get("social_register_calibration")`
in E13 plus a `is not None` check — but that silently accepts out-of-range values, which is worse.

**Why this fix and not another.** It is not defensive scaffolding under ED-1, because every sibling
setting already carries exactly this validation; omitting it for the new key is the deviation, not
adding it. It moves the failure from a Stage-3 traceback to a load-time `ConfigurationError` with
the level named. And it costs nine lines in a function that is already a flat list of nine identical
checks.

**What would change my mind.** If the planner intends `[voice]` to be forward-compatible with
additional keys and does not want `_check` to know about it, then say so and use `.get()` with a
range clamp in E13 instead. Either is defensible. Shipping neither is not.

---

### R02 · [B] C01's fix has no mechanism distinguishing it from the instruction that already failed

**The claim.** This is my most important finding. The evidence for C01 is that nine consecutive
packages under-covered material role functions. The framework **already instructed exactly this**.
E03 and E04 replace that instruction with a longer and better one. Nothing in the plan explains why
a better-worded version of an instruction that failed nine times will succeed the tenth.

**Evidence.** The current Stage-3 text is `stage3_final_writer_review.md:54`:

> "Address material requirements and gaps truthfully, build specific motivation, and remove
> repetition that adds neither a new function nor useful detail."

E04 replaces it with ten lines of considerably sharper guidance. But the observed failure was not a
comprehension failure. Stage 1 produced 12–19 well-formed `material_requirements` entries per run,
each with `importance`, `relation`, `note` and `evidence_refs`; Stage 3 received them via
`read.strategy`; and V01 correctly establishes that no data was lost. The instruction was clear
enough, the data was present, and the allocation still did not happen — in nine of nine runs, across
two policy generations and at least three different executing surfaces.

That is the signature of an **unobservable** duty, not an unclear one. No artefact in the pipeline
records what the writer decided about each requirement, so nothing can be inspected afterwards, and
no run can be compared with another. The plan's own next-run signal for M01 is *"the reviewer can
point to a supported action and recipient"* — which is a human reading the prose, exactly what was
being done before.

The adjudication identifies the vehicle and then declines to use it. V03, verbatim:

> "review already has `notes` (array of strings, review.schema.json:63), `material_strategy_change`,
> `upstream_claim_repaired`."

I verified that field: `"notes": { "type": "array", "items": { "type": "string", "minLength": 1 } }`.
It is an existing, optional, free-text array. Using it costs **no schema change, no new key, no
validator, no field on the package, and no ledger** — which is every objection F01 raises against my
P8, all of which I accept.

**Proposed fix.** One sentence appended to E04's replacement text:

```text
   Where a requirement the strategy marked SUPPORTED under MINIMUM or IMPORTANT is not
   answered in either document, say so once in review.notes with the reason. This is an
   existing free-text field; do not create a coverage field, matrix, ledger or score.
```

Alternatively — and this may be cleaner — fold it into the existing review instruction at
`stage3_final_writer_review.md:124-125` (*"Record known limitations relevant to human approval"*)
rather than adding to E04 at all, so the duty sits with the review where it belongs.

**Why this fix specifically.** It is the smallest intervention that converts an unobservable duty
into an observable one, and it reuses a field the adjudication itself named. It creates no
compliance matrix: the writer is not asked to account for every requirement, only to name the
SUPPORTED ones it chose to leave unanswered. And it produces a genuinely falsifiable next-run
signal — I checked all nine current reviews, and **not one names a single unanswered SUPPORTED
requirement**, so any occurrence after the change is evidence the instruction bit, and continued
silence is evidence it did not.

**What would change my mind, and this is a real possibility.** Two counter-arguments I would accept:

1. `review.notes` currently carries source-inspection caveats and deadline notes. If the planner
   judges that field semantically reserved, or judges that a required entry would produce ritual
   compliance ("all requirements addressed") rather than information, that is a fair call.
2. The planner may hold that C01 is simply not fixable by instruction and that E03/E04 are worth
   shipping as a partial improvement regardless.

**Either resolution is acceptable. What is not acceptable is leaving the gap unstated.** If no
observability mechanism ships, the plan should say plainly under M01 that the next run **cannot
confirm or refute** this proposal, so that a subsequent reader does not mistake an unchanged outcome
for a failed hypothesis, or an improved one for a working mechanism.

---

### R03 · [A] E21 leaves the relocated reference right-aligned

**The claim.** E21 moves `APP_REFERENCE_OPTIONAL` from the right-hand table cell to body level
without adjusting its paragraph properties. It carries a right-alignment that was authored for the
cell.

**Evidence.** Verified from the live master:

```xml
<w:pPr><w:spacing w:after="0"/><w:jc w:val="right"/></w:pPr>
```

E21 does `parents[reference].remove(reference)` then
`body.insert(list(body).index(table) + 1, reference)`, and touches no `pPr`. Body order after the
edit is `[tbl] [APP_REFERENCE_OPTIONAL] [p Title "Søknad: …"] [sdt APPLICATION_BODY] [p signature]`.
So a job with a reference renders a right-aligned `Referanse: 474473271` floating between the
address block and the subject line, against a left-aligned subject directly beneath it.

**Scope, stated honestly.** This is **latent, not currently visible**. I verified that the Avinor
job carries `"reference": None` in its manifest, so the control resolves empty for the job this plan
will be evaluated on. But E21 is a permanent master change, and FINN-sourced vacancies routinely
carry a reference.

**Proposed fix.** Two lines inside E21's transformation, after the relocation:

```python
for paragraph in reference.find(f"{W}sdtContent").findall(f"{W}p"):
    properties = paragraph.find(f"{W}pPr")
    justification = properties.find(f"{W}jc") if properties is not None else None
    if justification is not None:
        properties.remove(justification)
```

Removing `w:jc` lets the paragraph inherit the document default (left), which is what the subject
line beneath it uses.

**Secondary check I could not complete and am flagging rather than asserting.** With
`reference: None`, `fill_block` clears the control and `unwrap_content_controls` removes the wrapper.
Inside a table cell an empty result was invisible. At body level it may leave a stray empty
paragraph and a blank line between the address block and the subject. This is cheap to settle and
R05's smoke check would settle it as a side effect — but it should be settled before the master is
written, not after.

---

### R04 · [A] Cluster D has no fill-level check, only structural ones

**The claim.** Batch D validates that the revised masters *parse and count correctly*. Nothing
validates that they still *produce a document*.

**Evidence.** Batch D runs the E18–E23 and E25–E27 marker checks, the two existing T18 assertions,
and `python -m tools.prepare_masters --check`. Every one of those inspects structure: control
inventories, element order, attribute values, anchor resolution. None exercises
`docxfill.write_filled_docx` → `edit_document` → `fill_block`/`fill_inline` →
`unwrap_content_controls` → `assert_no_controls` against an actual package.

**Reasoning.** Cluster D makes two structural changes that a count check cannot cover. E20 removes
six `w:sdt` elements from `w:body` and reinserts them at a computed index — I verified all 17 CV
controls are direct body children, so the operation is feasible, but feasibility is not the same as
the fill path still working across the new ordering. E21 moves a block SDT **across a structural
boundary**, from inside `w:tc` to `w:body`. `fill_block` requires exactly one matching control and
deep-copies a prototype paragraph from `sdtContent`; `assert_no_controls` runs after unwrapping and
raises if any control survives. A structural assertion passes in every case where those would fail.

The plan explicitly forbids `--probe` and forbids new tests, and I agree with both. This is neither:
it is one command, at a cluster boundary, using functions and fixtures already in the repository.

**Proposed fix.** One command appended to batch D, written to leave nothing behind:

```powershell
& $Py -c @'
import json, tempfile, sys
from pathlib import Path
sys.path.insert(0, "runtime")
from jobbsok.docxfill import write_filled_docx, visible_text, control_inventory
pkg = json.loads(Path("evidence/vertical_slice/fixtures/final_package.json").read_text(encoding="utf-8"))
with tempfile.TemporaryDirectory() as d:
    for master, stem in (("CV_MASTER.docx", "cv"), ("APPLICATION_MASTER.docx", "letter")):
        out = Path(d) / f"{stem}.docx"
        # fill via the same entry point render.py uses; see render.py for the edit_document callable
        # assert no residual controls and that identity text survives
        print(stem, "filled:", out.exists())
'@
```

I have deliberately left the `edit_document` callable construction to the planner rather than
guessing it: `render.py` builds it and I did not trace that assembly closely enough to write it
verbatim, and this document does not ship unverified code. **The planner should complete this step
from `render.py`'s existing call site, or reject the finding.** What matters is the assertion set,
which is: both files produce, `assert_no_controls` passes, and `visible_text` contains the identity
anchors the map's `verification.identity` block already names.

**Why this fix.** It is ED-3 compliant — one validation at a cluster boundary, not per step. It adds
no test file and no artefact. And it converts "the XML still parses" into "the pipeline still
produces a document", which is the property Cluster D actually puts at risk.

---

### R05 · [C] E23's four replacements fail silently if any anchor has drifted

**The claim.** E23 performs four `str.replace(old, new, 1)` calls and writes the result
unconditionally. `str.replace` returns the string unchanged when the pattern is absent, so a drifted
anchor produces a silently unmodified file.

**Evidence.** I verified all four anchors exist **today**, exactly once each:

```
(("text", "Stilling:"), [(17, 20, *_KEEP), (17, 20, *_KEEP)]),          → 1
The control contract is deliberately untouched: the 17 CV tags and the 6 → 1
#: APPLICATION_MASTER.docx -- all 8 body paragraphs, 7 sized runs.       → 1
Anchors are SDT tags for the 24                                          → 1
```

So E23 will work if executed against the tree as it stands. The risk is that `prepare_masters.py` is
a live maintenance file and the plan's own execution model allows time between adjudication and
implementation.

**Reasoning on severity.** The first replacement is self-protecting: if the `Stilling:` row survives,
`_resolve_anchors` will demand a paragraph E21 deleted and `prepare_masters --check` fails loudly at
batch D. The other three are comment and docstring edits with no consumer, so a silent failure
leaves the module describing a contract it no longer has — which is exactly the documentation drift
C16 is about, reintroduced by the fix for C12. Only one of the four has an observable check.

**Proposed fix.** Four assertions, one per replacement:

```python
before = text
text = text.replace(old, new, 1)
assert text != before, "E23: anchor drifted — re-read prepare_masters.py before proceeding"
```

**Why this fix.** It is the minimum that makes a silent no-op loud, it matches the plan's own
per-step reversibility discipline, and it costs one line per replacement. The same pattern is not
needed for E22, E25 or E27, which write JSON or recomputed values unconditionally.

---

### R06 · [C] E27's prerequisite list is unsatisfiable when Cluster B is skipped

**The claim.** E27 lists `E01 … E26` as prerequisites with a parenthetical
"(selected/accepted steps only)". The implementation guidance says of Cluster B: *"Skip this entire
batch if no correction was accepted."*

**Reasoning.** The master plan states that it *"must contain no instruction that requires the
implementing model to make a design decision"*. A prerequisite list naming steps the same document
says to skip, disambiguated only by a parenthetical, is precisely such a decision. It is small, but
E27 is the last step before the run boundary and the one whose output is a provenance registry.

**Proposed fix.** State the prerequisite as "every step in clusters A, C and D that was executed,
plus cluster B only if a correction was accepted", and build `affected` from the files actually
modified rather than from a static list. The static list is currently harmless — recomputing an
unchanged file's hash yields the same value — but the derived form removes the ambiguity entirely.

---

### R07 · [D] E18 removes the label's visual function together with the wall, and there is a cheaper alternative

**The claim.** E18 sets `w:val="0"` on the competence run's `<w:b/>`, making the whole line regular
including the label `KJERNEOMRÅDER`. The wall of bold goes, and so does the only thing marking the
zone.

**Evidence.** Verified structure of `CV_CORE_COMPETENCE`:

```
sdtContent children: ['p']       paragraph pStyle: None       run count: 1
run0 rPr: <w:rFonts .../><w:b /><w:color w:val="17324D"/><w:sz w:val="24"/>
```

One paragraph, one run, `<w:b/>` as direct formatting with no competing paragraph style. So E18 will
work exactly as specified — I am not disputing the mechanism. The consequence is that after the edit
this zone is 31–81 words of undifferentiated regular text in a CV where every other section carries
a teal `Heading1` with a bottom border.

The plan's cost note says *"somewhat less visual emphasis within the competence line"*. That
understates it: the label stops being a label.

**Proposed alternative, offered as an option rather than a correction.** Move `KJERNEOMRÅDER` out of
`template_map.json`'s `prefix` and into the master as its own short bold paragraph immediately
before the SDT. Then the label keeps its weight, the competencies render regular, and — the key
point — **the renderer is untouched**. `_set_paragraph_text`'s one-run behaviour, which is the exact
reason F14 rejected my P2's tuple plumbing, becomes irrelevant, because the label is no longer inside
the control.

Cost of the alternative, stated honestly: it adds a line to a CV that already reaches three pages in
two of the measured packages, it changes vertical rhythm, and it needs a visual check that this pass
cannot perform. That may well be enough to prefer E18 as written. I am asking for the trade-off to be
made explicitly, not for a particular outcome.

**One smaller point on E18 regardless of which option is chosen.** Prefer *removing* the `<w:b/>`
element to setting `w:val="0"`. Both are valid `ST_OnOff` and both render identically. Removal is
what a human editing the master in Word would produce, and it is immune to any consumer that tests
for element presence rather than value. E18's own observable check would then assert
`find('.//w:rPr/w:b') is None`, which is also a cleaner assertion than comparing an attribute.

---

### R08 · [D] The distinction C09 needs is not in E06, E09 or E15

**The claim.** F19 correctly rejects my scoring of `3eeb10-stage1`'s aviation sentence as a trust
bonus. But C09 now folds that sentence in with the mandate disclaimers of C03, and no shipped edit
distinguishes them. They are different moves with different costs.

**The sentences.**

- `3eeb10-stage1`: *"Det som gjør Avinor interessant, er ikke luftfarten i seg selv. Der har jeg
  ingen bakgrunn. Det er at dere driver noe som ikke kan settes på pause mens det forbedres."*
- `0fa53b-solmed`: *"Rollen min har vært prosjekt- og metodeorientert, ikke et formelt konsernmandat
  for portefølje- eller programledelse."*

**Reasoning.** I concede the inference F19 strikes: absence of experience does not establish absence
of interest, and I should not have scored the first sentence as evidence of honesty. That is
correctly rejected and I am not asking for it back.

What remains is a structural difference the plan does not capture. The first names an absent domain
the reader can already see is absent, and **uses the naming to pivot into a supported claim in the
same breath** — the sentence exists to deliver "dere driver noe som ikke kan settes på pause". The
second names a requirement the advertisement marks *"en fordel"* and leaves it standing as a property
of the candidate, with no pivot.

E09 item 5 is the right hook — *"Behold et uttrykkelig forbehold når den konkrete teksten ellers
ville villede vesentlig"* — but it covers the misleading-silence case, not the redirect case. Without
the distinction, E14's register pass at level 2 or above has grounds to recast the first sentence as
"unødvendig avstand" or "seiers- eller konfliktpreg" and lose the pivot with it.

**Proposed fix.** One clause, best placed in E09 item 4:

```text
   En setning kan navngi et fravær når den i samme trekk går over til det som faktisk er
   støttet og bærer argumentet videre. Den skal ikke la fraværet stå igjen som en egenskap
   ved kandidaten.
```

**Why this fix.** It is one sentence in an edit that is already being made, it uses the distinction
the corpus actually shows, and it protects a construction that the register pass would otherwise have
licence to remove. It does not restore any scoring claim of mine.

---

### R09 · [C] Skipping Cluster B confounds the next run, and the plan does not say so

**The claim.** E08–E10 are the only shipped fixes for C02 and C03. The guidance permits shipping A,
C and D without them. If that happens, the next run cannot test M04, and the plan does not warn the
reader.

**Reasoning.** C02 (unknown status written as negative fact) and C03 (redundant negative mandate
clauses) are the two highest-confidence weaknesses in the catalogue with a shipped remedy. E14's
floor explicitly forbids the register pass from touching a material qualification — correctly. So if
Cluster B is skipped, the output of the next run still contains `ikke innført`-class sentences, and
the register pass is required to leave them alone. A reader inspecting that output has no way to tell
whether M04 underperformed or whether it was correctly declining to fix something outside its remit.

**Proposed fix.** No mechanism change. One sentence in the ordering section:

```text
If the M03 correction is not accepted before the boundary, the next run is not a test of M04:
C02 and C03 sentences will still be present and the register pass is required to preserve them.
Record that before rendering, and do not read their survival as a register-pass failure.
```

The alternative — seeking Vegard's acceptance before the boundary rather than after — is better if it
is available, and worth saying so.

---

### R10 · [D] Register levels 1–4 are not separable by observation, which makes the default unresolvable

**The claim.** The plan names its least certain decision as *"default register level 2"*. As
specified, no observation can ever resolve it.

**Evidence.** E14 defines level 4 as *"Gjør nivå 3 og velg den mest direkte, naturlige lokale
formuleringen som bevarer hele innholdet. Nivået gir ingen større adgang til å slette, omdisponere,
svekke eller tilføre noe enn nivå 1."* and closes with *"Ingen telling av markører, ord eller
evidensreferanser avgjør om pussen er god."*

**Reasoning.** Both statements are individually right — the invariant floor is the safety property
that makes this whole mechanic acceptable, and marker counting is correctly forbidden. Together they
mean levels 3 and 4 differ only in how hard the model tries at local phrasing, with no defined
observable difference and no permitted measurement. So the operator can turn the dial and cannot tell
whether it did anything, and the plan's own stated uncertainty is structurally unresolvable.

**Proposed fix — two options, either acceptable.**

1. **Collapse to 0–3**, with 3 as maximum. Levels 1, 2 and 3 have genuinely distinct scopes in E14's
   own text (pattern families added at each step); 4 adds only effort. Fewer levels, all separable.
2. **Keep 0–4 and say what the dial is.** Add one sentence to E14: the level is an operator intent
   signal, levels 3 and 4 are not expected to be distinguishable in a single output, and the default
   is a starting point rather than a measured optimum.

Option 2 is cheaper and matches the plan's existing honesty about the default. Option 1 is a better
interface. I would ship 2 now and consider 1 later.

---

### R11 · [D] Two items to verify rather than act on

Neither is a finding; both are things I could not settle and would rather name than assume.

**R11a — E13 and `REVIEW_ONLY`.** E13 gates on `stage == 3`. E16 states *"REVIEW_ONLY performs no
polish."* Exposing `final_polish` in a REVIEW_ONLY bundle is harmless but slightly misleading. If
`handoff.mode` is already resolved at that point in `cmd_context`, gating on it too is a one-line
tightening. I did not verify that the mode is available at that line, so this is a question, not a
proposal.

**R11b — C05's source-cause column.** V02's rejection of my keyword counting is correct and I accept
it entirely: a missing noun is not missing evidence. The residue that survives is a content
observation, and it is already C05. What C05's cause column does not name is *where* the available
evidence sits. `Work_experience.md § 6.9` carries "Executive/management decision support" and
"Workshops/presentations for mixed audiences"; `§ 5.2` carries "decision notes, executive summaries,
workshops, documentation and onboarding" adapted to "controllers, managers, specialists and technical
staff". None of it reaches employer text in any of the nine packages. E03's replacement text asks
Stage 1 to identify unanswered material questions but does not point at these sections. Naming them
in C05's cause column costs nothing and makes the catalogue entry actionable.

---

## 3. Summary of requested actions

| ID | Sev | Ask | Cost if accepted |
|---|---|---|---|
| R01 | A | Validate `[voice]` in `settings.py::_check`; E13 then safe as written | 9 lines |
| R02 | B | Give C01 an observability mechanism via existing `review.notes`, **or** state plainly that it has none | 1 sentence, either way |
| R03 | A | Strip `w:jc` from the relocated reference in E21; settle the empty-resolution case | 5 lines |
| R04 | A | One fill-level smoke check at the end of batch D, using existing fixtures | 1 command |
| R05 | C | Assert each of E23's four replacements changed the text | 4 lines |
| R06 | C | Derive E27's prerequisites and `affected` list from steps actually executed | spec only |
| R07 | D | Choose explicitly between E18 as written and a master-side label paragraph; prefer element removal to `w:val="0"` | spec, or 1 master edit |
| R08 | D | One clause in E09 separating a pivoting absence from a standing one | 1 sentence |
| R09 | C | Say that skipping Cluster B makes the next run not a test of M04 | 1 sentence |
| R10 | D | Collapse levels to 0–3, or state that 3 and 4 are not separable | 1 sentence |
| R11 | — | Verify `handoff.mode` availability at E13; name §6.9/§5.2 in C05 | — |

**If only three are taken: R02, R01, R04.** R02 is the difference between a plan that can be
evaluated and one that cannot. R01 and R04 are the two places where a shipped edit can break
something, and both are cheap.

---

## 4. What I am not asking for

Explicitly, so the planner does not spend effort defending decisions I accept:

- **No schema growth.** F01's governing ruling is correct on the evidence. `requirement_coverage`,
  `register_calibration` and `cv.selected_evidence` all stay rejected. R02 is deliberately built to
  need none of them.
- **No probe render.** V19 is right that it is a substantial new route, and R04 is a single
  cluster-boundary check, not a loop.
- **No metadata rewrite.** V20 and V21 are correct; P3 stays dropped for this pass.
- **No index restoration.** K2 above; P13 stays struck.
- **No similarity measurement, marker counting, cultural scoring, preservation ledger, model
  routing change or authority edit.** All correctly excluded, and R02 through R11 introduce none of
  them.
- **No restoration of my P2 tuple plumbing.** F14's reasoning holds; R07 offers an alternative that
  avoids the renderer entirely rather than reopening it.

---

## 5. One closing observation

The adjudication's own stated least-certain decision is default level 2. Mine is different: it is
**R02**. Every other finding here is a defect with a bounded fix. R02 is a question about whether the
plan's top-ranked proposal can work at all, and I hold it at medium confidence rather than high,
because the counter-argument — that the observed failure really was a comprehension failure and
sharper prose really will fix it — is not absurd. It is simply untested, and as the plan currently
stands it will remain untested after the next run too. That is the thing I would most like the next
iteration to close, in whichever direction it decides.
