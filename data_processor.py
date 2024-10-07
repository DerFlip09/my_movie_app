from random import randrange


class DataProcessor:
    @staticmethod
    def get_movie_ratings(storage):
        ratings = [details["rating"] for movie, details in storage.items()]
        return ratings

    @staticmethod
    def get_movie_titles(storage):
        titles = [movie for movie, details in storage.items()]
        return titles

    @staticmethod
    def get_average_rating(storage):
        ratings = DataProcessor.get_movie_ratings(storage)
        avg_rating = round(sum(ratings) / len(ratings), 1)
        return avg_rating

    @staticmethod
    def get_median_rating(storage):
        ratings = sorted(DataProcessor.get_movie_ratings(storage))
        middle_index = len(ratings) // 2
        if len(ratings) % 2 == 0:
            return round((ratings[middle_index - 1] + ratings[middle_index]) / 2, 1)
        else:
            return ratings[middle_index]

    @staticmethod
    def get_movies_by_rating(storage, find_max=True):
        ratings = DataProcessor.get_movie_ratings(storage)
        titles = DataProcessor.get_movie_titles(storage)

        target_rating = max(ratings) if find_max else min(ratings)

        indexes = [index for index, rating in enumerate(ratings) if rating == target_rating]

        movies = [f"{titles[index]}, {ratings[index]}" for index in indexes]
        return "\n".join(movies)

    @staticmethod
    def get_best_movie_by_rating(storage):
        return DataProcessor.get_movies_by_rating(storage)

    @staticmethod
    def get_worst_movie_by_rating(storage):
        return DataProcessor.get_movies_by_rating(storage, find_max=False)

    @staticmethod
    def get_movie_stats(storage):
        avg_rating = DataProcessor.get_average_rating(storage)
        median_rating = DataProcessor.get_median_rating(storage)
        best_movies = DataProcessor.get_best_movie_by_rating(storage)
        worst_movies = DataProcessor.get_worst_movie_by_rating(storage)

        movie_list_statistics = [
            f"Average rating: {avg_rating}",
            f"Median rating: {median_rating}",
            f"Best movie: {best_movies}",
            f"Worst movie: {worst_movies}"
        ]
        return "\n".join(movie_list_statistics)

    @staticmethod
    def get_random_movie(storage):
        ratings = DataProcessor.get_movie_ratings(storage)
        titles = DataProcessor.get_movie_titles(storage)
        index = randrange(0, len(titles))
        return f"Your movie for tonight: {titles[index]}, it's rated {ratings[index]}"

    @staticmethod
    def get_movie_with_name(storage):
        searching_word = input("Enter part of movie name: ")
        movie_list_with_rating = [f"{movie}, {details['rating']}" for movie, details
                                  in storage.items() if searching_word.lower()
                                  in movie.lower()]
        return "\n".join(movie_list_with_rating)

    @staticmethod
    def get_sorted_movies_by_rating(storage):
        sorted_movies = sorted(storage.items(), key=lambda item: item[1]["rating"], reverse=True)
        sorted_movies_list = [f"{movie}, {details['rating']}" for movie, details
                              in sorted_movies]
        return "\n".join(sorted_movies_list)

    @staticmethod
    def get_sorted_movies_by_year(storage):
        sort_order = None
        while sort_order is None:
            sort_order = input("Do you want the latest movies first? (Y/N) ").strip().upper()
            if sort_order == "Y":
                sort_order = True
            elif sort_order == "N":
                sort_order = False
            else:
                print('Please enter "Y" or "N"')
                sort_order = None

        sorted_movies = sorted(storage.items(), key=lambda item: item[1]["year"], reverse=sort_order)
        sorted_movies_list = [f"{movie}, {details['year']}" for movie, details in sorted_movies]

        return "\n".join(sorted_movies_list)

    @staticmethod
    def get_minimum_user_rating():
        min_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        return float(min_rating) if min_rating else 0

    @staticmethod
    def get_user_start_year():
        start_year = input("Enter start year (leave blank for no start year): ")
        return int(start_year) if start_year else 0

    @staticmethod
    def get_user_end_year() -> int:
        end_year = input("Enter end year (leave blank for no end year): ")
        return int(end_year) if end_year else 2100

    @staticmethod
    def get_filtered_movies_by_property(storage):
        min_rating = DataProcessor.get_minimum_user_rating()
        start_year = DataProcessor.get_user_start_year()
        end_year = DataProcessor.get_user_end_year()
        filtered_movies = [f"{movie} ({details['year']}): {details['rating']}" for movie, details
                           in storage.items() if details["rating"] > min_rating
                           and start_year <= details["year"] <= end_year]
        return "\n".join(filtered_movies)
