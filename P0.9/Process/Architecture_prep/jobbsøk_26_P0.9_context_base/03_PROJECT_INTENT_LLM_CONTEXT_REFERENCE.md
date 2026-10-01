---
document: Jobbsok_26_LLM_Context_Reference
purpose: canonical compact LLM context for architecture/design decisions
status: authoritative_intent_profile
language: nb-NO
scope: final framework goals, priorities, constraints, preferences, optimization target, architecture heuristics
---

# CORE_OBJECTIVE
Build the simplest Codex-native, file-based, manually controlled system that converts human-approved Norwegian vacancies + authoritative candidate truth into complete, highly vacancy-specific Norwegian application packages with maximum interview probability and minimum human rewriting. Primary product = employer-facing package, not analysis/state/QA artefacts.

# PRIMARY_UTILITY
Optimize distribution, not uniformity:

`Q_happy = f(median(package_quality), mean(top_80_percent(package_quality)))`

Operational intent:
- maximize median package quality;
- maximize average quality among strongest ~80%;
- accept that weakest ~20% may require separate rerun outside main framework;
- never weaken strong packages to improve batch uniformity;
- do not spend disproportionate model/engineering effort rescuing low-upside tail cases;
- identify tail cheaply via READY/CHECK/RERUN rather than eliminating it with heavy QA;
- success can mean ~75-85% top-quality packages if this removes most manual workload.

# SECONDARY_OBJECTIVES_ORDER
1. interview probability / Norwegian employer relevance;
2. decisive evidence selection + strategic framing;
3. natural, precise, persuasive Bokmål;
4. complete materially tailored CV;
5. complementary application + portal content;
6. low human rewrite minutes per submit-ready package;
7. simple, understandable, stable operator flow;
8. cheap mechanical controls directly protecting usable output;
9. credit efficiency;
10. all else.

# COST_HIERARCHY
`Human Effort > Human Complexity > LLM Complexity > LLM Effort`

Interpretation:
- bounded human final review is acceptable;
- extensive human rewriting = system failure;
- operator complexity is costly even if technically robust;
- semantic work belongs to models, not code;
- deterministic code handles mechanics only;
- Sol/Terra credits are cheap relative to human reconstruction;
- model downgrades are valid only if Q_happy and review time are preserved.

# NORTH_STAR
Protect truth hard. Maximize persuasion aggressively. Optimize median + strong majority. Flag weak tail cheaply. Do not build more system than the final package deserves.

# TRUTH_AUTHORITY
Authoritative candidate domains:
- Work_experience.md = work/project/responsibility/method/tool/contribution facts;
- Education.md = education/course/degree facts;
- Other_high_value_information.md = identity/contact/supporting facts;
- CV_BASELINE.md = derived stable CV rendering baseline, never supersedes authorities;
- vacancy = employer/role/requirement/channel facts only;
- language/application/market/persuasion files = advisory; may shape strategy/wording, never create candidate facts.

Hard prohibitions:
- no invented employer/title/dates/degree/institution/contact/result/metric/personnel responsibility/formal mandate/project lifecycle/production status;
- no silent upgrades from contribution to ownership, pilot to production, team result to personal result;
- no candidate-fact mutation by production models;
- no internal IDs/private flags in employer-facing text.

Persuasive freedom within truth:
- choose strongest accurate identity;
- use functional equivalence;
- expose documented functional leadership;
- emphasize scope/complexity/judgment/implementation/operational value;
- make sector transfer explicit;
- use strong verbs;
- formulate controlled future contribution;
- test = interview-defensible from authoritative sources.

# PERSUASION_POSTURE
Target voice:
`high clarity about work/responsibility + low self-aggrandizement + strong employer relevance + calm professional weight`

Strong on:
- actor/action;
- personal contribution;
- responsibility;
- scope;
- complexity;
- method;
- judgment;
- implementation;
- adoption/operational use;
- decision value.

Restrained on:
- self-ranking;
- superlatives;
- status signaling;
- identity inflation;
- theatrical confidence;
- performed enthusiasm;
- imported management language.

Jante calibration:
- correct = strong work language + sober self-evaluation;
- wrong = weak verbs + excessive caveats;
- wrong = strong self-praise + weak proof;
- move strength from adjectives to work, responsibility, scope, consequence.

Jeg/vi:
- `jeg` for supported personal contribution;
- `vi` for collective delivery;
- combine when both true;
- do not hide personal responsibility in vague `vi`;
- do not appropriate entire team output.

