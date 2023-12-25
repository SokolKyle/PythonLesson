num_students = int(input("Введите количество студентов: "))

students = {}

for i in range(num_students):
    name = input(f"{i+1}-й студент: Введите фамилию: ")
    score = int(input("Балл: "))
    students[name] = score

average_score = sum(students.values()) / num_students

print("Средний балл:", average_score)

print("Студенты с баллом выше среднего:")
for name, score in students.items():
    if score > average_score:
        print(name)