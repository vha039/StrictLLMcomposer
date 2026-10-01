> **SUPERSEDED 2026-09-18** by [`CONSOLIDATED_PLAN.md`](CONSOLIDATED_PLAN.md),
> which adjudicates this plan against `reviews/CODEX_DIFF_REVIEW.md`. Several
> items here (F4 `rebind`, F7 `DECISION_FIELDS`, D1-D5, the phase order) were
> rejected on verified premises. Kept for the reasoning trail only — implement
> the consolidated plan.

# Relay — next development plan, with the first-cluster fixes

Companion to [`reviews/FIRST_CLUSTER_ANALYSIS.md`](../reviews/FIRST_CLUSTER_ANALYSIS.md).
Every item below traces to something measured there; no item is speculative
hardening.

**Standing constraints, unchanged.** Nothing touches `P0.9\Build`. No QA
frameworks, test suites, generic preflight or compatibility layers — checks
below are intrinsic to the mechanism they belong to. Stages stay separate,
human-started sessions. Superseded files move to `archive_0.9.3\`.

**One theme runs through the whole plan.** The pipeline is careful about limits
and careless about assets. It protects `ceiling` verbatim and lets `proves`
be a paraphrase; it hard-gates publish and leaves decline ungated; it refuses
loudly when facts move and says nothing when a submit destroys four finished
letters. Phase 1 fixes the gate asymmetry, Phase 3 the evidence asymmetry.

---

## Phase 1 — harness (≈2 h)

### F1 · Let Stage 3 decline · **critical** · `cli.py`

Read `--reject` before the currency check, and gate the two paths differently:

```python
reject = bool(getattr(args, "reject", False))
required = pipeline.STAGES[stage].requires
if stage == 3 and reject:
    blocking = [n for n in required if state.loaded.get(n) is None]   # existence only
else:
    blocking = [n for n in required if not state.current(n)]
```

A rejection is a statement *about* a layer; it cannot require that layer to be
in good standing. The review still binds through `pipeline.upstream_hashes`, so
it records exactly which advocacy layer was declined and at what evidence state.

Add `--file` resolution for the reject path (write set is `("review",)` alone,
so the existing single-artifact `--file` branch already applies) — this makes a
decline possible even with no bundle on disk.

**One consequence to close at the same time.** The reject path calls
`artifacts.discard` on `polish` and `final_package`. `discard` is a no-op on a
missing file, so today it is harmless — the only way to reach reject is before
anything published. Relaxing the gate makes a second route reachable: a job
that published and *then* went stale could be rejected, silently moving a
published final into `history/`. Refuse `--reject` when a current
`final_package` exists, naming it:

```
[REFUSED] this job has a published final_package. A rejection would withdraw it.
          Re-run Stage 3 to replace it, or rebind if only the binding moved.
```

### F2 · `context` issues a bundle on stale upstream, with the diff · `cli.py`

Refuse only when a required artifact is **missing**. When one is stale, issue
the bundle and put the staleness in it:

```json
"upstream_state": {
  "advocacy_draft": {"state": "STALE",
                     "reason": "brief: 4 non-decision fields changed",
                     "changed_fields": ["units[].employer_problem", "notes", "traps", "reserve"]}
},
"write": {"allowed": ["review"], "blocked": {"polish": "upstream is stale; rebind or re-run Stage 2"}}
```

The stage then makes the judgment the Stage 3 session made by hand and got
right. Publishing a package built on a superseded layer stays blocked; reading,
editing and declining do not.

### F3 · `artifact_hash` excludes `binding` · `artifacts.py:38`

```python
SEMANTIC_EXCLUDED = ("binding", "artifact_role")
def artifact_hash(payload):
    skip = set(SEMANTIC_EXCLUDED)
    if payload.get("artifact_role") == "CURRENT_SEMANTIC_PACKAGE":
        skip.add("finalization")
    return sha256_canonical_json({k: v for k, v in payload.items() if k not in skip})
