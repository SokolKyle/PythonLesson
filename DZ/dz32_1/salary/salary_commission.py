# import salary_employee
from salary import salary_employee


class SalaryCommission(salary_employee.SalaryEmployee):
    """Торговые представители с фиксированной зарплатой + комиссия"""

    def __init__(self, id_employee, name, weekly_salary, commission):
        super().__init__(id_employee, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission
