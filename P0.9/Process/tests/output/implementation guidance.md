# Implementation guidance

Revised 2026-09-12 after the R01–R11 adversarial iteration. This is the standalone execution specification for the Avinor-driven P0.9 optimisation. It repeats every accepted edit. Do not open either original plan to infer missing intent.

**Scope:** maintain the named live source files only. Do not modify candidate facts, schemas, generated packages, frozen inputs or historical original masters. Do not add a new test, harness, CLI mode, similarity detector, semantic validator or diagnostic field. One existing template-count assertion is updated because the actual master contract changes.

**Owner decision:** E08–E10 are the exact proposed reusable correction for Vegard's acceptance/rejection. Execute them only if he explicitly accepts those corrections, including an explicit instruction to implement them. Otherwise skip them and proceed with the independent clusters. E11 is a separately optional example supplement; skip it in the first shipment unless explicitly requested and accepted. Do not ask for confirmation again after acceptance. This dependency comes from PERSUASION_CALIBRATION.md:11 and :83–84, not from a model-created approval rule.

**Default shipment:** A + C + D, including E04a and E12a. Add E08–E10 if the correction is accepted. E11 is optional. No implementing-model design choice remains: payloads, placement, boundaries and default skip behavior are specified.

If E08–E10 are not accepted before the boundary, the next child does not test M03's specific unknown-status and clause-gap correction. M04 can still be assessed on expression within its locked content; surviving C02/C03 content is not by itself a register-pass failure. Such sentences may persist, but are not inevitable: existing truth rules and E05 can already prevent some. In the ordinary completion message, before creating the child, state `M03 core correction: included` or `M03 core correction: skipped — not accepted`, according to the actual executed steps. Create no tracking file. Prefer obtaining the owner's decision before the single boundary; if it is absent, follow the stated skip path.

## Execution order and common mechanics

Run clusters A, B if accepted, C, then D. All chosen edits precede **one child-run creation at the end**. There is no freeze between clusters. A step names one file and one coherent edit. Steps with the same file are separate atomic changes; preserve the order.

Use the existing Build interpreter. The following is operator-session setup, not a file edit or shipped subsystem:

```powershell
$Build = 'C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build'
Set-Location -LiteralPath $Build
$Py = Join-Path $Build '.venv\Scripts\python.exe'
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONDONTWRITEBYTECODE = '1'
$Rollback = Join-Path $env:TEMP ('avinor-master-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $Rollback | Out-Null
$env:AVINOR_ROLLBACK = $Rollback
$Rollback
```

Keep the printed absolute rollback directory for this maintenance session. If tools start a fresh PowerShell process, set these variables and AVINOR_ROLLBACK to the same values again; do not generate a different rollback directory for each step. Backups are temporary operator recovery copies, not repository artifacts.

Before each selected step, copy **that one file's current bytes** to `$Rollback/<step ID>`. Its current state includes any earlier accepted edit to the same file. The per-step backup/restore commands below make the operation reversible. To roll back a group, restore steps in reverse order so a later same-file backup does not reintroduce an edit already undone.

For a text step, replace the exact complete old block once with the exact replacement. For an append step, append the block at the end. For a Python step, execute its complete code from Build by piping a PowerShell single-quoted here-string into `& $Py -`; do not save helper scripts in Build. All paths in those Python payloads are hardcoded relative to the stated Build directory. Preserve UTF-8 and actual newlines.

**Verification is batched.** Each step supplies one concrete check, but queue it until its cluster is complete. Run that cluster's listed checks in one validation batch. Do not generate a package or invoke Word between edits. Checks establish the property they name; a text match or T18 pass is not proof of output quality or pagination.

If an exact old anchor is absent, the source differs from the inspected baseline: do not silently fuzzy-match an unrelated passage. Reconcile that specific changed file with the proposed final behavior. This is an execution instruction for a stale source, not a new runtime validation layer.

## Cluster A — Content selection and role allocation

Prerequisites: none. Implements the highest-value policy changes using existing fields. No new social-register guidance enters Stage 1 or drafting. E01–E07, including E04a, all require new frozen policy inputs for the next run.


### E01 — Replace the average-score selection premise

**One file:** [policy/writing/WRITING_DOCTRINE.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/WRITING_DOCTRINE.md:149>).

**Prerequisites:** none. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M01; mitigates C01; C04.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Destination (Join-Path $Rollback 'E01')
```

**Exact anchor/current behavior:**

```text
Begrunnelsen er rangering, ikke telling. En leser vurderer en pakke omtrent som
et gjennomsnitt, ikke som en sum: et moderat argument ved siden av et sterkt
trekker helheten ned. Ikke konstruer et svakt andre case, og ikke kort ned bare
for å korte ned. Færre argumenter skal være en følge av sterkere prioritering og
dypere bevis.
```

**Replace the anchor once with exactly:**

```text
Begrunnelsen er arbeidsgiverens beslutning, ikke telling. Et nytt bevis har
verdi når det svarer på et vesentlig spørsmål som den beholdte pakken ikke
allerede besvarer. Et kort, konkret bevis for en annen avgjørende oppgave kan
derfor være viktigere enn mer dybde i hovedcaset. Ikke konstruer et svakt case
for å fylle en kategori, og ikke behold detaljer bare fordi de er unike.
Velg den kombinasjonen som gir det sterkeste, sannferdige beslutningsgrunnlaget
for denne stillingen. Færre argumenter er et mulig resultat av prioriteringen,
ikke et mål.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'Et kort, konkret bevis for en annen avgjørende oppgave' policy/writing/WRITING_DOCTRINE.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E01') -Destination (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Force
```

Restore later edits to this same file first. 

### E02 — Distinguish empty advertisement repetition from supported role vocabulary

**One file:** [policy/writing/WRITING_DOCTRINE.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/WRITING_DOCTRINE.md:475>).

**Prerequisites:** E01. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M01; mitigates C01.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Destination (Join-Path $Rollback 'E02')
```

**Exact anchor/current behavior:**

```text
1. gjengivelse av annonsen og generisk ros;
```

**Replace the anchor once with exactly:**

```text
1. gjengivelse av annonsen som ikke kobles til kandidatens arbeid, og generisk
   ros. Behold arbeidsgiverens faglige begreper når de presist navngir støttet
   erfaring eller et begrunnet fremtidig bidrag; et dekket krav er ikke
   annonseekko bare fordi samme begrep står i annonsen;
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'et dekket krav er ikke' policy/writing/WRITING_DOCTRINE.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E02') -Destination (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Force
```

Restore later edits to this same file first. 

### E03 — Allocate material requirements through existing strategy fields

**One file:** [policy/stages/stage1_decision_architecture.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/stages/stage1_decision_architecture.md:66>).

**Prerequisites:** E01, E02. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M01; mitigates C01; C05.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/stages/stage1_decision_architecture.md') -Destination (Join-Path $Rollback 'E03')
```

**Exact anchor/current behavior:**

```text
material_requirements retains every material minimum, important and desired
requirement using the existing importance/relation/note/evidence_refs fields.
objections handles real gaps. Adjacent evidence is not fulfillment of a
minimum. Choose affirmative, truthful transfer without inventing equivalence.
cv_direction allocates breadth and credible top signals; application_direction
allocates interpretation and carrying arguments. motivation_bridge connects
supported experience to the actual employer task.
```

**Replace the anchor once with exactly:**

```text
material_requirements retains every material minimum, important and desired
requirement using the existing importance/relation/note/evidence_refs fields.
For a compound requirement, distinguish alternatives from cumulative duties.
SUPPORTED for one alternative does not establish the others. State the supported
part and the remaining boundary in note; do not turn adjacent experience into
fulfillment of a minimum or into portfolio, programme or line authority.
After choosing the carrying evidence, identify material employer questions the
proposed pair would still leave unanswered. Use note to name the useful proof
and its intended function in the CV, letter or review. This is a reasoned
allocation, not a requirement to mention every vacancy noun or add a case for
every requirement. Where evidence is absent, retain the gap without inventing
a delivery, meeting outcome, recipient or mandate.
cv_direction allocates breadth and credible top signals; application_direction
allocates interpretation and carrying arguments. Put the remaining high-value
coverage decisions in those existing fields. A collaboration claim needs the
supported interaction, recipient and action where available; headcount alone
establishes scale. motivation_bridge connects supported experience to the
actual employer task. objections handles real gaps.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'SUPPORTED for one alternative does not establish the others.' policy/stages/stage1_decision_architecture.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E03') -Destination (Join-Path $Build 'policy/stages/stage1_decision_architecture.md') -Force
```

Restore later edits to this same file first. 

### E04 — Read the final pair against the vacancy before locking content

**One file:** [policy/stages/stage3_final_writer_review.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/stages/stage3_final_writer_review.md:54>).

**Prerequisites:** E03. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M01; mitigates C01; C05.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Destination (Join-Path $Rollback 'E04')
```

**Exact anchor/current behavior:**

```text
5. Address material requirements and gaps truthfully, build specific motivation,
   and remove repetition that adds neither a new function nor useful detail.
```

**Replace the anchor once with exactly:**

```text
5. Read the proposed CV and letter against the vacancy's material requirements.
   Use strategy.material_requirements and its notes as pointers, then judge the
   actual pair. Repair a missing high-value answer with supported evidence in
   the document where it helps most; do not add a keyword, case or claim merely
   to complete a list. Check compound requirements at the supported-clause
   level. A supported alternative does not establish an unproved mandate.
   Show recipient interaction where it is documented and useful, rather than
   treating a team size as proof of facilitation. Build specific motivation.
   Keep unresolved material gaps in the existing review fields; do not create
   a coverage field, ledger, score or separate artifact.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'Check compound requirements at the supported-clause' policy/stages/stage3_final_writer_review.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E04') -Destination (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Force
```

Restore later edits to this same file first. 

### E04a — Explain a supported material answer left out of the pair

**One file:** [policy/stages/stage3_final_writer_review.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/stages/stage3_final_writer_review.md>).

