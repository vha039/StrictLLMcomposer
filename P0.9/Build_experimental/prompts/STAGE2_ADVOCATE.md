# Stage 2 goal prompt - ADVOCATE

Paste this into a fresh session on the model mapped to ADVOCATE. One session
per stage and cluster. Replace `<RUN>` and `<CLUSTER>`.

~~~text
Goal: complete Stage 2 (ADVOCATE) for every CORE job in run <RUN>, cluster <CLUSTER>.
Work from C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build_experimental.
Use .\.venv\Scripts\jobbsok.exe for every command. This session is Stage 2 only:
you write the advocacy layer. You do not re-decide the position and you do not
do voice or personality polish - the Editor owns those.

Loop, one job at a time:
1. jobbsok next --run <RUN> --stage 2 --cluster <CLUSTER>
2. jobbsok context --run <RUN> --job <JOB> --stage 2
3. Reset to the bundle. Read read.playbook and read.policy in full, then the
   brief, the CV layer, the vacancy and cards_scoped.md. Read register.md
   before choosing wording, and rerun_advice.md if it is there.
4. If the argument needs evidence the brief did not name, fetch it
   (jobbsok cards --run <RUN> --ids "EV:..." or --search "<literal>") and list
   it in outside_brief_refs. Ceilings on the cards always bind.
5. Write advocacy_draft.semantic.json to write.return_paths, semantic fields
   only, following write.schema_paths.
6. jobbsok preview --run <RUN> --job <JOB> --stage 2
   One page for the letter, two for the CV, headline on one line.
7. Submit exactly the command in commands.submit. Fix and resubmit once if it
   is refused.

Rules that matter here:
- Follow the brief's letter plan and its opening and closing moves.
- Convert the employer fact once; complement the CV instead of retelling it.
- Judgment and consequence over implementation mechanics.
- One caveat per claim, one status per case, at most one transfer bridge.
- Coverage integrated into the arguments; no bolt-on paragraph.
- CV_ONLY delivery: letter null, argument moved into CV replacement fields,
  every screening question answered in form_answers.
- Mark one to four keystones: the sentences whose argument function must
  survive editing. Keystone text must appear verbatim in the document it names.
- Touch the CV only for complementarity; expect zero to two fields.

Finish the cluster with:
  jobbsok status --run <RUN> --json
  jobbsok register --run <RUN> --cluster <CLUSTER>
and report the outstanding jobs.
~~~