# NORWEGIAN_LANGUAGE
Generate directly in Bokmål, never translate from English rhetoric.
Use:
- normal Norwegian word order;
- explicit actor + finite verb;
- precise action verbs;
- short/moderate paragraphs;
- varied sentence length;
- dense but readable prose;
- exact technical product names inside ordinary Norwegian prose.
Avoid/review:
- brenner for;
- lidenskapelig opptatt av;
- unik mulighet;
- spennende reise;
- fremoverlent;
- resultatorientert;
- dynamisk;
- synergieffekter;
- game changer;
- revolusjonerende;
- sømløst;
- banebrytende;
- utnytte kraften i;
- jeg er overbevist om at;
- generic i skjæringspunktet mellom;
- unsupported ledet/significant gains;
- adjective triplets;
- noun-heavy bureaucracy;
- passive responsibility hiding;
- American corporate hype.

# SINGLE_BACKBONE
Every package must have exactly one dominant backbone:
`[primary candidate identity] + [dominant employer decision problem] + [two strongest complementary evidence bridges] + [optional controlled differentiator]`

Rules:
- same primary route across CV/application/portal unless channel function requires narrowing;
- breadth supports, never competes with, primary identity;
- if BI/AI/process/forecasting/economics/digitalization compete, choose route best explaining employer problem + strongest evidence;
- cut content that does not strengthen backbone, satisfy a hard screening need, or reduce hiring uncertainty;
- top CV zone + first application paragraph must expose same identity and proof logic;
- avoid Frankenstein profile / generalist blur.

# STRATEGIC_ASYMMETRY
Application = decision-shaping argument, not requirements checklist.
Default rhetorical allocation:
- ~70-85% of meaningful application content on top 1-2 employer pain points + top 2 evidence bridges;
- ~15-30% on motivation, framing, controlled future contribution, closing.

Rules:
- unequal evidence must not receive equal rhetorical weight;
- CV carries breadth/screening coverage;
- application concentrates argument;
- portal answers exact question directly;
- avoid paragraph order mirroring advertisement;
- avoid project catalogue and tool inventory.

# FRAMING_MATRIX
Internal transformation for each selected fact:
`raw fact -> employer latent need/risk -> strategic employer-value angle -> channel role -> natural Norwegian sentence`

Possible employer needs/risks:
- understands actual problem, not only requested artefact;
- delivers under operational/compatibility constraints;
- makes solution usable/understood/maintainable;
- creates trust via traceability/control/boundaries;
- prioritizes critical work over technical decoration;
- reduces ambiguity/manual handoffs/fragility;
- connects analysis to decisions/action.

Do not expose matrix mechanically. Avoid repetitive “Dette er relevant fordi”, identical problem-action-result formulas, dramatic fear language, formula prose.

# MOTIVATION
Motivation must be reasoned, not performed.
Anchor in:
- concrete task;
- employer problem;
- professional/social responsibility;
- credible link to candidate experience;
- controlled future contribution.

Avoid:
- generic employer praise;
- copied values;
- prestige motivation;
- vague industry interest;
- empty enthusiasm.

# CHANNEL_ROLES
CV:
- complete, factual, chronological, scannable;
- normally 1-2 pages;
- dynamic top zone materially tailored;
- explicit professional headline;
- profile + competencies + selected employment bullet overrides;
- stable contact/employer/title/dates/education/languages/support sections from baseline;
- evidence shows contribution, responsibility, method, scope, use.

Application:
- direct employer-specific opening;
- establish identity/backbone early;
- 2-3 connected evidence examples;
- explain employer problem + relevance + motivation;
- complement CV, not retell chronology;
- normally ~1 A4 page;
- at least one interview hook.

Portal:
- answer exact question;
- direct answer first;
- obey exact word/character limits;
- use 1-2 strongest proofs;
- do not paste miniature generic application.

# PRODUCTION_POLICY
- every human-approved job = PRODUCE;
- no semantic GO/NO-GO after approval;
- stretch/title mismatch/sector transfer/nontraditional profile/missing formal leadership title/functionally equivalent experience => reframe or flag, never veto;
- final semantic model = constructive editor/final writer, not PASS/REVISE/BLOCK judge;
- package always delivered if mechanically/factually usable.

# SELECTIVE_REVIEW
Private triage only:
- READY = expected submit-ready after rapid review;
- CHECK = likely strong, one/few bounded issues;
- RERUN = complete/useful but strategy/text should receive separate targeted round.

