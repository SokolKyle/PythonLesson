class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class MovieModel:
    def __init__(self):
        self.movies = {}

    def add_movie(self, dict_article):
        movie = Movie(*dict_article.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_singe_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "название": movie.title,
            "жанр": movie.genre,
            "режиссёр": movie.director,
            "год выпуска": movie.year,
            "длительность": movie.duration,
            "студия":movie.studio,
            "актеры": movie.actors,
        }
        return dict_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)
