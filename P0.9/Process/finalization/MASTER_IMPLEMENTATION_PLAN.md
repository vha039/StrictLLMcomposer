# MASTER IMPLEMENTATION PLAN — P0.9 final pilot-learned optimization pass

**Status:** reconciled master plan. Not authority; the frozen architecture governs.
**Produced:** 2026-09-01 by reconciling the Claude package, the Codex package and the live repository.
**Supersedes for execution:** `00_…md`–`07_…md` in this directory, which are retained as provenance.
**Companions:** `MASTER_RECONCILIATION_LEDGER.md` (why each item won) ·
`MASTER_VERIFICATION_AND_ACCEPTANCE.md` (how success is proven).

**Authority.** This file is an implementation proposal, not self-authorizing authority. It ranks
*below* the current explicit user instruction, the two frozen architecture files, and reproduced
repository behaviour. An implementing agent must still read the root `AGENTS.md` and both frozen
architecture documents, and must verify each premise against current code before acting. Where this
file and the repository disagree, the repository wins and the agent stops and reports.

**Revision, 2026-09-01 (post-review).** Corrected after an independent Codex review found eleven
issues, ten of which were valid — including one that made a step literally unimplementable. All are
folded in. See `MASTER_RECONCILIATION_LEDGER.md` §7 for each disposition.

---

## 0. Ground rules

1. **No `.git` in this checkout.** `git commit` and `git diff` against history are impossible.
   Step 0 (§8) creates the snapshot that *is* the rollback. Any instruction that says "commit per
   change" is wrong here.
2. **Scratch outside `P0.9/Build/`** for `--basetemp` and destructive work. Never inventory `.venv/`,
   `__pycache__/`, `.pytest_cache/`.
3. **The retained pilot run `r20260828-213932-7f13b4` is evidence.** Read it, copy from it, never
   write to it.
4. **Verify paths with `Path(...).is_file()`**, not by eyeballing piped CLI output — the build root
   contains `ø` and a shell pipe can mangle it.
5. **Word COM availability is session-dependent.** A COM failure is a session fact, not a converter
   defect. Skips are not passes; name each one.
6. **Order matters.** §8 gives the sequence and the reason for every dependency.
7. **Stop conditions are in §10.** Three of them are hard stops, not judgement calls.

---

## 1. File manifest — the complete change surface

Three numbers, kept distinct because conflating them has already caused one accounting error:

- **22 manifest paths** may be written or checked, and all 22 must be in the step-0 snapshot
  (recording `ABSENT` for the one that does not yet exist).
- **21 expected final diffs**, including `BUILDER_REPORT.md`. `generated/evidence_index.json` is
  rewritten by `index build` but must come back **byte-identical**, so it is a verification
  by-product, not a diff.
- **1 new file** (`policy/writing/FORFATTERSTEMME.md`), absent at baseline.

Two of the 21 are regenerated binaries. `pilot/PILOT_LOG.csv` is human-written data after Run B and is
outside the implementation diff.

| # | File | Changes | Kind |
|---|---|---|---|
| 1 | `policy/writing/WRITING_DOCTRINE.md` | A3, D5 | edit |
| 2 | `policy/writing/PERSUASION_CALIBRATION.md` | C1 | edit |
| 3 | `policy/writing/FORFATTERSTEMME.md` | E1 | **new** |
| 4 | `policy/stages/stage1_decision_architecture.md` | B1, B3, C2 | edit |
| 5 | `policy/stages/stage2_package_writer.md` | E2 | edit |
| 6 | `policy/stages/stage3_final_writer_review.md` | B2, C2, E2 | edit |
| 7 | `policy/RUNBOOK.md` | pilot-log line | edit |
| 8 | `authorities/CV_BASELINE.md` | D3 | edit |
| 9 | `generated/baseline_map.json` | D3 | **regenerated** |
| 10 | `generated/evidence_index.json` | — | rewritten **byte-identical**; not a diff |
| 11 | `templates/CV_MASTER.docx` | A1, A2, D4 | **regenerated binary** |
| 12 | `templates/APPLICATION_MASTER.docx` | A1, A2, D4 | **regenerated binary** |
| 13 | `runtime/tools/prepare_masters.py` | A1, A2, D4 machinery | edit |
| 14 | `runtime/jobbsok/render.py` | D1, D2, F1 call-site | edit |
| 15 | `runtime/jobbsok/atomicio.py` | F1 transaction option | edit |
| 16 | `runtime/jobbsok/leakage.py` | D4 (one string) | edit |
| 17 | `runtime/tests/conftest.py` | F2 helper | edit |
| 18 | `runtime/tests/test_t05_t08_ownership_schema_failure.py` | F2 | edit |
| 19 | `runtime/tests/test_t16_t18_containment_template.py` | T1–T3 | edit |
| 20 | `runtime/tests/test_t19_t23_render_security.py` | T4–T5 | edit |
| 21 | `pyproject.toml` | version → `0.9.2` | edit |
| 22 | `BUILDER_REPORT.md` | implementation/test ledger | edit |
| — | `pilot/PILOT_LOG.csv` | two rows after Run B | human data |

**Must not change:** `P0.9/Architecture/*` · every `schemas/*.json` · `templates/template_map.json` ·
`policy/settings.toml` · `policy/personality_facets.json` · `context/PERSONALITY_PROFILE.md` ·
`authorities/Work_experience.md`, `Education.md`, `Other_high_value_information.md` ·
`runtime/jobbsok/{artifacts,status,manifest,branch,merge,docxfill,pdf,schemas,paths,validate,failure,
baseline,evidence_index,batchinput,vacancy,hashing,ioenc,errors,cli}.py` · the retained pilot run ·
`evidence/gates/GATE-02/original_p07_masters/` · the eight `0*_…md` provenance files in this directory.

**Version discipline.** Bump the `version:` frontmatter of every changed control-plane file and
`pyproject.toml` to `0.9.2`. `SPEC_REVISION`, `SCHEMA_REVISION`, the `manifest.schema.json` consts and
`policy/settings.toml [spec]` all stay `0.9.0`.

---

## 2. A — Typography

### 2.1 Why the master, and why `prepare_masters`

`docxfill.fill_block` deep-copies the template paragraph inside each SDT, and
`docxfill._set_paragraph_text` deep-copies the **template run including its `w:rPr`**. Generated
paragraphs therefore inherit the master's **inline `w:sz`**. For `CV_MASTER.docx` the `styles.xml`
sizes are effectively inert — every paragraph carries an inline size. For `APPLICATION_MASTER.docx`
the opposite holds: `APPLICATION_BODY` and the signature have **no** inline size and take
`styles.xml Normal`. Changing only one mechanism silently does nothing.

`prepare_masters.py` is the only auditable route to a master edit in a repository with no version
control. It already reorders `w:pPr`/`w:rPr` for ECMA-376 validity, retargets absent fonts to Calibri,
removed the P0.7 forced page break, and **verifies the control contract before writing**.

### 2.2 The table is position-keyed, not value-keyed

A value map (`9.0 → 12`) is **not idempotent**: after one run the document holds 10 and 12, and a
second run fires again on the 10s. Key by **SDT tag** for the 24 controls and **normalized text
anchor** for static furniture, with an absolute target. Refuse to write on anchor mismatch, using the
existing control-contract refusal pattern.

### 2.3 Five tiers

