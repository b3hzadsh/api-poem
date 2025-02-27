from contextlib import asynccontextmanager

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI

from database import SessionLocal, engine
from models.poem import Poem, Verse
from routers.random_poem import router as random_poem_router

app = FastAPI()


app.include_router(random_poem_router)
