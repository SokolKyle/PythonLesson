class ValidOrderFields:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f'{self.__name} должно быть целым положительным числом')
        instance.__dict__[self.__name] = value


class Order:
    count = ValidOrderFields()
    price = ValidOrderFields()

    def __init__(self, title, count, price):
        self.title = title
        self.count = count
        self.price = price


order = Order('Apple', 5, 10)
print(f'{order.count * order.price}')


