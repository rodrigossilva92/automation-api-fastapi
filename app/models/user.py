from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime
