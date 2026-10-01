# 03 — Issue registry, mitigation and fix logic

**Status:** planning material. Not authority.
**Scope:** every validated issue from the two-vacancy pilot, one atomic entry each, with the full
causal, scope, alternative, interaction and verification reasoning.

Change IDs (`A1`, `B2`, `C1`, `D3`, `E1`, `F1` …) are defined in
`02_IMPLEMENTATION_DESCRIPTIONS_INSTRUCTIONS_AND_DEFINITIONS.md`. Evidence citations resolve in
`04_PILOT_FORENSIC_AUDIT.md`.

---

## 0. Registry summary

| ID | Title | Severity | Recurrence | Scope | Fix |
|---|---|---|---|---|---|
| ISS-01 | CV main prose below the readability floor (9 pt) | HIGH | CERTAIN | systemic | A1, A2 |
| ISS-02 | Letter body at 10.5 pt, a half-point size | HIGH | CERTAIN | systemic | A2 |
| ISS-03 | Half-point and inconsistent sizes across the CV | MEDIUM | CERTAIN | systemic | A1 |
| ISS-04 | Subordinate CV zones carry title-line run properties | MEDIUM | CERTAIN | systemic | A1 |
| ISS-05 | Ceremonial mission motivation promoted and then scored as passing the employer-swap test | HIGH | HIGH | systemic | B1, B2, B3 |
| ISS-06 | Truth attenuation: authority provenance frame written into first-person prose | HIGH | HIGH | systemic | C1, C2 |
| ISS-07 | Em dash used as a clause divider by the renderer | MEDIUM | CERTAIN | systemic | D1 |
| ISS-08 | En dashes in employer-facing baseline and master content | MEDIUM | CERTAIN | systemic | D3, D4 |
| ISS-09 | Consultant-form employer-restatement openings introduced by Stage 3 | MEDIUM | HIGH | systemic | E1, E2 |
| ISS-10 | Letter macro-skeleton prescribed by `structure_guidance` in both jobs | LOW | HIGH | systemic | B3 |
| ISS-11 | Stock closing formula and generic contribution sentence | MEDIUM | CERTAIN | systemic | E1 |
| ISS-12 | Ordinary hyphen used as a clause divider in generated prose | LOW | MODERATE | local | D5 |
| ISS-13 | Employer-facing outputs unreadable — staging-directory ACL carried by same-volume move | HIGH | CERTAIN | systemic | F1 |
| ISS-14 | Two tests coupled to production role mapping | MEDIUM | CERTAIN | local | F2 |
| ISS-15 | Pilot log never captured; no human-effort evidence exists | MEDIUM | HIGH | systemic | verification obligation + RUNBOOK line |
| ISS-16 | CV page 2 underutilized | — | — | **merged into ISS-01** | none of its own |

Severity is employer-facing impact. Recurrence is the likelihood the same defect appears in the next
cluster if nothing changes. `CERTAIN` means deterministic — it will recur on every render.

---

## ISS-01 — CV main prose is below the readability floor

| Field | Value |
|---|---|
| **Affected** | both jobs; `templates/CV_MASTER.docx`; every rendered CV page; render stage |
| **Observed evidence** | `word/document.xml` inline runs: `CV_PROFILE` 9.0 pt, `CV_CORE_COMPETENCE` 9.0, `CV_CURRENT_ROLE_TOP_EVIDENCE` 9.0 (`ListBullet`), `CV_EARLY_ROLE_EVIDENCE` 9.0, `CV_FUNCTIONAL_IDENTITY` 10.0. `styles.xml Normal` is also 9.0. |
| **Expected** | main employer-facing body text defaults to 12 pt (mandatory outcome A) |
| **Actual** | 9 pt for all substantive CV prose |
| **Employer-facing consequence** | the entire decision-relevant surface of the CV — profile, competencies, both bullet zones — is rendered at a size that is uncomfortable at normal reading distance and on screen. Directly degrades `Tjuesekunderstesten`, whose whole premise is a fast visual scan. |
| **First stage introduced** | none — it is a static property of the master, inherited from P0.7 and preserved through `prepare_masters` |
| **Stages that could have repaired it** | none. No semantic stage can set type size; the template map exposes no typography surface. This is correct design and must stay that way. |
| **Root cause** | the master was sized to force a one-page CV. `prepare_masters` removed the forced page break under GATE-05 but left the compensating type sizes in place. |
| **Contributing factors** | no readability floor existed in writing doctrine or template policy; the page target (`cv_expected_max_pages = 2`) has never produced a warning because the pilot's PDF conversion failed (F12), so nothing surfaced the trade-off. |
| **Root-cause confidence** | HIGH — read directly from OOXML |
| **Severity** | HIGH |
| **Recurrence** | CERTAIN (deterministic) |
| **Systemic/local** | systemic |
| **Scope boundary** | the inline `w:sz` of runs inside the CV's dynamic controls and the `styles.xml` fallbacks they depend on. **Not** the template map, not the control contract, not the merge semantics, not the render transaction, not page geometry, not spacing (see A5). |
| **Non-target surfaces** | `template_map.json`; the 17/7 control contract; `merge.py`; `docxfill` fill primitives; margins and `pgSz`; running header/footer at 8 pt; `cv_expected_max_pages`. |
| **Proposed fix** | **A1** (declarative typography table in `prepare_masters`) + **A2** (`styles.xml Normal`, `ListBullet`, `Heading1–3`). Main prose → 12 pt; headings and functional identity → 14 pt so the existing hierarchy is preserved rather than flattened; subordinate content → 10 pt. |
| **Why this fix surface** | `docxfill._set_paragraph_text` deep-copies the template run **including `w:rPr`**, so generated paragraphs inherit the master's inline size. `styles.xml` alone would change nothing in the CV. The master is the only place the size can live, and `prepare_masters` is the only reproducible way to change a master in a repository with no version control. |
| **Alternatives, and why they lose** | *(a) Edit `styles.xml` only* — provably ineffective for the CV. *(b) Hand-edit the DOCX* — unreproducible with no `.git`; the transform could never be audited or re-derived, which is precisely why `prepare_masters` exists. *(c) Expose typography in `template_map.json` and set it at render time* — puts presentation logic in the render path, widens the frozen template map, and gives no benefit over setting it once in the master. *(d) A per-document auto-fit* — explicitly prohibited by outcome A and by `DEC-24`. |
| **Interactions** | With **ISS-16** — resolves it entirely; page 2 becomes populated rather than sparse. With **ISS-03/ISS-04** — same table, one edit. With **ISS-08** — the master must be rewritten anyway, so the dash normalisation costs nothing extra, but the two must land together with `D3` or preflight fails. With **A3** — the doctrine must say the page target is met by compression, or a future writer will treat overflow as licence to shrink. |
| **Architecture impact** | none. Spec §22.2 grants the builder *"template layout changes proven by target-machine gates"*. `DEC-24` already treats typography as an editorial signal. No amendment. |
| **Cost/risk** | ~120 lines in `prepare_masters`, keyed by SDT tag and text anchor. Risk: the P0.7 masters were invalid OOXML repaired by this same tool, so any edit must keep `prepare_masters --check` green, preserve 17 CV / 7 letter controls, preserve GATE-06 parseability, and be **opened in Word**, not merely parsed. |
| **Verification** | one writing `prepare_masters` run followed by one `--check` dry run reporting zero pending typography/dash transforms (idempotence); `preflight` PASS; vertical slice PASS; new size-set test; hash-equal B0 snapshot versus Run A1 visual comparison; **human visual review**. |
| **Acceptance** | The two pilot CVs normally render to 2 balanced pages; body text is legible, hierarchy name > headings > body > detail remains intact, and no block is clipped/orphaned. A 3-page result triggers semantic compression and then canonical spacing/flow review, **never** type reduction or deletion of decision-relevant evidence; an extra usable page is accepted when the alternative is worse (`DEC-24`). |

