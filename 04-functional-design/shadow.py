# Example fo what to do when shadowing builtin functions
# Implementring a function bin to throw things away
# But there is a built in function bin that
# converts an integer number to a binary string prefixed with “0b”


def bin(thing):
    del thing


print(bin(23))
