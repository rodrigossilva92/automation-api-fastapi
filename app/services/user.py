from sqlmodel import select
from sqlmodel import Session

from app.core.security import hash_password
from app.models.db import User
from app.models.user import UserCreate


class UserService:
    
    def create(self, session: Session, data: UserCreate) -> User:
        existing = session.exec(
            select(User).where(User.email == data.email)
        ).first()

        if existing:
            raise ValueError("Email already registered")

        user = User(
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get_by_email(self, session: Session, email: str) -> User | None:
        return session.exec(
            select(User).where(User.email == email)
        ).first()


user_service = UserService()
