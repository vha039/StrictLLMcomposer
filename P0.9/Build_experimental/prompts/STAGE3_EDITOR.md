# Stage 3 goal prompt - EDITOR

Paste this into a fresh Claude Code session on the model mapped to EDITOR, with
the advisor available. One session per stage and cluster. Replace `<RUN>` and
`<CLUSTER>`.

~~~text
Goal: complete Stage 3 (EDITOR) for every CORE job in run <RUN>, cluster <CLUSTER>.
Work from C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build_experimental.
Use .\.venv\Scripts\jobbsok.exe for every command. This session is Stage 3 only.
You edit in layers or you decline; you never rebuild the package yourself.

Loop, one job at a time:
1. jobbsok next --run <RUN> --stage 3 --cluster <CLUSTER>
2. jobbsok context --run <RUN> --job <JOB> --stage 3
3. Reset to the bundle. Read read.playbook and read.policy in full, then the
   assembled draft, the brief, cards_used.md with its boundary appendix, the
   keystones, the distilled behaviours and register.md.
4. Four passes in order: screen-out, truth against the cards, personality and
   tone at the bundle's voice level, social risk.
5. Write polish.semantic.json - ONLY the fields you change, each with a reason -
   and review.semantic.json, to write.return_paths.
6. Iterate:
     jobbsok assemble --run <RUN> --job <JOB> --dry-run
     jobbsok preview  --run <RUN> --job <JOB> --stage 3
7. Consult your advisor once, with the assembled draft and your intended
   changes, before submitting.
8. Publish with commands.submit (add --finalize-render), or decline with
   commands.reject and a review whose triage is RERUN and rerun_stage is 1 or 2.

Rules that matter here:
- Return replacements, not rewrites of untouched fields.
- Declare a disposition for every keystone; removing one needs a TRUTH or
  SCREEN_OUT reason.
- Repair understatement as seriously as overstatement.
- Decline when upstream reconsideration is genuinely cheaper: wrong track,
  thesis or units (stage 1); employer-blind or structurally broken letter
  (stage 2).
- Triage on remaining repair scope, at most three reasons, never apply advice.

Finish the cluster with:
  jobbsok status --run <RUN> --json
  jobbsok register --run <RUN> --cluster <CLUSTER>
and report triage per job, any RERUN targets, and any degraded renders.
~~~
