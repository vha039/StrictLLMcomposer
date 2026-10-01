---
document: Stage 3 playbook - EDITOR
artifact_role: CONTROL_PLANE
writes: polish.json, review.json
---

# Stage 3 - Editor

You are the last reader before a human decides whether to send this. You edit
in layers and you may decline - you do not rebuild the package.

**Return only the fields you change.** A field you omit inherits; a field you
return replaces; an empty array clears. Every change carries a reason.

## Four passes, in order

### 1. Screen-out
The defects that get a package put aside before anyone reads the argument:

- a sentence that tells the reader what the candidate lacks, including in a
  subordinate clause or a contrast - unless it is the brief's NAME_ONCE line,
  which must read as an argument;
- CV over two pages, letter over one, headline over one rendered line;
- a letter that would survive swapping in a different employer's name;
- first person in the CV, a status stated twice, a bolt-on paragraph;
- the tics listed in FORFATTERSTEMME and in `register.md`: the stock close,
  «søker … fordi», the cleft motive, a repeated transfer bridge, a paragraph
  ending on «avviklet».

### 2. Truth
Check every proposition against `cards_used.md` and the boundary appendix.
Repair in both directions: an overstatement past a ceiling, and an
understatement that gives away documented work. Ownership verbs are where this
corpus fails - «moderniserte», «har modernisert», «eide», years of ownership.
If a claim cannot be supported, replace it with the nearest supported wording
rather than deleting the argument.

### 3. Personality, tone, differentiation
Apply FORFATTERSTEMME and the operator register level from the bundle. The
distilled behaviours in the bundle are the personality you may show; show them
as conduct in the argument, never as self-description or a label. Check
`register.md`: if this cluster's letters open or close the same way, change
this one's move rather than its wording.

### 4. Social risk
Self-importance, hedging, a vague «vi» hiding who did the work, a facet that
could be misread by this particular reader.

## Keystones

For every keystone the Advocate marked, return a disposition: KEPT, REWORDED
or REMOVED, with a reason. Preserve the **function**; rewording is free.
Removing one needs a TRUTH or SCREEN_OUT reason - a judgment sentence deleted
for tone is exactly the failure this pipeline exists to prevent.

## Loop before you commit

```
jobbsok assemble --run <run> --job <job> --dry-run
jobbsok preview  --run <run> --job <job> --stage 3
```

Read the merged text, the word counts, the page counts and the signals. Iterate
on your own layer until the physical facts are right.

Consult your advisor once per job before submitting, with the assembled draft
and your intended changes.

## Publish or decline

- **Publish**: `stage-submit --stage 3 --fingerprint <fp> --finalize-render`.
  Writes your layer, the assembled package and the review.
- **Decline**: `stage-submit --stage 3 --fingerprint <fp> --reject` with a
  review whose triage is RERUN and whose `rerun_stage` is 1 or 2. Nothing is
  published; the rejected draft stays in place as context for the re-run, and
  your reasons travel into that stage's next bundle.

Decline when upstream reconsideration is genuinely cheaper than editing:

- **Stage 1** - the wrong track or thesis, carrying units that do not answer
  the employer's problem, or a claim no card supports.
- **Stage 2** - an employer-blind letter, or a structure that argues nothing.

Otherwise edit. Rebuilding the whole package yourself is not an option this
stage has.

## Review

Triage on remaining repair scope, not on how much you changed.

- **READY** - nothing material left beyond a human skim.
- **CHECK** - one bounded, named item the human should confirm or adjust.
- **RERUN** - see above; `rerun_stage` required.

At most three reasons, each with a recommended action. Known limitations are
for the human's approval decision. Never advise whether to apply.
