# MASTER RECONCILIATION LEDGER — Claude × Codex × repository

**Status:** provenance and adjudication record. Not authority.
**Sources:** the Claude package (first revision of the eight `0*_….md` files) and the Codex package
(same filenames, current revision).

**Provenance correction.** An earlier version of this line said "both retained unmodified." That is
false: Codex revised the eight files **in place**, so the Claude first revision no longer exists on
disk. Only the Codex revision is retained. Where this ledger cites a "Claude" position, it is citing
this session's reasoning as recorded here and in the plan file, not a recoverable artifact.
**Adjudicator:** the live repository, the frozen architecture and the pilot artifacts. Neither package
wins on authorship or on detail.

Dispositions: `KEEP` (adopt as written) · `MERGE` (combine) · `MODIFY` (adopt with a change) ·
`REPLACE` (one supersedes the other) · `REJECT` · `DEFER`.

---

## 1. The four experiments that decided the material forks

Run against the live repository this turn. Measured output, not paraphrase.

### V1 — `tempfile.mkdtemp` creates a protected DACL · **Codex right, Claude wrong**

Python 3.14.3, Windows, measured by creating directories and reading their DACLs with `icacls`:

| Creation call | Resulting directory DACL |
|---|---|
| `os.mkdir(p)` — no mode | `…-2096395263:(I)(OI)(CI)(M)` · `vhaala\CodexSandboxUsers:(I)(OI)(CI)(M)` · `NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)` · `BUILTIN\Administrators:(I)(OI)(CI)(F)` · **`VHAALA\veggi:(I)(OI)(CI)(F)`** |
| `os.mkdir(p, 0o700)` | `NT AUTHORITY\SYSTEM:(OI)(CI)(F)` · `BUILTIN\Administrators:(OI)(CI)(F)` · `OWNER RIGHTS:(OI)(CI)(F)` — **no `(I)`, no `veggi`** |
| `tempfile.mkdtemp(dir=p)` | identical to the row above |
| `Path.mkdir(mode=0o777)` | inherits normally; `VHAALA\veggi:(I)(F)` present on child files |

And the promotion step end to end — a file `os.replace`d **out of** a `mkdtemp` directory **into** a
normally-inheriting destination:

```
moved.txt   NT AUTHORITY\SYSTEM:(F)
            BUILTIN\Administrators:(F)
            OWNER RIGHTS:(F)
```

No `(I)`, no `veggi`. Byte-for-byte the DACL shape of the four pilot DOCX.

Source confirmation: `tempfile.mkdtemp` calls `_os.mkdir(file, 0o700)` and its docstring states *"The
directory is readable, writable, and searchable only by the creating user."*

**Consequence.** The Claude fix — move `TransactionDir` to the job directory — was **inert**. The
protected descriptor comes from the mode, not the parent. Codex's opt-in inheritance-preserving mode
is correct, and `Path.mkdir(mode=0o777)` is verified as the mechanism.

Secondary consequences: ISS-13's root-cause confidence rises **MODERATE → HIGH** (the whole chain is
now measured, not inferred), and the mechanism is **universal, not sandbox-specific** — it bites
whenever the rendering identity differs from the reading identity.

### V2 — B0-by-copy works, but only for one identity · **Codex right, precondition missing**

```
shutil.copyfile(pilot CV DOCX -> scratch)  as vhaala\veggi
  -> COPY FAILED: PermissionError [Errno 13] Permission denied
```

The pilot outputs grant only `SYSTEM`, `Administrators` and `OWNER RIGHTS`; the owner is
`vhaala\CodexSandboxOnline`. Codex's §3.1 asserts *"the current sandbox owns and can byte-read"* the
files — true for its own session, false for the human and for any other agent. As written, the plan
hard-fails at step 0 under a different operator.

### V3 — Outcome B: the existing doctrine is sufficient · **Codex right, Claude's block was bulk**

`WRITING_DOCTRINE § Begrunnet motivasjon`, current text: motivation must be grounded in *"en konkret
oppgave eller et reelt virksomhetsproblem"*, and the section forbids *"generisk virksomhetsros,
**kopierte verdier**, prestisjemotivasjon, `brenner for` og entusiasme uten substans."*
`§ Arbeidsgiverbyttetesten` closes with *"Ikke reparer med slagord, verdikopiering eller ubegrunnet
virksomhetsros."*

"Kopierte verdier" literally names the Huseierne failure. Claude's proposed *Rangordning av
motivasjonskilder* block restated coverage that exists.

**But one thing is genuinely uncovered**, and it is exactly what happened: the doctrine forbids
*repairing* specificity with mission language; it does not forbid **citing** such language as evidence
that the test was *passed*. Stage 3 did the latter, in `review.reasons[1]`.

### V4 — Outcome C: a general leverage floor already exists · **Codex right**

