from abc import ABC, abstractmethod


# class Chess(ABC): # Абстрактный класс
#     @staticmethod
#     def draw():
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         # print('Метод move() в базовом классе')
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Ферзь перемещен на e2e4')
#
#
# # chess = Chess() # Создать экземпляр абстрактного класса нельзя
#
# queen = Queen()
# queen.draw()
# queen.move()

# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_tu_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return round(self.value * Dollar.rate_tu_rub, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, '=', self.convert_to_rub(), 'RUB')
#
#
# class Euro(Currency):
#     rate_tu_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return round(self.value * Euro.rate_tu_rub, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, '=', self.convert_to_rub(), 'RUB')
#
#
# dollars = [
#     Dollar(5),
#     Dollar(10),
#     Dollar(50),
#     Dollar(100),
# ]
#
# euros = [
#     Euro(5),
#     Euro(10),
#     Euro(50),
#     Euro(100),
# ]
#
# print('*' * 50)
# for dollar in dollars:
#     dollar.print_value()
# print('*' * 50)
# for euro in euros:
#     euro.print_value()

# Интерфейс

# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('Grandchild')
#
# father = Father()
# child = Child()
# grandchild = GrandChild()

#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def static_method():
#         print('Статический метод')
#
#     def outer_method(self):
#         print('Метод в наружном классе')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Вложенный класс', MyOuter.age, self.obj.name)
#             MyOuter.static_method()
#             self.obj.outer_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name: ', self.name)
#
#
# outer = Color()
# outer.show()
# # outer.lg.display()

# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Intern'
#
#         def display(self):
#             print('Name:', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Head'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Outer')
#
#     class Inner:
#         def __str__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Inner')
#
#         class InnerClass:
#             def show(self):
#                 print('Inner')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = inner1.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'


cat = Cat('Пушок')
print(cat)
