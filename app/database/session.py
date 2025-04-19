from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Create a configured "SessionLocal" class to manage DB sessions
engine = create_engine(settings.database_url, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for creating database models
Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
