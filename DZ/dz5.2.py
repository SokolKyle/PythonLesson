n = [input("->") for i in range(int(input("Введите кол-во цифр которые будете указывать: ")))]
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i], end=" ")
