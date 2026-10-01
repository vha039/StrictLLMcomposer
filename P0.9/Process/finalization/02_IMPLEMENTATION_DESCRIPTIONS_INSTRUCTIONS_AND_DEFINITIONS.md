# 02 — Implementation descriptions, instructions and definitions

**Status:** planning material. Not authority.
**Purpose:** leave the implementing agent with no design decisions. Every file, function, style,
anchor, string and test is named here.

Prerequisite reading: `01_CHANGE_ARCHITECTURE_SPECIFICATION.md` for why none of this needs an
amendment; `03_…md` for the causal justification of each change; `04_…md` for the evidence.

---

## 0. Ground rules for the implementation pass

1. **There is no `.git` in this checkout.** Git commit and `git diff` are impossible. Before touching
   anything, write a SHA-256 registry of the 21-path target set, recording `ABSENT` for the new
   `FORFATTERSTEMME.md`; copy the 20 existing files and current `PILOT_LOG.csv`, preserving relative
   paths, to `P0.9/Process/finalization_snapshots/pre_0.9.2/source_tree/`. Put the four ordinary
   (non-security-preserving) pilot DOCX copies in the sibling `b0/` directory. The snapshot root must
   not already exist; never overwrite a prior snapshot. Compare afterwards with
   `git diff --no-index`. Any instruction that says
   "commit per change" is wrong here.
2. **Use scratch paths outside `P0.9/Build/` for `--basetemp` and destructive work.** Do not inventory
   `.venv/`, `__pycache__/`, `.pytest_cache/`.
3. **Do not use the retained pilot run for anything destructive.** `r20260828-213932-7f13b4` is
   evidence and is preserved unchanged.
4. **Verify paths with `Path(...).is_file()`, not by reading piped CLI output** — the build root
   contains a non-ASCII character and a shell pipe can mangle it.
5. **Word COM availability is session-dependent.** A COM failure is a session fact, not a converter
   defect. Do not change converter code because one context could not activate Word. Skips are not
   passes; name them.
6. **Order matters.** §8 gives the sequence and the reason for each dependency.

---

## 1. File manifest — the complete change surface

Twenty-one repository files change, plus human-written pilot-log data after Run B. Two files are
regenerated binaries. `generated/evidence_index.json` is rewritten by `index build` but must remain
byte-identical, so it is a verification by-product rather than a changed file.

| # | File | Changes | Kind |
|---|---|---|---|
| 1 | `policy/writing/WRITING_DOCTRINE.md` | A3, D5 | edit |
| 2 | `policy/writing/PERSUASION_CALIBRATION.md` | C1 | edit |
| 3 | `policy/writing/FORFATTERSTEMME.md` | E1 | **new** |
| 4 | `policy/stages/stage1_decision_architecture.md` | B1, B3, C2 | edit |
| 5 | `policy/stages/stage2_package_writer.md` | E2 boundary sentence | edit |
| 6 | `policy/stages/stage3_final_writer_review.md` | B2, C2, E2 | edit |
| 7 | `policy/RUNBOOK.md` | pilot-log line | edit |
| 8 | `authorities/CV_BASELINE.md` | D3 | edit |
| 9 | `generated/baseline_map.json` | D3 | **regenerated** |
| 10 | `generated/evidence_index.json` | — | verification rewrite; **byte-identical, not a final diff** |
| 11 | `templates/CV_MASTER.docx` | A1, A2, D4 | **regenerated binary** |
| 12 | `templates/APPLICATION_MASTER.docx` | A1, A2, D4 | **regenerated binary** |
| 13 | `runtime/tools/prepare_masters.py` | A1, A2, D4 machinery | edit |
| 14 | `runtime/jobbsok/render.py` | D1, D2, F1 | edit |
| 15 | `runtime/jobbsok/leakage.py` | D4 (one string) | edit |
| 16 | `runtime/jobbsok/atomicio.py` | F1 inheritance-preserving transaction option | edit |
| 17 | `runtime/tests/conftest.py` | F2 helper | edit |
| 18 | `runtime/tests/test_t05_t08_ownership_schema_failure.py` | F2 | edit |
| 19 | `runtime/tests/test_t19_t23_render_security.py` | new tests | edit |
| 20 | `runtime/tests/test_t16_t18_containment_template.py` | new tests | edit |
| 21 | `pyproject.toml` | package version | edit |
| 22 | `BUILDER_REPORT.md` | implementation/test ledger | edit |
| — | `pilot/PILOT_LOG.csv` | two rows after Run B | data |

