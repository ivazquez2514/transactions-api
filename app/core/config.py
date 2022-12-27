import os
from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
from functools import lru_cache

env_path = Path(".") / ".env"
load_dotenv(dotenv_path = env_path)

class Settings(BaseSettings):
    mail_username: str = os.getenv("MAIL_USERNAME")
    mail_password: str = os.getenv("MAIL_PASSWORD")
    mail_from: str = os.getenv("MAIL_FROM")
    mail_port: str = os.getenv("MAIL_PORT")
    mail_server: str = os.getenv("MAIL_SERVER")
    mail_from_name: str = os.getenv("MAIL_FROM_NAME")

    class Config:
        env_file = env_path

@lru_cache
def get_settings():
    return Settings()