from app.database.session import engine
from app.models import news

# Initializes the database by creating tables based on the defined models.
def init_db():
    news.Base.metadata.create_all(bind=engine)
