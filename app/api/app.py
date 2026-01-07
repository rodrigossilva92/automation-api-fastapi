# app/main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel

from app.core.config import settings
from app.api.routes.basic import router as basic_router
from app.api.routes.tasks import router as task_router
from app.api.routes.auth import router as auth_router
from app.core.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    SQLModel.metadata.create_all(engine)
    yield
    # Shutdown logic here (if needed)


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan,
)

app.include_router(basic_router, tags=["Basic"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
