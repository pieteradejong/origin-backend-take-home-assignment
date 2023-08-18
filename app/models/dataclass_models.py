from dataclasses import dataclass
from pydantic_models import OwnershipStatusPayloadEnum, MaritalStatusPayloadEnum
from typing import Optional, List, Literal

@dataclass
class RiskProfile:
    name: str
    age: int
    address: str
    occupation: Optional[str]


@dataclass
class HousePayloadDataClass:
    ownership_status: OwnershipStatusPayloadEnum

@dataclass
class MaritalStatusPayloadDataClass:
    marital_status: MaritalStatusPayloadEnum

@dataclass
class VehiclePayloadDataClass:
    year: int


@dataclass
class PersonalInfoDataClass:
    age: int
    dependents: int
    house: Optional[HousePayloadDataClass]
    income: int
    marital_status: MaritalStatusPayloadDataClass
    risk_questions: List[Literal[0, 1]]
    vehicle: Optional[VehiclePayloadDataClass]
