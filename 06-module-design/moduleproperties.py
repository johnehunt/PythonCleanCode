import utils, sys

print('main Package Properties')
print('__name__):', __name__)
print('__doc__:', __doc__)
print('__file__:', __file__)

print('-' * 30)

print('utils Package Properties')
print('utils.__name__:', utils.__name__)
print('utils.__doc__:', utils.__doc__)
print('utils.__file__:', utils.__file__)
print('utils.__spec__:', utils.__spec__)

print(dir(utils))

print('-' * 30)

print('sys Package Properties')
print('sys.version: ', sys.version)
print('sys.__name__:', sys.__name__)
print('sys.__doc__:', sys.__doc__)
print('sys.__spec__:', sys.__spec__)