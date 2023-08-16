import uvicorn
from fastapi import FastAPI
from app.api.movies import movies
from app.api.configs import configs
from app.data.db import metadata, database, engine
from app.config import config
from functools import lru_cache

metadata.create_all(engine)


@lru_cache()
def get_settings():
    return config.Settings()


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])
app.include_router(configs, prefix='/api/v1/configs', tags=['configs'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
