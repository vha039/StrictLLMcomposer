# Relay, first cluster — analysis of the results, and against their `rung` counterparts

Run `r20260916-184816-a1ea76`, cluster `rung`, four jobs. Stages 0–3 all ran as
human-started sessions. Stage 3 could not submit. This document says why, what
the output is actually worth, and where the design is leaking value.

Counterpart corpus: `runs/r20260914-211651-5dbd38` — the same four vacancies,
same frozen authorities, produced by the two-stage 0.9.3 harness (`rung`,
GPT-6 Astra medium). Scores below reuse the rubric in
`Process/tests/output/runf-rung analysis and cross-run rankings - Opus 5.md`
§5.1 unchanged, and reproduce all four `rung` figures exactly before being
applied to the new packages.

---

## TL;DR

1. **The harness failure is a gate-placement bug, not a hashing bug.** Stage 3
   was locked out of `--reject` — the one action it was supposed to be able to
   take — because `cmd_stage_submit` checks upstream currency *before* it reads
   the `--reject` flag. The stage whose job is declining cannot decline exactly
   when declining is correct.
2. **A separate, real bug made the diagnosis harder:** `artifact_hash` includes
   the `binding` block, so `cv_draft` — semantically byte-identical across every
   revision in all four jobs — was reported as having "changed". The stale
   reason named two moved artifacts when only one moved. Worth fixing, but
   fixing it would **not** have unblocked this run: the briefs genuinely changed.
3. **The editorial work is good and the four design bets paid off.** Move
   variation, headline discipline, capacity, and tic elimination all show
   measurable, clean wins over `rung`.
4. **One systematic regression, and it is the expensive one.** Adoption and
   persistence facts — the evidence that the work was taken up and is still in
   use — went from 11 occurrences across the four `rung` letters to **0** in the
   four Relay letters.
5. **A documented, explicitly confirmed differentiator was dropped:** «i praksis
   eneste kodende utvikler», which the WORK §4.3 digest row lists under *can
   prove* and which `interview_defensibility` calls out by name. The Relay
   replaced it with the safe paraphrase in two letters and both CVs.
6. **Root cause of 4 and 5 is one schema asymmetry.** `brief.units` stores a
   **verbatim** `ceiling` and a **paraphrased** `proves`. The limit is protected
   word-for-word; the asset is degraded to the Architect's summary — and that
   summary is what the letters echo.
7. **`judgment` is `null` in 4 of 4 briefs.** The field the whole 0.9.2 lesson
   was about got 0% uptake because it is optional.
8. **A new tic class appeared that no detector covers:** impersonal generalising
   sentences. Counted: 14 in the `rung` letters, **27** in the Relay letters —
   and the composition inverted from facts to principles.

Scoring, same model as the earlier report: mean IOI **30.9 → ~34.8**, mean
expected chance **26.5 → ~30.0**. Three of the four Relay packages would rank
above `rung`'s best. See §D for the arithmetic and its caveats.

---

