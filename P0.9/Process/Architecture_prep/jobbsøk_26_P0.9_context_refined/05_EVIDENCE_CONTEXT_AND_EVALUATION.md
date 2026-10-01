# Evidence, Context-System and Evaluation Guidance

## 0. Reading contract

This document organizes empirical and interpretive evidence by **design consequence**. It does not let research choose project policy.

Use the following distinctions:

| Label | Meaning |
|---|---|
| `[FACT]` | External or implementation fact represented with relatively strong support in the corpus |
| `[RESEARCH]` | General empirical evidence that constrains risk or plausibility but is not a direct Jobbsøk_26 experiment |
| `[IMPLICATION]` | Reasoned design consequence of facts/research; not independently established fact |
| `[LOCAL-TEST]` | Claim whose useful answer depends on the target repository, machine, vacancies or model workflow |
| `[USER-POLICY]` | Project choice or permission; it may be authoritative for Jobbsøk_26 without being an empirical claim |
| `[OPEN]` | Current evidence is insufficient to select the final architecture |

Evidence strength must be scoped. Direct inspection of the actual P0.7 master is stronger for that master than generic document advice. Official platform rules are stronger than career-blog convention for platform behavior. A long-context benchmark can establish risk without determining the optimal cluster size for this workflow.

Primary source homes:

- P0.8 external evidence: SRC-09;
- P0.9 focused evidence: SRC-15;
- actual P0.7 implementation/master evidence: SRC-00 and the direct-audit portions of SRC-19;
- latest user/environment/evaluation inputs: SRC-18;
- canonical personality source and proposed interface: SRC-16 and SRC-17.

---

## 1. High-impact evidence map

| Finding | Design consequence | Strength / status |
|---|---|---|
| Norwegian application requirements, formats and portal fields vary by employer and vacancy | Intake must capture per-job channel facts; do not hardcode a universal delivery matrix | `[FACT]` strong where supported by platform/vendor material; actual inventory still required |
| Public-sector selection is tied to advertised qualification requirements | Stage 1 needs explicit requirement→evidence coverage; final prose should remain a coherent argument, not a mechanical checklist | `[FACT]` for state qualification principle; `[IMPLICATION]` for package design |
| Webcruiter commonly represents application text as a free-text field or employer-configured question module | Rendered letter styling may not reach the employer; portal text can be a separate downstream representation | `[FACT]` platform-dependent; supports but does not select portal detachment |
| ATS/parser behavior is heterogeneous and poorly specified | Use conservative logical structure and empirical extraction tests; do not redesign around folklore | `[FACT]` variability; `[LOCAL-TEST]` actual channels |
| Data-bound Word content controls can fail in LibreOffice; P0.7 controls were non-data-bound and unwrapped before conversion | Ban data-bound/transient controls in final output, but do not discard the proven P0.7 fill/unwrap method | Generic `[FACT/COMMUNITY]` plus direct `[VERIFIED]` artifact evidence |
| Headless LibreOffice has profile, quoting and partial-output failure modes | Use isolated profiles and independently validate each output; target machine spike is mandatory | `[FACT/COMMUNITY]`; `[LOCAL-TEST]` exact command/reliability |
| Large context windows do not guarantee uniform retrieval; lost-in-the-middle and upload/retrieval behavior matter | Preserve one-job focus, monitor position effects and avoid “everything is fully read” assumptions | `[RESEARCH]` strong general risk; exact workflow effect `[LOCAL-TEST]` |
| Summarization/compression can retain salient facts while losing qualifiers | Model summaries must not become factual authorities or destructive filters | `[RESEARCH]` supports reversible/source-linked context design |
| Preliminary labels/rankings can anchor later models | Delayed or independently formed judgment and source escape are valuable; preparation remains advisory | `[RESEARCH]`; exact magnitude in this workflow `[LOCAL-TEST]` |
| Manual chat JSON is not API-constrained Structured Output | Any JSON artifact produced in Work/Codex must be validated locally before completion | `[FACT]` represented official capability distinction |
| Codex-style surfaces can run local validators; plain chat cannot be assumed to | Same-session validate/repair depends on selected surface and permissions | `[FACT]` at capability level; `[STEP2_VERIFY]` actual environment |
| Luna is much weaker than Sol/Terra on the cited very-long-context benchmark | Do not use Luna as a global authoritative filter; only bounded advisory experiments | `[FACT]` benchmark; workflow value remains `[OPEN]` |
| Prompt injection cannot be fully solved by regex | Use control/data-plane separation, least privilege, validation and human irreversible gates | `[FACT/RESEARCH]`; no absolute guarantee |
| Historical application outputs and conversion rates are not comparable to the planned job set | Establish a new pilot baseline; do not claim improvement against stale anchors | `[USER-CORRECTION]` |
| The user can support 5–10 h/week and expects 10–20 total human minutes per submitted package | Total human time is a core evaluation metric and architecture constraint | `[USER-POLICY/FACT]` for project |

