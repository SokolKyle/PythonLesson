f = open("text4.txt", "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
f.close()

# f = open("text4.txt", "r")
# lines = f.readlines()
# f.close()
# lines[1] = "Hello world\n"
# # f.seek(0)
#
# # f.writelines(lines)
#
#
# # f = open("text4.txt", "r")
# # rl = f.readlines()
#
# f = open("text4.txt", "w")
# f.writelines(lines)
# f.close()

# f = open("text4.txt", "r")
# lines = f.readlines()
# f.close()
#
# print("Какую строку вы хотите удалить?")
# print("1. " + lines[0])
# print("2. " + lines[1])
# print("3. " + lines[2])
# lin = input("Введите цифру строки для удаления (1, 2, 3): ")
# if lin in ["1", "2", "3"]:
#     del_index = int(lin) - 1
#     del lines[del_index]
#     print("Строка успешно удалена!")
# else:
#     print("Неверный индекс строки!")
#
# f = open("text4.txt", "w")
# f.write()
# f.close()


# Открываем файл для чтения
# f = open("text4.txt", "r")
# lines = f.readlines()
# f.close()
#
# print("Какую строку вы хотите удалить?")
# print("1. " + lines[0].strip())
# print("2. " + lines[1].strip())
# print("3. " + lines[2].strip())
#
# lin = input("Введите цифру строки для удаления (1, 2, 3): ")
#
# if lin in ["1", "2", "3"]:
#     del_index = int(lin) - 1
#     del lines[del_index]
#     print("Строка успешно удалена!")
# else:
#     print("Неверный индекс строки!")
#
# # Перезаписываем файл с обновленными строками
# f = open("text4.txt", "w")
# for line in lines:
#     f.write(line)
# f.close()

# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файл
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'a+')
# print(f.write('I\'m learning Python'))
# print(f.tell())
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:3])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     # lt = list(map(str, lt))
#     lt = list(map(str, lt))
#     print(lt)
#     print(type(lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w+') as f:
#     # f.write(str(lst))  # [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#     f.write(get_line(lst))  # [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# with open(file_name, 'r') as f:
#     numbers = f.read()
#
# print(numbers)  # 4.5 2.8 3.9 1.0 0.3 4.33 7.777
#
# num_list = list(map(float, numbers.split()))
# print(num_list)
# print(type(num_list))
# print(sum(num_list))
# print(len(num_list))
#
# print('Done')

# def longest_worlds(file):
#     with open(file, 'r') as text:
#         text = text.read().split()
#         max_length = len(max(text, key=len))
#         res = [word for word in text if len(word) == max_length]
#         return res
#
#
# print(longest_worlds('task.txt'))
#
# one = 'one.txt'
# two = 'two.txt'
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#with open(one, 'w') as f:
#    f.write(text)
#
# with open(one, 'r') as first, open(two, 'w') as second:
#     for line in first:
#         line = line.replace('Строка', 'Линия -')
#         second.write(line)