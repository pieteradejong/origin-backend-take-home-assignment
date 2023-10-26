from pydantic import BaseModel, conint, conlist
from typing import Literal, Optional
from enum import Enum


class OwnershipStatusPayloadEnum(Enum):
    OWNED = "owned"
    MORTGAGED = "mortgaged"


class HousePayloadModel(BaseModel):
    ownership_status: OwnershipStatusPayloadEnum


# class MaritalStatusPayloadEnum(Enum):
#     SINGLE = "single"
#     MARRIED = "married"

# class MaritalStatusPayloadModel(BaseModel):
#     marital_status: MaritalStatusPayloadEnum


class VehiclePayloadModel(BaseModel):
    year: conint(ge=1885, le=2100)


class PersonalInfoPayloadModel(BaseModel):
    age: conint(ge=0, le=200)
    dependents: conint(ge=0)
    house: Optional[HousePayloadModel]
    income: conint(ge=0)
    # marital_status: MaritalStatusPayloadModel
    marital_status: Literal["single", "married"]
    risk_questions: conlist(conint(ge=0, le=1), min_items=3, max_items=3)
    vehicle: Optional[VehiclePayloadModel]