`WRITING_DOCTRINE § Rolig faglig tyngde`, line 83: *"Jante-kalibrering betyr sterke arbeidsverb og
nøktern selvevaluering. Det betyr ikke svake verb, mange forbehold eller **undersalg**."*

Anti-underselling is already doctrine. Claude's multi-bullet leverage floor was redundant. Only the
**speaker-transposition** case is uncovered.

---

## 2. Atomic dispositions

### 2.1 Root-cause and forensic findings

| # | Item | Claude | Codex | Repo | Disposition |
|---|---|---|---|---|---|
| RC-1 | All 15 frozen inputs byte-identical to live; stale-policy drift ruled out | yes | yes | confirmed by hash | **KEEP** both agree |
| RC-2 | Typography is inline (`w:rPr/w:sz`), not style-driven | yes | yes | confirmed in `docxfill._set_paragraph_text` | **KEEP** |
| RC-3 | Zero en/em dashes in either final package; all page dashes are deterministic | yes | yes | confirmed by grep | **KEEP** |
| RC-4 | ISS-04 — two content zones carry record-title run properties | yes (new) | yes | confirmed in `document.xml` ¶23, ¶31 | **KEEP** |
| RC-5 | ISS-05 escalates Stage 1 → 2 → 3, then is cited as swap-test pass evidence | yes | yes | confirmed verbatim | **KEEP** |
| RC-6 | ISS-06 originates in Stage 1 `evidence_plan[].role`; Stage 3 removed `fortsatt` | yes | yes | confirmed across six artifacts | **KEEP** |
| RC-7 | ISS-13 mechanism | `%TEMP%` DACL inherited (MODERATE) | `mkdtemp(0o700)` + `os.replace` (HIGH) | **V1 confirms Codex** | **REPLACE with Codex**; confidence → HIGH |
| RC-8 | ISS-16 page 2 merged into ISS-01, no separate fix | yes | yes | no page break in master | **KEEP** |
| RC-9 | ISS-14 two tests fail today | yes | yes | confirmed by source inspection | **KEEP** |
| RC-10 | OBS-06 refuted; OBS-03 reclassified | yes | yes | confirmed | **KEEP** |

### 2.2 Outcome A — typography

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| A-1 | Five tiers `{8,10,12,14,24}`, headings at 14 | yes | identical | **KEEP** — Codex adopted it unchanged |
| A-2 | 35-row CV / 8-row letter table, position-keyed and idempotent | yes | identical | **KEEP** |
| A-3 | De-bold exactly ¶23 and ¶31; record lines untouched | yes | identical | **KEEP** |
| A-4 | `styles.xml`: letter `Normal` load-bearing, CV entries defensive | yes | identical | **KEEP** |
| A-5 | Spacing unchanged, `w:line` held in reserve | yes | identical | **KEEP** |
| A-6 | A3 doctrine paragraph | yes | identical | **KEEP** |
| A-7 | CV page criterion | hard "2 pages" | "normally 2; a third accepted only if forcing 2 would reduce employer-facing quality" | **KEEP Codex** — correctly subordinates the page target to `DEC-24` and to the governing tiebreaker |

### 2.3 Outcome B — earned motivation

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| B-1 | Positive motivation hierarchy in the doctrine | add ~20 lines | do not add | **REPLACE with Codex** — V3; restates existing coverage |
| B-2 | Consequentiality test ("purpose is legitimate when it is a causal feature of the work") | add to doctrine | do not add | **REPLACE with Codex** — the discriminator is useful analysis but belongs in the audit, not as new policy; `kopierte verdier` already decides the Huseierne case |
| B-3 | Mission language cannot satisfy the swap test **by itself** | doctrine sentence | Stage-3 instruction sentence | **KEEP Codex placement** — it governs how Stage 3 reasons in its review, which is stage behaviour; Stage 2 does not run the test |
| B-4 | Route `motivation_bridge` → `Begrunnet motivasjon` at Stage 1 | yes | yes | **KEEP** both agree |
| B-5 | `structure_guidance` must not prescribe a default skeleton | yes | identical | **KEEP** |
| B-6 | Avinor's societal paragraph is legitimate and must survive | yes | yes | **KEEP** — both reached this independently; it is the reason B-1/B-2 stay narrow |

### 2.4 Outcome C — truthful leverage

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| C-1 | Multi-bullet leverage floor ("understatement is a defect on the same footing as inflation") | add | do not add | **REPLACE with Codex** — V4; `Rolig faglig tyngde` already forbids `undersalg` |
| C-2 | Provenance-voice rule, semantic not lexical | yes | yes, tighter wording | **KEEP Codex wording** |
| C-3 | Worked `PRJ-04` example with `riktig` / `for svakt` / **`for sterkt`** | yes | dropped | **RESTORE Claude** — see §3.1 |
| C-4 | Route Stage 1 to the leverage sections | `TOO_WEAK` only | `Rolig faglig tyngde` **and** `TOO_WEAK` | **KEEP Codex** — `undersalg` lives in the former |
| C-5 | Stage 3 repair duty made symmetric | yes | identical | **KEEP** |
| C-6 | Do not edit the authority files | yes | yes | **KEEP** — the provenance marker is true and useful *inside* the source |

