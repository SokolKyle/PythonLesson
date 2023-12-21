text_user = input("Введите ваш текст -> ")
count = 0
str_one = set("яиюэоауеёы")
for str_two in text_user:
    if str_two.lower() in str_one:
        count += 1
print("Кол-во гласных букв в тексте = ", (count))
