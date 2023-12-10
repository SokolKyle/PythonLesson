a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []

for number in a:
    if a.count(number) > 1:
        if number not in b:
            b.append(number)

print(b)


