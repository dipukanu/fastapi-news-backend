import requests
from app.config import settings


def get_news(country: str = "us", page: int = 1, page_size: int = 10):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": settings.news_api_key,
        "page": page,
        "pageSize": page_size,
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()
