# P0.9 External Evidence Report — Jobbsøk_26

## 1. Decision-impact summary

- **Assumption challenge (context loading):** GPT-5.6 Sol and Terra advertise a context window of over 1 million tokens with up to 128,000 output tokens, but a single ChatGPT/Work uploaded text/document file is capped at 2 million tokens and 512 MB, and Enterprise document ingestion reportedly loads ~110,000 tokens into context with the remainder retrieved. A "read all jobs in one big file, fully in context, every turn" design is therefore not guaranteed by the window size alone. [FACT-FIRST-PARTY][VOLATILE]
- **Assumption challenge (model tiers/pricing):** Verified current pricing (effective 30 July 2026) is Sol $5/$30, Terra $2/$12, Luna $0.20/$1.20 per million input/output tokens — Terra and Luna are cheaper than the brief's implied figures. Terra/Luna are NOT selectable in normal ChatGPT chat; they appear only in ChatGPT Work, Codex, and the API. Sol in chat requires medium-or-higher effort. [FACT-FIRST-PARTY][VOLATILE]
- **Luna long-context collapse:** Luna scores 41.3% on OpenAI MRCR v2 8-needle at both 256K–512K and 512K–1M, versus Sol 91.5%/73.8% and Terra 89.6%/72.5%. A cheap-model context-preparation pass (3c) that uses Luna over a large corpus is evidentially risky. [FACT-FIRST-PARTY]
- **Structured output (DC-4):** JSON-Schema-enforced Structured Outputs (constrained decoding) is an API-only guarantee. The OpenAI Structured Outputs guide states it "ensures the model will always generate responses that adhere to your supplied JSON Schema" and lists support only for "the Responses API, Chat Completions API, Assistants API, Fine-tuning API and Batch API" — not manual ChatGPT Work/Codex chat output. So `strategy.json` cannot be trusted as schema-valid when produced inside a chat turn; this favors `strategy.md` or a deterministic local validator. [FACT-FIRST-PARTY]
- **In-turn validate-repair-revalidate (N-04):** Codex CLI/IDE/desktop CAN run a validator, read errors, edit the artifact, and re-run within one agentic session (workspace-write sandbox auto-runs routine commands). Plain ChatGPT web chat CANNOT — it "doesn't expose the local Codex sandbox or approval-mode selector." N-04 is feasible only on the Codex surface, not on a plain "GPT web - Work" chat. [FACT-FIRST-PARTY]
- **Lost-in-the-middle is real and current:** Liu et al. (TACL 2024) find "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models"; corroborated by RULER/∞Bench and HELMET (2024–2026). Sequential jobs in one long chat will not receive uniform quality. [RESEARCH]
- **Summarization/compression chains lose decision-relevant info:** arXiv:2606.29251 finds "LLM-based compression can produce fluent and factually plausible compressed contexts that nevertheless alter downstream decisions" via "decontextualization, where salient evidence is retained but separated from the caveats and contextual qualifiers needed for correct interpretation"; multi-document work reports iterative pipelines "suffer catastrophic information loss." This cautions against any lossy model summary as the fact carrier. [RESEARCH]
- **Anchoring is measurable in LLMs:** Preliminary summaries/labels/relevance tiers bias later judgments; "reasoning is a cure to break this shallow anchoring" while simple prompt tricks are "not sufficient." Supports (but does not prove for this project) independent-read-first / delayed-context protocols and reversible annotation over destructive filtering. [RESEARCH]
- **Norwegian public sector — kvalifikasjonsprinsippet:** For state jobs it is lovfestet in statsansatteloven §3. Prop. 94 L (2016–2017) states "Det er de kravene som er fastsatt i kunngjøringsteksten som danner grunnlaget for den sammenlignende vurderingen av søkernes kvalifikasjoner," and Statens personalhåndbok pkt. 2.3.3.1 weights "utdanning, erfaring og personlig egnethet, sammenholdt med kvalifikasjonskravene som er fastsatt i utlysningen." Architecturally, the product must itemize each vacancy's stated krav and the candidate's evidence for it. [FACT-FIRST-PARTY]
- **Attachment/format limits are per-employer, not platform-wide:** In Webcruiter, whether a CV is required, whether attachments are mandatory vs optional, and whether the letter is a free-text field or replaced by a question module are all configured by the recruiting organisation. Limits cannot be hardcoded; they must be read from each vacancy. [FACT-FIRST-PARTY][COMMUNITY]
- **Application letter is usually a free-text field, not an upload:** In Webcruiter the søknadstekst is typically typed into the portal (and can be employer-replaced by a question module), constraining how much rendered-DOCX formatting ever reaches the employer for the letter. [FACT-FIRST-PARTY][COMMUNITY]
- **Content controls (SDT) are a rendering hazard:** LibreOffice is documented to show only placeholder text for data-bound Word content controls (not the bound value), and python-docx edits to `w:sdt` content frequently fail to persist. Template masters should avoid data-bound SDTs. [COMMUNITY]
- **Prompt injection cannot be fully solved and regex filters are not a primary control:** OpenAI agent-safety guidance says to "pass untrusted inputs through user messages" and "define structured outputs between nodes"; OWASP LLM01:2025 concludes injection cannot be fully mitigated and recommends defense-in-depth (least-privilege tooling, input/output filtering, human approval for high-risk actions, adversarial testing). An "AI firewall"/regex is risk-reduction only. [FACT-FIRST-PARTY][RESEARCH]
- **LibreOffice headless multi-file conversion has documented failure modes:** profile-lock contention (mitigated by per-invocation `-env:UserInstallation`), Windows quoting/URI pitfalls (retval=1), and non-preservation of metadata. Convert one job transaction at a time with an isolated profile. [COMMUNITY][FACT-FIRST-PARTY docs]
- **Cluster size and effort defaults are LOCAL-TEST territory** — do not derive from benchmarks. [LOCAL-TEST]

