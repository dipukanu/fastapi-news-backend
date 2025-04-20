import logging

import requests
from sqlalchemy.orm import Session

from app.config import settings
from app.models.news import News


logger = logging.getLogger(__name__)


def get_news(
    country: str = None, source: str = None, page: int = 1, page_size: int = 10
):
    if country and source:
        # NewsAPI limitation: cannot filter by both at the same time
        raise ValueError(
            "Cannot filter by both country and source due to API limitations."
        )

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": settings.news_api_key,
        "page": page,
        "pageSize": page_size,
    }

    if country:
        params["country"] = country
    if source:
        params["sources"] = source

    response = requests.get(url, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Return cleaner error messages
        raise ValueError(f"News API error: {response.json().get('message', str(e))}")

    return response.json()


def save_top_3_news_to_db(db: Session, country: str = "us"):
    try:
        news_data = get_news(country=country, page_size=3)
        for article in news_data["articles"]:
            if not db.query(News).filter(News.url == article["url"]).first():
                db_news = News(
                    title=article["title"],
                    description=article.get("description"),
                    url=article["url"],
                    source=article.get("source", {}).get("name"),
                    country=country,
                    published_at=article.get("publishedAt"),
                )
                db.add(db_news)
        db.commit()
        logger.info("Top 3 news articles saved to DB successfully.")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        db.rollback()
