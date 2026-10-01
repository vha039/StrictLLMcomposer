# 01 — Change architecture specification

**Status:** planning material. Not authority.
**Verdict: no normative architecture amendment is required for any change in this pass.**

This file diffs the proposed target state against the frozen P0.9 architecture, classifies every
change, and gives the positive argument for the no-amendment conclusion — including the one place
where the first draft of that argument was wrong and had to be rebuilt (§5).

Governing documents: `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` (`FROZEN_NORMATIVE`,
rev `0.9.0`) and `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`. Neither is edited.

---

## 1. Classification of every change

Spec §22.3 requires an amendment only when a **frozen rule** changes. Gate results and
implementation-default tuning do not. Each change below is classified into one of the six categories
the governing instructions require.

| ID | Change | Classification |
|---|---|---|
| A1 | Typography table in `prepare_masters`, applied to both masters | template/configuration change |
| A2 | `styles.xml Normal` (both), `ListBullet`/`Heading1` (CV) | template/configuration change |
| A3 | `WRITING_DOCTRINE § Myke redaksjonelle utgangspunkt` — compression, not shrinking | policy/writing-doctrine refinement |
| A4 | Page targets unchanged | no change |
| A5 | Spacing deliberately unchanged | no change |
| B1 | Stage 1 pointer from `motivation_bridge` to existing `Begrunnet motivasjon` | stage-responsibility clarification |
| B2 | Stage 3 named-section salience and cross-section precedence | stage-responsibility clarification |
| B3 | Stage 1 `structure_guidance` anti-template sentence | stage-responsibility clarification |
| C1 | `TOO_WEAK` — concise provenance-voice clarification | policy/writing-doctrine refinement |
| C2 | Stage 1 routing to `TOO_WEAK`; Stage 3 symmetric repair duty | stage-responsibility clarification |
| D1 | Em dash removed from `render.py:179` | implementation-only correction |
| D2 | En dashes removed from `docProps` metadata | implementation-only correction |
| D3 | `CV_BASELINE.md` dash normalisation + regenerated map | human source maintenance of a protected input |
| D4 | Master static furniture + `leakage.KNOWN_GOOD_PHRASES` | template/configuration change |
| D5 | `WRITING_DOCTRINE § Tegnsetting` | policy/writing-doctrine refinement |
| E1 | `policy/writing/FORFATTERSTEMME.md` | **context/frozen-input addition** |
| E2 | Stage 2 boundary sentence; Stage 3 ownership and anti-anchoring instructions | stage-responsibility clarification |
| F1 | Inheritance-preserving render transaction beside the output destination | implementation-only correction |
| F2 | Fixture-owned role mapping in two tests | test-only correction |

No change falls into the sixth category, *actual normative architecture amendment*.

---

## 2. A — typography and layout

### 2.1 Why this is builder freedom, not an amendment

Spec §22.2 enumerates what the Step-2 builder MAY choose, and the list includes verbatim:

> template layout changes proven by target-machine gates

Contract §21 repeats it as *"template tag names and placement after gates"*. The relevant gates are
`GATE-05` (fonts, glyphs and representative layout) and `GATE-06` (parseability and identity/contact
placement); both are re-discharged by the Run A1 render and the human visual review.

`DEC-24` (Spec §12.5) already governs the substance and is untouched:

> Page count, paragraph count and typography are normally review/editorial signals. A document fails
> mechanically only when unusable, corrupted, clipped beyond acceptable use or subject to a true
> explicit external constraint. P0.9 MUST NOT delete decision-relevant content merely to satisfy an
> inherited proxy page rule.

A3's doctrine paragraph is a refinement **inside** that rule, not a replacement of it: it says the
page target is met by editorial compression, and it draws the distinction the first draft of this plan
got wrong — **per-document shrinking is prohibited; canonical template design is legitimate.**

### 2.2 What is deliberately not changed

- No hard page, bullet, competency or paragraph limit (`DEC-24`, `DEC-33`, Contract §22).
- No deterministic truncation or auto-fit.
- `cv_expected_max_pages` / `letter_expected_max_pages` stay at 2 / 1 — they are advisory and become
  useful for the first time once a real page count exists (F12).
- `template_map.json` is untouched; typography stays in the master, not in the render path.
- The 17 CV / 7 letter control contract is preserved and machine-verified before any write.

### 2.3 Frozen-run semantics

Existing runs are governed by their own frozen manifest. `render_job` raises `ConfigurationError` if a
live master's hash differs from the frozen record, so **the pilot run cannot be re-rendered with the
new masters, by design**. This is correct provenance behaviour and is why verification requires new
runs (`02_…md` §9). The pilot run and its artifacts are preserved unchanged.

---

## 3. B and C — writing doctrine and persuasion calibration

