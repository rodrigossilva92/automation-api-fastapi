from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import select, Session

from app.models.user import UserCreate, UserResponse
from app.services.user import UserService
from app.core.security import verify_password, create_access_token
from app.core.database import get_session


router = APIRouter()

user_service = UserService()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    try:
        created_user = user_service.create(session, user)
        return created_user
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )


@router.post("/login")
def login(data: UserCreate, session: Session = Depends(get_session)):
    user = user_service.get_by_email(session, data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer",
    }