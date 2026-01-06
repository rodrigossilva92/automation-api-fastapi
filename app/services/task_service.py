# app/services/task_service.py

from uuid import uuid4, UUID
from typing import Dict, Any
import time

from app.models.schemas import TaskStatus
from app.storage.memory import task_storage


class TaskService:
    def create_task(self) -> UUID:
        task_id = uuid4()
        task_storage.create_task(task_id)
        return task_id

    def execute_task(self, task_id: UUID, payload: Dict[str, Any]) -> None:
        try:
            task_storage.set_status(task_id, TaskStatus.running)

            # Simulate processing time
            time.sleep(2)

            # Example business logic
            values = payload.get("values", [])
            result = {
                "count": len(values),
                "sum": sum(values),
            }

            task_storage.set_result(task_id, result)

        except Exception as exc:
            task_storage.set_status(task_id, TaskStatus.failed)
            raise exc

    def get_task(self, task_id: UUID) -> Dict[str, Any] | None:
        return task_storage.get_task(task_id)
