from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./khayam.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# SQLAlchemy Model
class Poem(Base):
    __tablename__ = "poem"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer)
    title = Column(String)


# Pydantic Model
class PoemResponse(BaseModel):
    id: int
    cat_id: int
    title: str

    class Config:
        orm_mode = True  # Allows conversion from ORM object to Pydantic model
        from_attributes = True


# FastAPI app
app = FastAPI()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to get poem by ID
@app.get("/poems/{poem_id}", response_model=PoemResponse)
def get_poem(poem_id: int, db: Session = Depends(get_db)):
    db_poem = db.query(Poem).filter(Poem.id == poem_id).first()
    if not db_poem:
        raise HTTPException(status_code=404, detail="Poem not found")
    return db_poem
