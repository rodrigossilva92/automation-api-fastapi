# app/api/routes.py

from fastapi import APIRouter, BackgroundTasks, HTTPException
from uuid import UUID

from app.models.schemas import (
    TaskCreate,
    TaskResponse,
    TaskResult,
)
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

task_service = TaskService()


@router.post("", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    background_tasks: BackgroundTasks,
):
    task_id = task_service.create_task()

    background_tasks.add_task(
        task_service.execute_task,
        task_id,
        task.payload,
    )

    return TaskResponse(
        task_id=task_id,
        status="pending",
    )


@router.get("/{task_id}", response_model=TaskResponse)
def get_task_status(task_id: UUID):
    task = task_service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return TaskResponse(
        task_id=task_id,
        status=task["status"],
    )


@router.get("/{task_id}/result", response_model=TaskResult)
def get_task_result(task_id: UUID):
    task = task_service.get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task["status"] != "completed":
        raise HTTPException(
            status_code=400,
            detail="Task not completed yet",
        )

    return TaskResult(
        task_id=task_id,
        result=task["result"],
    )
