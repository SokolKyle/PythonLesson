# class Point():
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'Координаты точки: ({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print('Инициализатор базового класса Prop')
#
#     def _get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args) -> None:
#         super().__init__(*args)
#         # Prop.__init__(self, *args)
#         print('Перепредеоленyый инициалаизатор Line')
#
#
#     def draw_line(self) -> str:
#         return f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._get_width()}'
#
#
# class Rect(Prop):
#     def draw_rect(self) -> str:
#         return f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._get_width()}'
#
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.draw_line())
# rect = Rect(Point(1, 2), Point(10, 20))
# print(rect.draw_rect())


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, new_color):
#         self.__color = new_color
#
#     @color.deleter
#     def color(self):
#         del self.__color
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self.__width = new_width
#         else:
#             raise ValueError('Некорректное значение ширины')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0 :
#             self.__height = new_height
#         else:
#             raise ValueError('Некорректное значение высоты')
#
#     def area(self):
#         print(f'Площадь {self.color} прямоугольника = ', end='')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.area())

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целочисленными")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.set_coord(Point(15.5, 45), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.set_coord(Point(55.5, 45.6), Point(100, 200))
# rect.draw_rect()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Фон: {self.fon}')
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border_width, border_solid, border_color):
#         super().__init__(width, height)
#         self.border_width = border_width
#         self.border_solid = border_solid
#         self.border_color = border_color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка:\n'
#               f'\tШирина рамки: {self.border_width}\n'
#               f'\tТип рамки: {self.border_solid}\n'
#               f'\tЦвет рамки:{self.border_color}\n'
#               )
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, '1px', 'solid', 'red')
# shape2.show_rect()

# class Vector(list):
#     def __init__(self, lst):
#         super().__init__()
#         self.lst = lst
#
#     def __str__(self):
#         return ' '.join(map(str, self.lst))
#
#
# v = Vector([1, 2, 3])
# print(sum(v))
# print(v)
# print(type(v))

# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата sp должна быть целочисленным значением")
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координата ep должна быть целочисленным значением")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными значениями")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(15, 45), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(55, 55))
# line.draw_line()
# line.set_coord(ep=Point(55, 55))
# line.draw_line()


# Абстрактный метод
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            return True
        return False

    def is_int(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


from abc import ABCMeta, abstractmethod


class Prop(metaclass=ABCMeta):
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coord(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")

    @abstractmethod
    def draw(self):
        pass
        # raise NotImplementedError('В дочернем классе должен быть переопределен метод draw()')


class Line(Prop):
    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Prop):
    def draw(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Ellipse(Prop):
    def draw(self):
        print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")


figs = list()
figs.append(Line(Point(0, 0), Point(10, 10)))
figs.append(Line(Point(10, 10), Point(20, 10)))
figs.append(Rect(Point(50, 50), Point(100, 100)))
figs.append(Ellipse(Point(-10, -10), Point(10, 10)))

for fig in figs:
    fig.draw()
