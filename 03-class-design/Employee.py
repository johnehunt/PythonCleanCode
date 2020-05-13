""" Example illustrating a class that exhibits the open-closed rule
    That is it is a class that is open for extension, but closed as
    no changes need to be made to the soruce code to extend it. """


class Employee(object):
    """ Extendable by providing a bonus_calculation function.
    This function takes hours worked and rate paid per hour. """

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
        self.bonus_calculation = None

    def calculate_pay(self):
        return self.hours * self.rate

    def set_bonus_calculation(self, bonus_function):
        self.bonus_calculation = bonus_function

    def calculate_bonus(self):
        if self.bonus_calculation is None:
            return 0
        return self.bonus_calculation(self.hours, self.rate)


employee = Employee('John', 40, 5.15)
employee.set_bonus_calculation(lambda h, r: h * r * 0.10)

print('employee.calculate_pay():', employee.calculate_pay())
print('employee.calculate_bonus():', employee.calculate_bonus())

employee.set_bonus_calculation(lambda h, r: h * r * 0.30)
print('employee.calculate_pay():', employee.calculate_pay())
print('employee.calculate_bonus():', employee.calculate_bonus())