---

## 2. Norwegian application channels and product boundary

### 2.1 Per-vacancy truth dominates platform averages

The research represented in SRC-15 found that platform behavior is often employer-configurable:

- whether a CV is required;
- whether attachments are mandatory, optional or unavailable;
- whether application text is a free-text field;
- whether free text is replaced by screening/question modules;
- size, format and field limits;
- whether structured CV fields must be entered separately;
- whether documents are uploaded directly or converted by the platform.

The system therefore needs a vacancy/channel fact model, even if portal text is detached from the core product. The minimum intake concepts are:

```text
channel/platform if known
required employer-facing components
accepted/required file formats
per-file and total size limits if stated
application text mode
portal questions and exact limits
structured CV re-entry requirement
mandatory/supporting attachments
submission deadline and exceptional instructions
```

Unknown facts should remain `UNKNOWN`, not be filled with market convention. The human can confirm channel facts at review/submission time; high-impact limits should be captured earlier where available.

### 2.2 Portal/application text behavior

The corpus supports these constraints:

- Webcruiter often uses a portal free-text application field and may replace it with questions.
- Other systems may accept uploaded letters, plain text, screening questions or combinations.
- Exact field limits may be configured by the employer rather than globally documented.
- FINN applications frequently route to external systems, so “FINN” alone does not define the contract.
- Jobbnorge/Grade and EasyCruit evidence illustrates that format, structured-CV and question behavior differs materially across systems.

**Design consequence:** the core employer argument should be representable independently of document styling. Even when a Word/PDF letter is produced, the semantic content should be recoverable as clean plain text. This supports a detachable portal layer but does not prove it is optimal for the real first batch.

### 2.3 Attachments outside the core package

Norwegian convention and platform evidence suggest that vitnemål, transcripts, attester and references may be requested per vacancy or later in the process. They should not automatically become part of the core CV/application generation pipeline.

The runtime should distinguish:

- generated core documents;
- vacancy-specific required attachments;
- human-supplied credential files;
- items normally held until requested;
- structured portal data entered manually.

The system may report an attachment checklist. It must not fabricate, transform or submit credentials without an explicit separate contract.

### 2.4 Public-sector qualification principle

The represented primary legal/administrative material establishes that, for Norwegian state hiring, advertised qualifications form the basis for comparative assessment and that education, experience and personal suitability are assessed against those requirements.

The architecture consequence is **coverage discipline**:

- preserve each stated minimum and important desired requirement;
- distinguish minimum, desired, task and contextual signals;
- map each to strongest candidate evidence, gap or uncertainty;
- ensure the final package does not omit a decisive requirement merely because another theme is more rhetorically attractive;
- keep a private coverage view for audit/review.

It does **not** follow that the employer-facing letter must contain one paragraph per requirement or read like a compliance matrix. A natural Norwegian argument can cover requirements through a stronger backbone. The private coverage artifact protects completeness while the final writer protects persuasion.

### 2.5 Product-boundary implication

The latest user permits:

- invariant CV + application as the normal core;
- portal detachment;
- Bokmål-only v1;
- separate handling for rare nonconforming jobs.

External evidence makes that simplification plausible, especially if portal questions affect only a minority of jobs and are often structured/short. The missing actual inventory prevents final selection. Step 1 should choose after deriving:

- actual portal prevalence;
- free-text depth;
- any CV-only/portal-only jobs;
- language exceptions;
- attachment constraints;
- whether the same approved package can reliably seed downstream answers.

---

## 3. ATS, parsing and document structure

### 3.1 What the evidence supports

The research does not establish one universal ATS-safe layout. It supports a conservative posture:

- logical reading order;
- normal text for critical content;
- minimal dependence on text boxes, graphics or decorative objects;
- readable standard fonts present on the render machine;
- text-selectable/extractable PDF;
- stable headings and ordinary paragraph structure;
- no essential fact only in an object that may be ignored by a parser;
- empirical extraction and channel tests.

Multi-column layouts, tables and headers/footers are not automatically forbidden. Their risk depends on the parser and use. Critical information should not be available **only** through a fragile structure.

### 3.2 Actual master evidence versus generic caution

The direct P0.7 audit materially narrows the problem:

- CV main body is a linear text flow with no tables, text boxes or drawings;
- CV name/“CV” is in the header;
- application uses two tables and header contact information;
- controls are non-data-bound;
- controls are filled and unwrapped before LibreOffice;
- final validation rejects residual `w:sdt`.

Therefore:

