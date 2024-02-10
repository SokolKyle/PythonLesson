#  ООП
#  Инкапсуляция, наследование и полиморфизм


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(id(p1))
#
# p2 = Point()
# p2.y = 24
# print(p2.x)
# print(p2.y)
# print(id(p2))
# print(id(Point))
# print(p2.__dict__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(
#             f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\n"
#             f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Nikolay", "06.06.1992", "66-66-66", "Russia", "Nyagan", "Stroitelnaya, 1")
# h1.print_info()
# h1.set_address("ul. Lenina, 25")
# print(h1.get_address())
# h1.set_name("Kolya")
# print(h1.get_name())


# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __del__(self):
#         print("Удаление экземпляра:", self)
#
#     def print_info(self):
#         # self.name = name
#         # self.surname = surname
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Viktor", "Resnik")
# p1.print_info()
# p1.add_skill(3)
# p1.__del__()
#
# p2 = Person("Anna", "Dolgich")
# p2.print_info()
# p2.add_skill(2)


class Robot:
    k = 0

    def __init__(self, name):
        self.name = name
        print("Инициализация робота", self.name)
        Robot.k += 1

    def __del__(self):
        print(self.name, "выключается!")

        Robot.k -= 1

        if Robot.k == 0:
            print(self.name, "Он был последним")
        else:
            print("Работающих роботов осталось:", Robot.k)
    def say_hi(self):
        print("Приветствую! Меня зовут:", self.name)


droid1 = Robot('R2-D2')
droid1.say_hi()
print("Число роботов:", Robot.k)
droid2 = Robot('C-3PO')
droid2.say_hi()
print("Число роботов:", Robot.k)
droid3 = Robot('C-3P1')
droid3.say_hi()
print("Число роботов:", Robot.k)

print("\nЗдесь роботы могут сделать какую то работу\n")

print("Роботы закончили свою работу. Давайте их выключим.")
del droid1
del droid2
del droid3
print("Число роботов:", Robot.k)