**Prerequisites:** E04. **Run boundary:** YES — include the maintained input in the single new/child run.

**Purpose:** M01 / C01 / C05; R02. Reuse review.notes for a material omission and reason, never an evidence-survival account.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Destination (Join-Path $Rollback 'E04a')
```

**Exact anchor/current behavior:**

```text
Give concise reasons with recommended actions — ordinarily about three of the
highest priority, while preserving enough detail to act. Record known
limitations relevant to human approval. Where you exercised elasticity
materially, or repaired an upstream claim, say so in the optional diagnostic
fields: those are process signals the pilot wants to see.
```

**Replace the anchor once with exactly:**

```text
Give concise reasons with recommended actions — ordinarily about three of the
highest priority, while preserving enough detail to act. Record known
limitations relevant to human approval.
If a material MINIMUM or IMPORTANT requirement marked SUPPORTED in strategy
remains unanswered in both documents, verify the supported clause against the
vacancy and factual source, then briefly name the unanswered supported part in review.notes
and explain the omission. Treat the strategy label as a pointer, not proof.
Do not account for every requirement or evidence item, write an all-covered
attestation, or create a coverage field, matrix, ledger, score or artifact.
An omission note does not determine triage; remaining repair scope still does.
Where you exercised elasticity materially, or repaired an upstream claim, say
so in the optional diagnostic fields: those are process signals the pilot wants to see.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'briefly name the unanswered supported part in review.notes' policy/stages/stage3_final_writer_review.md
```

**Expected:** the stated checks succeed. This is not evidence of model compliance or output quality.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E04a') -Destination (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Force
```

Restore later edits to this same file first.

### E05 — Make substantive selection and pair editing explicit before content lock

**One file:** [policy/stages/stage3_final_writer_review.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/stages/stage3_final_writer_review.md:65>).

**Prerequisites:** E04, E04a. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M02; mitigates C02; C04; C05; C06; C07.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Destination (Join-Path $Rollback 'E05')
```

**Exact anchor/current behavior:**

```text
**A realization-only pass follows.** You do not have to buy smoothness here by
deleting signal. Preserve the strongest evidence and judgment, and let the polish
pass make it read well. When a passage is both important and awkward, keep it and
fix it below — do not resolve the tension by cutting it.
```

**Replace the anchor once with exactly:**

```text
**Complete the substantive pair edit before locking content.** Read the CV and
letter together. For each retained case, make the candidate's action, useful
judgment, recipient or changed work legible where the sources support them.
Choose technical detail for the employer question it answers. Being unique
does not make a detail necessary; being awkward does not make useful judgment
dispensable. Replace weaker material when stronger supported evidence answers
a material question better. The strategy remains option value, not a checklist.

When a case appears in both documents, let the CV establish scope and delivery
and the letter explain the useful choice, implication or proposed contribution.
Remove repeated explanation that does the same job twice. Retain shared names,
dates, status and concise factual anchors when needed for intelligibility.
Do not enforce lexical difference or compute similarity.

Read each profile sentence, transition and conclusion as a complete claim.
Keep ownership, project identity, version, period, adoption and measured effect
attached to the correct evidence. A later version's status does not establish
the earlier version's scope or method. A design purpose does not establish an
observed user outcome. A case-specific judgment does not by itself establish a
universal causal rule. Repair those claims here, using K and the original
sources. Once the strongest supported content is selected, keep it through
the expression-only polish below.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'A design purpose does not establish an' policy/stages/stage3_final_writer_review.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E05') -Destination (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Force
```

Restore later edits to this same file first. 

### E06 — Replace absolute employer uniqueness with a defensible role connection

**One file:** [policy/writing/WRITING_DOCTRINE.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/WRITING_DOCTRINE.md:431>).

**Prerequisites:** E01. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M06; mitigates C09; C07.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Destination (Join-Path $Rollback 'E06')
```

**Exact anchor/current behavior:**

```text
# Arbeidsgiverbyttetesten

Bytt arbeidsgivernavn og tittel mentalt med en annen jobb i klyngen.

Pakken feiler testen når:

- åpningen fortsatt passer uten andre endringer;
- arbeidsgiverproblemet er generisk;
- motivasjonen er utskiftbar;
- samme bevispar og rekkefølge brukes uten individuell begrunnelse;
- CV-profilen bare lister kandidatens generelle styrker.

Reparer med substansiell jobbspesifisitet: konkret oppgave,
beslutningsproblem, utvelgelsesregime, relevant evidensfunksjon og begrunnet
fremtidig bidrag. Ikke overkorriger med ukritisk annonseekko. Målet er en
pakke som bare kan tilhøre denne arbeidsgiveren og rollen, samtidig som
kandidatens faktiske stemme og evidens bevares.

Testen gjelder også CV-toppen, ikke bare brevet. Dersom profilen fortsatt
virker fullt gyldig etter at arbeidsgiver, stillingstittel og bransje er
byttet ut, er overstyringen for generell. Tydeliggjør da den konkrete
oppgaven, beslutningssituasjonen eller gjennomføringsformen som gjør
kandidatens dokumenterte erfaring relevant. Ikke reparer med slagord,
verdikopiering eller ubegrunnet virksomhetsros. Resultatet skal fortsatt
være rolig, presist og naturlig bokmål.
```

**Replace the anchor once with exactly:**

```text
# Arbeidsgiverbyttetesten

Bytt arbeidsgivernavn og tittel mentalt med en annen jobb i klyngen. Undersøk
om pakken begrunner hvorfor kandidatens dokumenterte arbeid er relevant for
den konkrete oppgaven, beslutningssituasjonen eller gjennomføringsformen.

Et navn, en verdi eller et virksomhetstall gjør ikke begrunnelsen spesifikk.
Samtidig kan en god begrunnelse være relevant for flere arbeidsgivere med
lignende behov. Navnebyttet er et redaksjonelt spørsmål, ikke et krav om at
hver setning bare kan passe én arbeidsgiver.

Reparer en generell pakke med et støttet arbeid og en tydelig anvendelse i
rollen. Skill mellom hva kandidaten har gjort, hva annonsen faktisk oppgir,
og hva kandidaten foreslår å bidra med. En funksjonell parallell kan begrunne
overførbarhet; den beviser ikke at to virksomheter har samme modell, problemer
eller beslutningsprosess. Ikke legg til en arbeidsgiverpåstand for å gjøre
koblingen mer særegen.

CV-toppen skal gjøre det relevante kandidattilbudet raskt forståelig. Den
trenger ikke gjenta arbeidsgivernavnet eller annonsens formuleringer. Brevet
skal gi en konkret grunn til å søke og et begrunnet fremtidig bidrag.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'Navnebyttet er et redaksjonelt spørsmål' policy/writing/WRITING_DOCTRINE.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E06') -Destination (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Force
```

Restore later edits to this same file first. 

### E07 — Give the headline a distinct editorial function

**One file:** [policy/writing/WRITING_DOCTRINE.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/WRITING_DOCTRINE.md:94>).

**Prerequisites:** E06. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M06; mitigates C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Destination (Join-Path $Rollback 'E07')
```

**Exact anchor/current behavior:**

```text
- Etabler ankeret før du presenterer uvanlig bredde.
- Ikke oppgrader den formelle tittelen.
- Ikke bare gjenta stillingstittelen fra annonsen.
- Koble kandidatens stabile profesjon og nåværende rolle til funksjonen
  stillingen beskriver.
- Bredde kan utdype kategorien etter at den er lesbar. Den skal ikke
  konkurrere med den.
```

**Replace the anchor once with exactly:**

```text
- Etabler ankeret før du presenterer uvanlig bredde.
- Ikke oppgrader den formelle tittelen.
- Ikke bare gjenta stillingstittelen fra annonsen.
- Koble kandidatens stabile profesjon og nåværende rolle til funksjonen
  stillingen beskriver.
- Bredde kan utdype kategorien etter at den er lesbar. Den skal ikke
  konkurrere med den.

CV-overskriften navngir kandidatens relevante yrkesfunksjon. La profilen og
erfaringen forklare bredden; ikke legg hele argumentet eller en liste over
kompetanseområder i overskriften. Dette er en rollefordeling mellom feltene,
ikke en ord-, tegn- eller linjegrense.
```

**One queued check — run at the end of Cluster A:**

```powershell
rg -n -F 'CV-overskriften navngir kandidatens relevante yrkesfunksjon.' policy/writing/WRITING_DOCTRINE.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E07') -Destination (Join-Path $Build 'policy/writing/WRITING_DOCTRINE.md') -Force
```

Restore later edits to this same file first. 

## Cluster B — Explicitly accepted reusable calibration only

Prerequisite: Vegard's acceptance of the named correction. Without it, skip E08–E11 and continue at E12. E08–E10 are the core; E11 is optional later illustration. The existing verb-strength floor remains operative when this cluster is skipped. These are policy corrections, not edits to candidate facts.

### E08 — Proposed Vegard correction: distinguish unknown from negative status

**One file:** [policy/writing/PERSUASION_CALIBRATION.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/PERSUASION_CALIBRATION.md:115>).

**Prerequisites:** none. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run. **Acceptance condition:** follow Cluster B; E11 is optional and skipped by default.

**Purpose:** M03; mitigates C02; C07.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Destination (Join-Path $Rollback 'E08')
```

**Exact anchor/current behavior:**

```text
- Konseptevidens kan aldri låne implementerings-, adopsjons- eller
  resultatstatus, verken fra seg selv eller fra en annen post.
- Når to poster står i samme argument, beholder hver sin egen tilstand. En
  beslutning i én post er aldri årsaken til en annen posts varighet eller bruk.
```

**Replace the anchor once with exactly:**

