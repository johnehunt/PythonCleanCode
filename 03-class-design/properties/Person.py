class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        """ The docstring for the age property """
        print('In age method')
        return self.__age

    @age.setter
    def age(self, value):
        print('In set age method')
        if isinstance(value, int) & value > 0 & value < 120:
            self.__age = value

    @property
    def name(self):
        print('In name')
        return self.__name

    def __str__(self):
        return 'Person[' + \
               str(self.__name) + \
               '] is ' + \
               str(self.__age)


person = Person('John', 54)
print(person)
print(person.age)
print(person.name)
person.age = 21
print(person)