| Tier | pt | half-points | Role |
|---|---|---|---|
| T1 | 24 | 48 | candidate name |
| T2 | 14 | 28 | section headings and the CV functional identity |
| T3 | 12 | 24 | substantive body prose and record title lines; letter body |
| T4 | 10 | 20 | deliberately subordinate content and metadata |
| T5 | 8 | 16 | running header and footer — **unchanged** |

**The full contract is five body/furniture tiers PLUS one retained exception.** Stating it as a flat
five-value set was wrong: the letter's `Title` style is 20 pt (40 half-points) in
`APPLICATION_MASTER/word/styles.xml`, is applied by the subject-line paragraph, and is deliberately
kept. So:

- **Inline `w:sz` in either `word/document.xml`:** only `{16, 20, 24, 28, 48}` half-points
  = `{8, 10, 12, 14, 24}` pt.
- **Applied `styles.xml` styles:** CV `Normal`/`ListBullet` = 24, CV `Heading1` = 28, letter `Normal`
  = 24, **letter `Title` = 40 (20 pt), retained unchanged**.

No half-points anywhere. Headings go to 14, not 12, because they sit only 1 pt above body today;
setting both to 12 would remove a differential at the moment the body grows. Test T1 must assert both
lines above, including the `Title` exception explicitly — otherwise the contract is either
self-contradictory or silently untested in `styles.xml`.

### 2.4 `CV_MASTER.docx` — `word/document.xml`, all 35 body paragraphs

`w:szCs` is absent throughout both masters. Set `w:sz` only; do not add `w:szCs`.

| ¶ | Anchor | Now | → | Bold / colour |
|---|---|---|---|---|
| 1 | text `VEGARD HÅLAND` | 24.5 | **24** | keep `b`, `caps`, `17324D` |
| 2 | SDT `CV_FUNCTIONAL_IDENTITY` | 10.0 | **14** | keep `b`, `caps`, `0F6B73` |
| 3 | SDT `CV_VALUE_PROPOSITION` | 9.0 | **12** | unchanged (inert control, `source: none`) |
| 4 | text starting `Oslo  \|  +47` | 8.5 | **10** | unchanged (`5B6570`, not bold) |
| 5 | `Heading1` text `Profil` | 10.0 | **14** | keep `b`, `caps`, `0F6B73` |
| 6 | SDT `CV_PROFILE` | 9.0 | **12** | unchanged |
| 7 | SDT `CV_CORE_COMPETENCE` | 9.0 | **12** | unchanged |
| 8 | SDT `CV_TOOLS_METHODS` | 9.0 | **12** | unchanged (inert) |
| 9 | `Heading1` text `Yrkeserfaring` | 10.0 | **14** | keep |
| 10 | text `Rådgiver Økonomi og IKT  \|  Oslo universitetssykehus HF` | 10.0 | **12** | keep `b`, `17324D` |
| 10 | …its period run | 8.5 | **10** | keep `b`, `5B6570` |
| 11 | text `Direktørens stab…` (unit) | 9.0 | **10** | keep `b`, `1F2933` |
| 11 | …its period run | 8.5 | **10** | keep `b`, `5B6570` |
| 12 | SDT `CV_CURRENT_ROLE_TOP_EVIDENCE` (`ListBullet`) | 9.0 | **12** | unchanged |
| 13 | SDT `CV_SELECTED_EVIDENCE_HEADING` | 9.0 | **12** | inert |
| 14 | SDT `CV_SELECTED_EVIDENCE` (`ListBullet`) | 9.0 | **12** | inert |
| 15 | text `Barne- og ungdomsklinikken…` (unit) | 9.0 | **10** | keep |
| 15 | …its period run | 8.5 | **10** | keep |
| 16 | SDT `CV_EARLY_ROLE_EVIDENCE` (`ListBullet`) | 9.0 | **12** | unchanged |
| 17 | `Heading1` text `Utdanning` | 10.0 | **14** | keep |
| 18 | text `Masterprogram i kunstig intelligens  \|  …` | 9.5 | **12** | keep `b`, `17324D` |
| 18 | …its period run | 8.5 | **10** | keep |
| 19 | text `Pågående.` | 8.5 | **10** | unchanged |
| 20 | text `Master i samfunnsøkonomi  \|  NTNU` | 9.5 | **12** | keep |
| 20 | …its period run | 8.5 | **10** | keep |
| 21 | SDT `CV_RELEVANT_MASTER_SUBJECTS` | 8.5 | **10** | unchanged |
| 22 | text `Bachelor i samfunnsøkonomi  \|  …` | 9.5 | **12** | keep |
| 22 | …its period run | 8.5 | **10** | keep |
| 23 | SDT `CV_RELEVANT_BACHELOR_SUBJECTS` | 9.5 | **10** | **remove `w:b`; remove the `w:color` override so it inherits `Normal`** |
| 24 | SDT `CV_SUPPORT_SECTION_1` ¶1 (`Heading1`) | 10.0 | **14** | keep |
| 25 | SDT `CV_SUPPORT_SECTION_1` ¶2 | 9.0 | **10** | unchanged |
| 26 | SDT `CV_SUPPORT_SECTION_2` ¶1 (`Heading1`) | 10.0 | **14** | keep |
| 27 | SDT `CV_SUPPORT_SECTION_2` ¶2 | 9.0 | **10** | unchanged |
| 28 | SDT `CV_SUPPORT_SECTION_3` ¶1 (`Heading1`) | 10.0 | **14** | keep |
| 29 | SDT `CV_SUPPORT_SECTION_3` ¶2 | 9.0 | **10** | inert |
| 30 | SDT `CV_OPTIONAL_PREVIOUS_EXPERIENCE` ¶1 (`Heading1`) | 10.0 | **14** | keep |
| 31 | SDT `CV_OPTIONAL_PREVIOUS_EXPERIENCE` ¶2 | 9.5 | **10** | **remove `w:b`; remove the `w:color` override** |
| 32 | SDT `CV_OPTIONAL_TRUST` ¶1 (`Heading1`) | 10.0 | **14** | keep |
| 33 | SDT `CV_OPTIONAL_TRUST` ¶2 | 9.0 | **10** | unchanged |
| 34 | SDT `CV_OPTIONAL_LANGUAGES` ¶1 (`Heading1`) | 10.0 | **14** | keep |
| 35 | SDT `CV_OPTIONAL_LANGUAGES` ¶2 | 9.0 | **10** | unchanged |

**The bold/colour change applies to exactly ¶23 and ¶31.** These are *content* zones that inherited
*record-title* run properties. Paragraphs 10, 11, 15, 18, 20 and 22 are genuine record lines; their
bold and colour are correct design and **must not** be touched.

`word/header1.xml`, `word/footer1.xml`, `word/footer2.xml`: **unchanged**, 8 pt.

### 2.5 `APPLICATION_MASTER.docx` — all 8 body paragraphs

| ¶ | Anchor | Now | → |
|---|---|---|---|
| 1 | SDT `APP_EMPLOYER` (inline run) | 8.5 | **10** |
| 2 | SDT `APP_UNIT_OPTIONAL` | 8.5 | **10** |
| 3 | text `Oslo, ` + SDT `APP_DATE` | 8.5 | **10** |
| 4 | text `Stilling: ` + SDT `APP_JOB_TITLE` (1st) | 8.5 | **10** |
| 5 | SDT `APP_REFERENCE_OPTIONAL` | 8.5 | **10** |
| 6 | `Title` text `Søknad – ` + SDT `APP_JOB_TITLE` (2nd) | style 20 | **20 unchanged** — dash per D4 |
| 7 | SDT `APPLICATION_BODY` | style `Normal` | **via `styles.xml`** |
| 8 | text `Med vennlig hilsen` / `Vegard Håland` | style `Normal` | **via `styles.xml`** |

### 2.6 `styles.xml`

| Master | Style | now | → | Load-bearing? |
|---|---|---|---|---|
| CV | `Normal` | 18 | **24** | No — every CV paragraph has an inline size. Defensive, so a future paragraph without an override renders at 12, not 9. |
| CV | `ListBullet` | 18 | **24** | Defensive. |
| CV | `Heading1` | 20 | **28** | Defensive. |
| Letter | `Normal` | 21 | **24** | **Yes.** This is what moves the letter body to 12 pt. |

`Heading2`, `Heading3`, `BodyText*`, `List*`, `Quote`, `MacroText`, `Caption` and every character
style are latent Word boilerplate applied by no paragraph. Leave them. `Title` **is** applied (one
letter paragraph) and stays at 20.

### 2.7 Spacing: deliberately unchanged (A5)

Do **not** alter `w:spacing` or `w:line`. The tier scale models to ≈1.5 pages for the CV and ≈0.7 for
the letter, so it is unnecessary, and every spacing change costs page budget. At `w:line="252"` (1.05)
a 12 pt Calibri line is tight but legible. If the B0/A1 visual review judges the body cramped, a single
canonical `w:line` adjustment in both masters is a sanctioned follow-up under A3 — measured, not
speculative, and recorded as a separate change.

### 2.8 Page-count model — a model, not a measurement

CV text area 17.9 × 27.0 cm ⇒ ≈765 pt per page; the pilot CV content models to ≈1150 pt ⇒ **≈1.5
pages**, a genuine two-page CV with page 2 about half full. At today's 9 pt the same content models to
≈1.2 pages, which is why page 2 is nearly empty. Letter text area 17.0 × 26.3 cm ⇒ ≈745 pt per page;
the pilot letter models to ≈520 pt ⇒ **≈0.70 page**.

**Estimates. Replaced by the A1 measurement.** If the CV renders to three pages, apply A3 — editorial
compression, **never** a type-size reduction. `DEC-24` forbids deleting decision-relevant content to
satisfy a page rule. A third page is accepted only when compression and canonical spacing review show
that forcing two would reduce employer-facing quality.

### 2.9 The transform design must be settled before any master is written

§2.4–§2.6 specify the **output** — which paragraph ends at which size, weight and colour. They do not
specify the **transform**, and that gap is the largest remaining implementation risk in the pass: it
is the one place where a plausible-looking implementation can corrupt a binary that Word then refuses.

Before touching either master, the implementer must state, and I must be able to check:

1. **Anchor resolution** — how each of the 43 target paragraphs is located: SDT `w:tag` for the 24
   controls, and a normalized visible-text match for the static furniture. Which normalization
   (whitespace, case, the `  |  ` separators) is applied.
2. **Element scope** — that only `w:rPr/w:sz` is written, that `w:szCs` is not introduced (both
   masters have zero today), and that `w:b`/`w:color` are touched on exactly ¶23 and ¶31 of the CV.
3. **Refusal behaviour** — what happens when an anchor is missing, matches more than once, or already
   holds an unexpected value. The existing control-contract refusal is the pattern: report, refuse to
   write, exit non-zero. Never write a partially-transformed master.
4. **Counters** — the statistics `prepare()` returns and `main()` prints, extending the existing
   `parts_reordered` / `property_blocks_fixed` / `font_refs_retargeted` shape with typography and
   dash counts, so `--check` can report **0 pending** after a successful write.
5. **Idempotence argument** — why a second run is a no-op, given the table is position-keyed rather
   than value-keyed.
6. **Ordering inside `prepare()`** — where the typography and dash passes sit relative to the existing
   `retarget_fonts` and `reorder_properties`, and confirmation that writing `w:sz` cannot disturb the
   ECMA-376 child ordering that `reorder_properties` exists to guarantee.

Reuse the existing script, its `ZipFile` round-trip and its ElementTree approach. Add no new
dependency, no new module and no XML framework.

---

## 3. B and C — policy treatment

The governing finding: **the existing Norwegian doctrine already covers outcomes B and C almost
entirely.** The pilot failed on routing and salience, not on coverage. Two narrow insertions remain,
each tied to a specific reproduced failure that no existing sentence addresses.

### 3.1 A3 — `WRITING_DOCTRINE.md § Myke redaksjonelle utgangspunkt`

Append after the existing bullet list and the "Et dokument feiler mekanisk bare når…" sentence:

> Sidemål nås ved redaksjonell komprimering, aldri ved å krympe brødteksten. En stage skal aldri bytte
> skriftstørrelse eller linjeavstand mot plass i en enkelt pakke; typografi er ikke en variabel i det
> semantiske arbeidet. Malenes typografi og avstander settes én gang, av mennesket, i masterfilene, og
> er like for alle jobber. Når et dokument blir for langt, komprimer eller prioriter innhold. Mindre
> skrift er forbeholdt bevisst underordnet informasjon: kontaktlinje, enhets- og periodelinjer,
> fagdetaljer, støtteseksjoner og løpende topp-/bunntekst. Sidetall er fortsatt et redaksjonelt
> signal, ikke en valideringsgrense (`DEC-24`).

### 3.2 B — do **not** edit the motivation doctrine

Do not touch `§ Begrunnet motivasjon` or `§ Arbeidsgiverbyttetesten`. Both already cover the observed
defect. `Begrunnet motivasjon` requires motivation grounded in *"en konkret oppgave eller et reelt
virksomhetsproblem"* and forbids *"generisk virksomhetsros, **kopierte verdier**,
prestisjemotivasjon"* — which literally names the Huseierne failure. `Arbeidsgiverbyttetesten` already
says *"Ikke reparer med slagord, verdikopiering eller ubegrunnet virksomhetsros."*

The two control failures are fixed in the stage instructions instead: **B1** routes Stage 1's
`motivation_bridge` to the section, and **B2** stops Stage 3 citing rejected language as pass evidence
(§4.1, §4.3). A second formulation of an existing rule is exactly the failure mode this project has
already rejected twice.

### 3.3 D5 — `WRITING_DOCTRINE.md`, new `# Tegnsetting` section

Immediately before `# Tjuesekunderstesten`:

> # Tegnsetting
>
> Bruk vanlig norsk tegnsetting. Tankestrek (`–`) og lang tankestrek (`—`) skal ikke forekomme i
> arbeidsgivertekst. Vanlig bindestrek `-` brukes der rettskrivingen krever det: sammensetninger
> (`Barne- og ungdomsklinikken`, `Vakt- og sikringssoldat`), datoer og intervaller. Ikke bruk
> bindestrek bare for å dele en setning når punktum, komma, kolon eller parentes gjør samme jobb.
> Foretrekk `.`, `,`, `:`, `()`, `?`, `!` og anførselstegn. Semikolon er tillatt, men bør være
> uvanlig. `|` er et strukturelt skilletegn i overskrifter og titler og er fortsatt i orden.
>
> > Merk: dette er semantisk skriveveiledning. Deterministisk kode skal aldri felle en pakke fordi et
> > tegn forekommer (Spec 10.3, `INV-07`).

