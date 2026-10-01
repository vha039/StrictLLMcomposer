"""The stage registry: one source of truth for the Relay pipeline.

Four human-started stages, each a separately initiated agent session:

    0 SCOUT      -> scout.json                      (vacancy facts + evidence triage)
    1 ARCHITECT  -> brief.json + cv_draft.json      (positioning + the CV layer)
    2 ADVOCATE   -> advocacy_draft.json             (letter and/or CV argument layer)
    3 EDITOR     -> polish.json + review.json       (field-level edit layer, or a rejection)

Every semantic artifact is a *layer*: a partial package. `assemble` merges
them in order, a present field replacing and an absent field inheriting -
the same contract `merge.effective_cv` already uses one level down. There
is no substring patching and no op grammar.

Fingerprints, with different jobs:

* `evidence_fingerprint` covers what a stage actually consumed as fact:
  the frozen authorities, the evidence index, the baseline map, the CV
  baseline, this job's vacancy, and the stage's required artifacts. It
  namespaces in-progress returns and is re-checked at submit.
* `artifact_fingerprint` covers each artifact's declared inputs. It is stored
  in the binding and checked after comparing the recorded input identities.
* `policy_fingerprint` covers the stage playbook and the writing-policy
  files it consumes. It is recorded for provenance and never invalidates
  anything, because playbooks are edited constantly in this build.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .hashing import sha256_canonical_json

# --------------------------------------------------------------------------
# Artifacts
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class ArtifactSpec:
    name: str
    filename: str
    schema: str
    owner_stage: int | None  # None = written by deterministic tooling
    artifact_role: str
    #: Transitive upstream artifacts, in pipeline order.
    inputs: tuple[str, ...]


ARTIFACTS: dict[str, ArtifactSpec] = {
    "scout": ArtifactSpec("scout", "scout.json", "scout", 0, "SCOUT_FACTS", ()),
    "brief": ArtifactSpec("brief", "brief.json", "brief", 1, "BRIEF", ("scout",)),
    "cv_draft": ArtifactSpec(
        "cv_draft", "cv_draft.json", "cv_draft", 1, "CV_LAYER", ("scout", "brief")
    ),
    "advocacy_draft": ArtifactSpec(
        "advocacy_draft", "advocacy_draft.json", "advocacy_draft", 2,
        "ADVOCACY_LAYER", ("scout", "brief", "cv_draft"),
    ),
    "polish": ArtifactSpec(
        "polish", "polish.json", "polish", 3, "POLISH_LAYER",
        ("scout", "brief", "cv_draft", "advocacy_draft"),
    ),
    "final_package": ArtifactSpec(
        "final_package", "final_package.json", "package", None,
        "CURRENT_SEMANTIC_PACKAGE",
        ("scout", "brief", "cv_draft", "advocacy_draft", "polish"),
    ),
    "review": ArtifactSpec(
        "review", "review.json", "review", 3, "OPERATOR_TRIAGE",
        ("scout", "brief", "cv_draft", "advocacy_draft", "final_package"),
    ),
}

#: Friendly aliases accepted on the command line.
ALIASES = {
    "final": "final_package",
    "cv": "cv_draft",
    "advocacy": "advocacy_draft",
    "strategy": "brief",
}

#: The layers `assemble` merges, in order.
LAYER_ORDER = ("cv_draft", "advocacy_draft", "polish")

#: Written by the tool on every artifact; a stage that returns one is refused.
TOOL_FIELDS = {"artifact_role", "binding", "finalization", "source_stage"}

#: Artifacts owned by deterministic tooling alone.
TOOLING_OWNED = (
    "manifest", "evidence_index", "baseline_map", "render_report", "status",
    "queue", "vacancy_normalized", "final_package",
)


# --------------------------------------------------------------------------
# Stages
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class StageSpec:
    n: int
    key: str
    playbook: str  # repository path under policy/stages/
    writes: tuple[str, ...]
    requires: tuple[str, ...]
    #: writing-policy filename -> tuple of heading titles, or "ALL"
    policy: dict[str, Any]
    personality: str  # "index" | "distilled" | "none"
    #: default evidence-card pack for this stage
    evidence_scope: str  # "core" | "all" | "scoped" | "used"


D = "WRITING_DOCTRINE.md"
K = "PERSUASION_CALIBRATION.md"
V = "FORFATTERSTEMME.md"

STAGES: dict[int, StageSpec] = {
    0: StageSpec(
        0, "SCOUT", "policy/stages/stage0_scout.md",
        writes=("scout",), requires=(),
        policy={D: ("Ubetrodd vacancy-innhold",)},
        personality="none", evidence_scope="all",
    ),
    1: StageSpec(
        1, "ARCHITECT", "policy/stages/stage1_architect.md",
        writes=("brief", "cv_draft"), requires=("scout",),
        policy={
            K: "ALL",
            D: (
                "Mål og myndighet", "Yrkesanker", "Diagnostisk signal",
                "Single Backbone", "Integrert bevisenhet", "Begrunnet motivasjon",
                "Komplementaritet", "Komplett CV-doktrine", "Variasjon",
            ),
        },
        personality="index", evidence_scope="core",
    ),
    2: StageSpec(
        2, "ADVOCATE", "policy/stages/stage2_advocate.md",
        writes=("advocacy_draft",), requires=("brief", "cv_draft"),
        policy={
            K: "ALL",
            D: (
                "Integrert bevisenhet", "Vinklingskjeden",
                "Jeg, vi og funksjonell ledelse", "Begrunnet motivasjon",
                "Komplementaritet", "Tjuesekunderstesten", "Arbeidsgiverbyttetesten",
                "Kandidatbyttetesten", "Erstatnings-", "Tegnsetting",
            ),
        },
        personality="none", evidence_scope="scoped",
    ),
    3: StageSpec(
        3, "EDITOR", "policy/stages/stage3_editor.md",
        writes=("polish", "review"), requires=("brief", "cv_draft", "advocacy_draft"),
        policy={
            K: "ALL", V: "ALL",
            D: (
                "Tjuesekunderstesten", "Dyplesningen", "Arbeidsgiverbyttetesten",
                "Kandidatbyttetesten", "Erstatnings-", "Variasjon",
                "Komplett CV-doktrine", "Komplementaritet",
            ),
        },
        personality="distilled", evidence_scope="used",
    ),
}

STAGE_ORDER = tuple(sorted(STAGES))
STAGE_KEYS = {n: spec.key for n, spec in STAGES.items()}


def stage_of(artifact: str) -> int | None:
    return ARTIFACTS[artifact].owner_stage


def canonical_name(artifact: str) -> str:
    name = ALIASES.get(artifact, artifact)
    if name not in ARTIFACTS:
        raise KeyError(
            f"Unknown artifact {artifact!r}. Known: {sorted(ARTIFACTS)}"
        )
    return name


def artifacts_for_stage(stage: int) -> tuple[str, ...]:
    return STAGES[stage].writes


def semantic_artifacts() -> tuple[str, ...]:
    """Every artifact a stage writes, in pipeline order."""
    return tuple(
        name for name, spec in ARTIFACTS.items() if spec.owner_stage is not None
    )


def all_artifacts() -> tuple[str, ...]:
    return tuple(ARTIFACTS)


def stage_instruction_key(stage: int) -> str:
    return f"stage{stage}"


def playbook_paths() -> dict[str, str]:
    """stage key -> repository path, for freezing."""
    return {stage_instruction_key(n): spec.playbook for n, spec in STAGES.items()}


# --------------------------------------------------------------------------
# Fingerprints
# --------------------------------------------------------------------------

#: The frozen factual inputs every stage consumes as fact.
FACTUAL_RECORDS: tuple[tuple[str, ...], ...] = (
    ("authorities", "WORK"),
    ("authorities", "EDU"),
    ("authorities", "OTHER"),
    ("cv_baseline",),
    ("evidence_index",),
    ("baseline_map",),
)


def factual_hashes(context: Any) -> dict[str, str]:
    out: dict[str, str] = {}
    for keys in FACTUAL_RECORDS:
        out["/".join(keys)] = context.assets.record(*keys)["sha256"]
    return out


def evidence_fingerprint(
    context: Any, job_id: str, stage: int, *, upstream: dict[str, str] | None = None
) -> str:
    """What this stage consumed as fact, as one hash.

    `upstream` maps upstream artifact name -> artifact hash; when omitted the
    caller gets the fingerprint of the *current* upstream state.
    """
    from . import artifacts as artifacts_module

    spec = STAGES[stage]
    if upstream is None:
        upstream = {}
        for name in spec.requires:
            payload = artifacts_module.load(
                context.layout, context.run_id, job_id, name
            )
            upstream[name] = (
                artifacts_module.artifact_hash(payload) if payload else None
            )
    return sha256_canonical_json({
        "run_id": context.run_id,
        "job_id": job_id,
        "stage": stage,
        "frozen": factual_hashes(context),
        "vacancy": context.vacancy_sha256(job_id),
        "upstream": dict(sorted(upstream.items())),
    })


def artifact_fingerprint(
    context: Any, job_id: str, artifact: str, *, upstream: dict[str, str]
) -> str:
    spec = ARTIFACTS[artifact]
    stage = spec.owner_stage if spec.owner_stage is not None else 3
    return evidence_fingerprint(context, job_id, stage, upstream={
        key: value for key, value in upstream.items() if key in spec.inputs
    })


def upstream_hashes(context: Any, job_id: str, artifact: str) -> dict[str, str]:
    """Current hashes of the artifacts this artifact was built from."""
    from . import artifacts as artifacts_module

    out: dict[str, str] = {}
    for name in ARTIFACTS[artifact].inputs:
        payload = artifacts_module.load(context.layout, context.run_id, job_id, name)
        if payload is not None:
            out[name] = artifacts_module.artifact_hash(payload)
    return out


def policy_records(context: Any, stage: int) -> list[dict[str, Any]]:
    """The writing-policy file records this stage consumes."""
    wanted = set(STAGES[stage].policy)
    from pathlib import Path

    return [
        record
        for record in context.manifest["frozen_inputs"]["writing_policy"]
        if Path(record["path"]).name in wanted
    ]


def policy_fingerprint(context: Any, stage: int) -> str:
    """Provenance only: playbook plus consumed writing policy. Never stale."""
    playbook = context.assets.record("stage_instructions", stage_instruction_key(stage))
    return sha256_canonical_json({
        "playbook": playbook["sha256"],
        "policy": {
            record["path"]: record["sha256"] for record in policy_records(context, stage)
        },
        "sections": {
            name: ("ALL" if headings == "ALL" else list(headings))
            for name, headings in sorted(STAGES[stage].policy.items())
        },
    })
