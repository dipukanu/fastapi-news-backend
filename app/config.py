from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    news_api_key: str
    database_url: str
    client_id: str
    client_secret: str

    class Config:
        env_file = ".env"

settings = Settings()
