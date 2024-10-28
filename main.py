from storage.storage_json import StorageJson
from backend.movie_app import MovieApp


def main():
    storage = StorageJson('data/movie_storage.json')
    app_movie = MovieApp(storage)
    app_movie.run()


if __name__ == "__main__":
    main()
