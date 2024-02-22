# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <=3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# date = [
#     '30.12.2023',
#     '30-12-2023',
#     '01.31.2024',
#     '01.01.20.24',
#     '01.01.4001',
#     '18.02.2024'
# ]
#
# for string_date in date:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print("Nop")
# # date2 = Date.from_string("23.10.2024")
# # print(date2.string_to_db())
# # date3 = Date.from_string("25.12.2023")
# # print(date2.string_to_db())
# # string_date = "23.10.2024"
# # # day, month, year = map(int, string_date.split("."))
# # # print(day, month, year)
# # date = Date(day, month, year)
# # print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счёте: ')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_uer(self):
#         uer_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_uer()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_uer()

import re


class UserData:
    def __init__(self, fio, old, ps, wight):
        # self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_wight(wight)
        # self.verify_ps(ps)

        self.fio = fio
        self.old = old
        self.password = ps
        self.weight = wight

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__password = ps

    @property
    def wight(self):
        return self.__weight

    @wight.setter
    def wight(self, wight):
        self.verify_wight(wight)
        self.__weight = wight



    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 120 лет")

    @staticmethod
    def verify_wight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 кг")

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


p1 = UserData("Соколов Николай Сергеевич", 31, "1234 567567", 80.8)
