from data_processor import DataProcessor as Processor


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    @property
    def storage(self):
        return self._storage

    def _command_list_movies(self):
        movies = self.storage.movies
        movie_list = []
        for title, details in movies.items():
            movie_list.append(f"{title} ({details['year']}): {details['rating']}")
        return f"\n{len(movies)} movies in total\n{"-"*18}\n" + "\n".join(movie_list)

    def _command_add_movie(self):
        title = input("Enter new movies title: ")
        year = int(input("Enter the year: "))
        rating = float(input("Enter the rating: "))
        poster = input("Give me the filename of the poster: ")
        return self.storage.add_movie(title, year, rating, poster)

    def _command_delete_movie(self):
        title = input("Enter title to delete: ")
        return self.storage.delete_movie(title)

    def _command_update_movie(self):
        title = input("Enter title for update: ")
        rating = int(input("Enter new rating: "))
        return self.storage.update_movie(title, rating)

    def _command_movie_stats(self):
        movie_stats = Processor.get_movie_stats(self.storage.movies)
        return movie_stats

    def _command_random_movie(self):
        random_movie = Processor.get_random_movie(self.storage.movies)
        return random_movie

    def _command_search_movie(self):
        found_movie = Processor.get_movie_with_name(self.storage.movies)
        return found_movie

    def _command_sorted_movies_by_rating(self):
        sorted_movies = Processor.get_sorted_movies_by_rating(self.storage.movies)
        return sorted_movies

    def _command_sorted_movies_by_year(self):
        sorted_movies = Processor.get_sorted_movies_by_year(self.storage.movies)
        return sorted_movies

    def _command_filter_movie(self):
        filtered_movies = Processor.get_filtered_movies_by_property(self.storage.movies)
        return filtered_movies

    def _generate_website(self):
        pass

    @staticmethod
    def call_function(function, *args):
        function(*args)
        print()

    @staticmethod
    def dispatcher(welcome, menu, desc_funcs):
        print(welcome)
        while True:
            print("\nMenu:\n",menu)
            try:
                command = int(input(f"\nEnter choice (0-{len(desc_funcs) - 1}): "))
                if not 0 <= command <= len(desc_funcs) - 1:
                    raise ValueError
            except ValueError:
                print("Invalid choice!")
                continue
            if command == 0:
                print("Good Bye!")
                break
            else:
                print(desc_funcs[command][1](), "\n")
                input("Press enter to continue ")

    def run(self):
        welcome = "*" * 10 + " My Movie Database " + "*" * 10
        desc_funcs = (("Exit", None),
                      ("List movies", self._command_list_movies),
                      ("Add movie", self._command_add_movie),
                      ("Delete movie", self._command_delete_movie),
                      ("Update movie", self._command_update_movie),
                      ("Stats", self._command_movie_stats),
                      ("Random movie", self._command_random_movie),
                      ("Search movie", self._command_search_movie),
                      ("Movie sorted by rating", self._command_sorted_movies_by_rating),
                      ("Movie sorted by year", self._command_sorted_movies_by_year),
                      ("Filter movie", self._command_filter_movie),
                      ("Generate Website", self._generate_website))

        menu = "\n".join(f"{i}. {desc}" for i, (desc, _) in enumerate(desc_funcs))
        MovieApp.dispatcher(welcome, menu, desc_funcs)