---

## ISS-02 — Letter body at 10.5 pt, a half-point size

| Field | Value |
|---|---|
| **Affected** | both jobs; `templates/APPLICATION_MASTER.docx`; every rendered letter |
| **Observed evidence** | `styles.xml` `Normal` = 21 half-points = **10.5 pt**. The `APPLICATION_BODY` control's template paragraph carries **no inline `w:sz`**, so the entire letter body inherits it. |
| **Expected** | 12 pt body; no half-point sizes |
| **Actual** | 10.5 pt |
| **Employer-facing consequence** | the letter — the document that carries the whole employer-decision argument — is set below the readability floor at a size that also signals fit-tuning rather than design. |
| **First stage introduced** | none; static master property |
| **Stages that could have repaired it** | none |
| **Root cause** | as ISS-01: inherited P0.7 sizing chosen to force one page |
| **Contributing factors** | the letter master differs structurally from the CV master (style-driven rather than inline), so a fix aimed at one would miss the other |
| **Root-cause confidence** | HIGH |
| **Severity** | HIGH |
| **Recurrence** | CERTAIN |
| **Systemic/local** | systemic |
| **Scope boundary** | `styles.xml Normal` in `APPLICATION_MASTER.docx`, plus the five address-block runs at 8.5 pt. **Not** `Title` (20 pt, even, in scale — unchanged), not the letter's margins, not `letter_expected_max_pages`. |
| **Non-target surfaces** | `Title` style; `APPLICATION_BODY` control structure; the `|`-free letter layout; `template_map.json`. |
| **Proposed fix** | **A2** — `Normal` → 24 half-points. **A1** — the five metadata runs 8.5 → 10, matching the CV's subordinate tier. |
| **Why this fix surface** | for this master the body genuinely is style-driven; setting `Normal` is the minimal correct edit and automatically carries the signature line, which also has no inline size. |
| **Alternatives** | *(a) Add an inline `w:sz` to the `APPLICATION_BODY` template paragraph* — works, but adds an override where none exists and leaves `Normal` wrong for every other paragraph. *(b) Leave 10.5* — fails the mandatory outcome. |
| **Interactions** | With **ISS-05** — removing the ceremonial motivation paragraph frees roughly a paragraph of vertical space, which offsets part of the 14 % growth from 10.5 → 12. With **ISS-08** — the `Søknad – ` subject line is in the same master and is fixed in the same pass. |
| **Architecture impact** | none; §22.2 |
| **Cost/risk** | two `w:sz` values in `styles.xml` plus five inline runs. Low risk; the letter has 8 body paragraphs and no page break. |
| **Verification** | modelled at ≈0.70 page before the ISS-05 saving, so one page is not in doubt; confirmed by Run A1 PDF page count = 1 and by the visual review. |
| **Acceptance** | each pilot letter renders to 1 page at 12 pt with the address block clearly subordinate. This is a content-specific expectation, not a hard framework limit. |

---

## ISS-03 — Half-point and inconsistent sizes across the CV

| Field | Value |
|---|---|
| **Affected** | both jobs; `CV_MASTER.docx`; every rendered CV |
| **Observed evidence** | distinct inline sizes `{8.5, 9.0, 9.5, 10.0, 24.5}`. `CV_RELEVANT_MASTER_SUBJECTS` is 8.5 while `CV_RELEVANT_BACHELOR_SUBJECTS` — the same class of content — is 9.5. The candidate's name is 24.5. |
| **Expected** | a discrete human-readable scale: 8, 9, 10, 11, 12, then even sizes above 12; no half-point micro-tuning |
| **Actual** | three half-point sizes, two of which apply to equivalent content at different values |
| **Employer-facing consequence** | visible inconsistency between two adjacent education lines; the whole document reads as fit-tuned rather than designed. Low individually, cumulative with ISS-01/ISS-04. |
| **First stage introduced** | none; static master property |
| **Stages that could have repaired it** | none |
| **Root cause** | successive manual fit adjustments in the P0.7 lineage, never rationalised |
| **Contributing factors** | earlier inventories read `styles.xml` only, where 8.5 and 9.5 do not appear at all, so the inconsistency was invisible to every prior report |
| **Root-cause confidence** | HIGH |
| **Severity** | MEDIUM |
| **Recurrence** | CERTAIN |
| **Systemic/local** | systemic |
| **Scope boundary** | inline `w:sz` values only. Bold, caps and colour change **only** where ISS-04 applies. |
| **Non-target surfaces** | running header/footer at 8 pt — deliberately subordinate furniture, in scale, and unchanged. |
| **Proposed fix** | **A1** — collapse to `{8, 10, 12, 14, 24}` via the five-tier table. |
| **Why this fix surface** | same edit as ISS-01; separating them would mean touching the master twice. |
| **Alternatives** | *(a) Round each value to the nearest whole point* — preserves the arbitrary structure and would keep master-subjects at 8/9 and bachelor-subjects at 10, i.e. still inconsistent. The tier table fixes the classification, not just the arithmetic. |
| **Interactions** | ISS-01, ISS-04 — one table. |
| **Architecture impact** | none |
| **Cost/risk** | included in A1 |
| **Verification** | test asserting the closed size set; `prepare_masters --check` idempotence |
| **Acceptance** | exactly five sizes present in both masters, all in the user's scale, no half-points. |

---

## ISS-04 — Subordinate CV zones carry title-line run properties

*New finding. Not present in any prior report or in `NON_AUTHORITATIVE_CONSIDERATIONS.md`.*

| Field | Value |
|---|---|
| **Affected** | both jobs; `CV_MASTER.docx` paragraphs 23 and 31; the TIDLIGERE ERFARING block and the bachelor-subject line on every rendered CV |
| **Observed evidence** | `CV_RELEVANT_BACHELOR_SUBJECTS` and `CV_PREVIOUS_EXPERIENCE_CONTENT` both render **9.5 pt, `w:b`, colour `17324D`** — identical run properties to the education and employment *title* lines. The equivalent `CV_RELEVANT_MASTER_SUBJECTS` zone is 8.5 pt, non-bold, body colour. |
| **Expected** | subordinate content is visually subordinate; equivalent content classes are formatted alike |
| **Actual** | the four previous-employment lines and one education-detail line render in bold navy, styled as record titles |
| **Employer-facing consequence** | the least decision-relevant content on the page — student and military jobs from 2013–2021 — is given title-level visual weight and competes with the teal section headings for the recruiter's eye. This works directly against `Tjuesekunderstesten`, whose requirement is that the three strongest signals are visible before secondary breadth. |
| **First stage introduced** | none; static master property inherited from P0.7 |
| **Stages that could have repaired it** | none |
| **Root cause** | an SDT was placed on a paragraph whose run properties belonged to the preceding label; the copied run then became the template run for all generated content in that zone via `_set_paragraph_text` |
| **Contributing factors** | `prepare_masters` reorders `w:rPr` children for schema validity but does not inspect their semantics; no test looks at run properties; the pilot's renders were never opened by a reviewer because of ISS-13 |
| **Root-cause confidence** | HIGH |
| **Severity** | MEDIUM |
| **Recurrence** | CERTAIN |
| **Systemic/local** | systemic |
| **Scope boundary** | `w:b` and `w:color` on the runs of the two named zones, plus their size. **Not** the employment or education *title* lines, which are correctly bold navy and stay so. |
| **Non-target surfaces** | all `Heading1` runs; the name; the employment/education title lines; the master-subjects zone beyond its size change. |
| **Proposed fix** | **A1** — the T4 subordinate tier sets size 10, removes `w:b`, and sets body/grey colour for both zones. |
| **Why this fix surface** | the defect is in the master's run properties; nothing downstream can see or change them. |
| **Alternatives** | *(a) Leave it and rely on size alone* — bold navy at 10 pt would still read as a title against 12 pt plain body; the weight is the dominant signal. *(b) Move the SDT to a different paragraph* — restructures the master and risks the control contract for no additional gain. |
| **Interactions** | ISS-01/ISS-03 — same table. Also interacts with **ISS-07**: the same TIDLIGERE ERFARING block carries the four em dashes, so both defects are on the same four lines and are verified by the same visual check. |
| **Architecture impact** | none; §22.2 |
| **Cost/risk** | three extra columns in the A1 table |
| **Verification** | test asserting the two zones are non-bold and not navy; visual A/B |
| **Acceptance** | TIDLIGERE ERFARING and both education-detail zones read as clearly subordinate to their section headings in the rendered PDF. |