> ## CORRECTIONS — 2026-09-18
>
> An independent review (`reviews/CODEX_DIFF_REVIEW.md`) overturned six items
> below. All six were re-verified against the repository; the review is right on
> every one. **Where this block and the body disagree, this block is correct.**
> The body is left intact so the reasoning that produced the errors stays legible.
>
> | Item | Body says | Verified truth |
> |---|---|---|
> | §B.6, TL;DR 7 | `judgment` is `null` in 4 of 4 briefs | **False.** All four current briefs and all six historical ones carry a populated `judgment` object with refs and a ceiling (`current/brief.json:37-45` per job). My diagnostic read a `claim` key that does not exist; the field is `judgment`. Norwegian's judgment even contains the controller-handover fact. **§B.6 is withdrawn in full.** |
> | §B.5, TL;DR 6 | Root cause is the `proves`/`ceiling` schema asymmetry | **Not established.** The facts were present at every upstream point: Norwegian's `current/brief.json:40` states completion and handover, and its delivered `cards_scoped.md:87,117-121,155` carries sole-coder, hospital-wide use and handover. Nothing was paraphrased away. The competing explanation is concrete and sits in policy: `policy/writing/WRITING_DOCTRINE.md:295-297` — «En statusopplysning som allerede står i CV-en gjentas ikke i brevet» — and the Relay CVs carry hospital-wide use in 3 of 4. The letters obeyed the doctrine. |
> | §B.1 counts | CV 1761→1458, letters 1608→1361 | Recounted with the runtime counters (`signals.cv_dynamic_words` / `letter_words`, which include the tools line): counterpart **1818 / 1613**, Relay **1458 / 1361** — CV −19.8%, letter −15.6%. Per job, counterpart CV/letter: Stortinget 431/458, Norwegian 504/446, EIE 424/374, Abacus 459/335. |
> | §B.3 count | "11 adoption facts" | Wrong unit. The five literal phrases give counterpart **8 matches across 4 sentences** (Stortinget 2/1, Norwegian 4/2, EIE 0/0, Abacus 2/1) and Relay **0/0**. It is a *letter* omission, not package-wide loss, and completion/handover is not the same lifecycle state as organizational adoption. |
> | §D caveat | The polish layer "never reached disk in a place `preview` reads" | **False.** `preview._in_progress` recursively finds every saved polish return and all four are discoverable. The correct statement is the one the reviews themselves make: the editor measured the pre-polish draft and no post-polish render exists. (Separately, `preview` selects the *lexicographically last* fingerprint directory, not the current one — see A6 in the development plan.) |
> | §A.1 | "no decision field moved" in the second brief pass | **False.** Stortinget's and EIE's second revisions rewrote `stances[].line`, the prescribed NAME_ONCE sentence — Stortinget from «det jeg tar med, er» to «Med meg tar jeg». That is the *same* cleft repair Stage 3 later made as K4 REWORDED. The two saved Stage 3 returns for those jobs are therefore not blindly reusable. |
> | Header | "same frozen authorities" | Same vacancies and identical EDU/OTHER hashes; **WORK differs** by the corrected BAR digest sentence (`frozen/authorities/Work_experience.md:66`). A confound wherever early-role ownership is assessed. |
>
> **Unchanged and re-confirmed:** the `--reject` gate defect (§A.2), binding-inclusive
> hashing (§A.3), the silent downstream invalidation (§A.4), the gate-placement
> inconsistency (§A.5), move/headline/tic wins (§B.2), and that the adoption facts
> are absent from all four letters (§B.3, with the corrected count).
>
> **§D scoring is withdrawn as a predictive claim.** The IOI and expected-chance
> figures rest on an uncalibrated logistic with no observed outcomes, and the
> Norwegian row compares different delivery instruments. Read the paired document
> differences, not the probabilities.

---

# Part A — the harness

## A.1 What actually happened

| Time (UTC, 16 Sep) | Event | Evidence |
|---|---|---|
| ~21:5x | Stage 1 submits brief + cv_draft, round 1 | superseded copies exist |
| 21:57–22:01 | Stage 2 writes all four letters | `advocacy_draft` binding `inputs` |
| 22:03:44–45 | **Stage 1 re-submits all four briefs** | `history/20260916T2203xxZ_brief.json` |
| 22:05:53–58 | Stage 1 re-submits Stortinget and EIE again | `history/20260916T2205xxZ_*` |
| later | Stage 3 opens, `context --stage 3` refuses on all four | transcript |

Verified by recomputing the tool's own hashes rather than trusting the session
report. Per job, comparing each `history/` copy with `current/`, excluding
`binding`/`artifact_role`:

| Job | `brief` semantically identical? | `cv_draft` semantically identical? |
|---|---|---|
| abacus | **no** | **yes** |
| eie (2 revisions) | **no**, **no** | **yes**, **yes** |
| norwegian | **no** | **yes** |
| stortinget (2 revisions) | **no**, **no** | **yes**, **yes** |

