def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        print("Действия с фильмами")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Создание фильма")
    def add_user_movie(self):
        dict_movie = {
            "название": None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None,
        }
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key}: ")
        return dict_movie

    @add_title("Каталог фильмов")
    def show_all_movies(self, movies):
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie}")

    @add_title("Ввод названия фильма")
    def get_user_movie(self):
        user_movie = input("Введите название фильма: ")
        return user_movie

    @add_title("Просмотр информации о фильме")
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_movie(self, movie):
        print(f"Фильм {movie} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")