- generic warnings about data-bound controls do not prove the P0.7 technique is defective;
- the header placement of name/contact is a concrete parseability test target;
- application tables should be inspected for reading order and plain-text extraction;
- final outputs should be tested, not inferred from the template source alone.

### 3.3 Minimum parseability spike

For representative sparse, normal and dense fixtures, Step 2 should:

1. generate final DOCX/PDF from the actual adapted masters;
2. extract text from each format with at least one ordinary parser;
3. inspect reading order;
4. verify name/contact/headline/employers/dates/education are present;
5. verify no placeholder/control text remains;
6. visually inspect pages;
7. where practical, upload to the actual target portal or use its preview/parsing flow;
8. record differences rather than claim generic “ATS compliance.”

A failed header test should lead to moving or duplicating critical identity into normal body text, not a wholesale template rewrite unless necessary.

---

## 4. Word, DOCX, PDF and LibreOffice

### 4.1 Content controls

The evidence requires a precise rule:

- **Data-bound SDTs and unresolved conditional controls:** avoid in final masters/output because LibreOffice and `python-docx` behavior can expose placeholder or stale content.
- **Known non-data-bound SDTs used as temporary template anchors:** acceptable only when the implementation fills them deterministically, unwraps them, verifies no controls remain and is tested on the actual masters.
- **Unknown controls:** fail preflight rather than ignore.

This preserves proven P0.7 capital while protecting against the actual failure class.

### 4.2 Rendering transaction

Headless LibreOffice risks represented in the research include:

- profile-lock contention;
- Windows path/URI and quoting problems;
- nonzero returns or missing outputs;
- possible partial success when processing multiple files;
- font substitution;
- metadata/layout differences from Word.

The robust implementation posture is:

```text
one job = operational transaction
one document = independently verified result
isolated LibreOffice profile per invocation
absolute quoted paths
exit/error capture + expected-file checks
no persistent daemon
```

A single invocation for both job documents may be used only after a target-machine smoke proves the failure semantics are observable and reliable. Otherwise the smaller one-document invocation is preferable despite startup cost.

### 4.3 Fonts and Norwegian glyphs

The target machine must have the selected fonts or a deliberate, tested substitute. Verify:

- `æ`, `ø`, `å` and relevant punctuation;
- expected line wrapping/page count;
- font embedding/substitution in PDF where inspectable;
- Word and LibreOffice visual output;
- locale/hyphenation behavior where it changes layout.

Font choice is an environment-backed template decision, not a purely aesthetic spec choice.

### 4.4 DOCX versus PDF

Research and Norwegian convention favor PDF where stable appearance matters, but vacancy rules control. Preserve both when economical:

- DOCX: editable/auditable and useful if explicitly required;
- PDF: stable rendering and common upload format;
- plain text: required for portal fields and useful as a semantic fallback.

The system should not assume a rich Word letter is the exact representation the employer sees.

---

## 5. Model, surface and runtime facts

### 5.1 Volatility rule

Model names, tier availability, effort labels, prices, context limits, upload caps, retention and tool permissions are volatile. The corpus records a 2026 state, including Sol/Terra/Luna availability and prices, but the durable architecture should encode roles and requirements rather than hard-wire dated commercial facts.

Before implementation and each production batch, verify:

- available models and effort settings on the selected surface;
- whether Terra/Luna are selectable there;
- context/upload limits;
- local workspace/command access;
- approval and network permissions;
- retention/privacy controls relevant to candidate files;
- model output/token limits.

### 5.2 Structured output

The represented official distinction is load-bearing:

- API Structured Outputs can constrain decoding to a supplied JSON Schema;
- a manual ChatGPT Work/Codex response is not automatically schema-guaranteed merely because the prompt requests JSON;
- Codex/local tooling may validate and repair the resulting file.

Therefore serialization choice and validation mechanism must be separate:

- Markdown requires semantic/section validation appropriate to its contract;
- JSON requires local parsing and schema validation before completion;
- neither format makes the strategy factually or strategically authoritative;
- malformed output must be visible and repairable.

This evidence does not resolve `strategy.md` versus `strategy.json`; it prevents false confidence in chat-generated JSON.

### 5.3 Same-session validation and repair

The user confirms Work/Desktop and Codex/local terminal/Python are available. External evidence says Codex-style environments can run validators, while ordinary chat cannot be assumed to expose the local sandbox.

The selected stage surface must therefore be tested for:

- repository access;
- command execution;
- reading validator diagnostics;
- editing the artifact;
- re-running validation;
- bounded visible attempts;
- preservation of the original failure record.

If the surface cannot do this, validation becomes a separate operator step. Architecture should not pretend the loop exists universally.

### 5.4 Context window is not effective attention

