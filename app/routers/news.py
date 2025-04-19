from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_client
from app.database.session import get_db
from app.services.news import get_news, save_top_3_news_to_db
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


@router.post(
    "/save-latest",
    summary="Save top 3 news articles to the database",
)
def save_latest_news(
    country: str = Query("us"),
    db: Session = Depends(get_db),
    current_client: str = Depends(get_current_client),
):
    save_top_3_news_to_db(db, country=country)
    return {"message": "Top 3 news articles saved."}


@router.get(
    "/headlines/country/{country_code}",
    response_model=NewsListResponse,
    summary="Fetch top headlines by country",
)
def headlines_by_country(
    country_code: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    current_client: str = Depends(get_current_client),
):
    return get_news(country=country_code, page=page, page_size=page_size)


@router.get(
    "/headlines/source/{source_id}",
    response_model=NewsListResponse,
    summary="Fetch top headlines by source",
)
def headlines_by_source(
    source_id: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    current_client: str = Depends(get_current_client),
):
    return get_news(source=source_id, page=page, page_size=page_size)


@router.get(
    "/headlines/filter",
    response_model=NewsListResponse,
    summary="Fetch top headlines by country or source (not both)",
)
def filtered_headlines(
    country: str = Query(None, min_length=2, max_length=2),
    source: str = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    current_client: str = Depends(get_current_client),
):
    try:
        return get_news(country=country, source=source, page=page, page_size=page_size)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
