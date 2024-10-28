from storage.istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self._file = file_path

    def list_movies(self):
        with open(self._file, "r") as file:
            movies = json.load(file)
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        with open(self._file, "w") as file:
            json.dump(movies, file, indent=4)
        return "Movie successful added!"

    def delete_movie(self, title):
        movies = self.list_movies()
        del movies[title]
        with open(self._file, "w") as file:
            json.dump(movies, file, indent=4)
        return "Movie successful deleted!"

    def update_movie(self, title, rating):
        movies = self.list_movies()
        movies[title]["rating"] = rating
        with open(self._file, "w") as file:
            json.dump(movies, file, indent=4)
        return "Movie successful updated!"