## 2. Current OpenAI capability matrix

| Capability | Surface/model | Current fact | Source/date | Confidence | Architectural relevance |
|---|---|---|---|---|---|
| Availability | Sol/Terra/Luna | GA since 9 July 2026 across ChatGPT, Codex, API | openai.com/index/gpt-5-6, 9 Jul 2026 | High [FACT-FIRST-PARTY] | Confirms all three tiers usable |
| Chat access | Sol | Plus/Pro/Business/Enterprise access Sol at medium+ effort; Sol Pro for Pro/Enterprise | openai.com, 9 Jul 2026 | High | Effort routing lever |
| Work/Codex access | Terra/Luna | Free/Go get Terra; paid choose Sol/Terra/Luna and set per-model effort; `max` all tiers; `ultra` (4-agent) Pro/Enterprise in Work, Plus+ in Codex | openai.com, 9 & 30 Jul 2026 | High | Terra/Luna only outside normal chat |
| Effort settings | All | medium/high/xhigh/`max`; `ultra` = 4 parallel agents | openai.com, 9 Jul 2026 | High | Effort routing lever |
| Context window | All tiers | >1,000,000 tokens; up to 128,000 output tokens | emergent.sh citing OpenAI launch, Jul 2026 | Medium [VOLATILE] | Large but see file caps |
| Long-context quality | MRCR v2 8-needle | Sol 91.5%/73.8%; Terra 89.6%/72.5%; Luna 41.3%/41.3% (256K–512K / 512K–1M) | openai.com, 9 Jul 2026 | High | Luna unsafe for long shared context |
| Pricing (current) | Per 1M tokens | Sol $5/$30; Terra $2/$12; Luna $0.20/$1.20 | openai.com, 30 Jul 2026 | High [VOLATILE] | Effort/stage cost model |
| Prompt caching | All | Explicit cache breakpoints; 30-min min cache life; writes 1.25×, reads 90% discount | openai.com, 9 Jul 2026 | High | Repeated authority-file reads cheaper |
| File upload cap | ChatGPT/Work | 512 MB/file; 2M tokens/file (text/doc); ~10 files/message batch; Projects 20 (Plus)/40 (higher) | help.openai.com File Uploads FAQ, 2026 | Medium [VOLATILE] | Multi-file chat design limit |
| Enterprise doc ingest | ChatGPT Enterprise | Reported: ~110,000 tokens loaded into context, remainder via retrieval | datastudios.org, 2025 | Low [COMMUNITY] | "Read everything" not guaranteed |
| Structured Outputs | API only | JSON-Schema strict mode via constrained decoding = schema-guaranteed | developers.openai.com structured-outputs | High [FACT-FIRST-PARTY] | DC-4: JSON trustworthy only via API/local validation |
| Codex local access | CLI/IDE/desktop | OS sandbox; default workspace-write (read almost anywhere, write in workspace, no network unless enabled); approval policy | developers.openai.com Codex docs, 2026 | High [FACT-FIRST-PARTY] | N-04 feasible on Codex |
| Codex Windows sandbox | Windows | Elevated (recommended) vs unelevated fallback; SIDs + write-restricted tokens; no admin elevation needed | openai.com Codex Windows sandbox, 2026 | High | Local finalize scripts fit workspace-write |
| Retention | Business/Enterprise | Not trained on by default; deletions removed within 30 days; admin-set retention (Enterprise min 90 days); non-Library files expire 48h (Enterprise) | openai.com/enterprise-privacy; help.openai.com, 2025–2026 | High [FACT-FIRST-PARTY] | Candidate-file privacy |
| ZDR | API | Programmatic Tool Calling is ZDR-compatible; ZDR for eligible endpoints | openai.com, 9 Jul 2026 | High | Only relevant if API used |

