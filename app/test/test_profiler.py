import pytest
from app.services.profiler import Profiler
from app.models.dataclass_models import PersonalInfoDataClass


@pytest.fixture
def default_personal_info() -> PersonalInfoDataClass:
    # def default_personal_info_data(request) -> PersonalInfoDataClass:
    default_params = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }
    # params = {**default_params, **getattr(request, "param", {})}
    params = {**default_params}

    return PersonalInfoDataClass(**params)


@pytest.fixture
def profiler():
    profiler = Profiler()
    yield profiler
    del profiler


def test_profiler_initialization(profiler):
    assert isinstance(profiler, Profiler), "Profiler instance not created"


"""
# TODO: was trying to generate large set of test data.
# But instead, each criteria should be tested individually based off a default.
# the inputs should be base_score and personal_info_data_default, and each user property
# should be tested individually
"""
"""
def generate_test_data(personal_info_data_default):
    AGE_VARIATIONS = [25, 35, 60]
    INCOME_VARIATIONS = [50_000, 100_000, 250_000]

    test_data = []
    for age in AGE_VARIATIONS:
        for income in INCOME_VARIATIONS:
            test_data.append(
                (
                    replace(personal_info_data_default, age=age, income=income),
                    # You'd need to define how you determine the expected score:
                    # TODO get_expected_risk_score is not defined
                    # get_expected_risk_score(age, income),
                )
            )

    return test_data
"""
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
