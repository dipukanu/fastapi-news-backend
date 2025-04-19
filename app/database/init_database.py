from app.database.session import Base, engine
from app import models


# Initializes the database by creating tables based on the defined models.
def init_db():
    Base.metadata.create_all(bind=engine)
