from storage_json import StorageJson
from movie_app import MovieApp
from storage_csv import StorageCsv


def main():
    storage = StorageCsv('movie_storage.csv')
    app_movie = MovieApp(storage)
    app_movie.run()


if __name__ == "__main__":
    main()
