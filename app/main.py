from fastapi import FastAPI

from app.api import api


app = FastAPI()
app.include_router(api.router)


@app.on_event("startup")
async def startup_event():
    print("Starting application...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down application...")

