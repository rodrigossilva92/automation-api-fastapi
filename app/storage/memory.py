# app/storage/memory.py

from typing import Dict, Any
from uuid import UUID
from app.models.schemas import TaskStatus


class InMemoryTaskStorage:

    def __init__(self) -> None:
        self._tasks: Dict[UUID, Dict[str, Any]] = {}

    def create_task(self, task_id: UUID) -> None:
        self._tasks[task_id] = {
            "status": TaskStatus.pending,
            "result": None,
        }

    def set_status(self, task_id: UUID, status: TaskStatus) -> None:
        self._tasks[task_id]["status"] = status

    def set_result(self, task_id: UUID, result: Dict[str, Any]) -> None:
        self._tasks[task_id]["result"] = result
        self._tasks[task_id]["status"] = TaskStatus.completed

    def get_task(self, task_id: UUID) -> Dict[str, Any]:
        return self._tasks.get(task_id)


task_storage = InMemoryTaskStorage()
