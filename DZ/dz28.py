from math import pi
from abc import ABCMeta, abstractmethod, ABC


class Table(metaclass=ABCMeta):
    def __init__(self, width=None, height=None, radius=None):
        if radius is None:
            self.table_type = 'прямоугольный'
            self.width = width
            self.height = height
        else:
            self.table_type = 'круглый'
            self.radius = radius

    def __str__(self):
        description = f'Форма стола: {self.table_type}\n'
        if self.table_type == 'прямоугольный':
            return (
                    description +
                    f'Ширина стола: {self.width}\n'
                    f'Высота стола: {self.height}'
            )
        else:
            return (
                    description +
                    f'Радиус стола: {self.radius}'
            )

    @abstractmethod
    def square(self):
        pass


class RectangleTable(Table):
    def __init__(self, width, height):
        super().__init__(
            width=width,
            height=height
        )

    def square(self):
        return self.width * self.height


class CircleTable(Table):
    def __init__(self, radius):
        super().__init__(radius=radius)

    def square(self):
        return round(pi * self.radius ** 2, 2)


tables = [
    RectangleTable(20, 10),
    RectangleTable(20, 20),
    CircleTable(radius=20),
]

for table in tables:
    print(table)
    print(f'Площадь стола: {table.square()}\n')
