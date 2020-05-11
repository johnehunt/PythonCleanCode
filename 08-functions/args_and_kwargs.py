def printall(*args, **kwargs):
    # Handle the args values
    print('args:')
    for arg in args:
        print(arg)
    print('-' * 20)
    # Handle the key value pairs in kwargs
    print('kwargs:')
    for arg in kwargs.values():
        print(arg)


printall(1, 2, 3, a="John", b="Hunt")