**Must not change:** `P0.9/Architecture/*`; any `schemas/*.json`; `templates/template_map.json`;
`policy/settings.toml`; `authorities/Work_experience.md`, `Education.md`,
`Other_high_value_information.md`; `context/PERSONALITY_PROFILE.md`; `policy/personality_facets.json`;
`runtime/jobbsok/{artifacts,status,manifest,branch,merge,docxfill,pdf,schemas,paths,validate,
failure,baseline,evidence_index,batchinput,vacancy,hashing,ioenc,errors,cli}.py`; the retained pilot
run; `evidence/gates/GATE-02/original_p07_masters/`.

Version discipline: bump the `version:` frontmatter of every changed control-plane file to `0.9.2` and
`pyproject.toml` to `0.9.2`. `SPEC_REVISION`, `SCHEMA_REVISION`, the `manifest.schema.json` consts and
`policy/settings.toml [spec]` all stay `0.9.0`.

---

## 2. A — Typography

### 2.1 Why the master, and why `prepare_masters`

`docxfill.fill_block` deep-copies the template paragraph inside each SDT, and
`docxfill._set_paragraph_text` deep-copies the **template run including its `w:rPr`**. Generated
paragraphs therefore inherit the master's **inline `w:sz`**. For `CV_MASTER.docx` the `styles.xml`
sizes are effectively inert — every paragraph carries an inline size. For `APPLICATION_MASTER.docx`
the opposite holds: `APPLICATION_BODY` and the signature line have **no** inline size and take
`styles.xml Normal`.

`prepare_masters.py` is the only auditable route to a master edit in a repository with no version
control. It already reorders `w:pPr`/`w:rPr` for ECMA-376 validity, retargets absent fonts to Calibri,
removed the P0.7 forced page break, and **verifies the control contract before writing**. The
typography table joins it as a fourth transform.

### 2.2 The table must be position-keyed, not value-keyed

A value map (`9.0 → 12`, `10.0 → 12`) is **not idempotent**: after one run the document contains 10
and 12, and a second run would fire again. Key the table by **SDT tag** for the 24 controls and by
**normalized text anchor** for static furniture, and set an absolute target. Setting a value to N
twice is a no-op.

Refuse to write if an anchor does not match, using the same pattern as the existing control-contract
refusal.

### 2.3 The five tiers

| Tier | pt | half-points | Role |
|---|---|---|---|
| T1 | 24 | 48 | candidate name |
| T2 | 14 | 28 | section headings and the CV functional identity |
| T3 | 12 | 24 | substantive body prose and record title lines; letter body |
| T4 | 10 | 20 | deliberately subordinate content and metadata |
| T5 | 8 | 16 | running header and footer — **unchanged** |

Resulting size set across both masters: `{8, 10, 12, 14, 24}`. No half-points.

### 2.4 `CV_MASTER.docx` — `word/document.xml`, all 35 body paragraphs

`w:szCs` is absent throughout both masters; set `w:sz` only, and do not add `w:szCs`.

| ¶ | Anchor | Now | → | Bold / colour |
|---|---|---|---|---|
| 1 | text `VEGARD HÅLAND` | 24.5 | **24** | keep `b`, `caps`, `17324D` |
| 2 | SDT `CV_FUNCTIONAL_IDENTITY` | 10.0 | **14** | keep `b`, `caps`, `0F6B73` |
| 3 | SDT `CV_VALUE_PROPOSITION` | 9.0 | **12** | unchanged (control is `source: none`, renders empty) |
| 4 | text starting `Oslo  |  +47` | 8.5 | **10** | unchanged (`5B6570`, not bold) |
| 5 | `Heading1` text `Profil` | 10.0 | **14** | keep `b`, `caps`, `0F6B73` |
| 6 | SDT `CV_PROFILE` | 9.0 | **12** | unchanged |
| 7 | SDT `CV_CORE_COMPETENCE` | 9.0 | **12** | unchanged |
| 8 | SDT `CV_TOOLS_METHODS` | 9.0 | **12** | unchanged (inert control) |
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

**The bold/colour change applies to exactly two paragraphs: 23 and 31.** These are *content* zones
that inherited *record-title* run properties (ISS-04). Paragraphs 10, 11, 15, 18, 20 and 22 are
genuine record lines: their bold and colour are correct design and **must not** be touched.

`word/header1.xml`, `word/footer1.xml`, `word/footer2.xml`: **unchanged**, 8 pt.