```

Identity becomes what the stage actually wrote. A sibling re-submitted unchanged
stops cascading (`brief`+`cv_draft` and `polish`+`review` are both sibling
pairs, so this is a live hazard, not a hypothetical).

**Migration cost, stated plainly:** this changes every stored
`evidence_fingerprint` whose upstream is non-empty — `brief`, `cv_draft`,
`advocacy_draft` and below all go stale once. `scout` is unaffected (no
inputs). F4 is the migration, so land F3 and F4 together and sweep once.

### F4 · `jobbsok rebind` — the missing cheap verb · new, small · `artifacts.py` + `cli.py`

```
jobbsok rebind --run R --job J --artifact advocacy_draft --reason "..."
jobbsok rebind --run R --all --reason "artifact_hash definition changed"
```

Re-stamps an existing artifact's binding to current upstream without touching a
single semantic field, and records the assertion in the binding:

```json
"rebound": {"from": "c6c908b0", "to": "0a09581d",
            "at": "2026-09-17T…Z", "reason": "brief compaction, no decision field moved"}
```

This is the action the Stage 3 session correctly identified and could not
perform. Three intrinsic properties make it safe enough for this tree:

- it **cannot** alter semantic content — it writes only `binding`;
- it **requires** a reason, so equivalence is always *asserted by someone*,
  never inferred by the tool (D02's "re-stamping never establishes
  equivalence" holds — it establishes a *declared, attributed* equivalence);
- the previous fingerprint stays in the record, so the chain is reconstructible.

Answers H5 and H7 at once, and gives `branch` a third option besides reuse and
drop.

### F5 · Submit says what it will invalidate · `cli.py`

Before writing, list existing artifacts owned by stages **below** the one being
submitted whose fingerprint the write will change:

```
[WARN] this submit will stale: advocacy_draft (Stage 2)
       downstream work exists for this job; finish the stage before revising
```

Not a gate. Record the same list as `superseded_downstream` in the new
artifact's binding, so a run can later explain why its letters went stale.
This is the single cheapest fix for what actually happened on 16 September.

### F6 · `preview` and `register` report state instead of ignoring it

One banner line in `preview`, and a `stale` column in `register.md`. `register`
is the only cross-job differentiation check there is; it must not silently
present superseded text as the cluster's variation baseline.

### F7 · Staleness names the *kind* of change · `pipeline.py` + `artifacts.py`

Declare per artifact in the registry which fields are decisions:

```python
DECISION_FIELDS = {
  "brief": ("position", "delivery", "units[].refs", "units[].ceiling",
            "units[].placement", "judgment", "stances", "distinctiveness",
            "employer_fact", "letter_plan.paragraphs[].unit_ids"),
  ...
}
```

`_stale_reason` then emits `brief: 4 non-decision fields changed (notes, traps,
reserve, units[].employer_problem)` instead of `upstream changed: brief,
cv_draft`, and `status.recommended_action` routes to `rebind` rather than
"Run Stage 2 (ADVOCATE)". The registry already owns artifact shape, so this
lives where it belongs.

---

## Phase 2 — recover the `rung` cluster (≈20 min, no model sessions)

The four Stage 3 layers are complete, schema-valid and sitting at
`generated/returns/r20260916-184816-a1ea76/<job>/stage3/<old fp8>/`. Nothing in
them is invalidated — `_read_return` resolves by path and `stamp` rebuilds the
binding from the live context.

```powershell
# 1. one sweep after F3+F4
.\.venv\Scripts\jobbsok.exe rebind --run r20260916-184816-a1ea76 --all `
    --reason "artifact_hash now excludes binding; brief compaction moved no decision field"

# 2. per job: new bundle, move the finished returns into its fp8 dir, submit
.\.venv\Scripts\jobbsok.exe context --run r20260916-184816-a1ea76 --job <JOB> --stage 3
#    copy polish.semantic.json + review.semantic.json from the old fp8 dir
.\.venv\Scripts\jobbsok.exe stage-submit --run r20260916-184816-a1ea76 --job <JOB> `
    --stage 3 --fingerprint <NEW fp8> --finalize-render