### 3.4 C1 — `PERSUASION_CALIBRATION.md § TOO_WEAK`

The general leverage floor already exists in `WRITING_DOCTRINE § Rolig faglig tyngde`
(*"Det betyr ikke svake verb, mange forbehold eller **undersalg**"*). Only the speaker-transposition
case is uncovered. Keep the two existing bullets and append **one bullet plus the worked example**:

> - Ikke bær kildefilenes dokumentasjonsstemme inn i kandidatens egen tekst. Når myndigheten sier at
>   kandidaten «oppgir X», er X kandidatens egen opplysning og kan sies direkte av ham. Bevar reelle
>   grenser som omtrentlighet, observasjonstidspunkt, lifecycle-tilstand og fravær av måling; fjern
>   bare avstanden som oppstår fordi kilden er skrevet *om* kandidaten. Kjent sannhet skal låte kjent.
>
> Mønstereksempel, med generisk innhold. Kilden sier at noe «ble innført som Y-standard» og er
> «oppgitt aktivt om lag N år senere»:
>
> ```text
> riktig:      «… ble innført som Y-standard og var fortsatt i bruk om lag N år senere.»
> for svakt:   «… var rapportert i bruk om lag N år senere.»
> for sterkt:  «… er fortsatt i bruk i dag.»   (kilden gjelder N år senere, ikke i dag)
> ```

**The example is deliberately generic — no project, no real figures, no candidate fact.** A worked
boundary is load-bearing, because over-application (stripping a genuine qualification and drifting
into overclaiming) is the most serious risk in this change set, and `for sterkt` is the only place the
rule draws that line concretely. But a *candidate-specific* example inside universal persuasion policy
would let a writer lift a finished sentence without re-checking the authority, turning policy into a
second path to a factual claim and undercutting `INV-03`. The concrete `PRJ-04` instance therefore
lives in the Run B acceptance criteria and `BUILDER_REPORT.md`, where it functions as a check rather
than a template.

---

## 4. Stage instructions

### 4.1 B1 + B3 + C2 — `stage1_decision_architecture.md`

**Replace** the paragraph beginning `**Named doctrine sections.**` in its entirety with:

> **Named doctrine sections.** Consult the writing policy only at the sections named below, each bound
> to the strategy field it governs. You are not writing the package; do not read the policy as a
> writing manual.
>
> | Field you are authoring | Section |
> |---|---|
> | backbone, evidence pair, route | `WRITING_DOCTRINE.md § Single Backbone og strategisk asymmetri`, and `PERSUASION_CALIBRATION.md § WRONG_ROUTE` |
> | `evidence_plan[].role`, `claim_ceiling` | `WRITING_DOCTRINE.md § Rolig faglig tyngde`, and `PERSUASION_CALIBRATION.md § TOO_WEAK` |
> | `motivation_bridge` | `WRITING_DOCTRINE.md § Begrunnet motivasjon` |
>
> Do not default to BI, AI or technical prestige where process, economy, governance, implementation or
> adoption explains this employer's need better. Select evidence for this vacancy, not the familiar
> strongest pair.
>
> `evidence_plan[].role` is where you frame a proposition for both downstream writers. Frame it at the
> strength the evidence defends. The authority files are written *about* the candidate; their
> provenance wording is not a qualification to pass on.
>
> `structure_guidance` names the argument **this** vacancy needs. It is not a letter template. Do not
> prescribe a default open-with-the-employer-problem, two-cases, close-with-motivation shape unless
> this vacancy actually calls for it.

Stage 1 is a **non-consumer** of `FORFATTERSTEMME.md`: `motivation_bridge` is strategy, and the
universal doctrine governs it. Voice is expression and belongs downstream.

### 4.2 E2 — `stage2_package_writer.md`

In `## Inputs`, **replace** the bullet

```
- `policy/writing/WRITING_DOCTRINE.md` and
  `policy/writing/PERSUASION_CALIBRATION.md`;
```

with

> - `policy/writing/WRITING_DOCTRINE.md`, `policy/writing/PERSUASION_CALIBRATION.md` and
>   `policy/writing/FORFATTERSTEMME.md`. The last is the candidate's professional author voice; use it
>   as a light prior for natural Bokmål. Do not trade completeness, strategy execution or factual
>   precision for voice — Stage 3 owns final authorship;

This is the **only** change to Stage 2. It exists because the file genuinely reaches Stage 2 through
`read.writing_policy` and is already declared content-governing for `draft_package` in
`branch.CONTENT_GOVERNING`. Saying nothing would leave an unexplained candidate-specific file in
Stage 2's read block.

### 4.3 B2 + C2 + E2 — `stage3_final_writer_review.md`

**(a)** In `## Read order`, replace the paragraph beginning ``The context's `read.writing_policy`
supplies`` with:

> The context's `read.writing_policy` supplies `policy/writing/WRITING_DOCTRINE.md`,
> `policy/writing/PERSUASION_CALIBRATION.md` and `policy/writing/FORFATTERSTEMME.md`. Before choosing
> triage, apply these named sections: `Tjuesekunderstesten`, `Arbeidsgiverbyttetesten`, `Begrunnet
> motivasjon`, `Rolig faglig tyngde`, `Tegnsetting`, `TOO_WEAK` and `UNNATURAL_NORWEGIAN`. Repair,
> rather than merely report, what they expose. **Language rejected under `Begrunnet motivasjon` cannot
> be cited as evidence that `Arbeidsgiverbyttetesten` is passed.**
>
> Before reading the strategy and draft, form an independent thesis and decide the likely opening,
> evidence order and employer register from the vacancy and candidate evidence. Then read upstream as
> an evidence inventory and hypothesis, not as a prose or structure template.
>
> `FORFATTERSTEMME.md` is the candidate's professional author voice. Apply it **after** you have
> grounded the package and decided what it should say. It governs expression only, and can never
> create or remove a proposition, move a claim ceiling, change a lifecycle state or qualification, or
> select evidence. You are this package's author, not its proof-reader.

The bolded sentence is the whole of outcome B's policy change. It targets the reproduced failure
exactly: Stage 3 cited the mission clause in `review.reasons[1]` as proof the swap test passed.

**(b)** In `## What you may not change`, extend the existing bold sentence:

> **A known unsupported or inflated upstream claim must be repaired before you save the final. It must
> never ship under `CHECK`.** The duty is symmetric: a known **material understatement** of an
> established fact is equally yours to repair. See `PERSUASION_CALIBRATION.md § TOO_WEAK`.

### 4.4 `policy/RUNBOOK.md`

In the per-vacancy loop, immediately after the human reviews the rendered package:

> Append one row to `pilot/PILOT_LOG.csv` for the job: triage, actual repair scope, submit-ready,
> factual corrections, minutes through the submission decision, render issues, friction and outcome.
> The columns already exist; this is a hand-written row, and it is the only record of what the package
> actually cost you (Spec §18.3, `ACC-20`).

---

## 5. E1 — `policy/writing/FORFATTERSTEMME.md`

New file. Derived from `PERSONALITY_PROFILE.md` §1 and §6 plus anti-patterns reproduced from the pilot
output. **Vegard reviews and corrects it before Run B.** It contains no facets, no facet IDs, no
typology and no trait claims, so it does not touch the personality interface (Spec §10, Contract §12).