So: **the briefs really did change; the CV layers never did.** Stage 1 ran a
late tightening pass over the cluster after Stage 2 had already written. The
transcript's description of that pass is accurate — `employer_problem` trimmed
to one quoted phrase, `notes`/`traps`/`reserve` shortened, no decision field
moved.

## A.2 H1 — `--reject` is gated behind the condition it exists to handle · **critical**

`runtime/jobbsok/cli.py`, `cmd_stage_submit`:

```python
missing = [name for name in pipeline.STAGES[stage].requires if not state.current(name)]
if missing:
    raise JobError(f"Stage {stage} needs current {', '.join(missing)}. ...")
...
reject = bool(getattr(args, "reject", False))          # read 15 lines too late
```

`state.current()` is `loaded and valid and not stale`. Stage 3 `requires`
`brief, cv_draft, advocacy_draft`. A stale `advocacy_draft` therefore blocks
`--reject`, whose entire purpose is to say *this upstream layer is not fit to
publish, re-run stage N*. `cmd_context` carries the same check, so there is no
bundle either, and the fingerprint the submit command wants cannot be obtained.

Net effect: the run reached a state with **no legal next action from Stage 3 at
all** — it could not publish, could not decline, and could not record why.
That is the defect that cost the session.

## A.3 H2 — `artifact_hash` includes `binding`, so staleness over-reports · **high**

`runtime/jobbsok/artifacts.py:38-47` hashes the whole payload, excluding
`finalization` only for the package role. `binding.inputs` is part of it.

`cv_draft` declares `brief` as an input. So when `brief` changed:

```
abacus: advocacy_draft stored inputs  brief=0cc55253  cv_draft=79c756c4
        recomputed                    brief=e63ce70b  cv_draft=966221bd
        cv_draft SEMANTIC hash                        106512af  (unchanged)
```

`_stale_reason` then emitted `upstream changed: brief, cv_draft`. Only `brief`
changed. The Stage 3 session spent a turn building a theory around a phantom
`cv_draft` change and reported "half the staleness is a no-op resubmit" — a
conclusion the tool's own message invited.

**Be clear about what this costs.** It does not cause false staleness here,
because `brief` moved for real. It costs *diagnostic honesty*, and it will
cause false staleness the moment a stage resubmits one of a sibling pair
unchanged. Both `brief`+`cv_draft` (Stage 1) and `polish`+`review` (Stage 3)
are sibling pairs, so this is a live hazard, not a hypothetical.

## A.4 H3 — an upstream submit silently invalidates downstream work · **high**

`cmd_stage_submit` never looks at what already exists below the stage being
submitted. Stage 1's 22:03 pass invalidated four finished letters and printed
nothing about it. Nothing is written to the record either — the run cannot
later explain why the letters went stale.

## A.5 H4 — the gates are in three different places · **medium**

| Command | Refuses on stale upstream? |
|---|---|
| `context` | yes |
| `stage-submit` | yes |
| `preview` | **no** — `preview.py` has no currency check at all |
| `assemble --dry-run` | **no** |
| `register` | **no** — reads `current/` regardless |

This is what let the Stage 3 session do the whole editorial job while being
unable to record it. Convenient here, but it means `register.md` can silently
describe superseded text as if it were the cluster's variation baseline, which
is a quiet correctness hazard for the one check that governs cross-job
differentiation.

## A.6 H5 — the recommended action is wrong for the common case · **medium**

`status` emits `recommended_action: Run Stage 2 (ADVOCATE)`. For a brief whose
*decision* fields did not move, re-running Stage 2 means paying a full advocacy
session to re-produce essentially the same letter. There is no cheaper verb —
no `--rebind`, no "confirm this layer still stands against the new upstream".

## A.7 H6 — `branch` is not a recovery path

`branch.py:204` carries the parent's `inputs` hashes into the new stamp, then
re-tests staleness and **drops** whatever is still stale. Branching from stage 3
would delete the four letters. The Stage 3 session checked this and was right
not to run it.

## A.8 Not harness defects

