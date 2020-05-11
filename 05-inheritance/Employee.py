class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, emp_id, name, role):
        super.__init__(name)
        self.employee_id = emp_id
        self.role = role


class Role:
    def __init__(self, description):
        self.description = description


class Developer(Role):
    def __init__(self, description, languages):
        self.description = description
        self.languages = languages


class Sales(Role):
    def __init__(self, description, region):
        self.description = description
        self.region = region


class Manager(Role):
    def __init__(self, description, department):
        self.description = description
        self.department = department


employee = Employee('123', 'John', Developer('Junior', ['Python', 'Java']))
