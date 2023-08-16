from sqlalchemy import (Column, Integer, MetaData, String, Table, ARRAY)
from sqlalchemy import create_engine
from app.config import config


from databases import Database

settings = config.Settings()
DATABASE_URI = f"postgresql://{settings.database_user}:{settings.database_pwd}@{settings.database_host}/{settings.database_name}"

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URI)
