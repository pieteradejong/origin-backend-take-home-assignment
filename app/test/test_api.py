from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
"""

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {
        "status": "success",
        "message": "This is a risk assessment API.",
    }


def test_risk_profile():
    headers = {"Content-Type": "application/json"}
    payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": [{"year": 2018}],
    }

    response = client.post("/risk_profile", headers=headers, json=payload)

    assert response.status_code == 200
    expected_response = {
        "status": "success",
        "risk_score": {
            "auto": "regular",
            "disability": "ineligible",
            "home": "economic",
            "life": "regular",
        },
    }
    assert response.json() == expected_response
"""
