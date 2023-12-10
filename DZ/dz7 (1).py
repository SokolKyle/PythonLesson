import random
a = [random.randint(0, 9) for i in range(50)]
c = []

for el in a:
    if el in c:
        c.append(el)
        ix = c.index(el)
        c.pop(ix)

    if len(c) < 10 and el not in c:
        c.append(el)
    if len(c) == 10:
        break
print("Уникальные случайные числа:", c)
