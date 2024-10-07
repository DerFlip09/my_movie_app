import json
from random import randrange
from data_storage_handling import convert_movie_dict_to_list


def load_data(filename: str):
    """
    Loads data from a JSON file.

    :param filename: Path to the JSON file.
    :returns: Data loaded from the file.
    """
    with open(filename, "r") as file:
        return json.load(file)


def get_movie_ratings(data: dict) -> list:
    """
    Extracts movie ratings.

    :param data: Movie data dictionary.
    :returns: List of ratings.
    """
    ratings = [details["rating"] for movie, details in data.items()]
    return ratings


def get_movie_titles(data: dict) -> list:
    """
    Extracts movie titles.

    :param data: Movie data dictionary.
    :returns: List of titles.
    """
    titles = [movie for movie, details in data.items()]
    return titles


def get_average_rating(data: dict) -> float:
    """
    Calculates the average rating.

    :param data: Movie data dictionary.
    :returns: Average rating.
    """
    ratings = get_movie_ratings(data)
    avg_rating = round(sum(ratings) / len(ratings), 1)
    return avg_rating


def get_median_rating(data: dict) -> float:
    """
    Calculates the median rating.

    :param data: Movie data dictionary.
    :returns: Median rating.
    """
    ratings = sorted(get_movie_ratings(data))
    middle = len(ratings) // 2
    if len(ratings) % 2 == 0:
        return round((ratings[middle - 1] + ratings[middle]) / 2, 1)
    else:
        return ratings[middle]


def get_best_movie_by_rating(data: dict) -> str:
    """
    Finds the highest-rated movie(s).

    :param data: Movie data dictionary.
    :returns: Movie title(s) and rating of the best movie(s).
    """
    ratings = get_movie_ratings(data)
    titles = get_movie_titles(data)
    indexes = []
    old_rating_index = 0
    for rating in ratings:
        if rating == max(ratings):
            indexes.append(ratings.index(rating, old_rating_index))
            old_rating_index = ratings.index(rating) + 1
    best_movies = [f"{titles[index]}, {ratings[index]}" for index in indexes]
    return "\n".join(best_movies)


def get_worst_movie_by_rating(data: dict) -> str:
    """
    Finds the lowest-rated movie(s).

    :param data: Movie data dictionary.
    :returns: Movie title(s) and rating of the worst movie(s).
    """
    ratings = get_movie_ratings(data)
    titles = get_movie_titles(data)
    indexes = []
    old_rating_index = 0
    for rating in ratings:
        if rating == min(ratings):
            indexes.append(ratings.index(rating, old_rating_index))
            old_rating_index = ratings.index(rating) + 1
    worst_movies = [f"{titles[index]}, {ratings[index]}" for index in indexes]
    return "\n".join(worst_movies)


def get_random_movie(data: dict) -> str:
    """
    Selects a random movie.

    :param data: Movie data dictionary.
    :returns: Title and rating of the selected movie.
    """
    ratings = get_movie_ratings(data)
    titles = get_movie_titles(data)
    index = randrange(0, len(titles))
    return f"Your movie for tonight: {titles[index]}, it's rated {ratings[index]}"


def get_movie_list_statistics(data: dict) -> str:
    """
    Generates movie statistics: average rating, median rating, best, and worst movies.

    :param data: Movie data dictionary.
    :returns: Movie statistics as a string.
    """
    movie_list_statistics = []
    avg_rating = get_average_rating(data)
    movie_list_statistics.append(f"Average rating: {avg_rating}")

    median_rating = get_median_rating(data)
    movie_list_statistics.append(f"Median rating: {median_rating}")

    best_movies = get_best_movie_by_rating(data)
    movie_list_statistics.append(f"Best movie: {best_movies}")

    worst_movies = get_worst_movie_by_rating(data)
    movie_list_statistics.append(f"Worst movie: {worst_movies}")
    return "\n".join(movie_list_statistics)


def get_movie_with_name(data: dict) -> str:
    """
    Searches for movies by name.

    :param data: Movie data dictionary.
    :returns: Movies matching the search term.
    """
    searching_word = input("Enter part of movie name: ")
    movie_list_with_rating = [f"{movie}, {details['rating']}" for movie, details in data.items() if searching_word.lower() in movie.lower()]
    return "\n".join(movie_list_with_rating)


def get_sorted_movies_by_rating(data: dict) -> str:
    """
    Sorts movies by rating in descending order.

    :param data: Movie data dictionary.
    :returns: Sorted list of movies by rating.
    """
    sorted_movies = sorted(data.items(), key=lambda item: item[1]["rating"], reverse=True)
    sorted_movies_list = [f"{movie}, {details['rating']}" for movie, details in sorted_movies]
    return "\n".join(sorted_movies_list)


def get_sorted_movies_by_year(data: dict) -> str:
    """
    Sorts movies by year, in ascending or descending order.

    :param data: Movie data dictionary.
    :returns: Sorted list of movies by year.
    """
    while True:
        sort_order = input("Do you want the latest movies first? (Y/N) ")
        if sort_order.upper() not in ("Y", "N"):
            print('Please enter "Y" or "N"')
            continue
        elif sort_order.upper() == "N":
            sort_order = False
            break
        sort_order = True
        break

    sorted_movies = sorted(data.items(), key=lambda item: item[1]["year"], reverse=sort_order)
    sorted_movies_list = [f"{movie}, {details['year']}" for movie, details in sorted_movies]
    return "\n".join(sorted_movies_list)


def get_minimum_user_rating() -> float | int:
    """
    Prompts the user to input a minimum rating.

    :returns: Minimum rating as a float, or 0 if left blank.
    """
    min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
    return float(min_rating) if min_rating else 0


def get_user_start_year() -> int:
    """
    Prompts the user to input a start year.

    :returns: Start year as an integer, or 0 if left blank.
    """
    start_year = input("Enter start year (leave blank for no start year): ")
    return int(start_year) if start_year else 0


def get_user_end_year() -> int:
    """
    Prompts the user to input an end year.

    :returns: End year as an integer, or 2100 if left blank.
    """
    end_year = input("Enter end year (leave blank for no end year): ")
    return int(end_year) if end_year else 2100


def get_filtered_movies_by_property(data: dict) -> str:
    """
    Filters movies by rating and year range.

    :param data: Movie data dictionary.
    :returns: List of filtered movies.
    """
    min_rating = get_minimum_user_rating()
    start_year = get_user_start_year()
    end_year = get_user_end_year()
    filtered_movies = {movie: details for movie, details in data.items() if details["rating"] > min_rating and start_year <= details["year"] <= end_year}
    return "\n".join(convert_movie_dict_to_list(filtered_movies))

