from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List, Optional

class Article(BaseModel):
    title: str
    description: Optional[str]
    url: HttpUrl
    publishedAt: datetime

class NewsListResponse(BaseModel):
    status: str
    totalResults: int
    articles: List[Article]
