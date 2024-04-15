from view import UserInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.movie_model = MovieModel()  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            movie = self.user_interface.add_user_movie()
            self.movie_model.add_movie(movie)
        elif answer == '2':
            movies = self.movie_model.get_all_movies()
            self.user_interface.show_all_movies(movies)
        elif answer == '3':
            movie_title = self.user_interface.get_user_movie()
            try:
                movie = self.movie_model.get_singe_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(movie_title)
            else:
                self.user_interface.show_single_movie(movie)
        elif answer == '4':
            movie_title = self.user_interface.get_user_movie()
            try:
                title = self.movie_model.remove_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(movie_title)
            else:
                self.user_interface.remove_single_movie(title)
        elif answer == 'q':
            pass
        else:
            self.user_interface.show_incorrect_answer_error(answer)