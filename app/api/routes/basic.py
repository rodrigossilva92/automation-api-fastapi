from fastapi import APIRouter

from app.core.config import settings


router = APIRouter()


@router.get("/")
def read_root():
    return {"message": f"Welcome to {settings.app_name}!"}


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }
