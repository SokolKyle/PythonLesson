# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name: str = name
#         self.marks: list = marks
#
#     def __repr__(self):
#         marks = ', '.join(map(str, self.marks))
#         return f'Студент: {self.name}: {marks}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         return self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def get_file_name(self):
#         return self.name + '.json'
#
#     def dump_to_json(self):
#         data = {
#             'name': self.name,
#             'marks': self.marks
#         }
#         with open(self.get_file_name(), 'w') as file:
#             json.dump(data, file)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), 'r') as file:
#             print(json.load(file))
#
#
# class Group:
#     def __init__(self, students: list[Student], group: str):
#         self.students: list[Student] = students
#         self.group: str = group
#
#     def __repr__(self):
#         return f'Группа: {self.group}\n' + ',\n'.join(map(str, self.students))
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group_1, group_2, index):
#         group_2.add_student(group_1.remove_student(index))
#
#     def dump_to_json(self):
#         data = {
#             'group': self.group,
#             'students': [
#                 {'name': student.name, 'marks': student.marks} for student in self.students
#             ]
#         }
#         with open(self.get_file_name(), 'w', encoding='UTF-8') as file:
#             json.dump(data, file, indent=2)
#
#     def get_file_name(self):
#         return self.group.lower().replace(' ', '-') + '.json'
#
#     def load_from_file(self):
#         with open(self.get_file_name(), 'r') as file:
#             print(json.load(file))
#
#     # @staticmethod
#     # def update_to_json(group1, group2):
#     #     return group1.update(group2)
#
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# sts1 = [st1, st2]
#
# group1 = Group(sts1, 'ГК Python')
# # # print(group1)
# # group1.add_student(st3)
# # # print(group1)
# # group1.remove_student(1)
# # print(group1)
# sts2 = [st2]
# # group2 = Group(sts2, 'ГК Web')
# # print(group2)
# # Group.change_group(group1, group2, 0)
# # print(group1)
# # print(group2)
#
# # st1.dump_to_json()
# # st1.load_from_file()
# group1.dump_to_json()
# group1.load_from_file()
# Group.update_to_json(sts1, sts2)


import json


class CountryCapital:
    @staticmethod
    def add_country(file_name):
        new_country = input('Введите название страны: ').lower()
        new_capital = input('Введите название столицы: ').lower()

        try:
            data = json.load(open(file_name))
        except FileNotFoundError:
            data = {}
        finally:
            data[new_country] = new_capital

        with open(file_name, 'w+', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as file:
            print({key.capitalize(): value.capitalize() for key, value in json.load(file).items()})


file = 'list_capital.json'


while True:
    index = input(
        'Выбор действия:\n'
        '1 - добавление данных\n'
        '2 - удаление данных\n'
        '3 - поиск даннах\n'
        '4 - редактирование даннах\n'
        '5 - просмотр данных\n'
        '6 - завершение работы\n'
        'Ввод: ')

    match index:
        case '1':
            CountryCapital.add_country(file)
        case '5':
            CountryCapital.load_from_file(file)
        case '6':
            break
        case _:
            print('Не корректные данные. Убедитесь в корректность ввода и повторите попытку')