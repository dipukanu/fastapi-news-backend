# 📰 News Aggregator API

A FastAPI backend for aggregating and managing news content via NewsAPI.

## 🔧 Features

- OAuth2 client credentials authentication
- Integration with [NewsAPI](https://newsapi.org/)
- Endpoints to fetch and save news
- PostgreSQL database support
- Dockerized for easy deployment
- Modular and scalable codebase

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dipukanu/fastapi-news-backend.git
cd fastapi-news-backend

# Create and Activate Virtual Environment
python3.10 -m venv venv
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Set Environment Variables
# Create a .env file in the root directory with the following example:
DATABASE_URL=postgres://username:password@localhost:5432/news_db

# Run the Application
uvicorn app.main:app --reload

# Docker (Optional)
docker build -t news-api .
docker run -p 8000:8000 news-api


```