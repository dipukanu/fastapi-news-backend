from fastapi import FastAPI

from app.database.init_database import init_db
from app.routers import client, news, auth

app = FastAPI(title="News Aggregator API")


@app.on_event("startup")
def on_startup():
    # This will create tables (clients, news, etc.) on every app startup.
    init_db()


app.include_router(auth.router)
app.include_router(client.router)
app.include_router(news.router)
