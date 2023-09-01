# FastAPI Base App
[![pytest](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml)

Refer to README_original.md for the original README and project requirements by [Origin Financial](https://www.useorigin.com/).

**Purpose**: Good practice with translating requirements into an API endpoint with basic modular and extensible functionality.

An opportunity to use my personal FastAPI template.

**Audience**: Anyone interested in FastAPI/Pydantic projects.


## Design
* API endpoints
  * `GET /api/`; returns "about" message
  * `POST /api/risk_profile`; for example payload, see original readme
* Profiler: two possible approaches:
  * 1) stateful profile, implement using "build" pattern. Useful in conjunction with persistence.
  * 2) provider of functionaltiy, not stateful for individual profiles. A related collection of static methods, with some class variables.
  * Given the requirement for only a completely deterministic, rule-based API response, and no specified persistence, we'll implement approach number 2.
* Profiler implementation:
  * separate static methods for each profiling step: `base score` (0-3), `risk_score` (pos/neg increments), and `final_score` ("economic", "regular", "irresponsible").
  * each method used for scoring will have a name with prefix `calc_score_`, and Runner (TODO write about) will dynamically during runtime call all these methods on `personal_info`. That way new scoring methods will automatically be run if they are named by the prefix.
  * benefits to **modularity, testing, maintainability, extensibility**: changes to any step are made in that function; testing is easier because the functions will be pure, i,e. have no side effects;  each step can be modified, expanded, or removed, or new steps added.
* `class RiskScore`:
  * will have `insurance lines` field, because the knowledge of insurance lines is inherently part of the risk score. 



## Usage local

```
pip install -r requirements.txt
```
```
uvicorn app.main:app --reload
```
```
pytest app/test.py
```
```
docker-compose up -d --build
```
```
docker-compose exec app pytest test/test.py
```

## API Documentation (Swagger UI)

```
http://127.0.0.1:8000/docs
```


## TODOs
* `POST /risk_profile`: add param for "line": ("auto", "disability", "home", "life")
* add `logging`
* ? make enums for `INSURANCE_LINES` and `FINAL_SCORES`
* extract into class var the 'finalize' thresholds,  `view_final` should just have dict comprehension
