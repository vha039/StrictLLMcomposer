# P0.9 control-package finalization notes

Compact record of what changed and why. The package itself is the product; this file exists so the
changes are auditable and so a later agent does not re-derive a closed decision.

## Verdict

The draft package was strong: property-based Desired Final State, proof-based Definition of Done,
plan explicitly subordinate to both, durable ledger, correct `GO_FOR_TWO_JOB_SMOKE` boundary. It did
**not** need restructuring. It needed a visible strictness layer, adjudication of the ten open remedy
disputes, duplication removal, and path repair after the repository reorganization.

Kept: six-document topology, single-owner discipline, all `DFS-*` and `DOD-*` IDs, phase order `P0`–`P8`,
the DEFER set.

## Material package changes

| Change | Why |
|---|---|
| **Normative-force key** (`[HARD]` / `[RULE]` / `[ROUTE]` / `[GUIDE]` / `[OPTION]` / `[EVIDENCE]`) added to `00_READ_FIRST.md` §2 and applied across the package | The commissioning brief's mandatory deliverable. Previously strictness had to be inferred from prose, so every sentence read as equally binding — the condition that produces both scripture-following and silent scope invention. |
| **`D-01`…`D-10` adjudicated decisions** added to `FINAL_EXECUTION_PLAN.md` §2.5 | The ten disputes were open. Leaving them open would have spent Sol's first hours re-deriving evidence already gathered, and risked the wrong call on the revision strategy. |
| **`AR-*` anti-regression register** now has IDs and a single owner (`GUIDANCE` §10); `DOD-23` audits by ID instead of restating | The list previously appeared three times in three wordings. Added `AR-16`…`AR-20` (OOXML serialization safety, post-freeze inbox isolation, warning-channel integrity, freeze reconciliation gate, automation-process ownership). Reframed as **properties**, so no library or technique is banned by name. |
| **State register** added at the head of `EXECUTION_LEDGER.md` with `GOAL / SCOPE / PHASE / PROGRESS / FACTS / REJECTED / NEXT / STOP / RULE`; update cadence changed from "continuously" to "at stable conclusions" | Directly from the documented Codex compaction failure mode (below). `REJECTED` is the field that prevents re-litigating closed decisions after a bad resume. |
| **Path repair** throughout | `P0.9/Finalization_Review/` and `Architecture/Process/` no longer exist. The commissioning brief itself says `Architecture_stage/` where the directory is `Architecture_prep/`. The evidence register had no path at all in the drafts. |
| **`FINAL_GOAL_COMMAND.md`** added to the package | Keeps the launched objective recoverable from the repository rather than only from the terminal. |
| **`goal_prep/Proposed_AGENTS.md` removed** | Two competing root-`AGENTS.md` candidates with stale paths is exactly the hazard the brief warns about. Superseded by `Opus_Handoff/PROPOSED_ROOT_AGENTS.md`. |

## Research findings that changed the design

