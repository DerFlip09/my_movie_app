import requests
import os
from dotenv import load_dotenv
from backend.data_processor import DataProcessor as Processor

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = f"http://www.omdbapi.com/?apikey={API_KEY}&t="


class MovieApp:
    """
    MovieApp provides a command-line interface for managing a movie database,
    allowing users to add, delete, update, and retrieve movie information.
    """

    def __init__(self, storage):
        """
        Initialize the MovieApp object with the given storage.

        :param storage: An instance of a storage class implementing IStorage.
        """
        self._storage = storage

    @property
    def storage(self):
        """Return the storage instance."""
        return self._storage

    def _command_list_movies(self):
        """
        List all movies in the storage.

        :return: A string representation of all movies and their details.
        """
        movies = self.storage.list_movies()
        movie_list = [f"{title} ({details['year']}): {details['rating']}" for title, details in movies.items()]
        return f"\n{len(movies)} movies in total\n{"-" * 18}\n" + "\n".join(movie_list)

    def _command_add_movie(self):
        """
        Add a new movie to the storage by querying an external API.

        :return: Confirmation message after adding the movie.
        """
        title = input("Enter new movie title: ")
        api_query = API_URL + title
        response = requests.get(api_query).json()
        return self.storage.add_movie(title, int(response["Year"]), float(response["imdbRating"]), response["Poster"])

    def _command_delete_movie(self):
        """
        Delete a movie from the storage.

        :return: Confirmation message after deleting the movie.
        """
        title = input("Enter title to delete: ")
        return self.storage.delete_movie(title)

    def _command_update_movie(self):
        """
        Update the rating of an existing movie in the storage.

        :return: Confirmation message after updating the movie rating.
        """
        title = input("Enter title for update: ")
        rating = float(input("Enter new rating: "))
        return self.storage.update_movie(title, rating)

    def _command_movie_stats(self):
        """
        Retrieve and return statistics about movies in the storage.

        :return: String representation of movie statistics.
        """
        movie_stats = Processor.get_movie_stats(self.storage.list_movies())
        return movie_stats

    def _command_random_movie(self):
        """
        Get a random movie from the storage.

        :return: String representation of a randomly selected movie.
        """
        random_movie = Processor.get_random_movie(self.storage.list_movies())
        return random_movie

    def _command_search_movie(self):
        """
        Search for a movie by name in the storage.

        :return: String representation of the found movie(s).
        """
        found_movie = Processor.get_movie_with_name(self.storage.list_movies())
        return found_movie

    def _command_sorted_movies_by_rating(self):
        """
        Retrieve and return movies sorted by rating.

        :return: String representation of movies sorted by rating.
        """
        sorted_movies = Processor.get_sorted_movies_by_rating(self.storage.list_movies())
        return sorted_movies

    def _command_sorted_movies_by_year(self):
        """
        Retrieve and return movies sorted by year.

        :return: String representation of movies sorted by year.
        """
        sorted_movies = Processor.get_sorted_movies_by_year(self.storage.list_movies())
        return sorted_movies

    def _command_filter_movie(self):
        """
        Filter movies based on user-defined criteria.

        :return: String representation of filtered movies.
        """
        filtered_movies = Processor.get_filtered_movies_by_property(self.storage.list_movies())
        return filtered_movies

    def _generate_website(self):
        """
        Generate a static HTML website representation of the movie database.

        :return: Confirmation message after generating the website.
        """
        template_path = "_static/index_template.html"
        with open(template_path, "r") as file:
            html_template = file.read()

        movie_item_template = """<li>
            <img src="__POSTER_URL__" alt="Poster of __TITLE__">
            <h2 class="movie-title">__TITLE__</h2>
            <div class="movie-year">__MOVIE_YEAR__</div>
            <div class="movie-rating">IMDb Rating: __IMDB_RATING__</div>
        </li>"""

        movies = self.storage.list_movies()
        movie_items = []
        for title, data in movies.items():
            movie_html = movie_item_template.replace("__POSTER_URL__", data["poster"])
            movie_html = movie_html.replace("__TITLE__", title)
            movie_html = movie_html.replace("__MOVIE_YEAR__", str(data["year"]))
            movie_html = movie_html.replace("__IMDB_RATING__", str(data["rating"]))
            movie_items.append(movie_html)

        movie_grid = "\n".join(movie_items)
        final_webpage = html_template.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

        with open("_static/index.html", "w") as file:
            file.write(final_webpage)

        return "Website generated successfully as 'index.html'"

    @staticmethod
    def dispatcher(welcome, menu, desc_funcs):
        """
        Handle user input for navigating through the command menu.

        :param welcome: Welcome message to display.
        :param menu: Menu options to display.
        :param desc_funcs: List of tuples containing command descriptions and corresponding functions.
        """
        print(welcome)
        while True:
            print("\nMenu:\n", menu)
            try:
                command = int(input(f"\nEnter choice (0-{len(desc_funcs) - 1}): "))
                if not 0 <= command <= len(desc_funcs) - 1:
                    raise ValueError
            except ValueError:
                print("Invalid choice!")
                continue
            if command == 0:
                print("Goodbye!")
                break
            else:
                print(desc_funcs[command][1](), "\n")
                input("Press enter to continue ")

    def run(self):
        """
        Run the main application loop, displaying the menu and processing user commands.
        """
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
