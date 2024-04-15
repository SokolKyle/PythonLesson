def add_title(title):
    def wrapper(func):
        print(f" {title} ".center(50, "="))

        def wrap(*args, **kwargs):
            output = func(*args, **kwargs)
            return output

        return wrap

    return wrapper


class UserInterface:

    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        # print(f' {title} '.center(50, "="))
        print("Действие со статьями")
        print("1 - добавление статьи"
              "\n2 - вывод статьи"
              "\n3 - просмотр определенной статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")
        user_answer = input("Выберете вариант действия: ")
        print("=" * 50)
        return user_answer

    @add_title("Создание статьи")
    def add_user_article(self):
        dict_article = {
            "Название": None,
            "Автор": None,
            "Количество страниц": None,
            "Описание": None
        }
        print(" Создание статьи: ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи")
        print("=" * 50)
        return dict_article

    @add_title("вывод статьи")
    def show_all_articles(self, articles):
        print(" Список статей ".center(50, '='))
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")

    @add_title('Ввод названия статьи')
    def get_user_article(self):
        user_article = input("Введите название статьи: ")
        return user_article

    @add_title("Просмотр статьи")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} статьи - {article[key]}")

    @add_title("Сообщение об ошибки")
    def show_incorrect_title_error(self, user_title):
        print(f"Статья с названием {user_title} не существует")

    @add_title('выберете статью которую нужно удалить')
    def remove_single_article(self, article):
        print(f"Статья {article} - была удалена")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
