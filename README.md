# FastAPI Base App
[![pytest](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pieteradejong/fastapi-base/actions/workflows/ci.yml)

Refer to README_original.md for the original README and project requirements by [Origin Financial](https://www.useorigin.com/).

**Purpose**: Good practice with translating requirements into an API endpoint with basic modular and extensible functionality.

An opportunity to use my personal FastAPI template.

**Audience**: Anyone interested in FastAPI/Pydantic projects.


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