Advertised context capacity and upload limits do not prove that every source atom is equally available. Document ingestion may use retrieval, and long-context benchmarks show positional degradation. Hence:

- keep job-local contexts focused;
- avoid unnecessary batch history in the semantic turn;
- use stable source navigation rather than a single monolithic summary;
- log sequence position and compare early/middle/late quality;
- reset or split clusters when observed quality declines;
- do not derive a universal jobs-per-chat number from unrelated benchmarks.

---

## 6. Context-system design criteria

### 6.1 Factual substrate

The three candidate authorities and canonical vacancy files remain the non-lossy factual substrate. No context preparation may replace them. A model-generated package, strategy, summary or personality interpretation is not a candidate fact source.

The P0.7 source register also carried a candidate-source maintenance backlog not shown as resolved by later files. Before prominent use, Step 3 should verify the current authority files rather than infer missing detail:

| Area | Unresolved/source-maintenance item | Safe interim ceiling |
|---|---|---|
| Claim index | `CLM-BAR-*` / `CLM-PRJ10-*` owner-file evidence may need pack-level index synchronization without renumbering | Use owner-file evidence; do not treat a lagging global index as absence |
| BAR work | Exact task list, recipient counts, error categories, clinic names, tool-use counts and savings | Use documented operational contribution without unverified scale/savings |
| `PRJ-01` | Exact dashboard name, page/user counts, current status and decommission reason | Use the verified management-BI contribution; avoid unsupported scale/lifecycle specifics |
| `PRJ-02` | Exact report/unit/current status and support scope | Avoid sole ownership or formal-training claims unless sourced |
| `PRJ-03` | Final delivery/current status and actual 2027 use after the historical August 2026 plan | Do not call planned work completed or production-used without updated evidence |
| `PRJ-04` | Exact framework name, approval route, individual contribution split and measured effect | Preserve four-person/team boundary; no personal effect claim without evidence |
| `PRJ-05` | Deployment/performance and language-specific authorship | Do not upgrade repository/development work to proven production or sole authorship |
| `PRJ-06` | Implementation, weights, handover, adoption and realized benefits | Retain transparent proxy/design status unless later authority confirms implementation |
| `PRJ-07` | Platform access/scope and formal governance role | Use pilot/exposure/modernization-mapping language; avoid platform-owner inflation |
| Education | Exact NTNU award date/thesis/specialization/grades; UiA progress/completion; UiB average grade | State only verified degree/study status; omit grades/specialization/progress precision until sourced |

“Current authority file” means the source is the active authority; it does not automatically resolve every historical open field. Any actual current-source content that resolves these questions supersedes this backlog.

The minimal context system should make it easy to answer:

- where is the exact support for this candidate claim?
- what is the claim ceiling?
- which role/employment/project does it belong to?
- what caveat or attribution qualifier applies?
- what requirement does it support?
- can the final writer escape back to the full source?

### 6.2 Deterministic structural index

A lossless deterministic index is a strong candidate because it can provide navigation without semantic authority. Possible entries include:

```text
evidence_id
source_file
heading/path
line or stable anchor
source domain
employment/project/education association
explicit dates/numbers/tool names
short source-preserving descriptor
```

The index should not:

- assign final relevance;
- rewrite the fact into a stronger claim;
- exclude unindexed source text;
- become a new manually maintained truth file;
- require a vector database to function.

It should be generated, reproducible and disposable. Whether it is mandatory baseline architecture remains `STEP1_FREEZE`; its exact utility and authoring cost can be measured during Step 3.

**Historical retrieval experiment to preserve.** The earlier candidate-source work rejected a new global reverse index as duplicative/overprompting. Local `CROSS_REF` metadata was piloted for `PRJ-03`, `PRJ-04` and `PRJ-08`; represented evaluation found no recall improvement and precision fell to `0.789`, so neither that variant nor `BRIDGES_TO` was promoted. An earlier retrieval A/B in the P0.5.3 lineage reported recall/precision `1.000/1.000`, while the extra cross-reference variant reduced precision. This is narrow historical evidence, not proof that every deterministic index is harmful: the P0.9 candidate is a generated structural address layer, not another semantic cross-reference authority. Step 3 should nevertheless require measured marginal value and avoid adding links merely because they are technically easy.

### 6.3 Semantic segmentation

Source documents may benefit from clearer stable sections or evidence atoms. The governing criteria are:

- preserve qualifiers and provenance;
- avoid fragmenting one evidential unit into misleading pieces;
- keep stable IDs across ordinary wording/layout maintenance where practical;
- allow multiple role tags without forcing one ontology;
- prefer human-readable structure that also supports search;
- do not restructure canonical sources solely to satisfy a speculative retrieval stack.

