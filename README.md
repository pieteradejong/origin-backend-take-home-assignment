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
  * 1) Create individualized profile, implement using "build" pattern.
  * 2) Use Profiler as a provider of functionaltiy, but doesn't maintain state of any individual profile. E.g. just a collection/libarry of static methods.
  * Given the requirement to only give an immediate API response to a small json request, and there is no persistence requirement, we should probably stick to only providing functionality and NOT maintaining state for an individual profile. But might implement both for kicks.


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
* add `logging` library
* 