Spec §4.5:

> Writing guidance, persuasion calibration and personality are interpretive or advisory. They may
> guide selection and expression but MUST NOT establish candidate facts, formal roles, achievements,
> results, dates, metrics or claim ceilings.

Every B and C change stays inside that sentence. Nothing creates a candidate fact; nothing moves a
claim ceiling. Outcome B adds **no new doctrine at all**: the canonical Norwegian source already
covers it, so only routing and salience change. C1 clarifies how to transpose source provenance into
first-person candidate prose while preserving every real qualification.

Other frozen rules checked and untouched:

- `INV-03` — the three factual authorities remain the only source of candidate facts. **The
  authorities themselves are not edited**; ISS-06 is fixed by teaching the reader how to transpose a
  source's provenance wording, not by rewriting the source.
- `DEC-31` (Spec §9, doctrine §Mål og myndighet) — no stage reopens apply/no-apply, computes a fit
  score, or produces GO/NO-GO. Nothing here touches that.
- `INV-07` / Spec §10.3 — generic style phrases must never fail deterministic validation. D5 and E1
  both carry that sentence explicitly, and no new validator or render warning is introduced.
- Spec §9.3 minimum semantic surfaces and `strategy.schema.json` — unchanged. B1/B3 change what Stage 1
  is told about two existing fields; it does not add, remove or retype a field.
- Spec §13.2 Stage-3 elasticity — unchanged. C2 makes an existing repair duty symmetric; it does not
  constrain reconstruction.

### 3.1 The one thing that would have been an amendment, and was rejected

A **categorical prohibition** on mission and societal-purpose language in employer-facing text would
have been a new normative constraint on the letter contract (Spec §12.4). It was rejected on evidence,
not to avoid the word "amendment": Avinor's societal framing is a legitimate operating-environment
motivation and the categorical rule would have destroyed it (`04_…md` §3.1a). The existing doctrine
already supplies the right distinction. B1 makes Stage 1 apply it to `motivation_bridge`; B2 makes
Stage 3 apply it before triage and prevents language rejected by that canonical section from being
reused as swap-test pass evidence. Neither adds a second rule.

---

## 4. D — punctuation

- **D1 and D2** are implementation-only corrections to deterministic code. No validator, normalizer,
  warning channel or state change is added; `DEC-41` and the three orthogonal axes (Spec §7.5,
  `DEC-42`) are untouched.
- **D3** is human source maintenance of a protected input. `AGENTS.md` grants it explicitly:
  *"Explicit human-invoked source-maintenance tooling may still update its maintained targets between
  runs."* `DEC-23` baseline ownership is preserved — the human edits `CV_BASELINE.md`, no stage does,
  and `jobbsok index` regenerates the map deterministically. Formal employers, titles, units, periods,
  order, education, contact and languages are unchanged in substance; only the dash glyph changes,
  plus two unit names where a comma replaces an apposition dash.
- **D4** is a template/configuration change under §22.2, carried by the same auditable tool as A1.
- **D5** is a doctrine refinement, explicitly marked as semantic guidance that must never fail
  deterministic validation.

Verified: no JSON-schema `pattern` and no runtime regex depends on the en dash. `status.schema.json`
and `render_report.schema.json` are not touched.

---

## 5. E — the professional-voice file · the argument rebuilt

This is the only change that adds a frozen input, and the first version of its justification was
wrong. The correction is recorded rather than quietly replaced.

### 5.1 What the first draft claimed, and why it was false

The first draft asserted that Stage 3 owns voice and **Stage 2 is not affected**. That is false.
`cmd_context` builds `read.writing_policy` unconditionally for every stage:

```python
"writing_policy": [
    str(frozen_path(layout, run_id, record))
    for record in read_frozen(layout, manifest, "writing_policy")
],
```

and `manifest.stage_policy_sha256` folds every writing-policy record into the digest for **all three**
stages. A file placed in `policy/writing/` reaches Stage 2 whether or not its instruction names it.

### 5.2 What settles the placement

`branch.CONTENT_GOVERNING` — the table that decides when a child run may rebind an artifact — already
declares `("writing_policy",)` content-governing for **`strategy`, `draft_package`, `final_package`
and `review`**. The architecture has therefore already decided that every `policy/writing/*.md` file
governs Stage 2's content. Placing a voice file there is consistent with a deliberate existing
declaration, not a side effect of a glob.

The alternative — `context/FORFATTERSTEMME.md` as a new frozen-input key routed only to Stages 1 and
3 — is **worse, not merely costlier**. It would create an artifact that governs Stage 3's content but
is absent from `CONTENT_GOVERNING`, so a child-run rebind could silently reuse a `final_package`
produced under a different voice file. That trades an integrity property for a routing preference.