Rules:
- max 3 concise reasons;
- no numeric quality score;
- no long self-critique;
- no automatic rerun;
- RERUN does not block rendering;
- prioritize tail identification, not tail elimination.

Metrics:
- Q_happy;
- submit-ready share;
- human edit minutes per ready package;
- TailRecall20;
- ReviewLoad;
- credits per ready package.

# QA_POLICY
Hard per-job failures only when output objectively unusable:
- invalid/unreadable source or JSON;
- wrong employer/title/job identity;
- unknown employment ID;
- baseline merge failure;
- missing required channel;
- hard portal limit violation;
- unsupported formal fact;
- internal/private leakage;
- broken/unopenable rendering;
- lost static CV history.

Soft review, not discard:
- CV >2 pages;
- application >1 page;
- genericity risk;
- extensive final rewrite;
- strategy change;
- alternate valid evidence route;
- similarity with another package;
- weak motivation;
- missing status metadata;
- incomplete batch.

Batch behavior:
- partial success mandatory;
- render/preserve all usable jobs;
- per-job statuses: DELIVERED_READY / DELIVERED_CHECK / DELIVERED_RERUN / FAILED;
- nonzero batch exit may coexist with preserved successful output.

# HUMAN_ROLE
Vegard = final semantic authority, fact validator, claim-strength validator, submission decision-maker.
Vegard should primarily:
- skim READY;
- inspect bounded CHECK reasons;
- route RERUN to separate revision;
- make local strength/fact adjustments.

Vegard should not routinely:
- invent candidate identity;
- replace main evidence;
- rebuild strategy;
- rewrite full application;
- reconstruct CV.

No automated submission, employer contact, publication, or external profile modification.

# ARCHITECTURE_PREFERENCES
Preferred operating model:
- Codex/ChatGPT Work native;
- local file-based repository;
- manually started, cognitively distinct model chats;
- no OpenAI Python API orchestrator;
- no hidden retries;
- no autonomous external action;
- short root instructions + narrow stage instructions;
- model writes semantic artefacts directly to files;
- deterministic scripts only for ingest/finalize/render/limits/identity/baseline merge;
- artefact presence + minimal status sufficient for recovery;
- one job completed and persisted before next job;
- clusters share evidence/policy, never finished prose.

# CURRENT_BEST_TARGET_ARCHITECTURE_HYPOTHESIS
Not yet empirically locked; strongest current direction:

Stage 1: Decision Architecture
- model: GPT-5.6 Sol Max;
- cluster: ~8-10 strategically coherent jobs, normal upper limit ~12;
- internal Phase A: candidate-blind employer/hiring analysis;
- internal Phase B: candidate-aware retrieval, identity, evidence, blueprint, compute class;
- outputs per job: job_identity.json + blueprint.md;
- cluster output: short cluster_strategy.md + prioritized job order;
- classify PRIME / STANDARD / MANUAL_LATER, never GO/NO-GO.

Stage 2: Native Package Writer
- model: GPT-5.6 Terra Max for first pilot; XHigh only if real evals preserve Q_happy/review time;
- process PRIME first, then STANDARD, then MANUAL_LATER;
- write complete package JSON: headline, profile, competencies, employment overrides, application, portal answers;
- Phase A complete draft;
- Phase B quality self-edit focused on identity, opening, evidence complementarity, specificity, motivation, Norwegian naturalness, interview hook;
- short mechanical check last;
- PRIME may internally generate/compare multiple headline/opening variants but output only winner.

Stage 3: Final Writer + Selective Review
- model: GPT-5.6 Sol Max for first pilot; test XHigh later;
- independent end-state view before reading draft;
- full authority to change identity/headline/evidence/channel structure within truth boundaries;
- blueprint = strong hypothesis, not constraint against improvement;
- output final_package.json + review.json;
- READY/CHECK/RERUN.

Deterministic layer:
- ingest.py;
- finalize.py;
- no advance/split script if same cluster persists through all stages;
- finalize supports per-job rerender, partial success, baseline merge, DOCX/PDF from original masters.

# MODEL_ROUTING_HEURISTIC
Sol:
- employer psychology;
- non-linear strategy;
- evidence prioritization;
- candidate identity;
- reframing;
- final persuasive editing.

Terra:
- output-heavy full-package drafting;
- natural Norwegian production from strong blueprint;
- large text volume;
- internal self-edit.

Luna:
- deferred; only introduce if measured end-to-end value exists;
- never insert cheap pass that requires later repair.

