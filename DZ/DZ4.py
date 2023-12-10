number_x = 13
i = 1

while True:
    number_y = int(input("Угадайте загаданное число в диапазоне от 1 до 100 (введите 0 для выхода):"))

    if number_y == 0:
        print("Вы вышли из игры.")
        break
    elif number_y < 1 or number_y > 100:
        print("Число не в диапазоне от 1 до 100.")
        i += 1
        continue

    if number_y < number_x:
        print("Загаданное число больше")
    elif number_y > number_x:
        print("Загаданное число меньше")
    else:
        print("Верно! Вы угадали число с", i, "попытки.")
        break

    i += 1
