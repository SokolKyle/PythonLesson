# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
#
# print(lst[0])
# print(d['one'])


# d = {}
# print(d)
# print(type(d))

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# x = 1
# for key in d:
#     x *= d[key]
# print('Произведение', x)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой эелемент исключить?"))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['core -i3-4330', 9, 4500],
#     '2': ['core -i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['core -i5-340G', 5, 6400]
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Кол-во: '))
#         goods[n][1] += qty
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")


d = {'a': 1, 'b': 2, 'c': 3}
# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i, j in d.items():
#     print(i, "->", j)

# print(d['b'])
# value = d.get('b')
# print(value)