```text
- Konseptevidens kan aldri låne implementerings-, adopsjons- eller
  resultatstatus, verken fra seg selv eller fra en annen post.
- Når to poster står i samme argument, beholder hver sin egen tilstand. En
  beslutning i én post er aldri årsaken til en annen posts varighet eller bruk.
- Uavklart eller ikke dokumentert status betyr ikke at noe ikke har skjedd.
  Når kilden bare fastslår utforming, kan teksten si hva kandidaten utformet.
  Den kan ikke derfor si «ikke innført». Et uttrykkelig negativt statusutsagn
  krever støtte for fraværet, på samme måte som et positivt utsagn krever støtte
  for gjennomføringen.
- Hold artefaktets ferdigstillelse, overlevering, organisatoriske bruk og
  målte effekt fra hverandre. Bevar også skillet mellom versjoner og perioder;
  senere bekreftet bruk endrer ikke automatisk beskrivelsen av tidligere arbeid.
```

**One queued check — run at the end of Cluster B:**

```powershell
rg -n -F 'Uavklart eller ikke dokumentert status betyr ikke' policy/writing/PERSUASION_CALIBRATION.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E08') -Destination (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Force
```

Restore later edits to this same file first. 

### E09 — Proposed Vegard correction: apply the gap rule to clauses as well as paragraphs

**One file:** [policy/writing/PERSUASION_CALIBRATION.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/PERSUASION_CALIBRATION.md:125>).

**Prerequisites:** E08. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run. **Acceptance condition:** follow Cluster B; E11 is optional and skipped by default.

**Purpose:** M03; mitigates C02; C03; C05.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Destination (Join-Path $Rollback 'E09')
```

**Exact anchor/current behavior:**

```text
1. Antyd aldri at et uoppfylt minstekrav er oppfylt.
2. Si positivt hva den nærliggende, overførbare evidensen faktisk er, når den
   reduserer arbeidsgiverens usikkerhet.
3. Bruk arbeidsgiverens substansielle vokabular bare der det er dekket.
4. Unngå et defensivt «jeg mangler X»-avsnitt med mindre taushet ville villede
   vesentlig.
5. Hold det uløste gapet synlig i `review.json` for mennesket.
6. Et kjent gap alene tvinger ikke `CHECK` når ingen faktabekreftelse eller
   lokal reparasjon gjenstår.

Den positive overføringsbroen er en formulering om det kandidaten faktisk har
gjort, ikke en omskrivning av det han mangler.
```

**Replace the anchor once with exactly:**

```text
1. Antyd aldri at et uoppfylt minstekrav er oppfylt.
2. Si positivt hva den nærliggende, overførbare evidensen faktisk er, når den
   reduserer arbeidsgiverens usikkerhet. Behold det sterkeste støttede
   arbeidsverbet og riktig personlig bidrag.
3. Bruk arbeidsgiverens substansielle vokabular bare der det er dekket.
4. Avgrens først selve påstanden: arbeidsverb, eierskap, omfang, periode,
   leveransestatus og resultat. Når dette gir riktig forståelse, skal teksten
   ikke i tillegg bære en generell liste over mandat eller erfaring kandidaten
   ikke har. Dette gjelder også en innskutt leddsetning eller kontrast, ikke
   bare et eget «jeg mangler X»-avsnitt.
5. Behold et uttrykkelig forbehold når den konkrete teksten ellers ville villede
   vesentlig. Ikke flytt en nødvendig opplysning til review for å få en sterkere
   søknad. Ukjent bruk eller effekt skal heller ikke omskrives til kjent fravær.
6. Hold det uløste materialgapet synlig i eksisterende felter i review.json.
   Et kjent gap alene tvinger ikke CHECK når ingen faktabekreftelse eller lokal
   reparasjon gjenstår.

Den positive overføringsbroen sier hva kandidaten faktisk har gjort og hvordan
det kan brukes. Den skal verken blåse opp erfaringen eller gjøre et
ikke-diskvalifiserende fravær til et nytt argument mot kandidaten.
```

**One queued check — run at the end of Cluster B:**

```powershell
rg -n -F 'Dette gjelder også en innskutt leddsetning eller kontrast' policy/writing/PERSUASION_CALIBRATION.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E09') -Destination (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Force
```

Restore later edits to this same file first. 

### E10 — Proposed Vegard correction: label the lifecycle example as syntax, not a template

**One file:** [policy/writing/PERSUASION_CALIBRATION.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/PERSUASION_CALIBRATION.md:65>).

**Prerequisites:** E08. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run. **Acceptance condition:** follow Cluster B; E11 is optional and skipped by default.

**Purpose:** M03; mitigates C08.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Destination (Join-Path $Rollback 'E10')
```

**Exact anchor/current behavior:**

```text
Mønstereksempel, med generisk innhold. Kilden sier at noe «ble innført som
Y-standard» og er «oppgitt aktivt om lag N år senere»:
```

**Replace the anchor once with exactly:**

```text
Mønstereksempelet viser bare forskjellen mellom kandidatstemme,
dokumentasjonsstemme og en for sterk tidsangivelse. Det er ikke en
setningsmal som skal gjenbrukes. Behold kildens faktiske status og tidspunkt,
men la formuleringen følge argumentet i den aktuelle teksten. Kilden i dette
generiske eksempelet sier at noe «ble innført som Y-standard» og er «oppgitt
aktivt om lag N år senere»:
```

**One queued check — run at the end of Cluster B:**

```powershell
rg -n -F 'Det er ikke en' policy/writing/PERSUASION_CALIBRATION.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E10') -Destination (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Force
```

Restore later edits to this same file first. 

### E11 — Optional proposed Vegard correction: concrete verb-floor examples

**One file:** [policy/writing/PERSUASION_CALIBRATION.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/PERSUASION_CALIBRATION.md:58>).

**Prerequisites:** E09. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run. **Acceptance condition:** follow Cluster B; E11 is optional and skipped by default.

**Purpose:** M03; mitigates C03; C04.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Destination (Join-Path $Rollback 'E11')
```

**Exact anchor/current behavior:**

```text
- Ikke bær kildefilenes dokumentasjonsstemme inn i kandidatens egen tekst. Når
  myndigheten sier at kandidaten «oppgir X», er X kandidatens egen opplysning og
  kan sies direkte av ham. Bevar reelle grenser som omtrentlighet,
  observasjonstidspunkt, lifecycle-tilstand og fravær av måling; fjern bare
  avstanden som oppstår fordi kilden er skrevet *om* kandidaten. Kjent sannhet
  skal låte kjent.
```

**Replace the anchor once with exactly:**

```text
- Ikke bær kildefilenes dokumentasjonsstemme inn i kandidatens egen tekst. Når
  myndigheten sier at kandidaten «oppgir X», er X kandidatens egen opplysning og
  kan sies direkte av ham. Bevar reelle grenser som omtrentlighet,
  observasjonstidspunkt, lifecycle-tilstand og fravær av måling; fjern bare
  avstanden som oppstår fordi kilden er skrevet *om* kandidaten. Kjent sannhet
  skal låte kjent.

Verbene skal følge den dokumenterte handlingen, ikke statusprestisje:
«utformet en modell» sier utforming; «avviste direkte fordeling fordi
datagrunnlaget ikke bar den» sier en dokumentert faglig beslutning;
«gjennomførte kodeendringene» sier egen gjennomføring. Ingen av dem skal
automatisk bli «bidro til» fordi kandidaten manglet linje- eller
programmyndighet. Bruk «bidro til» eller «medutviklet» når det er den presise
beskrivelsen av et delt arbeid. Dette er eksempler på styrkekalibrering, ikke
påbud om bestemte verb.
```

**One queued check — run at the end of Cluster B:**

```powershell
rg -n -F 'Verbene skal følge den dokumenterte handlingen, ikke statusprestisje:' policy/writing/PERSUASION_CALIBRATION.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E11') -Destination (Join-Path $Build 'policy/writing/PERSUASION_CALIBRATION.md') -Force
```

Restore later edits to this same file first. 

## Cluster C — Last-part-of-Stage-3 register control

Prerequisites: complete A; B is independent and may be skipped. Keep E12–E17, including E12a, together so the knob, frozen-file transport, level definitions and last-pass invocation agree. No Stage-1 file gets the marker system. The absence of an older frozen knob is explicitly handled by skipping the new extended pass, while ordinary final polish remains.

### E12 — Add the operator's final-polish register setting

**One file:** [policy/settings.toml](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/settings.toml:21>).

**Prerequisites:** none. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M04; mitigates C10.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/settings.toml') -Destination (Join-Path $Rollback 'E12')
```

**Exact anchor/current behavior:**

```text
[personality]
# DEC-35: personality is ON in the baseline and is not a dormant stub.
# There is no OFF switch; the valid null outcome is Stage 1 selecting zero
# facets, which the strategy schema already permits. Adding a toggle with
# no consumer would be an optionality-only hook (Contract 21).
profile = "context/PERSONALITY_PROFILE.md"
facet_index = "policy/personality_facets.json"
max_selected_facets = 3
```

**Replace the anchor once with exactly:**

```toml
[personality]
# DEC-35: personality is ON in the baseline and is not a dormant stub.
# There is no OFF switch; the valid null outcome is Stage 1 selecting zero
# facets, which the strategy schema already permits. Adding a toggle with
# no consumer would be an optionality-only hook (Contract 21).
profile = "context/PERSONALITY_PROFILE.md"
facet_index = "policy/personality_facets.json"
max_selected_facets = 3

[voice]
# Operator setting for the last, content-locked pass in Stage 3 only.
# Integer levels 0..3 are defined in FORFATTERSTEMME.md.
# It does not govern evidence selection, drafting, claim strength or triage.
social_register_calibration = 2
```

**One queued check — run at the end of Cluster C:**

```powershell
& $Py -c "import tomllib; from pathlib import Path; s=tomllib.loads(Path('policy/settings.toml').read_text(encoding='utf-8')); assert s['voice']['social_register_calibration']==2; print('voice level 2')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E12') -Destination (Join-Path $Build 'policy/settings.toml') -Force
```

Restore later edits to this same file first. 

### E12a — Validate the manually edited dial in the existing settings loader

**One file:** [runtime/jobbsok/settings.py](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/runtime/jobbsok/settings.py>).

