# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(type(a))
# # b = tuple()
# # print(type(b))
# # print(b)
# a = 5, 9, 7, 8
# print(a)

from random import randint


# s = tuple(int(input("->")) for i in range(5))

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# # print(t1 + t2)
# # print(t1 * 2)
# t3 = t1 + t2
# print(t3)
# # # t4 = list(t3)
# # # print(t4)
# # print(t3.count("l"))
# # if 'e' in t3:
# #     print(t3.index("e"))
# for i in t3:
#     print(i, end="")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # a = tpl.index(el)
#             # b = tpl.index(el, a + 1) + 1
#             # return tpl[a:b]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


first_name, years, mar = get_user()

print(first_name, years, mar)









