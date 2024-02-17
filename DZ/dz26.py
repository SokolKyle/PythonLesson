class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @name.deleter
    def name(self):
        del self.__name

    @age.deleter
    def age(self):
        del self.__age


p = Person('Irina', 26)
print(p.__dict__)
del p.age
print(p.__dict__)

p.name = 'Igor'
p.age = 31
print(p.name)
print(p.age)
print(p.__dict__)

del p.name
print(p.__dict__)
