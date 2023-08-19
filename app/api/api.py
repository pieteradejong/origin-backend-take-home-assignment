from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
from app.models.pydantic_models import PersonalInfoPayloadModel

router = APIRouter()

class SuccessResponse(BaseModel):
    status: Literal["success"]
    message: str

@router.get("/", response_model=SuccessResponse, status_code=200)
def root():
    return {
        "status": "success",
        "message": "This is a risk assessment API."
    }

@router.post("/risk_profile")
def risk_profile(personal_info: PersonalInfoPayloadModel):
    pass
    # TODO: grab payload and pass to risk module
    # e.g. risk_profile = Profiler.assess(payload)

    """
    return something like the following:
    {
        "status": "success",
        "risk_score": {
            "auto": "regular",
            "disability": "ineligible",
            "home": "economic",
            "life": "regular"
        }
    }
    """


    return {
        "status": "success",
        "message": "This will return a risk assessment."
    }
