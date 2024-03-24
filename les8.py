import random

#
# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)]for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# import random
#
#
# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)]for y in range(h)]
# # matrix = [[random.randint(-20, 10) for x in range(3)] for i in range(4)]
# print(matrix)
# count = 0
# for i in matrix:
#     for j in i:
#         if j < 0:
#             count += 1
# print(count)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# import geometry
#
# num1 = geometry.sqrt(4)
# num2 = geometry.ceil(3.1)
# num3 = geometry.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(geometry.pi)

# import geometry as m
#
# num1 = m.sqrt(4)
# print(num1)

# import geometry as m
# # from geometry import sqrt, ceil
# from geometry import *
# num1 = sqrt(4)
# num2 = ceil(3.1)
# print(num1, num2)

import time
import locale
locale.setlocale(locale.LC_ALL, "")

# seconds = time.time()
# print("Кол-во секунд:", seconds)
#
# local_time = time.ctime()
# print("Местное время: ", local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%d.%m.%Y, %H:%M:%S"))
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

#  Function


# def hello(name):
#     print("Hello", name)
#
#
# hello("Nikolay")
# hello("Tatyana")

#
# def get_sum(a, b):
#     print(a + b)
#
#
# x, y = 2, 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'x', 'o')


# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
#
#
# x, y = 2, 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# print(maximum(17, 16))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     # print(lst)
#     # symbol1 = lst.pop(0)
#     # symbol2 = lst.pop()
#     # lst.append(symbol1)
#     # lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['С', 'Л', 'О', 'Н']))



# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a, b = 10, 15
# print(is_greater(a, b))
# print(is_greater(5, 10))
# if is_greater(a, b):
#     print(a, "Больше", b)
# else:
#     print(b, "Больше", a)


def check_password(password):
    has_upper = False
    has_lower = False
    has_num = False


    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_num = True


    if len(password) >= 8:
        return True
    return False


p = input("Введите пароль: ")
if check_password(p):
    print("Это надежный пароль!")
else:
    print("Этот пароль не надежный")


