from fastapi import FastAPI
from app.routers import news

app = FastAPI(title="News Aggregator API")

app.include_router(news.router, prefix="/api/v1/news", tags=["News Route"])
