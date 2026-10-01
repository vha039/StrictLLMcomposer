# Opus 5 Max meta-review — rationale notes

Compact companion to the `OPUS_META_ADD` blocks in
`P0.9_Final_Multi_Model_Review_Reconciliation.md`. Nothing here is authority;
everything decision-relevant is in the reconciliation itself.

## Verdict

The reconciliation stands. Its eight-family compression, evidence weighting,
refusal to vote-count and `NO-GO` verdict all survive independent
re-verification. This pass added one root cause, one blocker, several severity
corrections, four anti-regression guards and two factual repairs — no competing
synthesis, no rewrite.

## What changed, and why it matters to the Codex run

| Addition | Why it changes the run |
|---|---|
| **OM-004** — the manual Stage-2/3 binding handoff cannot complete | `context` omits the upstream semantic hash the schema requires, the RUNBOOK never supplies it, and `stage-submit` accepts a wrong one while archiving the good artifact. The smoke fails at its first Stage-2 submission. `MMR-006` and `MMR-035` each held half of this; neither drew the conclusion, and `MMR-035`'s `IMPROVE/Medium/"friction"` framing would have deprioritized it. |
| **OM-003** — RC-9, containment is exception-class-scoped | A `dd.mm.yyyy` date typo aborts a multi-job render mid-transaction and leaves a CV without its letter; a malformed artifact kills `status` and `next`. `MMR-017` and `MMR-018` are its two symptoms; connecting them turns three local patches into one shared correction. |
| **OM-002** — the delivered evidence is not re-derivable | The §19 slice documents a run that no longer exists; the surviving run's render receipt binds a hash matching nothing; three final generations are implied and two exist nowhere. Raises `MMR-046` from "reports overclaim" to "the primary conformance evidence cannot be re-derived", and warns Codex not to treat the delivered run as a worked example. |
| **OM-007** — `AMEND-4` would legalize the dangerous half | `--dest` writing into `authorities/` and `templates/` is control-plane contamination, not "external export". Wording that permits external paths without refusing protected in-repo roots leaves the reproduced defect legal. |
| **OM-008** — a smaller remedy for branch staleness | The cascade exists because `artifact_hash` includes `binding.run_id`/`manifest_sha256`. Excluding them (as `finalization` already is) makes rebind hash-neutral and removes the need for topological re-stamping. Run identity is enforced directly by `_check_identity`, so nothing weakens. |
| **OM-006** — `AR-16`…`AR-19` | The pass touches `docxfill`, `prepare_masters` and `pdf`. Reintroducing `python-docx`/`lxml` would silently recreate the exact `docProps/core.xml` defect that made the P0.7 masters unopenable in Word. Also carries forward Gemini `RT-09` (post-freeze inbox isolation), which the register dropped. |
| **OM-005b** — a falsified hypothesis, recorded | Word COM does **not** hijack or close the operator's session; Word 16 isolates automation instances. Recorded so no later agent "fixes" it — and because it supplies the safety proof §5.6 said `MMR-024`'s exact-instance cleanup would need. |
| **OM-005** — coordinates for 24 register rows | Line numbers, exact hashes, measured thresholds. Removes re-hunting cost and lets Codex spend its falsification budget on judgment rather than location. |

## Minority findings deliberately preserved

- **Sonnet `F-01`'s remedy constraint** — *do not* add `"render"` as a peer key in
  `ARTIFACTS`. The register carries the finding but not the constraint, and
  `RC-4`'s "receipt" framing invites a larger refactor. Carried in OM-005.
- **Gemini `RT-09`** — post-freeze inbox isolation, a KEEP the register did not
  carry into the `AR` table. Now `AR-17`, because `MMR-014` is the change most
  likely to break it.
- **Sonnet `F-04`** — the `history/` mechanism is benign, as Sonnet found. Its
  *characterisation* of this run's residue as ordinary re-runs is qualified in
  OM-002 by the three-generation gap.
- **Sonnet `F-03`** — `max_selected_facets` is pinned independently in
  `settings.toml` and `personality_facets.json` with no cross-check. Trivial,
  absent from the register, and not worth a block; one assertion closes it if
  Codex is already in that file.
- **Luna `HWF-02/08/09/10/12/13/16/20`** are subsumed by `MMR-034/035/014` or are
  observational. Nothing material was dropped, so Codex need not open Luna's file
  except for `HWF-14/15` queue-detail texture.

## Two repository facts to act on

1. The reconciliation is `P0.9_Final_Multi_Model_Review_Reconciliation.md`, not
   `00_FINAL_RECONCILIATION.md`. Either rename it once and update the pointers,
   or leave it and keep referencing the real name — but do not let a fresh agent
   conclude it is missing. The proposed `AGENTS.md` and `/plan` prompt both use
   the real name.
2. `P0.9/Build/Build.zip` exists and holds a second copy of the candidate
   authorities and personality profile outside every protected root. Delete or
   relocate it and add it to `.gitignore`.

## Method note

Destructive reproductions ran on scratch copies at a short filesystem path
(`MAX_PATH` and `paths.MAX_PATH_CHARS` were themselves under test). The
canonical `P0.9/Build/` was re-verified afterwards: `verify-integrity` intact,
4/4 artifacts valid, master and schema hashes unchanged. Frozen Architecture
files were not touched.