| Finding | Source | Effect |
|---|---|---|
| Long-running sessions can resume at the **wrong semantic point** after compaction, repeating finished analysis; the community fix is a *small* authoritative state register updated only at stable conclusions, with an explicit `REJECTED` field | [codex#25900](https://github.com/openai/codex/issues/25900) | Ledger restructured around a ≤25-line register; cadence rule rewritten. |
| A strong goal has six parts — outcome, verification surface, constraints, boundaries, iteration policy, blocked stop condition — and completion must be **evidence-checked, not believed** | [OpenAI cookbook: Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) | The Goal command was rewritten to that shape. Each of the six parts is present exactly once. |
| `/goal` objectives cap at **4 000 characters**; longer ones are materialized into an attachment file | [codex#21477](https://github.com/openai/codex/issues/21477), [codex#27508](https://github.com/openai/codex/pull/27508) | Objective held to 2 761 characters and made to point at the package rather than restate it. |
| The runtime may start **hidden continuation turns when the thread is idle** | Codex `/goal` documentation | Stop conditions had to live inside the objective text, not only in the guidance file — a continuation turn has no operator present. Hence the deliberate, single restatement in the Goal. |
| Leaner system prompts improved evaluation scores ~10–15% while cutting tokens 41–66%; state each directive **once**; keep policies in **one place** | [OpenAI GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Justified the single-owner audit and the duplication removals rather than "more thorough" documents. |
| `max` is for work forming **one unbroken chain of reasoning**; `xhigh` for routine bounded work; OpenAI advises testing one level *lower* when migrating to GPT-5.6 | [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model) | **Recommendation: xhigh, not max.** This task is nine bounded phases with explicit acceptance criteria — deliberately splittable, which is the stated signal *against* max. Max also increases exploration, which is the wrong pressure on a task whose main risk is scope creep. |
| `AGENTS.md` is truncated past 32 KiB; shorter files are followed more reliably; nearest file wins and the whole root-to-cwd chain is combined | AGENTS.md field guides, 2026 | Root file kept as a ~120-line map; the roadmap carries task detail. |
| The two documented goal-mode failure modes are **scope creep** and **unprovable completion** | Codex goal-mode practitioner reports | Validated the two structural defences already in the drafts: the scope-admission rule and the property-based DoD. Both were promoted to `[HARD]`. |

## Remedy adjudications that changed a prior recommendation

- **`D-03` review/render orthogonality** — resolved from the frozen text rather than by amendment.
  Spec §16.2 `DEC-21` step 1 already requires the finalizer to validate the current final **and review**;
  Spec §7.2 already omits review from render binding. `render.py` has zero references to review, so the
  precondition is unimplemented, not undecided. This removes one proposed amendment.
- **`D-07` Word cleanup** — **reverses my own earlier meta-review suggestion.** I had argued that
  before/after PID differencing was "ownership-proven by construction". It is not: it is a heuristic that
  misattributes under concurrent Word activity. Truthful diagnostics are `[HARD]`; automatic termination
  is `[OPTION]` and only on real ownership proof. Killing nothing is an acceptable outcome.
- **`D-08` OOXML** — **reverses my earlier `AR-16` wording**, which named `lxml`/`python-docx`. The brief
  is right that a library ban is not architecture. The register now protects the serialization property.
- **Generic "every helper needs a caller" test** — my earlier proposal; the draft guidance already
  rejected it as coverage aesthetics, and I agree on re-reading. `DOD-21` proves the specific
  contract-critical wiring instead. The draft's position was better than mine.
- **`D-01` revision strategy** — rejects the original Codex plan's blanket `0.9.1` bump. Verified that
  `map_version` and `index_version` are artifact-format fields, that `manifest.schema.json` pins
  `spec_revision`/`schema_revision` as `const`, and that a live bump before Phase 1 would invalidate every
  existing frozen run. The Phase-1-before-revision sequencing constraint is new and is `[HARD]`.
- **`D-09` semantic-hash neutrality** — the consumer inventory is now done (three intra-run production
  consumers, all listed), so Sol inherits the evidence but still owes the empirical
  wrong-run-rejection proof before adopting. Left `[OPTION]` deliberately.

## Genuine user-owned decisions still open

1. **Install the root `AGENTS.md` replacement?** The active root file points at
   `P0.9/Finalization_Review/` and `Architecture/Process/`, neither of which exists. A fresh Sol will
   follow a dead pointer on its first move. The corrected candidate is
   `Opus_Handoff/PROPOSED_ROOT_AGENTS.md`; it was **not** installed, per the brief. This is the one
   change I would make before launching.
2. **`GATE-10` account facts** — which surfaces satisfy `SOL_CLASS`/`TERRA_CLASS`, and the account's
   file-access and retention posture. Not inferable from the repository. `DOD-19` will otherwise stop at
   `BLOCKED_USER`, which is a legitimate terminal state but blocks the real smoke rather than this Goal.

## Verified untouched by this pass

`P0.9/Build/` (all hashes unchanged, no file modified), the four frozen files in `P0.9/Architecture/`,
`P0.9/Process/Architecture_prep/`, `P0.9/Process/plan_prep/`, and the active root `AGENTS.md`.
