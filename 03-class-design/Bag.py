class Bag:

    def __init__(self):
        self.__data = []

    # Iterable Protocol
    def __iter__(self):
        return self.__data.__iter__()

    # Len Protocol
    def __len__(self):
        return self.__data.__len__()

    # Membership protocol
    def __contains__(self, member):
        return member in self.__data

    def add(self, value):
        self.__data.append(value)


bag = Bag()
bag.add('Apple')

print(len(bag))
print('Apple' in bag)

for item in bag:
    print(item)