## 3. Decision-critical findings

**Finding A — Tier availability by surface constrains stage allocation.**
Evidence: "Terra and Luna are not selectable in normal ChatGPT chats — they show up in Codex, Work, and the API instead"; Work/Codex paid users "choose among GPT-5.6 Sol, Terra, and Luna and set an effort level for each." [FACT-FIRST-PARTY, openai.com 9 Jul 2026; techjournal.org]
Applicability: A manual flow can route work across all three tiers only inside Work/Codex/API, not plain chat.
Affected decisions: model/stage allocation; effort routing.
Does NOT establish: whether a single Work conversation can switch tiers mid-thread.
Residual uncertainty: per-message tier/effort switching inside one Work thread.
Best next evidence: LOCAL TEST — attempt per-message tier/effort switch in one Work chat.

**Finding B — Verified current pricing supersedes the brief's figures.**
Evidence: 30 July 2026 OpenAI post: Terra "$2 per million input tokens and $12 per million output tokens" and Luna "$0.20 per million input tokens and $1.20 per million output tokens"; "Sol pricing remains unchanged" ($5/$30). [FACT-FIRST-PARTY]
Applicability: Confirms the brief's 30 July reduction; replace any earlier numbers with these.
Affected decisions: effort/stage cost model.
Does NOT establish: ChatGPT Work/Codex credit-to-token conversion ("quota budgets remain unchanged; Terra and Luna usage now consumes fewer credits").
Residual uncertainty: exact credit accounting in Work.
Best next evidence: USER DECISION on plan + LOCAL TEST of credit burn.

**Finding C — Luna collapses on long multi-needle retrieval.**
Evidence: MRCR v2 8-needle: Luna 41.3% at both 256K–512K and 512K–1M vs Sol 91.5%/73.8%, Terra 89.6%/72.5%; GraphWalks BFS 1M f1: Luna 51.2% vs Sol 77.1%. [FACT-FIRST-PARTY]
Applicability: A Luna preparation pass over the full corpus (3c) risks missing/mis-locating facts.
Affected decisions: DC-3 (3c feasibility); context-loading design.
Does NOT establish: Luna performance on small, job-local slices (short context may be fine).
Residual uncertainty: quality at this project's actual per-job context sizes.
Best next evidence: LOCAL TEST — Luna preparation over a real 2-job slice, checked against source.

**Finding D — Structured Outputs schema guarantee is API-only (DC-4).**
Evidence: OpenAI Structured Outputs guide: "Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema… Both Structured Outputs and JSON mode are supported in the Responses API, Chat Completions API, Assistants API, Fine-tuning API and Batch API." No enforceable equivalent is documented for manual ChatGPT Work/Codex chat output. [FACT-FIRST-PARTY]
Applicability: `strategy.json` produced inside a manual chat turn is NOT schema-guaranteed; only an API call or a local validator can enforce it.
Affected decisions: DC-4 (strategy.json vs strategy.md); structured-handoff assumptions.
Does NOT establish: that JSON is unusable — only that validity must be enforced deterministically outside the chat.
Residual uncertainty: real-world malformed-JSON rate for this schema in unconstrained chat.
Best next evidence: LOCAL TEST — local JSON-schema validator on chat output across N jobs; measure repair rate.