### 2.5 `APPLICATION_MASTER.docx` — `word/document.xml`, all 8 body paragraphs

| ¶ | Anchor | Now | → |
|---|---|---|---|
| 1 | SDT `APP_EMPLOYER` (inline run) | 8.5 | **10** |
| 2 | SDT `APP_UNIT_OPTIONAL` | 8.5 | **10** |
| 3 | text `Oslo, ` + SDT `APP_DATE` | 8.5 | **10** |
| 4 | text `Stilling: ` + SDT `APP_JOB_TITLE` (1st) | 8.5 | **10** |
| 5 | SDT `APP_REFERENCE_OPTIONAL` | 8.5 | **10** |
| 6 | `Title` text `Søknad – ` + SDT `APP_JOB_TITLE` (2nd) | style 20 | **20, unchanged** — but see D4 for the dash |
| 7 | SDT `APPLICATION_BODY` | style `Normal` | **via `styles.xml`** |
| 8 | text `Med vennlig hilsen` / `Vegard Håland` | style `Normal` | **via `styles.xml`** |

### 2.6 `styles.xml`

| Master | Style | `w:sz` now | → | Load-bearing? |
|---|---|---|---|---|
| CV | `Normal` | 18 | **24** | No — every CV paragraph has an inline size. Changed **defensively**, so a future paragraph without an override renders at 12, not 9. |
| CV | `ListBullet` | 18 | **24** | Same; defensive. |
| CV | `Heading1` | 20 | **28** | Same; defensive. |
| Letter | `Normal` | 21 | **24** | **Yes.** `APPLICATION_BODY` and the signature have no inline size. This is the change that moves the letter body to 12 pt. |

`Heading2`, `Heading3`, `BodyText*`, `List*`, `Quote`, `MacroText`, `Caption`, `Title` and every
character style are **latent Word boilerplate applied by no paragraph** in either master. Leave them
alone; changing unused styles widens the diff for no rendered effect. (`Title` **is** applied — one
paragraph in the letter — and stays at 20.)

### 2.7 Spacing: deliberately unchanged

Do **not** alter `w:spacing` or `w:line` in this pass. The modelled result at the tier scale is
≈1.5 pages for the CV and ≈0.7 for the letter, so it is not needed, and every spacing change costs
page budget. At `w:line="252"` (1.05) a 12 pt Calibri line is tight but legible.

If the B0/A1 visual review (§9) judges the body cramped, a **single canonical `w:line` adjustment in
both masters** is a sanctioned follow-up under A3 — measured, not speculative. Record it as a separate
change if it happens.

### 2.8 Page-count model — a model, not a measurement

CV text area 17.9 × 27.0 cm ⇒ ≈765 pt per page. At the tier scale the pilot CV content models to
≈1150 pt ⇒ **≈1.5 pages**, i.e. a genuine two-page CV with page 2 roughly half full. At the current
9 pt scale the same content models to ≈1.2 pages, which is why page 2 is nearly empty today (ISS-16).

Letter text area 17.0 × 26.3 cm ⇒ ≈745 pt per page; the pilot letter models to ≈520 pt ⇒ **≈0.70
page**, before the space reclaimed by removing the ceremonial motivation paragraph.

**These numbers are estimates and must be replaced by the Run A1 measurement.** Decision rule if the
CV renders to 3 pages: apply A3 (editorial compression) — **never** reduce type size. `DEC-24` forbids
deleting decision-relevant content to satisfy a page rule; compression means tightening prose and
prioritising competencies, not dropping evidence.

---

## 3. B, C, D5 — canonical policy treatment and verbatim text

Insert exactly as written where an insertion is specified. All of it is Norwegian, in the canonical
files, with no English rubric added anywhere.

### 3.1 A3 — `WRITING_DOCTRINE.md § Myke redaksjonelle utgangspunkt`

Append after the existing bullet list and the "Et dokument feiler mekanisk bare når…" sentence:

> Sidemål nås ved redaksjonell komprimering, aldri ved å krympe brødteksten. En stage skal aldri bytte
> skriftstørrelse eller linjeavstand mot plass i en enkelt pakke; typografi er ikke en variabel i det
> semantiske arbeidet. Malenes typografi og avstander settes én gang, av mennesket, i masterfilene, og
> er like for alle jobber. Når et dokument blir for langt, komprimer eller prioriter innhold. Mindre
> skrift er forbeholdt bevisst underordnet informasjon: kontaktlinje, enhets- og periodelinjer,
> fagdetaljer, støtteseksjoner og løpende topp-/bunntekst. Sidetall er fortsatt et redaksjonelt
> signal, ikke en valideringsgrense (`DEC-24`).