**Prerequisites:** E12. **Run boundary:** No independent snapshot change; finish before the same boundary as E12.

**Purpose:** M04 / C10; R01 and R10. Use the existing ConfigurationError route. No clamp, silent fallback, new schema, validation subsystem or historical-run rewrite.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'runtime/jobbsok/settings.py') -Destination (Join-Path $Rollback 'E12a')
```

**Exact anchor/current behavior:**

```text
    personality = data.get("personality", {})
    max_facets = personality.get("max_selected_facets")
    if max_facets != 3:
        raise ConfigurationError(
            f"{path.name}: [personality].max_selected_facets must be 3. The "
            "zero-to-three bound is the frozen interface (DEC-35, Spec 9.4)."
        )
```

**Replace the anchor once with exactly:**

```python
    personality = data.get("personality", {})
    max_facets = personality.get("max_selected_facets")
    if max_facets != 3:
        raise ConfigurationError(
            f"{path.name}: [personality].max_selected_facets must be 3. The "
            "zero-to-three bound is the frozen interface (DEC-35, Spec 9.4)."
        )

    voice = data.get("voice")
    if voice is not None:
        level = voice.get("social_register_calibration")
        if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 3:
            raise ConfigurationError(
                f"{path.name}: [voice].social_register_calibration must be an "
                "integer 0..3. FORFATTERSTEMME.md defines exactly those levels. "
                f"Found {level!r}."
            )
```

**One queued check — run at the end of Cluster C:**

```powershell
& $Py -c @'
import copy
import sys
from pathlib import Path
sys.path.insert(0, "runtime")
from jobbsok.settings import load_path, _check
from jobbsok.errors import ConfigurationError
path = Path("policy/settings.toml")
data = load_path(path)
assert data["voice"]["social_register_calibration"] == 2
historical = copy.deepcopy(data)
historical.pop("voice")
_check(historical, path)
for value in (0, 1, 2, 3):
    candidate = copy.deepcopy(data)
    candidate["voice"] = {"social_register_calibration": value}
    _check(candidate, path)
for voice in ({}, {"social_register_calibration": 4},
              {"social_register_calibration": "2"},
              {"social_register_calibration": 2.5},
              {"social_register_calibration": True}):
    candidate = copy.deepcopy(data)
    candidate["voice"] = voice
    try:
        _check(candidate, path)
    except ConfigurationError as exc:
        assert "integer 0..3" in str(exc)
    else:
        raise AssertionError(f"Invalid voice setting accepted: {voice!r}")
print("voice: default 2; 0..3 accepted; historical absence accepted; invalid values rejected")
'@
```

**Expected:** the stated checks succeed. This is not evidence of model compliance or output quality.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E12a') -Destination (Join-Path $Build 'runtime/jobbsok/settings.py') -Force
```

Restore later edits to this same file first.

### E13 — Expose the frozen voice setting only in Stage-3 authoring context

**One file:** [runtime/jobbsok/cli.py](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/runtime/jobbsok/cli.py:1168>).

**Prerequisites:** E12, E12a. **Run boundary:** no independent snapshot change; complete before the same boundary with its input dependencies.

**Purpose:** M04; mitigates C10.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'runtime/jobbsok/cli.py') -Destination (Join-Path $Rollback 'E13')
```

**Exact anchor/current behavior:**

```text
            "instruction": (
                "Return only semantic fields. Do not include tooling-owned fields; "
                "stage-submit validates and inserts canonical metadata before commit."
            ),
        },
    }

    if legacy:
```

**Replace the anchor once with exactly:**

```python
            "instruction": (
                "Return only semantic fields. Do not include tooling-owned fields; "
                "stage-submit validates and inserts canonical metadata before commit."
            ),
        },
    }

    if stage == 3 and envelope["mode"] == "FINAL_AND_REVIEW":
        voice = context.assets.settings.get("voice")
        if voice is not None:
            bundle["final_polish"] = {
                "social_register_calibration": voice["social_register_calibration"]
            }

    if legacy:
```

**One queued check — run at the end of Cluster C:**

```powershell
rg -n -A 7 -F 'if stage == 3 and envelope["mode"] == "FINAL_AND_REVIEW":' runtime/jobbsok/cli.py
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E13') -Destination (Join-Path $Build 'runtime/jobbsok/cli.py') -Force
```

Restore later edits to this same file first. 

### E14 — Define the bounded, manually tunable social-register pass

**One file:** [policy/writing/FORFATTERSTEMME.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/FORFATTERSTEMME.md:180>).

**Prerequisites:** E12, E13. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M04; mitigates C10; C08; C13.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/FORFATTERSTEMME.md') -Destination (Join-Path $Rollback 'E14')
```

**Exact anchor/current behavior:**

```text
## Uttrykkskilde for sluttpussen

Denne filen er uttrykkskilden for den avsluttende, innholdslåste pussen i
Stage 3. Når innholdet er låst, er det seksjonene over — målinntrykk,
argumentvaner, sosial temperatur, setningsarkitektur og selvfremstilling — som
avgjør hvordan det låste innholdet skal lyde.

Den pussen kan endre hvordan noe sies. Den kan aldri endre hva arbeidsgiveren
får vite.
```

**Replace the anchor once with exactly:**

```text
## Uttrykkskilde for sluttpussen

Denne filen er uttrykkskilden for den avsluttende, innholdslåste pussen i
Stage 3. Når innholdet er låst, er det seksjonene over — målinntrykk,
argumentvaner, sosial temperatur, setningsarkitektur og selvfremstilling — som
avgjør hvordan det låste innholdet skal lyde.

Den pussen kan endre hvordan noe sies. Den kan aldri endre hva arbeidsgiveren
får vite.

### Operatørstyrt sosialregister i siste puss

Denne mekanikken brukes bare i den siste, innholdslåste pussen i Stage 3
FINAL_AND_REVIEW. Den skal ikke leses eller brukes til utvalg, strategi,
utkast eller substansiell omskriving. REVIEW_ONLY utfører ingen registerpuss.
Nivået kommer fra final_polish.social_register_calibration i den fryste
Stage-3-bundelen, med kilde i [voice] i policy/settings.toml. Operatøren velger
heltall fra 0 til 3. Mangler feltet i en eldre fryst bunt, brukes ikke denne
utvidede registerpussen.

Alle nivåer har samme gulv: Behold hver materiell opplysning, personlig handling,
faglig vurdering, mottaker, kvalifikasjon, eierskapsgrense, status, periode,
arbeidsgiverbegrunnelse og argumentrekkefølge. Behold sterke støttede verb.
Ikke legg til ydmykhetsfraser, forbehold, svakere eierskap eller et diffust «vi».
Ikke fjern et case, kort ned for å nå et sidetall eller bytt ut dokumentert
skjønn med generelle kompetanseord. Nivået er et redaksjonelt valg, ikke en
kvalitetsskår eller en grad av påstått kompetanse.

Mønstrene nedenfor gjelder bare når de kan omformes uten å endre det låste
innholdet. De er ikke forbudte ord eller strenger:
- Forelesningspreg: Leseren får egen virksomhet forklart med en autoritet som
  det konkrete kandidatbidraget ikke trenger.
- Selvrangering eller eksakt-passform: En innramming annonserer hvor godt
  kandidaten passer, fremfor å la det allerede beskrevne arbeidet vise det.
- Gjentatt egenposisjonering: En relevansbro eller metakommentar sier på nytt
  det samme som den nærmeste teksten allerede gjør.
- Seiers- eller konfliktpreg: Måten et dokumentert valg presenteres på gjør
  samarbeidet til en rangering av personer. Behold selve valget, rammen,
  begrunnelsen og nødvendig attribusjon.
- Unødvendig avstand: Abstrakt innpakning, gjentatt setningsstart eller
  dokumentasjonsspråk gjør en allerede konkret handling vanskeligere å lese.

Nivå 0: Hopp over denne utvidede registerpussen. Den ordinære innholdslåste
stemmepussen gjelder fortsatt.

Nivå 1: Omform tydelig forelesningspreg, selvrangering og eksakt-passform der
endringen bare gjelder innramming eller allerede overflødig metatekst.

Nivå 2: Gjør nivå 1 og omform også gjentatt egenposisjonering og seiers- eller
konfliktpreg. Behold en spørsmålstilling eller metakommentar når den faktisk
bærer en egen del av argumentet. Annonsert abstraksjon er ingen automatisk
slettegrunn.

Nivå 3: Gjør nivå 2 og arbeid mer med lokal setningsrytme, subjektplassering
og avstand til leseren. Varier bare når samme handling og samme aktør fortsatt
er like tydelige. Et nødvendig «jeg» skal ikke bli et uklart passiv eller «vi».

Nivåene angir hvilke mønsterfamilier operatøren ønsker prioritert; de garanterer
ikke at to enkeltutkast blir forskjellige. Nivå 2 er et startpunkt, ikke et
målt optimum. Nivå 3 er høyeste nivå; det finnes ikke et eget innsatsnivå 4.

På alle aktive nivåer kan et faguttrykk få en betydningslik, mer lesbar
formulering. Forklar ikke en teknisk virkemåte som den låste teksten ikke
allerede fastslår. En term som må beholdes for presisjon, beholdes.

Gjør én sammenhengende puss, ikke en serie poengstyrte gjennomløp. Når en
foreslått endring ville endre en materiell opplysning, la den formuleringen
stå. Registerpussen kan ikke reparere en ustøttet påstand eller flytte en
nødvendig avgrensning til review. Håndter eventuelle slike funn etter de
eksisterende innholds- og triagereglene, uten å bruke registeret som grunnlag
for ny utvelgelse. Ingen telling av markører, ord eller evidensreferanser
avgjør om pussen er god.
```

**One queued check — run at the end of Cluster C:**

```powershell
rg -n -F 'Nivå 3 er høyeste nivå' policy/writing/FORFATTERSTEMME.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E14') -Destination (Join-Path $Build 'policy/writing/FORFATTERSTEMME.md') -Force
```

Restore later edits to this same file first. 