```

Then **render and read the page counts** — §D of the analysis flags this as the
one unverified knock-out cue. Stage 3's own page figures came from the
pre-polish draft.

Two things to check on the rendered output before anything is sent:

- Stortinget's deadline (14 September) has passed. Vegard's call.
- Norwegian was delivered as LETTER_AND_CV where the earlier corpus treated it
  as a CV-only instrument. Worth one look at the ad before submitting.

Do Phase 2 **before** Phase 3: Phase 3 changes `brief.schema.json`, which makes
the four existing briefs invalid and would force a Stage 1 re-run.

---

## Phase 3 — close the evidence leak (≈1.5 h)

This is where the return is. §B.3–B.5 of the analysis measured 11 adoption
facts going to zero and a confirmed differentiator disappearing, and traced both
to one schema shape.

### D1 · `brief.units` gains `evidence_quote[1..3]` — verbatim · `schemas/brief.schema.json`

Symmetric with `ceiling`. Each unit must quote, word for word from a card it
references, the specific fact the unit rides on — not the Architect's summary
of it. `proves` stays as the abstraction that drives the argument; the quote is
what the Advocate is allowed to build sentences from.

Intrinsic check, using machinery that already exists: `validate.py` resolves
every `EV:` ref and can therefore fetch the card text. Assert the quote is a
substring of one referenced card. No matcher, no fuzzy logic — exact or refused.

This alone would have kept «i praksis eneste kodende utvikler», because it is a
phrase in PRJ-03's *can prove* column and the Architect would have had to look
at that column to fill the field.

The substring check also enforces the right *scope*. The authority's phrase is
«i praksis eneste kodende utvikler **for kodeendringene**, bekreftet 2026-09-06,
innenfor en bred interessentprosess på ca. 50 personer». `rung` wrote the bare
"Var i praksis eneste kodende utvikler", dropping the scope — which reads as
sole authorship of the modernisation and sits closer to the ceiling than it
should. An exact-substring rule accepts the scoped phrase and refuses the
truncation, which is precisely the discrimination this field exists to make.

### D2 · `brief.units` gains `outcome` — required key, nullable value

```json
"outcome": {"fact": "sykehusdekkende bruk i budsjettprosessene for 2026 og 2027",
            "ref": "EV:WORK#022-4-3-prj-03-modernisering-og-nyutvikling"}
