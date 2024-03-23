# #  Функторы
#
#
# # class Counter:
# #     def __init__(self):
# #         self.__count = 0
# #
# #     def __call__(self, *args, **kwargs):
# #         self.__count += 1
# #         print(self.__count)
# #
# #
# # c1 = Counter()
# # c1()
# # c1()
# # c1()
# # c2 = Counter()
# # c2()
# # c2()
# # c1()
#
#
# # class StripChars:
# #     def __init__(self, chars):
# #         self.__chars = chars
# #
# #     def __call__(self, *args, **kwargs):
# #         if not isinstance(args[0], str):
# #             raise ValueError("Argument str!!!")
# #         return args[0].strip(self.__chars)
# #
# #
# # s1 = StripChars("?:!.; ")
# # print(s1(" Hello world!  "))
#
# # class Power:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     def __call__(self, x, y):
# #         return self.func(x, y) ** 2
# #
# #
# # @Power
# # def my_func(a, b):
# #     return a * b
# #
# #
# # print(my_func(2, 3))
#
#
# # Функторы
# # class Counter:
# #     def __init__(self):
# #         self.__count = 0
# #
# #     def __call__(self, *args, **kwargs):
# #         self.__count += 1
# #         print(self.__count)
# #
# #
# # c1 = Counter()
# #
# # c1()
# # c1()
# # c1()
# # c2 = Counter()
# # c2()
# # c2()
#
# # class StripChars:
# #     def __init__(self, chars):
# #         self.__chars = chars
# #
# #     def __call__(self, *args, **kwargs):
# #         if not isinstance(args[0], str):
# #             raise ValueError('Аргумент должен быть строкой')
# #         return args[0].strip(self.__chars)
# #
# #
# # s1 = StripChars('?:!.; ')
# # print(s1(' Hello World! '))
#
# # def strip_chars(chars)
#
# # class MyDecorator:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     def __call__(self):
# #         print('Перед вызовом функции')
# #         self.func()
# #         print('После вызова функции')
# #
# #
# # @MyDecorator
# # def function():
# #     print('Текст функции')
# #
# #
# # function()
#
#
# # class MyDecorator:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     # def __call__(self, x, y):
# #     #     print('Перед вызовом функции')
# #     #     res = self.func(x, y)
# #     #     print('После вызова функции')
# #     #     return res
# #
# #     def __call__(self, x, y):
# #         return (f'Перед вызовом функции\n'
# #                 f'{self.func(x, y)}\n'
# #                 f'После вызова функции')
# #
# # @MyDecorator
# # def function(a, b):
# #     return a * b
# #
# #
# # print(function(2, 5))
#
# # class Power:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     def __call__(self, x, y):
# #         return (f'Перед вызовом функции\n'
# #                 f'{self.func(x, y) ** 2}\n'
# #                 f'После вызова функции')
# #
# #
# # @Power
# # def function(a, b):
# #     return a * b
# #
# #
# # print(function(5, 5))
#
# # class MyDecorator:
# #     def __init__(self, arg):
# #         self.name = arg
# #
# #     def __call__(self, func):
# #         def wrap(*args, **kwargs):
# #             return (f'Перед вызовом функции {self.name}\n'
# #                     f'{func(*args, **kwargs)}\n'
# #                     f'После вызова функции')
# #
# #         return wrap
# #
# #
# # @MyDecorator(' два параметра')
# # def function(a, b):
# #     return a * b
# #
# #
# # @MyDecorator(' три параметра')
# # def function1(a, b, c):
# #     return a * b * c
# #
# #
# # print(function(2, 5))
# # print(function1(2, 5, 2))
#
#
# # class Power:
# #     def __init__(self, num):
# #         if not isinstance(num, int):
# #             raise ValueError('Степень должна быть целым положительным числом')
# #         self.num = num
# #
# #     def __call__(self, func):
# #         def wrap(*args, **kwargs):
# #             return f'Результат: {func(*args, **kwargs) ** self.num}\n'
# #
# #         return wrap
# #
# #
# # @Power(3)
# # def function(a, b):
# #     return a * b
# #
# #
# # print(function(2, 2))
#
# # Декорирование методов
#
# # def dec(fn):
# #     def wrap(*args, **kwargs):
# #         print('*' * 20)
# #         fn(*args, **kwargs)
# #         print('*' * 20)
# #
# #     return wrap
# #
# #
# # class Person:
# #     def __init__(self, name, surname):
# #         self.name = name
# #         self.surname = surname
# #
# #     @dec
# #     def info(self):
# #         print(f'{self.name} {self.surname}')
# #
# #
# # p1 = Person('Виталий', 'Карасев')
# # p1.info()
#
# # def decorator(cls):
# #     class Wrapper(cls):
# #         def double(self, value):
# #             return value * 2
# #
# #     return Wrapper
# #
# #
# # @decorator
# # class ActualClass:
# #     def __init__(self):
# #         print('Инициализатор ActualClass')
# #
# #     def quad(self, value):
# #         return value * 4
# #
# #
# # obj = ActualClass()
# # print(obj.quad(4))
# # print(obj.double(4))
# # print(type(obj))
#
# # Дескриптор (__get__, __set__, __delete__, __set_name__)
#
# # class String:
# #     def __init__(self, value=None):
# #         if value:
# #             self.set(value)
# #
# #     def set(self, value):
# #         if not isinstance(value, str):
# #             raise ValueError(f'{value} должно быть строкой')
# #         self.__value = value
# #
# #     def get(self):
# #         self.__value
# #
# #
# # class Person:
# #     def __init__(self, name, surname):
# #         self.name = String(name)
# #         self.surname = String(surname)
# #
# #     # @property
# #     # def name(self):
# #     #     return self.__name
# #     #
# #     # @name.setter
# #     # def name(self, value):
# #     #     if not isinstance(value, str):
# #     #         raise ValueError(f'{value} должно быть строкой')
# #     #     self.__name = value
# #     #
# #     # @property
# #     # def surname(self):
# #     #     return self.__surname
# #     #
# #     # @name.setter
# #     # def surname(self, value):
# #     #     if not isinstance(value, str):
# #     #         raise ValueError(f'{value} должно быть строкой')
# #     #     self.__surname = value
# #
# #
# # p = Person('Ivan', 'Petrov')
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# p = Person('Ivan', 'Petrov')
# # p.surname = 5
# print(p.name)
# print(p.surname)
# print(p.__dict__)