### E15 — Permit an ordinary closing without forced uniqueness

**One file:** [policy/writing/FORFATTERSTEMME.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/writing/FORFATTERSTEMME.md:133>).

**Prerequisites:** E14. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M06; mitigates C09; C13.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/writing/FORFATTERSTEMME.md') -Destination (Join-Path $Rollback 'E15')
```

**Exact anchor/current behavior:**

```text
1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …`
   som avslutning. Avslutt heller med noe som bare gjelder denne stillingen.
```

**Replace the anchor once with exactly:**

```text
1. `Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …`
   som generisk avslutning. En kort, naturlig invitasjon til samtale er
   tilstrekkelig når bidrag og motivasjon allerede er tydelige. Behold et
   stillingsspesifikt poeng når det tilfører noe; ikke finn på et nytt poeng
   bare for å gjøre avslutningen særegen. I innholdslåst puss beholdes alt
   materielt innhold også når avslutningen omformuleres.
```

**One queued check — run at the end of Cluster C:**

```powershell
rg -n -F 'En kort, naturlig invitasjon til samtale er' policy/writing/FORFATTERSTEMME.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E15') -Destination (Join-Path $Build 'policy/writing/FORFATTERSTEMME.md') -Force
```

Restore later edits to this same file first. 

### E16 — Call the register mechanism only inside the final content lock

**One file:** [policy/stages/stage3_final_writer_review.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/policy/stages/stage3_final_writer_review.md:156>).

**Prerequisites:** E14, E15. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M04; mitigates C10.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Destination (Join-Path $Rollback 'E16')
```

**Exact anchor/current behavior:**

```text
>
> Express the locked content so a Norwegian hiring manager is likely to
> experience the writer as competent, grounded, useful, interesting, credible
> and easy to work with, rather than impressive-seeking, intense or
> self-conscious.
```

**Replace the anchor once with exactly:**

```text
>
> Express the locked content so a Norwegian hiring manager is likely to
> experience the writer as competent, grounded, useful, interesting, credible
> and easy to work with, rather than impressive-seeking, intense or
> self-conscious.
>
> Only now, in FINAL_AND_REVIEW after the substantive content is locked, read
> FORFATTERSTEMME.md and apply its ordinary expression guidance. If the bundle
> contains final_polish.social_register_calibration, apply the corresponding
> extended register pass from that file once, still under this entire lock.
> A missing setting means no extended pass for that historical bundle.
> REVIEW_ONLY performs no polish. The setting never governs evidence selection,
> drafting, substantive repair, claim strength, page fit or triage. Do not add
> a review field, marker count, evidence-preservation list or quality score.
```

**One queued check — run at the end of Cluster C:**

```powershell
rg -n -F 'Only now, in FINAL_AND_REVIEW after the substantive content is locked' policy/stages/stage3_final_writer_review.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E16') -Destination (Join-Path $Build 'policy/stages/stage3_final_writer_review.md') -Force
```

Restore later edits to this same file first. 

### E17 — Delay opening the voice file until the final pass

**One file:** [prompts/STAGE3_PROMPT.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/prompts/STAGE3_PROMPT.md:96>).

**Prerequisites:** E16. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M04; mitigates C10.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'prompts/STAGE3_PROMPT.md') -Destination (Join-Path $Rollback 'E17')
```

**Exact anchor/current behavior:**

```text
   - Apply the named writing-doctrine sections before choosing triage. Apply
     `FORFATTERSTEMME.md` only after the package is factually and strategically
     grounded: it governs expression, and can never create or remove a
     proposition, move a claim ceiling, change a lifecycle state or select
     evidence.
```

**Replace the anchor once with exactly:**

```text
   - Apply the named WRITING_DOCTRINE.md sections and
     PERSUASION_CALIBRATION.md during substantive authoring and before triage.
     Defer opening FORFATTERSTEMME.md from read.writing_policy until the
     Final polish content lock in FINAL_AND_REVIEW. Its register guidance and
     the bundle's final_polish setting are not drafting inputs. At that final
     pass, follow the frozen stage instruction. REVIEW_ONLY performs no polish.
     Voice can never create or remove a proposition, move a claim ceiling,
     change a lifecycle state or select evidence.
```

**One queued check — run at the end of Cluster C:**

```powershell
rg -n -F 'Defer opening FORFATTERSTEMME.md' prompts/STAGE3_PROMPT.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E17') -Destination (Join-Path $Build 'prompts/STAGE3_PROMPT.md') -Force
```

Restore later edits to this same file first. 

## Cluster D — Master corrections and existing consumer alignment

Prerequisites: A and C complete. E18 is the cheap competence-style subset; E19/E20 are subsequent CV-flow edits. E21–E24 form the letter-master contract change. E25–E27 maintain current source evidence without changing the old observations. Do not render or freeze the partially changed pair. No content controls are added and no extra semantic zone is activated.

### E18 — Remove the competence wall's uniform bold weight

**One file:** [templates/CV_MASTER.docx](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/templates/CV_MASTER.docx>).

**Prerequisites:** none. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M05; mitigates C11.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'templates/CV_MASTER.docx') -Destination (Join-Path $Rollback 'E18')
```

**Exact anchor/current behavior:**

word/document.xml: CV_CORE_COMPETENCE / w:sdtContent / w:p / w:r / w:rPr contains <w:b/>. Remove that element. Keep one joined paragraph and the KJERNEOMRÅDER prefix. Do not add a label paragraph or change the map/renderer. The label loses bold emphasis but retains uppercase letters and the existing teal colour; this deliberately avoids an extra line. Current Normal/docDefaults supply no inherited bold.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
import re
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path("runtime").resolve()))
from jobbsok.docxfill import read_document, iter_controls, _merge_root_tag, DOCUMENT_PART, W

path = Path("templates/CV_MASTER.docx")
tree, original_root = read_document(path)
control = dict(iter_controls(tree))["CV_CORE_COMPETENCE"]
bold = control.find(f".//{W}rPr/{W}b")
control.find(f".//{W}rPr").remove(bold)
body_bytes = ET.tostring(tree, encoding="utf-8", xml_declaration=False)
generated_root = re.match(rb"<[^>]+>", body_bytes)
xml = (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       + _merge_root_tag(original_root, generated_root.group(0))
       + body_bytes[generated_root.end():])
buffer = BytesIO()
with ZipFile(path) as source, ZipFile(buffer, "w") as target:
    for item in source.infolist():
        target.writestr(item, xml if item.filename == DOCUMENT_PART
                        else source.read(item.filename))
path.write_bytes(buffer.getvalue())
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "import sys; sys.path.insert(0,'runtime'); from pathlib import Path; from jobbsok.docxfill import *; r,_=read_document(Path('templates/CV_MASTER.docx')); c=dict(iter_controls(r))['CV_CORE_COMPETENCE']; assert c.find('.//'+W+'rPr/'+W+'b') is None; print('competence direct bold removed')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E18') -Destination (Join-Path $Build 'templates/CV_MASTER.docx') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E19 — Release the chain of earlier employments

**One file:** [templates/CV_MASTER.docx](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/templates/CV_MASTER.docx>).

**Prerequisites:** E18. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M05; mitigates C14.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'templates/CV_MASTER.docx') -Destination (Join-Path $Rollback 'E19')
```

**Exact anchor/current behavior:**

word/document.xml: CV_OPTIONAL_PREVIOUS_EXPERIENCE, second prototype paragraph, identified by {{CV_PREVIOUS_EXPERIENCE_CONTENT}}, has <w:keepNext/> and no w:keepLines. fill_block clones that paragraph for every older employment.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
import re
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path("runtime").resolve()))
from jobbsok.docxfill import read_document, iter_controls, _merge_root_tag, DOCUMENT_PART, W

path = Path("templates/CV_MASTER.docx")
tree, original_root = read_document(path)
control = dict(iter_controls(tree))["CV_OPTIONAL_PREVIOUS_EXPERIENCE"]
paragraph = control.find(f"{W}sdtContent").findall(f"{W}p")[1]
properties = paragraph.find(f"{W}pPr")
keep_next = properties.find(f"{W}keepNext")
position = list(properties).index(keep_next)
properties.remove(keep_next)
properties.insert(position, ET.Element(f"{W}keepLines"))
body_bytes = ET.tostring(tree, encoding="utf-8", xml_declaration=False)
generated_root = re.match(rb"<[^>]+>", body_bytes)
xml = (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       + _merge_root_tag(original_root, generated_root.group(0))
       + body_bytes[generated_root.end():])
buffer = BytesIO()
with ZipFile(path) as source, ZipFile(buffer, "w") as target:
    for item in source.infolist():
        target.writestr(item, xml if item.filename == DOCUMENT_PART
                        else source.read(item.filename))
path.write_bytes(buffer.getvalue())
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "import sys; sys.path.insert(0,'runtime'); from pathlib import Path; from jobbsok.docxfill import *; r,_=read_document(Path('templates/CV_MASTER.docx')); p=dict(iter_controls(r))['CV_OPTIONAL_PREVIOUS_EXPERIENCE'].find(W+'sdtContent').findall(W+'p')[1]; assert p.find(W+'pPr/'+W+'keepNext') is None and p.find(W+'pPr/'+W+'keepLines') is not None; print('one employment kept together; chain removed')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E19') -Destination (Join-Path $Build 'templates/CV_MASTER.docx') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E20 — Move low-priority support below earlier experience and languages

**One file:** [templates/CV_MASTER.docx](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/templates/CV_MASTER.docx>).

