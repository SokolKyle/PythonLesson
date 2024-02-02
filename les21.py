# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
# n1 = int(input("На каком вы этаже?: "))
#
# elevator(n1)



# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# # print(to_str(18, 2))
# # print(to_str(18, 8))
# # print(to_str(18, 16))
# print(to_str(254, 16))
# print(254 % 16)


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
# # print(names[0])
# # print(names[1])
# # print(isinstance(names[0], list))
# # print(isinstance(names[1], list))
# # print(names[1][0])
# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))


# def remove (text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])

# print(remove("Hello\tWorld "))




#Текстовые
#Бинарные

# f = open(r'C:\Users\Учебная\Desktop\виртуалка\pyt\Lesson\test.txt', 'r')   #mode='r'
# f = open(r'test.txt', 'r')   #mode='r'
# print(*f)
# print(f)
#
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)



# f = open(r'test.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()



# f = open(r'test1.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open(r'test1.txt', 'r')
# print(f.readlines())
# f.close()

# f = open('test1.txt', 'r')
# for line in f:
#     print(line)
# f.close()


# f = open('test1.txt', 'r')
# count = 0
# for i in f:
#     print(i)
#     count += 1
#
# f.close()
# print("count =", count)

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!\n")
# f.close()
#
# f = open("xyz.txt", "a")
# f.write("New text.\n")
# f.close()


# f = open("xyz.txt", "w")
# line = ['This is line1\n', 'This is line2\n']
# f.writelines(line)
# f.close()





