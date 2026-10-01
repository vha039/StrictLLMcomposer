# Stage 0 goal prompt - SCOUT

Paste this into a fresh session on the model mapped to SCOUT. One session per
stage and cluster. Replace `<RUN>` and `<CLUSTER>`.

~~~text
Goal: complete Stage 0 (SCOUT) for every CORE job in run <RUN>, cluster <CLUSTER>.
Work from C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build_experimental.
Use .\.venv\Scripts\jobbsok.exe for every command. This session is Stage 0 only:
do not author a brief, a CV, a letter or a review.

Loop, one job at a time:
1. jobbsok next --run <RUN> --stage 0 --cluster <CLUSTER>
2. jobbsok context --run <RUN> --job <JOB> --stage 0
3. Reset to the bundle: read read.playbook and read.policy in full, then the
   vacancy, the digests, the retrieval index and the catalog. The bundle's job
   identity is authority; your memory of the previous job is not.
4. Read the frozen authorities or fetch cards as needed:
   jobbsok cards --run <RUN> --search "<literal>"   /   --ids "EV:...,EV:..."
5. Write ONLY the semantic fields of scout.json to write.return_paths.scout,
   following write.schema_paths.scout. Never write artifact_role or binding.
6. Submit exactly the command in commands.submit.
7. If submission is refused, read the reason, fix it once, and resubmit.

Rules that matter here:
- Quote the ad verbatim for every requirement, threshold, track, employer fact
  and submission statement. Leave a field null rather than guessing.
- Thresholds compare the ad against the candidate's own record. Report
  MEETS/MISSES/UNCLEAR. Never advise whether to apply.
- letter_requirement records what the ad says, not what you would do.
- Triage demotes, never drops: core (<=12) is what the Architect reads first,
  reserve is everything else plausible. Include at least one non-obvious
  candidate per major requirement.
- Ignore FINN match percentages and platform advice.

Finish the cluster with:
  jobbsok status --run <RUN> --json
and report which jobs now have a current scout and which are outstanding.
~~~
