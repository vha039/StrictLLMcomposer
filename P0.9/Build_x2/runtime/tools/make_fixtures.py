"""Generate valid and adversarial artifact fixtures for the vertical slice.

Contract 19 requires the deterministic vertical slice to run one synthetic
core job with a valid strategy fixture, an invalid strategy fixture, and
valid draft/final/review fixtures, against the actual authorities, baseline
and masters.

These fixtures stand in for manually initiated model chats. They are
deliberately hand-written content that satisfies the mechanical contracts;
they are NOT product-quality writing and prove nothing about semantic
quality (INV-08).

Usage:
    python -m tools.make_fixtures --run <run_id> [--out DIR]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from jobbsok.atomicio import atomic_write_json, read_json  # noqa: E402
from jobbsok.manifest import (  # noqa: E402
    find_job,
    frozen_path,
    load_manifest,
    read_frozen,
)
from jobbsok.artifacts import artifact_hash  # noqa: E402
from jobbsok.hashing import sha256_file  # noqa: E402
from jobbsok.paths import Layout  # noqa: E402


def binding(layout: Layout, manifest: dict, job: dict, stage: int) -> dict:
    run_id = manifest["run_id"]
    key = {1: "stage1", 3: "stage3"}[stage]
    return {
        "run_id": run_id,
        "job_id": job["job_id"],
        "employer": job["employer"],
        "title": job["title"],
        "manifest_sha256": sha256_file(layout.run_dir(run_id) / "manifest.json"),
        "vacancy_sha256": job["source"]["sha256"],
        "evidence_index_sha256": read_frozen(layout, manifest, "evidence_index")["sha256"],
        "stage_instruction_sha256": read_frozen(
            layout, manifest, "stage_instructions", key
        )["sha256"],
    }


def build(layout: Layout, run_id: str, out: Path) -> None:
    manifest = load_manifest(layout, run_id)
    job = manifest["jobs"][0]
    index = read_json(
        frozen_path(layout, run_id, read_frozen(layout, manifest, "evidence_index"))
    )
    ids = {e["evidence_id"] for e in index["entries"]}

    def pick(source: str, needle: str) -> str:
        for entry in index["entries"]:
            if entry["source_id"] == source and needle in entry["evidence_id"]:
                return entry["evidence_id"]
        return f"EV:{source}#file"

    ev_role = pick("WORK", "navaerende-rolle")
    ev_bar = pick("WORK", "barne")
    ev_core = pick("WORK", "ous-kjerne")
    ev_edu = pick("EDU", "gradskronologi")
    ev_other = pick("OTHER", "profesjonell-kjernetese")
    for ref in (ev_role, ev_bar, ev_core, ev_edu, ev_other):
        assert ref in ids, ref

    out.mkdir(parents=True, exist_ok=True)

    # ---------------- strategy (valid) ----------------
    strategy = {
        "artifact_role": "STRATEGY_HYPOTHESIS",
        "authority": "NON_FACTUAL_NON_FINAL",
        "elasticity": "ELASTIC",
        "final_writer_may_reconstruct": True,
        "source_escape_permitted": False,
        "binding": binding(layout, manifest, job, 1),
        "employer_decision_problem": (
            "Avdelingen har store datamengder, men for lite anvendbar "
            "beslutningsstøtte for økonomi, aktivitet og bemanning."
        ),
        "selection_logic": (
            "De vil se dokumentert evne til å omsette uklare behov fra ledere "
            "til etterprøvbare rapporter, ikke verktøybredde alene."
        ),
        "primary_candidate_identity": (
            "Rådgiver som bygger beslutningsstøtte i sykehusøkonomi"
        ),
        "headline_hypothesis": "Økonomi · Beslutningsstøtte · IKT",
        "shortlist_thesis": (
            "Kandidaten har gjort nøyaktig dette arbeidet i en tilsvarende "
            "sykehusorganisasjon, med ansvar for både tallgrunnlag og leveranse."
        ),
        "material_requirements": [
            {"requirement_id": "R01",
             "text": "Høyere utdanning innen økonomi, statistikk eller tilsvarende",
             "importance": "MINIMUM", "relation": "SUPPORTED",
             "evidence_refs": [ev_edu]},
            {"requirement_id": "R02",
             "text": "Erfaring med rapportering og analyse i større virksomhet",
             "importance": "MINIMUM", "relation": "SUPPORTED",
             "evidence_refs": [ev_role]},
            {"requirement_id": "R03",
             "text": "Gode ferdigheter i SQL og Power BI",
             "importance": "IMPORTANT", "relation": "SUPPORTED",
             "evidence_refs": [ev_role, ev_core]},
            {"requirement_id": "R04",
             "text": "Bidra i budsjett- og prognosearbeid",
             "importance": "IMPORTANT", "relation": "SUPPORTED",
             "evidence_refs": [ev_bar]},
            {"requirement_id": "R05",
             "text": "God skriftlig og muntlig framstillingsevne på norsk",
             "importance": "MINIMUM", "relation": "SUPPORTED",
             "evidence_refs": [ev_other]},
            {"requirement_id": "R06",
             "text": "Interesse for prosessforbedring og automatisering",
             "importance": "DESIRED", "relation": "ADJACENT",
             "evidence_refs": [ev_core],
             "note": "Dokumentert som verktøybygging, ikke som formelt forbedringsmandat."},
        ],
        "evidence_plan": [
            {"evidence_refs": [ev_role], "role": "Hovedbevis for beslutningsstøtte",
             "claim_ceiling": "Utvikling og forbedring av beslutningsstøtte; ikke "
                              "eierskap til plattformdrift eller formelt personalansvar.",
             "lifecycle": "IN_USE", "baseline_refs": ["BL:EMP_OUS_ANALYSE"]},
            {"evidence_refs": [ev_bar], "role": "Bevis for tallgrunnlag og avstemming",
             "claim_ceiling": "Overtok en tildelt månedsoppgjørsflyt etter opplæring; "
                              "ikke ansvar for hele klinikkens økonomifunksjon.",
             "lifecycle": "COMPLETED", "baseline_refs": ["BL:EMP_OUS_BAR"]},
            {"evidence_refs": [ev_edu], "role": "Formell kvalifikasjon",
             "claim_ceiling": "Fullført mastergrad i samfunnsøkonomi; pågående "
                              "masterprogram i KI skal omtales som pågående.",
             "lifecycle": "COMPLETED"},
        ],
        "objections": [
            {"objection": "Erfaringen er fra én arbeidsgiver.",
             "reframe": "To ulike enheter med ulike behov og ulike leveranser, "
                        "innenfor samme foretak.",
             "honesty_note": "Ikke fremstill dette som bredde på tvers av sektorer."},
        ],
        "motivation_bridge": (
            "Arbeidet handler om å gjøre tallgrunnlag brukbart for dem som "
            "faktisk tar beslutningene. Det er den delen av økonomifaget "
            "kandidaten har brukt mest tid på."
        ),
        "cv_draft": {
            "headline": "Økonomi · Beslutningsstøtte · IKT",
            "profile": "Rådgiver ved OUS med beslutningsstøtte for økonomi og aktivitet.",
            "competencies": ["Beslutningsstøtte", "Økonomioppfølging"],
            "employment_overrides": [
                {"employment_id": "EMP_OUS_ANALYSE", "bullets": [
                    "Utvikler beslutningsstøtte for økonomi, bemanning og aktivitet."
                ]},
                {"employment_id": "EMP_OUS_BAR", "bullets": [
                    "Overtok den tildelte månedsoppgjørsflyten etter opplæring."
                ]},
            ],
        },
        "application_direction": {
            "backbone": "Kandidaten har bygget den beslutningsstøtten avdelingen mangler.",
            "top_employer_problems": [
                "Data finnes, men blir ikke til beslutningsgrunnlag.",
                "Tallgrunnlaget må kvalitetssikres før det kan brukes.",
            ],
            "structure_guidance": "Åpne på arbeidsgiverproblemet, ikke på kandidaten.",
        },
        "avoid_guidance": [
            "Ikke bruk «brenner for» eller tilsvarende entusiasmefraser.",
            "Ikke oppgrader funksjonell ledelse til personalansvar.",
            "Ikke gjør sykehusets skala til personlig effekt.",
            "Ikke la KI-studiet bli den bærende identiteten.",
        ],
        "counterfactual_route": None,
        "risk_notes": ["Rollen kan i praksis være mer controller enn analytiker."],
        "personality_facets": [
            {"facet_id": "PF-01",
             "plain_language_label": "Systems mapping & causal decomposition",
             "evidence_refs": [ev_role],
             "expression_ceiling": "Beskriv arbeidsmåte gjennom konkrete leveranser; "
                                   "ikke som en påstand om analytisk overlegenhet.",
             "vacancy_relevance": "Avdelingen beskriver uklare behov som må struktureres.",
             "intended_employer_interpretation": "En rådgiver som gjør uklare "
                                                 "behov til et beslutningsklart "
                                                 "grunnlag.",
             "misread_risk": "Kan leses som analysetung uten gjennomføringsevne.",
             "expression_guardrail": "Par alltid med en gjennomført leveranse."},
            {"facet_id": "PF-12",
             "plain_language_label": "Auditability / source-of-truth orientation",
             "evidence_refs": [ev_bar],
             "expression_ceiling": "Knytt til avstemming og kvalitetssikring som "
                                   "faktisk er dokumentert.",
             "vacancy_relevance": "Kvalitetssikring av datagrunnlag er en oppgave i utlysningen.",
             "intended_employer_interpretation": "En som gjør tallene etterprøvbare "
                                                 "før de brukes i beslutninger.",
             "misread_risk": "Kan leses som kontrollorientert framfor "
                             "beslutningsstøttende."},
        ],
        "writer_guidance": (
            "Rolig, presist bokmål. To hovedbevis. Ikke symmetrisk oppbygning."
        ),
        "requires_source_inspection_observed": False,
    }
    atomic_write_json(out / "strategy.valid.json", strategy)

    # ---------------- strategy (adversarial) ----------------
    invalid = json.loads(json.dumps(strategy))
    invalid["binding"]["employer"] = "Feil Arbeidsgiver AS"      # identity drift
    invalid["elasticity"] = "FIXED"                              # forbidden constant
    invalid["evidence_plan"][0]["evidence_refs"] = ["EV:WORK#999-finnes-ikke"]
    invalid["personality_facets"].append(
        {"facet_id": "PF-03", "plain_language_label": "x",
         "evidence_refs": [ev_core], "expression_ceiling": "x"})
    invalid["personality_facets"].append(
        {"facet_id": "PF-99", "plain_language_label": "y",
         "evidence_refs": [ev_core], "expression_ceiling": "y"})  # 4 facets + unknown id
    invalid["cv_draft"]["employment_overrides"][0]["employment_id"] = "EMP_FINNES_IKKE"
    atomic_write_json(out / "strategy.invalid.json", invalid)

    # ---------------- final package content ----------------
    cv = {
        "headline": "Økonomi · Beslutningsstøtte · IKT",
        "profile": (
            "Rådgiver i Analyseavdelingen ved Oslo universitetssykehus med "
            "arbeid innen beslutningsstøtte for økonomi, bemanning og aktivitet. "
            "Arbeidet omfatter både tallgrunnlag og rapporter: definisjoner, "
            "avstemming og dokumentasjon er det som gjør at ledere faktisk kan "
            "bruke tallene."
        ),
        "competencies": [
            "Beslutningsstøtte og styringsinformasjon",
            "Power BI, DAX og Power Query",
            "SQL og datakvalitet",
            "Økonomistyring og månedsoppgjør",
            "Dokumentasjon og kompetanseoverføring",
        ],
        "employment_overrides": [
            {"employment_id": "EMP_OUS_ANALYSE",
             "bullets": [
                 "Utvikler og forbedrer beslutningsstøtte for økonomi, bemanning, "
                 "aktivitet/DRG og pasientflyt i Power BI, DAX, Power Query, "
                 "Excel/VBA og SQL.",
                 "Omsetter brede og uklare behov til avgrensede løsninger med "
                 "kontroller, dokumentasjon og leveranser ledere og controllere "
                 "kan bruke.",
                 "Bidrar til strukturering av leveranser, workshops og "
                 "kompetanseoverføring i tverrfaglige oppdrag.",
             ]},
            {"employment_id": "EMP_OUS_BAR",
             "bullets": [
                 "Overtok etter opplæring den tildelte månedsoppgjørsflyten med "
                 "periodisering, avstemming, kvalitetssikring og resultatforklaring.",
                 "Utviklet Excel/VBA-verktøy for konvertering og validering ved "
                 "overgangen til REGERP, og bidro i budsjett og "
                 "aktivitetsrapportering.",
             ]},
        ],
    }
    letter = {
        "opening": (
            "Testetaten HF skriver at dere har store datamengder, men for lite "
            "anvendbar beslutningsstøtte. Det er den oppgaven jeg har arbeidet "
            "med de siste årene."
        ),
        "body_paragraphs": [
            "I Analyseavdelingen ved Oslo universitetssykehus utvikler jeg "
            "beslutningsstøtte for økonomi, bemanning og aktivitet. Arbeidet "
            "starter sjelden med et ferdig krav: det starter med en leder som "
            "har et spørsmål, og min oppgave er å finne ut hvilket tallgrunnlag "
            "som faktisk svarer på det, og deretter bygge noe som kan brukes "
            "hver måned.",
            "Før dette hadde jeg månedsoppgjørsflyten i Barne- og "
            "ungdomsklinikken, med periodisering, avstemming og "
            "resultatforklaring. Den erfaringen er grunnen til at jeg "
            "kvalitetssikrer datagrunnlaget før jeg bygger rapporten. Et tall "
            "som ikke lar seg avstemme, blir ikke brukt av noen.",
            "Utlysningen nevner både forvaltning av rapporter og "
            "kompetanseoverføring til brukerne. Jeg har dokumentert løsninger "
            "og holdt workshops i tverrfaglige oppdrag, og jeg regner "
            "overlevering som en del av leveransen, ikke som noe som kommer "
            "etterpå.",
        ],
        "closing": (
            "Jeg stiller gjerne til intervju for å gå nærmere gjennom hvordan "
            "jeg har løst tilsvarende oppgaver."
        ),
    }
    # The active route has no draft: Stage 3 writes the complete package
    # directly and binds the strategy it was written from.
    final = {
        "artifact_role": "CURRENT_SEMANTIC_PACKAGE",
        "source_stage": "STAGE3_FINAL",
        "binding": {
            **binding(layout, manifest, job, 3),
            "strategy_sha256": artifact_hash(strategy),
            "baseline_map_sha256": read_frozen(layout, manifest, "baseline_map")["sha256"],
        },
        "used_evidence_refs": [ev_role, ev_bar, ev_core, ev_edu, ev_other],
        "cv": json.loads(json.dumps(cv)),
        "letter": json.loads(json.dumps(letter)),
        "writer_note": "Strammet åpningen og spisset overskriften mot utlysningen.",
        "finalization": {"state": "DRAFT", "document_date": None,
                         "finalized_at": None, "finalized_by": None},
    }
    final["cv"]["headline"] = "Beslutningsstøtte for økonomi og aktivitet"
    final["letter"]["opening"] = (
        "Dere beskriver et kjent problem: dataene finnes, men de blir ikke til "
        "beslutningsgrunnlag. Det er den oppgaven jeg har arbeidet med de siste "
        "årene i Analyseavdelingen ved Oslo universitetssykehus."
    )
    atomic_write_json(out / "final_package.json", final)

    # ---------------- review ----------------
    review = {
        "artifact_role": "OPERATOR_TRIAGE",
        "binding": {
            "run_id": manifest["run_id"],
            "job_id": job["job_id"],
            "final_package_sha256": artifact_hash(final),
        },
        "triage": "CHECK",
        "reasons": [
            {"reason": "Utlysningen nevner prognosearbeid; pakken dekker det bare indirekte.",
             "recommended_action": "Bekreft om prognoseerfaringen er sterk nok til å nevnes.",
             "priority": 1},
            {"reason": "Kontaktperson og frist er ikke omtalt i brevet.",
             "recommended_action": "Vurder én setning om frist dersom det er ønskelig.",
             "priority": 2},
        ],
        "known_limitations": [
            "Ingen dokumentert erfaring med prognosemodeller ut over "
            "budsjettarbeid.",
        ],
        "material_strategy_change": "Overskriften ble spisset fra generisk til rollenær.",
        "upstream_claim_repaired": None,
    }
    atomic_write_json(out / "review.json", review)

    print(f"Fixtures written to {out}")
    for path in sorted(out.glob("*.json")):
        print(f"  {path.name:28s} {path.stat().st_size:6d} B")
    print("\nEvidence references used:")
    for label, ref in (("role", ev_role), ("bar", ev_bar), ("core", ev_core),
                       ("edu", ev_edu), ("other", ev_other)):
        print(f"  {label:6s} {ref}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    layout = Layout.discover(Path(__file__).resolve().parents[2])
    out = Path(args.out) if args.out else layout.evidence / "vertical_slice" / "fixtures"
    build(layout, args.run, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
