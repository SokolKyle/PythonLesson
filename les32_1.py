# class Integer:
#
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должно быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.__name = "coord_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.x)
# print(p1.__dict__)


#   Metoclass

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
# MyList1 = type(
#     "MyList1",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
# lst1 = MyList1()
# lst1.append(5)
# lst1.append(8)
# print(lst, lst.get_length())
# print(MyList.__dict__)
# print(MyList1.__dict__)


# import geometry.rect
# import geometry.sq
# import geometry.trian
#
# from geometry import rect, sq, trian
#
# # from geometry import *
# print("Hello")
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# class PayrollSystem:
#     def calculate(self, employees):
#         print("Рассчёт заработной платы:")
#         print("=" * 50)
#         for employee in employees:
#             print(f"Зарплата: {employee.id} - {employee.name}")
#
#
# class Employee:
#     def __init__(self, id_employee, name):
#         self.id = id_employee
#         self.name = name
#
#
# class SaleryEmployee(Employee):
#     """Административные работники с фиксированной зарплатой"""
#
#     def __init__(self, id_employee, name, weekly_salary):
#         super().__init__(id_employee, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники с почасовой зарплатой"""
#
#     def __init__(self, id_employee, name, hours_worked, hour_rate):
#         super().__init__(id_employee, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate


from car import electrocar

e_car = electrocar.ElectroCare("Tesla", "T", 2018, 99000)
e_car.show_car()
e_car.description_battary()
