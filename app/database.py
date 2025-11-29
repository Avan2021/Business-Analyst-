import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()


def _build_connection_string() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///./sales.db")


DATABASE_URL = _build_connection_string()

# Configure connection arguments based on database type
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    # For PostgreSQL (including Supabase), configure SSL if needed
    connect_args = {}
    # If sslmode is in the URL, psycopg2 will handle it automatically
    # For Supabase, ensure we're using psycopg2 driver
    if "postgresql://" in DATABASE_URL and "+psycopg2" not in DATABASE_URL:
        # Replace postgresql:// with postgresql+psycopg2:// for explicit driver
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

engine = create_engine(DATABASE_URL, echo=False, future=True, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

