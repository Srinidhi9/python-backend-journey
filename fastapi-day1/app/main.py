from fastapi import FastAPI
from app.database import engine
from app import models
from app.auth import router as auth_router

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include auth routes
app.include_router(auth_router)

# Root route
@app.get("/")
def home():
    return {"message": "FastAPI Job Tracker API is running"}