D01 — SHOULD — Preserve late editorial judgment; delete the substring-edit language

- **Plan:** Design; Phases 2/4/6: binding brief, closed Stage-2 evidence set, substring ops, 50% keystone deletion rule, ~35% rewrite → RERUN.
- **Repo:** `runtime/jobbsok/merge.py::effective_cv` already supports complete replacement of dynamic fields and employment bullet arrays. `policy/stages/stage3_final_writer_review.md::Sequence` separates substantive reconstruction from subsequent content-locked polish.
- **Delta:** Make the brief a strong default; keep factual ceilings binding. Let Advocates/Editors retrieve additional frozen cards and declare the refs actually used. Return replacements for changed scalar fields, paragraph/competency arrays and employment-keyed bullet arrays; omission inherits, an empty permitted array clears. Delete substring matching, tolerant matching, punctuation repair and rewrite-percentage routing. Preserve keystone *argument functions* through editorial judgment, not character overlap. RERUN only when upstream reconsideration is actually cheaper/better.
- **Why:** A restrictive brief recreates draft anchoring. `replace` can erase a keystone while passing the proposed delete-only check; lexical protection neither preserves meaning nor permits efficient restructuring. Field replacement reduces implementation and quoting overhead without requiring complete-package re-emission.
- **Confidence:** H on mechanism; M on quality advantage. **Value:** H.

D02 — MUST — Bind to inputs actually read, including across branches

- **Plan:** Phase 1 deletes `verify_handoff` and `CONTENT_GOVERNING`; binds only artifact inputs/playbook; branches copy earlier stages and re-stamp. Phase 3 reuses fixed return directories.
- **Repo:** `artifacts.py::verify_handoff` compares the issued context with current inputs before stamping. `branch.py::branch` freezes **current working-tree inputs**; `_same_governing_inputs` prevents inappropriate reuse. `evidence_index.py::build_index` generates ordinal/heading IDs: changed body text can retain the same ID.
- **Delta:** Replace the envelope with one context fingerprint covering run/job/stage, consumed frozen inputs and upstream artifacts. Emit it in the submit command and namespace in-progress returns by it; compare before stamping. Include factual sources/index/baseline and consumed policy in reuse identity. Prefer branches inheriting the parent's snapshot; if branches refresh inputs, reuse only artifacts whose consumed-input fingerprints still match. Re-stamping cannot establish equivalence.
- **Why:** Otherwise a delayed draft can acquire newer upstream hashes it never saw; a branch can silently certify old claims against changed evidence. These are intrinsic binding semantics, not a new QA system.
- **Implications:** Preview must select the same context's returns; staleness and branch reuse share this identity.
- **Confidence:** H. **Value:** H.

D03 — MUST — Make RERUN possible without manufacturing a final

- **Plan:** Phase 3 always assembles/stamps final+review, then `--finalize-render`; status checks missing final before RERUN. Phase 6 allows the Editor to reject unsupported carrying claims or wrong strategy.
- **Repo:** `schemas/review.schema.json` requires a final hash. `cli.py::cmd_finalize` requires current artifacts but never checks `review.triage`. Extracting its body preserves that behavior.
- **Delta:** Allow `review.json` with RERUN bound to the rejected draft/input fingerprint, without creating a final. READY/CHECK reviews additionally bind the assembled final. Handle a current RERUN before missing-final routing; suppress finalize/render for it. An upstream replacement expires that rejection for routing, while its reasons remain advisory input to the requested stage.
- **Why:** An Editor declining reconstruction must not publish the rejected draft merely to record the rejection. Old RERUN decisions must not trap a repaired job in the same stage.
- **Implications:** Conditional review binding and Stage-3 write set; no new failure artifact or retry engine.
- **Confidence:** H. **Value:** H.

D04 — EXPERIMENT — Route advocacy to the submitted document, not around CV-only jobs

- **Plan:** Scout infers NONE from “upload an updated copy of your CV”; NONE skips Stage 2. Registry nevertheless makes edits depend on `letter_draft`.
- **Repo:** Copied Visma vacancy (`runs/r20260914-211650-5d3516/jobs/visma_product_manager/derived/vacancy_normalized.md:154`) requests an extensive CV plus application questions. Norwegian's corresponding vacancy at `runs/r20260914-211651-5dbd38/jobs/norwegian_senior_manager_digital_governance/derived/vacancy_normalized.md:153` requests a CV. Neither establishes a letter prohibition. Current `merge.py::effective_cv` already offers CV replacement surfaces.
- **Delta:** Scout records REQUIRED/OPTIONAL/UNSPECIFIED with the quote; Architect chooses delivery explicitly. Keep ADVOCATE in the chain: for CV-only delivery it strengthens the CV's argument and returns `letter:null` plus CV replacements; for letter delivery it writes the letter. Rename the artifact `advocacy_draft`; make its schema and keystones cover either document. Keep rendering conditional on document presence.
- **Why:** CV-only screening increases the CV's argumentative burden. Skipping the designated persuasion specialist reverses the intended allocation. Unknown: incremental persuasive value versus another pass's cost; compare the Architect and Advocate CVs on one human-started CV-only job before making this permanent. If skipping wins, explicitly make the registry dependency conditional.
- **Confidence:** H on omission/dependency; M on allocation advantage. **Value:** H.

D05 — MUST — Separate an implementation smoke from human-started model trials

- **Plan:** Verification steps 2–4 seed only CV/letter returns but submit Stage 3; step 5 requires a real named-model chain and dual review within implementation completion.
- **Repo:** `cli.py::cmd_context` requires current upstream artifacts; the proposed registry additionally requires scout+brief. `prompts/STAGE1_PROMPT.md::Goal scope` explicitly confines one session to one stage; `cli.py::build_parser` provides deterministic commands, not model-session dispatch.
- **Delta:** Use raw seeded returns only for direct assembly/render smoke; exercise stage-submit only with a complete new-schema upstream chain. Define deterministic implementation completion separately from the later human-started specialist sessions; print their concrete launch prompts and stop at that boundary. Resume package comparison after those sessions produce real outputs; do not call the quality trial completed at the implementation stop.
- **Why:** Seeded drafts cannot satisfy the proposed upstream contract. One implementing session cannot also stand in for the promised independently human-started specialist chain.
- **Confidence:** H. **Value:** H.

## Net plan delta

- **Replace:** binding strategy/substrings/percentage rules → elastic briefs, frozen-source retrieval and field replacements.
- **Add:** one consumed-context fingerprint; input-bound RERUN without a final.
- **Replace:** Stage-2 skip → document-aware advocacy; channel inference → quoted requirement plus explicit delivery choice.
- **Remove:** substring matcher/repair machinery and lexical keystone enforcement.
- **Reorder:** complete deterministic smoke separately from human-started quality trials.
- **Adjudicate:** parent-snapshot versus refreshed-input branches; CV-only advocacy's extra cost versus quality benefit.
