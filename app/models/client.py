from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, unique=True, nullable=False, index=True)
    client_secret = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
