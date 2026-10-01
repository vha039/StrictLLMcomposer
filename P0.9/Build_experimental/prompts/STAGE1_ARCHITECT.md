# Stage 1 goal prompt - ARCHITECT

Paste this into a fresh session on the model mapped to ARCHITECT. One session
per stage and cluster. Replace `<RUN>` and `<CLUSTER>`.

~~~text
Goal: complete Stage 1 (ARCHITECT) for every CORE job in run <RUN>, cluster <CLUSTER>.
Work from C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build_experimental.
Use .\.venv\Scripts\jobbsok.exe for every command. This session is Stage 1 only:
you write the brief and the CV layer, never the letter and never a review.

Loop, one job at a time:
1. jobbsok next --run <RUN> --stage 1 --cluster <CLUSTER>
2. jobbsok context --run <RUN> --job <JOB> --stage 1 --stats
3. Reset to the bundle. Read read.playbook and read.policy in full, then the
   scout, the vacancy and cards_core.md. Read rerun_advice.md if it is there.
4. Challenger sweep before deciding: reserve.md, the digests, the catalog, and
   jobbsok cards --run <RUN> --search "<literal>" or --ids "EV:...".
   Name at least one challenger per carrying unit; record anything you use from
   outside the scout's core in outside_scout_refs.
5. Write brief.semantic.json and cv_draft.semantic.json to write.return_paths,
   semantic fields only, following write.schema_paths.
6. jobbsok preview --run <RUN> --job <JOB> --stage 1
   Iterate on the CV until it is two pages with a one-line headline, inside the
   capacity figure in the bundle.
7. Submit exactly the command in commands.submit. Fix and resubmit once if it
   is refused.

Rules that matter here:
- Choose the track explicitly; write one thesis sentence; choose delivery
  (LETTER_AND_CV / CV_ONLY / CV_PLUS_FORM_ANSWERS) with a reason.
- At most three carrying units, each with a verbatim ceiling from its card.
- Convert exactly one employer fact.
- NAME_ONCE only for a threshold the screener sees anyway, as one sentence that
  turns it into the argument. Otherwise OMIT or BRIDGE.
- Pick opening and closing moves that differ from register.md.
- No gaps, caveats or learning instructions in positive fields.
- No first person in the CV; tools go on the tools line; state a status once.
- Keep the brief under about 8 KB.

Do the cluster-level tightening pass before submitting, not after the register
view at the end of the cluster. If you revise a brief after submitting it,
say so in the session report and name what it invalidated.

Finish the cluster with:
  jobbsok status --run <RUN> --json
  jobbsok register --run <RUN> --cluster <CLUSTER>
and report the outstanding jobs.
~~~
