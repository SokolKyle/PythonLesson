# Модуль OS и OS.PATH

import os

# print(os.getcwd())  # Путь к текущей директории.
# print(os.listdir())  # Список директорий и файлов.
# print(os.listdir('..'))

# os.mkdir('../Lesson24')  # Создание директории
# os.rmdir('../Lesson24')
# os.makedirs('../Lesson24/Homework24')  # Создание директории
# os.rename('../Lesson24/Homework24', '../Lesson25')  # Переименование с перемещением
# os.renames('../Lesson24/Homework24', '../ll/Lesson25')  # Переименование с перемещением для работы с файлами

# os.mkdir('Test_folder')
# for i in range(1, 4):
#     with open(f'Test_folder/file{i}.txt', 'w') as file:
#         ...
# os.mkdir('Test_folder/Inner_test_folder1')
# for i in range(4, 9):
#     with open(f'Test_folder/Inner_test_folder1/file{i}.txt', 'w') as file:
#         ...
# os.mkdir('Test_folder/Inner_test_folder2')
# for i in range(9, 15):
#     with open(f'Test_folder/Inner_test_folder2/file{i}.txt', 'w') as file:
#         ...

# for root, dirs, files in os.walk("Test_folder", topdown=False):
#     print('Root', root)
#     print('Subdirs', dirs)
#     print('Files', files)

# os.mkdir('folder/')
# os.mkdir('folder/inner_folder1/')
# os.mkdir('folder/inner_folder2/')
# os.mkdir('folder/inner_folder1/inner_inner1_folder1/')
# os.mkdir('folder/inner_folder1/inner_inner1_folder2/')
# os.mkdir('folder/inner_folder2/inner_inner2_folder1/')
# os.mkdir('folder/inner_folder2/inner_inner2_folder2/')

# os.rmdir('folder/inner_folder1/inner_inner_folder2/')
# os.rmdir('folder/inner_folder1/inner_inner_folder1/')
# os.rmdir('folder')


# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree, topdown=False):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директории {root} удалена')
#
#
# remove_empty_dirs('folder')

# print(os.path.split('/home/konstantin/PycharmProjects/Top-Academy-Python-Developer-Group-313'))
# print(os.path.dirname('/home/konstantin/PycharmProjects/Top-Academy-Python-Developer-Group-313'))
# print(os.path.basename('/home/konstantin/PycharmProjects/Top-Academy-Python-Developer-Group-313'))
# print(os.path.join('/home/konstantin', 'PycharmProjects', 'op-Academy-Python-Developer-Group-313'))
# print(os.path.join('PycharmProjects', '/home/konstantin', 'op-Academy-Python-Developer-Group-313'))

# directories = ['Work/F1/', 'Work/F2/F21',]
# for directory in directories:
#     os.makedirs(directory)

# files = {
#     'Work': ['w.txt',],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt',],
#     'Work/F2/F21': ['f211.txt', 'f212.txt',],
# }
#
# basenames = ['w.txt', 'f12.txt', 'f211.txt', 'f212.txt']
#
# for folder, filenames in files.items():
#     for filename in filenames:
#         path = os.path.join(folder, filename)
#         with open(path, 'w') as f:
#             if os.path.basename(path) in basenames:
#                 f.write(path)


# def print_tree(root, topdown=True):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('-' * 50)
#
#
# print_tree('Work', False)
# print_tree('Work')


# print(os.path.exists(  # Проверяет существование пути.
#     '/home/konstantin/'
#     'PycharmProjects/'
#     'Top-Academy-Python-Developer-Group-313/'
#     'Python/'
#     'Lesson23/'
#     'Work/'
#     'F2/'
#     'F21/'
#     'f212.txt'
#     )
# )
#
# print(os.path.isfile(  # Проверяет, что указанный путь является правильным путем к файлу.
#     '/home/konstantin/'
#     'PycharmProjects/'
#     'Top-Academy-Python-Developer-Group-313/'
#     'Python/'
#     'Lesson23/'
#     'Work/'
#     'F2/'
#     'F21/'
#     'f212.txt'
#     )
# )
#
#
# print(os.path.isdir(  # Проверяет, что указанный путь является правильным путем к файлу.
#     '/home/konstantin/'
#     'PycharmProjects/'
#     'Top-Academy-Python-Developer-Group-313/'
#     'Python/'
#     'Lesson23/'
#     'Work/'
#     'F2/'
#     'F21'
#     )
# )

import time


# print(os.path.getsize('lesson23.py'))  # Возвращает размер файла в байтах (FileNotFoundError).
# print(os.path.getsize('lesson23.py') / 1024)   # Возвращает размер файла в килобайтах.
#
# # Возвращает время последнего доступа к файлу.
# print(time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(os.path.getatime('lesson23.py'))))
# # Возвращает время создания файла (ОС Windows).
# print(time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(os.path.getctime('lesson23.py'))))
# # Возвращает последнего изменение файла.
# print(time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(os.path.getmtime('lesson23.py'))))

# file_path = (
#     '/home/konstantin/'
#     'PycharmProjects/'
#     'Top-Academy-Python-Developer-Group-313/'
#     'Python/'
#     'Lesson23/'
#     'Work/'
#     'F2/'
#     'F21/'
#     'f2123.txt'
# )
#
# #
# # if os.path.exists(file_path):
# #     directory, file_name = os.path.split(file_path)
# #     print(f'{file_name} ({directory}) - последний доступ к файлу: {os.path.getsize(file_path)}')
# # else:
# #     print(f'Файл {file_path} не существует')
# try:
#     os.path.exists(file_path)
# except FileNotFoundError():
#     print(f'Файл {file_path} не существует')
# else:
#     directory, file_name = os.path.split(file_path)
#     print(f'{file_name} ({directory}) - последний доступ к файлу: {os.path.getsize(file_path)}')