Step 3 may compare improved segmentation against the current source layout. It should not begin by building a graph/vector platform.

### 6.4 Lexical, semantic, vector and graph approaches

The corpus permits evaluation of several retrieval approaches but supports no blanket requirement:

| Approach | Potential value | Main risk/cost | Current treatment |
|---|---|---|---|
| Direct source reading | Maximum fidelity and source escape | Attention cost, positional effects | Required fallback/control |
| Deterministic heading/ID index | Lossless navigation, simple invalidation | May not surface conceptual equivalence | Strong candidate |
| Lexical search | Exact tools/names/numbers and auditability | Vocabulary mismatch | Cheap optional support |
| Model-assisted contextual preparation | Vacancy-conditioned navigation | Anchoring, omission, summary distortion | Bounded experiment only |
| Embeddings/vector search | Conceptual retrieval at scale | Maintenance, false confidence, privacy and overengineering | Deferred until demonstrated need |
| Knowledge graph/GraphRAG | Explicit relationships and multi-hop navigation | Ontology and infrastructure burden | Out of P0.9 baseline; no evidence of marginal value |

The selection criterion is not technical sophistication. It is measured improvement in decisive evidence selection and human/package quality per complexity.

### 6.5 Source escape and observability

Any preparation layer should make recovery cheap:

- include source-linked evidence IDs;
- never hide the full authority files;
- allow Final Sol to search outside prepared material;
- record when decisive evidence was recovered outside preparation;
- distinguish “not selected” from “not present”;
- avoid a relevance tier becoming a claim ceiling.

`evidence_outside_prep` is useful as diagnostic telemetry, but the metric is imperfect: low use can mean excellent preparation or anchoring. Interpret it with paired output review, not as a standalone KPI.

### 6.6 Invalidation

At this scale, a static invalidation matrix is likely sufficient:

| Change | Minimum stale scope |
|---|---|
| Candidate authority changed | Candidate index/context views; all unapproved downstream strategies/packages whose claims may depend on it |
| One vacancy changed | That job’s intake, strategy, draft, final package and rendered outputs |
| Cluster order changed | Run/cluster manifest and sequence metrics; job facts unchanged |
| Strategy changed | Draft/final/review/render for that job |
| Final package changed | Final refs, review and render for that job |
| Template changed | Rendered outputs using that template; semantic packages may remain current |
| Personality/context-prep toggle changed | Only outputs/stages that consume it; factual sources unchanged |

The final architecture should define exact invalidation classes without introducing a runtime dependency graph unless actual complexity demands one.

---

## 7. Personality context

### 7.1 Source status

SRC-16 is a high-signal canonical interpretive profile built from explicit self-report, repeated self-report, observed behavior and bounded inference. It includes:

- cognitive and decision style;
- communication preferences and likely friction;
- motivations and values;
- work/execution patterns;
- failure modes/countermeasures;
- collaboration protocol;
- confidence and interpretation boundaries.

It is not a clinical assessment, psychometric truth or candidate-fact authority.

SRC-17 adapts that source into a proposed P0.9 interface with stable facets (`PF-01`…`PF-20`), confidence/usage tags, anti-inference rules and a distilled handoff. It is a well-developed proposal, not an adopted runtime contract.

The decision-relevant personality signal can be compressed as follows without treating it as employer-facing fact:

| Source facets | Interpretive signal | Potential application use | Misread / expression control |
|---|---|---|---|
| `PF-01`, `PF-12` | Systems mapping, causal decomposition, auditability and source-of-truth orientation | Complex transformation, governance, architecture, strategy, quality and traceability roles | Express only through evidenced work; avoid abstract “systems thinker” self-label without proof |
| `PF-02`, `PF-10`, `PF-18` | Exploratory breadth, rapid learning and exploration contained by engineered convergence | Innovation, ambiguous domains, cross-disciplinary transfer and problem discovery | Prevent generalist blur; choose one vacancy backbone and show closure/delivery evidence |
| `PF-03`, `PF-19` | Reversible action, evidence loops and pro-change experimentation with production guardrails | Pilots, continuous improvement, implementation and learning under uncertainty | Do not imply recklessness or permanent experimentation; distinguish test from production |
| `PF-04`, `PF-11` | Craft/integrity/usefulness standards and leverage/toolmaking orientation | Durable tools, process redesign, automation, operational value and quality | Strength should come from concrete artifacts/outcomes, not perfectionist or visionary rhetoric |
| `PF-05`, `PF-06` | Governance-based control, verified delegation and high autonomy without reflexive opposition | Decision rights, standards, interfaces, leadership without title and responsible autonomy | Do not inflate into personnel authority; show how governance enabled collaboration |
| `PF-07`, `PF-20` | Promotion/expansion motivation and low status/conformity motivation | Credible motivation around capability, usefulness and difficult problems rather than prestige | Avoid claiming disinterest in status or cultural superiority; translate into job-specific motivation |
| `PF-08`, `PF-09` | Cognitive empathy and precision-first, evidence-backed communication | Stakeholder translation, requirements, advisory work and difficult decisions | Prevent cold/combative framing; show receptivity, adaptation and decision usefulness where evidenced |
| `PF-13`, `PF-14` | Assertive ambivert with low appeasement/context-sensitive agreeableness | Independent counsel, challenge, workshops and cross-functional influence | Do not encode personality labels; use concrete collaboration and influence evidence |
| `PF-15`, `PF-16`, `PF-17` | Analysis escalation under stress, scope expansion/continued comparison/novelty decay, and social-temperature risk | Primarily internal misread control and prompt guardrails | Normally not positive employer claims; constrain over-complexity, over-intellectualization and tone |

