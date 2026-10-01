# Stage goal prompts

One prompt per stage. You start each session yourself, on the model mapped to
that stage's role in `policy/settings.toml` → `[stages.role_mapping]`:

| Stage | Role | File |
|---|---|---|
| 0 | SCOUT | [`STAGE0_SCOUT.md`](STAGE0_SCOUT.md) |
| 1 | ARCHITECT | [`STAGE1_ARCHITECT.md`](STAGE1_ARCHITECT.md) |
| 2 | ADVOCATE | [`STAGE2_ADVOCATE.md`](STAGE2_ADVOCATE.md) |
| 3 | EDITOR | [`STAGE3_EDITOR.md`](STAGE3_EDITOR.md) |

One session covers one **stage × cluster** and works the cluster's jobs in
order. A session never crosses a stage boundary.

These prompts are operator scaffolding: they are not frozen into a run and
carry no authority. The frozen playbook in `policy/stages/` and the writing
policy assembled into each bundle's `policy.md` are what govern a stage. Where
a prompt and the frozen instruction disagree, the frozen instruction wins.

The context bundle prints every path a stage needs, the exact return paths, the
evidence fingerprint and the exact submit command. Nothing else is authority -
not chat history, not a remembered path from the previous job.
