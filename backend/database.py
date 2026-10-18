import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Override with the DATABASE_URL environment variable (see .env.example).
# The default matches the database started by docker-compose.yml.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:admin@localhost:5432/ragdb",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


def get_db():
    """FastAPI dependency: yield a session and always close it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
