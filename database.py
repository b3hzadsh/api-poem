from typing import Generator

import sqlalchemy
from pytest import Session
from sqlalchemy.orm import Session, sessionmaker

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./khayam.sqlite3"

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get DB session
def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


min_poem_id = 1119
max_poem_id = 1296
