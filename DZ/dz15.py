import math

area = [
    lambda r: math.pi * r ** 2,
    lambda a, b: a * b,
    lambda a, b, h: (a + b) * h / 2
]

shapes = int(input("Выберите фигуру: \n1 - Окружность. \n2 - Прямоугольник. \n3 - Трапеция \n->"))

if shapes == 1:
    radius = float(input("Введите радиус круга --> "))
    print("Площадь окружности =", round(area[0](radius), 4))
elif shapes == 2:
    side_a = float(input("Введите сторону a --> "))
    side_b = float(input("Введите сторону b --> "))
    print("Площадь прямоугольника = ", round(area[1](side_a, side_b), 4))
elif shapes == 3:
    side_a = float(input("Введите сторону a --> "))
    side_b = float(input("Введите сторону b --> "))
    side_h = float(input("Введите высоту --> "))
    print("Площадь трапеции = ", round(area[2](side_a, side_b, side_h), 4))
else:
    print("Такого значения нету")