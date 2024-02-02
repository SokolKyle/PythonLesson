def negative_numbers(data, index=0):
    if index == len(data):
        return 0

    current_number = data[index]
    count = 1 if current_number < 0 else 0

    return count + negative_numbers(data, index + 1)


data = [-2, 3, 8, -11, -4, 6, 5, 13, -25, 40]
negative = negative_numbers(data)
print("Количество отрицательных чисел:", negative)
