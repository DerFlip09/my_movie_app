from storage_csv import StorageCsv
from movie_app import MovieApp
import json


def add_movie(title, year, rating, poster):
    with open("movie_storage.json", "a") as file:
        movie = {title: {"year": year, "rating": rating, "poster": poster}}
        file.write(json.dumps(movie))
    return "Movie successful added!"


add_movie("Matrix", 1999, 8.4, "matrix.img")
