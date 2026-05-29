from fastapi import FastAPI

from app.database import engine
from app import models
from app.auth import router as auth_router

app = FastAPI(
    title="FastAPI Authentication API"
)

models.Base.metadata.create_all(
    bind=engine
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "project": "FastAPI Authentication API",
        "status": "running",
        "docs": "/docs"
    }