import math


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return (base * height) / 2


def circle_area(radius):
    return math.pi * radius ** 2


print("Площадь чего нужно найти?")
print("1 - Площадь прямоугольника", "\n2 - Площадь треугольника", "\n3 - Площадь круга")

choice = int(input("Ваш выбор:"))

if choice == 1:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = rectangle_area(length, width)
    print("Площадь прямоугольника: ", area)
elif choice == 2:
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = triangle_area(base, height)
    print("Площадь треугольника: ", area)
elif choice == 3:
    radius = float(input("Введите радиус круга: "))
    area = circle_area(radius)
    print("Площадь круга: ", area)
else:
    print("Неправильный выбор. Пожалуйста, выберете число от 1 до 3.")