quantity = int(input("Введите кол-во символов: "))
symbol = input("Введите тип символа: ")
print(" 0 - горизонтальная \n 1 - вертикальная")
line = int(input("Введите ориентацию линии"))
i = 0

while i < quantity:
    if line == 0:
        print(symbol, end="")
        i += 1
    elif line == 1:
        print(symbol)
        i += 1
    else:
        print("Введенное значение ориентации недопустимо")