### 2.5 Outcome D — punctuation

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| D-1 | `render.py:179` em dash → period | yes | identical | **KEEP** |
| D-2 | `render.py:832` metadata dashes → `\|` | yes | identical | **KEEP** |
| D-3 | 16 baseline edits; 4 `authority_anchor` values protected | yes | identical | **KEEP** |
| D-4 | Master furniture + `leakage.py:98`, landing with D3 | yes | identical | **KEEP** |
| D-5 | `Tegnsetting` doctrine section | yes | identical | **KEEP** |
| D-6 | **Advisory render-time dash warning** | add (~8 lines + 1 test) | remove | **REJECT the warning — accept Codex, with a condition** (§3.4) |
| D-7 | Verification of outcome D on *model-generated* prose | via D-6 | **absent** | **MODIFY — close the gap** (§3.4) |

### 2.6 Outcome E — professional voice

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| E-1 | File lives in `policy/writing/`, justified by `branch.CONTENT_GOVERNING` | yes | identical | **KEEP** — the strongest shared argument in either package |
| E-2 | Stage 3 primary owner; Stage 2 light prior, one sentence | yes | identical | **KEEP** |
| E-3 | Stage 3 forms an independent thesis, opening, evidence order and register **before** reading upstream | absent | added | **KEEP Codex — genuinely new signal.** It attacks ISS-09/ISS-10 at the mechanism; Claude treated ISS-09 only through the voice file's anti-pattern list. |
| E-4 | Stage 1 consumes `§ Motivasjonsregister` | yes | non-consumer | **KEEP Codex** — `motivation_bridge` is strategy; the universal doctrine governs it |
| E-5 | `§ Motivasjonsregister` exists in the voice file at all | yes | deleted | **MODIFY — restore, narrowed** (§3.2) |
| E-6 | Anti-pattern list | 4 items | 3 items (dropped two, added a structural one) | **MERGE — 5 items** (§3.3) |
| E-7 | `Sosial temperatur` warmth sentence | absent | added | **KEEP Codex** — useful and evidence-consistent |
| E-8 | `Setningsarkitektur` anti-symmetry line | absent | added | **KEEP Codex** |
| E-9 | Anti-caricature section, channel calibration, stable-author/variable-register | yes | identical | **KEEP** |

### 2.7 Mechanical corrections

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| F-1a | F1 mechanism | move staging to the job dir | opt-in inheritance-preserving `TransactionDir` | **REPLACE with Codex** — V1; Claude's fix was inert |
| F-1b | Staging location | job dir | under `out_dir` | **KEEP Codex** — also guarantees same-volume promotion in `--dest` export mode |
| F-1c | Default stays private (`cli.py:735` rollback) | n/a | yes | **KEEP Codex** — confirmed: two call sites only |
| F-1d | `MAX_PATH_CHARS` constraint noted | yes | yes | **KEEP** |
| F-2 | Fixture-owned role mapping, not assertion deletion | yes | identical, with a more robust section-scoped regex | **KEEP Codex implementation** |

### 2.8 Scope, tests and verification

| # | Item | Claude | Codex | Disposition |
|---|---|---|---|---|
| S-1 | File count | 20 | 21 + `BUILDER_REPORT.md`; adds `atomicio.py`, splits version/ledger | **KEEP Codex** — more accurate |
| S-2 | `evidence_index.json` counted as a diff | yes | no — byte-identical by-product | **KEEP Codex** |
| S-3 | Test count | 6 → 257 | 5 → 256 | **KEEP Codex** — consistent with rejecting D-6 |
| S-4 | `prepare_masters --check` **twice** to prove idempotence | yes | **write, then `--check`** | **KEEP Codex — Claude's instruction was wrong.** `--check` does not write; two dry runs prove nothing. |
| S-5 | Controlled A/B | two replay runs (A0 + A1) | recovered B0 + one A1 | **MODIFY — Codex primary, Claude fallback** (§3.5) |
| S-6 | Replay by semantic-field projection, not artifact copy | yes | identical | **KEEP** |
| S-7 | Run B property-based acceptance, not surface bans | yes | identical | **KEEP** |
| S-8 | Avinor regression guard | yes | yes | **KEEP** |
| S-9 | `VISUAL_HUMAN` / `ACC-18` discharged by the visual A/B | yes | yes | **KEEP** |
| S-10 | ISS-13 acceptance | human open | `Get-Acl` **and** human open | **KEEP Codex** — the dual check catches a partial fix |
| S-11 | Pilot-log rows as a Run B obligation; RUNBOOK line, no tooling | yes | identical | **KEEP** |
| S-12 | Representative-cluster gate and stopping rule | yes | identical | **KEEP** |

### 2.9 Architecture

