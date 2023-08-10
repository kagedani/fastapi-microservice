from fastapi import FastAPI, HTTPException
from app.data.Movie import Movie
from typing import List

app = FastAPI()

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


@app.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db


@app.post('/', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.__dict__
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}


@app.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.__dict__
    try:
        fake_movie_db[id] = movie
        return None
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f"Movie with id {id} not found")

