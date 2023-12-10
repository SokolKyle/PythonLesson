#  Короткий вариант
import random
#
# n1 = int(input("Размер списка: "))
#
# d = random.sample(range(n1), n1)
#
# print("Уникальные случайные числа:", d)

#  Import оставил один на оба кода
#  Длинный вариант

numbers = int(input("Размер списка: "))
a = []
while len(a) < numbers:
    element = random.randint(0, numbers - 1)
    if element not in a:
        a.append(element)

print(a)
