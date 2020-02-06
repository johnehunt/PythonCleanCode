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

print(complex_function(1, 2, 3))
print(complex_function(1, None, 3))

print(complex_function2(1, 2, 3))
print(complex_function2(1, None, 3))