- **The "audit tampering" block was Claude Code's own permission layer**, not
  `jobbsok`. The harness has no such classifier. Worth knowing, because the
  right conclusion is "re-stamping bindings by hand is outside the tool's
  surface", not "the tool defends itself".
- **The missing `advocacy_draft` history entry** was correct behaviour:
  `artifacts.py` moves a *superseded* copy to `history/`, so an artifact
  submitted once has none. The session corrected this itself.
- **`review.semantic.json` / `polish.semantic.json` are recoverable.** They sit
  under `generated/returns/<run>/<job>/stage3/<old fp8>/`. `_read_return`
  resolves by path only and `stamp` rebuilds the binding from the live context,
  so after Stage 2 resubmits, copying the two files into the new `fp8`
  directory printed by `context` is sufficient. No content is invalidated.

---

# Part B — the output, measured

## B.1 The headline numbers

| Job | letter words | CV dynamic words | adoption facts | impersonal sentences |
|---|---|---|---|---|
| Stortinget `rung` | 457 | 417 | 3 | 4 |
| Stortinget Relay | **322** | **349** | **0** | **5** |
| Norwegian `rung` | 445 | 492 | 5 | 6 |
| Norwegian Relay | **321** | **383** | **0** | **9** |
| EIE `rung` | 373 | 409 | 0 | 2 |
| EIE Relay | **356** | **381** | **0** | **6** |
| Abacus `rung` | 333 | 443 | 3 | 2 |
| Abacus Relay | **362** | **345** | **0** | **7** |
| **total** | 1608 → **1361** (−15%) | 1761 → **1458** (−17%) | 11 → **0** | 14 → **27** |

*Adoption facts* = sentences carrying `ble brukt` / `brukes nå` / `er i bruk` /
`overlevert` / `ble ferdigstilt`. *Impersonal sentences* = sentences of ≥7 words
containing no first-person pronoun. Both are regex counts over the merged
letter text.

## B.2 What got better — and it is not small

**Move variation: 4/4 distinct openings and 4/4 distinct closings.**

| Job | Relay opening | Relay closing | `rung` opening | `rung` closing |
|---|---|---|---|---|
| Stortinget | EMPLOYER_FACT | QUESTION | title restated | «søker fordi» + stock close |
| Norwegian | JUDGMENT_CASE | CONTRIBUTION | title restated | stock close |
| EIE | PROBLEM | NEXT_STEP | title restated | «søker fordi» + stock close |
| Abacus | TRACK_CHOICE | MOTIVE_ECHO | title restated | stock close |

`rung` restated the vacancy title in **4 of 4** openings and used a stock
"happy to talk more" close in **4 of 4**. The Relay has **zero** of either. This
is the single cleanest validation of the design in the whole run: the
`register.md` + `distinctiveness.opening_move/closing_move` mechanism does what
it was built to do.

**Headlines.** `rung`: three of four begin "Samfunnsøkonom og rådgiver…",
longest 93 characters — near-certainly two rendered lines in caps, which is a
screen-out cue. Relay: 44–55 characters, four distinct functional headlines,
each naming a function rather than listing three things. E-12/E-17 worked.

**First person in the CV.** `rung`'s Stortinget profile reads "…har jeg erfaring
med selvstendig månedsoppgjør…" — a doctrine violation. All four Relay profiles
are clean.

**Capacity.** CV dynamic words 345–383 against a measured two-page boundary
above 605. Letters 321–362 against a 400 signal. Page overrun risk is low —
though see the caveat in §D.

**A self-weakening fact removed.** `rung`'s EIE letter says the dashboard ran
"til det ble avviklet rundt februar 2026" — the «avviklet» ending tic, and a
volunteered decommissioning. The Relay letter carries the same user-testing
evidence with no such ending.

**The judgment sentences are real.** Norwegian's "Jeg valgte bevisst bort kode i
kjernen som ville gjort controllere avhengige av en utvikler" and Abacus's
rejection of direct allocation are stronger, better-placed reasoning than
anything in the `rung` letters.

## B.3 The regression: adoption and persistence facts went to zero

Present in `rung`, absent from every Relay letter:

