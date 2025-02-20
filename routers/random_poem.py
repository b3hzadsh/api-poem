import random

from fastapi import APIRouter, HTTPException
from returns.pipeline import is_successful
from returns.result import Failure, Result, Success

from database_m import database, max_poem_id, min_poem_id, poems_table
from models.poem import Poem, PoemIn, Verse

# router = APIRouter()


# async def find_random_poem() -> dict:
#     rand_num = random.randint(min_poem_id, max_poem_id)
#     print(f"{rand_num=}")
#     poem_id = rand_num
#     query = poems_table.select().where(poems_table.c.id == poem_id)
#     try:
#         poem_dict = await database.fetch_one(query)
#         poem: dict = poem_dict.__dict__
#         print(f"{poem=}")
#         return poem
#     except Exception as e:
#         raise Exception("failure happend with this exception {}".format(e))


# @router.get("/random-poem", response_model=PoemIn)
# async def random_poem():
#     return await find_random_poem()


router = APIRouter()


async def fetch_poem_by_id(poem_id: int) -> Result[dict, str]:
    """Fetch a poem by its ID from the database."""
    query = poems_table.select().where(poems_table.c.id == poem_id)
    poem = await database.fetch_one(query)
    if poem:
        return Success(poem.__dict__)  # Convert to dict for better compatibility
    return Failure(f"Poem with ID {poem_id} not found.")


async def find_random_poem() -> dict:
    """Find a random poem within the given ID range."""
    rand_num = random.randint(min_poem_id, max_poem_id)
    result = await fetch_poem_by_id(rand_num)

    if is_successful(result):
        return result.unwrap()
    else:
        # If the poem is not found, try again recursively (with a limit to avoid infinite loops)
        if rand_num < max_poem_id:
            return await find_random_poem()
        raise HTTPException(status_code=404, detail="No poems available.")


@router.get("/random-poem", response_model=PoemIn)
async def random_poem():
    """Endpoint to fetch a random poem."""
    try:
        poem = await find_random_poem()
        return poem
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