**It deliberately contains no motivation register, and none may be added.** An earlier revision
included a `§ Motivasjonsregister` naming what motivates this candidate. That was wrong and is
withdrawn. Every `policy/writing/*.md` file is routed to all three stages on every job, so such a
section would deliver a candidate-specific motivation claim **unconditionally** — bypassing Stage 1's
frozen zero-to-three facet selection, the requirement that each selected facet be bound to factual
evidence, and the distilled-handoff boundary (Spec §10.2). It would let a writer attribute a motive to
the candidate with no evidence binding, which is precisely what the facet interface exists to prevent.

If a vacancy genuinely needs the candidate's motivation profile, the architecture already has the
mechanism: Stage 1 selects the relevant facet and binds it to evidence. Zero facets being a valid
outcome is the design, not a gap in it.

````markdown
---
document: Jobbsøk_26 P0.9 forfatterstemme
version: 0.9.2
language: nb-NO
owner: Vegard Håland
artifact_role: CONTROL_PLANE
authority_domain: employer_facing_expression_only
factual_authority: false
claim_authority: false
strategy_authority: false
qualification_authority: false
primary_consumer: Stage 3
secondary_consumers: ["Stage 2 (lett prior)"]
non_consumer: "Stage 1 (filen følger writing_policy-ruten, men strategi-instruksen peker ikke til den)"
status: ACTIVE
provenance: >
  Avledet fra context/PERSONALITY_PROFILE.md §1 og §6, og fra mønstre observert
  i den faktiske pilotproduksjonen (r20260828-213932-7f13b4). Ingen fasetter,
  ingen typologi, ingen egenskapspåstander. Filen kan ikke etablere
  kandidatfakta og kan ikke heve eller senke et claim-tak.
---

# Forfatterstemme

Denne filen svarer på ett spørsmål: **hvordan ville denne kandidaten faktisk
skrevet dette, når han legger fram et seriøst faglig argument?**

Den er ikke en «humanizer», ikke et forsøk på å etterligne chat-språk, og ikke
en instruks om å vise personlighet. Den er en generativ prior for uttrykk.

## Rangorden

1. Sannhet og evidensgrenser.
2. Arbeidsgiverens overtalelse og lesbarhet.
3. Stemme.

Stemme kan aldri endre en påstand, et claim-tak, en lifecycle-tilstand, et
forbehold eller et evidensvalg. Den kan endre rekkefølgen på allerede valgt
stoff, argumentets uttrykksform og formulering, men den flytter aldri en grense.

## Argumentvaner

- Sett den bærende påstanden først, begrunnelsen etter.
- Forklar mekanisme og årsak i stedet for å bruke adjektiver. Skriv hvordan noe
  virker, ikke at det er strategisk, innovativt eller spennende.
- Bevar de skillene som faktisk betyr noe for konklusjonen. Ikke glatt dem ut
  for å få en penere setning.
- Bruk konkrete verb og konkret omfang.
- Skriv om oppførsel og resultat, ikke om gunstige egenskaper ved deg selv.
- Ta en spesifikk faglig vurdering framfor en allment akseptabel plattityde.

## Sosial temperatur

Direkte, men profesjonell. Samarbeidsvillig uten ritualhøflighet. Ikke
karikert kontant, ikke kald, ikke konfronterende. Presisjon er høflighet her.
Vis moderat varme gjennom den konkrete, allerede evidensstøttede nytten
argumentet viser for mottakeren, ikke gjennom ros, smiger eller påtatt
entusiasme.

## Setningsarkitektur

- Høy tetthet av relevant signal. Korthet er ikke et mål i seg selv, og
  fullstendighet skal ikke ofres for stramhet.
- Sterk makrostruktur, mindre lakkerte overganger. En tekst kan være godt
  ordnet uten at hvert avsnitt starter med en brolegging.
- Varier setningslengde og avsnittsform når argumentet tilsier det. Ikke bygg
  parallelle bevisblokker bare fordi symmetrien ser ryddig ut.
- En lengre setning er i orden når et forbehold faktisk krever det.
- La avsnittsformen følge argumentet i denne stillingen. To jobber kan gjerne
  få samme form når begge trenger den, men formen skal komme fra jobben og
  ikke fra en mal.

## Mønstre som skal erstattes

Disse er observert i faktisk produksjon og gjenkjennes som generisk
søknadsspråk. De er mønstre å erstatte, ikke forbudte strenger, og
deterministisk validering skal aldri felle en pakke fordi en av dem
forekommer (Spec 10.3, `INV-07`). Om en formulering er akseptabel avhenger
av fortsettelsen: det er den generiske bruken som skal bort, ikke ordene i
seg selv.

