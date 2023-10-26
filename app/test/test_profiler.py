import pytest
from app.services.profiler import Profiler
from app.models.dataclass_models import PersonalInfoDataClass
from app.models.pydantic_models import (
    OwnershipStatusPayloadEnum,
    HousePayloadModel,
    VehiclePayloadModel,
)


@pytest.fixture
def personal_info():
    # Do not modify; tested as default profile below.
    default_test_case = {
        "age": 35,
        "dependents": 2,
        "house": HousePayloadModel(ownership_status=OwnershipStatusPayloadEnum.OWNED),
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": VehiclePayloadModel(year=2018),
    }
    # (End of) Do not modify.
    personal_info = PersonalInfoDataClass(**default_test_case)
    yield personal_info
    del personal_info


@pytest.fixture
def profiler():
    profiler = Profiler()
    yield profiler
    del profiler


def test_profiler_initialization(profiler):
    assert isinstance(profiler, Profiler), "Profiler instance not created"


def test_correct_default_score(profiler, personal_info):
    expected = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "economic",
        "life": "regular",
    }
    risk_score = profiler.calc_risk_score(personal_info)
    assert risk_score == expected


# def test_ineligible_scores(profiler, personal_info):
#     personal_info.income = 0
#     risk_score = profiler.calculate_risk_score(personal_info)
#     assert risk_score.risk_score["disability"] == "ineligible"


def test_ineligible_scores(profiler, personal_info):
    pass


"""
# TODO: test multiple combinations
risk_questions_combinations = [
    ({"risk_questions": [0, 0, 0]}, 0),
    ({"risk_questions": [1, 0, 0]}, 1),
    ({"risk_questions": [0, 1, 1]}, 2),
    ({"risk_questions": [1, 1, 1]}, 3),
]

risk_score_combinations = [
    ({"age": 25}, {"auto": -2, "disability": -2, "home": -2, "life": -2}),
    ({"age": 35}, {"auto": -1, "disability": -1, "home": -1, "life": -1}),
    ({"income": 250_000}, {"auto": -1, "disability": -1, "home": -1, "life": -1}),
    (
        {"house": {"ownership_status": OwnershipStatusPayloadEnum.MORTGAGED}},
        {"auto": 0, "disability": 1, "home": 1, "life": 0},
    ),
    ({"dependents": 1}, {"auto": 0, "disability": 1, "home": 0, "life": 1}),
    (
        {"marital_status": {"marital_status": MaritalStatus.MARRIED}},
        {"auto": 0, "disability": -1, "home": 0, "life": 1},
    ),
    # ... Add more combinations as required
]


# @pytest.mark.parametrize("default_personal_info_data",
#                          [{"risk_questions": [1, 0, 1]}],
#                          indirect=True)
# def test_profiler_calulates_base_score(default_profiler):
#     assert default_profiler.calc_base_score() == 2
@pytest.mark.parametrize(
    "default_personal_info_data, expected_sum",
    risk_questions_combinations,
    indirect=["default_personal_info_data"],
)
def test_profiler_calulates_base_score(default_personal_info_data, expected_sum):
    result = Profiler.calc_base_score(default_personal_info_data)
    assert result == expected_sum


# @pytest.mark.parametrize("default_personal_info_data, expected_risk_score",
#                          risk_score_combinations,
#                          indirect=["default_personal_info_data"])
# def test_calculate_risk_score(default_personal_info_data, expected_risk_score):
#     result = Profiler.calc_risk_score_by_insurance_line(default_personal_info_data)
#     assert result == expected_risk_score


@pytest.mark.parametrize(
    "default_personal_info_data, expected_risk_score",
    risk_score_combinations,
    indirect=["default_personal_info_data"],
)
def test_calculate_risk_score(default_personal_info_data, expected_risk_score):
    result = Profiler.calc_risk_score_by_insurance_line(default_personal_info_data)
    assert result == expected_risk_score
"""
