import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def diagonal(self):
        return math.sqrt(self.height ** 2 + self.width ** 2)

    def draw(self):
        for _ in range(self.height):
            print('* ' * self.width)

    def display_info(self):
        print("Высота прямоугольника:", self.height)
        print("Ширина прямоугольника:", self.width)
        print("Площадь прямоугольника:", self.area())
        print("Периметр прямоугольника:", self.perimeter())
        print("Гипотенуза прямоугольника:", "{:.2f}".format(self.diagonal()))
        print("Прямоугольник:")
        self.draw()


# Создаем объект прямоугольника
rectangle = Rectangle(3, 9)

# Вызываем метод для вывода информации
rectangle.display_info()