**Prerequisites:** E19. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M05; mitigates C11; C14.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'templates/CV_MASTER.docx') -Destination (Join-Path $Rollback 'E20')
```

**Exact anchor/current behavior:**

After CV_RELEVANT_BACHELOR_SUBJECTS the body currently orders CV_SUPPORT_SECTION_1, CV_SUPPORT_SECTION_2, CV_SUPPORT_SECTION_3, CV_OPTIONAL_PREVIOUS_EXPERIENCE, CV_OPTIONAL_TRUST, CV_OPTIONAL_LANGUAGES.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
import re
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path("runtime").resolve()))
from jobbsok.docxfill import read_document, iter_controls, _merge_root_tag, DOCUMENT_PART, W

path = Path("templates/CV_MASTER.docx")
tree, original_root = read_document(path)
controls = dict(iter_controls(tree))
body = tree.find(f"{W}body")
order = [
    "CV_OPTIONAL_PREVIOUS_EXPERIENCE",
    "CV_OPTIONAL_TRUST",
    "CV_OPTIONAL_LANGUAGES",
    "CV_SUPPORT_SECTION_1",
    "CV_SUPPORT_SECTION_2",
    "CV_SUPPORT_SECTION_3",
]
for tag in order:
    body.remove(controls[tag])
position = list(body).index(controls["CV_RELEVANT_BACHELOR_SUBJECTS"]) + 1
for offset, tag in enumerate(order):
    body.insert(position + offset, controls[tag])
body_bytes = ET.tostring(tree, encoding="utf-8", xml_declaration=False)
generated_root = re.match(rb"<[^>]+>", body_bytes)
xml = (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       + _merge_root_tag(original_root, generated_root.group(0))
       + body_bytes[generated_root.end():])
buffer = BytesIO()
with ZipFile(path) as source, ZipFile(buffer, "w") as target:
    for item in source.infolist():
        target.writestr(item, xml if item.filename == DOCUMENT_PART
                        else source.read(item.filename))
path.write_bytes(buffer.getvalue())
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "import sys; sys.path.insert(0,'runtime'); from pathlib import Path; from jobbsok.docxfill import *; r,_=read_document(Path('templates/CV_MASTER.docx')); t=[x for x,_ in iter_controls(r)]; assert t[-6:]==['CV_OPTIONAL_PREVIOUS_EXPERIENCE','CV_OPTIONAL_TRUST','CV_OPTIONAL_LANGUAGES','CV_SUPPORT_SECTION_1','CV_SUPPORT_SECTION_2','CV_SUPPORT_SECTION_3']; print('CV tail order correct')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E20') -Destination (Join-Path $Build 'templates/CV_MASTER.docx') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E21 — Keep one subject title and preserve the optional reference

**One file:** [templates/APPLICATION_MASTER.docx](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/templates/APPLICATION_MASTER.docx>).

**Prerequisites:** none. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M05; mitigates C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'templates/APPLICATION_MASTER.docx') -Destination (Join-Path $Rollback 'E21')
```

**Exact anchor/current behavior:**

word/document.xml: first table has row 1 [APP_EMPLOYER + APP_UNIT_OPTIONAL; Oslo, APP_DATE] and row 2 [Stilling: APP_JOB_TITLE; APP_REFERENCE_OPTIONAL]. A second APP_JOB_TITLE occurs in the separate subject paragraph. The right cell in row 2 is not empty: it owns APP_REFERENCE_OPTIONAL, whose paragraph has right alignment for that cell. Remove its direct w:jc on relocation. With a null reference, fill_block clears it and unwrapping contributes zero body children, so the subject directly follows the table. Batch D exercises null and populated references.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
import re
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path("runtime").resolve()))
from jobbsok.docxfill import read_document, iter_controls, _merge_root_tag, DOCUMENT_PART, W

path = Path("templates/APPLICATION_MASTER.docx")
tree, original_root = read_document(path)
body = tree.find(f"{W}body")
table = body.find(f"{W}tbl")
row = table.findall(f"{W}tr")[1]
reference = dict(iter_controls(tree))["APP_REFERENCE_OPTIONAL"]
parents = {child: parent for parent in tree.iter() for child in parent}
parents[reference].remove(reference)
table.remove(row)
body.insert(list(body).index(table) + 1, reference)
for paragraph in reference.find(f"{W}sdtContent").findall(f"{W}p"):
    properties = paragraph.find(f"{W}pPr")
    justification = properties.find(f"{W}jc") if properties is not None else None
    if justification is not None:
        properties.remove(justification)
body_bytes = ET.tostring(tree, encoding="utf-8", xml_declaration=False)
generated_root = re.match(rb"<[^>]+>", body_bytes)
xml = (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       + _merge_root_tag(original_root, generated_root.group(0))
       + body_bytes[generated_root.end():])
buffer = BytesIO()
with ZipFile(path) as source, ZipFile(buffer, "w") as target:
    for item in source.infolist():
        target.writestr(item, xml if item.filename == DOCUMENT_PART
                        else source.read(item.filename))
path.write_bytes(buffer.getvalue())
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "import sys; sys.path.insert(0,'runtime'); from pathlib import Path; from jobbsok.docxfill import *; p=Path('templates/APPLICATION_MASTER.docx'); c=control_inventory(p); r,_=read_document(p); assert sum(c.values())==6 and c['APP_JOB_TITLE']==1 and c['APP_REFERENCE_OPTIONAL']==1 and c['APP_DATE']==1; assert len(r.find(W+'body/'+W+'tbl').findall(W+'tr'))==1; ref=dict(iter_controls(r))['APP_REFERENCE_OPTIONAL']; assert ref in list(r.find(W+'body')) and ref.find('.//'+W+'jc') is None; print('one subject; body-level reference left-aligned; date retained')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E21') -Destination (Join-Path $Build 'templates/APPLICATION_MASTER.docx') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E22 — Align the canonical map with the revised letter master

**One file:** [templates/template_map.json](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/templates/template_map.json>).

**Prerequisites:** E21. **Run boundary:** YES — the changed maintained input must be frozen into the one new/child run.

**Purpose:** M05; mitigates C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'templates/template_map.json') -Destination (Join-Path $Rollback 'E22')
```

**Exact anchor/current behavior:**

documents.letter.controls.APP_JOB_TITLE = {"kind":"inline","count":2,"source":"job.title","required":true,"note":"Appears twice in the master: the reference block and the subject line. Both are filled."}
The top-level note says 17 CV controls and 7 letter controls (6 unique; APP_JOB_TITLE twice).

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
import json
path = Path("templates/template_map.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["documents"]["letter"]["controls"]["APP_JOB_TITLE"] = {
    "kind": "inline",
    "count": 1,
    "source": "job.title",
    "required": True,
    "note": "Filled once in the subject line. The optional reference remains a separate control below the address/date table."
}
data["note"] = (
    "The ONE canonical package-to-template map (Contract 13.3). Code, "
    "documentation and tests consume this file and no other. Duplicate, "
    "missing or unknown controls fail preflight rather than being ignored "
    "(Spec 16.3). CV_MASTER.docx carries 17 non-data-bound SDTs and "
    "APPLICATION_MASTER.docx carries 6, one per tag. Neither master uses "
    "w:dataBinding or docPartObj."
)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "import json; from pathlib import Path; m=json.loads(Path('templates/template_map.json').read_text(encoding='utf-8')); assert m['documents']['letter']['controls']['APP_JOB_TITLE']['count']==1; assert m['documents']['cv']['controls']['CV_CORE_COMPETENCE']['transform']=='join_middot'; print('map count 1; existing competence transform retained')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E22') -Destination (Join-Path $Build 'templates/template_map.json') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E23 — Keep the existing master-maintenance tool compatible

**One file:** [runtime/tools/prepare_masters.py](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/runtime/tools/prepare_masters.py>).

**Prerequisites:** E18, E19, E20, E21, E22. **Run boundary:** no independent snapshot change; complete before the same boundary with its input dependencies.

**Purpose:** M05; mitigates C11; C12; C14.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'runtime/tools/prepare_masters.py') -Destination (Join-Path $Rollback 'E23')
```

**Exact anchor/current behavior:**

The LETTER_PARAGRAPHS table requires the "Stilling:" paragraph at line 185. _resolve_anchors requires every body paragraph to be claimed once. The module's lines 35–37 describe an invariant of 7 total letter controls. After E21 that paragraph no longer exists. The current _KEEP behavior preserves the CV edits; no new CV transform is needed.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
path = Path("runtime/tools/prepare_masters.py")
text = path.read_text(encoding="utf-8")
old_text = text
text = text.replace(
    '    (("text", "Stilling:"), [(17, 20, *_KEEP), (17, 20, *_KEEP)]),\n',
    "", 1
)
assert text != old_text, "E23: anchor drifted; re-read prepare_masters.py"
old_text = text
text = text.replace(
    "The control contract is deliberately untouched: the 17 CV tags and the 6\n"
    "unique / 7 total letter tags must survive byte-for-byte in structure, and\n"
    "the tool verifies that before writing.",
    "The maintenance pass preserves the control inventory of its input masters.\n"
    "The current masters carry 17 CV controls and 6 letter controls, one per tag;\n"
    "templates/template_map.json owns the current render contract.", 1
)
assert text != old_text, "E23: anchor drifted; re-read prepare_masters.py"
old_text = text
text = text.replace(
    "#: APPLICATION_MASTER.docx -- all 8 body paragraphs, 7 sized runs.\n"
    "#: Paragraphs 6 to 8 are style-driven (Title, Normal) and keep no inline size.",
    "#: APPLICATION_MASTER.docx -- all 7 body paragraphs, 5 sized runs.\n"
    "#: Paragraphs 5 to 7 are style-driven (Title, Normal) and keep no inline size.", 1
)
assert text != old_text, "E23: anchor drifted; re-read prepare_masters.py"
old_text = text
text = text.replace(
    "Anchors are SDT tags for the 24\n# controls",
    "Anchors are SDT tags for the 23\n# controls", 1
)
assert text != old_text, "E23: anchor drifted; re-read prepare_masters.py"
path.write_text(text, encoding="utf-8")
```

**One queued check — run at the end of Cluster D:**

```powershell
rg -n -F 'The current masters carry 17 CV controls and 6 letter controls' runtime/tools/prepare_masters.py
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E23') -Destination (Join-Path $Build 'runtime/tools/prepare_masters.py') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E24 — Update the existing actual-master assertion

**One file:** [runtime/tests/test_t16_t18_containment_template.py](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/runtime/tests/test_t16_t18_containment_template.py:383>).

