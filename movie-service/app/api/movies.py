from fastapi import HTTPException, APIRouter
from app.data.Movie import MovieIn, MovieOut
from typing import List
from app.api import db_manager


movies = APIRouter()


@movies.get('/', response_model=List[MovieOut])
async def index():
    return await db_manager.get_all_movies()


@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)
    return {'id': movie_id, **payload.__dict__}


@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {id} not found")

    updated_data = payload.__dict__
    updated_version = MovieIn(**movie)

    updated_movie_copy = updated_version.copy(update=updated_data)
    return await db_manager.update_movie(id, updated_movie_copy)


@movies.delete('/{id}')
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {id} not found")
    return await db_manager.delete_movie(id)
