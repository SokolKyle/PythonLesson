# a = ["one", 1, 2, 3, "two", 10, 20, "tree", 15, 36, 60, "four", -20]
#
# d = dict()
# current_key = ""
# for item in a:
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
# print(d)


# d = dict(zip([1, 2, 3], ["one", "two", "tree"]))
# print(d)
#
# a = [1, 2, 3]
# b = ["one", "two", "tree"]
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# b = ["one", "two", "tree"]
# c = zip(a, b)
# print(c)

# d_one = {'name': "Igor", 'last_name': "Petrov", 'job': "Consultant"}
# d_two = {'name': "Irina", 'last_name': "Irisiva", 'job': "Manager"}
#
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

d = [(1, 'one'), (2, 'two'), (3, 'three')]
a, b = zip(*d)
print(a)
print(b)