### 5.3 Zero-plumbing properties of the chosen placement

`manifest.py:221` freezes writing policy by globbing:

```python
"writing_policy": [
    _frozen_file(layout, path) for path in sorted(writing_dir.glob("*.md"))
],
```

and `manifest.schema.json` declares it `{"type": "array", "minItems": 1, "items": {"$ref":
"#/$defs/frozenFile"}}` — no enumeration, no `maxItems`. A third file is therefore automatically
frozen, hashed, copied into `runs/<run>/frozen/policy/writing/`, folded into `stage_policy_sha256` and
exposed through `read.writing_policy`, with **no code, no schema and no manifest change**. Grep
confirms zero test coupling to the file count or to `stage_policy_sha256` values.

### 5.4 Why it does not touch the personality interface

Spec §22.1 freezes the *"personality ON/0–3 interface"*. Spec §10.2 requires that Stage 2 receive only
distilled selected guidance and that Stage 3 receive the distilled guidance rather than the full
profile by default. Contract §12 requires distilled-only handoff and prohibits *"full-profile
injection into every stage by default"*; Contract §22 prohibits *"personality OFF/stub default, trait
scoring or full-profile repeated injection"*.

`FORFATTERSTEMME.md` is outside all of that because it is not the personality profile and contains
none of its machinery:

| Personality interface | `FORFATTERSTEMME.md` |
|---|---|
| facets `PF-01`…`PF-20`, selected 0–3 by Stage 1 | **none** — no facets, no facet IDs |
| typology (MBTI, DISC, Big Five, Enneagram, RIASEC) | **none** |
| trait claims, calibration vectors, failure modes | **none** |
| misread controls, anti-inference index | **none** |
| per-vacancy selection and evidence binding | **none** — it is candidate-invariant and vacancy-independent |
| interpretive data plane (`context/`) | control plane (`policy/`), per Contract §3 |

Contract §3 defines `policy/` as *"settings, **writing/persuasion rules** and stage instructions
(control plane)"*. A candidate-owned expression rule set is a writing rule. `PERSUASION_CALIBRATION.md`
is already a candidate-owned file in that directory (`owner: Vegard Håland`), so the precedent exists.

The personality mechanism is unchanged in every respect: Stage 1 still selects 0–3 evidence-bound
facets, zero remains valid, Stage 2 still receives only distilled guidance, Stage 3 may still suppress
every facet, and no facet or typology label may reach employer-facing text.

### 5.5 The stage-responsibility statement, made explicit

Because the routing is what it is, the design must say what each stage does with the file rather than
pretend one of them does not see it:

| Stage | Relationship |
|---|---|
| **Stage 3** | primary author and accountable owner; applies it after factual and strategic grounding; it can never change a proposition, ceiling, lifecycle state, qualification or evidence selection |
| **Stage 1** | non-consumer. The file is present in `read.writing_policy` because routing is collection-wide, but Stage 1's named-section map does not point to it; strategy and motivation remain governed by the existing doctrine and evidence. |
| **Stage 2** | light prior for natural Bokmål; must not trade completeness, strategy execution or factual precision for voice |

This is a **stage-responsibility clarification**, recorded here and in the three instructions. It is
not an amendment: no frozen rule assigns or withholds writing-policy exposure by stage, and the
existing exposure is universal by construction.

### 5.6 Anti-goals, checked

| Anti-goal | Status |
|---|---|
| new semantic Stage 4 for voice | not proposed |
| numeric "sounds like Vegard" score | not proposed; Spec §13.4 and Contract §22 forbid it and nothing here adds one |
| generic deterministic humanizer | not proposed; no code touches semantic text |
| personality cosplay | `§ Anti-karikatur` addresses it directly; employer persuasion outranks visible personality |
| new factual claims from personality | frontmatter sets all four authority flags `false`; `§ Rangorden` states it |
| dynamic per-vacancy personality facts | the file is candidate-invariant and static |
| architecture/state expansion for style | zero schema, zero state, zero command, zero new artifact |

---

## 6. F — mechanical corrections

**F1** increases conformance with the frozen text rather than deviating from it. `DEC-21` (Spec §16.2)
enumerates the ten render steps, and step 6 reads:

> 6. write to a temporary **job** path;

The current implementation writes to a `tempfile.mkdtemp()` workspace under `%TEMP%`. Python 3.14.3
creates that directory with Windows mode `0o700`, producing the protected creator-only DACL observed
on the pilot DOCX. Merely changing its parent would therefore **not** fix the defect. F1 adds an
opt-in inheritance-preserving creation path to `TransactionDir` and uses it only for the
employer-facing render workspace, placed directly under `out_dir`. Rollback workspaces keep the
private default. Containment (Spec §17.2, Contract §15) is preserved; atomic promotion (Spec §5.6,
`GATE-08`) is strengthened because staging is beside the destination and same-volume by construction.

