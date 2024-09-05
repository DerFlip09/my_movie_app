import json


FILENAME = "movie_storage.json"


def convert_movie_dict_to_list(data: dict) -> list:
    """
    Converts a dictionary of movies into a formatted list of strings.

    :param data: Dictionary with movie titles as keys and their details as values.
    :returns: A list of strings, each containing the movie title, year, and rating formatted as
              "Title (Year): Rating".
    """
    movie_list = []
    for title, details in data.items():
        movie_list.append(f"{title} ({details['year']}): {details['rating']}")
    return movie_list


def get_movie_list(data: dict) -> str:
    """
    Generates a formatted string listing all movies with their year and rating.

    :param data: Dictionary with movie titles as keys and their details as values.
    :returns: A formatted string with the total number of movies and each movie's details on a new line.
    """
    movie_list = convert_movie_dict_to_list(data)
    return f"{len(data)} in total:\n" + "\n".join(movie_list)


def get_and_check_user_new_movie_title(data: dict, sentence="Enter movie name: ") -> ValueError | str:
    """
    Prompts the user to enter a new movie title and checks for its validity.

    :param data: Dictionary of existing movie titles.
    :param sentence: The prompt text for the user. Defaults to "Enter movie name: ".
    :raises ValueError: If the entered title already exists in the data.
    :returns: The valid and unique movie title entered by the user.
    """
    title = input(sentence)
    while title == "":
        print("Please enter a valid movie name!")
        title = input(sentence)
    if title in data.keys():
        raise ValueError(title)
    return title


def get_and_check_user_movie_title(data: dict, sentence="Enter movie name: ") -> ValueError | str:
    """
    Prompts the user to enter an existing movie title and checks for its validity.

    :param data: Dictionary of existing movie titles.
    :param sentence: The prompt text for the user. Defaults to "Enter movie name: ".
    :raises ValueError: If the entered title does not exist in the data.
    :returns: The valid movie title entered by the user.
    """
    title = input(sentence)
    while title == "":
        print("Please enter a valid movie name!")
        title = input(sentence)
    if title not in data.keys():
        raise ValueError(title)
    return title


def get_and_check_user_movie_year(sentence="Enter movie year: ") -> int:
    """
    Prompts the user to enter a valid movie year and checks for its validity.

    :param sentence: The prompt text for the user. Defaults to "Enter movie year: ".
    :returns: The valid movie year entered by the user, within the range 1888-2100.
    """
    while True:
        try:
            year = int(input(sentence))
            if 1888 <= year <= 2100:
                return year
            else:
                print("Please enter a real year!")
        except ValueError:
            print("Please enter a real year!")


def get_and_check_user_movie_rating(sentence="Enter new movie rating: ") -> float:
    """
    Prompts the user to enter a valid movie rating and checks for its validity.

    :param sentence: The prompt text for the user. Defaults to "Enter new movie rating: ".
    :returns: The valid movie rating entered by the user, within the range 1-10.
    """
    while True:
        try:
            rating = float(input(sentence))
            if 1 <= rating <= 10:
                return rating
            else:
                print("Please enter a rating between 1-10!")
        except ValueError:
            print("Please enter a rating between 1-10!")


def change_file_data(data: dict):
    """
    Saves the current movie data to a file in JSON format.

    :param data: Dictionary containing movie data to be saved.
    """
    with open(FILENAME, "w") as handle:
        handle.write(json.dumps(data))


def add_movie(data: dict) -> ValueError | str:
    """
    Adds a new movie to the data after validating the title, year, and rating.

    :param data: Dictionary containing the existing movie data.
    :returns: A success message if the movie is added, or an error message if the movie already exists.
    """
    try:
        title = get_and_check_user_new_movie_title(data)
    except ValueError as title:
        return f"Movie {title} already exists!"
    year = get_and_check_user_movie_year("Enter new movie year: ")
    rating = get_and_check_user_movie_rating()
    data[title] = {"year": year, "rating": rating}
    change_file_data(data)
    return f"Movie {title} was successfully added."


def delete_movie(data: dict) -> str:
    """
    Deletes an existing movie from the data after validating the title.

    :param data: Dictionary containing the existing movie data.
    :returns: A success message if the movie is deleted, or an error message if the movie doesn't exist.
    """
    try:
        movie = get_and_check_user_movie_title(data, "Enter movie name to delete: ")
    except ValueError as title:
        return f"Movie {title} doesn't exist!"
    user_validation = input(f"Do you want to delete {movie} ('Y' for delete or press enter for abort)? ")
    if user_validation.lower() == "y":
        del data[movie]
        change_file_data(data)
        return f"Movie {movie} was successfully deleted"
    else:
        return f"You will go back to menu"


def update_movie_ratings(data: dict) -> str:
    """
    Updates the rating of an existing movie in the data.

    :param data: Dictionary containing the existing movie data.
    :returns: A success message if the movie is updated, or an error message if the movie doesn't exist.
    """
    try:
        movie = get_and_check_user_movie_title(data)
    except ValueError as title:
        return f"Movie {title} doesn't exist!"
    new_rating = get_and_check_user_movie_rating()
    data[movie]["rating"] = new_rating
    change_file_data(data)
    return f"Movie {movie} successful updated"