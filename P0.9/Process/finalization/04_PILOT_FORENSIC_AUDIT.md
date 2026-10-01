# 04 — Pilot forensic audit

**Status:** planning material. Not authority.
**Run:** `r20260828-213932-7f13b4` · cluster `pilot_live_smoke` · frozen `2026-08-28T21:39:32Z`
**Jobs:** `huseierne_strategi_maalstyring` (seq 1, HIGH), `avinor_digital_transformasjon` (seq 2, NORMAL)
**Method:** every claim below was reproduced from disk on 2026-08-31/2026-09-01. Quotes are verbatim
from the named artifact. Where a claim could not be reproduced it is marked **UNVERIFIED** with the
reason.

---

## 0. Reading this file

§1 establishes the run identity and what the freeze actually pinned. §2 is the stage-by-stage lineage
per job. §3 traces the four material defect chains through all three stages. §4 covers rendered
output, typography and environment. §5 is cross-job comparison. §6 is the limitations register — what
this audit could **not** see.

Issue IDs are defined in `03_ISSUE_REGISTRY_MITIGATION_AND_FIX_LOGIC.md`.

---

## 1. Run identity and what the freeze pinned

### 1.1 Manifest facts

| Field | Value |
|---|---|
| `run_id` | `r20260828-213932-7f13b4` |
| `parent_run_id` | none |
| `spec_revision` / `schema_revision` | `0.9.0` / `0.9.0` |
| `frozen_at` | `2026-08-28T21:39:32Z` |
| `baseline_reconciliation.reviewed_by` | `Vegard Håland` |
| `baseline_reconciliation.reviewed_at` | `2026-08-28` |
| `baseline_reconciliation.conflicts_known` | `[]` |
| frozen role mapping | `SOL_CLASS = "Codex / GPT-5.6 Sol"`, `TERRA_CLASS = "Codex / GPT-5.6 Terra"` |
| jobs | 2 CORE, 0 EXCEPTION, both `requires_source_inspection: true` |

`cluster` is per job, not top-level: both jobs carry `cluster: "pilot_live_smoke"`. Avinor carries
`deadline: "2026-09-13"`, Huseierne none. Both carry a `unit`; neither carries a `reference`.

### 1.2 The pilot ran the current policy — verified by hash across all 15 frozen inputs

Every entry in `manifest.frozen_inputs` was hashed against the live file. **All 15 are
byte-identical**, including both Word masters and the generated baseline map:

```
authorities/Work_experience.md                 SAME
authorities/Education.md                       SAME
authorities/Other_high_value_information.md    SAME
authorities/CV_BASELINE.md                     SAME
context/PERSONALITY_PROFILE.md                 SAME
policy/personality_facets.json                 SAME
policy/settings.toml                           SAME
policy/stages/stage1_decision_architecture.md  SAME
policy/stages/stage2_package_writer.md         SAME
policy/stages/stage3_final_writer_review.md    SAME
templates/CV_MASTER.docx                       SAME
templates/APPLICATION_MASTER.docx              SAME
templates/template_map.json                    SAME
generated/evidence_index.json                  SAME
generated/baseline_map.json                    SAME
```

`frozen_inputs.writing_policy` is a two-element array recording
`policy/writing/PERSUASION_CALIBRATION.md` (`b8155b3f…`, 3169 bytes) and
`policy/writing/WRITING_DOCTRINE.md` (`de4e4648…`, 12853 bytes), both matching live.

**Consequence, and it governs the whole analysis.** Stale-policy drift is ruled out. The pilot ran
with the Stage-3 writing-policy pointer, both named final tests, the calibrated `READY`, the Stage-1
and Stage-3 cross-job resets and the Stage-1 decision-density rule all present and in force. Every
defect below is therefore one of: **non-compliance with an in-force rule**, **a rule present but not
routed to the stage that needed it**, or **a genuine coverage gap**. Never "the policy was old". §3
classifies each defect into exactly one of those three.

### 1.3 What ran, mechanically