**Finding E — In-turn validate-repair-revalidate (N-04) depends on surface.**
Evidence: Codex "can read files, make edits, and run commands in the working directory automatically" in Auto/workspace-write; approval policy governs pauses. ChatGPT web "doesn't expose the local Codex sandbox or approval-mode selector." [FACT-FIRST-PARTY]
Applicability: N-04 (validator → read error → repair → re-validate in one turn, no second prompt) is achievable only in a Codex agentic session, not in plain "GPT web - Work" chat.
Affected decisions: N-04; manual-chat interactive feasibility; where finalize/validation lives.
Does NOT establish: reliability/step-count for this specific validator.
Residual uncertainty: how many auto-approved iterations Codex takes before pausing.
Best next evidence: LOCAL TEST — Codex run with the real validator on a template.

**Finding F — Lost-in-the-middle and order effects are current and general.**
Evidence: Liu et al. (TACL vol. 12, 2024, pp. 157–173): "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models," worsening as context lengthens; HELMET: models "prefer the most recent context and struggle with recalling facts in the middle and earlier parts." [RESEARCH]
Applicability: Sequential jobs in one long chat will not get uniform treatment; early/late positions favored.
Affected decisions: DC-3; context-loading order/size; cluster design.
Does NOT establish: the exact optimal jobs-per-chat for GPT-5.6 (unrelated benchmarks).
Residual uncertainty: magnitude on GPT-5.6 Sol at this project's sizes.
Best next evidence: LOCAL TEST — early-vs-late job quality within one cluster chat.

**Finding G — Compression/summarization chains distort decisions.**
Evidence: arXiv:2606.29251: "LLM-based compression can produce fluent and factually plausible compressed contexts that nevertheless alter downstream decisions," via decontextualization; arXiv:2502.06617: "iterative methods suffer catastrophic information loss in their multistage pipeline." [RESEARCH]
Applicability: Any stage that replaces the immutable authority files with a model-written summary risks silently dropping decision-relevant facts.
Affected decisions: DC-3 (3b vs 3c); structured-handoff; whether preparation is lossless.
Does NOT establish: that a NON-semantic, deterministic index (3b) loses information — by construction it does not.
Residual uncertainty: whether an advisory (non-destructive) cheap pass avoids the harm.
Best next evidence: RESEARCH sufficient to prefer lossless/reversible; LOCAL TEST for the advisory variant.

**Finding H — Anchoring from preliminary labels/summaries.**
Evidence: 2024–2026 studies find LLM judgments drift toward initial anchors; "reasoning is a cure to break this shallow anchoring" while CoT/ignore-anchor prompts are "not sufficient"; label anchoring shown even when candidates are content-equivalent. [RESEARCH]
Applicability: A cheap model's relevance tiers/labels (3c) could bias a stronger model's independent judgment; independent-read-first / delayed-context protocols are plausible mitigations.
Affected decisions: DC-3 (3c anchoring risk); handoff format (advisory vs authoritative).
Does NOT establish: magnitude for THIS project's "advisory tiers" hypothesis — no direct evidence exists for structured-strategy anchoring in a CV pipeline. [NO-EVIDENCE for the project-specific hypothesis]
Residual uncertainty: whether reversible, source-linked annotation avoids anchoring here.
Best next evidence: LOCAL TEST — compare Sol decisions with vs without the cheap pass visible.

**Finding I — kvalifikasjonsprinsippet drives explicit requirement coverage.**
Evidence: statsansatteloven §3; Prop. 94 L (2016–2017): "Det er de kravene som er fastsatt i kunngjøringsteksten som danner grunnlaget for den sammenlignende vurderingen"; Statens personalhåndbok pkt. 2.3.3.1: weight on "utdanning, erfaring og personlig egnethet, sammenholdt med kvalifikasjonskravene som er fastsatt i utlysningen." [FACT-FIRST-PARTY]
Applicability: Product must produce application text itemizing each stated krav and the candidate's evidence for it, per vacancy.
Affected decisions: what the product must produce; per-vacancy requirement extraction.
Does NOT establish: any specific document format the employer requires (per-vacancy).
Residual uncertainty: none material to the principle.
Best next evidence: REAL VACANCY inspection for stated krav structure.