---

## ISS-05 — Ceremonial mission motivation, promoted by Stage 3 and then scored as passing the employer-swap test

| Field | Value |
|---|---|
| **Affected** | `huseierne_strategi_maalstyring`; `strategy.json`, `draft_package.json`, `final_package.json`, `review.json`; letter body paragraph 4 |
| **Observed evidence** | Stage 1 `motivation_bridge`: *"…i en medlemsorganisasjon der bedre prioriteringer kan gjøre det tryggere og enklere å være boligeier."* → Stage 2 closing, restrained → Stage 3 `body_paragraphs[3]`: *"Det som særlig motiverer meg, er at bedre virksomhetsstyring hos Huseierne skal understøtte et tydelig medlemsoppdrag: å gjøre det tryggere og enklere å være boligeier."* → Stage 3 `review.reasons[1]`: *"Pakken består Arbeidsgiverbyttetesten: … og **medlemsoppdraget** gjør både CV-profilen og søknaden spesifikke for Huseierne."* |
| **Expected** | motivation grounded in the actual work, problem, responsibility, environment, learning or leverage; mission invoked only when genuinely consequential and credibly motivating for this candidate |
| **Actual** | the employer's own public slogan, connected to no feature of the work and to no documented candidate motive, promoted to the letter's motivational climax and then counted as evidence of employer specificity |
| **Employer-facing consequence** | the paragraph a recruiter reads as the candidate's reason for applying is borrowed employer branding. It is the most performative sentence in either package and is exactly the kind of copy a reader discounts. |
| **First stage introduced** | **Stage 1**, as a trailing subordinate clause in `motivation_bridge` |
| **Stages that could have repaired it** | Stage 2 (carried it, restrained) and **Stage 3** (had full reconstructive authority, the doctrine in scope, and instead amplified it and scored it positively) |
| **Root cause** | multivariate. **(a) Routing:** Stage 1's instruction directs it to the doctrine *"only at"* `Single Backbone` and `WRONG_ROUTE`, so `Begrunnet motivasjon` — the section that governs `motivation_bridge` — was formally out of scope for the field that produced the defect. **(b) Salience/competing instruction:** Stage 3's instruction names `Tjuesekunderstesten` and `Arbeidsgiverbyttetesten` by name and tells Stage 3 to *repair* what they expose; it does not name `Begrunnet motivasjon`. Mission language is maximally employer-specific, so it satisfies the named test on its face while violating the unnamed rule. **(c) Ordering:** `structure_guidance` told the writer to end with motivation, which turns a trailing clause into a paragraph that needs filling. |
| **Contributing factors** | a generic application-writing prior that expects a mission paragraph; the relevant existing section had less stage salience than the two named final-review tests |
| **Root-cause confidence** | HIGH for (a) and (b) — both read directly from the instructions and the review; HIGH for (c) — read from `structure_guidance` in both jobs |
| **Severity** | HIGH |
| **Recurrence** | HIGH — the routing and salience conditions are unchanged for every future job |
| **Systemic/local** | systemic |
| **Scope boundary** | the *evidential status* of mission and values language, and the routing of `Begrunnet motivasjon` to Stage 1 and Stage 3. **Not** a ban on mission or societal language. |
| **Non-target surfaces** | **Avinor's societal-purpose paragraph, which is legitimate and must survive** — it names the operating environment, which is a causal feature of the work and the basis of the candidate's transfer argument (`04 §3.1a`). Also: `Arbeidsgiverbyttetesten` itself as a test; employer specificity as a goal; the `motivation_bridge` field; the strategy schema. |
| **Proposed fix** | **B1** — Stage 1's field→section map binds `motivation_bridge` to the existing `WRITING_DOCTRINE § Begrunnet motivasjon`. **B2** — Stage 3 must apply that named section before triage, and text it rejects cannot be reused as proof that `Arbeidsgiverbyttetesten` passes. **B3** — `structure_guidance` must describe the argument this vacancy needs, not prescribe a default motivation-shaped closing. No doctrine text is added for B. |
| **Why this fix surface** | coverage exists and is calibrated; the failure was routing, salience and ordering. Pointing the two responsible stages to the canonical Norwegian section is the smallest change that reaches the behaviour. Another hierarchy, checklist or voice-level motivation rule would create a second source of truth. |
| **Alternatives, and why they lose** | *(a) Ban mission/societal language categorically* — **rejected on evidence**: it would destroy the correct Avinor paragraph to fix the incorrect Huseierne one. *(b) Strengthen or restate `Begrunnet motivasjon`* — current text already requires concrete work-grounding and forbids copied values and unsupported employer praise; more policy would not fix the missing pointer. *(c) A Stage-3 motivation rubric in English* — another source of truth. *(d) Remove `motivation_bridge`* — it is a required strategy surface and its routing, not its existence, failed. *(e) Fix only Stage 3* — leaves the origin untouched. |
| **Interactions** | With **ISS-10** — B3 removes the ordering pressure that creates a motivation-shaped hole to fill. With **ISS-11/E1** — voice handles generic authorial form, but motivation remains exclusively governed by the canonical doctrine. With **ISS-02** — removing ceremonial copy may reclaim vertical space that partly offsets the 12 pt lift. |
| **Architecture impact** | none. Spec §4.5 already classes writing guidance as advisory; `DEC-31` forbids fit scoring and is untouched; the strategy schema is unchanged. No amendment. |
| **Cost/risk** | one Stage-1 table row, one anti-template sentence and one Stage-3 named-section/salience clause. Risk: over-correction producing motivation-free letters; mitigated by the existing positive work-grounding language and the Avinor regression guard. |
| **Verification** | Run B semantic review: every motivation sentence traceable to work, decision problem, operating environment or a documented candidate motive; where mission language appears, it names a causal feature of the work. **Avinor's paragraph surviving is a positive acceptance signal, not a failure.** |
| **Acceptance** | the Huseierne letter no longer contains a slogan-derived motivation sentence; the Avinor letter retains its operating-environment framing; neither review cites mission language as evidence for `Arbeidsgiverbyttetesten`. |

---

## ISS-06 — Truth attenuation: an authority provenance frame written into first-person prose