### 3.2 B — existing doctrine is sufficient; change routing, not policy

Do **not** edit `WRITING_DOCTRINE.md § Begrunnet motivasjon` or
`§ Arbeidsgiverbyttetesten` for outcome B. The existing Norwegian text already requires motivation to
come from the work and explicitly says not to repair specificity with slogans, copied values or
unfounded employer praise. The pilot failure was Stage-1 routing and Stage-3 salience: neither stage
was required to apply `Begrunnet motivasjon` to the field/text it controlled, and Stage 3 rewarded a
mission clause while applying the swap test. B1 and B2 below fix those two control failures without a
second formulation of the same rule.

### 3.3 D5 — `WRITING_DOCTRINE.md`, new `# Tegnsetting` section

Place it immediately before `# Tjuesekunderstesten`:

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

Keep the two existing bullets. Append:

> - Ikke bær kildefilenes dokumentasjonsstemme inn i kandidatens egen tekst. Når myndigheten sier at
>   kandidaten «oppgir X», er X kandidatens egen opplysning og kan sies direkte av ham. Bevar reelle
>   grenser som omtrentlighet, observasjonstidspunkt, lifecycle-tilstand og fravær av måling; fjern
>   bare avstanden som oppstår fordi kilden er skrevet *om* kandidaten. Kjent sannhet skal låte kjent.

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

This is the **only** change to Stage 2, and it exists because the file genuinely reaches Stage 2
through `read.writing_policy` and is already declared content-governing for `draft_package` in
`branch.CONTENT_GOVERNING`. Saying nothing would leave an unexplained candidate-specific file in
Stage 2's read block.

### 4.3 B2 + C2 + E2 — `stage3_final_writer_review.md`

**(a)** In `## Read order`, replace the paragraph beginning `The context's \`read.writing_policy\`
supplies` with:

> The context's `read.writing_policy` supplies `policy/writing/WRITING_DOCTRINE.md`,
> `policy/writing/PERSUASION_CALIBRATION.md` and `policy/writing/FORFATTERSTEMME.md`. Before choosing
> triage, apply these named sections: `Tjuesekunderstesten`, `Arbeidsgiverbyttetesten`, `Begrunnet
> motivasjon`, `Rolig faglig tyngde`, `Tegnsetting`, `TOO_WEAK` and `UNNATURAL_NORWEGIAN`. Repair,
> rather than merely report, what they expose. Language rejected under `Begrunnet motivasjon` cannot
> be cited as evidence that `Arbeidsgiverbyttetesten` is passed.
>
> Before reading the strategy and draft, form an independent thesis and decide the likely opening,
> evidence order and employer register from the vacancy and candidate evidence. Then read upstream as
> an evidence inventory and hypothesis, not as a prose or structure template.
>
> `FORFATTERSTEMME.md` is the candidate's professional author voice. Apply it **after** you have
> grounded the package and decided what it should say. It governs expression only, and can never
> create or remove a proposition, move a claim ceiling, change a lifecycle state or qualification, or
> select evidence. You are this package's author, not its proof-reader.

**(b)** In `## What you may not change`, extend the existing bold sentence:

> **A known unsupported or inflated upstream claim must be repaired before you save the final. It must
> never ship under `CHECK`.** The duty is symmetric: a known **material understatement** of an
> established fact is equally yours to repair. See `PERSUASION_CALIBRATION.md § TOO_WEAK`.

### 4.4 `policy/RUNBOOK.md`

In the per-vacancy loop, immediately after the step where the human reviews the rendered package, add
one line:

> Append one row to `pilot/PILOT_LOG.csv` for the job: triage, actual repair scope, submit-ready,
> factual corrections, minutes through the submission decision, render issues, friction and outcome.
> The columns already exist; this is a hand-written row, and it is the only record of what the package
> actually cost you (Spec §18.3, `ACC-20`).

---

## 5. E1 — `policy/writing/FORFATTERSTEMME.md`

New file. Norwegian. Derived from `PERSONALITY_PROFILE.md` §1 (canonical runtime compression) and §6
(communication and collaboration guidance), plus the anti-patterns
reproduced from the pilot output. **Vegard reviews and corrects it before Run B.**

It contains no facets, no facet IDs, no typology labels and no trait claims, so it does not touch the
personality interface (Spec §10, Contract §12) — see `01_…md` §5.

