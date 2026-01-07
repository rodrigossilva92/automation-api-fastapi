from sqlmodel import create_engine, Session

from app.core import paths


DATABASE_URL = f"sqlite:///{paths.PLANNER_DATABASE}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def get_session():
    with Session(engine) as session:
        yield session