**Finding J — Per-employer configurability of Webcruiter requirements.**
Evidence: Bærum kommune guide: "Du må legge inn minimum ett vedlegg for å komme videre" plus mandatory work-experience/education; vs Bydel Grorud/Oslo: "Vedlegg… Det er valgfritt" and CV upload "frivillig." Talentech blog: the letter question module "kan også erstatte søknadsbrevet." A DIFFERENT system, Grade/Jobbnorge, documents "The maximum file size for each attachment are 30MB. The maximum total file size for attachments are 100 MB. Allowed file types are: .jpg .jpeg .png .doc .docx .pdf." [FACT-FIRST-PARTY vendor + COMMUNITY employer guides]
Applicability: Limits and required attachments cannot be hardcoded platform-wide; they must be read from each vacancy/portal instance.
Affected decisions: Norwegian ATS boundaries; whether limits are static config or per-vacancy inputs.
Does NOT establish: Webcruiter's own exact max file size/page limit — its "Vedlegg i Webcruiter" support article was not machine-accessible, and the 30MB/100MB numbers above belong to Jobbnorge/Grade, not Webcruiter. [NO-EVIDENCE for exact Webcruiter numeric cap]
Residual uncertainty: Webcruiter numeric file/size caps; any letter character limit.
Best next evidence: REAL VACANCY inspection + user-side login to the actual portals.

**Finding K — Content controls (SDT) degrade through LibreOffice and resist python-docx edits.**
Evidence: Ask LibreOffice: a data-bound content control shows "only the placeholder text" in LibreOffice while Word shows the bound data; python-docx issue #965: content-control `w:t` edits "don't seem to be updating when I save"; Pandoc strips content-control table cells. [COMMUNITY]
Applicability: Data-bound SDTs in the masters risk placeholder leakage in the PDF and unreliable programmatic fill.
Affected decisions: DOCX template constraints; fill mechanism.
Does NOT establish: behavior for non-data-bound plain-text SDTs in the specific LibreOffice version used (version-specific).
Residual uncertainty: current LibreOffice version behavior on the exact template.
Best next evidence: LOCAL TEST — render the real master through headless LibreOffice.