```markdown
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
Vis moderat varme gjennom den konkrete, allerede evidensstøttede nytten argumentet
viser for mottakeren, ikke gjennom ros, smiger eller påtatt entusiasme.

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
forekommer (Spec 10.3, `INV-07`).

1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …`
   som avslutning. Avslutt heller med noe som bare gjelder denne stillingen.
2. `Når <arbeidsgiver> skal <X>, må <Y> …` som standardåpning. En åpning som
   bare refererer arbeidsgiverens egen situasjon tilbake til dem, bruker den
   viktigste setningen i brevet på noe leseren allerede vet.
3. En fast åpning–to bevis–motivasjon–avslutning-form eller speilvendte
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
```

---

## 6. D — punctuation, code and assets

### 6.1 D1 — `render.py`, `resolve_control`, `effective.previous_employments`

Line 179 currently:

```python
lines.append(f"{line} — {summary}" if summary else line)
```

Replace with:

```python
lines.append(f"{line}. {summary}" if summary else line)
```

The line already uses `|` for structure (`period | title, employer, unit`), so a period is the natural
divider. Do **not** use a hyphen — that reintroduces exactly the clause-dividing hyphen outcome D
prohibits. Do not touch the `·` competency separator or the `•` bullet separator on the same code path.

### 6.2 D2 — `render.py`, `_build_document`, line 832

```python
title=f"{spec['output_stem']} – {effective['candidate']['full_name']} – {job['title']}",
```

Replace both en dashes with `|`:

```python
title=f"{spec['output_stem']} | {effective['candidate']['full_name']} | {job['title']}",
```

This is `docProps` metadata rather than page content, but it ships inside the employer-facing file.

### 6.3 D3 — `authorities/CV_BASELINE.md`

Sixteen edits inside the single fenced JSON block between `<!-- CV_BASELINE_DATA_START -->` and
`<!-- CV_BASELINE_DATA_END -->`. Line numbers are as of the current file.

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
| 202–204 | trust items | `10.2017–01.2019`, `01.2019–01.2020`, `01.2020–08.2020` | hyphens |

**Do not change lines 88, 102, 116 and 130.** Those are `authority_anchor` values —
`baseline_map.schema.json` records them as *"Inert human-readable note … NOT resolvable as a factual
evidence reference"*, `baseline.py` copies them to an inert `baseline_provenance` field, they never
render, and two of them (`July 2015–August 2021`, `February–April 2015`) are verbatim cross-references
to strings in `Work_experience.md`. Changing them would break a human cross-reference for zero
employer-facing gain.

The unit names take a **comma**, not a hyphen: `Direktørens stab - Analyseavdelingen` would be a
clause-dividing hyphen, which the same outcome prohibits.

Then regenerate and prove:

```bash
.\.venv\Scripts\jobbsok.exe index build
.\.venv\Scripts\jobbsok.exe index verify
```

`index build` rewrites both `generated/evidence_index.json` and `generated/baseline_map.json`. The
three authorities are unchanged, so `evidence_index.json` regenerates byte-identical; only
`baseline_map.json` changes content. `index verify` asserts byte-identical regeneration from the same
inputs and is a free correctness proof.

### 6.4 D4 — master static furniture, in the same `prepare_masters` pass

The masters duplicate baseline values as static furniture, and `render.preflight_templates` compares
them through `static_baseline_assertions`. **D3 and D4 must land together or preflight fails.**

`CV_MASTER.docx` — 8 en dashes in `word/document.xml`, all mirroring D3:

- `03.2023–d.d.` → `03.2023-d.d.` (¶10)
- `Direktørens stab – Analyseavdelingen` → `Direktørens stab, Analyseavdelingen` (¶11)
- `12.2023–d.d.` → `12.2023-d.d.` (¶11)
- `Barne- og ungdomsklinikken – Stab` → `Barne- og ungdomsklinikken, Stab` (¶15)
- `03.2023–11.2023` → `03.2023-11.2023` (¶15)
- `2024–d.d.` → `2024-d.d.` (¶18)
- `2020–2022` → `2020-2022` (¶20)
- `2017–2020` → `2017-2020` (¶22)

`APPLICATION_MASTER.docx` — 1 en dash: `Søknad – ` → `Søknad: ` (¶6, the `Title` paragraph).

`runtime/jobbsok/leakage.py` line 98, in `KNOWN_GOOD_PHRASES`:

```python
"Direktørens stab – Analyseavdelingen",   ->   "Direktørens stab, Analyseavdelingen",
```

Verified safe: no JSON-schema `pattern` and no runtime regex depends on the en dash; `leakage.py:98`
and `render.py:832` are the only two code references.

### 6.5 F1 — accessible, atomic render staging

Moving the existing `tempfile.mkdtemp()` under the job directory is **not** a fix. This checkout runs
Python 3.14.3, and `mkdtemp()` calls `os.mkdir(..., 0o700)`; on current Windows that deliberately
creates a protected, creator-only DACL. A same-volume `os.replace` then carries that descriptor into
`out/`. The current pilot files show exactly that protected descriptor, while their parent `out/`
directory has ordinary inherited access including `vhaala\veggi`.

Make the existing abstraction explicit instead of adding ACL-reset code. In
`runtime/jobbsok/atomicio.py`:

1. import `secrets`;
2. add `inherit_parent_permissions: bool = False` to `TransactionDir.__init__` and store it;
3. keep the current `tempfile.mkdtemp()` path unchanged when the flag is false;
4. when true, try up to 100 names of the form `.{prefix}.{secrets.token_hex(4)}` and create the first
   free path with `Path.mkdir(mode=0o777)`. On Windows, using a mode other than the special `0o700`
   preserves normal parent-DACL inheritance; on POSIX the process umask still applies;
5. raise `FileExistsError` if all 100 collision attempts fail;
6. keep `__exit__` unchanged.

The resulting constructor and entry method are exactly:

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

The default must remain private because `cli.py` uses `TransactionDir` for rollback snapshots. Only
the employer-facing render workspace opts into inherited permissions.

In `render_job`, replace:

```python
with TransactionDir(
    Path(tempfile.gettempdir()), prefix=f"jb-{job_id[:16]}"
) as workspace:
```

with a sibling staging directory under the actual output directory:

```python
with TransactionDir(
    out_dir, prefix="rnd", inherit_parent_permissions=True
) as workspace:
```

Notes for the implementer:

- Canonical `out_dir` is already checked with `assert_writable`; `--dest` is resolved and authorized by
  the existing export path. Do not change either check.
- Staging beside the destination preserves same-volume atomic rename and inherits the **destination's**
  access policy. It also removes the latent cross-volume failure in export mode.
- `.rnd.<8 hex>` adds only a short path segment. Keep the prefix short; do not use the job id.
- `tempfile` becomes unused in `render.py`; remove that import there. It remains used in `atomicio.py`
  and `cli.py`.
- A killed process can leave a hidden `.rnd.*` directory in `out/`; this is preferable to silently
  publishing inaccessible files, and the existing context manager removes it on ordinary exit.
- `pdf.convert` keeps its own `%TEMP%` working directory (`.wordcom_*`). That is untouched — the PDF
  is written next to the staged DOCX in the workspace and promoted from there.

Do not reset ACLs after promotion and do not switch to a non-atomic direct copy. The target-machine
acceptance check must inspect the staging/output DACL and then open the promoted DOCX as the human.

### 6.6 F2 — fixture-owned role mapping

In `runtime/tests/conftest.py`, add `import re` with the standard-library imports, then add:

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

- `test_t05_public_handoff_completes_all_stages_and_review_only` — call
  `set_role_mapping(layout, sol="synthetic-sol", terra="synthetic-terra")` before `freeze`, and
  **replace** `assert stage1["configured_model"] is None` with
  `assert stage1["configured_model"] == "synthetic-sol"`. This is stronger than the assertion it
  replaces: it proves the configured mapping actually flows through the public handoff, which the
  `is None` check never did.
- `test_t05_context_exposes_configured_capability_surface` — replace the literal
  `.replace('SOL_CLASS = ""', …)` with `set_role_mapping(...)`, then keep the existing
  `assert context["configured_model"] == "synthetic-sol-surface"` against whatever value the helper
  was given.

Both tests must then pass with the production mapping populated **and** with it blank. Do not touch
`policy/settings.toml`, runtime behaviour, the schema or the GATE-10 evidence.

---

## 7. Tests

`test_traceability.py` requires every Tier-1 item and mechanical `ACC` id to name a real test by
`test_tNN_` prefix, so new tests keep the owning file's prefix.

| # | File | Test | Asserts |
|---|---|---|---|
| T1 | `test_t16_t18_containment_template.py` | `test_t16_master_typography_uses_the_discrete_scale` | every `w:sz` in both masters' `word/document.xml` is in `{16, 20, 24, 28, 48}` half-points, and `styles.xml Normal` is 24 in both |
| T2 | `test_t16_t18_containment_template.py` | `test_t16_subordinate_zones_are_not_title_formatted` | the paragraphs inside `CV_RELEVANT_BACHELOR_SUBJECTS` and `CV_OPTIONAL_PREVIOUS_EXPERIENCE` (content paragraph) carry no `w:b` and no `w:color` override |
| T3 | `test_t16_t18_containment_template.py` | `test_t16_masters_and_baseline_contain_no_en_or_em_dash` | zero `–`/`—` in either master's `w:t` text and in every rendered value of `baseline_map.json` except `baseline_provenance` |
| T4 | `test_t19_t23_render_security.py` | `test_t19_previous_employment_line_uses_plain_punctuation` | the rendered TIDLIGERE ERFARING lines contain no em dash |
| T5 | `test_t19_t23_render_security.py` | `test_t19_render_stages_beside_destination_with_inherited_permissions` | render requests an inheritance-preserving transaction under `out_dir`; the workspace is removed afterwards. Target-machine DACL/openability remains a human acceptance gate, not a portable assertion. |

An ACL assertion is deliberately **not** a test: it is not portable across machines and users. ISS-13
is verified by the Run A1 target-DACL and human-open step in §9.

**Test arithmetic — state it, do not restate "251".**

| Point | Word COM | No COM |
|---|---|---|
| Now (251 tests, 2 failing) | 249 passed / 2 failed / 0 skipped | 239 passed / 2 failed / 10 skipped |
| After F2 only | **251 / 0 / 0** | 241 passed / 10 skipped |
| After the full change set (**+5**) | **256 / 0 / 0** | 246 passed / 10 skipped |

If a planned test proves redundant with existing coverage, drop it and **adjust the arithmetic
explicitly** in `BUILDER_REPORT.md`. Skips are not passes; name each one.

---

## 8. Implementation order

Dependencies are real; this order is not a preference.

| Step | Work | Why here |
|---|---|---|
| 0 | SHA-256 registry of the 21-path target set (`ABSENT` for new E1) + scratch copies of the 20 existing targets and current `PILOT_LOG.csv`; hash-equal accessible copies of the four pilot DOCX → **B0** | no `.git`; this is the rollback and the old-typography visual baseline |
| 1 | **F2** and its verification | bounded, independently reproduced, and every later gate needs a green suite. Stop if the suite is not 251/0/0. |
| 2 | **D1, D2, F1** + tests T4, T5 | bounded runtime corrections; F1 must prove accessibility in A1 |
| 3 | **A3, B1, B2, B3, C1, C2, D5, E1, E2** + RUNBOOK + version bumps | complete the control plane before any new freeze |
| 4 | **D3** → `index build` → `index verify` | must precede D4 |
| 5 | **A1, A2, D4** via one writing `prepare_masters` run → one `--check` dry run → `preflight` → tests T1, T2, T3 | the dry run must report zero pending transforms, proving idempotence; D3 must already be present |
| 6 | projected **Run A1** — fresh handoffs, same semantic fields, finalize/render; human B0/A1 visual A/B and DACL/openability check | discharges A, deterministic/static D and `VISUAL_HUMAN`; first target proof of F1 |
| 7 | Full suite, adversarial set, `prepare_masters --check`, vertical slice, scope gate | mechanical acceptance |
| 8 | **Run B** — fresh Stage 1/2/3 under the new policies; human semantic review; two `PILOT_LOG.csv` rows | discharges B, C, semantic D and E |

`FORFATTERSTEMME.md` must be reviewed by Vegard before step 6 and again in the blind A/B after Run B.

---

## 9. The B0 snapshot and Run A1 replay procedure

Before implementation, copy the four pilot output DOCX into the external snapshot and verify each
copy's SHA-256 equals its source. The current sandbox owner can read those bytes; copy semantics give
the B0 copies ordinary snapshot-directory inheritance. Do not change or re-render the pilot.

The pilot semantic artifacts **cannot be submitted verbatim** to A1. They carry a `binding` pinned to the pilot manifest,
strategy and draft hashes, plus a `finalization` block; `stage-submit` stamps those from the current
handoff and the stage instructions say explicitly not to return them.

The correct replay is a **semantic-field projection through fresh handoffs**, using
`artifacts.MECHANICAL_FIELDS` to strip exactly the tool-owned keys:

| Artifact | Strip these keys; submit everything else |
|---|---|
| `strategy` | `artifact_role`, `authority`, `elasticity`, `final_writer_may_reconstruct`, `source_escape_permitted`, `binding` |
| `draft_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `final_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `review` | `artifact_role`, `binding` |

Procedure for A1, per job, in stage order:

1. `jobbsok freeze` a new run from a `batch_input.csv` naming the same two vacancies. Use cluster
   `verify_a1` so the operational run list stays readable. `--reviewed-by` records a
   genuine human attestation; use Vegard's name (it is a real freeze).
2. `jobbsok context --stage 1` → read `write.return_paths` and `write.semantic_fields`.
3. Project the pilot `strategy.json` minus its mechanical keys into the stage-1 return path.
4. Run the emitted `submission.command` verbatim.
5. Repeat for stage 2 (`draft_package`) and stage 3 (`final_package` + `review`).
6. `jobbsok finalize` then `jobbsok render`.

**No model calls.** `used_evidence_refs` resolve because `evidence_index.json` remains byte-identical.

Two things to state plainly rather than discover later:

- **A1 deliberately re-injects the known semantic defects** (the mission paragraph, the
  `rapportert i bruk` hedge and the clause hyphen). That is the point: content is held constant so
  typography and deterministic/static punctuation deltas are isolated. Run B, not A1, accepts the
  semantic outcomes.
- **A run's frozen manifest pins its masters**, and `render_job` raises `ConfigurationError` if a live
  master's hash differs from the frozen record. A1 therefore needs fresh bindings; B0 does not need a
  fresh run because it is a hash-equal copy of the already-rendered old-master output.

---

## 10. Verification commands

Run from `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build`.

```powershell
.\.venv\Scripts\python.exe -m pytest runtime\tests -q -p no:cacheprovider --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-full
```

```powershell
.\.venv\Scripts\python.exe -m pytest runtime\tests\test_t09_t12_state_evidence.py runtime\tests\test_t13_t15_merge_leakage_personality.py runtime\tests\test_t16_t18_containment_template.py runtime\tests\test_traceability.py -q -p no:cacheprovider --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-adversarial
```

```powershell
.\.venv\Scripts\python.exe -m tools.prepare_masters
```

```powershell
.\.venv\Scripts\python.exe -m tools.prepare_masters --check
```

```powershell
.\.venv\Scripts\jobbsok.exe index build
.\.venv\Scripts\jobbsok.exe index verify
```

```powershell
.\.venv\Scripts\jobbsok.exe preflight
```

```powershell
.\.venv\Scripts\python.exe -m tools.vertical_slice --out C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-evidence --workdir C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-work
```

Expected: full suite **256 / 0 / 0** with Word COM; adversarial set green; the writing
`prepare_masters` run preserves the 17/7 control contract, and the single following `--check` reports
0 reorders, 0 font retargets, 0 page-break removals, **0 typography and 0 dash normalizations**;
`index verify` PASS; `preflight` PASS; vertical slice PASS with 21 steps, 4 outputs and
`render overall : OK`.

---

## 11. Rollback and stop conditions

**Rollback.** Restore the affected files from the step-0 scratch snapshot. For the masters, restore
the snapshot copies rather than re-running `prepare_masters` — the tool is idempotent forward, not
backward. Runs `verify_a1` and `verify_b` are additive and can be left in place; nothing
reads them.

**Stop and escalate if:**

1. `prepare_masters --check` reports the control contract changed (17 CV / 7 letter) — the master edit
   is wrong; do not force it.
2. Either master fails to open in **Word** after the change. Parsing is not opening; the P0.7 masters
   parsed fine in LibreOffice while Word rejected them. This is the single highest-risk check.
3. `preflight` fails after step 6 — D3 and D4 are out of agreement; fix, do not relax the assertion.
4. `index verify` fails — the baseline edit broke byte-identical regeneration.
5. The suite does not reach 251/0/0 after step 1, before anything else lands.
6. Run A1 renders the CV to 3+ pages and the result is visually unbalanced or less usable. Try
   semantic compression first, then a canonical spacing/section-flow adjustment. If reaching 2 pages
   would drop decision-relevant content, accept the extra page and its advisory warning; never reduce
   main-prose type size.
7. Run B produces a package that is worse than the pilot on truth, tailoring or the §1.7 regression
   guard. Soften `FORFATTERSTEMME.md` rather than reverting the whole change set.

**Final scope gate.** Before declaring done, confirm no new dependency, command, parser branch,
schema, runtime module, status field, state axis, authority, client, automatic retry, approval
abstraction, hard threshold or architecture edit was introduced, and that the changed-file list
matches §1 exactly.
