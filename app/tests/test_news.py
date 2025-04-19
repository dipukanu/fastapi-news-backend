from fastapi import status
from fastapi.testclient import TestClient

from unittest.mock import patch

from app.auth.dependencies import get_current_client
from app.main import app


# Override dependency
def override_get_current_client():
    return "test-user-id"


app.dependency_overrides[get_current_client] = override_get_current_client

client = TestClient(app)


# Mock response for test purpose
mock_response = {
    "status": "ok",
    "totalResults": 2,
    "articles": [
        {
            "title": "Test Title",
            "description": "Test Description",
            "url": "http://example.com/article1",
            "publishedAt": "2024-04-01T12:00:00Z",
        },
        {
            "title": "Another Title",
            "description": "Another Description",
            "url": "http://example.com/article2",
            "publishedAt": "2024-04-02T15:30:00Z",
        },
    ],
}


@patch("app.routers.news.get_news", return_value=mock_response)
def test_get_news_list(mock_get, client):
    response = client.get(
        "/api/v1/news", headers={"Authorization": "Bearer test-token"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert len(response.json()["articles"]) == 2


@patch("app.services.news.get_news", return_value=mock_response)
def test_country_headlines(mock_get, client):
    response = client.get(
        "/api/v1/news/headlines/country/us",
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 200


@patch("app.services.news.get_news", return_value=mock_response)
def test_source_headlines(mock_get, client):
    response = client.get(
        "/api/v1/news/headlines/source/bbc-news",
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 200


@patch("app.services.news.get_news", return_value=mock_response)
def test_filter_headlines_source_only(mock_get, client):
    response = client.get(
        "/api/v1/news/headlines/filter?source=cnn",
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 200


def test_filter_headlines_both_invalid(client):
    response = client.get(
        "/api/v1/news/headlines/filter?country=us&source=cnn",
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 400
