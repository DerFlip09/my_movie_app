from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self._file = file_path
        with open(self._file, "r") as file:
            self._movies = json.load(file)

    @property
    def movies(self):
        return self._movies

    def add_movie(self, title, year, rating, poster):
        self.movies[title] = {"year": year, "rating": rating, "poster": poster}
        with open(self._file, "w") as file:
            file.write(json.dumps(self._movies))
        return "Movie successful added!"

    def delete_movie(self, title):
        del self.movies[title]
        with open(self._file, "w") as file:
            file.write(json.dumps(self._movies))
        return "Movie successful deleted!"

    def update_movie(self, title, rating):
        self.movies[title]["rating"] = rating
        with open(self._file, "w") as file:
            file.write(json.dumps(self._movies))
        return "Movie successful updated!"
