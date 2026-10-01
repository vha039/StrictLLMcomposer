# Build_x2 package review — 2026-09-30

Scope: all 14 x2 packages (13 harness jobs in runs `838ddd`, `57ef9e`, `984088`, plus the manual Etra run), compared with the stable `Build` runs (rund/runf/rung/0920) and the experimental Relay run (branch `sx_doctrine_v2`). Reviewer: Claude, single pass. Scores are editorial judgements on the Opus 5 §5.1 rubric (`Process/tests/output/runf-rung analysis and cross-run rankings - Opus 5.md`), not measured outcomes. Nothing is written to `evaluation/scorecard.csv`: that belongs to the blind protocol and is still empty.

## Bottom line

- **9 of 14 are sendable exactly as generated, 1 needs a one-word fix, 4 need a fix first.** No unsupported claim, ownership or lifecycle error of substance found (high-risk claims checked against each run's own frozen authorities; not every CV bullet re-verified line by line). Every CV is 2 pages, every letter 1; all 13 harness render reports are OK and every harness PDF matches its recorded SHA-256 (Etra has no render receipt).
- **Fix first:** **Eika** (letter subject says 'slash' instead of '/'), **Politi** (addressee block prints 'Politiets IT-enhet' twice; both come from the operator's batch input), **Trifid** (open ad: letter dated 23.09, and 'har i om lag tre år svart på kollegers spørsmål' attaches the ~3 years to answering, while the authority attaches them to the superuser title; same slip in the NAV-RO letter, one word to fix), **Etra** (the letter files are not the ≤1,500-character letter you instructed: ~2,550 vs ~1,200 characters in `final_package.json`; the CV already matches, so re-render the letter only).
- **Timing:** every package was generated on or before its søknadsfrist, except Politi (letter dated 24.09, frist 23.09). PDFs were renamed after render in seven packages (SHA still matches), which looks like submission prep, so I cannot tell which were already sent. Only Trifid and Etra ('snarest') are still open.
- **Filenames:** harness PDFs carry no candidate name; five renamed ones do not either (`CV_controller.pdf`, `CV_Data_Governance.pdf`, `CV_Helse_og_velferd.pdf`, `CV_Prosjektleder.pdf`, `CV_Enterprise_Architect.pdf`). Name them before sending.
- **x2 vs the other harnesses:** cleaner on every measured defect and a few points higher on my scoring, but the comparison is cross-vacancy, so it is directional, not proven.

## x2 packages, ordered by send priority (expected chance = odds x vacancy fit)

`Yes` = document sendable as generated (whether it was sent, and whether the ad is still open, is in the Frist column and the notes). Compound = rubric layers 1–2. IOI applies the knock-out cue with one rule for every arm I scored: x0.90 when a letter names a lack, or says it 'will learn', something the ad lists as a requirement; x0.85 when that sits in the opening or fills a paragraph; nothing for items the ad marks optional. Published arms keep Opus 5's cues. Fit is a separate column so clean package and worth-sending stay apart.

| # | Package | Frist | Sendable | CV | Letter | Pkg | Compound | IOI | Fit | Exp. | Note |
|--:|---|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | Bærum kommune – rådgiver virksomhetsstyring (vikariat) | 23.09 (closed) | **Yes** | 87.5 | 84.2 | 86.6 | 86.1 | 39.0 | 1.25 | 44.4 | Best fit of the set (experience is 'fordel, ikke krav'). No lack-sentence. Best letter. |
| 2 | NAV – forretningscontroller | 27.09 (closed) | **Yes** | 87.8 | 83.9 | 87.0 | 86.2 | 39.2 | 1.1 | 41.5 | Strong fit. Ad says no letter needed: CV + screening questions. The CV is the strong document. |
| 3 | Würth – digital integrasjonskoordinator | 25.09 (closed) | **Yes** | 87.2 | 84.2 | 86.6 | 86.0 | 38.9 | 1.0 | 38.9 | Junior-profile ad. EDI gap is optional in the ad, so the disclosure costs nothing. |
| 4 | Stendi – prosjektleder PMO (vikariat) | 27.09 (closed) | **Yes** | 85.9 | 83.7 | 85.2 | 84.9 | 37.0 | 0.8 | 31.9 | Clean, functional-PM framing, no overclaim. |
| 5 | Etra Gruppen – Group Business Controller (manual run) | Snarest (open) | **FIX FIRST** | 87.2 | 83.5 | 82.5 | 84.5 | 36.2 | 0.55 | 23.8 | Letter files (~2,550 chars) are not the ≤1,500-char letter you instructed and `final_package.json` holds (~1,200 chars, written ~70 s later). Re-render the letter only; the letter score here is for the on-disk version. 5-yr minimum not met. |
| 6 | Hydro – Data Governance Lead | 27.09 (closed) | **Yes** | 86.9 | 84.5 | 85.4 | 85.6 | 38.2 | 0.5 | 23.6 | English ad ('excellent English required'), Bokmål letter (harness rule). |
| 7 | Bufdir – spesialrådgjevar tilskot | 25.09 (closed) | **Yes** | 86.7 | 81.6 | 85.4 | 84.5 | 33.8 | 0.55 | 21.9 | States a lack on two 'du må ha' items (state grants, regelverk). Low odds. |
| 8 | Nittedal – rådgiver helse og velferd | 24.09 (closed) | **Yes** | 85.9 | 81.5 | 84.9 | 84.0 | 33.0 | 0.4 | 16.5 | Letter says 'ikke helsefag' against the first listed requirement. |
| 9 | NAV – seniorrådgiver ResearchOps | 23.09 (closed) | **Yes + 1 word** | 86.0 | 81.0 | 85.0 | 83.9 | 32.8 | 0.4 | 16.3 | Letter says 'har i om lag tre år svart' – the ~3 yrs belongs to the superuser title, not the answering. Core ResearchOps/qualitative requirement unmet; letter hands qualitative method and privacy to colleagues. |
| 10 | Nortura – fagleder masterdata | 27.09 (closed) | **Yes** | 86.8 | 83.4 | 86.2 | 85.4 | 35.4 | 0.35 | 16.1 | SAP requirement unmet and said so in the letter. Honest, low odds. |
| 11 | KPMG – prosjektleder CFO Advisory | 25.09 (closed) | **Yes** | 86.2 | 80.0 | 85.0 | 83.6 | 32.3 | 0.4 | 16.0 | 5–8 yrs consulting/PM unmet; letter says 'ikke fra konsulentbransjen'. |
| 12 | Trifid – senior KI-konsulent | Snarest (open) | **FIX FIRST** | 86.0 | 82.3 | 85.4 | 84.5 | 33.8 | 0.35 | 15.2 | Open ad. Letter is dated 23.09 and says 'har i om lag tre år svart' (duration belongs to the superuser title). 7-yr minimum and client KI-governance unmet; letter frames project-level honestly. |
| 13 | Politiets IT-enhet – senior bemanningsansvarlig | 23.09 (closed) | **FIX FIRST** | 84.9 | 78.0 | 84.2 | 82.2 | 32.3 | 0.3 | 12.5 | Addressee block prints 'Politiets IT-enhet' twice (batch unit = employer). Letter dated 24.09, a day after the frist. Ad: 'må oppfylle alle kravene' incl. staffing/recruiting in a large organisation, not met; CV must be re-keyed in Jobbnorge. |
| 14 | Eika – Lead Enterprise Architect | 27.09 (closed) | **FIX FIRST** | 85.6 | 80.6 | 84.4 | 83.5 | 32.1 | 0.25 | 10.6 | Subject line reads 'Lead Enterprise Architect slash Senior Virksomhetsarkitekt' (batch title typed with 'slash'; ad says '/'). Poorest fit; letter says 'ikke som virksomhetsarkitekt'. Dense (468 words). |

## Against the other harness versions

| Arm (n) | CV / Letter / Pkg | IOI | CV over 2 pages | Letter over 1 page | Headline wraps | 1st person in CV | Letters with explicit lack-sentence | Adoption sentences per letter | Scorer |
|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| Build `rund` (12) | 80.4 / 72.0 / 79.3 | 23.2 | 0 | 0 | 8/11 | 0/11 | 8/11 | 2.9 | Opus 5 (published) |
| Build `runf` (4) | 83.5 / 82.9 / 80.8 | 27.1 | **3/4** | 0 | 3/4 | 0/4 | 0/4 | 3.2 | Opus 5 (published) |
| Build `rung` (4) | 82.2 / 79.7 / 83.6 | 30.9 | 0 | 0 | 2/4 | 2/4 | 1/4 | 2.8 | Opus 5 (published) |
| Build `0920` latest (2) | 81.6 / 75.9 / 76.8 | 21.1 | 0 | **1/2** | 2/2 | 2/2 | 1/2 | 3.0 | this review |
| Experimental Relay branch (4) | 84.0 / 79.5 / 84.6 | 30.9 | 0 | 0 | 0/4 | 0/4 | 3/4 (all 'will learn') | 0.8 | this review |
| **Build_x2 (14)** | **86.5 / 82.3 / 85.3** | **35.3** | 0 | 0 | 0/14 | 0/14 | 7/14 (+1 optional-item) | 2.9 | this review |

Counts (pages, headline wraps, first person, lack-sentences, adoption sentences) are scripted over the rendered PDFs; scores are judgement. The published arms (rund/runf/rung) were scored by a different reviewer and include their knock-out cues. I re-scored `rung` EIE and Abacus as calibration: my sub-scores land within 0.5 of the published totals, but I had seen those totals, so this anchors my scale rather than validating it.

**What x2 fixes** (measured): headlines average 59 characters and never wrap (Build arms 73–80, wrapping in every Build arm); no first person in any CV (Build rung and 0920: half or more); no page overruns (runf 3/4 CVs on 3 pages; 0920 SpareBank1 letter on 2 pages); adoption and lifecycle facts stay in the letters (Relay dropped them to 0.8 per letter); the review lists concrete limitations for the operator (Relay's READY reviews are empty).

**What x2 costs:** seven letters state an explicit lack against a listed requirement (Nortura SAP, Bufdir state grants, Nittedal health education, KPMG consulting, Eika enterprise architecture, Trifid governance, NAV-RO qualitative method and privacy). The rubric treats that as a screening cue. x2 places it late and bridges it, so it gets the mild x0.90. Build `rung` and `runf` had almost none; `rund` had 8/11. Each sentence is a one-line deletion and no fact depends on it, so this is your call: honest disclosure against screening risk. Also, letters re-narrate the CV's budget-tool, STE-model and benefits-framework units in nearly every package (division of labour about 78–82).

**Confidence.** Cross-vacancy and one reviewer. x2 (35.3) vs Relay (30.9) and vs `rung` (30.9) is borderline (about 4 points, my noise is about ±3). x2 vs Build rund/runf/0920 (21–27) is outside it. None of the x2 vacancies exist in Build or experimental, and the six-vacancy paired gate in `evaluation/PROTOCOL.md` has not been run, so promotion evidence is still missing.

## Appendix — sub-scores (CV K,E,M,A,C,N | letter S,J,K,A,C,N | package G,R,M,X,Z)

| Package | CV | Letter | Package |
|---|---|---|---|
| Baerum | 88,88,90,86,88,82 | 86,80,86,82,88,84 | 88,80,88,90,88 |
| KPMG | 86,88,90,82,86,82 | 84,82,82,74,74,82 | 86,78,88,90,84 |
| NAV-RO | 86,86,90,84,86,82 | 86,82,84,76,74,80 | 86,78,88,90,84 |
| Nittedal | 84,88,90,82,88,82 | 86,82,84,80,72,82 | 84,80,88,90,84 |
| Politi | 84,86,90,78,88,82 | 78,76,78,76,82,80 | 82,78,88,90,86 |
| Trifid | 88,86,90,80,86,82 | 86,86,84,78,74,82 | 86,80,88,90,84 |
| Wurth | 88,88,90,84,88,82 | 88,82,86,82,82,84 | 88,80,88,90,88 |
| Bufdir | 86,88,90,84,88,82 | 86,84,84,78,72,82 | 86,80,88,90,84 |
| Eika | 84,88,90,80,88,82 | 86,82,82,76,74,80 | 84,78,88,90,84 |
| Hydro | 88,88,90,82,88,82 | 88,86,86,80,82,82 | 86,82,84,90,86 |
| NAV-FC | 88,88,90,88,88,82 | 84,84,82,82,88,84 | 88,82,88,90,88 |
| Nortura | 86,90,90,82,88,82 | 88,84,84,82,76,84 | 86,82,88,90,86 |
| Stendi | 84,88,90,82,88,82 | 84,84,84,80,88,82 | 84,80,88,90,86 |
| Etra | 86,88,90,88,88,82 | 84,82,82,82,88,84 | 86,80,80,78,88 |
| B0920 Tolletaten | 84,84,76,82,88,76 | 80,80,78,70,70,74 | 84,72,74,86,82 |
| B0920 SpareBank1 | 86,86,72,80,84,74 | 84,84,78,66,62,72 | 84,66,60,84,78 |
| Relay Stortinget | 82,78,90,84,88,84 | 84,84,78,84,68,74 | 82,84,90,86,84 |
| Relay Norwegian | 80,80,90,82,88,82 | 78,88,76,80,82,76 | 80,82,90,86,84 |
| Relay EIE | 82,80,90,84,88,84 | 86,80,80,84,76,78 | 84,82,90,86,84 |
| Relay Abacus | 84,80,90,84,88,84 | 82,84,80,70,60,78 | 82,82,90,86,82 |
| CAL rung EIE | 84,80,80,82,88,80 | 86,72,84,78,88,80 | 84,82,86,88,86 |
| CAL rung Abacus | 86,80,80,82,88,80 | 76,64,86,82,82,80 | 86,78,84,88,84 |
