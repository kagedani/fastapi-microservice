from fastapi import APIRouter, Depends
from app.config import config
from functools import lru_cache
from typing_extensions import Annotated


@lru_cache()
def get_settings():
    return config.Settings()


configs = APIRouter()


@configs.get('/')
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "database_name": settings.database_name,
        "database_user": settings.database_user,
        "database_host": settings.database_host
    }