| Field | Value |
|---|---|
| **Affected** | **both jobs**; `strategy.json`, `draft_package.json`, `final_package.json`; CV bullet and letter body in each — **4 occurrences in shipped employer-facing text** |
| **Observed evidence** | Authority `Work_experience.md § 4.4`: *"Vegard **reports** it remained active approximately 2.5 years later"*; `STATUS_OUTCOME`: *"reported active approximately 2.5 years later"*. Stage 1 `evidence_plan[].role`: `var rapportert aktivt omtrent 2,5 år senere`. Stage 2: `var **fortsatt** rapportert aktivt om lag 2,5 år senere`. Stage 3: `var rapportert i bruk om lag 2,5 år senere`. |
| **Expected** | once a proposition clears the truth bar, state it with the maximum defensible persuasive force; do not add uncertainty or distancing absent from the evidence; preserve genuine qualification |
| **Actual** | the source file's third-person provenance marker was carried verbatim into the candidate's own first-person prose, and Stage 3 additionally removed the `fortsatt` that Stage 2 had added |
| **Employer-facing consequence** | the candidate's single strongest durability claim — a team-built framework adopted hospital-wide and still in use ~2.5 years later — reads as second-hand and unvouched. A recruiter discounts a reported claim relative to an asserted one. This is a material loss of interview value on the lead evidence of one job and the second evidence of the other. |
| **First stage introduced** | **Stage 1**, in `evidence_plan[].role` — the field whose function is to frame the proposition for both downstream writers |
| **Stages that could have repaired it** | Stage 2 (moved toward the correct reading by adding `fortsatt`, but kept the frame) and **Stage 3**, which touched the sentence, changed `aktivt` to `i bruk`, and removed `fortsatt` — a deliberate re-word that net-weakened the claim |
| **Root cause** | the candidate authorities are written *about* the candidate by a documentation process; the application is written *by* the candidate. "Vegard reports X" asserts X on the candidate's own knowledge. Transposed into first person, the reporting frame becomes attribution distance that the evidence does not contain. Existing `Rolig faglig tyngde`/`TOO_WEAK` covers under-selling generally but does not state this non-obvious speaker change, and neither responsible stage is pointed to those sections. |
| **Contributing factors** | a claim-ceiling culture correctly tuned against overclaiming, with no symmetric duty against understatement; Stage 3's repair duty is worded one-directionally (*"unsupported or inflated"*); `upstream_claim_repaired` is `null` in both reviews, consistent with a stage that was looking only for inflation |
| **Root-cause confidence** | HIGH — the full chain is reproducible across six artifacts and the authority wording is explicit |
| **Severity** | HIGH |
| **Recurrence** | HIGH — the authorities contain other provenance-marked statements, and nothing currently prevents the same transposition |
| **Systemic/local** | systemic |
| **Scope boundary** | attribution voice only: the distinction between a marker of *where the fact was recorded* and a qualification of *what the fact supports*. **Not** the claim ceilings, not the lifecycle vocabulary, not the result classes, not the authorities themselves. |
| **Non-target surfaces** | `Work_experience.md` and the other two authorities — **the authority wording is correct and must not be edited**; the `evidence_plan` schema; `used_evidence_refs` semantics; the `TOO_STRONG`, `LIFECYCLE_MISREPRESENTATION` and `HARD_FACTUAL_BOUNDARIES` sections; the approximation `om lag` and the horizon `2,5 år senere`, both of which must survive. |
| **Proposed fix** | **C1** — append one concise bullet to `PERSUASION_CALIBRATION § TOO_WEAK`: do not carry third-person source provenance into the candidate's own voice; remove only that speaker-distance while preserving approximation, observation horizon, lifecycle and measurement limits. **C2** — route Stage 1's `evidence_plan[].role`/`claim_ceiling` to `Rolig faglig tyngde` and `TOO_WEAK`, and make Stage 3's repair duty symmetric for known material understatement. |
| **Why this fix surface** | the narrow provenance-transposition case is genuinely uncovered, while the general leverage behavior already exists. `TOO_WEAK` is the canonical home and needs one clarification, not a new leverage rubric. Fixing the origin and the last line of defence prevents both downstream writers from inheriting the attenuation. |
| **Alternatives, and why they lose** | *(a) A lexical rule naming `rapportert` and `oppgitt`* — **rejected**: invites substitution rather than judgement, would strip the word where the qualification is real, and generalises to nothing. The rule must be about who is speaking. *(b) Edit the authority to remove "reports"* — **rejected and dangerous**: the provenance marker is *true and useful inside the authority*; it records that the claim rests on self-report rather than measurement, which is exactly the kind of distinction the evidence architecture exists to preserve. *(c) Stage-3-only repair duty* — leaves the origin. *(d) A deterministic hedge detector* — a semantic judgement no validator can make; `INV-07` and Spec §10.3 forbid failing a package on a string. |
| **Interactions** | With **B1/B3** — all new Stage-1 pointers land in the same field→section map, so the "only at" scoping is restructured once. With **E1** — the voice file has no qualification or claim authority; C1 remains the sole provenance clarification. With **ISS-05** — both are Stage-3 failures to repair and both are handled before triage. |
| **Architecture impact** | none. `INV-03` and the claim-ceiling model are untouched — the fix strengthens confidence *inside* the evidence boundary and does not move the boundary. No schema change. No amendment. |
| **Cost/risk** | one four-line Norwegian bullet plus two short stage pointers. The serious risk is stripping a real qualification; the bullet names exactly which limits survive and Run B checks both attenuation and inflation. |
| **Verification** | Run B: the framework claim reads `fortsatt i bruk` or an equally strong evidence-defensible form, with `om lag` and the `2,5 år senere` horizon preserved and no documentation frame. Checked in both directions: no claim exceeds its authority ceiling and `review.known_limitations` remains accurate. |
| **Acceptance** | the durability claim is stated on the candidate's own authority with its genuine qualifications intact, in both jobs, in both CV and letter; and no new claim anywhere in either package exceeds what the authorities support. |

---

## ISS-07 — Em dash used as a clause divider by the renderer

| Field | Value |
|---|---|
| **Affected** | both jobs; `runtime/jobbsok/render.py:179`; the TIDLIGERE ERFARING block on every rendered CV — **4 em dashes per CV** |
| **Observed evidence** | `lines.append(f"{line} — {summary}" if summary else line)`. Confirmed in the readable vertical-slice CV: `EM=4`, e.g. *"03.2014-02.2015 | Vakt- og sikringssoldat, Luftforsvaret, Sola — Utførte…"* |
| **Expected** | no em dash in employer-facing text; no dash used merely to divide clauses where ordinary punctuation will do |
| **Actual** | deterministic code injects an em dash as a clause divider on every previous-employment line |
| **Employer-facing consequence** | the only em dashes anywhere in the package, on four consecutive lines, in the exact position outcome D targets. Also a recognisable polished-LLM typographic signature. |
| **First stage introduced** | none — deterministic render code |
| **Stages that could have repaired it** | none; no semantic stage sees or controls this string |
| **Root cause** | a formatting choice in `resolve_control` for `effective.previous_employments`, predating the punctuation rule |
| **Contributing factors** | nothing verifies the produced document's punctuation; the pilot's renders were never opened because of ISS-13 |
| **Root-cause confidence** | HIGH |
| **Severity** | MEDIUM |
| **Recurrence** | CERTAIN |
| **Systemic/local** | systemic |
| **Scope boundary** | one f-string. **Not** the `|` separator on the same line, which is a legitimate structural divider and is explicitly permitted; not the `·` competency separator; not the `•` bullet separator. |
| **Non-target surfaces** | `resolve_control`'s other branches; `join_middot`; the template map. |
| **Proposed fix** | **D1** — replace the em dash with a period and space, matching how the line already uses `|` for structure. |
| **Why this fix surface** | the string is emitted by deterministic code; there is nowhere else it can be fixed. |
| **Alternatives** | *(a) Replace with a hyphen* — reintroduces exactly the clause-dividing hyphen outcome D prohibits. *(b) Replace with a colon* — acceptable, but a period reads better after a `|`-separated identity line. *(c) Restructure the whole line* — wider than needed. |
| **Interactions** | With **ISS-04** — the same four lines carry both defects, so both are confirmed by one visual check. |
| **Architecture impact** | none; implementation-only correction |
| **Cost/risk** | one line; negligible |
| **Verification** | new test asserting the previous-employment line contains no em dash; extracted employer-facing text contains zero en/em dashes |
| **Acceptance** | zero em dashes in both produced documents. |

