""" Contains an example of Monkey Patching"""


class Bag():
    """ Bag doe snot define a method get_length """
    def __init__(self):
        self.data = ['a', 'b', 'c']

    def __getitem__(self, pos):
        return self.data[pos]

    def __str__(self):
        return 'Bag(' + str(self.data) + ')'


b = Bag()
print(b)


def get_length(self):
    """ Function to be used in Monkey pactching the class Bag """
    return len(self.data)


# Monkey patching class
Bag.__len__ = get_length

print(len(b))

Bag.name = 'My Bag'
print(b.name)

b.name = 'Johns Bag'
print(b.name)

b2 = Bag()
print(b2.name)
