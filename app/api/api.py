from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
from app.models.pydantic_models import PersonalInfoPayloadModel
from app.services.profiler import Profiler

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
    risk_score = Profiler.calc_risk_score(personal_info)
    return {
        "status": "success",
        "risk_score": risk_score
    }
    """
    

    sync return something like the following:
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


    
