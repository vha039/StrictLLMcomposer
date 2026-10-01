# Operator stage prompts

The active route is **Stage 1 → Stage 3; separate instance/chat for each.**
Stage 2 is retired; its prompt is gone and only historical runs still contain a
frozen Stage-2 instruction.

One prompt per active semantic stage. Each initiates a **stage × cluster** task: fill in
`RUN` and `CLUSTER` at the top, send everything below the line, and the model
works that cluster's outstanding jobs sequentially from current disk state.

```
STAGE1_PROMPT.md   Decision Architecture      SOL_CLASS    writes strategy
STAGE3_PROMPT.md   Elastic Final Writer       SOL_CLASS    writes final_package + review,
                                                           then finalize + render
```

## These are not frozen inputs

This directory is **not** control plane in the hash-bound sense. Nothing here is
read by `jobbsok`, hashed into a manifest, or verified by `verify-integrity`.
The frozen control plane a run actually binds to is `policy/`, `schemas/`,
`templates/`, `authorities/` and `context/`, recorded in
`runs/<run_id>/manifest.json` and copied under `runs/<run_id>/frozen/`.

That separation is deliberate, and it is why every prompt tells the model to
read the frozen `read.stage_instruction` path that `context` prints, never the
live `policy/stages/...` copy. The live policy can move between runs; only the
frozen copy governs a given run.

A prompt may therefore be edited at any time without invalidating any existing
run. It is operator material: it carries the loop, the reset discipline, the
submission mechanics and the failure handling. It carries no product policy,
and where it and a stage instruction disagree, the stage instruction wins.

## Model roles

Roles are frozen per run in `policy/settings.toml [stages.role_mapping]` and
snapshotted into the manifest. The prompts deliberately say nothing about
reasoning effort — that is selected in the product UI, not in prose.
