from datetime import date
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, Depends
from sqlmodel import Session

from app.models.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
)
from app.api.dependencies import get_current_user_id
from app.services.task import TaskService
from app.core.database import get_session


router = APIRouter()

task_service = TaskService()
    

@router.post("", response_model=TaskResponse, status_code=201)
def create_task(
    task: TaskCreate,
    session: Session = Depends(get_session),
    user_id: UUID = Depends(get_current_user_id),
):
    return task_service.create(session, user_id, task)


@router.get("", response_model=list[TaskResponse])
def list_tasks(
    task_date: date | None = Query(default=None),
    session: Session = Depends(get_session),
    user_id: UUID = Depends(get_current_user_id),
):
    return task_service.list(session, user_id, task_date)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: UUID,
    session: Session = Depends(get_session),
    user_id: UUID = Depends(get_current_user_id),
):
    task = task_service.get(session, user_id, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: UUID, data: TaskUpdate,
    session: Session = Depends(get_session),
    user_id: UUID = Depends(get_current_user_id),
):
    task = task_service.update(session, user_id, task_id, data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: UUID,
    session: Session = Depends(get_session),
    user_id: UUID = Depends(get_current_user_id),
):
    if not task_service.delete(session, user_id, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