Both jobs reached `production_state: VALID`, `highest_valid_stage: FINAL`, `semantic_triage: READY`,
with current final+review bindings. `status.json` (derived `2026-08-29T08:46:37Z`) reports
`integrity.ok: true`, 0 mismatches, 0 stale, 0 failed, 0 blocked. Render is `DEGRADED` for both jobs:
both DOCX `OK`, all four PDFs `DEGRADED` with the diagnostic `Retrieving the COM class factory for
component with …` and `Word COM export returned exit code 1`. Document date `2026-08-29` for both;
`finalized_by` is `operator`.

---

## 2. Stage-by-stage lineage

### 2.1 Huseiernes Landsforbund — Strategi- og målstyringsrådgiver

**Vacancy.** Six-page scanned PDF, no extractable text, `requires_source_inspection: true`. This pass
rendered and visually inspected all six original pages and found no material conflict with the
derived vacancy identity, requirements or Stage-1 framing. Stage 1 recorded in `risk_notes`:
*"Originalkilden er en seks siders skannet jobbside og ble visuelt
inspisert; side 4-5 inneholder et personlig, KI-generert JobMatch-panel som må holdes utenfor
evidensgrunnlaget."* Both stages carried the exclusion into `avoid_guidance` and the review `notes`.
**Exemplary behaviour and an explicit non-target** — the system correctly refused to treat an
AI-generated match panel as employer or candidate evidence.

**Stage 1 — `strategy.json`.** Twenty material requirements (`R01`–`R20`) mapped
`SUPPORTED`/`ADJACENT`/`GAP`/`UNKNOWN`, no truncation. Two honest `GAP`s: the literal five-year
minimum (`R02`) and practical OKR experience (`R04`). Route: practical governance, shared method,
decision support and implementation. Four objections with reframes and honesty notes. Three
personality facets — `PF-01`, `PF-11`, `PF-08` — each with evidence refs, expression ceiling, misread
risk and guardrail. The strategy is decision-dense and the route is defensible. **Two of its fields
are the origin of downstream defects** (§3.1, §3.2).

**Stage 2 — `draft_package.json`.** Complete tailored CV and letter. Headline `Samfunnsøkonom og
rådgiver | styringsinformasjon, forbedring og gjennomføring`. Seven competencies. Letter: opening +
4 body paragraphs + closing. Paragraph 4 is an explicit gap disclosure:

> *"Jeg har ikke praktisk OKR-erfaring, og den dokumenterte relevante erfaringen min er kortere enn
> fem år. Jeg vil derfor ikke fremstå som en ferdig OKR-spesialist."*

**Stage 3 — `final_package.json` + `review.json`.** Triage `READY`. Six competencies, trimmed from
seven. `material_strategy_change` records: *"Stage 3 fjernet Stage-2-brevets defensive avsnitt om
manglende OKR-erfaring og kortere ansiennitet."* That removal was **correct** —
`PERSUASION_CALIBRATION § TOO_WEAK` forbids turning a non-disqualifying gap into defensive prose, and
the limitations were preserved in `review.known_limitations`.

Stage 3 also made three changes that were **not** improvements:

1. replaced Stage 2's plain opening with a consultant-form employer restatement (§3.3);
2. promoted the mission clause into a dedicated motivation paragraph (§3.1);
3. removed the word `fortsatt` from the framework claim (§3.2).

`upstream_claim_repaired` is `null` in both jobs. That is consistent with the evidence — no overclaim
was present. The gap is that the **opposite** direction, understatement, was neither detected nor
treated as repairable.

### 2.2 Avinor AS — Seniorrådgiver Digital Transformasjon

**Vacancy.** Also a six-page scanned PDF with the same JobMatch exclusion. This pass independently
rendered and inspected all six pages and found no material conflict with the derived vacancy or the
Stage-1 requirement framing.

