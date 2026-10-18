from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routers import users, addresses


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Development only: create tables if they don't exist.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="FastAPI Async SQLAlchemy",
    version="1.0.0",
    lifespan=lifespan,
)

# app.include_router(users.router)
# app.include_router(addresses.router)

app.include_router(users.user_router)


@app.get("/")
async def root():
    return {"message": "FastAPI application is running"}