---

## ISS-08 — En dashes in employer-facing baseline and master content

| Field | Value |
|---|---|
| **Affected** | both jobs; `authorities/CV_BASELINE.md`, `generated/baseline_map.json`, both masters' static furniture; every rendered CV (**15**) and letter (**1**) |
| **Observed evidence** | `CV_BASELINE.md` contains 20 en dashes at known lines: 11 rendered date ranges (`period`, `employment_group_period`, education `period`), 2 unit names (`Direktørens stab – Analyseavdelingen`, `Barne- og ungdomsklinikken – Stab`), 3 trust-section ranges, and 4 inert `authority_anchor` values. `APPLICATION_MASTER` static text: `Søknad – {{APP_JOB_TITLE}}`. `CV_MASTER` static furniture mirrors the baseline periods and unit names. |
| **Expected** | no en dash in employer-facing text; ordinary hyphen for compounds, dates and ranges |
| **Actual** | 16 en dashes reach the page |
| **Employer-facing consequence** | typographically correct Norwegian, but in direct breach of a mandatory outcome and part of the same polished-machine signature the pass is removing. |
| **First stage introduced** | none — human-maintained baseline and static master content |
| **Stages that could have repaired it** | none; the baseline owns chronology and no stage may alter it (`DEC-23`) |
| **Root cause** | conventional typography choices in the P0.7-derived assets, predating the rule |
| **Contributing factors** | the master duplicates baseline values as static furniture, so the two must be kept in agreement |
| **Root-cause confidence** | HIGH |
| **Severity** | MEDIUM |
| **Recurrence** | CERTAIN |
| **Systemic/local** | systemic |
| **Scope boundary** | the 16 rendered en dashes. **The 4 `authority_anchor` values are explicitly out of scope** — `baseline.py` and the schema record them as *"Inert human-readable note … NOT resolvable as a factual evidence reference"*, they never render, and two of them are verbatim cross-references to strings in `Work_experience.md`. Changing them would break a human cross-reference for no employer-facing gain. |
| **Non-target surfaces** | `authority_anchor`; the authorities themselves; the `|` separators in the master; the `baseline_map` schema; chronology, order and formal titles. |
| **Proposed fix** | **D3** — 14 date ranges → `-`; the 2 unit names → **comma** (`Direktørens stab, Analyseavdelingen`), because a hyphen there would itself be a clause divider. Then `jobbsok index build` and `jobbsok index verify`. **D4** — the same normalisation in both masters' static furniture, in the same change, plus `Søknad – ` → `Søknad: ` and the `leakage.KNOWN_GOOD_PHRASES` unit string. |
| **Why this fix surface** | the strings live in a human-maintained protected input and in the masters. `AGENTS.md` explicitly permits human-invoked source maintenance of protected inputs between runs, and `prepare_masters` is the auditable route for master content. |
| **Alternatives** | *(a) Normalise at render time* — puts a text transform in the render path, hides the source of truth, and would break `static_baseline_assertions` unless it also ran there. *(b) Leave date ranges as en dashes* — outcome D prohibits the character in employer-facing text without a date exemption, and explicitly lists dates and ranges among the hyphen's legitimate uses. *(c) Hyphen for the unit names* — creates a clause-dividing hyphen, which the same outcome prohibits. |
| **Interactions** | **Hard ordering dependency:** `preflight_templates` compares master static text against `baseline_map` values via `static_baseline_assertions`, so D3 and D4 **must land together** or preflight fails. Both ride on the same `prepare_masters` invocation as **ISS-01/03/04**, so the master is rewritten once. |
| **Architecture impact** | none. `DEC-23` baseline ownership is preserved — the human edits the baseline, no stage does. No schema change: verified that no JSON-schema `pattern` and no runtime regex depends on the en dash; the only two code references are `leakage.py:98` and `render.py:832`. |
| **Cost/risk** | 16 string edits in one JSON block plus the mirrored master text. Risk: forgetting one side breaks preflight — which is also the detection mechanism. |
| **Verification** | `jobbsok index verify` PASS (byte-identical regeneration); `jobbsok preflight` PASS; extracted DOCX/PDF text contains zero `–` and zero `—`. |
| **Acceptance** | zero en dashes and zero em dashes in the extracted text of all four produced documents. |

---

## ISS-09 — Consultant-form employer-restatement openings, introduced by Stage 3

| Field | Value |
|---|---|
| **Affected** | both jobs; `final_package.letter.opening` |
| **Observed evidence** | Stage 2 wrote *"Jeg søker stillingen som … fordi …"* in both jobs. Stage 3 replaced both: *"Huseierne skal omsette medlemsvekst, nye produkter og større organisatorisk kompleksitet til tydelige prioriteringer og resultater."* and *"Når Avinor skal bruke teknologi, data og nye arbeidsformer …, må digitale initiativer skape verdi uten at driftskontinuitet og sikkerhet blir en ettertanke."* |
| **Expected** | an opening that creates a candidate bridge, not one that demonstrates vacancy comprehension |
| **Actual** | both openings restate the employer's own situation to the employer before the candidate appears; the Avinor form is the recognisable `Når <employer> skal <X>, må <Y> uten <Z>` consultant pattern |
| **Employer-facing consequence** | the first sentence — the highest-value real estate in the letter — spends itself telling the reader something they already know. Moderate: the openings are competent and employer-specific, just not candidate-advancing. |
| **First stage introduced** | **Stage 3** — this is a reconstruction, not an inherited defect |
| **Stages that could have repaired it** | Stage 3 itself; there is no later stage |
| **Root cause** | a polished-application prior activating at the point of final reconstruction, reinforced by `structure_guidance` telling the writer to open with the employer problem |
| **Contributing factors** | `Arbeidsgiverbyttetesten` rewards employer specificity, and an employer-situation restatement is maximally employer-specific — the same mechanism as ISS-05 |
| **Root-cause confidence** | MODERATE — the pattern is reproduced in both jobs, but the model's internal reason is inferred |
| **Severity** | MEDIUM |
| **Recurrence** | HIGH |
| **Systemic/local** | systemic |
| **Scope boundary** | opening rhetoric only. **Employer-problem openings are not banned** — the fix distinguishes an opening that creates a useful candidate bridge from one that merely demonstrates comprehension. |
| **Non-target surfaces** | `Arbeidsgiverbyttetesten`; employer specificity as a goal; Stage 3's reconstructive authority; the strategy's `top_employer_problems`. |
| **Proposed fix** | **E1 § mønstre som skal erstattes** names `Når <arbeidsgiver> skal <X>, må <Y> …` as a stock opening to replace, and **§ argumentvaner** prefers claim-first construction. **E2** makes Stage 3 read the voice file as final authorship rather than polish. |
| **Why this fix surface** | this is an authorship habit, not a rule violation. No prohibition will produce a better opening; a generative prior about how this candidate constructs an argument might. It is therefore voice, not doctrine. |
| **Alternatives** | *(a) A doctrine rule forbidding employer-situation openings* — over-broad; some vacancies genuinely need one, and a ban would push the model to a different stock form. *(b) Prescribe an opening template* — replaces one formula with another. *(c) Do nothing* — the openings are acceptable; this is the weakest entry in the registry and is explicitly a judgement call. |
| **Interactions** | With **ISS-10** and **ISS-11** — all three are the same underlying phenomenon (a polished-application prior at Stage 3) and all three are addressed by E1 plus the B3 `structure_guidance` sentence. **No separate mechanism is added for any of them.** |
| **Architecture impact** | none |
| **Cost/risk** | included in E1. Risk: over-correction producing mannered openings. Mitigated by E1's anti-caricature section and the blind A/B. |
| **Verification** | Run B blind A/B; the named pattern absent or deliberately retained with a stated reason |
| **Acceptance** | each opening reaches the candidate within its first sentence or two and would not read as generic consultant copy if the employer name were removed. |

