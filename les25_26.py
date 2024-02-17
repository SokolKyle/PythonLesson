#   OOP lesson two
# -------------------


# class Point:
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # private
#             self.__y = y
#         # self.set_coord(x, y)
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_coord(self):  #
#         return self.__x, self.__y
#
#     def set_coord(self, x, y):  # Установить
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата должна быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата должна быть числом")
#
#
# p1 = Point("5", 10)
# # # print(p1.get_coord())
# # p1.set_coord(100, 200)
# # print(p1.get_coord())
# # print(p1.get_x())
# # print(p1.get_y())
# # print(p1.__dict__)
# # print(p1._Point__x)
# #  Модификаторы доступа public \protected _\private __


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())
# # print(p1.get_y())
# p1.x = 100
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.__kg, "кг =>", end=" ")
#         print(self.to_pounds(), "Количество фунтов")
#
#
# weight = KgToPounds(12)
# # print(weight.kg, "кг =>", end=" ")
# # print(weight.to_pounds(), "Количество фунтов")
# weight.print_data()
# weight.kg = 41
# # print(weight.kg, "кг =>", end=" ")
# # print(weight.to_pounds(), "Количество фунтов")
# weight.print_data()
# weight.kg = float(input("Введите кг"))
# weight.print_data()


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p2.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Tools:
#     @staticmethod
#     def maximum(my_list):
#         return max(my_list)
#
#     @staticmethod
#     def minimum(my_list):
#         return min(my_list)
#
#     @staticmethod
#     def middle(my_list):
#         return sum(my_list) / len(my_list)  # среднее арифметическое
#
#     @staticmethod
#     # def factorial(number):
#     #     if number == 1:
#     #         return 1
#     #     else:
#     #         return Tools.factorial(number - 1) * number
#     def factorial(number):
#         fact = 1
#         for i in range(1, number + 1):
#             fact *= i
#
#         return fact
#
# print(f'Максимальное число: {Tools.maximum([3, 5, 7, 9])}')
# print(f'Минимум число: {Tools.minimum([3, 5, 7, 9])}')
# print(f'Среднее арифметическое: {Tools.middle([3, 5, 7, 9])}')
# print(f'Факториал числа {5}: {Tools.factorial(5)}')


# class Square:
#     count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))

# from math import sqrt
#
#
# class Square:
#     count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.count
#
#
# print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
# print('Площадь квадрата:', Square.square_area(7))
# print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
# print('Количество подсчетов площади:', Square.get_count())
# print(Square.square_triangle1(3, 4, 5))

from math import sqrt


class Square:
    __count = 0

    @staticmethod
    def square_triangle1(a, b, c):
        Square.__count += 1
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def square_triangle2(a, b):
        Square.__count += 1
        return 0.5 * a * b

    @staticmethod
    def square_area(a):
        Square.__count += 1
        return a * a

    @staticmethod
    def square_rectangle(a, b):
        Square.__count += 1
        return a * b

    @staticmethod
    def get_count():
        return Square.__count


print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
print('Площадь квадрата:', Square.square_area(7))
print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
print('Количество подсчетов площади:', Square.get_count())
