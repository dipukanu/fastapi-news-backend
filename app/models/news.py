from sqlalchemy import Column, String, DateTime, Integer
from app.database.session import Base


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    url = Column(String, unique=True)
    source = Column(String)
    country = Column(String)
    published_at = Column(DateTime)
