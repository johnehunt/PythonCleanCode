class Car:
    """ Car """

    def move(self):
        print('Car - move()')


class Toy:
    """ Toy """

    def move(self):
        print('Toy - move()')


class ToyCar(Car, Toy):
    """ A Toy Car """


class CarToy(Toy, Car):
    """ A Toy Car """


tc = ToyCar()
tc.move()

print('-' * 30)

ct = CarToy()
ct.move()
