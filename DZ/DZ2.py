month = int(input("Введите номер месяца:"))
if 1 <= month <= 2 or month == 12:
    print("Ваш месяц зимний - ", end="")
    if month == 1:
        print("Январь")
    if month == 2:
        print("Февраль")
    if month == 12:
        print("Декабрь")
elif 2 < month < 6:
    print("Ваш месяц весенний - ", end="")
    if month == 3:
        print("Март")
    if month == 4:
        print("Апрель")
    if month == 5:
        print("Май")
elif 5 < month < 9:
    print("Ваш месяц летний - ", end="")
    if month == 6:
        print("Июнь")
    if month == 7:
        print("Июль")
    if month == 8:
        print("Август")
elif 8 < month < 12:
    print("Ваш месяц осенний - ", end="")
    if month == 9:
        print("Сентябрь")
    if month == 10:
        print("Октябрь")
    if month == 11:
        print("Ноябрь")
else:
    print("Такого месяца не существует!")
