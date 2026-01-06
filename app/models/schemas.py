# app/models/schemas.py

from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, Dict
from uuid import UUID


class TaskStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class TaskCreate(BaseModel):
    task_type: str = Field(..., example="data_processing")
    payload: Dict[str, Any]


class TaskResponse(BaseModel):
    task_id: UUID
    status: TaskStatus


class TaskResult(BaseModel):
    task_id: UUID
    result: Dict[str, Any]
