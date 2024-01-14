# print(bin(18))  #двоичная
# print(oct(18))  #восмиричная
# print(hex(18))  #шестнадцеритчная
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0x12 + 0o22 + 0b10010 + 18)


# q = 'pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print(e * -3)
# print('y' in e)
# print(e[1])


# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = changeCharToStr(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt\\")
# print(r"C:\folder\file.txt\\"[:-1])
# print(r"C:\folder\file.txt" + "\\")

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет")
#
# m = 2.543563635
# print(f"{round(m, 2)}")
# print(f"{m:.2f}")
# print(f"{m:.3f}")


# x = 10
# y = 5
#
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")
# num = 74
# print(f"{{{num}}}")


# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")

# s = """
# Многострочный
# текст
# """
# print(s)
#
# s1 = '''
#
# '''

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычесляет площадь цилиндра на оснавании заданной высоты и радиуса основания
#     :param r: Положительное число, радиус основания цилиндра
#     :param h: Положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 1 * pi * r * (r * h)


# print(cylinder(2, 5))


# print(ord("a"))
# print(ord("а"))

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


s = "Test string for me"
arr = [ord(x) for x in s]
print("ASCII коды:", arr)
arr = [int(sum(arr) / len(arr))] + arr
print("Среднее арифметическое", arr)
arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
print(arr)
print(arr.count(arr[-1]) - 1)
arr.sort(reverse=True)
print(arr)


# print(chr(97))
# print(chr(1010))












