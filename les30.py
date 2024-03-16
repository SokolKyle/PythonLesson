# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
#
# pt1 = Point(1, 2)
#
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + "is player")
#
#
# class Dog(Animal, Pet):
#     def __init__(self):
#         Creature.__init__(self)
#         Animal.__init__(self)
#         Pet.__init__(self)
#         print("Иннициализатор Dog")
#
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# dog.sleep()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y}"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("innit Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("innit pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"print line: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(10, 10), Point(100, 100), "green", 5
# l1.draw()


#  Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="sublog.txt")
#
#
# subclass = MySubClass()
# subclass.display("Строка будет отображаться и запишется в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         print("init goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class Mixinlog:
#     ID = 0
#
#     def __init__(self):
#         print("init MixinLog")
#         Mixinlog.ID += 1
#         self.id = Mixinlog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: Товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, Mixinlog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 3500)
# n.print_info()
# n.save_sell_log()


class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Скунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)


c1 = Clock(100)
c2 = Clock(200)
print(c1.get_format_time())
print(c2.get_format_time())
c3 = c1 + c2
print(c3.get_format_time())