**Stage 1.** Route: controlled digital change, benefit discipline, technology-to-business translation
in a regulated environment. Five objections, including security clearance handled correctly (*"Ikke
omtale klarering i arbeidsgiverteksten med mindre prosessen krever et direkte svar"*). Claim ceilings
preserved around enterprise portfolio and formal leadership. Facets `PF-19`, `PF-01`, `PF-11` — **a
materially different selection from Huseierne's**, direct evidence that the Stage-1 cross-job reset
worked at facet level.

**Stage 2.** Headline `Samfunnsøkonom og rådgiver | digitalisering, gevinst og kontrollert
gjennomføring`. Eight competencies. Paragraph 4 is again an explicit gap disclosure (*"Jeg har ikke
hatt ansvar for en konsernportefølje, et formelt transformasjonsprogram eller linjeledelse."*).
Paragraph 2 includes the STE proxy model, described accurately as *"et beslutningsdesign, ikke
dokumentasjon på realisert gevinst"*.

**Stage 3.** Triage `READY`. Six competencies. `material_strategy_change` records that Stage 3 made
controlled digital change the first proof, benefit methodology the second, and the founding of
Analyseavdelingen supporting evidence, and that it removed both the unimplemented proxy design and
the defensive paragraph. **All three are correct editorial judgements.** The Avinor package is the
stronger of the two.

---

## 3. The four material defect chains

### 3.1 Mission motivation escalates at every stage (ISS-05)

**Stage 1**, `motivation_bridge`, final clause:

> *"…i en medlemsorganisasjon der bedre prioriteringer kan gjøre det tryggere og enklere å være
> boligeier."*

**Stage 1**, `application_direction.structure_guidance`:

> *"Åpne med arbeidsgiverproblemet og kandidatidentiteten. … **Avslutt med konkret motivasjon og
> ønsket bidrag.**"*

**Stage 2**, `letter.closing`, restrained:

> *"Jeg motiveres av å bruke denne erfaringen i en medlemsorganisasjon der bedre styring kan styrke
> prioriteringer, samhandling og arbeidet for boligeierne."*

**Stage 3**, `letter.body_paragraphs[3]`, promoted to a dedicated paragraph and intensified:

> *"**Det som særlig motiverer meg**, er at bedre virksomhetsstyring hos Huseierne skal understøtte et
> tydelig medlemsoppdrag: å gjøre det tryggere og enklere å være boligeier."*

**Stage 3**, `review.json`, `reasons[1]` — the load-bearing find:

> *"Pakken består Arbeidsgiverbyttetesten: medlemsvekst, nye produkter, praktisk måloppfølging **og
> medlemsoppdraget** gjør både CV-profilen og søknaden spesifikke for Huseierne."*

Stage 3 did not merely retain the mission clause. It **cited it as evidence that the package passed
the employer-swap test** — the very test P0.9.1 added to Stage 3 to raise employer specificity. The
mechanism is the one hypothesised at `NON_AUTHORITATIVE_CONSIDERATIONS.md` §12.9, now reproduced from
the artifact rather than hypothesised.

`WRITING_DOCTRINE § Begrunnet motivasjon` forbids *"generisk virksomhetsros, kopierte verdier,
prestisjemotivasjon"* and was in force. `Arbeidsgiverbyttetesten` says *"Ikke reparer med slagord,
verdikopiering eller ubegrunnet virksomhetsros."* Both were present. But Stage 3's instruction names
the two tests and does not name `Begrunnet motivasjon`; and Stage 1's instruction says to consult the
doctrine **"only at"** `Single Backbone og strategisk asymmetri` and `WRONG_ROUTE`, so the section
governing `motivation_bridge` was formally out of Stage 1's scope when it authored that field.

**Classification: covered, but mis-routed at Stage 1 and out-weighed at Stage 3 by a more salient
named test.** Not a coverage gap.

### 3.1a The Avinor case is materially different and must not be swept up

Avinor's equivalent paragraph:

> *"Avinors kombinasjon av samfunnskritisk infrastruktur, sikker drift og bærekraftig utvikling gjør
> oppgaven faglig meningsfull. Jeg ønsker å bidra til at digitale initiativer blir valgt på et godt
> grunnlag, gjennomført med nødvendig kontroll og fulgt opp ut fra den verdien de faktisk skal skape
> for Avinor og samfunnet."*

The two cases are not the same defect:

| | Huseierne | Avinor |
|---|---|---|
| Source of the phrase | the employer's public slogan | the operating environment of the role |
| Connection to the work | none — governance quality is merely asserted to "support" the mission | direct — criticality is *why* change must be controlled and *why* the benefit case must be defensible |
| Connection to the candidate's argument | none | load-bearing: the whole transfer bridge is *"samfunnskritisk drift, regulering, høy feilkonsekvens, komplekse avhengigheter"* (Stage-1 objection 3 reframe) |
| Verdict | **defective** — `kopierte verdier` | **earned** — legitimate operating-environment motivation |

What *is* weak in the Avinor paragraph is its second sentence, the generic `Jeg ønsker å bidra til
at …` construction — which is ISS-11, not ISS-05.

**This distinction is why the fix is a non-sufficiency rule, not a category ban.** A categorical
exclusion of mission and societal language would destroy a correct paragraph in order to fix an
incorrect one.

### 3.2 Truth attenuation — a documentation frame transcribed into the candidate's own voice (ISS-06)

The factual authority, `Work_experience.md § 4.4 PRJ-04`:

> `STATUS_OUTCOME` — *"Implemented as hospital-wide standard; **reported active** approximately 2.5
> years later"*
> Supported contribution — *"**Vegard reports** it remained active approximately 2.5 years later."*
> §4 lifecycle index — *"Implemented hospital-wide and **reported active** ~2.5 years later"*

"Reported" marks **provenance inside the source file**: the fact rests on the candidate's own
statement rather than third-party measurement. It is not a hedge the candidate holds about his own
knowledge.

Trace across all six artifacts:

| Stage | Artifact / field | Text |
|---|---|---|
| 1 | `strategy.evidence_plan[].role`, both jobs | `var **rapportert aktivt** omtrent 2,5 år senere` |
| 2 | `draft_package` CV bullet + letter, both jobs | `var **fortsatt rapportert aktivt** om lag 2,5 år senere` |
| 3 | `final_package` CV bullet + letter, both jobs | `var **rapportert i bruk** om lag 2,5 år senere` |

Two separate failures:

1. **Stage 1 is the origin.** The provenance frame first appears in `evidence_plan[].role` — the field
   whose entire job is to frame the proposition for both downstream writers. Both inherited it.
2. **Stage 3 net-weakened it.** Stage 2 had added `fortsatt`, moving toward the correct reading.
   Stage 3 **touched the same sentence** (changing `aktivt` to `i bruk`) and **removed `fortsatt`**.
   A deliberate re-word, not inattention, and it made the claim weaker than the draft it replaced.

Effect on the reader: `var rapportert i bruk` reads as *someone told me it was still in use and I
cannot vouch for it*. The evidence supports *it was still in use about 2.5 years later, on my own
knowledge*. The approximation (`om lag`) and the observation horizon (`2,5 år senere`, not "today")
are genuine qualifications that must survive; the attribution distance is not.

Coverage check. `PERSUASION_CALIBRATION § TOO_WEAK` forbids replacing supported verbs with `bidro
litt`/`fikk anledning til` and forbids defensive prose about non-disqualifying gaps. Neither covers
this. `WRITING_DOCTRINE § Fakta- og lifecycle-grenser` distinguishes lifecycle states and result
classes but says nothing about attribution voice. **Classification: genuine missing semantic coverage
— the only one of the five mandatory outcomes for which that is true.**

Occurrences in shipped employer-facing text: **4** (CV bullet + letter body, both jobs).

### 3.3 Openings and the letter skeleton (ISS-09, ISS-10)

Stage 2's openings, both jobs, were plain and candidate-first:

> *"Jeg søker stillingen som strategi- og målstyringsrådgiver fordi Huseierne står i en vekstfase der…"*
> *"Jeg søker stillingen som seniorrådgiver digital transformasjon fordi Avinor beskriver et mandat…"*

Stage 3 replaced both with employer-first consultant forms:

> *"Huseierne skal omsette medlemsvekst, nye produkter og større organisatorisk kompleksitet til
> tydelige prioriteringer og resultater."*
> *"Når Avinor skal bruke teknologi, data og nye arbeidsformer til å utvikle tjenestene på tvers av 43
> flyplasser og i flysikringen, må digitale initiativer skape verdi uten at driftskontinuitet og
> sikkerhet blir en ettertanke."*

The Avinor opening is the recognisable `Når <employer> skal <X>, må <Y> uten <Z>` consultant form.
Both restate the employer's own situation back to the employer before the candidate appears.

**The skeleton is prescribed upstream.** Both Stage-1 strategies independently specified the same
macro-shape in `application_direction.structure_guidance`:

| | Huseierne | Avinor |
|---|---|---|
| open | *"Åpne med arbeidsgiverproblemet og kandidatidentiteten"* | *"Åpne med Avinors gjennomførings- og gevinstproblem"* |
| proof 1 | gevinstrammeverket | budsjettmoderniseringen |
| proof 2 | budsjettmoderniseringen | gevinstrammeverket |
| support | *"la styrings-BI dokumentere data- og KPI-siden kort"* | *"Bruk beslutningsmodellen og styrings-BI kort som støtte"* |
| close | *"Avslutt med konkret motivasjon og ønsket bidrag"* | *"Avslutt med samfunnsoppdraget og et nøkternt bilde av bidraget"* |

The two strategies were written independently with a reset between jobs and their wording differs, so
this is **not** cross-job carry-over. It is a **convergent prior**: the schema field invites an
opening/body/closing answer and the model fills it the same way each time. Both final letters follow
it exactly — employer problem → proof 1 → proof 2 → current role → motivation → polite close.

**Low severity, and it must be handled carefully.** The shape is a defensible argument for both
vacancies. The defect is not similarity; it is that `structure_guidance` was answered as a generic
letter template rather than as *the argument this vacancy needs*. Testing the letter's silhouette
would reward difference for its own sake.

### 3.4 Punctuation — nothing came from the models (ISS-07, ISS-08, ISS-12)

Direct grep of both `final_package.json`: **en dash 0, em dash 0**. The models generated no prohibited
dash in either job.

Exactly one ordinary hyphen is used as a clause divider in generated prose in the entire pilot:

> *"…en felles metode både gir retning og fungerer i arbeidshverdagen **-** en problemstilling jeg
> kjenner igjen i Huseiernes ambisjon…"* — Huseierne `final_package.letter.body_paragraphs[0]`

Every dash that reaches an employer-facing page is **deterministic**:

| Source | Rendered count | Kind |
|---|---|---|
| `runtime/jobbsok/render.py:179` — `lines.append(f"{line} — {summary}" …)` | **4 em dashes** | clause divider, one per previous employment, in TIDLIGERE ERFARING |
| `authorities/CV_BASELINE.md` → `generated/baseline_map.json`, mirrored in master static furniture | **15 en dashes** | 11 date ranges, 2 unit names, 3 trust-section ranges |
| `templates/APPLICATION_MASTER.docx` static text | **1 en dash** | subject line `Søknad – {title}` |
| `runtime/jobbsok/render.py:832` | 2 en dashes | `docProps` title/subject metadata, not on the page |

Verified in the readable vertical-slice render (same masters, synthetic content): CV `EN=15 EM=4`,
letter `EN=1 EM=0`.

**Dependency that constrains the fix.** `render.preflight_templates` compares the masters' visible
text against `baseline_map` values through `static_baseline_assertions`, including
`{employment[EMP_OUS_ANALYSE].unit}` and `{employment[EMP_OUS_ANALYSE].employment_group_period}`. The
baseline and both masters must change in the same step or preflight fails.

Verified safe: no JSON-schema `pattern` and no runtime regex depends on the en dash. The only two code
references are `leakage.py:98` (`KNOWN_GOOD_PHRASES`) and `render.py:832`.

---

## 4. Rendered output, typography and environment

### 4.1 Typography is inline, not style-driven — this corrects a prior finding

`docxfill.fill_block` does `copy.deepcopy(templates[…])` on the template paragraph inside each SDT,
and `docxfill._set_paragraph_text` deep-copies the **template run including its `w:rPr`**. Every
generated paragraph therefore inherits the master's **inline `w:sz`**, not the `styles.xml` value.

`CV_MASTER.docx` `word/document.xml` carries **41 `w:sz` elements and zero `w:szCs`**, distinct values
`{8.5, 9.0, 9.5, 10.0, 24.5}`. `APPLICATION_MASTER.docx` carries **7 `w:sz`**, all `8.5`; its
`APPLICATION_BODY` control has **no inline size at all** and therefore renders at `styles.xml Normal`
= **10.5**.

Consequence: **the CV requires the inline runs to be rewritten; the letter requires `styles.xml`.**
Changing only `styles.xml`, as a prior report implied, would leave the CV almost entirely unchanged.

The half-point sizes `8.5` and `9.5` appear in neither master's `styles.xml` size list, which is why
earlier inventories missed them.

### 4.2 Hierarchy is carried by bold, caps and colour — and two content zones are mis-formatted

| Element | sz | bold | caps | colour |
|---|---|---|---|---|
| `VEGARD HÅLAND` | 24.5 | Y | Y | `17324D` navy |
| `CV_FUNCTIONAL_IDENTITY` | 10.0 | Y | Y | `0F6B73` teal |
| `Heading1` ×9 | 10.0 | Y | Y | `0F6B73` teal |
| employment title line | 10.0 | Y | – | `17324D` navy |
| employment period run | 8.5 | Y | – | `5B6570` grey |
| unit lines | 9.0 | Y | – | `1F2933` body |
| education title lines | 9.5 | Y | – | `17324D` navy |
| contact line | 8.5 | – | – | `5B6570` grey |
| profile, competencies, both bullet zones | 9.0 | – | – | body |
| `CV_RELEVANT_MASTER_SUBJECTS` | 8.5 | – | – | body |
| **`CV_RELEVANT_BACHELOR_SUBJECTS`** | **9.5** | **Y** | – | **navy** |
| **`CV_PREVIOUS_EXPERIENCE_CONTENT`** | **9.5** | **Y** | – | **navy** |

Two findings, neither previously recorded.

**(a) Section headings sit only 1 pt above body text.** The hierarchy is real but is carried almost
entirely by weight, capitals and colour. Any change that lifts body text to 12 pt must lift the
headings too, or it removes a differential that currently exists.

**(b) Two content zones inherit title-line run properties (ISS-04).** The bachelor-subject line and
the whole TIDLIGERE ERFARING block render **bold, navy, 9.5 pt** — styled like record titles — while
carrying the least decision-relevant content on the page. They are also inconsistent with the
equivalent master-subject zone at 8.5 plain. This competes with the section headings for the
recruiter's eye and works directly against `Tjuesekunderstesten`. It reads as an inherited P0.7
artifact in which an SDT was placed on a paragraph whose run properties belonged to the preceding
label.

### 4.3 Page behaviour — page 2 is overflow, not layout

`CV_MASTER.docx` contains **zero `<w:br w:type="page">` and zero `lastRenderedPageBreak`**. A forced
page break existed in the P0.7 original and was removed by `tools/prepare_masters.py` under GATE-05.
There is no static second-page layout: page 2 exists only when content overflows page 1.

Page geometry: A4 (`11906×16838` twips). CV margins `top/bottom 765`, `left/right 879` → text area
17.9 × 27.0 cm. Letter margins `top/bottom 964`, `left/right 1134` → 17.0 × 26.3 cm.

**Therefore OBS-03 ("CV page 2 substantially underutilized") is not an independent layout defect.** At
9 pt the CV runs to roughly 1.2 pages, leaving page 2 nearly empty. Lifting the body to 12 pt moves it
to roughly 1.5 pages, which *populates* page 2. The observation and the typography complaint have a
single cause and a single fix.

### 4.4 Render outcome

Both DOCX `OK` and promoted `CREATED`; all four PDFs `DEGRADED` with `page_count: null` and
`warnings: []`. Correct behaviour under `DEC-41` and F12: a page warning is produced only when PDF
conversion succeeds. The Word COM failure is a session-context fact — an interactive session on the
same machine reproduced a working converter — and is **not** a converter defect.

**Consequence for this audit: no page-count evidence exists for the pilot.** The typography and
page-balance observations rest on the human's visual inspection, not on disk.

### 4.5 OBS-12 reproduced — the output ACL problem, root-caused (ISS-13)

The earlier human-context attempt to read either pilot CV or letter as `vhaala\veggi` produced:

```
System.UnauthorizedAccessException — "Access to the path '…\out\CV_Avinor_AS_…docx' is denied."
icacls …\out\CV_Avinor_AS_…docx   ->  Access is denied.   (cannot even read the DACL)
Get-Item -Stream *                 ->  Access is denied.
```

This is `ERROR_ACCESS_DENIED`, **not** a sharing violation. A current identity-aware check sharpens the
evidence: `vhaala\CodexSandboxOnline` can read the four files because it owns them; their DACL is
protected and grants only Owner Rights, SYSTEM and Administrators. `vhaala\veggi` is absent. The
containing `out/` directory is unprotected and inherits `vhaala\veggi` FullControl. The JSON artifacts
in `current/` carry ordinary inherited DACLs.

The asymmetry maps exactly onto the two write paths:

- `atomicio.atomic_write_bytes` creates its temp file **in the destination directory**
  (`dir=path.parent`), so the promoted file inherits `current/`'s ACL. Its own docstring gives the
  reason: *"The temp file lives in the destination directory so the rename stays on one volume."*
- `render.render_job` opens `TransactionDir(Path(tempfile.gettempdir()), …)`. This checkout runs
  Python 3.14.3; the current `tempfile.mkdtemp()` implementation calls `os.mkdir(..., 0o700)`, which
  intentionally creates a protected creator-only directory on Windows. The DOCX inherits that DACL.
  `os.replace` then preserves it instead of re-evaluating `out/` inheritance.

Direct cause: private `0o700` transaction directory plus same-volume move (confidence HIGH). This also
invalidates the tempting one-line repair of merely moving `mkdtemp` under the job directory: the
special mode would still produce the private DACL. F1 must create the employer-facing transaction
with ordinary parent inheritance while keeping rollback transactions private.

Two further observations. `DEC-21` step 6 requires the finalizer to *"write to a temporary **job**
path"*, and `Layout.writable_roots` includes `runs` — so the current implementation already deviates
from the frozen wording and the fix moves toward it. And `render.verify_receipt` re-reads the output
to re-hash it, so `status` run by the human on this run reports the render unverifiable.

---

## 5. Cross-job comparison

### 5.1 What differed — evidence the reset worked

| | Huseierne | Avinor |
|---|---|---|
| headline | `styringsinformasjon, felles metode og gjennomføring` | `digital endring, gevinst og gjennomføring` |
| personality facets | `PF-01`, `PF-11`, `PF-08` | `PF-19`, `PF-01`, `PF-11` |
| lead evidence | gevinstrammeverket | budsjettmoderniseringen |
| second evidence | budsjettmoderniseringen | gevinstrammeverket |
| CV bullet order | benefit framework first | budget tool first |
| CV bullet 4 | need-to-delivery translation | founding of Analyseavdelingen |
| competencies | 6, governance-weighted | 6, change/delivery-weighted |
| objections | 4 | 5 (incl. security clearance) |

Different facets, different lead evidence, different bullet order, different competency sets. The
Stage-1 and Stage-3 cross-job resets demonstrably worked at the level of *what to say*.

### 5.2 What was identical

Two CV bullets are byte-identical across both jobs:

> *"Samarbeidet i et firepersonsteam om å videreutvikle et gevinstrealiseringsrammeverk som ble innført
> som sykehusdekkende standard og var rapportert i bruk om lag 2,5 år senere."*
> *"Rekonstruerte arkitekturen og sto for hoveddelen av kodeendringene da et arvet, virksomhetskritisk
> budsjettverktøy ble modernisert i en bred interessentprosess. …"*

**This is not a defect.** `WRITING_DOCTRINE § Variasjon innenfor en klynge`: *"Delte fakta er
legitimt; gjentatt generisk ordlyd, arbeidsgiverproblem eller motivasjon er det ikke."* These bullets
are specific factual statements, they appear in different positions, and the surrounding CV top zone
differs materially. Recorded as an explicit **non-target**.

What *is* repeated generic wording:

- `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …` — the closing of **both**
  final letters, and present in both Stage-2 drafts. **Four occurrences across two jobs and two
  stages**, and Stage 3 did not touch it in either job. The single most reproducible formulaic
  signature in the pilot.
- `Jeg ønsker å bidra …` as a standalone motivation sentence — both final letters.
- The macro-skeleton of §3.3.

### 5.3 The strongest existing voice evidence — a regression guard

From Avinor `final_package.letter.body_paragraphs[1]`:

> *"Det har gitt meg en nøktern tilnærming til gevinster: forventninger må gjøres etterprøvbare,
> ansvar og antakelser må være synlige, og metoden må fungere for dem som skal bruke den."*

Claim → criteria → auditability → practical usability, in one sentence, with no ornament. This is
what the candidate's professional voice sounds like when it survives. **Any change set that makes this
sentence worse is over-applied**, and it is carried as an acceptance guard in
`07_VERIFICATION_ACCEPTANCE_AND_STOPPING_PLAN.md`.

---

## 6. Limitations — what this audit could not see

Recorded explicitly rather than inferred, because several downstream conclusions depend on knowing
which evidence is missing.

1. **No rendered PDF exists for the pilot.** Both jobs are render `DEGRADED` with `page_count: null`.
   No page count, no page-balance measurement and no render page warning exists on disk for either
   job.
2. **The four pilot DOCX can be read as bytes by the current sandbox owner, but not visually opened in
   Word here.** Word COM activation failed in this session, and the read-only Computer Use attempt was
   not authorized for Word. The `.png` files under `P0.9/Build/tmp/pdfs/` are six-page renders of the
   **source vacancy PDFs**, not of the output documents.
3. **Typography and page-balance findings are therefore analytical, not visual.** §4.1–4.3 derive from
   the OOXML and from the readable vertical-slice render, which uses the same masters with synthetic
   content. The page estimates in `02_…md` are a model, marked as such, and are discharged by
   measurement in Run A1.
4. **`pilot/PILOT_LOG.csv` contains only its header**, last written `2026-08-24` — before the pilot.
   The repository retains no human quality score, edit list, minutes-through-submission, post-render
   factual correction, actual repair scope versus triage, submission decision or outcome. `ACC-20` and
   Spec §18.3 expect all of these. `NON_AUTHORITATIVE_CONSIDERATIONS.md` contains deliberation material,
   not a substitute log; only observations independently reproduced in this audit are retained.
5. **Claims carried as the user's direct observation rather than disk evidence:** OBS-01 and OBS-02
   (body text is *too small* — the sizes are verified, the judgement is the user's) and OBS-03 (page 2
   sparse — consistent with the geometry but not measured).
6. **One considerations-file claim is refuted.** OBS-06 states *"One package weakened a fact that
   another package stated correctly as current continued use."* Both packages carry the identical
   hedge; no pilot artifact contains the stronger form. The stronger form appears only in the Stage-2
   drafts, and only as `fortsatt rapportert aktivt`.
7. **Visual output balance remains unresolved even though the ACL chain is now observable.** Current
   SDDL, process identity and Python source establish the access mechanism; only Run A1 under the new
   staging mode can prove the repair at the human identity boundary.
8. **Semantic product quality remains unproven by any mechanical evidence.** `INV-08` forbids citing
   engineering results as product evidence, and nothing in this audit does so.