1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …`
   som avslutning. Avslutt heller med noe som bare gjelder denne stillingen.
2. `Jeg ønsker å bidra …` som frittstående motivasjonssetning. Si hva du vil
   gjøre, og la det følge av arbeidet.
3. `Det som særlig motiverer meg, er …` fulgt av arbeidsgiverens formål eller
   slagord.
4. `Når <arbeidsgiver> skal <X>, må <Y> …` som standardåpning. En åpning som
   bare refererer arbeidsgiverens egen situasjon tilbake til dem, bruker den
   viktigste setningen i brevet på noe leseren allerede vet.
5. En fast åpning–to bevis–motivasjon–avslutning-form eller speilvendte
   bevisblokker på tvers av jobber. La strukturen følge argumentet.

## Kanalkalibrering

- **CV:** lett. Profil, nøkkelkompetanser og bullets skal være dokumenterende
  og skannbare. Stemme viser seg her som presisjon og konkret omfang, ikke som
  stil.
- **Søknad:** moderat. Åpning, argumentrekkefølge, motivasjon, sikkerhetsnivå
  og avslutning er der stemmen hører hjemme.

## Stabil forfatter, variabelt register

Invariant på tvers av arbeidsgivere: presisjon, årsaksstruktur, lav
performativitet, sikkerhet innenfor evidensgrensen, eksplisitte skiller der de
betyr noe, konkrete mekanismer, lite seremoniell retorikk.

Variabelt: varme, formalitetsnivå, teknisk dybde, setningslengde,
abstraksjonsnivå, forklaringstetthet og ordforråd.

To pakker til to ulike arbeidsgivere skal ikke være like. De skal ha samme
forfatter.

## Anti-karikatur

- Ikke gjør hvert avsnitt analytisk.
- Ikke press inn systemspråk, rammeverksjargong eller metaspråk om metode.
- Ingen personlighetsetiketter, ingen typologi, ingen selvkarakteristikk.
- Ikke etterlign uformell tone eller chat-tegnsetting.
- Ikke gjør kandidaten kranglete eller belærende.
- Arbeidsgiverens overtalelse og lesbarhet slår alltid synlig personlighet.
- Ingen fakta oppstår her. Stemme er uttrykk, ikke evidens.

## Tegnsetting

Følg `WRITING_DOCTRINE.md § Tegnsetting`. Ingen egne regler her.
````

---

## 6. D — punctuation, code and assets

### 6.1 D1 — `render.py:179`, `resolve_control`

```python
lines.append(f"{line} — {summary}" if summary else line)     # before
lines.append(f"{line}. {summary}" if summary else line)      # after
```

The line already uses `|` for structure, so a period is the natural divider. **Not** a hyphen — that
reintroduces the clause-dividing hyphen outcome D prohibits. Do not touch the `·` competency separator
or the `•` bullet separator on the same code path.

### 6.2 D2 — `render.py:832`, `_build_document`

```python
title=f"{spec['output_stem']} – {…full_name…} – {job['title']}",   # before
title=f"{spec['output_stem']} | {…full_name…} | {job['title']}",   # after
```

### 6.3 D3 — `authorities/CV_BASELINE.md`

Sixteen edits inside the fenced JSON block between `<!-- CV_BASELINE_DATA_START -->` and
`<!-- CV_BASELINE_DATA_END -->`. Line numbers as of the current file.

| Line | Field | From | To |
|---|---|---|---|
| 49 | `unit` | `Direktørens stab – Analyseavdelingen` | `Direktørens stab, Analyseavdelingen` |
| 51 | `period` | `12.2023–d.d.` | `12.2023-d.d.` |
| 52 | `employment_group_period` | `03.2023–d.d.` | `03.2023-d.d.` |
| 66 | `unit` | `Barne- og ungdomsklinikken – Stab` | `Barne- og ungdomsklinikken, Stab` |
| 68 | `period` | `03.2023–11.2023` | `03.2023-11.2023` |
| 83 | `period` | `07.2015–08.2021` | `07.2015-08.2021` |
| 97 | `period` | `02.2015–04.2015` | `02.2015-04.2015` |
| 111 | `period` | `03.2014–02.2015` | `03.2014-02.2015` |
| 125 | `period` | `10.2013–03.2014` | `10.2013-03.2014` |
| 140 | `period` | `2024–d.d.` | `2024-d.d.` |
| 152 | `period` | `2020–2022` | `2020-2022` |
| 166 | `period` | `2017–2020` | `2017-2020` |
| 180 | `period` | `2011–2013` | `2011-2013` |
| 202–204 | trust items | three ranges | hyphens |

**Do not change lines 88, 102, 116, 130** — `authority_anchor` values. The schema records them as
*"Inert human-readable note … NOT resolvable as a factual evidence reference"*, `baseline.py` copies
them to an inert `baseline_provenance` field, they never render, and two are verbatim
cross-references to strings in `Work_experience.md`.

Unit names take a **comma**, not a hyphen: `Direktørens stab - Analyseavdelingen` would itself be a
clause-dividing hyphen.

Then `jobbsok index build` followed by `jobbsok index verify`.

### 6.4 D4 — master static furniture, same `prepare_masters` pass

`render.preflight_templates` compares master static text against `baseline_map` through
`static_baseline_assertions`. **D3 and D4 must land together or preflight fails.**

`CV_MASTER.docx`, 8 en dashes, all mirroring D3: `03.2023–d.d.` (¶10),
`Direktørens stab – Analyseavdelingen` and `12.2023–d.d.` (¶11),
`Barne- og ungdomsklinikken – Stab` and `03.2023–11.2023` (¶15), `2024–d.d.` (¶18), `2020–2022` (¶20),
`2017–2020` (¶22).

`APPLICATION_MASTER.docx`, 1 en dash: `Søknad – ` → `Søknad: ` (¶6).

`runtime/jobbsok/leakage.py:98` in `KNOWN_GOOD_PHRASES`:
`"Direktørens stab – Analyseavdelingen"` → `"Direktørens stab, Analyseavdelingen"`.

Verified safe: no JSON-schema `pattern` and no runtime regex depends on the en dash; `leakage.py:98`
and `render.py:832` are the only two code references.

### 6.5 No runtime punctuation validator or warning

Outcome D says the behavioural rule is strong but "do not automatically assume it needs a new Python
validator". After D1–D4 every deterministic source is fixed, and both pilot final packages contain
**zero** en dashes and zero em dashes, so no model-generated dash has ever been observed. T3 covers
the static side at build time. **No render-time warning, no normalizer, no lint is added.**

The residual risk — a future model emitting a dash — is covered by an **acceptance check on extracted
text in both A1 and Run B**, at zero code cost. See `MASTER_VERIFICATION_AND_ACCEPTANCE.md` §3.4 and
§5.1. This is the one place the master plan is stricter than the Codex package, which removed the
warning without adding a Run B punctuation check and so left outcome D unverified on model prose.

---

## 7. F — mechanical corrections

### 7.1 F1 — accessible, atomic render staging

**Moving `tempfile.mkdtemp()` under the job directory is not a fix.** Measured on this checkout
(Python 3.14.3, Windows):

| Creation call | Resulting DACL |
|---|---|
| `os.mkdir(p)` — no mode | inherits normally; `VHAALA\veggi:(I)(OI)(CI)(F)` present |
| `os.mkdir(p, 0o700)` and `tempfile.mkdtemp(...)` | **protected**: `SYSTEM`, `Administrators`, `OWNER RIGHTS` only, no inheritance |
| `Path.mkdir(mode=0o777)` | inherits normally — **the fix**, verified |

And end to end: a file `os.replace`d **out of** a `mkdtemp` directory **into** a normally-inheriting
destination arrives carrying `SYSTEM:(F) Administrators:(F) OWNER RIGHTS:(F)` — no `(I)`, no `veggi`.
That is byte-for-byte the DACL shape of the four pilot DOCX.

The protected descriptor comes from the **mode**, not the parent, so a location-only change preserves
the defect exactly.

**Scope of the claim.** This is *systematic on the supported target* — Windows with Python 3.14.3 —
and it bites whenever the rendering identity differs from the reading identity. It is not a
cross-platform statement: on POSIX, `0o700` is a genuine and intended permission mode, and
`mkdtemp`'s privacy there is correct behaviour rather than a defect. That is exactly why the fix is an
**opt-in** on the render path and the private default is preserved for every other caller.

In `runtime/jobbsok/atomicio.py`: import `secrets`, add `inherit_parent_permissions: bool = False` to
`TransactionDir.__init__`, keep the existing `mkdtemp` path when false, and when true allocate a
collision-safe hidden directory with `Path.mkdir(mode=0o777)`:

```python
def __init__(
    self,
    parent: Path,
    prefix: str = "render",
    *,
    inherit_parent_permissions: bool = False,
) -> None:
    self.parent = Path(parent)
    self.prefix = prefix
    self.inherit_parent_permissions = inherit_parent_permissions
    self.path: Path | None = None

def __enter__(self) -> Path:
    self.parent.mkdir(parents=True, exist_ok=True)
    if not self.inherit_parent_permissions:
        self.path = Path(
            tempfile.mkdtemp(prefix=f".{self.prefix}.", dir=self.parent)
        )
        return self.path

    for _ in range(100):
        candidate = self.parent / f".{self.prefix}.{secrets.token_hex(4)}"
        try:
            candidate.mkdir(mode=0o777)
        except FileExistsError:
            continue
        self.path = candidate
        return self.path
    raise FileExistsError(
        f"Could not allocate transaction directory below {self.parent}"
    )
```

`__exit__` is unchanged. **The default must stay private** — `cli.py:735` uses `TransactionDir` for
rollback snapshots, and only the employer-facing render workspace opts in.

In `render.py:566`:

```python
with TransactionDir(                                            # before
    Path(tempfile.gettempdir()), prefix=f"jb-{job_id[:16]}"
) as workspace:

