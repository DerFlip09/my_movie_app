from storage.storage_json import StorageJson
from backend.movie_app import MovieApp


def main():
    """
    Main function to initialize the movie storage and run the MovieApp.
    """
    storage = StorageJson('data/movie_storage.json')
    app_movie = MovieApp(storage)
    app_movie.run()


if __name__ == "__main__":
    main()
