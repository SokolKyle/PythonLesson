name = input("Введите имя сотрудника: ")
age = int(input("Введите возраст сотрудника: "))
salary = int(input("Введите зарплату сотрудника: "))
city = input("Введите город сотрудника: ")

person = {'name': name, 'age': age, 'salary': salary, 'city': city}
new_dict = {'name': person['name'], 'salary': person['salary']}

del person['name']
del person['salary']

print(new_dict)
print(person)
