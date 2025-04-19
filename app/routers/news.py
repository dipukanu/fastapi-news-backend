from fastapi import APIRouter, Depends, Query

from app.auth.dependencies import get_current_client
from app.services.news import get_news
from app.schemas.news import NewsListResponse

router = APIRouter(prefix="/api/v1/news", tags=["News"])


@router.get(
    "",
    response_model=NewsListResponse,
    summary="Fetch all news with pagination",
)
def news_list(
    current_client: str = Depends(get_current_client),
    country: str = Query(
        "us", min_length=2, max_length=2, description="2‑letter country code"
    ),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
):
    """
    Returns paginated top headlines from NewsAPI.
    """
    return get_news(country=country, page=page, page_size=page_size)