---

## ISS-10 — Letter macro-skeleton prescribed by `structure_guidance` in both jobs

| Field | Value |
|---|---|
| **Affected** | both jobs; `strategy.application_direction.structure_guidance`; both final letters |
| **Observed evidence** | Huseierne: *"Åpne med arbeidsgiverproblemet … Avslutt med konkret motivasjon og ønsket bidrag."* Avinor: *"Åpne med Avinors gjennomførings- og gevinstproblem … Avslutt med samfunnsoppdraget og et nøkternt bilde av bidraget."* Both letters follow: employer problem → proof 1 → proof 2 → current role → motivation → polite close. |
| **Expected** | the letter's shape follows this vacancy's decision problem |
| **Actual** | both strategies independently prescribed the same generic open/body/close skeleton, and both letters followed it |
| **Employer-facing consequence** | low per job — the shape is defensible for both vacancies. Moderate at cluster scale, where a recruiter would never see two but the operator would notice the framework has one letter shape. |
| **First stage introduced** | **Stage 1** |
| **Stages that could have repaired it** | Stage 2 and Stage 3, both of which had full freedom over structure |
| **Root cause** | a **convergent prior**, not cross-job carry-over: the two strategies were written independently with a reset between jobs and their wording differs. The `structure_guidance` field invites an opening/body/closing answer and the model fills it the same way each time. |
| **Contributing factors** | Stage 1's obligations list requires a motivation bridge and CV/letter allocation, which naturally produces a sequence; nothing tells Stage 1 that the field should express *this vacancy's argument* rather than a letter template |
| **Root-cause confidence** | HIGH for the mechanism, MODERATE for the claim that a different shape would be better for either job |
| **Severity** | LOW |
| **Recurrence** | HIGH |
| **Systemic/local** | systemic |
| **Scope boundary** | what `structure_guidance` is for. **Not** a requirement that letters differ. |
| **Non-target surfaces** | the strategy schema; `application_direction`; the observed shape itself, which remains a legitimate answer when the vacancy supports it; `Variasjon innenfor en klynge`, which is already correct. |
| **Proposed fix** | **B3** — one sentence in the Stage-1 instruction: `structure_guidance` must name the argument this vacancy needs and must not prescribe a default letter skeleton. Reinforced by **E1 § setningsarkitektur** (vary paragraph shape between jobs when the vacancy gives grounds). |
| **Why this fix surface** | the field is authored at Stage 1, so that is where the instruction belongs. One sentence. |
| **Alternatives** | *(a) Remove `structure_guidance`* — removes a useful field to fix its guidance. *(b) A cross-job similarity detector* — explicitly prohibited (Contract §22, Spec §3); `EXP-07` defers convergence to human observation. *(c) Require structural variation* — **rejected**: would reward difference for its own sake and could make one letter worse to keep it unlike the other. |
| **Interactions** | With **ISS-05** — removing "close with motivation" removes the ordering pressure that creates a motivation-shaped hole. With **ISS-09**, **ISS-11** — same underlying prior, one shared fix. |
| **Architecture impact** | none |
| **Cost/risk** | one sentence |
| **Verification** | **judged on the strategy field, not the letter's silhouette.** Two jobs may legitimately converge if both need the same shape. The failure signal is a `structure_guidance` that would read identically for any employer. |
| **Acceptance** | each `structure_guidance` names something specific to its vacancy's decision problem and could not be transplanted to the other job unchanged. |

---

## ISS-11 — Stock closing formula and generic contribution sentence

| Field | Value |
|---|---|
| **Affected** | both jobs; `draft_package` and `final_package`; letter closing and motivation paragraph |
| **Observed evidence** | *"Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan …"* — **4 occurrences across 2 jobs × 2 stages**; Stage 3 did not touch it in either job. *"Jeg ønsker å bidra …"* as a standalone motivation sentence in both final letters. |
| **Expected** | a close that adds something; motivation expressed through the work |
| **Actual** | an interchangeable ceremonial closing and a generic contribution sentence, both surviving reconstruction untouched |
| **Employer-facing consequence** | the last sentence a recruiter reads is boilerplate. Small per instance, but it is the most reproducible formulaic signature in the pilot and the clearest single marker of generic application prose. |
| **First stage introduced** | **Stage 2**, retained verbatim by **Stage 3** |
| **Stages that could have repaired it** | Stage 3, which rewrote everything around it and left it intact — strong evidence that it is a default the model does not perceive as content |
| **Root cause** | a generic application-writing prior for closings; nothing in the doctrine addresses closings, and `Rolig faglig tyngde` targets self-description rather than ceremony |
| **Contributing factors** | closings are low-attention; `Tjuesekunderstesten` reads top-down and never reaches them |
| **Root-cause confidence** | HIGH |
| **Severity** | MEDIUM |
| **Recurrence** | CERTAIN on current evidence — 4/4 |
| **Systemic/local** | systemic |
| **Scope boundary** | closing formulae and standalone contribution sentences. **Not** the existence of a closing, and not politeness. |
| **Non-target surfaces** | `Med vennlig hilsen` and the signature block, which are correct letter convention; the `closing` field. |
| **Proposed fix** | **E1 § mønstre som skal erstattes** names both patterns as patterns to replace, not as banned strings. |
| **Why this fix surface** | derived from actual observed output, which makes it the highest-confidence part of the voice file. It is a candidate-specific expression matter, not universal doctrine — a different candidate might legitimately close that way. |
| **Alternatives** | *(a) A doctrine rule against ceremonial closings* — makes a candidate-specific preference universal. *(b) A deterministic phrase check* — forbidden by `INV-07` and Spec §10.3, which state that generic style phrases must never fail deterministic validation. *(c) Do nothing* — 4/4 recurrence and Stage 3's failure to touch it say it will not self-correct. |
| **Interactions** | With **ISS-05** and **ISS-09** — same prior, one mechanism. With **ISS-02** — a shorter close reclaims a little vertical space. |
| **Architecture impact** | none |
| **Cost/risk** | ~6 lines in E1. Risk: a banned-phrase list read as a lint. Mitigated by framing them as patterns to replace and by stating explicitly that this is semantic guidance which must never fail validation. |
| **Verification** | Run B: the four named patterns absent, or deliberately retained with a better reason. **Not a lint.** |
| **Acceptance** | the two letters do not share a closing formula, and neither close is interchangeable between them. |

---

## ISS-12 — Ordinary hyphen used as a clause divider in generated prose

