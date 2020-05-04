def apply(operation, value1, value2):
    if operation == "+":
        if value1 is not None:
            if value2 is not None:
                return value1 + value2
    elif operation == '-':
        if value1 is not None:
            if value2 is not None:
                return value1 - value2
    raise TypeError("Unknown operation: " + operation)


def apply_ff(operation, value1, value2):
    if value1 is None or value2 is None:
        raise ValueError('Values must be Non None')
    if operation != '+' and operation != '-':
        raise TypeError("Unknown operation: " + operation)

    if operation == "+":
        return value1 + value2
    elif operation == '-':
        return value1 - value2


try:
    print(apply('+', 3, 4))
    print(apply('*', 3, 4))
except TypeError as error:
    print(error)

try:
    print(apply_ff('+', 3, 4))
    print(apply_ff('*', 3, 4))
except TypeError as error:
    print(error)


def get_property(name):
    return None


def max_connections():
    conn_property = get_property('max-connections')
    if conn_property is None:
        return 10
    else:
        return int(property)


def max_connections_ff():
    conn_property = get_property('max-connections')
    if conn_property is None:
        raise ValueError("Missing property max connections")
    else:
        return int(property)


print('max_connections():', max_connections())

try:
    print('max_connections_ff():', max_connections_ff())
except ValueError as error:
    print(error)
