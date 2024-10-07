import data_storage_handling as dsh
import data_handling as dh


COMMAND_DISPATCHER = {0: {"description": "Exit", "function": None},
                      1: {"description": "List movies", "function": dsh.get_movie_list},
                      2: {"description": "Add movie", "function": dsh.add_movie},
                      3: {"description": "Delete movie", "function": dsh.delete_movie},
                      4: {"description": "Update movie", "function": dsh.update_movie_ratings},
                      5: {"description": "Stats", "function": dh.get_movie_list_statistics},
                      6: {"description": "Random movie", "function": dh.get_random_movie},
                      7: {"description": "Search movie", "function": dh.get_movie_with_name},
                      8: {"description": "Movies sorted by rating", "function": dh.get_sorted_movies_by_rating},
                      9: {"description": "Movies sorted by year", "function": dh.get_sorted_movies_by_year},
                      10: {"description": "Filter movies", "function": dh.get_filtered_movies_by_property}}


def print_welcome():
    """
    Prints a welcome message for the Movie Database CLI.
    """
    print("*" * 10, "My Movie Database", "*" * 10)


def print_menu():
    """
    Displays the menu of available commands in the CLI.
    """
    print("\nMenu:")
    for command_number, command_info in COMMAND_DISPATCHER.items():
        print(f"{command_number}. {command_info['description']}")


def initialize_cli(data: dict):
    """
    Initializes the CLI, displays the menu, and handles user commands.

    :param data: Movie data dictionary.
    """
    print_welcome()
    while True:
        print_menu()
        try:
            command = int(input("\nEnter choice (0-10): "))
            if not 0 <= command <= 10:
                raise ValueError
        except ValueError:
            print("Invalid choice!\n")
            continue
        if command == 0:
            print("Good Bye!")
            break
        else:
            print(COMMAND_DISPATCHER[command]["function"](data), "\n")
            input("Press enter to continue ")
