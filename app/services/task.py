from datetime import datetime, date
from uuid import UUID

from sqlmodel import select, Session

from app.models.db import Task
from app.models.task import TaskCreate, TaskUpdate


class TaskService:
    def create(self, session: Session, user_id: UUID, data: TaskCreate) -> Task:
        task = Task(
            user_id=user_id,
            title=data.title,
            description=data.description,
            date=data.date,
            priority=data.priority,
        )

        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    def list(
        self,
        session: Session,
        user_id: UUID,
        task_date: date | None = None,
    ) -> list[Task]:
        stmt = select(Task).where(Task.user_id == user_id)

        if task_date:
            stmt = stmt.where(Task.date == task_date)

        return session.exec(stmt).all()

    def get(self, session: Session, user_id: UUID, task_id: UUID) -> Task | None:
        return session.exec(
            select(Task)
            .where(Task.id == task_id, Task.user_id == user_id)
        ).first()

    def update(
        self,
        session: Session,
        user_id: UUID,
        task_id: UUID,
        data: TaskUpdate,
    ) -> Task | None:
        task = self.get(session, user_id, task_id)
        if not task:
            return None

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(task, field, value)

        task.updated_at = datetime.utcnow()
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    def delete(self, session: Session, user_id: UUID, task_id: UUID) -> bool:
        task = self.get(session, user_id, task_id)
        if not task:
            return False

        session.delete(task)
        session.commit()
        return True


task_service = TaskService()
