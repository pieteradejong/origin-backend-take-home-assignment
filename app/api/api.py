from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return { "message" : "This is a risk assessment API." }

@router.post("/risk_profile")
def risk_profile():
    return { "message" : "This will return a risk assessment." }

