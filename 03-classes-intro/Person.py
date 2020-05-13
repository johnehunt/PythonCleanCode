""" Module to define the Person concept """


class InvalidAgeError(Exception):
    """ Valid Ages must be between 0 and 120 """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'InvalidAgeError(' + str(self.value) + ')'


class Person(object):

    # Class variable
    instance_count = 0
    # Class constant
    MAXIMUM_AGE = 120
    MINIMUM_AGE = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count = cls.instance_count + 1

    def __init__(self, name, age):
        Person.increment_instance_count()
        self.__name = name
        self.age = age
        self._address = None
        self.rate = 5.5

    def birthday(self):
        self.__age = self.__age + 1
        print('Happy Birthday', self.__name, 'you are ', self.__age)

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
        if Person.MINIMUM_AGE <= value < Person.MAXIMUM_AGE:
            self.__age = value
        else:
            raise InvalidAgeError(value)
        print('Well that was nice')

    def __str__(self):
        return 'Person: ' + self.__name + ' is ' + str(self.__age)


p1 = Person('John', 1)
try:
    print(p1)
    p1.age = -1
except InvalidAgeError as e:
    print(e)





