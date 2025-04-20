from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_name: str
    news_api_key: str
    database_url: str
    client_id: str
    client_secret: str

    class Config:
        env_file = ".env"


settings = Settings()