**Prerequisites:** E22, E23. **Run boundary:** no independent snapshot change; complete before the same boundary with its input dependencies.

**Purpose:** M05; mitigates C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'runtime/tests/test_t16_t18_containment_template.py') -Destination (Join-Path $Rollback 'E24')
```

**Exact anchor/current behavior:**

```text
    assert dict(control_inventory(layout.templates / "CV_MASTER.docx")).__len__() == 17
    letter = control_inventory(layout.templates / "APPLICATION_MASTER.docx")
    assert len(letter) == 6 and sum(letter.values()) == 7
```

**Replace the anchor once with exactly:**

```python
    assert dict(control_inventory(layout.templates / "CV_MASTER.docx")).__len__() == 17
    letter = control_inventory(layout.templates / "APPLICATION_MASTER.docx")
    assert len(letter) == 6 and sum(letter.values()) == 6
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -m pytest runtime/tests/test_t16_t18_containment_template.py::test_t18_actual_masters_match_the_single_canonical_map runtime/tests/test_t16_t18_containment_template.py::test_t18_masters_are_not_data_bound -q
```

**Expected:** both existing T18 tests pass. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E24') -Destination (Join-Path $Build 'runtime/tests/test_t16_t18_containment_template.py') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E25 — Add current master measurements without rewriting historical observations

**One file:** [evidence/gates/GATE-02/inventory.json](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/evidence/gates/GATE-02/inventory.json>).

**Prerequisites:** E18, E19, E20, E21, E22, E23, E24. **Run boundary:** no independent snapshot change; complete before the same boundary with its input dependencies.

**Purpose:** M05; mitigates C14; C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'evidence/gates/GATE-02/inventory.json') -Destination (Join-Path $Rollback 'E25')
```

**Exact anchor/current behavior:**