- "Verktøyet ble brukt i hele sykehusets budsjettprosess for 2026 og brukes nå i
  prosessen for 2027." (Stortinget, Norwegian, Abacus)
- "Modellen ble ferdigstilt og overlevert til controllerne tidlig i 2026."
  (Norwegian)
- "Kort etter overgangen ble verktøyene brukt relativt ofte av økonomirådgivere
  i flere klinikker." (Abacus, EIE)

These are the sentences that convert *I did work* into *the work was adopted and
is still running*. They are the cheapest credibility a letter can carry, and
they are all in the frozen authority — `Work_experience.md:70`, PRJ-03's digest
row, lists "sykehusdekkende bruk i budsjettprosessene for 2026 og 2027" under
what the claim *can prove*.

This is narrower than "the Relay lost consequence". It did not: Stortinget's
"innen om lag tre måneder hadde jeg overtatt hele den tildelte
månedsoppgjørsflyten" is a consequence, and Stage 3 correctly logged adding it
as a TRUTH repair for understatement. What vanished is specifically the
**adoption/persistence** class.

## B.4 A documented, confirmed differentiator was dropped

`authorities/Work_experience.md:70`, PRJ-03 digest row, *can prove* column:

> …i praksis eneste kodende utvikler for kodeendringene, bekreftet 2026-09-06,
> innenfor en bred interessentprosess på ca. 50 personer…

and `Work_experience.md:383`:

> `interview_defensibility` — Principal coding and concrete workflow change are
> clear; I praksis eneste kodende utvikler for 2025-moderniseringen, uttrykkelig
> bekreftet 2026-09-06…

`rung` used it in the Norwegian and Abacus CVs and both letters. The Relay
replaced it everywhere with "Gjennomførte kodeendringene … innenfor en
interessentprosess på om lag 50 personer" — true, in-ceiling, and materially
weaker. The ceiling column (`Ikke opphavsperson eller budsjetteier; ingen
eierskap til hele moderniseringen eller budsjettprosessen; ingen besparelse …
ingen godkjente målinger av effekt`) forbids ownership of the modernisation and
of the budget process, and forbids any effect claim. It does **not** forbid the
sole-coder fact.

So this is not a truth win. It is the same defect class as §B.3: the strongest
item in the *can prove* column did not survive the journey to the letter.

**But restore the scoped form, not `rung`'s.** The authority says «i praksis
eneste kodende utvikler **for kodeendringene**, bekreftet 2026-09-06, innenfor
en bred interessentprosess på ca. 50 personer». `rung`'s CV profile wrote the
bare "Var i praksis eneste kodende utvikler" — dropping both the scope to the
code changes and the stakeholder-process qualifier, which reads as sole
authorship of the modernisation and sits closer to the ceiling than it should.
The right sentence is neither the Relay's hedge nor `rung`'s bare claim: it is
the phrase with its own scope attached.

## B.5 Root cause: the brief protects the limit and paraphrases the asset

`schemas/brief.schema.json`, `units[].properties`:

```
id · refs · proves · employer_problem · ceiling · placement
```

- `ceiling` is required to be **verbatim from the card** — and all four briefs
  comply, quoting exactly.
- `proves` is **free text written by the Architect**.

Norwegian's U2 `proves` reads: *"Gjennomførte kodeendringene i moderniseringen av
et forretningskritisk verktøy innenfor en interessentprosess…"* — which is,
almost word for word, the sentence that ended up in the letter and the CV
profile. The Advocate rendered the brief faithfully. The loss happened one stage
earlier, when the Architect compressed a digest row containing *sole coder*,
*hospital-wide use in 2026 and 2027*, *~80% behaviour-preserving refactor*,
*acceptance criteria and risk register*, *controller onboarding* into a single
hedged clause.

Nothing in the pipeline can recover a fact the brief paraphrased away, because
the Advocate's bundle is scoped to the brief's refs and it has no reason to
suspect the summary is lossy.

**The asymmetry is the bug:** verbatim protection is applied only to the
constraint. The asset gets no such protection.