| # | Item | Disposition |
|---|---|---|
| X-1 | No normative amendment required for any change | **KEEP** — both packages agree; survives reconciliation |
| X-2 | A under Spec §22.2 builder freedom, gated by `GATE-05`/`GATE-06` | **KEEP** |
| X-3 | E1 outside the personality interface (no facets/typology/trait claims) | **KEEP** |
| X-4 | `context/` placement would be an integrity regression (absent from `CONTENT_GOVERNING`) | **KEEP** |
| X-5 | F1 *increases* `DEC-21` step-6 conformance | **KEEP**, with the mechanism corrected per V1 |
| X-6 | Frozen-run semantics: the pilot cannot be re-rendered with new masters, by design | **KEEP** |

---

### 2.10 Issue → disposition index

Every `ISS-*` in the Codex registry, and where its disposition lives above. No issue is dropped.

| Issue | Dispositioned at | Outcome |
|---|---|---|
| ISS-01 CV prose below the readability floor | A-1, A-2, A-4 | KEEP |
| ISS-02 letter at 10.5 pt | A-4 | KEEP |
| ISS-03 half-point and inconsistent sizes | A-1, A-2 | KEEP |
| ISS-04 subordinate zones formatted as titles | RC-4, A-3 | KEEP |
| ISS-05 ceremonial mission motivation | B-1 … B-6 | doctrine untouched; fixed by routing + the Stage-3 sentence |
| ISS-06 provenance frame in first-person prose | C-1 … C-6 | Codex wording + Claude's worked example restored |
| ISS-07 em dash from `render.py:179` | **D-1** | KEEP |
| ISS-08 en dashes in baseline and masters | D-3, D-4 | KEEP |
| ISS-09 consultant-form openings | E-3, E-6 | KEEP Codex's independent-thesis rule + merged anti-patterns |
| ISS-10 letter macro-skeleton | B-5, E-3 | KEEP |
| ISS-11 stock closing and generic contribution sentence | **E-6** | MERGE — both dropped patterns restored (§3.3) |
| ISS-12 clause hyphen in generated prose | D-5, D-7 | KEEP + Run B check |
| ISS-13 outputs unreadable | RC-7, F-1a … F-1d, S-10 | REPLACE with Codex; mechanism corrected by V1 |
| ISS-14 tests coupled to role mapping | RC-9, F-2 | KEEP Codex implementation |
| ISS-15 pilot log never captured | **S-11** | KEEP — RUNBOOK line + Run B obligation, no tooling |
| ISS-16 CV page 2 underutilized | RC-8 | KEEP — merged into ISS-01, no separate fix |

---

## 3. The six modifications — where the master plan differs from Codex

### 3.1 Restore the C1 worked example · `RESTORE Claude`

Codex kept the provenance bullet and dropped the `PRJ-04` example. The example is load-bearing, not
decoration: it pins the exact reproduced defect (`for svakt: var rapportert i bruk`) **and** the
over-correction boundary (`for sterkt: er fortsatt i bruk i dag` — the evidence horizon is ~2.5 years
later, not today).

Codex's own `00_…md` §9 names over-application as open uncertainty #3: *"Stripping a real qualification
would be worse than the understatement being fixed."* Without the example, that risk has no worked
boundary anywhere in the change set. Restored.

### 3.2 Restore `§ Motivasjonsregister`, narrowed · `MODIFY`

Codex deleted it to keep the voice file expression-only and avoid a second motivation source. The
purification instinct is right; the deletion goes one step too far.

Stage 2 and Stage 3 receive only **distilled selected facets**, and Stage 1 may legitimately select
zero. Under Codex's design, when no motivation-related facet is selected, **nothing anywhere tells the
writer what this candidate actually finds motivating** — only what not to write. `Begrunnet motivasjon`
is universal doctrine; it says motivation must come from the work, not what moves *this* person.

