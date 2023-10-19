import pytest
from app.services.risk_score import RiskScore


@pytest.fixture
def risk_score():
    risk_score = RiskScore()
    yield risk_score
    del risk_score


@pytest.mark.parametrize(
    "score, expected_final",
    [
        ("ineligible", "ineligible"),
        (0, "economic"),
        (-1, "economic"),
        (1, "regular"),
        (2, "regular"),
        (3, "responsible"),
        (4, "responsible"),
    ],
)
def test_calc_final(score, expected_final, risk_score):
    result = risk_score.calc_final(score)
    assert result == expected_final


def test_baseline_score_as_numeric():
    risk_score_service = RiskScore()
    expected_result = {"auto": 0, "disability": 0, "home": 0, "life": 0}
    result = risk_score_service.risk_score
    assert result == expected_result


@pytest.mark.parametrize(
    "increments, expected",
    [
        ({"auto": 1}, {"auto": 1, "disability": 0, "home": 0, "life": 0}),
        ({"disability": 1}, {"auto": 0, "disability": 1, "home": 0, "life": 0}),
        ({"home": 1}, {"auto": 0, "disability": 0, "home": 1, "life": 0}),
        ({"life": 1}, {"auto": 0, "disability": 0, "home": 0, "life": 1}),
        (
            {"auto": "ineligible"},
            {"auto": "ineligible", "disability": 0, "home": 0, "life": 0},
        ),
    ],
)
def test_risk_score_update(increments, expected, risk_score):
    risk_score.risk_score_update(increments)
    assert risk_score.risk_score == expected


@pytest.mark.parametrize(
    "increments, expected_result",
    [
        (
            {"auto": 1, "disability": 2, "home": 3, "life": 4},
            {"auto": 1, "disability": 2, "home": 3, "life": 4},
        ),
        (
            {"auto": "ineligible", "disability": 2, "home": 3, "life": 4},
            {"auto": "ineligible", "disability": 2, "home": 3, "life": 4},
        ),
    ],
)
def test_risk_score_update_multiple_insurance_lines(
    increments, expected_result, risk_score
):
    risk_score.risk_score = increments
    assert risk_score.risk_score == expected_result


def test_ineligible_score_is_irreversible(risk_score):
    expected = "ineligible"

    ineligible_input = {"auto": "ineligible"}
    subsequent_input = {"auto": 2}

    risk_score.risk_score_update(ineligible_input)
    risk_score.risk_score_update(subsequent_input)

    assert risk_score.view_final()["auto"] == expected
