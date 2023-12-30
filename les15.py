# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda x=2, y=5: x ** 2 + y ** 2)())
# print((lambda x=2, y=5: x ** 2 + y ** 2)(10, 20))
# print((lambda x=2, y=5: x ** 2 + y ** 2)(y=10))

# print((lambda *args: args)(1, 2, 3, 4, 5))

# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for i in y:
#     print(i("abc___"))


# def outer(n):
#     def inner(x):
#         return x + n
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))
#
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer2(5)
# print(f2(10))
#
# print((lambda n: lambda x: x + n)(5)(10))
# print((lambda n: lambda x: lambda y: x + n + y)(2)(4)(6))


# def func(item):
#     return item[1]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# d1 = dict(lst)
# print(d1)


# players = [
#     {'name': 'Антон', 'last name': 'Бириков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Фёдор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res2 = sorted(players, key=lambda item: item['raiting'], reverse=True)

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]
#
# print(a[3](5, 2))


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
#
# d[6]()


# print((lambda a, b, c: a if a < b or a < c else b < c)(15, 16, 17))
# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(18, 19, 17))







