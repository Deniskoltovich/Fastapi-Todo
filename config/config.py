import os

from dotenv import find_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_HOST: str
    APP_PORT: int

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    DATABASE_URL: str

    class Config:
        env_file = find_dotenv('.env')
        env_file_encoding = "utf-8"


settings = Settings()