Two qualifications matter for authenticity: the main closure risk is option/scope expansion and later novelty decay, not simply anxious perfectionism; high standards are primarily craft-, integrity- and usefulness-driven. The profile also describes a preference for governance, observability and credible delegation rather than mandatory hands-on control. These distinctions can change motivation and leadership framing when factual evidence supports them.

For internal model collaboration, the profile supports a direct evidence-first protocol: lead with the decision, distinguish fact/inference/open uncertainty, preserve source authority and auditability, challenge weak framing rather than appease it, make reversible experiments observable, and use explicit stop conditions when option expansion stops adding decision value. Social/receptivity sequencing should still be considered when the objective is stakeholder adoption rather than analytical correction.

### 7.2 Hard boundaries

Personality context may:

- help select among factually supported identity routes;
- identify likely authentic motivations;
- sharpen employer-value framing;
- prevent predictable misreadings;
- guide tone and evidence emphasis;
- expose whether wording performs a generic persona rather than the candidate.

It may not:

- create achievements, responsibilities, skills or results;
- increase a claim ceiling;
- insert typology labels into employer-facing text;
- diagnose the candidate;
- override vacancy/candidate evidence;
- force a trait into every package;
- become a hidden ranking criterion for employers or jobs.

### 7.3 Proposed bounded mechanism

The strongest bounded proposal is:

1. Stage 1 understands the vacancy and factual evidence first.
2. Only then, if enabled, it selects zero to three useful facets.
3. Each facet is tied to factual evidence, desired recruiter interpretation, misread risk and expression ceiling.
4. Terra receives only distilled guidance, not the full profile.
5. Final Sol may retain, reduce, replace or ignore it.
6. `NOT_USEFUL`/zero facets is valid.

This design reduces stereotype and anchoring risk, but its marginal package value is unproven. The only user-locked state is that the feature must be optional/toggleable if implemented. Default and exact interface remain open.

### 7.4 Evaluation

A small paired test can compare personality OFF versus ON while holding vacancy, model, effort and factual context constant. Review should examine:

- authenticity/recognizability;
- employer relevance;
- unsupported inference;
- generic personality prose;
- over-intellectualization or over-complexity;
- motivation specificity;
- human edit time;
- whether week-later judgment remains stable.

Because the user estimates week-later self-rating consistency at about 7/10, results should not be overinterpreted from a single pair. The feature can remain optional after architecture lock if deadlines make prelock testing lower value.

---

## 8. Luna/context-preparation hypothesis

### 8.1 What is established

- Luna is materially cheaper than Sol/Terra in the 2026 evidence.
- The cited OpenAI long-context benchmark shows substantially weaker Luna performance at large context lengths.
- General research establishes anchoring and summary-distortion risks.
- No direct Jobbsøk_26 evidence shows that a Luna preparation pass improves final packages.
- User permits optional model-routing experiments but does not select Luna as baseline.

### 8.2 Safe experimental contract

A Luna pass, if tested, should be:

- job-local or small-context, not global-corpus filtering;
- advisory and source-linked;
- prohibited from drafting final employer prose;
- prohibited from excluding evidence or mutating authorities;
- easy for Sol to ignore;
- fail-open to direct source/index;
- attributable in the run record;
- compared against the strongest practical control: direct source plus any deterministic index.

The wrong comparison is `Luna versus no context`. The useful comparison is:

```text
Control: deterministic/direct-source navigation → Sol
Treatment: same navigation + Luna advisory preparation → Sol
```

Measure final decision quality and evidence recall, not Luna output elegance.

### 8.3 Activation rule

Do not include Luna in baseline correctness. Activate only if:

- the deterministic/direct-source control has a measured attention/retrieval problem;
- the preparation pass can be bounded cheaply;
- the test shows material quality or effort gain without decisive omissions;
- the operational prompt count remains compatible with the 20–25 normal envelope.

