from random import randrange


class DataProcessor:
    """
    DataProcessor class provides static methods for processing and retrieving
    movie data from a given storage dictionary containing movie details.
    """

    @staticmethod
    def get_movie_ratings(storage):
        """
        Extract ratings from the movie storage.

        :param storage: Dictionary with movie titles as keys and details (including 'rating') as values.
        :return: List of movie ratings.
        """
        return [details["rating"] for movie, details in storage.items()]

    @staticmethod
    def get_movie_titles(storage):
        """
        Retrieve movie titles from the storage.

        :param storage: Dictionary with movie titles as keys.
        :return: List of movie titles.
        """
        return [movie for movie in storage.keys()]

    @staticmethod
    def get_average_rating(storage):
        """
        Calculate the average rating of movies in the storage.

        :param storage: Dictionary with movie details including 'rating'.
        :return: Average rating rounded to one decimal.
        """
        ratings = DataProcessor.get_movie_ratings(storage)
        return round(sum(ratings) / len(ratings), 1)

    @staticmethod
    def get_median_rating(storage):
        """
        Calculate the median rating of movies in the storage.

        :param storage: Dictionary with movie details including 'rating'.
        :return: Median rating.
        """
        ratings = sorted(DataProcessor.get_movie_ratings(storage))
        middle_index = len(ratings) // 2
        if len(ratings) % 2 == 0:
            return round((ratings[middle_index - 1] + ratings[middle_index]) / 2, 1)
        return ratings[middle_index]

    @staticmethod
    def get_movies_by_rating(storage, find_max=True):
        """
        Retrieve movies with the highest or lowest rating.

        :param storage: Dictionary with movie details including 'rating'.
        :param find_max: Boolean flag to find highest if True, lowest if False.
        :return: String with movies and ratings.
        """
        ratings = DataProcessor.get_movie_ratings(storage)
        titles = DataProcessor.get_movie_titles(storage)
        target_rating = max(ratings) if find_max else min(ratings)
        indexes = [index for index, rating in enumerate(ratings) if rating == target_rating]
        return "\n".join(f"{titles[index]}, {ratings[index]}" for index in indexes)

    @staticmethod
    def get_best_movie_by_rating(storage):
        """
        Retrieve the movie with the highest rating.

        :param storage: Dictionary with movie details including 'rating'.
        :return: String with the best movie and rating.
        """
        return DataProcessor.get_movies_by_rating(storage)

    @staticmethod
    def get_worst_movie_by_rating(storage):
        """
        Retrieve the movie with the lowest rating.

        :param storage: Dictionary with movie details including 'rating'.
        :return: String with the worst movie and rating.
        """
        return DataProcessor.get_movies_by_rating(storage, find_max=False)

    @staticmethod
    def get_movie_stats(storage):
        """
        Retrieve statistics on the movie ratings, including average, median,
        best, and worst movies.

        :param storage: Dictionary with movie details.
        :return: String with formatted movie statistics.
        """
        avg_rating = DataProcessor.get_average_rating(storage)
        median_rating = DataProcessor.get_median_rating(storage)
        best_movies = DataProcessor.get_best_movie_by_rating(storage)
        worst_movies = DataProcessor.get_worst_movie_by_rating(storage)
        return "\n".join([
            f"Average rating: {avg_rating}",
            f"Median rating: {median_rating}",
            f"Best movie: {best_movies}",
            f"Worst movie: {worst_movies}"
        ])

    @staticmethod
    def get_random_movie(storage):
        """
        Select a random movie from the storage.

        :param storage: Dictionary with movie details including 'rating'.
        :return: String with the randomly selected movie and its rating.
        """
        ratings = DataProcessor.get_movie_ratings(storage)
        titles = DataProcessor.get_movie_titles(storage)
        index = randrange(len(titles))
        return f"Your movie for tonight: {titles[index]}, it's rated {ratings[index]}"

    @staticmethod
    def get_movie_with_name(storage):
        """
        Retrieve movies whose titles contain a user-specified substring.

        :param storage: Dictionary with movie titles and details.
        :return: String of matching movie titles and ratings.
        """
        searching_word = input("Enter part of movie name: ")
        return "\n".join(
            f"{movie}, {details['rating']}" for movie, details in storage.items()
            if searching_word.lower() in movie.lower()
        )

    @staticmethod
    def get_sorted_movies_by_rating(storage):
        """
        Retrieve movies sorted by rating in descending order.

        :param storage: Dictionary with movie details including 'rating'.
        :return: String with sorted movies and ratings.
        """
        sorted_movies = sorted(storage.items(), key=lambda item: item[1]["rating"], reverse=True)
        return "\n".join(f"{movie}, {details['rating']}" for movie, details in sorted_movies)

    @staticmethod
    def get_sorted_movies_by_year(storage):
        """
        Retrieve movies sorted by year in either ascending or descending order.

        :param storage: Dictionary with movie details including 'year'.
        :return: String with sorted movies and years.
        """
        sort_order = None
        while sort_order is None:
            user_input = input("Do you want the latest movies first? (Y/N) ").strip().upper()
            if user_input in ["Y", "N"]:
                sort_order = user_input == "Y"
            else:
                print('Please enter "Y" or "N"')
        sorted_movies = sorted(storage.items(), key=lambda item: item[1]["year"], reverse=sort_order)
        return "\n".join(f"{movie}, {details['year']}" for movie, details in sorted_movies)

    @staticmethod
    def get_minimum_user_rating():
        """
        Prompt the user for a minimum rating to filter movies.

        :return: Minimum rating as a float.
        """
        min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        return float(min_rating) if min_rating else 0

    @staticmethod
    def get_user_start_year():
        """
        Prompt the user for a starting year to filter movies.

        :return: Starting year as an integer.
        """
        start_year = input("Enter start year (leave blank for no start year): ")
        return int(start_year) if start_year else 0

    @staticmethod
    def get_user_end_year():
        """
        Prompt the user for an ending year to filter movies.

        :return: Ending year as an integer.
        """
        end_year = input("Enter end year (leave blank for no end year): ")
        return int(end_year) if end_year else 2100

    @staticmethod
    def get_filtered_movies_by_property(storage):
        """
        Retrieve movies that meet the user's specified rating and year range criteria.

        :param storage: Dictionary with movie details including 'rating' and 'year'.
        :return: String with filtered movies, including their year and rating.
        """
        min_rating = DataProcessor.get_minimum_user_rating()
        start_year = DataProcessor.get_user_start_year()
        end_year = DataProcessor.get_user_end_year()
        return "\n".join(
            f"{movie} ({details['year']}): {details['rating']}" for movie, details in storage.items()
            if details["rating"] > min_rating and start_year <= details["year"] <= end_year
        )
