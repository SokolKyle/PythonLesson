import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.verify_surname(surname)
        self.__surname = surname

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.varify_num(num)
        self.__num = num

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.verify_percent(percent)
        self.__percent = percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.verify_value(value)
        self.__value = value

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снять!")
        self.print_balance()

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Поле обладатель должно быть строкой")
        f = surname.split()
        if len(f) != 1:
            raise TypeError("Неверный формат")
        letters = "".join(re.findall("[a-zа-яё-]", surname, re.IGNORECASE))
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError("В обладателе можно использовать только буквы и дефис")

    @staticmethod
    def varify_num(num):
        if not isinstance(num, str):
            raise TypeError("Номер должен быть строкой")
        if len(num) != 5:
            raise TypeError("Неверный формат номера")
        for m in num:
            if not m.isdigit():
                raise TypeError("Номер должен быть числом")

    @staticmethod
    def verify_percent(percent):
        if not isinstance(percent, (int, float)):
            raise TypeError("Процент должен быть числом")
        if percent < 0 or percent > 1:
            raise ValueError("Процент должен быть числом от 0 до 1")

    @staticmethod
    def verify_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")

    def print_info(self):
        print('Информация о счете:')
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account("Долгих", "12345", 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_eur()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)