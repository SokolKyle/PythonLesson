def arithmetic(fn):
    def wrap():
        x = fn()
        total_sum = sum(x)
        average = total_sum / len(x)
        print("Сумма чисел:", total_sum)
        print("Среднее арифметическое:", average)

    return wrap


@arithmetic
def summa():
    x = []
    print("Введите число для рассчёта среднего арифметического. (Для выхода введите пустую строку)")

    while True:
        number_input = input("Введите число -->")

        if number_input:
            try:
                number = int(number_input)
                x.append(number)
            except ValueError:
                print("Вы ввели не число. Попробуйте снова.")
        else:
            break

    if not x:
        print("Вы ничего не внесли")
        return

    return x


summa()
