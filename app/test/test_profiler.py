import pytest
from app.models.dataclass_models import PersonalInfoDataClass
from app.profiler import Profiler

@pytest.fixture
def default_personal_info_data(request) -> PersonalInfoDataClass:
    age = getattr(request, 'param', {}).get('age', 35)
    dependents = getattr(request, 'param', {}).get('dependents', 2)
    house = getattr(request, 'param', {}).get('house', {"ownership_status": "owned"})
    income = getattr(request, 'param', {}).get('income', 0)
    marital_status = getattr(request, 'param', {}).get('marital_status', "married")
    risk_questions = getattr(request, 'param', {}).get('risk_questions', [0, 1, 0])
    vehicle = getattr(request, 'param', {}).get('vehicle', {"year": 2018})
    
    return PersonalInfoDataClass(
        age=age,
        dependents=dependents,
        house=house,
        income=income,
        marital_status=marital_status,
        risk_questions=risk_questions,
        vehicle=vehicle
    )



@pytest.fixture
def default_profiler(default_personal_info_data) -> Profiler:
    return Profiler(personal_info=default_personal_info_data)

risk_questions_combinations = [
    ([0, 0, 0], 0),
    ([1, 0, 0], 1),
    ([0, 1, 1], 2),
    ([1, 1, 1], 3)
]


@pytest.mark.parametrize("default_personal_info_data", 
                         [{"risk_questions": [1, 0, 1]}], 
                         indirect=True)
def test_profiler_calulates_base_score(default_profiler):
    assert default_profiler.calc_base_score() == 2
