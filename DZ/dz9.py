from random import randint


def create_tuple(start, stop, size):
    return tuple(randint(start, stop) for _ in range(size))


tpl1 = create_tuple(0, 5, 10)
tpl2 = create_tuple(-5, 0, 10)
tpl3 = tpl1 + tpl2
zero = tpl3.count(0)

print(tpl1)
print(tpl2)
print(tpl3)
print("Кол-во нулей в третьем списке =", zero)


