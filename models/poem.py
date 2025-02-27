from turtle import position

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Verse(Base):
    __tablename__ = "verse"

    poem_id = Column(Integer)
    vorder = Column(Integer)
    position = Column(Integer)
    text = Column(String, primary_key=True, index=True)


class VerseResponse(BaseModel):
    vorder: int
    text: str

    class Config:
        orm_mode = True  # Allows conversion from ORM object to Pydantic model
        from_attributes = True


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
