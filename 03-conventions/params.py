def make_complex1(*args):
    x, y = args
    return dict(**locals())


def make_complex2(x, y):
    return {'x': x, 'y': y}


print(make_complex1(1, 2))
print(make_complex2(1, 2))