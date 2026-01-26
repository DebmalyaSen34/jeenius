from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "JEEnius"
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./tutor.db"
    project_name: str = "JEEnius API"
    project_version: str = "1.0.0"
    question_bank_path: str = "data/processed/question_bank.json"

    gemini_api_key: str | None = None
    groq_api_key: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()