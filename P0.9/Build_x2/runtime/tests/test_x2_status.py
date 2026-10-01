from jobbsok import artifacts, status
from jobbsok.validate import RunContext


def test_status_formula_warning_does_not_change_triage(staged):
    layout, run_id, manifest, job_id, fixture_dir = staged
    context = RunContext(layout, manifest)
    before = next(j for j in status.derive(layout, manifest, context=context)["jobs"] if j["job_id"] == job_id)
    final = artifacts.load(layout, run_id, job_id, "final_package")
    review = artifacts.load(layout, run_id, job_id, "review")
    final["cv"]["headline"] = "Jeg er analytiker"
    replacement = artifacts.submit(layout, run_id, job_id, stage=3, artifact="final_package",
                                   payload=final, timestamp="20260823T070000Z")
    assert replacement.ok
    review["binding"]["final_package_sha256"] = artifacts.artifact_hash(final)
    replacement = artifacts.submit(layout, run_id, job_id, stage=3, artifact="review",
                                   payload=review, timestamp="20260823T070001Z")
    assert replacement.ok
    after = next(j for j in status.derive(layout, manifest, context=context)["jobs"] if j["job_id"] == job_id)
    assert after["semantic_triage"] == before["semantic_triage"]
    assert after["production_state"] == before["production_state"]
    assert any(w["code"] == "cv_first_person" for w in after["editorial_warnings"])
