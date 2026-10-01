from jobbsok.signals import inspect_package


def test_formula_signals_are_advisory_and_located():
    package = {
        "cv": {"headline": "Jeg søker jobb", "profile": "Jeg bygger rapporter", "competencies": [], "employment_overrides": []},
        "letter": {
            "opening": "Jeg søker stillingen som rådgiver fordi jeg liker analyse.",
            "body_paragraphs": ["Dette arbeidet ble avviklet.", "Jeg kan ta med erfaringen inn i rollen."],
            "closing": "Jeg ser frem til å høre fra dere.",
        },
    }
    codes = {item["code"] for item in inspect_package(package, title="rådgiver")}
    assert {"cv_first_person", "seeker_because", "title_restatement", "avviklet_ending", "stock_close"} <= codes


def test_no_formula_signal_changes_content():
    package = {"cv": {"headline": "Analytiker", "profile": "Bygger rapporter", "competencies": [], "employment_overrides": []},
               "letter": {"opening": "Jeg har utviklet beslutningsgrunnlag i sykehus.", "body_paragraphs": [], "closing": "Jeg tar gjerne en samtale."}}
    before = repr(package)
    assert inspect_package(package, title="rådgiver") == []
    assert repr(package) == before


def test_first_person_in_effective_baseline_bullets_is_seen():
    package = {"cv": {"headline": "Analytiker", "profile": "Rådgiver", "competencies": [], "employment_overrides": []},
               "letter": {"opening": "Arbeidet gjelder rapporter.", "body_paragraphs": [], "closing": "Samtale ønskes."}}
    effective = {"employments": [{"bullets": ["Jeg laget rapporten."]}]}
    assert any(item["code"] == "cv_first_person" for item in inspect_package(package, effective_cv=effective))


def test_stock_close_detects_opportunity_to_elaborate_formula():
    package = {"cv": {}, "letter": {"opening": "Åpning", "body_paragraphs": [],
                                 "closing": "Jeg ser frem til muligheten til å utdype hvordan erfaringen min kan bidra."}}
    assert any(item["code"] == "stock_close" for item in inspect_package(package))
