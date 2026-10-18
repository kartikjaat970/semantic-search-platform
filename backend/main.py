import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

import models.document  # noqa: F401  (registers the table on Base.metadata)
from database import Base, engine
from routes.search import router as search_router
from routes.upload import router as upload_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # The extension must exist before a Vector column can be created.
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Semantic Search Platform", lifespan=lifespan)

origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(search_router)


@app.get("/")
def root():
    return {"status": "ready"}
