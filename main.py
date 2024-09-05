from data_handling import load_data
from CLI import initialize_cli


FILENAME = "movie_storage.json"


# if new properties will be added, there should also be a check if adding a new movie,
# to get all keys of the second dictionary and add inside a for loop for each key a value.

def main():
    """
    Main entry point of the program. Loads movie data and starts the CLI.

    :raises FileNotFoundError: If the specified data file is not found.
    """
    try:
        movies = load_data(FILENAME)
        initialize_cli(movies)
    except FileNotFoundError:
        print(f"The file {FILENAME} was not found.")


if __name__ == "__main__":
    main()