## B.6 `judgment` is `null` in 4 of 4 briefs

The 0.9.2 finding that motivated the whole keystone/disposition mechanism was
that a polish stage deleted the judgment sentence. The Relay's answer was a
`judgment` atom in the brief plus a keystone disposition in Stage 3.

The disposition half works — 16 dispositions, 12 KEPT, 4 REWORDED, 0 REMOVED,
and all three JUDGMENT keystones kept verbatim. The brief half did not happen at
all: every Architect left `judgment: null`, because the schema allows null and
the playbook calls it "an optional judgment atom".

The judgment arrived anyway, invented at Stage 2 — which is the stage explicitly
told not to re-decide. The strongest content in three of the four letters is
therefore *undecided* content: not chosen by the Architect, not ceiling-checked
against a nominated card at Stage 1, and only caught by Stage 3 after the fact.

## B.7 The new tic class nobody is watching

`signals.TICS` covers eight patterns, all inherited from the `rund`/`runf`
corpus. None of them fires on what the Relay actually produces.

Counted: impersonal sentences of ≥7 words rose from **14** (`rung`) to **27**
(Relay). Classified by reading — and labelled as such, because this half is a
judgment not a regex — the composition inverts:

| | `rung` | Relay |
|---|---|---|
| impersonal sentences carrying a **fact** (adoption, employer fact, artefact description) | ~12 | ~15 |
| impersonal sentences carrying a **principle** | ~2 | **~12** |

Examples of the principle class, all Relay:

- "En annen foretrukket løsning fritar ikke for å gjøre den valgte løsningen etterprøvbar."
- "En oppgaveliste alene viser ikke hvem som må bidra, eller hva som må avklares før neste steg."
- "En som skal vedlikeholde en modell, trenger noe annet enn en som skal bruke svaret i sitt daglige arbeid."
- "En ny mulighet må kunne beskrives som en konkret oppgave brukeren kan utføre og kontrollere."
- "Å gjøre usikkerheten synlig er en del av rådet…"

Each is good on its own. Two to four per letter, and twelve across a cluster of
four, is a voice signature — the writer stepping out of the account to tell the
reader what to conclude. FORFATTERSTEMME already names this under
self-presentation; Stage 3 caught exactly one instance (Norwegian's closing
lesson sentence) and left the rest.

A related uniformity: the antithesis construction (`fremfor` / `ikke bare` /
`i stedet for`) appears 3 times in the Relay letters and **0** times in `rung`.
Small, but it is the same voice tell surfacing a second way.

`register.md` cannot catch either, because it tracks **moves** and the first and
last sentence — one level coarser than sentence architecture.

## B.8 The evidence funnel is narrowing, not enriching

| Stage | refs available / used |
|---|---|
| Scout core | ≤12 per job |
| Brief (units + reserve + stances + facets + plan + outside_scout_refs) | 13–14 |
| Advocate `used_evidence_refs` | **4–7** |
| Advocate `outside_brief_refs` | **0 in all four** |

