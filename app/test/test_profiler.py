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


"""
Should test the following ineligiblity scenarios:
- income=0 -> ineligible for disability (already tested)
- vehicles=None -> auto
- house=None -> home
- age >60 -> disability, life
"""
