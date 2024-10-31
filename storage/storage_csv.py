import csv
from storage.istorage import IStorage


class StorageCsv(IStorage):
    """
    StorageCsv provides methods to interact with a CSV file storage system
    for managing movie information including adding, deleting, and updating
    movies, as well as listing all movies.
    """

    def __init__(self, file_path):
        """
        Initialize the StorageCsv object with the file path.

        :param file_path: Path to the CSV file where movie data is stored.
        """
        self._file = file_path

    def list_movies(self):
        """
        List all movies in the CSV storage.

        :return: Dictionary of movies, where each key is a movie title and
                 value is a dictionary of its details.
        """
        movies = {}
        with open(self._file, 'r', newline='', encoding='utf-8') as file:
            next(file)  # Skip the header row
            csv_reader = csv.reader(file)
            for movie in csv_reader:
                if len(movie) < 7:  # Ensure there are enough columns
                    movie += [""] * (7 - len(movie))
                title, year, rating, poster, notes, imdb_id, flag = movie
                movies[title] = {
                    "year": year,
                    "rating": rating,
                    "poster": poster,
                    "notes": notes,
                    "imdb_id": imdb_id,
                    "flag": flag
                }
        return movies

    @staticmethod
    def json_to_csv(json_data):
        """
        Convert JSON data to a list of CSV rows.

        :param json_data: Dictionary of movie data.
        :return: List of lists representing CSV rows.
        """
        csv_data = [["title", "year", "rating", "poster", "notes", "imdb_id", "flag"]]
        for title, info in json_data.items():
            row = [
                title, info["year"],
                info["rating"], info["poster"],
                info["notes"], info["imdb_id"],
                info["flag"]
            ]
            csv_data.append(row)
        return csv_data

    def add_movie(self, title, year, rating, poster, notes=" ", imdb_id=" ", flag=" "):
        """
        Add a movie to the CSV storage.

        :param title: Title of the movie.
        :param year: Release year of the movie.
        :param rating: Rating of the movie.
        :param poster: URL or file path for the movie poster.
        :param notes: Additional notes about the movie (default is a space).
        :param imdb_id: IMDB ID of the movie (default is a space).
        :param flag: Any additional flag (default is a space).
        :return: Confirmation message indicating the movie was added successfully.
        """
        movies = self.list_movies()
        movies[title] = {
            "year": year,
            "rating": rating,
            "poster": poster,
            "notes": notes,
            "imdb_id": imdb_id,
            "flag": flag
        }
        with open(self._file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.json_to_csv(movies))
        return "Movie successfully added!"

    def delete_movie(self, title):
        """
        Delete a movie from the CSV storage.

        :param title: Title of the movie to delete.
        :return: Confirmation message if deleted successfully, else a not-found message.
        """
        movies = self.list_movies()
        for movie_title in list(movies):
            if title.lower() == movie_title.lower():
                del movies[movie_title]
                with open(self._file, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(self.json_to_csv(movies))
                return "Movie successfully deleted!"
        return f"Movie '{title}' could not be found in the database."

    def update_movie(self, title, rating):
        """
        Update the rating of an existing movie in the CSV storage.

        :param title: Title of the movie to update.
        :param rating: New rating for the movie.
        :return: Confirmation message if updated successfully, else a not-found message.
        """
        movies = self.list_movies()
        for movie_title in list(movies):
            if title.lower() == movie_title.lower():
                movies[movie_title]["rating"] = rating
                with open(self._file, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(self.json_to_csv(movies))
                return "Movie successfully updated!"
        return f"Movie '{title}' could not be found in the database."
