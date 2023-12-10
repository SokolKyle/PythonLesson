# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:-6:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# # s[1] = 20
# print(s)
# # # s[4:] = []
# # print(s)
# # s[2:5] = []
# # print(s)
# del s[2:5]
# print(s)

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец
# print(s)
# s.extend([1, 3, 2])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (второй параметр), в заданный индекс (первый параметр)
# s.insert(3, 200)
# s.insert(7, 10)
# s.insert(-1, 100)  # В предпоследний
# s.insert(20, 100)  # попадет в конец списка если задать не существующий индекс
# print(s)

# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     #  s.append(x)
#     s.insert(0, x)
# print(s)


# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число"))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3")
# print(s)

a = [5, 9, 2, 1, 4, 3]
b = [4, 2, 1, 3, 7]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)   # [2, 1, 4, 3]























