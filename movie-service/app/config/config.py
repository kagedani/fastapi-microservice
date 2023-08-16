from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()


def env_selection(env: str = ".env_default"):
    if os.environ['env'] == "local":
        env = ".env_local"
    elif os.environ['env'] == "test":
        env = ".env_test"
    return env


class Settings(BaseSettings):
    app_name: str = "Lightweight Microservice"
    database_user: str
    database_pwd: str
    database_host: str
    database_name: str
    model_config = SettingsConfigDict(env_file=env_selection())
