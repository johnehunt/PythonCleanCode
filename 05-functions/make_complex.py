def make_complex1(*args):
    x, y = args
    return dict(**locals())


def make_complex2(x, y):
    return {'x': x, 'y': y}


print(make_complex1(5, 6))
print(make_complex2(5, 6))