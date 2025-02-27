import random
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from returns.pipeline import is_successful
from returns.result import Failure, Result, Success
from sqlalchemy.orm import Session

from database import get_db, max_poem_id, min_poem_id
from models.poem import Poem, PoemResponse, Verse, VerseResponse

router = APIRouter()


async def fetch_poem_by_id(
    poem_id: int,
    db: Session,
) -> Result[PoemResponse, str]:
    db_poem = db.query(Poem).filter(Poem.id == poem_id).first()
    if not db_poem:
        Failure("Poem not found")
    return Success(PoemResponse.model_validate(db_poem))


async def find_random_poem(db: Session) -> dict:
    """Find a random poem within the given ID range."""
    rand_num = random.randint(min_poem_id, max_poem_id)
    result = await fetch_poem_by_id(rand_num, db)

    if is_successful(result):
        return result.unwrap().model_dump()
    else:
        raise HTTPException(status_code=404, detail="No poems available.")


@router.get("/random-poem", response_model=list[VerseResponse])
async def random_poem(db: Annotated[Session, Depends(get_db)]):
    """Endpoint to fetch a random poem."""
    try:
        poem = await find_random_poem(db)
        list_verse = db.query(Verse).filter(Verse.poem_id == poem["id"]).all()
        list_verse_response = []
        for verse in list_verse:
            list_verse_response.append(VerseResponse.model_validate(verse))
        print(f"{list_verse_response=}")
        return list_verse_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