```
or explicitly `"outcome": null`.

Required-but-nullable is the whole point: the Architect must *look at* the
adoption column and record that there is nothing there, rather than omitting the
question. §B.6 is the evidence that optional high-value fields get 0% uptake.

### D3 · `judgment` becomes required, with `judgment_absent_reason`

Same device. `judgment: null` stays legal, but only alongside a sentence saying
why this vacancy has no judgment worth leading with. Four of four Architects
skipped it and the Advocate invented one anyway — at the stage explicitly told
not to decide.

### D4 · `letter_plan.paragraphs[]` gains `carries[]`

Enum: `DECISION` · `ACTION` · `OUTCOME` · `EMPLOYER_LINK` · `GAP_TURN`.
When any unit has a non-null `outcome`, at least one paragraph must carry
`OUTCOME`. This turns §B.3 from an editorial hope into a plan the Advocate
receives.

### D5 · One signal, not a detector · `signals.py` + `preview`

Add `impersonal_sentences: N of M` to what `preview` prints — sentences of ≥7
words with no first-person pronoun. A **count**, reported like word count and
pages, in line with "counts and pages are editorial signals only". No boolean
tic, no threshold in code, no classifier: the Relay wrote 27 of these against
`rung`'s 14 and nobody saw it, which is a visibility problem, not a rules
problem.

Add the antithesis count (`fremfor` / `ikke bare` / `i stedet for`) to
`register`'s cluster tic counts — same tuple, same mechanism, one more row.

### D6 · Stage 2 playbook

- Write from `evidence_quote`, not from `proves`. `proves` tells you what the
  unit is for; the quote is the material.
- When a unit carries an `outcome`, the letter says what happened to the work —
  who took it up, whether it is still running. One sentence.
- Domain vocabulary belongs in the **letter** as well as the CV when the
  vacancy screens on it. The Abacus letter moved «prosjektnulling, periodisering,
  reversering, avsetninger, bilagsflyt» into the CV profile and lost the
  strongest qualification signal it had on the highest-fit vacancy in the
  cluster. Division of labour is about *argument*, not about vocabulary.
- Restore a quoted fact **with the scope the authority gives it**. «i praksis
  eneste kodende utvikler for kodeendringene … innenfor en bred
  interessentprosess» is the sentence; the bare "eneste kodende utvikler" is
  not, and neither is the Relay's hedge that drops the fact entirely.

### D7 · Stage 3 playbook

- Truth pass, understatement direction: if the brief carries an `outcome` and
  the letter does not, that is a defect. It is the same class as the Stortinget
  repair Stage 3 already made correctly.
- Screen-out pass: read the `impersonal_sentences` count, then read the
  sentences it counted. The count is deliberately crude — it catches legitimate
  employer-fact sentences («Abacus er ISO-sertifisert…») alongside the ones that
  matter. What you are looking for is the writer stepping out of the account to
  tell the reader what to conclude; FORFATTERSTEMME already names it under
  self-presentation, and the first cluster carried about twelve of them against
  `rung`'s two. Judge them; no threshold is set in code, because the number
  `preview` prints is not the quantity the rule is about.

### D8 · Stage 1 prompt and playbook — one paragraph

> A submitted brief is upstream of finished work. Do the cluster-level
> tightening pass **before** you submit, not after the register view at the end
> of the cluster. If you must revise a submitted brief, say so in the session
> report so the operator knows what it invalidated.

With F5's warning line, this closes the 16 September sequencing failure from
both ends: the playbook says don't, and the tool says what it costs.

**Re-freeze after Phase 3** — playbooks are frozen into runs.

---

## Phase 4 — the real test

Run the `runf` cluster (Tieto, BearingPoint, Amesto, Visma) end to end with
Phase 1 and Phase 3 in place. It is the better test than repeating `rung`:

- three of its four CVs ran to **three pages** in the old corpus, so it exercises
  capacity where capacity actually failed;
- Visma is a genuine CV-only instrument («Vi krever selvfølgelig ikke
  søknadsbrev» plus application questions), so it is the first real exercise of
  `CV_ONLY` / `CV_PLUS_FORM_ANSWERS` and of D04's bet that Stage 2 earns its keep
  when the CV carries the whole argument;
- it is the cluster where the previous harness's best model pairing (Opus+Opus)
  produced its wordiest output, so a length comparison means something.

Then score all three corpora on the same rubric and read three numbers:

| Question | Metric |
|---|---|
| Did the evidence leak close? | adoption facts per letter, `rung` 11 → Relay 0 → ? |
| Did the voice tell come down? | impersonal sentences, 14 → 27 → ? |
| Did the variation win hold on a second cluster? | distinct opening/closing moves, 4/4 |

---

## Ordering, and why

```
F3+F4 ──► one rebind sweep ──► Phase 2 (finish rung, render, read pages)
F1,F2,F5,F6,F7 ──┘                        │
                                          ▼
                              Phase 3 (schema + playbooks) ──► re-freeze ──► Phase 4 (runf)
```

Phase 3 invalidates the four existing briefs, so the `rung` cluster must be
finished and rendered first. Phase 1 is a prerequisite for Phase 2 because
without F4 there is no way to move those four letters forward except paying for
four fresh Stage 2 sessions.

## Deliberately not doing

| Rejected | Why |
|---|---|
| A sentence-architecture analyzer | A new QA layer. D5's count is one more number next to word count, in a tuple that already exists. |
| A hard cap on impersonal sentences | The stage should decide with the number in front of it, as with pages and words. |
| Auto-rebind when only non-decision fields moved | Equivalence must be asserted by someone. F4 requires a reason; the tool never infers one. |
| A lock or scheduler preventing out-of-order stages | Stages are human-started by design. F5's warning plus D8's paragraph is the right weight. |
| Re-running `rung` from Stage 0 | The four packages are good and nearly finished; the open questions are answered better by `runf`. |

## Open, carried forward

- Leftover `Soknad_*` files after a CV-only republish (from `HANDOVER.md`).
- CLM-BAR-004 — still Vegard's call.
- `branch --refresh-inputs` drop path still unexercised against a real fact
  change; F4 gives it a third option worth adding when it is next touched.
