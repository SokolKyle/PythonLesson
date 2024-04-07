# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         data[new_country] = new_capital
#
#         with open(file_name, 'w', encoding="utf-8") as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         if country in data:
#             print(f"Страна {country.capitalize()} столица {data[country].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {country.capitalize()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input('Введите страну для корректировки: ').lower()
#         new_capital = input('Введите новое название столицы: ').lower()
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         if country in data:
#             data[country] = new_capital
#             with open(file_name, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск даннах\n"
#                   "4 - редактирование даннах\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")


# import requests
# import json
# from pprint import pp
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(type(response.text))
# # print(response.text)
# todos = json.loads(response.text)
# # pp(todos)
# # print(type(todos[0]))
# # pp(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# top_complete = max(todos_by_user.values())
# top_users = [user for user in todos_by_user.items() if user[1] == top_complete]
#
# # m = "s" if len(users) > 1 else ""
# # print(f'user{m} {max_users} completed {}')
#
# filter_todos = [item for item in todos if item['userId'] in (5, 10) and item['completed']]
#
# with open('filter.json', 'w') as file:
#     json.dump(filter_todos, file, intent=2)

import csv

with open("data.csv", encoding="utf-8") as f:
    file_reader = csv.reader(f, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        else:
            print(f"{row[0]} - {row[1]}. Родился в {row[2]}")

        count += 1


