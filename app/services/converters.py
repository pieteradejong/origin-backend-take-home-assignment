from app.models.pydantic_models import *
from app.models.dataclass_models import *

def pydantic_to_dataclass(model: PersonalInfoPayloadModel) -> PersonalInfoDataClass:
    return PersonalInfoDataClass(
        age=model.age,
        dependents=model.dependents,
        house=HousePayloadDataClass(ownership_status=model.house.ownership_status) if model.house else None,
        income=model.income,
        marital_status=MaritalStatusPayloadDataClass(marital_status=model.marital_status.marital_status),
        risk_questions=model.risk_questions,
        vehicle=VehiclePayloadDataClass(year=model.vehicle[0].year) if model.vehicle else None
    )
