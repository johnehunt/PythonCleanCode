""" Module to define the Person concept """


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._address = None
        self.rate = 5.5

    def birthday(self):
        self.__age = self.__age + 1
        print('Happy Birthday', self._name, 'you are ', self.__age)

    def calculate_pay(self, hour):
        return self.rate * hour

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        print('-' * 25)
        return self.__age

    @age.setter
    def age(self, value):
        print('in set for age with ', value)
        if value > 0 and value < 120:
            self.__age = value

person1 = Person('John', 21)
print(person1.age)
print(person1.name)
person1.age = -1

person2 = Person('Denise', 36)
print(person2)
person2.birthday()