---

## 9. Security, trust and privacy

### 9.1 Threat model

Relevant risks are:

- instruction-like or malicious text in vacancy files;
- model output trying to redefine authority or control state;
- path traversal, unsafe filenames, symlinks/reparse points;
- oversized or unsupported files;
- authority-file mutation;
- stale source/context use;
- internal/private information leaking into employer-facing output;
- accidental external network/action permissions;
- candidate-file retention/privacy on model surfaces;
- human over-trust in polished but unsupported output.

### 9.2 Minimum architecture

Use a control/data-plane boundary:

```text
CONTROL PLANE
system/stage instructions
source authority definitions
run manifest and expected set
validator policy
permissions
submission boundary

DATA PLANE
vacancies
candidate/context/personality content
strategy/draft/final outputs
context preparation
research/reference material
```

Data-plane content may inform semantic work. It may not change permissions, authority, expected jobs, validators, submission rights or system instructions.

### 9.3 Defense in depth

Appropriate controls include:

- least-privilege workspace access;
- network disabled unless explicitly required;
- human approval for irreversible/external actions;
- protected authority directories or hash checks;
- deterministic path/file validation;
- unsupported/oversized input rejection;
- private-token/source-ID leakage scans;
- schema/contract validation;
- visible model instructions that vacancy content is untrusted data;
- adversarial fixtures;
- audit logs and rollback.

Regex/instruction scans may flag risk but are not a security guarantee. No “prompt-injection solved” claim should appear in the release evidence.

### 9.4 Privacy

The corpus records general no-training/retention distinctions for business/enterprise/API surfaces as of 2026. These are volatile. Before production, verify the selected account/surface and local policy. Minimize uploads to the sources needed for the stage, and avoid placing unnecessary personal data in logs or generated reports.

---

## 10. Evaluation and pilot design

### 10.1 Why a new baseline is required

The user explicitly states that historical applications and interview-conversion rates are too old or incomparable to the intended P0.9 vacancy set. Therefore:

- do not use them as calibrated quality anchors;
- do not claim P0.9 uplift against them;
- use the first batch to establish a new baseline;
- preserve user feedback and edits as evaluation evidence without silently converting approved prose into candidate truth.

### 10.2 Evaluation layers

#### Layer 1 — engineering correctness

Before model comparisons:

- valid state/artifacts;
- identity isolation;
- source protection;
- merge correctness;
- final refs;
- partial success;
- targeted rerun/render;
- document integrity;
- security boundary.

Failure here invalidates product comparisons because the outputs are not trustworthy.

#### Layer 2 — baseline product observation

Run the simplest frozen baseline on representative real jobs and record:

- overall package quality;
- employer/role specificity;
- truth and attribution defects;
- evidence choice;
- CV positioning;
- application argument and complementarity;
- natural Bokmål;
- final status;
- review/edit minutes;
- total human minutes through submission;
- stage/chat/order position;
- mechanical failures;
- package ultimately submitted or dropped.

This establishes whether the system delivers the target strong majority.

#### Layer 3 — causal feature tests

Only then compare uncertain mechanisms:

- strategy Markdown versus JSON/structured form;
- direct/index context versus index + Luna;
- personality OFF versus ON;
- cluster order or size;
- model/effort routing;
- Priority treatment if retained.

Each test should change one material variable where practical.

### 10.3 Primary and guardrail metrics

The architecture’s product metric remains:

```text
Q_happy = (median(package_quality) + mean(top_80_percent(package_quality))) / 2
```

For small `n`, report the raw ordered scores and sensitivity rather than pretending the top-80 discretization is precise. P0.8.1’s recommended `n=8` primary view excludes two jobs (`top 6`) and reports sensitivity against excluding one and excluding none. This is a strong measurement convention, not a universal statistical truth.

Also report:

- count/share `READY`, `CHECK`, `RERUN`;
- `TailRecall20`: how often Stage 3's triage includes the human-judged weak tail, explicitly interpreted as self-triage calibration rather than independent QA recall;
- `ReviewLoad`: how much of the batch is escalated, because high tail recall is trivial if almost everything is flagged;
- truth/attribution violations: target zero;
- median and distribution of total human minutes per submitted package;
- number of packages submitted/dropped;
- mechanical completion/failure rate;
- source-escape use where context preparation is tested;
- quality by cluster position, with early/late comparisons treated as descriptive at small `n`;
- optional feature on/off comparison;
- prompt/run cost as secondary diagnostic.

Model cost should be logged at the unit where it actually arises: model/surface/effort and input/output/total credits per stage chat or run. Do not fabricate precise per-job credit allocation for a shared cluster chat. Derived metrics may report cluster/run cost per `READY` or submitted package, with the allocation method stated.