with TransactionDir(                                            # after
    out_dir, prefix="rnd", inherit_parent_permissions=True
) as workspace:
```

Notes:

- Canonical `out_dir` is already checked by `assert_writable`; `--dest` is resolved and authorized by
  the existing export path. Change neither.
- Staging beside the destination preserves the same-volume atomic rename **and** inherits the
  destination's access policy. It also removes the latent cross-volume failure in export mode, which
  the current `%TEMP%` staging survives only because both happen to sit on one volume.
- `.rnd.<8 hex>` is a short segment; `paths.MAX_PATH_CHARS = 240` and the longest current output path
  is ≈200 characters. Keep the prefix short; do not use the job id.
- `tempfile` becomes unused in `render.py` — remove that import there. It stays used in `atomicio.py`
  and `cli.py`.
- A killed process can leave a hidden `.rnd.*` in `out/`. Preferable to silently publishing
  inaccessible files; the context manager removes it on ordinary exit.
- `pdf.convert` keeps its own `%TEMP%` working directory (`.wordcom_*`) — untouched. The PDF is
  written next to the staged DOCX and promoted from there.

Do **not** reset ACLs after promotion and do **not** switch to a non-atomic copy.

### 7.2 F2 — fixture-owned role mapping

In `runtime/tests/conftest.py`, add `import re` with the stdlib imports, then:

```python
def set_role_mapping(layout, *, sol: str, terra: str) -> None:
    """Give a test ownership of [stages.role_mapping]. Call BEFORE freeze.

    conftest copies the real policy/ tree into every build root, so a test that
    asserts on a production configuration value is a defect (F20). assets.settings
    resolves to the run's frozen copy, so this must run before freeze (F24).
    """
    path = layout.policy / "settings.toml"
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r'(?ms)^\[stages\.role_mapping\][ \t]*\r?\n(?P<body>.*?)(?=^\[|\Z)', text
    )
    assert match is not None, "missing [stages.role_mapping]"
    body = match.group("body")
    body, sol_count = re.subn(
        r'(?m)^SOL_CLASS\s*=\s*".*"$', f'SOL_CLASS = "{sol}"', body
    )
    body, terra_count = re.subn(
        r'(?m)^TERRA_CLASS\s*=\s*".*"$', f'TERRA_CLASS = "{terra}"', body
    )
    assert (sol_count, terra_count) == (1, 1)
    text = text[: match.start("body")] + body + text[match.end("body") :]
    path.write_text(text, encoding="utf-8", newline="\n")