The Architects did reach — `outside_scout_refs` has 3–4 entries per job, so the
challenger sweep happened. The Advocates did not reach once, and used roughly
a third of what the brief offered. That is consistent with the design ("the
brief is a strong default") but it means retrieval openness is currently
theoretical: the mechanism exists and is unexercised.

Also worth recording: Stage 3's review claims "Brevet bruker evidens utenfor
briefen … deklarert av Stage 2" for Norwegian and Abacus. That is wrong. Those
refs are in the brief's `outside_scout_refs`, and `outside_brief_refs` is empty
in all four advocacy drafts. Minor, but it is a review statement that does not
survive checking.

---

# Part C — job by job

## C.1 Stortinget — strongest structural gain

The `rung` letter was its weakest (76.7): 457 words, four body paragraphs, title
restated in the opening, and a closing carrying **two** tics at once. The Relay
letter opens on the converted employer fact («ivareta og fornye» → new working
methods must be verifiable while operations keep running), chooses the rådgiver
track explicitly in the opening paragraph, and closes on a genuine question
about the department's annual cycle.

Stage 3 earned its keep here: it found that the letter was *understating* —
EV:WORK#012 documents taking over the whole assigned month-close flow in about
three months, and the letter omitted it — and repaired it. That is the exact
behaviour the "understating is also a defect" rule was written for.

Cost: "Verktøyet ble brukt i hele sykehusets budsjettprosess for 2026 og brukes
nå i prosessen for 2027" is gone, and with it the only hard adoption fact the
letter had.

Live limitation: the deadline was 14 September and has passed. Correctly logged
as `known_limitations` rather than forced to CHECK.

## C.2 Norwegian — best opening in the cluster, biggest evidence loss

Opening straight into the sterile-logistics judgment is the strongest single
paragraph the Relay produced: a rejected approach, the reason it was rejected,
the alternative, and a deliberate design constraint (no code in the core, so
controllers stay independent of a developer). No `rung` letter opens on
judgment.

Two costs, both large for this vacancy:
- **«i praksis eneste kodende utvikler» dropped** (§B.4) — for a Senior Manager
  posting where the fit factor is 0.35, the scarce-role signal is precisely what
  execution can contribute.
- **Two adoption facts dropped** — the model handed over to controllers early
  2026, the tool in hospital-wide use for 2026 and 2027.

Also the highest impersonal-sentence count (9) and the highest principle count.

**Delivery differs from `rung`.** The Architect chose LETTER_AND_CV where the
earlier report treated Norwegian as a CV-only instrument ("upload an updated copy
of your CV", `letter_requirement: UNSPECIFIED`, portal route). Defensible — the
ad does not forbid a letter — but it changes the scoring weighting, and it is the
one place where a Relay delivery decision should be reviewed by a human before
sending.

## C.3 EIE — cleanest letter, smallest change

The only job where `rung` was already tic-free in the body, so the Relay's gain
is narrower. It still removes the «søker fordi» + stock-close pair, removes the
volunteered decommissioning, and replaces a generic sign-off with a concrete
NEXT_STEP tied to specific broker enquiries and Brokio.

The PROBLEM opening ("En veiledning hjelper lite hvis brukeren ikke finner
svaret når arbeidet stopper opp") does real work: it states the role's actual
failure mode before any claim about the candidate.

Highest concentration of principle sentences relative to length (4 in 21
sentences) and both antithesis constructions.

The gap handling is right: no real-estate background, named once, argued as the
qualification route rather than apologised for.

## C.4 Abacus — highest expected chance, and the clearest specificity cost

Best structural decision in the cluster: the NAME_ONCE threshold (no BNXT
experience) is moved into the **opening** and converted into the reason for
choosing the rådgiver track over the senior track. `rung` did the same move but
buried it in the closing, behind a title-restating opening.

But this is the highest-fit vacancy (1.10) and the one where domain vocabulary
*is* the qualification signal, and the Relay letter gave some of it away.
`rung`'s body paragraph reads:

> …prosjektnulling, periodisering, reversering, avsetninger, bilagsflyt,
> avstemming og resultatforklaring … prosjektopprettelse, ekstern finansiering,
> fakturering og prosjektavslutning.

The Relay letter compresses this to "sto jeg selv for den tildelte
månedsoppgjørsflyten" and moves the detail to the CV profile. The division of
labour is doctrinally correct — CV gives scope, letter gives choice — but for an
ERP consultancy screening on finance-process vocabulary, that vocabulary in the
letter is not redundancy, it is the proof.

Gained in exchange: the gevinstfordeling judgment, which `rung`'s Abacus letter
did not have at all, and the ISO employer-fact conversion.

---

# Part D — scoring

Rubric, weights, logistic and knock-out multipliers are the earlier report's
§5.1, unchanged. The model reproduces all four `rung` figures to within
rounding, so the deltas are comparable. Sub-scores below are **my judgment**;
they have not been independently re-derived by a second reviewer.

| Job | | CV | Letter | Package | compound | IOI † | fit | expected † |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Stortinget | `rung` | 83.4 | 76.7 | 84.8 | 81.4 | 30.9 | 0.90 | 28.7 |
| | **Relay** | **84.5** | **83.0** | **86.5** | **84.5** | **36.3** | | **33.9** |
| Norwegian | `rung` | 79.5 | *(n/c)* | 80.8 | 79.9 | 28.6 | 0.35 | 12.3 |
| | **Relay** | **81.0** | **83.0** | **82.5** | **82.1** | **32.1** | | **14.2** |
| EIE | `rung` | 82.6 | 81.1 | 84.9 | 82.7 | 33.2 | 0.95 | 32.1 |
| | **Relay** | **84.0** | **84.0** | **86.0** | **84.6** | **36.3** | | **35.2** |
| Abacus | `rung` | 83.3 | 77.5 | 83.8 | 81.3 | 30.9 | 1.10 | 32.9 |
| | **Relay** | **84.0** | **82.0** | **85.0** | **83.6** | **34.6** | | **36.7** |
| **mean** | `rung` | 82.2 | 78.4 | 83.6 | 81.3 | **30.9** | | **26.5** |
| | **Relay** | 83.4 | 83.0 | 85.0 | 83.7 | **34.8** | | **30.0** |

**† Every IOI and expected figure above assumes no knock-out multiplier, and
the Relay packages have not been rendered.** A three-page CV would apply ×0.70
and a two-page letter ×0.75. Read the Relay column as conditional on the render
in Phase 2 of the development plan.

`rung`'s Norwegian was scored as a CV-only instrument (CV .65 / package .35);
the Relay's Norwegian carries a letter, so it is scored .35/.35/.30. Two
consequences for that row: roughly a point of its gain is the instrument change
rather than execution, and `rung`'s Norwegian letter — which scored **83.5**
uncounted — is level with the Relay's 83.0. On execution alone, Norwegian is the
one job where the Relay letter is not an improvement.

**Where the gains come from.** Letters move most (+4.6 mean), which is what the
design predicted: calibration (no tics), architecture (three paragraphs, chosen
moves), conversion (an employer fact converted in every letter) and judgement
all rise. Specificity is the one letter sub-score that **falls**, and it falls
for exactly the reasons in §B.3–B.5.

**Knock-out cues: none identified — but not measured.** No self-disqualification,
no employer-blind letter. CV page count and letter page count were **not
rendered**: Stage 3's polish layer never reached disk in a place `preview` reads,
so its own page figures are from the pre-polish draft. Word counts make two-page
CVs and one-page letters near-certain (345–383 dynamic words against a measured
boundary above 605), but a ×0.70 cue on an unrendered document is not something
to assume away. **Render before sending.**

**Headroom.** Restoring the adoption facts and the sole-coder fact is a
specificity and evidence gain, not a length problem — the letters are 321–362
words against a 400 target, so there is room. Rough estimate: +2 to +3 on
letters, +2 on CVs, worth about **2 further IOI points**, putting the cluster
mean near 37. That is the single highest-value fix available and it is a schema
change plus two playbook lines.

---

# Part E — what to keep

The four design bets that paid, in order of how cleanly they show:

1. **Move selection against a cluster register.** 4/4 distinct openings and
   closings, and the tic classes the previous corpus could not shake went to
   zero. Keep exactly as is.
2. **Layers with declared dispositions.** 16 keystone dispositions, 0 REMOVED,
   all JUDGMENT keystones kept verbatim. The 0.9.2 failure mode did not recur,
   and the change list makes every edit legible with a reason.
3. **Evidence cards carrying ceilings.** Every brief quoted its ceilings
   verbatim and no letter exceeded one. The Relay has no overstatement defects
   at all — which is what makes the *understatement* defect the interesting one.
4. **Measured capacity.** One-line headlines in 4/4 after five of eight failed
   in the previous corpus.

And the one to fix first: the brief carries a verbatim limit and a paraphrased
asset. Make that symmetric and most of Part B's regression goes away.
