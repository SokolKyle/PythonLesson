# num = 4321
# print("Исходное число:", num)
# a = num // num
# print(a)
# b = a + 1

# num1 = "2.3"
# num2 = 3
# # res = num1 + num3  #Error
# # res = num1 + str(num2)  # Concat
# res = float(num1) + num2  # sum
#
# print(int(res))
# name = "Николай"
# age = 28
# print("Меня зовут", name + ". Мне", str(age), "лет.")
# print("Меня зовут", name, ". Мне", str(age), "лет.")
# print("Меня зовут" + name + ". Мне" + str(age) + "лет.")
# print("Меня зовут", name, ". Мне", str(age), "лет.", sep=" ")

# name = input("Введите имя:")
# print(name)
# num = input("Вевидите число:")
# power = input("Вевидите степень:")
# res = int(num) ** int(power)
# print("Число", num, "в степени", power, "равно", res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

#  False =>
#
# print(bool("Python")) # True
# print(bool(""))  # False
# print(bool(5)) # True
# print(bool(-5)) #True
# print(bool(0)) # False
# print(bool(False)) # False
# print(bool(None)) # False
#
# test = None
# print(test)None

# a = 10
# b = 5
# c = a == b
# print(a, b, c) # 10 5 False
# Логические операторы or "и" not "не" and"или"
# print(5 - 3 == 2 and 1 + 3 == 4)  # true (true:true)
# print(5 - 3 == 2 and 1 + 3 < 4)  # false (true:false)
# print(5 - 3 > 2 and 1 + 3 < 4)  # false (false:false)
# print(5 - 3 > 2 and 1 + 3 == 4)  # false (false:true)
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # true (true:true)
# print(5 - 3 == 2 or 1 + 3 < 4)  # true (true:false)
# print(5 - 3 > 2 or 1 + 3 < 4)  # false (false:false)
# print(5 - 3 > 2 or 1 + 3 == 4)  # true (false:true)

# not(true) = false
# not(false) = true

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input("Введите свой возрас: "))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# a = 50
# b = 50
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = int(input("Введите сторону1: "))
# b = int(input("Введите сторону2: "))
# c = int(input("Введите сторону3: "))
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == c or b == c:
#     print("равнобедренный")
# else:
#     print("разносторонний")


day = int(input("Введите день недели цифрой: "))
if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
    print("Рабочий день - ", end="")
    if day == 1:
        print("Понедельник")
    if day == 2:
        print("Вторник")
    if day == 3:
        print("Среда")
    if day == 4:
        print("Четверг")
    if day == 5:
        print("Пятница")
elif day == 6 or day == 7:
    print("Выходной день - ")
else:
    print("Такого не существует")
