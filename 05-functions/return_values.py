def complex_function(a, b, c):
    if not a:
        return None
    if not b:
        return None
    x = a + b + c
    if not x:
        return None
    return x


def complex_function2(a, b, c):
    result = None
    if a and b:
        result = a + b + c
    return result


def complex_function3(a, b, c):
    if not a and not b:
        return None
    return a + b + c


print('complex_function(1, 2, 3):', complex_function(1, 2, 3))
print('complex_function2(1, 2, 3):', complex_function2(1, 2, 3))
