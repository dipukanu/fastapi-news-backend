# 📰 News Aggregator API

A FastAPI backend for aggregating and managing news content from [NewsAPI.org](https://newsapi.org/), with OAuth2 security and PostgreSQL integration.

---

## 🔧 Features

- 🔐 OAuth2 (Client Credentials Flow)
- 🌍 Filter top headlines by country and/or source
- 💾 Save favorite news articles
- 🔎 Retrieve saved articles
- 🧪 Unit tests with coverage reporting
- 🐳 Docker support for easy deployment

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/dipukanu/fastapi-news-backend.git
```
### 2. Create and Activate Virtual Environment
```
python3.10 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Set Environment Variables (Create a .env file in the root directory with the following example:)
```
DATABASE_URL=postgres://username:password@localhost:5432/news_db
NEWS_API_KEY=your-news-api-key
DB_USER=your-postgres-username
DB_PASS=your-postgres-password
DB_NAME=your-db-name
```
### 5. Run the Application
```
uvicorn app.main:app --reload
```
### 6. Docker (Optional)
```
docker build -t news-api .
docker run -p 8000:8000 news-api
```

## 🧪 Running Tests

Make sure your virtual environment is activated.

To run all tests:

```bash
pytest
```

To run tests with coverage report:
```
pytest --cov=app --cov-report=term-missing
```

## 🔐 Access Token (OAuth2)

### 1️⃣ Register a Client
Send a POST request to `api/v1/clients/register` with the following payload to register your service and receive a `client_id` and `client_secret`:
```
{
  "name": "MyService",
  "description": "Backend service for billing"
}
```
### 2️⃣ Get an Access Token
Use your client_id and client_secret to obtain an access token.

Send a POST request to `api/v1/token` with this payload:
```
{
  "client_id": "your client id",
  "client_secret": "your client secret"
}
```
You will receive a response containing the access token:
```
{
  "access_token": "your_access_token",
  "token_type": "bearer"
}
```
### 3️⃣ Use the Access Token
Include the token in the Authorization header for all secured endpoints:
```
Authorization: Bearer <access_token>
```

## 📡 API Usage
### 1. GET /api/v1/news
- Description: Get top headlines.
- Requires token.
- Query params: page, page_size
- Example:
```
GET /api/v1/news?page=1&page_size=5
OR
GET /api/v1/news
```

### 2. GET /api/v1/news/headlines/source/{source_id}
- Description: Get top headlines by source.
- Example:
```
  GET /api/v1/news/headlines/source/cnn
```

### 3. GET /api/v1/news/headlines/country/{country_code}
- Description: Get top headlines by country code.
- Example:
```
  GET /api/v1/news/headlines/country/us
```

### 4. GET /api/v1/news/headlines/filter?country=xx&source=yy
- Description: Filter headlines by country and source.
- Note: NewsAPI does not allow filtering by both at the same time. Your app will raise a 400 error if both are provided.
- Example:
```
GET /api/v1/news/headlines/filter?country=us
OR
GET /api/v1/news/headlines/filter?source=cnn
```

### 5. POST /api/v1/news/save-latest
- Description:
- Fetches the latest 3 news articles from NewsAPI and saves them to the database.
Authentication:
- ✅ Requires an access token.
- Response Example:
```
{
  "message": "3 latest articles saved successfully."
}
```
