numbers = [input("->") for i in range(int(input("Введите кол-во цифр которые будете указывать: ")))]
print("Введённые числа:", numbers)
s = count = 0
for i in range(len(numbers)):
    if int(numbers[i]) != 0:
        s += int(numbers[i])
        count += 1
print("Среднее арифметическое число введенных чисел не включая 0 равна:", s / count)
