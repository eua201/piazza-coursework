#Adapted from Week 4 of Labs class-4/solutions/auth-api
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/database.py
#Changes: location now comes from an environment variable with a default, and the parent folder is created if missing.
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DEFAULT_DB_PATH = Path(__file__).resolve().parent / "piazza.db"

#Reading the path from an environment variable with a fallback default
# follows the approach in Python Environment Variables: os.environ Guide & Examples,OpenPython
# https://openpython.org/articles/python-environment-variables-os-environ
# (accessed 17 Nov 2026)

DATABASE_PATH = Path(os.getenv("DATABASE_PATH",DEFAULT_DB_PATH)).resolve()

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()