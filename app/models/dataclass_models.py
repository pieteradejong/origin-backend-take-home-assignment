from dataclasses import dataclass
from app.models.pydantic_models import OwnershipStatusPayloadEnum
from typing import Optional, List, Literal
from enum import Enum


@dataclass
class RiskProfile:
    name: str
    age: int
    address: str
    occupation: Optional[str]


@dataclass
class HousePayloadDataClass:
    ownership_status: OwnershipStatusPayloadEnum


class MaritalStatus(Enum):
    SINGLE = "single"
    MARRIED = "married"


@dataclass
class MaritalStatusPayloadDataClass:
    marital_status: MaritalStatus


@dataclass
class VehiclePayloadDataClass:
    year: int


@dataclass
class PersonalInfoDataClass:
    age: int
    dependents: int
    house: Optional[HousePayloadDataClass]
    income: int
    # marital_status: MaritalStatusPayloadDataClass
    marital_status: MaritalStatus
    risk_questions: List[Literal[0, 1]]
    vehicle: Optional[VehiclePayloadDataClass]
