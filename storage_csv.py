from istorage import IStorage
import csv


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self._file = file_path

    def list_movies(self):
        movies = {}
        with open(self._file, 'r', newline='', encoding='utf-8') as file:
            next(file)
            csv_reader = csv.reader(file)
            for movie in csv_reader:
                if len(movie) < 7:
                    movie += [""] * (7 - len(movie))
                title, year, rating, poster, notes, imdb_id, flag = movie
                movies[title] = {"year": year,
                                 "rating": rating,
                                 "poster": poster,
                                 "notes": notes,
                                 "imdb_id": imdb_id,
                                 "flag": flag}
        return movies

    @staticmethod
    def json_to_csv(json_data):
        csv_data = [["title", "year", "rating", "poster", "notes", "imdb_id", "flag"]]
        for title, info in json_data.items():
            row = [title, info["year"],
                   info["rating"], info["poster"],
                   info["notes"], info["imdb_id"],
                   info["flag"]]
            csv_data.append(row)
        return csv_data

    def add_movie(self, title, year, rating, poster, notes=" ", imdb_id=" ", flag=" "):
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating,
                         "poster": poster, "notes": notes,
                         "imdb_id": imdb_id, "flag": flag}
        with open(self._file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.json_to_csv(movies))
        return "Movie successfully added!"

    def delete_movie(self, title):
        movies = self.list_movies()
        del movies[title]
        with open(self._file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.json_to_csv(movies))
        return "Movie successful deleted!"

    def update_movie(self, title, rating):
        movies = self.list_movies()
        movies[title]["rating"] = rating
        with open(self._file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.json_to_csv(movies))
        return "Movie successful updated!"