**Finding L — Headless LibreOffice multi-file conversion reliability.**
Evidence: Isolated-profile pattern `-env:UserInstallation=file:///…` documented as enabling concurrent/repeated runs; Windows single-quote/URI quoting bug causes retval=1 (Dolibarr #38651); soffice "does not preserve metadata when converting to PDF" and command-line globbing issues motivate per-file invocation. [COMMUNITY][FACT-FIRST-PARTY docs]
Applicability: Convert one job transaction at a time with a fresh isolated user profile; use double-quoted absolute Windows paths and `soffice.com`; check exit codes and output existence.
Affected decisions: DOCX/PDF rendering constraints; finalize-script reliability.
Does NOT establish: exact multi-file batch exit-code semantics on the target Windows version.
Residual uncertainty: partial-success behavior for a multi-input single invocation.
Best next evidence: LOCAL TEST — batch convert several DOCX and inspect exit codes/outputs.

**Finding M — Norwegian glyphs and font substitution.**
Evidence: LibreOffice embeds fonts on PDF export (since 4.1; 4.2+ tends to always embed); if a requested font is unavailable it silently substitutes a fallback, changing appearance; embedded fonts may not be used in a headless convert on a machine lacking the font. [COMMUNITY]
Applicability: æ/ø/å render correctly only if the chosen font contains the glyphs AND is installed/embedded on the converting Windows machine; substitution is a silent risk.
Affected decisions: safe font family choice; substitution detection.
Does NOT establish: which specific fonts are installed on the target machine (environment-specific); Norwegian locale effect on line-breaking/hyphenation is not separately documented here. [NO-EVIDENCE on nb-NO hyphenation specifics]
Residual uncertainty: exact substitution behavior on the target box.
Best next evidence: LOCAL TEST — render an æ/ø/å sample; enumerate embedded fonts in the output PDF; assert expected font names.

**Finding N — Prompt injection controls for untrusted vacancy documents.**
Evidence: OpenAI agent-safety guide: "Pass untrusted inputs through user messages" (developer messages take precedence and give attackers most control); "define structured outputs between nodes… eliminate freeform channels." OWASP LLM01:2025: injection cannot be fully mitigated; recommends defense-in-depth — least-privilege tooling, input/output filtering, human approval for high-risk actions, adversarial testing. OpenAI publicly acknowledged (13 Feb 2026) injection "may never be fully patched." [FACT-FIRST-PARTY][RESEARCH]
Applicability: Treat vacancy PDFs/docs as untrusted data, not instructions; least-privilege file access; human confirmation before finalize/submit; a regex/"AI firewall" is risk-reduction only, never the primary control.
Affected decisions: minimal security/runtime controls; human-confirmation boundaries.
Does NOT establish: a specific detector's efficacy for Norwegian vacancy text.
Residual uncertainty: residual injection rate after layered controls.
Best next evidence: RESEARCH sufficient for principle; USER POLICY on human-confirmation gates.

## 4. Norwegian platform/template matrix

| Platform | Accepted formats | Auto-parse / manual re-entry | Letter: upload/free-text/either | Field limits | Mandatory extra attachments | LibreOffice-vs-Word issues |
|---|---|---|---|---|---|---|
| Webcruiter (Talentech) | CV upload MS Word or PDF (auto-parsed); cloud sources (Drive/OneDrive/Dropbox/iCloud) | Yes — CV parsing to structured CV; but candidate also fills Arbeidserfaring/Utdanning fields | Usually free-text søknadstekst; employer can replace with question module | Exact size/char limits not documented; letter/question config per-employer | Per-employer: mandatory at some (Bærum "minimum ett vedlegg"), optional at others (Grorud "valgfritt") | Not documented for Webcruiter specifically |
| Jobbnorge (Grade) | .jpg .jpeg .png .doc .docx .pdf; 30 MB/attachment, 100 MB total | Structured CV in portal; 3 CV types chosen by employer; no transfer between CV types | Free-text application + attachments | 30 MB/file, 100 MB total; advise filenames with only letters/numbers | Per-vacancy (check utlysning); vitnemål/attester often brought to interview | Not documented |
| Talentech/ReachMee | Not documented in first-party sources accessed | Not documented | Not documented | Not documented | Not documented | Not documented |
| EasyCruit (Visma) | Existing doc formats + image (JPEG) as CV/letter, auto-converted to PDF (Jul 2026 release); CV upload can auto-fill fields | CV upload for autofill OR as attachment; image CV parsing NOT yet supported | Free-text plus screening questions (radiobutton/dropdown, scored) | Employer builds question sets; value thresholds → auto-reject folder | Per-employer; upload points for vitnemål exist but labeling unclear | Not documented |
| Varbi | Not documented in first-party sources accessed | Not documented | Not documented | Not documented | Not documented | Not documented |
| finn.no application flows | Employer-dependent; FINN offers its own CV-template tool; many ads route to external portals or e-mail | Varies; "enkel søknad" flows vary | Either, employer-dependent | Not documented | Per-vacancy | Not documented |

General Norwegian convention (multiple career-service sources): the søknad/letter should be ≤ ~1 A4 page; PDF is strongly recommended for e-mailed/uploaded documents to preserve formatting; vitnemål/attester are typically brought to interview unless requested in the ad. [COMMUNITY]

## 5. Template design rules (Word CV + letter masters)

DO:
- DO author masters as plain styled paragraphs, with real tables only where necessary; keep a single-column main text flow for parseability.
- DO use a font that (a) contains æ/ø/å glyphs and (b) is installed on the converting Windows machine; prefer widely available families (e.g., a Liberation/Carlito/Calibri- or Arial/Times-class font) and embed fonts on PDF export.
- DO fill variable text by direct paragraph/run text replacement (python-docx on normal runs), NOT via Word content controls.
- DO produce the final deliverable as PDF (Norwegian convention; avoids .docx render drift), keeping the DOCX as the editable master.
- DO keep the letter to ≤ 1 A4 page and structure the body to itemize each vacancy krav with candidate evidence (kvalifikasjonsprinsippet).
- DO verify, after conversion, that the output PDF contains no placeholder tokens and that expected fonts are embedded (programmatic check).
- DO convert one job at a time with a fresh `-env:UserInstallation` profile and double-quoted absolute paths; check the exit code AND that the output file exists and is non-empty.
- DO read per-vacancy format/size/attachment/letter-length requirements from each vacancy rather than hardcoding.

DO-NOT:
- DO-NOT use data-bound Word content controls (SDT) or conditional-content controls in the masters (LibreOffice shows placeholder text; python-docx edits unreliable; risk of placeholder leakage / empty paragraphs).
- DO-NOT rely on multi-column layouts, text boxes, headers/footers carrying critical content, or graphics for information that must be parsed by an ATS.
- DO-NOT assume a chosen font is present on the render machine; unhandled substitution is silent.
- DO-NOT assume the letter's rich formatting survives — in Webcruiter the letter is often pasted as free text.
- DO-NOT push many DOCX through a single soffice invocation and assume all-or-nothing success; treat each conversion independently.
- DO-NOT embed instructions in the template that a downstream model might read as commands (injection hygiene).

## 6. Evidence map to open P0.9 mechanisms

| Mechanism/decision | Evidence supporting | Evidence cautioning | Evidential status | Local test still needed? |
|---|---|---|---|---|
| DC-3 (3a direct retrieve) | Sol strong long-context (MRCR 91.5% @256–512K) | Lost-in-middle; file-token caps; ~110K Enterprise ingest | Mixed [RESEARCH+FACT] | Yes — early/late job quality |
| DC-3 (3b deterministic lossless index) | Compression research favors lossless/reversible; no model pass = no anchoring/loss | None material | Favorable by construction [RESEARCH] | Optional |
| DC-3 (3c cheap-model advisory pass) | Anchoring "reasoning is a cure"; advisory/reversible plausible | Luna long-context collapse; anchoring; summary distortion; NO direct project evidence | Contested [RESEARCH + NO-EVIDENCE] | Yes — Sol with/without pass |
| DC-4 (strategy.json vs .md) | API Structured Outputs = schema-guaranteed | Chat has NO enforceable guarantee | Resolved: JSON needs API/local validation [FACT] | Yes — measure chat JSON malformed rate |
| N-04 (in-turn validate-repair-revalidate) | Codex workspace-write auto-runs commands | Plain chat exposes no sandbox | Resolved: Codex-only [FACT] | Yes — iteration count |
| DC-1, DC-2, DC-5, DC-6, DC-7 | — | — | Cannot map without brainstorm_review.md | See §8 |
| N-01, N-02, N-03, N-05, N-06 | — | — | Cannot map without brainstorm_review.md | See §8 |

Note: full mapping to DC-1/DC-2/DC-5/DC-6/DC-7 and N-01/N-02/N-03/N-05/N-06 is not possible without brainstorm_review.md, which was not attached; only DC-3, DC-4, and N-04 are defined inline in the brief and are resolved above.

## 7. Local tests that dominate further research (ranked)

1. **Chat JSON validity rate (DC-4).** Smallest adequate test: run the real strategy prompt on 5–10 jobs in Work chat, feed outputs to a local JSON-schema validator, count malformed/repaired. Dominates because the Structured Outputs guarantee is API-only.
2. **Codex validate-repair loop (N-04).** Smallest adequate test: one Codex session with the actual validator + one deliberately bad artifact; observe whether it repairs and re-validates within one turn and how many auto-approved steps occur.
3. **Early-vs-late job quality in one cluster (DC-3 / lost-in-middle).** Smallest adequate test: a 2-job cluster, swap order, compare output fidelity to source.
4. **Cheap-pass anchoring (DC-3 3c).** Smallest adequate test: Sol decision on 2 jobs with vs without Luna's advisory tiers visible; compare.
5. **Template render fidelity (Track D).** Smallest adequate test: render the real CV+letter masters via headless LibreOffice on the target Windows box; grep the PDF for placeholder tokens; assert embedded font names; check æ/ø/å.
6. **Multi-file conversion robustness.** Smallest adequate test: convert several DOCX one-by-one with isolated profiles; inspect exit codes and outputs.
7. **Real portal limits.** Smallest adequate test: user logs into the actual Webcruiter/Jobbnorge vacancies and records per-vacancy format/size/letter-field limits.

## 8. Conflicts / superseded project assumptions

- **Pricing:** The brief's "Terra/Luna price reduction on 30 July 2026" is correct in direction; verified current numbers are Terra $2/$12, Luna $0.20/$1.20, Sol $5/$30 — use these, not any earlier figures. [FACT-FIRST-PARTY, 30 Jul 2026]
- **"GPT web - Work" chat as universal executor:** The assumption that a manual chat can do everything is partially contradicted — Terra/Luna are unavailable in normal chat (only Work/Codex/API), and in-turn validator execution (N-04) and schema-guaranteed JSON (DC-4) require Codex and API respectively, not plain chat.
- **"Three immutable files as sole fact source" read wholesale in-context:** Compatible with the >1M window in principle, but file-token caps (2M/file), the reported ~110K Enterprise ingest, and lost-in-the-middle mean "the model reliably reads everything, everywhere, every turn" is a design assumption to test, not to assume.
- **Hardcoding ATS limits:** Any assumption that platform format/size/attachment/letter limits are fixed is contradicted; they are per-employer in Webcruiter and per-vacancy in Jobbnorge.
- **Source-document limitation:** The P0.8 spec, P0.8.1, Brainstorm_Brief.md, brainstorm_review.md and the vacancy inventory were NOT attached. I therefore cannot check conflicts against DC-1/DC-2/DC-5/DC-6/DC-7 or N-01/N-02/N-03/N-05/N-06, nor confirm which platforms are actually in the real vacancy set. These require the actual documents.

## 9. Source register (load-bearing)

- OpenAI, "GPT-5.6: Frontier intelligence…" (9 Jul 2026) — tiers, availability, effort, benchmarks incl. MRCR/long-context, pricing, context/output caps. [FACT-FIRST-PARTY]
- OpenAI, "Advancing the price-performance frontier with GPT-5.6" (30 Jul 2026) — Terra $2/$12, Luna $0.20/$1.20, Fast mode. [FACT-FIRST-PARTY]
- OpenAI Developers, Structured Outputs guide — API-only schema guarantee. [FACT-FIRST-PARTY]
- OpenAI Developers, Codex Agent approvals & security / Windows sandbox / Sandbox — local file/command access. [FACT-FIRST-PARTY]
- OpenAI, Enterprise privacy / File Uploads FAQ / Chat & File Retention — retention, 512MB/2M-token caps. [FACT-FIRST-PARTY]
- OpenAI API, "Safety in building agents" — untrusted input via user messages; structured outputs between nodes. [FACT-FIRST-PARTY]
- Liu et al., "Lost in the Middle" (TACL vol. 12, 2024, pp. 157–173); HELMET (arXiv 2410.02694) — positional degradation. [RESEARCH]
- "When Summaries Distort Decisions" (arXiv 2606.29251); "Scaling Multi-Document Event Summarization" (arXiv 2502.06617) — compression/summary information loss. [RESEARCH]
- "Anchoring Bias in LLMs" (arXiv 2412.06593); "Understanding the Anchoring Effect of LLM" (arXiv 2505.15392) — anchoring + mitigation. [RESEARCH]
- OWASP LLM Prompt Injection Prevention Cheat Sheet / OWASP LLM01:2025; Vectra summary of OpenAI Lockdown Mode (13 Feb 2026) — defense-in-depth. [RESEARCH][FACT-FIRST-PARTY]
- Lovdata Statens personalhåndbok 2.1.2.1 / 2.3.3.1; statsansatteloven §3; Prop. 94 L (2016–2017); Juristforbundet — kvalifikasjonsprinsippet. [FACT-FIRST-PARTY]
- Talentech/Webcruiter login & blog; Bærum kommune & Bydel Grorud candidate guides — per-employer config, letter free-text, CV parsing. [FACT-FIRST-PARTY vendor + COMMUNITY]
- Grade/Jobbnorge knowledge base — 30 MB/attachment, 100 MB total, filetypes (NOTE: Jobbnorge/Grade, NOT Webcruiter). [FACT-FIRST-PARTY]
- EasyCruit release notes (Jul 2026) & user manual — image upload→PDF, screening questions. [FACT-FIRST-PARTY]
- Ask LibreOffice (content controls; font fallback/embedding); python-docx issue #965; Dolibarr #38651 — SDT/render/conversion failure modes. [COMMUNITY][FACT-FIRST-PARTY docs]

## 10. What external research cannot decide

Requires USER POLICY decision:
- Which ChatGPT plan/surface (Work vs Codex vs API) and whether API use is acceptable given the "manual chat" constraint — this gates DC-4 (schema-guaranteed JSON) and N-04 (in-turn repair).
- Human-confirmation gate placement for injection defense and manual submission.
- Acceptable privacy posture for uploading candidate authority files (Business/Enterprise default no-training vs API ZDR).

Requires REAL VACANCY / FILE inspection:
- Which platforms are actually in the vacancy set; each vacancy's stated krav structure; per-vacancy format/size/attachment/letter-length limits.
- Whether the CV/letter masters use SDTs today; which fonts they specify.
- Resolution of DC-1/DC-2/DC-5/DC-6/DC-7 and N-01/N-02/N-03/N-05/N-06 (need brainstorm_review.md).

Requires LOCAL TECHNICAL test:
- Chat JSON malformed/repair rate; Codex iteration count; early-vs-late cluster quality; cheap-pass anchoring; LibreOffice render fidelity (placeholder leakage, font embedding, æ/ø/å); multi-file conversion exit-code behavior; optimal cluster size and effort defaults.

---

*Note: This report gathers and tags external evidence only. It does not design, select, evaluate, or recommend a P0.9 architecture, per the brief's scope.*