| Field | Value |
|---|---|
| **Affected** | `huseierne_strategi_maalstyring`; `final_package.letter.body_paragraphs[0]`; **one occurrence in the entire pilot** |
| **Observed evidence** | *"…fungerer i arbeidshverdagen **-** en problemstilling jeg kjenner igjen i Huseiernes ambisjon…"* |
| **Expected** | ordinary sentence punctuation where it will do the job; the hyphen reserved for compounds, dates and ranges |
| **Actual** | one hyphen used as a clause divider |
| **Employer-facing consequence** | negligible in isolation |
| **First stage introduced** | **Stage 3** — the sentence is a Stage-3 reconstruction; the Stage-2 draft phrased the same idea without it |
| **Stages that could have repaired it** | Stage 3 |
| **Root cause** | no punctuation guidance exists anywhere in the control plane |
| **Contributing factors** | none identified |
| **Root-cause confidence** | HIGH |
| **Severity** | LOW |
| **Recurrence** | MODERATE — one instance in roughly 3,700 words of generated Norwegian |
| **Systemic/local** | local, but the absence of a rule is systemic |
| **Scope boundary** | one short doctrine subsection. **No validator.** |
| **Non-target surfaces** | hyphens in compounds (`Barne- og ungdomsklinikken`, `Vakt- og sikringssoldat`), dates and ranges; `|` as a structural divider; the semicolon, which remains permitted but uncommon. |
| **Proposed fix** | **D5** — a short `Tegnsetting` subsection in `WRITING_DOCTRINE`, explicitly marked semantic guidance that must never fail deterministic validation (`INV-07`, Spec §10.3). |
| **Why this fix surface** | universal writing doctrine, applicable to any candidate, so it belongs in the canonical universal source and not in the candidate voice file. The voice file points at it rather than duplicating it. |
| **Alternatives** | *(a) A validator or render warning* — outcome D says not to assume one is needed, `INV-07` forbids failing on a character, and a warning would not detect clause hyphens without false positives. *(b) Put it in the voice file* — makes universal punctuation candidate-specific. |
| **Interactions** | With **ISS-07/ISS-08** — same mandatory outcome, different layers: D5 covers generated prose; D1/D3/D4 cover deterministic sources. Human extraction/inspection verifies the combined output. |
| **Architecture impact** | none |
| **Cost/risk** | ~8 lines of Norwegian |
| **Verification** | Run B semantic review; no mechanical check |
| **Acceptance** | no hyphen used as a clause divider in either Run B letter. |

---

## ISS-13 — Employer-facing outputs unreadable: staging-directory ACL carried by a same-volume move

| Field | Value |
|---|---|
| **Affected** | both jobs; all four output DOCX; `runtime/jobbsok/render.py`; operator workflow |
| **Observed evidence** | current file bytes are readable by `vhaala\CodexSandboxOnline`, the file owner. Each pilot output has a protected DACL owned by that SID with only Owner Rights, SYSTEM and Administrators; `vhaala\veggi` is absent. Its parent `out/` is unprotected and inherits `vhaala\veggi` FullControl. Earlier human-context reads returned `ERROR_ACCESS_DENIED`. The contrast is current and identity-specific, not a corrupt-file symptom. |
| **Expected** | the human can open the employer-facing files from the run output directory |
| **Actual** | the sandbox owner can read the files, but the human account cannot open them directly from the canonical output path |
| **Employer-facing consequence** | none to the document content. **Real operator friction**: the human cannot review the deliverable where the system says it is, and `status --json` names an unreadable path as the output. `verify_receipt` re-reads the output to re-hash it, so `status` run by the human reports the render unverifiable. |
| **First stage introduced** | none — deterministic render code |
| **Stages that could have repaired it** | none |
| **Root cause** | `render_job` opens `TransactionDir(Path(tempfile.gettempdir()), …)`. In Python 3.14.3, `tempfile.mkdtemp()` calls `os.mkdir(..., 0o700)`; Windows gives that directory a protected creator-only DACL. The generated DOCX inherits it, and same-volume `os.replace` preserves it instead of re-evaluating `out/` inheritance. |
| **Contributing factors** | staging is remote from the destination, so export also relies on `%TEMP%` and the destination sharing a volume |
| **Root-cause confidence** | HIGH — current file/parent SDDL, current process SID, Python version/source and the promotion code form one consistent chain |
| **Severity** | HIGH (operator-facing) |
| **Recurrence** | CERTAIN under the same execution context |
| **Systemic/local** | systemic |
| **Scope boundary** | render workspace creation and location: one opt-in mode on `TransactionDir`, used only by `render_job`. **Not** the private rollback workspace, promotion decisions, `promote_file`, no-clobber/`REFUSED_FOREIGN`, or the PDF converter's internal temp handling. |
| **Non-target surfaces** | `atomicio.promote_file`; `Promotion` semantics; `ACC-17` human-edit protection; `verify_receipt`; `pdf.py`. |
| **Proposed fix** | **F1** — add `inherit_parent_permissions=False` to `TransactionDir`. When true, create a collision-safe hidden directory with `Path.mkdir(mode=0o777)` rather than `mkdtemp`'s special `0o700`. `render_job` alone opts in and stages under the actual `out_dir`; rollback stays private. |
| **Why this fix surface** | a parent-path-only change is provably insufficient under Python 3.14. The opt-in preserves the private default, gives employer-facing files the destination's intended access policy, satisfies `DEC-21`'s temporary job-path rule for canonical renders, and guarantees same-volume atomic promotion for canonical and `--dest` output. |
| **Alternatives, and why they lose** | *(a) Merely pass the job directory to `mkdtemp`* — still creates `0o700`; this was the first design and is rejected. *(b) Reset ACL after promotion* — Windows-specific security-descriptor code and a period where the canonical file is wrong. *(c) Copy instead of move* — can re-inherit but must be rebuilt as sibling-temp + rename to retain atomicity; larger than an opt-in directory creation. *(d) Document a copy-out step* — leaves canonical status/receipt paths unusable. *(e) Change `%TEMP%` ACL* — `mkdtemp`'s protected child still defeats it. |
| **Interactions** | With the whole verification plan — **until this is fixed, no human can open a rendered package from the run directory**, which is why it is sequenced first among the code changes. `MAX_PATH_CHARS = 240` constrains the staging directory name: the longest current output path is ≈200 characters, so the prefix must be short. |
| **Architecture impact** | none; implementation-only correction that increases conformance with `DEC-21`. Containment is preserved — `runs` is already a writable root. |
| **Cost/risk** | ~20 lines in `atomicio.py`, one render call-site change. Risk: accidentally making rollback snapshots inheritable; prevented by default-false and a test that only render opts in. A killed process can leave `.rnd.*` under `out/`. |
| **Verification** | focused test asserts render stages under `out_dir` with the inheritance option and cleans the workspace; target-machine `Get-Acl` confirms the staging/output DACL is unprotected/inherited; then the human opens both DOCX directly from `out/`. |
| **Acceptance** | both produced DOCX are readable and openable by `vhaala\veggi` directly from the run output directory. |

---

## ISS-14 — Two tests coupled to production role mapping

