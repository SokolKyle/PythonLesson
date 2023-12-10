# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len)
# print(b)

# import random
#
# print(random.random())
# print(random.randint(3, 9))
# print(random.randrange(3, 9, 2))
#
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))
#
#
#
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = (mas)
# print(max_)
# mas.remove((max_))
# mas.insert(0, max_)
# print(mas)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)

# import random
# lst = [random.randint(0,100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("min =", min_ch)
#
# ind_min = lst.index(min_ch)
# print("index min =", ind_min)
#
# del lst[0: ind_min]
# print(lst)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)

# lst = [5]
# print(bool(lst))
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

import random

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("третий список: ", c)
# c = []
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print("Элементы без повторений: ", d)
# e =[]
# for i in a:
#     if i in b:
#         e.append(i)
# print("Общие элементы для двух списков: ", e)
# f = [min(a), min(b), max(a), max(b)]
# print("min and max:", f)

m = [[1, 2 ,3, 4], [5, 6, 7, 8, 9], [10, 11, 12]]
print(m)
print(len(m))
print(m[1][2])













