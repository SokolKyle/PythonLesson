# def mult(t):
#     return t * 2
#
#
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst1))
# print(lst2)

#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)


# t1 = [1, 2, 3]
# t2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, t1, t2))
# print(res)


# t = ('abcd', 'abc', 'asdfg', 'def', 'grt')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [66, 90, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)


# def hello():
#     return 'Hello, I am func "super_func"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
# super_func(hello)


# def my_decorator(func):
#     def wrap():
#         print("Код до функции -->")
#         func()
#         print("Код после функции -->")
#     return wrap
#
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)


# def my_decorator(func):
#     def wrap():
#         print("*" * 30)
#         func()
#         print("=" * 30)
#     return wrap
#
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
# func_test()
# # test = my_decorator(func_test)
# # test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap()
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap()
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
# print(hello)


# def cnt(fn):
#     count = 0
#     def wrap(arg1, arg2):
#         nonlocal count
#         count = count + 1
#         fn(arg1, arg2)
#         print("Вызов функции:", count, "\n", "*" * 20, sep="")
#     return wrap
#
# @cnt
# def hello(a, b):
#     print("Hello,", a, "\nHello,", b)
#
#
# hello("Python", "JavaScript")
# hello('one', 'two')
# # hello()


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#         return wrap
#     return args_dec
#
# @decor("сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


def multiplay(arg):
    def test(fn):
        def wrap(x):
            return fn(x) * arg
        return









