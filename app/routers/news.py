from fastapi import APIRouter

router = APIRouter()

@router.get("", summary="News list endpoint")
def news_list():
    return {"detail": "This is the news list."}