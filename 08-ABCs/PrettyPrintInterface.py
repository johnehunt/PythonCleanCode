from abc import ABC, abstractmethod
import pprint


class PrettyPrintInterface(ABC):
    """Acts as part of a contract to be implemented
       More formal than a Protocol
       Can check type meets this contract"""
    @abstractmethod
    def pretty_print(self): pass

    @abstractmethod
    def long_print(self): pass


class Person(PrettyPrintInterface):
    def pretty_print(self):
        pprint.pprint(self)

    def long_print(self):
        print('Person')


def main():
    p = Person()

    # Can check to see if type implements interface if required
    if isinstance(p, PrettyPrintInterface):
        p.pretty_print()
        p.long_print()


if __name__ == '__main__':
    main()