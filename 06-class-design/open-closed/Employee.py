class Employee:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate

    def calculate_bonud(self, bonus_func):
        return bonus_func(self.hours, self.rate)