Compute allocation:
- route by expected marginal quality gain, not difficulty alone;
- PRIME/high-upside roles may receive Max effort;
- MANUAL_LATER gets complete standard pass, not endless automatic rescue;
- credits secondary to review time and package quality.

# CLUSTER_POLICY
- target ~4 coherent clusters for ~40 jobs;
- ~8-10 jobs typical; <=12 normal upper bound;
- split if identity/evidence/selection regime/tone diverge;
- cluster sizes need not be equal;
- same cluster follows strategy -> write -> final;
- process one job at a time;
- prioritize PRIME/high-value jobs early;
- no macro/minicluster hierarchy unless pilot proves necessary;
- no reuse of finished application prose.

# OPERATOR_FLOW
Desired:
`add vacancies -> ingest -> run one standard prompt per cluster/stage -> next stage reads prior files directly -> finalize all usable jobs -> review READY/CHECK/RERUN -> rerun/rerender selected job only`

Operator requirements:
- few prompt templates;
- explicit model/effort choice;
- obvious working directory/input/output;
- no complex state interpretation;
- simple recovery;
- per-job rerender;
- visible mechanical errors;
- short chat completions.

# IMPLEMENTATION_RULES
When building:
- deliver real repository files/code/prompts/templates/tests/packaged release;
- do not substitute architecture report or pseudocode;
- inventory first but do not stall in analysis;
- preserve working code/assets; patch surgically;
- retain professional original Word masters;
- never fabricate missing originals;
- candidate authorities remain read-only/byte-preserved unless explicitly updated by user;
- test compile/import/schema/ingest/finalize/rendering;
- visually inspect actual pages;
- distinguish PASS/FAIL/BLOCKED/NOT RUN honestly;
- do not claim implemented/tested/production-ready without evidence.

# DEFERRED_OR_REJECTED
Do not build without measured need:
- vector database;
- embeddings retrieval/QA;
- archetype memory;
- semantic cache;
- outcome learning/self-modifying policies;
- multi-agent/subagent/custom-agent systems;
- agent debate;
- automatic model router;
- full-package best-of-N;
- semantic auto-repair loops;
- SQLite/state machine/event sourcing;
- provenance platform;
- large similarity engine;
- automatic employer research by default;
- automatic submission;
- numeric fit probability;
- generalized release-governance platform;
- edge-case optimization not improving median/top-80 output.

# SUCCESS_CRITERIA
Strategy:
- one identity;
- one dominant employer problem;
- two complementary main proofs;
- evidence ranked by hiring-decision value;
- breadth subordinate;
- credible motivation;
- interview hook.

CV:
- complete chronology;
- strong explicit headline;
- materially tailored top zone;
- 1-2 page natural flow preferred;
- contributions/responsibility/method/use visible;
- no static-data loss.

Application:
- employer-specific from opening;
- argument-led, not checklist-led;
- calm professional authority;
- strong claims without self-ranking;
- natural Bokmål;
- complementary to CV;
- roughly one page preferred.

Portal:
- exact answer;
- direct-first;
- within limits;
- no generic mini-letter.

Human outcome:
- most packages READY or local-edit only;
- typical edit time target after calibration ~<10 minutes;
- no new identity/evidence/full rewrite/CV reconstruction for happy-path majority.

# TIE_BREAKERS
When goals conflict:
1. preserve truth;
2. preserve employer relevance + selected backbone;
3. choose strongest natural persuasive Norwegian wording;
4. maximize Q_happy and reduce human reconstruction;
5. preserve complete usable package;
6. prefer simple operator flow;
7. prefer cheaper model/less QA only if above remain unchanged;
8. discard internal symmetry, process purity, uniformity, and technical elegance before sacrificing final package quality.

# GOLDEN_BALANCE
- truth vs persuasion: maximum interview-defensible strength;
- confidence vs Jante: strong action language, sober self-evaluation;
- breadth vs clarity: one identity + two proofs, breadth as support;
- coverage vs argument: CV covers, application persuades;
- quality vs uniformity: maximize median/top-80, flag tail;
- QA vs freedom: hard facts/mechanics, soft semantic flags;
- automation vs control: automate mechanics, retain human submission authority;
- compute vs cost: strong model where marginal quality gain is high;
- clustering vs specificity: shared evidence, independent prose;
- stages vs friction: minimum distinct stages that improve text;
- page limits vs value: strong preference, not reason to discard otherwise usable package;
- strategy lock vs final quality: strong blueprint, free final writer inside truth;
- complexity vs robustness: simply robust MVP, not enterprise platform.