**F2** is test-only. It restores the standing rule that no test may depend on a production
configuration value the human must change, and it does so by giving the tests ownership of their
fixture rather than by deleting an assertion.

---

## 7. Frozen-run and backward-compatibility semantics

| Question | Answer |
|---|---|
| Are existing runs affected? | No. Spec §22.3: *"Existing frozen runs remain governed by their frozen specification and manifest."* The pilot keeps its frozen policy, masters and baseline map. |
| Can the pilot be re-rendered with the new masters? | **No, by design.** `render_job` verifies the live master against the frozen record and raises `ConfigurationError` on mismatch. Verification uses new runs. |
| Does `SPEC_REVISION` / `SCHEMA_REVISION` change? | No. Both stay `0.9.0`, hard-pinned by `manifest.schema.json` as `"const": "0.9.0"` (F14). No schema is edited. |
| Does the package version change? | Yes, `pyproject.toml` and the changed control-plane frontmatter go to `0.9.2`. That is implementation versioning, which P0.9.1 already established as distinct from spec revision. |
| Does adding a writing-policy file invalidate anything? | No. `stage_policy_sha256` changes for **future** runs only; the handoff digest is computed per run. Existing handoffs and receipts are unaffected. |
| Is a migration or compatibility shim needed? | No. None is proposed, and Contract §22 prohibits building one. |
| Does `branch` still work? | Yes. `CONTENT_GOVERNING` already lists `("writing_policy",)` for all four artifacts, so a child run of a *new* parent correctly refuses to rebind an artifact across a voice-file change. |

---

## 8. Explicit statement for each change: why no amendment

Required by the governing instructions — *"If no architecture amendment is necessary for a change, say
so explicitly and explain why."*

| Change | No amendment because |
|---|---|
| A1, A2, D4 | §22.2 grants template layout changes proven by target-machine gates; `DEC-24` already treats typography as an editorial signal; the control contract and parseability outcome are preserved and re-proven. |
| A3, C1, D5 | Spec §4.5 already classes writing guidance as advisory control plane; these refine existing named sections in the canonical Norwegian source and create no new source of truth. |
| B1, B2, B3, C2, E2 | Stage instructions are control-plane documents, not frozen architecture. No stage gains or loses an artifact, an authority or a write permission. `INV-09` stage write ownership is untouched. |
| D1, D2, F1 | Deterministic implementation details. §22.2 and Contract §21 grant module topology and no-clobber UX. F1 increases `DEC-21` conformance without changing promotion semantics. |
| D3 | `AGENTS.md` grants human-invoked source maintenance of protected inputs between runs. `DEC-23` baseline ownership is preserved. |
| E1 | The file is a writing rule in the control plane (Contract §3), not the personality profile; it carries no facets, facet IDs, typology or trait claims, so Spec §10 and Contract §12/§22 are untouched. `frozen_inputs.writing_policy` is an unbounded, globbed array — no schema, code or manifest change. §22.1's frozen personality interface is unchanged. |
| F2 | Tests are not architecture. |

---

## 9. What a hostile reviewer would press on, and the answer

1. *"A candidate-specific voice file is personality by another name, and Stage 2 gets it — that is
   full-profile injection."* — It contains no facets, no typology, no trait claims and no misread
   controls, and it is candidate-invariant rather than vacancy-selected. Contract §22 prohibits
   *full-profile* injection; this is neither the profile nor a distillation of it. The Stage-2
   exposure is pre-declared by `branch.CONTENT_GOVERNING` and is now stated in Stage 2's instruction
   rather than left implicit.
2. *"You edited the masters, and the P0.7 masters were invalid OOXML."* — Which is exactly why the
   edit goes through `prepare_masters`, the tool that repaired them, verifies the control contract
   before writing, and is `--check`-able and idempotent. And the acceptance gate requires **opening
   both files in Word**, not parsing them.
3. *"A leverage floor invites overclaiming."* — The plan does not create a new leverage rubric. C1
   adds one provenance-voice clarification inside existing `TOO_WEAK`; the existing truth ceiling
   remains first, and Run B checks both attenuation and inflation.
4. *"Moving the temp directory is not an ACL fix on Python 3.14."* — Correct; that earlier design was
   rejected. F1 avoids the special `0o700` path only for employer-facing staging, keeps rollback
   staging private, and requires target-machine DACL inspection plus human openability.
5. *"Twenty-one implementation files is not MVP-KISS."* — Every final diff traces to a mandatory
   outcome or a reproduced defect. The byte-identical evidence-index rewrite is explicitly excluded
   from the final diff, and no validator, schema, command or state surface was added. `06_…md` shows
   the trace for each.
