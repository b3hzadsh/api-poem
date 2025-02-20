from pydantic import BaseModel, ConfigDict


class Verse(BaseModel):
    text: str
    position: int
    vorder: int


class VerseIn(Verse):
    poem_id: int

    model_config = ConfigDict(from_attributes=True)


class Poem(BaseModel):
    title: str


class PoemIn(Poem):
    id: int
    cat_id: int

    model_config = ConfigDict(from_attributes=True)