The user’s practical success target is roughly 30 strong packages from about 40, not uniform rescue of every job.

### 10.4 Quality rubric

A human rubric should cover a small number of separable dimensions, for example:

| Dimension | Question |
|---|---|
| Truth/defensibility | Is every material factual implication supported and interview-defensible? |
| Employer specificity | Could this package plausibly fit another employer after noun replacement? |
| Backbone/positioning | Is there one clear candidate identity tied to the employer’s decision problem? |
| Evidence selection | Are the strongest and most relevant facts used without crowding or omission? |
| CV quality | Does the headline/profile/bullet set materially improve fit while preserving chronology? |
| Application quality | Does the letter add motivation, interpretation and argument rather than duplicate the CV? |
| Norwegian language | Is the Bokmål natural, precise, restrained and free of translated/corporate clichés? |
| Channel usability | Does the deliverable fit the vacancy’s actual format/limit requirements? |
| Human effort | How many minutes were required to trust, edit and submit it? |

Truth should be a hard guardrail, not averaged away by persuasive strength.

### 10.5 Review states as operational outcome

Use repair scope rather than a hidden scalar threshold:

- `READY`: no known material factual/semantic/channel defect; only ordinary approval/submission.
- `CHECK`: bounded confirmation or local edit, expected within the 10–20-minute total human envelope.
- `RERUN`: coherent strategic rewrite or evidence reselection is required.

A status should include a concise reason and recommended action. It should not become an immutable label: human review may change it.

### 10.6 Experiment discipline

The user allows approximately three to four small, high-decision-value prearchitecture tests, but deadlines under two weeks mean not all should run before freeze. Prioritize tests where the wrong choice is expensive to reverse:

1. actual vacancy/channel inventory;
2. target master/render spike;
3. runtime/state/validator vertical slice or strategy-format spike if serialization changes build structure;
4. optional personality/Luna tests only when they would change baseline architecture rather than remain easy toggles.

For each experiment record:

- hypothesis and decision it can change;
- control/treatment;
- jobs selected and why;
- model/surface/effort;
- frozen sources;
- raw outputs;
- human scores and edit time;
- mechanical defects;
- interpretation and uncertainty;
- resulting decision, non-decision or follow-up.

Blinding preference remains unresolved; do not claim a blinded design without user clarification. Where practical, randomized order and delayed labels can reduce anchoring, but operational simplicity may outweigh formal blinding in a tiny pilot.

### 10.7 Stop rules

Stop architecture experimentation and proceed to baseline build when:

- product/state/serialization choices that materially change the repository are resolved;
- target rendering risk has a safe implementation path;
- reversible quality enhancers can remain optional;
- remaining empirical uncertainty has explicit pilot metrics;
- no experiment is likely to alter a costly structural decision before current deadlines.

Stop adding context machinery when the marginal test shows no meaningful gain in evidence selection, package quality or human time. Do not use technical novelty as evidence of need.

---

## 11. What remains externally uncertain

The following should not be represented as settled facts:

- the exact 2026 model names, prices, context/upload caps and surface availability at the future implementation/run date;
- how the selected Work/Desktop/Codex surface will ingest every attached file in practice;
- optimal jobs per cluster;
- which model/effort route maximizes package quality;
- the actual first-batch platform and language distribution;
- how each target ATS parses the adapted masters;
- whether one LibreOffice invocation for both documents is reliable on the target machine;
- whether deterministic indexing improves final evidence selection enough to justify core status;
- whether Luna preparation adds value;
- whether personality context adds value and what its default should be;
- whether strategy JSON or Markdown produces fewer total failures and better final packages;
- whether historical outcome proxies can ever become comparable after more data.

The final architecture should either assign these to `STEP2_VERIFY`/`STEP3_EXPERIMENT` or choose a safe reversible interim rule. It should not settle them by confidence in a research narrative.

---

## 12. Evidence-based design posture

The evidence supports a restrained but high-quality system:

1. preserve full candidate/vacancy authorities;
2. make requirements and evidence addressable;
3. keep preliminary interpretations revisable;
4. use deterministic validation for mechanics;
5. keep one job as the failure/delivery unit;
6. treat channel facts and rendering behavior as empirical;
7. use actual masters before generic redesign;
8. avoid lossy context authority and destructive filtering;
9. keep personality/Luna/retrieval sophistication optional until comparative value is shown;
10. evaluate package quality and total human effort on real vacancies;
11. retain human authority over truth, final approval and submission.

This posture preserves the evidence needed for Step 3 to choose among semantic segmentation, stable evidence IDs, relevance maps, lexical/semantic search, vector or graph approaches—without promoting any of them beyond their demonstrated marginal value.