| Field | Value |
|---|---|
| **Affected** | `runtime/tests/test_t05_t08_ownership_schema_failure.py`; the full-suite baseline |
| **Observed evidence** | line 178 asserts `stage1["configured_model"] is None`, but `conftest.py` copies the real `policy/` tree and production `settings.toml` now contains `SOL_CLASS = "Codex / GPT-5.6 Sol"`. `test_t05_context_exposes_configured_capability_surface` performs `.replace('SOL_CLASS = ""', …)`, and that literal no longer exists, so the replacement is a no-op and the assertion compares the real mapping against a synthetic value. |
| **Expected** | tests are configuration-independent (F20 and the explicit standing rule) |
| **Actual** | both fail as a direct consequence of the human correctly performing GATE-10 |
| **Employer-facing consequence** | none. It blocks every acceptance gate that depends on a green suite. |
| **First stage introduced** | test authoring, before GATE-10 was performed |
| **Stages that could have repaired it** | n/a |
| **Root cause** | tests written against a placeholder configuration value that the human was always required to change |
| **Contributing factors** | `conftest.py` copies the **real** `authorities/ context/ policy/ templates/ schemas/` trees into every test build root, so production values reach test expectations by design |
| **Root-cause confidence** | HIGH — confirmed by source inspection, and independently reproduced by the Codex handoff at 239 passed / 2 failed / 10 skipped |
| **Severity** | MEDIUM |
| **Recurrence** | CERTAIN until fixed |
| **Systemic/local** | local defect, systemic lesson |
| **Scope boundary** | the two tests and one shared helper. **Not** production `settings.toml`, not runtime behaviour, not the schema, not the GATE-10 evidence. |
| **Non-target surfaces** | `policy/settings.toml`; `manifest.settings.snapshot`; `stage_policy_sha256`; `GATE_REPORTS.md`; `conftest.py`'s policy-copy behaviour, which is correct and deliberate. |
| **Proposed fix** | **F2** — a helper that rewrites the `[stages.role_mapping]` block deterministically and value-independently **before `freeze`** (required by F24, since `assets.settings` resolves to the run's frozen copy). Both tests then assert their own synthetic values. |
| **Why this fix surface** | fixture ownership is the durable fix and the one the standing rule actually asks for. It also **increases** coverage: the first test currently asserts a placeholder is absent; afterwards it proves the configured mapping genuinely flows through the public handoff. |
| **Alternatives, and why they lose** | *(a) Delete the `is None` assertion* — the smallest change, but it removes coverage and teaches the wrong lesson; the test would still be silent about whether the mapping propagates. *(b) Blank the production mapping* — expressly forbidden; it would falsify GATE-10 evidence. *(c) Stop copying the real policy tree in `conftest`* — a large change to a deliberate design that gives tests realistic inputs. |
| **Interactions** | none with A–E. Sequenced **first** because it is bounded, independently reproduced, and every later gate depends on a green suite. |
| **Architecture impact** | none |
| **Cost/risk** | one helper plus two call sites; low |
| **Verification** | both tests pass with the production mapping populated **and** with it blank |
| **Acceptance** | full suite 251 passed / 0 failed / 0 skipped in a Word-COM session before any other change lands. |

---

## ISS-15 — Pilot log never captured; no human-effort evidence exists

| Field | Value |
|---|---|
| **Affected** | `P0.9/Build/pilot/PILOT_LOG.csv`; the entire evaluation loop |
| **Observed evidence** | the file contains only its 19-column header and was last written `2026-08-24`, before the pilot froze on `2026-08-28` |
| **Expected** | per-job triage, actual repair scope, submit-ready, factual corrections, human minutes through submission, render issues, friction and outcome (Spec §18.3, `ACC-20`) |
| **Actual** | nothing recorded |
| **Employer-facing consequence** | none directly. It means **this pass has no measurement of whether it reduced human repair effort**, and the representative cluster will produce none either unless the loop changes. |
| **First stage introduced** | operator workflow |
| **Stages that could have repaired it** | the operator, after render |
| **Root cause** | the RUNBOOK's vacancy loop does not include a log-writing step, so nothing prompts it |
| **Contributing factors** | `[paths].pilot_log` is one of the six settings keys read by no code (F22); automatic pilot-log tooling was considered and deliberately deferred |
| **Root-cause confidence** | HIGH |
| **Severity** | MEDIUM |
| **Recurrence** | HIGH |
| **Systemic/local** | systemic |
| **Scope boundary** | one RUNBOOK line and an acceptance obligation. **No tooling.** |
| **Non-target surfaces** | `[paths].pilot_log` — stays unwired, per the standing deferral; the CSV schema, which already has the right columns; any automatic capture. |
| **Proposed fix** | one line in `policy/RUNBOOK.md` placing the log entry immediately after the human reviews the rendered package, plus a **Run B acceptance requirement** that two rows exist. |
| **Why this fix surface** | the columns already exist and the act is human. The gap is that nothing asks for it at the moment the information is in the operator's head. |
| **Alternatives** | *(a) Build capture tooling* — previously deliberated and deferred; a deferred item returns only on repeated real-production evidence that also beats the smallest local remedy, and a RUNBOOK line is the smallest local remedy. *(b) Wire `[paths].pilot_log`* — F22 records that the six dead keys were deliberated and deferred; none causes a production failure. *(c) Accept the gap* — leaves the pass unmeasurable. |
| **Interactions** | With every semantic change: the log is the only instrument that will show whether B, C and E reduced repair effort. |
| **Architecture impact** | none; it moves toward `ACC-20` compliance |
| **Cost/risk** | one line, two rows |
| **Verification** | two rows present after Run B |
| **Acceptance** | `PILOT_LOG.csv` contains one complete row per Run B job. |

---

## ISS-16 — CV page 2 underutilized · **merged into ISS-01, no separate fix**

Recorded so the merge is auditable rather than silent.

`CV_MASTER.docx` contains **zero** page breaks and zero `lastRenderedPageBreak`; the forced break that
existed in the P0.7 original was removed under GATE-05. There is no static page-2 layout, so page 2
exists only on overflow. At 9 pt the CV runs to roughly 1.2 pages, leaving page 2 nearly empty; at the
A1 tier scale it runs to roughly 1.5 pages, which populates it.

The observed symptom and the typography complaint therefore have **one cause and one fix**. Adding a
content-allocation or page-balance mechanism on top of A1 would be a redundant second remedy for an
already-mitigated issue, which the governing instructions explicitly forbid.

Residual risk: if the A1 scale pushes a future CV to three pages, `cv_expected_max_pages = 2` produces
an advisory warning and **A3** directs the response to editorial compression, never to type-size
reduction. `DEC-24` forbids deleting decision-relevant content to satisfy a page rule. This is
measured in Run A1, not assumed.

---

## 17. Reproduced and **not** defective — protected from refactoring

Recorded explicitly because the governing instructions require adjacent non-defective behaviour to be
named and protected.

| Observation | Why it is correct |
|---|---|
| Two CV bullets byte-identical across both jobs | `Variasjon innenfor en klynge`: *"Delte fakta er legitimt; gjentatt generisk ordlyd … er det ikke."* These are specific factual statements in different positions, inside CV top zones that differ materially. |
| **Avinor's societal-purpose motivation paragraph** | Names the operating environment, which is a causal feature of the work and the basis of the transfer argument. Legitimate under the existing `Begrunnet motivasjon`. **Must survive the change set.** |
| The Avinor sentence *"forventninger må gjøres etterprøvbare, ansvar og antakelser må være synlige, og metoden må fungere for dem som skal bruke den"* | The strongest existing evidence of the candidate's professional voice. Carried as a **regression guard**: if Run B loses this quality, the change set is over-applied. |
| Stage 3 removing both defensive "I lack X" paragraphs | Correct under `TOO_WEAK`; limitations preserved in `review.known_limitations`. |
| Both `READY` triage values | Correctly calibrated against the P0.9.1 definition; no known material repair remained. |
| Exclusion of the AI-generated JobMatch panel from evidence, in both jobs independently | Exactly right, and recorded in `risk_notes`, `avoid_guidance` and the review `notes`. |
| Render `DEGRADED` on the pilot | A Word-COM session fact, not a converter defect. Correct under `DEC-41`. |
| Header and footer at 8 pt | Deliberately subordinate running furniture, in the user's discrete scale. |
| The six `source: none` template zones | Render as absent, not as leftover placeholders. Working as designed. |
| `upstream_claim_repaired: null` in both reviews | Truthful — no overclaim was present. The gap was the *opposite* direction, which ISS-06 addresses. |
