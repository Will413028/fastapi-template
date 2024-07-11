from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alembic import command
from alembic.config import Config
from src.config import settings

if settings.MODE == "dev":
    engine = create_engine(settings.DATABASE_URL, echo=True)
else:
    engine = create_engine(settings.DATABASE_URL, pool_size=100, max_overflow=50, pool_recycle=300)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
