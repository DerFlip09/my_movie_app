import json
from storage.istorage import IStorage



class StorageJson(IStorage):
    """
    StorageJson provides methods to interact with a JSON file storage system
    for managing movie information including adding, deleting, and updating
    movies, as well as listing all movies.
    """

    def __init__(self, file_path):
        """
        Initialize the StorageJson object with the file path.

        :param file_path: Path to the JSON file where movie data is stored.
        """
        self._file = file_path

    def list_movies(self):
        """
        List all movies in the JSON storage.

        :return: Dictionary of movies, where each key is a movie title and
                 value is a dictionary of its details.
        """
        with open(self._file, "r") as file:
            movies = json.load(file)
        return movies

    def add_movie(self, title, year, rating, poster):
        """
        Add a movie to the JSON storage.

        :param title: Title of the movie.
        :param year: Release year of the movie.
        :param rating: Rating of the movie.
        :param poster: URL or file path for the movie poster.
        :return: Confirmation message indicating the movie was added successfully.
        """
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        with open(self._file, "w") as file:
            json.dump(movies, file, indent=4)
        return "Movie successfully added!"

    def delete_movie(self, title):
        """
        Delete a movie from the JSON storage.

        :param title: Title of the movie to delete.
        :return: Confirmation message if deleted successfully, else a not-found message.
        """
        movies = self.list_movies()
        for movie_title in list(movies):
            if title.lower() == movie_title.lower():
                del movies[movie_title]
                with open(self._file, "w") as file:
                    json.dump(movies, file, indent=4)
                return "Movie successfully deleted!"
        return f"Movie '{title}' could not be found in the database."

    def update_movie(self, title, rating):
        """
        Update the rating of an existing movie in the JSON storage.

        :param title: Title of the movie to update.
        :param rating: New rating for the movie.
        :return: Confirmation message if updated successfully, else a not-found message.
        """
        movies = self.list_movies()
        for movie_title in list(movies):
            if title.lower() == movie_title.lower():
                movies[movie_title]["rating"] = rating
                with open(self._file, "w") as file:
                    json.dump(movies, file, indent=4)
                return "Movie successfully updated!"
        return f"Movie '{title}' could not be found in the database."