```

In `test_t05_t08_ownership_schema_failure.py`:

- `test_t05_public_handoff_completes_all_stages_and_review_only` — **the fixture must change first.**
  The test currently takes `frozen`, which has *already* called `freeze(...)` before the body runs, so
  there is no `freeze` for `set_role_mapping` to precede. Change the signature from `frozen` to
  `layout`, then open the body with the three lines the `frozen` fixture performed, with the mapping
  set in between:

  ```python
  def test_t05_public_handoff_completes_all_stages_and_review_only(layout):
      set_role_mapping(layout, sol="synthetic-sol", terra="synthetic-terra")
      result = freeze(
          layout, layout.inbox / "batch_input.csv",
          reviewed_by="Test Reviewer", moment=FIXED_MOMENT,
      )
      assert result.ok, result.result.render()
      run_id, manifest = result.run_id, load_manifest(layout, result.run_id)
      job_id = manifest["jobs"][0]["job_id"]
      ...
  ```

  Then replace `assert stage1["configured_model"] is None` with
  `assert stage1["configured_model"] == "synthetic-sol"`, and leave every other assertion in the test
  untouched. `freeze` and `load_manifest` are already imported from `jobbsok.manifest`, and
  `FIXED_MOMENT` from `conftest`, so no new import is needed beyond `set_role_mapping`. The
  replacement assertion is stronger than the one it replaces: it proves the configured mapping
  actually flows through the public handoff, which `is None` never did.
- `test_t05_context_exposes_configured_capability_surface` — replace the literal
  `.replace('SOL_CLASS = ""', …)` with `set_role_mapping(...)` and keep the existing assertion against
  the value the helper was given.

Both tests must pass with the production mapping populated **and** blank. Do not touch
`policy/settings.toml`, runtime behaviour, the schema or the GATE-10 evidence.

---

## 8. Implementation order

| Step | Work | Gate before proceeding |
|---|---|---|
| 0 | Snapshot (§9) | 22-path SHA-256 registry written (one `ABSENT`); **B0 confirmed present** |
| 1 | **F2** | **251 / 0 / 0** with COM, **or provisionally 241 / 0 / 10 named COM skips** (§8.1) |
| 2 | **D1, D2, F1** (`render.py`, `atomicio.py`) + tests T4, T5 | focused tests green; suite still green |
| 3 | Policy: **A3, B1, B2, B3, C1, C2, D5, E1, E2**, RUNBOOK, version bumps | `FORFATTERSTEMME.md` reviewed by Vegard |
| 4 | **D3** → `index build` → `index verify` | `index verify` PASS |
| 5 | **A1, A2, D4** via `prepare_masters` (write, then `--check`) → `preflight` → tests T1–T3 | control contract 17/7 preserved; **both masters open in Word**; `preflight` PASS |
| 6 | **Run A1** replay + render | mechanical acceptance; human visual A/B against B0 |
| 7 | Full suite, adversarial set, vertical slice, scope gate | **256 / 0 / 0**; §11 budget met |
| 8 | **Run B** — fresh Stage 1/2/3; semantic review; two `PILOT_LOG.csv` rows | acceptance criteria |
| 9 | One representative cluster | throughput and convergence |

Dependencies that are not preferences: F2 first because every later gate needs a green suite; code
before Run A1 so the comparison isolates typography; D3 before D4 or preflight fails; the master edit
after the policy edits so a single `prepare_masters` run carries A1+A2+D4 together.

### 8.1 Word COM is a provisional gate, not a hard blocker

COM availability is session-dependent, and the pilot's own render failed COM under one account while
an interactive session on the same machine reached 251/0. Treating it as an unconditional step-1
blocker would stall the entire pass on a session fact.

Therefore, after F2, **either** result lets work continue:

- `251 passed / 0 failed / 0 skipped` — COM available; or
- `241 passed / 0 failed / 10 skipped` — COM unavailable, **provisional**, every skip named and
  confirmed to be one of the ten known Word-COM-scoped cases.

A provisional pass permits all subsequent independent work. It does **not** substitute for final
acceptance: the interactive `251/0/0`, then `256/0/0` after the new tests, the Word-open check on both
masters, the A1 render with real page counts, and the cross-identity open must all be satisfied before
the pass is complete. Never diagnose a COM-unavailable session as a converter defect.

---

## 9. Step 0 — snapshot, and the B0 precondition

No `.git`, so the snapshot is the rollback.

1. Write a SHA-256 registry of the **22-path manifest set** (§1), recording `ABSENT` for the new
   `policy/writing/FORFATTERSTEMME.md`. Snapshot every path that may be written, not only those
   expected to differ.
2. Create `P0.9/Process/finalization_snapshots/pre_0.9.2/`. It **must not already exist**; never
   overwrite a prior snapshot. Copy the 21 existing targets and the current header-only
   `pilot/PILOT_LOG.csv` under `source_tree/`, preserving relative paths.
3. **B0 — the "before" typography evidence. Already present; no recovery step is needed.**

   The human has placed readable copies of both pilot vacancy folders, including all four rendered
   DOCX, at `P0.9/Process/finalization/test-run output/`. Verified from a `vhaala\veggi` session:
   all four open and read normally, while the originals under `runs/…/out/` still raise
   `PermissionError` — which is ISS-13 itself, reproduced once more.

   Content identity against `runs/…/current/final_package.json` is **verified**: CV profile text, CV
   bullet text, the letter's mission paragraph and the `var rapportert i bruk om lag 2,5 år senere`
   hedge all appear in the rendered documents. Formatting identity is verified too — the CV's run
   sizes are exactly the master's inline values `{8.5, 9.0, 9.5, 10.0, 24.5}`, the letter's body runs
   inherit from `styles.xml`, both files have zero residual SDTs and no placeholders.

   **Caveat, stated rather than glossed:** byte-identity to the originals cannot be proven from a
   `veggi` session, because the originals are unreadable there. Content and formatting identity are
   proven and are what B0 is for. If byte-identity is wanted, a session running as
   `vhaala\CodexSandboxOnline` can hash both sides.

   Copy these four files into `pre_0.9.2/b0/` so the snapshot is self-contained, and record their
   hashes. **Do not modify the pilot run, do not take ownership, do not force access.**

### 9.1 Fallback — Run A0 · *not required, retained for completeness*

B0 is present (§9 step 3), so **this fallback is not part of the planned sequence.** It applies only
if the `test-run output/` copies are found to be missing, truncated or not the pilot's output. In that
case, produce the "before" side by replaying the pilot semantics against the **unchanged** masters,
before step 5:

Freeze a run with cluster `verify_a0` over the same two vacancies, replay the semantic fields (§9.2),
`finalize`, `render`, and export the PDFs. Because this happens after step 2, the code changes are
already in — so B0 and A1 still differ only in masters and baseline. Policy differs too, but policy is
inert in a replay because no model runs.

This costs one extra run and works for any identity.

### 9.2 The replay recipe (A0 and A1)

Pilot artifacts **cannot be copied verbatim** — they carry a `binding` pinned to the pilot manifest,
strategy and draft hashes, plus a `finalization` block, and the stage instructions forbid returning
those. Project only the semantic fields through fresh handoffs, stripping exactly the keys in
`artifacts.MECHANICAL_FIELDS`:

| Artifact | Strip; submit everything else |
|---|---|
| `strategy` | `artifact_role`, `authority`, `elasticity`, `final_writer_may_reconstruct`, `source_escape_permitted`, `binding` |
| `draft_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `final_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `review` | `artifact_role`, `binding` |

Per job, in stage order: `jobbsok freeze` (`--reviewed-by "Vegard Håland"`, only after a genuine human
attestation) → `jobbsok context --stage N` → project the pilot artifact minus its mechanical keys into
`write.return_paths` → run the emitted `submission.command` **verbatim** → repeat for stages 2 and 3
(`final_package` + `review` together) → `finalize` → `render`.

**No model calls.** `used_evidence_refs` resolve because `evidence_index.json` is byte-identical.
The replay **deliberately re-injects the pilot's known semantic defects**; holding content constant is
the point. A1 verifies typography, punctuation and access — **not** outcomes B, C or E.

---

## 10. Rollback and stop conditions

**Rollback:** restore from `pre_0.9.2/source_tree/`. For the masters restore the snapshot copies —
`prepare_masters` is idempotent forward, not backward. Verification runs are additive; nothing reads
them.

**Hard stops — do not work around:**

1. `prepare_masters` reports the control contract changed (≠ 17 CV / 7 letter).
2. Either master fails to **open in Word**. Parsing is not opening: the P0.7 masters parsed in
   LibreOffice while Word rejected them. This is the highest-risk check in the pass.
3. `preflight` fails after step 5 — D3 and D4 disagree. Fix them; never relax the assertion.

**Stop and escalate:**

- the suite does not reach 251/0/0 after step 1;
- `index verify` fails;
- the CV renders to 3+ pages and compression cannot reach 2 without dropping decision-relevant
  content — escalate rather than reducing type size;
- Run B is worse than the pilot on truth, tailoring or the Avinor regression guard — soften
  `FORFATTERSTEMME.md`, do not revert the set;
- Run B triage shifts to `CHECK` on both jobs — the new rules made the model defensive; that is a
  finding, not a pass;
- any change appears to need an architecture amendment — escalate against the exact governing ID with
  target-machine evidence. Never resolve by silent deviation.

---

## 11. Scope gate

Confirm before declaring done: the changed-file list matches §1 exactly, and every row below holds.

| Axis | Budget | Expected |
|---|---|---|
| new dependencies | 0 | 0 |
| new commands / flags | 0 | 0 |
| schema edits | 0 | 0 |
| new runtime modules | 0 | 0 |
| new status fields / state axes | 0 | 0 |
| architecture edits | 0 | 0 |
| new control-plane files | 1 | 1 (`FORFATTERSTEMME.md`) |
| edited runtime modules | 4 | 4 (`render.py`, `atomicio.py`, `leakage.py`, `tools/prepare_masters.py`) |
| regenerated binaries | 2 | 2 |
| new tests | 5 | 5 |
| manifest paths snapshotted | 22 | 22 (one recorded `ABSENT`) |
| **expected final diffs** | **21** | 21, including `BUILDER_REPORT.md` |
| new files | 1 | 1 (`FORFATTERSTEMME.md`) |
| `generated/evidence_index.json` | rewritten, **byte-identical** | not a diff |

Also confirm none of Contract §22's prohibited redesigns appears: no `letter_required`, no core
branching, no event sourcing, no progress markers, no RERUN subsystem, no automatic model
orchestration or retry, no hard semantic limits, no cross-job personality memory, no convergence
detector, no PDF-failure-as-semantic-failure, no numeric quality judge, no approval abstraction, no
migration shim.

---

## 12. Architecture verdict

**No normative amendment is required.** Unchanged from `01_…md`, with one mechanism correction:

- **A1, A2, D4** — Spec §22.2 grants *"template layout changes proven by target-machine gates"*;
  `DEC-24` already treats typography as an editorial signal. Discharged by `GATE-05`/`GATE-06`
  evidence from A1.
- **A3, C1, D5** — refinements of existing named sections in the canonical Norwegian source; Spec §4.5
  classes writing guidance as advisory control plane. **B adds no doctrine text at all.**
- **B1–B3, C2, E2** — stage-responsibility clarifications. No stage gains or loses an artifact, an
  authority or a write permission; `INV-09` untouched; no schema change.
- **E1** — a writing rule in the control plane (Contract §3), carrying no facets, facet IDs, typology
  or trait claims, so Spec §10 and Contract §12/§22 are untouched. `frozen_inputs.writing_policy` is
  an unbounded globbed array, so no schema, code or manifest change. `branch.CONTENT_GOVERNING`
  already declares writing policy content-governing for all four artifacts, which is why
  `policy/writing/` is the correct home and `context/` would be an integrity regression.
- **D1, D2, F1, F2** — implementation and test corrections. F1 *increases* conformance with `DEC-21`
  step 6 (*"write to a temporary **job** path"*) and preserves `promote_file`, `ACC-17` no-clobber and
  rollback privacy.

**Frozen-run semantics:** existing runs keep their frozen inputs; `render_job` refuses to render when
a live master no longer matches its frozen record. The pilot therefore cannot be re-rendered with the
new typography **by design**, which is why verification needs a new run.