The JSON contains original_p07/* and prepared/* entries from the historical GATE-02 run. Their hashes already differ from the current masters. Preserve all four existing entries.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
from hashlib import sha256
import json
import sys
sys.path.insert(0, str(Path("runtime").resolve()))
from jobbsok.docxfill import control_inventory, binding_report
path = Path("evidence/gates/GATE-02/inventory.json")
data = json.loads(path.read_text(encoding="utf-8"))
for name in ("CV_MASTER.docx", "APPLICATION_MASTER.docx"):
    master = Path("templates") / name
    controls = dict(control_inventory(master))
    raw = master.read_bytes()
    data["avinor_optimization/" + name] = {
        "sha256": sha256(raw).hexdigest(),
        "bytes": len(raw),
        "controls": controls,
        "control_total": sum(controls.values()),
        "bindings": binding_report(master)
    }
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "import json; from pathlib import Path; d=json.loads(Path('evidence/gates/GATE-02/inventory.json').read_text(encoding='utf-8')); assert d['prepared/APPLICATION_MASTER.docx']['control_total']==7; assert d['avinor_optimization/APPLICATION_MASTER.docx']['control_total']==6; assert d['avinor_optimization/CV_MASTER.docx']['control_total']==17; print('historical 7 retained; current 6 recorded')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E25') -Destination (Join-Path $Build 'evidence/gates/GATE-02/inventory.json') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E26 — Distinguish the new source inventory from the historical Word gate

**One file:** [evidence/gates/GATE-02/GATE-02.md](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/evidence/gates/GATE-02/GATE-02.md>).

**Prerequisites:** E25. **Run boundary:** no independent snapshot change; complete before the same boundary with its input dependencies.

**Purpose:** M05; mitigates C14; C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'evidence/gates/GATE-02/GATE-02.md') -Destination (Join-Path $Rollback 'E26')
```

**Exact anchor/current behavior:**

The file already labels itself historical and records a dated PASS for the old 17/7 masters. Append after its final paragraph; do not change that historical result.

**Append exactly at end of the file:**

```text

## Avinor optimisation source revision

The source-maintenance revision uses 17 CV controls and 6 letter controls,
one per tag. The optional reference is below the letter's address/date
table; the subject contains the only APP_JOB_TITLE. The CV keeps its
existing competence transform with regular text, releases the earlier-role
keepNext chain, and places earlier experience and languages before the
support sections.

The avinor_optimization entries in inventory.json record the revised source
bytes and control structure. The original_p07 and prepared entries above
remain historical observations. This addition is not a new Word-open,
pagination or PDF gate result. Those properties must be observed on the
next normally finalized and rendered package; an absent PDF page count
does not establish that a page target was met.

```

**One queued check — run at the end of Cluster D:**

```powershell
rg -n -F 'This addition is not a new Word-open,' evidence/gates/GATE-02/GATE-02.md
```

**Expected:** the exact displayed marker is present at the intended location. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E26') -Destination (Join-Path $Build 'evidence/gates/GATE-02/GATE-02.md') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

### E27 — Refresh only the affected registry entries

**One file:** [evidence/finalization/HASHES.sha256](<C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26/P0.9/Build/evidence/finalization/HASHES.sha256>).

**Prerequisites:** all mandatory steps in A (E01–E07 including E04a), C (E12–E17 including E12a), and D through E26 completed. Add E08–E10 only if the core correction was explicitly accepted; add E11 only if separately accepted. Unaccepted B steps are skipped and never block E27. **Run boundary:** no independent snapshot change; finish before the single boundary. Keep AVINOR_ROLLBACK set to the original session directory.

**Purpose:** M05; mitigates C14; C12.

**Capture reversal bytes before this edit:**

```powershell
Copy-Item -LiteralPath (Join-Path $Build 'evidence/finalization/HASHES.sha256') -Destination (Join-Path $Rollback 'E27')
```

**Exact anchor/current behavior:**

The registry includes historical hashes, including masters aff96d15… and 80a41a75…, which already differ from the live masters 3e41cf96… and 4eab1778…. It is not a current whole-tree PASS. Keep unrelated lines. Derive affected paths from existing per-step reversal copies: compare each file with its earliest executed-step copy and refresh it only if its current bytes differ. The mapping includes E04a and E12a; it is not a new execution log.

**Exact one-file transformation:** Execute the following complete Python payload from Build. It changes only the named file. The template transformations preserve every other zip payload; they do not use the final-package fill function or unwrap controls.

```python
from pathlib import Path
from hashlib import sha256
path = Path("evidence/finalization/HASHES.sha256")
import os
rollback = Path(os.environ["AVINOR_ROLLBACK"])
step_files = [
    ("E01", "policy/writing/WRITING_DOCTRINE.md"),
    ("E02", "policy/writing/WRITING_DOCTRINE.md"),
    ("E03", "policy/stages/stage1_decision_architecture.md"),
    ("E04", "policy/stages/stage3_final_writer_review.md"),
    ("E04a", "policy/stages/stage3_final_writer_review.md"),
    ("E05", "policy/stages/stage3_final_writer_review.md"),
    ("E06", "policy/writing/WRITING_DOCTRINE.md"),
    ("E07", "policy/writing/WRITING_DOCTRINE.md"),
    ("E08", "policy/writing/PERSUASION_CALIBRATION.md"),
    ("E09", "policy/writing/PERSUASION_CALIBRATION.md"),
    ("E10", "policy/writing/PERSUASION_CALIBRATION.md"),
    ("E11", "policy/writing/PERSUASION_CALIBRATION.md"),
    ("E12", "policy/settings.toml"),
    ("E12a", "runtime/jobbsok/settings.py"),
    ("E13", "runtime/jobbsok/cli.py"),
    ("E14", "policy/writing/FORFATTERSTEMME.md"),
    ("E15", "policy/writing/FORFATTERSTEMME.md"),
    ("E16", "policy/stages/stage3_final_writer_review.md"),
    ("E17", "prompts/STAGE3_PROMPT.md"),
    ("E18", "templates/CV_MASTER.docx"),
    ("E19", "templates/CV_MASTER.docx"),
    ("E20", "templates/CV_MASTER.docx"),
    ("E21", "templates/APPLICATION_MASTER.docx"),
    ("E22", "templates/template_map.json"),
    ("E23", "runtime/tools/prepare_masters.py"),
    ("E24", "runtime/tests/test_t16_t18_containment_template.py"),
    ("E25", "evidence/gates/GATE-02/inventory.json"),
    ("E26", "evidence/gates/GATE-02/GATE-02.md"),
]
before = {}
for step_id, relative in step_files:
    backup = rollback / step_id
    if backup.is_file() and relative not in before:
        before[relative] = backup.read_bytes()
affected = [relative for relative, original in before.items()
            if Path(relative).read_bytes() != original]
lines = path.read_text(encoding="utf-8").splitlines()
by_path = {
    line.split("  ", 1)[1]: i
    for i, line in enumerate(lines)
    if line and not line.startswith("#") and "  " in line
}
new_lines = []
for relative in affected:
    digest = sha256(Path(relative).read_bytes()).hexdigest()
    replacement = digest + "  " + relative
    if relative in by_path:
        lines[by_path[relative]] = replacement
    else:
        new_lines.append(replacement)
lines += [
    "# Avinor optimisation: only actually changed maintenance surfaces were refreshed.",
    "# Unrelated entries retain their historical provenance; this is not a new gate PASS."
]
lines += new_lines
path.write_text("\n".join(lines) + "\n", encoding="utf-8")
```

**One queued check — run at the end of Cluster D:**

```powershell
& $Py -c "from pathlib import Path; from hashlib import sha256; p='templates/APPLICATION_MASTER.docx'; expected=sha256(Path(p).read_bytes()).hexdigest()+'  '+p; assert expected in Path('evidence/finalization/HASHES.sha256').read_text(encoding='utf-8').splitlines(); print('revised letter master registered')"
```

**Expected:** the assertion succeeds and the printed statement describes the expected value. This check is limited to that source/contract property.

**Reverse this step:**

```powershell
Copy-Item -LiteralPath (Join-Path $Rollback 'E27') -Destination (Join-Path $Build 'evidence/finalization/HASHES.sha256') -Force
```

Restore later edits to this same file first. Do not use a partially restored master/map/tool combination for rendering.

## Cluster validation and the single run boundary

The check printed in each step is the concrete property to verify. Run the checks as the following four **batches**, not after every edit:

| Batch | Run after | Checks to include once | What it does not prove |
|---|---|---|---|
| A | E07 | E01–E07 and E04a marker checks in one shell invocation. Inspect the edited S1 and S3 sequence together: requirements remain existing fields; content changes end before final polish. | An actual generated pair covers the vacancy. |
| B | E10, or E11 if explicitly accepted | Only the selected E08–E11 marker checks, in one invocation. Read the complete K section once to verify the strong-verb and necessary-caveat exceptions remain. Skip this entire batch if no correction was accepted. | That a model applies the correction reliably. |
| C | E17 | E12–E17 and E12a checks in one invocation. Read the E13 block with its Stage-3 FINAL_AND_REVIEW guard; parse the module as below. Stage 1's writing-policy filenames remain exactly D and K. | Hard filesystem isolation or measured benefit of level 2. |
| D | E27 | E18–E23 and E25–E27 checks, plus E24's existing two T18 tests **once** in the same batch. No new tests. Run the existing preparation check and the disposable fill check below once each; neither invokes Word. The fill check creates only temporary outputs and removes them. | Word-open, PDF pagination, or a new whole-repository GATE PASS. |

For C, syntax-check the two changed modules without producing cache files:

```powershell
& $Py -c "import ast; from pathlib import Path; [ast.parse(Path(p).read_text(encoding='utf-8')) for p in ('runtime/jobbsok/cli.py','runtime/jobbsok/settings.py')]; print('CLI and settings parse')"
```

For D, run the existing maintenance command from its runtime import directory:

```powershell
Push-Location -LiteralPath (Join-Path $Build 'runtime')
try {
    & $Py -m tools.prepare_masters --check
} finally {
    Pop-Location
}
```

Expected: no refusal, control inventory preserved at **17 CV / 6 letter**. The check's canonical core-property comparison may report work independently of these layout edits; do not launch an unrelated metadata repair. No Word process is started by this check. If restoring a rejected template step, restore its dependent map/tool/test/evidence edits before any subsequent render.

For D, after the preparation check, run this **single disposable fill command**. It covers E18–E24 using the existing fixture and the live masters/map. `_build_document` is the actual `render_job` call site: it constructs `edit`, resolves the canonical map, calls `fill_inline`/`fill_block`, then calls `write_filled_docx`, which unwraps and asserts. There is no guessed callback, new renderer, CLI mode or test file. The date and reference here are fixed mechanical-check inputs, not production finalization metadata or candidate claims.

```powershell
& $Py -c @'
import json
import tempfile
import sys
from pathlib import Path
sys.path.insert(0, "runtime")
from jobbsok.paths import Layout
from jobbsok.merge import effective_cv
from jobbsok.render import _build_document, resolve_substitutions
from jobbsok.docxfill import read_document, visible_text, normalized, assert_no_controls, W
build = Path.cwd()
pkg = json.loads(Path("evidence/vertical_slice/fixtures/final_package.json").read_text(encoding="utf-8"))
baseline = json.loads(Path("generated/baseline_map.json").read_text(encoding="utf-8"))
template_map = json.loads(Path("templates/template_map.json").read_text(encoding="utf-8"))
effective = effective_cv(baseline, pkg)
job = {key: pkg["binding"][key] for key in ("job_id", "employer", "title")}
job.update(unit=None, reference=None)
with tempfile.TemporaryDirectory(prefix="avinor-fill-") as directory:
    for component, spec in template_map["documents"].items():
        references = [None] if component == "cv" else [None, "474473271"]
        for reference in references:
            case = dict(job, reference=reference)
            output = Path(directory) / f"{component}-{reference or 'none'}.docx"
            _build_document(
                Layout(build), spec, output, master=build / spec["master"],
                effective=effective, package=pkg, job=case,
                document_date="2026-09-12",
            )
            assert output.is_file() and output.stat().st_size > 0
            tree, _ = read_document(output)
            assert_no_controls(tree, output.name)
            text = normalized(visible_text(output)).casefold()
            for anchor in spec["verification"]["identity"]:
                expected = normalized(resolve_substitutions(anchor, effective, case)).casefold()
                assert expected and expected in text, (component, anchor)
            if component == "letter":
                body = tree.find(f"{W}body")
                table = body.find(f"{W}tbl")
                following = list(body)[list(body).index(table) + 1]
                following_text = "".join(node.text or "" for node in following.iter(f"{W}t"))
                if reference is None:
                    assert following_text == "Søknad: " + case["title"]
                else:
                    assert following_text == "Referanse: " + reference
                    assert following.find(f"{W}pPr/{W}jc") is None
            print(component, reference, "filled; identity present; no residual controls")
print("Temporary fills removed; no Word or PDF invoked")
'@
```

Expected: one CV and two letter fills succeed; identity text survives; no control remains. With no reference, the subject is the first body block after the table; with a reference, the left-inheriting reference paragraph occupies that position. TemporaryDirectory removes all outputs. **Reversal:** no source edit occurs; only temporary files are created and automatically removed. A failure blocks use of the changed master/map combination until the responsible E18–E24 edit is corrected or reversed, not semantic submission on a new criterion. This does not establish Word-open compatibility, pagination, typography or recruitment quality.

### Exactly one boundary for this implementation

**End all source maintenance here.** E12 changes settings and E12a validates that input; E01–E17 (including E04a) change the named policy/prompt inputs and context transport; E18–E22 change templates/map. DEC-40 requires a new or child run to consume these versions. Runtime and evidence-maintenance files are not themselves an excuse to edit a frozen snapshot.

Use **one child from Stage 1** of the existing Avinor source run, after the actual baseline-to-authorities comparison has been made. The operator supplies the identity of the person who really performed that comparison; do not invent “Vegard reviewed” metadata. This is required run input, not an unresolved design decision. No new schemas are involved.

The existing public command is:

```powershell
# $ActualReviewer is the truthful operator-supplied reviewer identity.
& $Py -m jobbsok branch --run r20260908-154257-0fa53b --from-stage 1 --model-tag avinor_master --reviewed-by $ActualReviewer
```

Run it from Build only when source maintenance and the required review are complete. Use the child reference **returned by that command**; do not invent a timestamped child path, mutate the parent, create another intermediate freeze, or treat the operator model tag as verified model execution provenance. The command's syntax and --from-stage choices were checked in live cli.py:1327–1342.

Before that child's Stage 1, its context must still omit FORFATTERSTEMME from writing_policy and omit final_polish. In its Stage-3 FINAL_AND_REVIEW context, final_polish.social_register_calibration must equal the value in the child's **frozen** policy/settings.toml (default 2), and writing_policy may name V, which the prompt now defers opening until final polish. A REVIEW_ONLY context must omit final_polish. These are checks of the normal context already needed for execution, not a new test artifact or a second freeze.

The child regenerates strategy and final authoring through the normal next/context/stage-submit workflow. No stage-2 resurrection. Use the exact submission command in the fresh context; then normal finalize and render, once each for the completed package. Do not introduce --probe or edit a finalized package in place to meet a page target.

Inspect the resulting CV and letter together once. Expected observations:

- The strongest supported gain judgment remains, while a documented interaction or useful breadth can answer a previously weak role function. If an actually supported material MINIMUM/IMPORTANT answer is absent from both documents, review.notes names that supported part and gives the reason. Silence is a failure of the note duty only if an eligible omission actually exists; notes alone do not prove coverage or causal improvement.
- No unsupported “not implemented”, false portfolio mandate, PRJ-04/06 transfer or merged 2025/2027 treatment is introduced.
- The new register guidance was applied only after content lock; strong verbs, attribution and meaningful caveats survived.
- One subject title, reference/date retained, regular competence text and the reordered CV tail.
- Actual PDF page counts when conversion succeeds. Null counts remain unknown; a 3-page CV or 2-page letter is an editorial observation, not automatic CHECK.

If the operator later tunes **only** the knob, set the chosen integer 0–3 in the live TOML and explicitly create a **new** child with --from-stage 3. The current automatic settings comparison does not include arbitrary future voice keys. Do not amend the previously frozen file or add branch machinery for this purpose. This describes a later separate tuning task, not another boundary in the present implementation.

### Reversal and completion

A step's restore command returns exactly its file to the bytes captured before that step. Reverse later same-file steps first. After restoring a connected template change, restore dependent contract/evidence edits as well before using the source tree. Preserve the parent run regardless of source rollback.

Completion for the implementing model is: selected source changes applied; the four applicable check batches reported at their actual scope; one clearly identified freeze/child boundary for use of the new sources; and no invented claim of Word/PDF verification. The normal rendered package, if that subsequent semantic run is authorised and executed, supplies output evidence. Do not mark source-edit checks as proof of recruitment performance.

No rejected proposal is a follow-on TODO for the implementing model. No new schema, detector, field, preservation account, probe loop, global course removal, model switch or candidate-fact edit belongs to this execution.


## Proposal rehearsal record — 2026-09-12

Before delivery, this exact guide was applied to disposable copies with B skipped (25 steps) and with every conditional edit included (29 steps). All anchors matched once; the changed Python parsed; the settings and mode checks passed. The two existing T18 assertion-function bodies passed directly against the copied masters, and prepare_masters --check returned 0 with the expected 17/6 inventories. The D fill command produced all three temporary documents with identity retained and no residual controls. The hash refresh included changed paths and left skipped K untouched. No live framework source changed; this rehearsal is not owner acceptance of B, a full pytest run, semantic execution, Word-open verification or a pagination result.

M01 now has limited observability through existing review.notes, but its expected improvement in allocation is still the least-certain proposal. Verify an eligible omission against the actual pair before judging a missing note. A valid omission explanation is evidence that the note duty operated, not evidence that coverage improved. The 0–3 register dial's default 2 remains an unmeasured starting point.