Restored as an **expression register** rather than a motive hierarchy, with an explicit subordination
clause (*"Dette er uttrykksveiledning, ikke en konkurrerende motivasjonsregel. Ved tvil gjelder
doktrinen."*). Stage 1 stays a non-consumer, per E-4.

Residual risk accepted: two files now mention motivation. Mitigated by the subordination clause and by
the register being descriptive (which registers read as authentic) rather than normative (what must
ground motivation).

### 3.3 Restore two reproduced anti-patterns · `MERGE`

Codex's list dropped `Jeg ønsker å bidra …` and `Det som særlig motiverer meg, er …` and added a
structural item. Merged: 5 items, Codex's structural item retained as #5.

**Occurrence counts corrected.** An earlier version of this entry said both dropped items are
"reproduced in both final letters." Measured against the two `final_package.json` files:

| Phrase | Huseierne | Avinor |
|---|---|---|
| `Jeg ønsker å bidra` | 1 | 1 |
| `Det som særlig motiverer meg` | 1 | **0** |
| `Jeg ser frem til muligheten til å utdype` | 1 | 1 |

So `Det som særlig motiverer meg` appears **once, in one letter**. It is still worth listing — it is
the Huseierne mission defect verbatim and the pattern generalises — but it is a single observation,
not a cross-job regularity, and the ledger must not claim otherwise. Only
`Jeg ser frem til muligheten til å utdype` and `Jeg ønsker å bidra` are reproduced in both.

All five remain **semantic review cues, never forbidden strings**. Acceptability depends on the
continuation: the generic use is the target, not the words.

### 3.4 ~~Close outcome D's verification hole~~ · **WITHDRAWN — the premise was false**

*Superseded 2026-09-01. Retained because a withdrawn claim is more informative than a deleted one.*

Codex removed the advisory render warning **and** has no punctuation check in Run B. The result: after
D1–D4 fix every deterministic source, and T3 asserts the static side at build time, **nothing verifies
model-generated prose for prohibited punctuation at all.**

The warning itself is correctly rejected — outcome D explicitly says not to assume a validator is
needed, and the pilot shows 0 model-generated dashes across two jobs. But Run B is the only run with
fresh model prose, so it is the only place the risk lives.

Resolution, at **zero code cost**: add to Run B acceptance — *zero `–`/`—` in the extracted text of all
four documents, and no hyphen used as a clause divider*. A1 already carries the dash check for the
deterministic side.

**Why this is withdrawn.** The claim that Codex "has no punctuation check in Run B" is false.
`07_VERIFICATION_ACCEPTANCE_AND_STOPPING_PLAN.md` §5.1 item 6 already reads: *"All Run B
employer-facing text contains zero en dash and zero em dash. Ordinary hyphens remain only where normal
Bokmål calls for them (compounds, dates and ranges), not as clause dividers. This is checked in
extracted output and by reading the sentence in context; no runtime validator is added."*

So there was no hole. The check in `MASTER_VERIFICATION_AND_ACCEPTANCE.md` §5.1 item 5 is **retained
as content** — it is correct and belongs there — but it is Codex's contribution, not a Claude
correction. The rejection of the runtime warning (D-6) stands on its own merits and is unaffected.

### 3.5 B0 precondition gate and A0 fallback · `MODIFY`

Codex's B0-by-copy saves an entire verification run and is the better primary path. But V2 shows it
succeeds only for `vhaala\CodexSandboxOnline`; `shutil.copyfile` as `vhaala\veggi` raises
`PermissionError [Errno 13]`. As written the plan hard-fails at step 0 under a different operator, and
the identity dependency is not stated.

Resolution: keep the copy as primary, gate it on an explicit precondition (all four copy, hashes equal,
**and** `vhaala\veggi` can open the copies), and fall back to Claude's **Run A0** replay — which works
for any identity — when the precondition fails. Strictly better than either package alone.

### 3.6 Sharpen the F1 specification with measured evidence · `MODIFY`

Codex's F1 is correct but argues from Python source reading. The master plan records the **measured**
three-row DACL table, the `os.replace` propagation result, and the verification that
`Path.mkdir(mode=0o777)` restores inheritance. It also states the mechanism as **universal rather than
sandbox-specific**, which Codex's framing understates: any renderer whose identity differs from the
reader's produces this, on any machine.

---

## 4. Rejected alternatives — preserved from both packages

Nothing here is reopened without new evidence.

| Alternative | Source | Why it loses |
|---|---|---|
| Edit only `styles.xml` for typography | (considered) | provably inert for the CV — generated runs carry inline `w:sz` |
| Hand-edit the master DOCX once | both | unreproducible with no `.git`; `prepare_masters` exists for exactly this |
| Typography block in `template_map.json` | both | presentation logic in the render path; widens a frozen input for no gain |
| Value-keyed size map | both | not idempotent — a second run refires on the new 10s |
| Headings at 12 (flatten) | Claude v1 | removes a differential that exists today, at the moment body grows |
| Proportional scaling of every size | Claude | 13.3 pt is outside the user's scale and blows the page budget |
| Categorical ban on mission/societal language | Claude v1 | would destroy Avinor's legitimate operating-environment paragraph |
| New motivation hierarchy in the doctrine | Claude | restates existing coverage (V3) |
| Multi-bullet leverage floor | Claude | `Rolig faglig tyngde` already forbids `undersalg` (V4) |
| Lexical rule naming `rapportert`/`oppgitt` | both | invites substitution over judgement; strips genuine qualifications |
| Edit `Work_experience.md` to remove "reports" | both | the provenance marker is true and useful inside the authority |
| Deterministic hedge detector | both | semantic judgement; `INV-07` and Spec §10.3 forbid failing on a string |
| Advisory render-time dash warning | Claude | outcome D warns against assuming a validator; superseded by acceptance checks |
| Hyphen for the two unit names | both | would itself be a clause-dividing hyphen; comma chosen |
| Converting `authority_anchor` en dashes | both | inert, never rendered, and two are cross-references into `Work_experience.md` |
| Normalising dashes at render time | both | hides the source of truth and breaks `static_baseline_assertions` |
| Voice file in `context/` with a new frozen-input key | both | absent from `branch.CONTENT_GOVERNING` → a child rebind could reuse a final produced under a different voice file |
| Voice section inside `PERSONALITY_PROFILE.md` | both | Spec §10.2 / Contract §12 forbid full-profile downstream; needs a routing mechanic |
| Voice inside `WRITING_DOCTRINE.md` | both | conflates universal doctrine with one candidate's habits |
| Voice inside `PERSUASION_CALIBRATION.md` | both | that file is a corrections log |
| A new Stage 4 / 3.5 for voice | both | Contract §22 prohibits a fourth stage |
| Dynamic per-vacancy voice from Stage 1 | both | voice is candidate-invariant; register adaptation belongs to the writer |
| Deterministic humanizer or LLM voice judge | both | Contract §22, Spec §13.4 |
| Heavy voice conditioning in Stage 2 | both | **refuted by the pilot**: Stage 3 replaced both openings, deleted a paragraph each, reordered evidence and trimmed competencies — it is not anchored |
| Move `mkdtemp` to the job directory | Claude | **V1: inert** — the mode, not the parent, creates the protected DACL |
| Reset ACLs after promotion | both | Windows-specific SD code, and a window where the canonical file is wrong |
| Copy instead of atomic move | both | re-inherits but loses the atomic rename `GATE-08`/Spec §5.6 depend on |
| Document a copy-out step in the RUNBOOK | both | leaves `status --json` naming an unreadable path and `verify_receipt` unable to re-hash |
| Change the sandbox `%TEMP%` ACL | Codex | `mkdtemp`'s protected child defeats it anyway |
| Delete the stale `configured_model is None` assertion | Claude v1 | removes coverage; fixture ownership adds it |
| Blank the production role mapping | both | would falsify GATE-10 evidence |
| Stop copying the real policy tree in `conftest` | both | large change to a deliberate design |
| Cross-job similarity/convergence detector | both | prohibited (Contract §22, Spec §3); `EXP-07` defers to human observation |
| Requiring structural variation between letters | Claude v1 | rewards difference for its own sake |
| Automatic pilot-log tooling | both | deferred; a RUNBOOK line is the smallest local remedy |
| Adding `warnings` to `status --json` | both | `status.schema.json` is closed (F10) |
| Wiring the six dead settings keys | both | deliberated and deferred (F22) |
| Removing the dormant `converter = "auto"` | both | deferred; production uses `word_com` |
| `NOT_RENDERED` for superseded receipts | both | implemented, tested and reverted; broke four `ACC-05`/`DEC-42` assertions |
| Renaming `reviewed_by` / `finalized_by` | both | settled by RUNBOOK wording |

---

## 5. Reproduced but **not** defective — protected from refactoring

Carried forward from both packages; nothing here is touched.

| Observation | Why it is correct |
|---|---|
| Two byte-identical CV bullets across both jobs | `Variasjon innenfor en klynge` permits shared facts; these are specific, in different positions, under materially different CV tops |
| **Avinor's societal-purpose motivation paragraph** | names the operating environment, a causal feature of the work and the basis of the transfer argument. **Must survive.** |
| Avinor's *"forventninger må gjøres etterprøvbare, ansvar og antakelser må være synlige, og metoden må fungere for dem som skal bruke den"* | the strongest existing evidence of the candidate's voice; carried as the **regression guard** |
| Stage 3 removing both defensive "I lack X" paragraphs | correct under `TOO_WEAK`; limitations preserved in `known_limitations` |
| Both `READY` triage values | correctly calibrated |
| Exclusion of the AI-generated JobMatch panel, independently in both jobs | exactly right |
| Render `DEGRADED` on the pilot | a Word-COM session fact, not a converter defect |
| Header/footer at 8 pt | deliberately subordinate running furniture, in scale |
| Six `source: none` template zones | render as absent, working as designed |
| Latent Word styles (`Heading2`, `BodyText*`, `Quote`, …) | applied by no paragraph in either master |
| `upstream_claim_repaired: null` in both reviews | truthful — no overclaim was present; the gap was the opposite direction |

---

## 6. Where each package was wrong

Recorded because the reconciliation is only trustworthy if it names its own errors.

**Claude package, corrected here:**

1. F1 mechanism — the fix was inert (V1). The most serious error in either package: it would have
   shipped, passed its own test, and left the defect in place.
2. ISS-13 root cause attributed to the sandbox `%TEMP%` DACL at MODERATE confidence; the real cause is
   `mkdtemp`'s mode, measurable and universal.
3. `prepare_masters --check` twice as an idempotence proof — `--check` does not write.
4. A new motivation hierarchy and a multi-bullet leverage floor that restate existing Norwegian
   coverage (V3, V4).
5. File count 20 and test count 257, both understated/overstated respectively.
6. A hard "CV must be 2 pages" criterion that outranks `DEC-24`.

**Codex package, corrected here:**

1. B0-by-copy assumes an identity precondition it does not state; it hard-fails for any operator that
   is not the file owner (V2).
2. The C1 worked example was dropped, leaving the over-application risk without a worked boundary —
   a risk Codex itself lists as open uncertainty #3.
3. `§ Motivasjonsregister` was deleted entirely, so nothing tells any writer what this candidate finds
   motivating when Stage 1 selects no motivation facet.
4. Two reproduced anti-patterns were dropped in favour of one inferred structural item.
5. Removing the render warning **and** having no Run B punctuation check leaves outcome D unverified
   on model-generated prose.

**Both packages were right, independently, about:** the typography table and tier design, ISS-04, the
`policy/writing/` placement and its `CONTENT_GOVERNING` argument, rejecting Stage-2 voice conditioning
on pilot evidence, the semantic-field replay recipe, property-based Run B criteria, the Avinor
regression guard, the no-amendment conclusion, and the stopping rule.

---

## 7. Post-review corrections — Codex review of the master package, 2026-09-01

Codex reviewed the three MASTER files and returned eleven findings with a verdict of
**conditional NO-GO**. Ten are valid, one is partly valid. All are folded in. This section is the
disposition record.

The verdict was correct: one finding made a step **literally unimplementable**, so "not yet safe to
implement literally" was the right call, not a stylistic objection.

| # | Codex finding | Verified? | Disposition |
|---|---|---|---|
| 1 | **F2 cannot be implemented as written.** The test takes the `frozen` fixture, which has already called `freeze(...)`, so "set role mapping before freeze" is impossible. | **YES** — `test_t05_public_handoff_completes_all_stages_and_review_only(frozen)` at line 169; `frozen` calls `freeze(...)` in `conftest.py:91`. | **ACCEPT IN FULL.** Plan §7.2 now specifies the signature change to `layout`, the explicit `freeze(...)` call reproducing the fixture, and confirms `freeze`/`load_manifest`/`FIXED_MOMENT` are already imported. **This was implementation-blocking and I missed it.** |
| 2 | **`Motivasjonsregister` bypasses the frozen 0–3 facet interface.** | **YES, on reasoning.** | **ACCEPT — my restoration was wrong; withdrawn.** See §7.1. |
| 3 | **The typography contract contradicts itself** (size set excludes 20 pt; letter `Title` stays 20 pt). | **PARTLY.** The contradiction in the stated set is real — `Title` = 40 half-points in `styles.xml` and is applied. But the claim that T1 "would reject the intended master" is wrong: T1 scans `document.xml`, where the letter's only inline size after A1 is 20 half-points. `Title`'s 40 lives in `styles.xml`, which T1 did not scan at all. | **ACCEPT the conclusion, correct the mechanism — and the fix is better than either version.** The real defect is that the contract was *both* mis-stated *and* under-tested: nothing checked applied `styles.xml` sizes beyond `Normal`. Plan §2.3 now states five tiers **plus the retained 20 pt Title**; T1 now asserts inline sizes **and** every applied style, with `Title = 40` as a named exception. |
| 4 | **File accounting is inconsistent** — 22 manifest paths, 21 expected diffs including `BUILDER_REPORT.md`, not "21 plus Builder". | **YES** — my table listed 22 rows and my prose said "21 + `BUILDER_REPORT.md`", double-counting row 22. | **ACCEPT.** Plan §1 and §11 now separate the three numbers: 22 snapshotted, 21 diffs, 1 new file, `evidence_index.json` byte-identical. |
| 5 | **Overstated authority and provenance** — "needs nothing else" is unsafe; "both retained unmodified" is unsupported. | **YES on both.** Codex revised the eight source files in place, so the Claude first revision is gone. | **ACCEPT.** Plan header now ranks the master files *below* the frozen architecture and current code, and requires `AGENTS.md` plus both architecture files to be read. Ledger header corrected. |
| 6 | **The `PRJ-04` worked example is in the wrong layer** — a candidate-specific project claim inside universal persuasion policy risks turning policy into a factual carrier. | **YES on the risk.** | **ACCEPT the relocation, keep the mechanism** — see §7.2. |
| 7 | **The ledger contains disproven claims** — 07 already has a Run B punctuation check; the phrase evidence is overstated. | **YES on both.** `07…md` §5.1 item 6 is a Run B punctuation check. Measured: `Det som særlig motiverer meg` appears in Huseierne only, not Avinor. | **ACCEPT.** §3.4 withdrawn, §3.3 corrected with measured counts. |
| 8 | **COM used as an unconditional early blocker despite being session-dependent.** | **YES** — my step-1 gate read "251/0/0 with Word COM", which stalls everything on a session fact. | **ACCEPT.** Plan §8.1 and Verification §2.1 now allow `241 / 0 / 10 named skips` as provisional, with final acceptance still requiring the interactive counts, Word-open, A1 page counts and the cross-identity open. |
| 9 | **The cluster gate is absent from the numbered success criteria.** | **YES** — it was in §7 and §9 but not §8.1. | **ACCEPT.** Verification §8.1 gains item 11 and an explicit statement that items 1–10 are not terminal. |
| 10 | **The largest transformation is not decision-complete** — `prepare_masters` has output tables but no transform design. | **YES.** | **ACCEPT.** Plan §2.9 now requires anchor resolution, element scope, refusal behaviour, counters, the idempotence argument and pass ordering to be settled *before* either master is written. |
| 11 | **"Universal" ACL language is overbroad** — `0o700` is intentional on POSIX. | **YES.** | **ACCEPT.** Plan §7.1 now scopes the claim to the supported Windows/Python 3.14.3 target and explains that the opt-in exists precisely because POSIX privacy is correct behaviour. |

### 7.1 Reversal — `§ Motivasjonsregister` is withdrawn

Ledger §2.6 E-5 and §3.2 recorded a `MODIFY` restoring the register as "expression guidance, not a
motive hierarchy." **That was wrong, and Codex's original deletion was right.**

The distinction I drew does not survive scrutiny. The section said *"Troverdig: … mestring, leverage,
læring, autonomi, det å bygge kapasitet"* — that tells a writer **what motives to attribute to the
candidate**. That is substance, not expression. And because every `policy/writing/*.md` file is routed
to all three stages on every job, it would deliver that claim unconditionally, bypassing Stage 1's
zero-to-three facet selection, the evidence-binding requirement, and the distilled-handoff boundary
(Spec §10.2). A writer could then write *"jeg motiveres av å bygge kapasitet"* with no evidence
binding — precisely what the facet interface prevents.

My justification was that if Stage 1 selects no motivation facet, nothing tells the writer what
motivates this candidate. **That is the architecture working as designed, not a gap.** Zero facets is
an explicitly valid outcome; when motivation matters, Stage 1 selects the facet and binds it to
evidence. Building a bypass because the sanctioned channel is sometimes empty is how frozen interfaces
erode.

Disposition: **E-5 REVERSED to `REJECT`.** The register is removed and the plan carries an explicit
note forbidding its reintroduction.

### 7.2 Modification — the `PRJ-04` example is genericised, not deleted

Ledger §2.4 C-3 and §3.1 recorded `RESTORE Claude` for the concrete worked example. Codex is right
about the risk: a finished candidate-specific sentence sitting in universal policy is a second path to
a factual claim that bypasses the authority files, which undercuts `INV-03`.

But deleting the example outright loses the only concrete statement of the **over-correction
boundary**, and over-correction — stripping a real qualification and drifting into overclaiming — is
the most serious risk in the change set. Both concerns are legitimate.

Disposition: **C-3 MODIFIED to `MERGE`.** The example stays in `TOO_WEAK` but becomes **generic**
(`Y-standard`, `N år`), carrying the three-way `riktig` / `for svakt` / `for sterkt` boundary with no
project, no figures and no candidate fact. The concrete `PRJ-04` instance moves to the Run B
acceptance criteria and `BUILDER_REPORT.md`, where it is a check rather than a template. This is
better than either the Claude or the Codex position.

### 7.3 What the review changed about confidence

Two findings (1 and 3) were only findable by executing against the repository rather than reading the
plan. That is the second time in this project that reading-level review missed something
execution-level review caught, and it is the strongest available argument for keeping an adversarial
opposite-family review in the loop after implementation, not only after planning.

### 7.4 New evidence: B0 is present, and the pilot output is now inspectable

After the review, the human copied both pilot vacancy folders — including all four rendered DOCX — to
`P0.9/Process/finalization/test-run output/`. This has two consequences.

**B0 no longer needs recovery.** The identity-gated copy step and the Run A0 fallback are both
withdrawn from the planned sequence (retained only as a contingency). This also removes one of the two
arguments that favoured a `veggi`-identity implementer.

**Every typography and punctuation claim is now verified against the real rendered output**, not the
vertical-slice proxy:

| Claim | Predicted from the masters | Measured in the pilot CV/letter |
|---|---|---|
| CV en dashes | 15 | **15** |
| CV em dashes | 4 | **4** |
| Letter en dashes | 1 | **1** |
| CV inline run sizes | `{8.5, 9.0, 9.5, 10.0, 24.5}` | **identical** |
| Letter body sizing | inherits `styles.xml Normal` | **confirmed — no inline size** |
| ISS-04 TIDLIGERE ERFARING formatting | 9.5 pt bold navy `17324D` | **confirmed, on the same line as an em dash** |

The whole outcome-A and outcome-D analysis now rests on the actual employer-facing documents. That
raises confidence in the largest change in the pass from *modelled* to *measured*.
