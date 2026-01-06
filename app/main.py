# app/main.py

from fastapi import FastAPI

from app.core.config import settings
from app.api.routes import router as task_router


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(task_router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": f"Welcome to {settings.app_name}!"}


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }
