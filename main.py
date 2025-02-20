from contextlib import asynccontextmanager

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI

from database_m import database
from models.poem import Poem, Verse
from routers.random_poem import router as random_poem_router


@asynccontextmanager
async def life_span(app: FastAPI):
    db_connection_result = await database.connect()
    print(f"{db_connection_result=}")
    yield
    await database.disconnect()


app = FastAPI(lifespan=life_span)


app.include_router(random_poem_router)
