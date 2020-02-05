# Recursive functions
import timeit


def printer_factorial(n, depth=1):
    if n == 1:  # The base case
        print('\t' * depth, 'Returning 1')
        return 1
    else:  # The recursive part
        print('\t' * depth, 'Recursively calling factorial(', n - 1, ')')
        result = n * printer_factorial(n - 1, depth + 1)
        print('\t' * depth, 'Returning:', result)
        return result


print('Calling factorial( 5 )')
print(printer_factorial(5))


def factorial(n):
    if n == 1:  # The base case
        return 1
    else:  # The recursive part
        return n * factorial(n - 1)


# Tail recursive example
def tail_factorial(n, accumulator=1):
    if n == 1:
        return accumulator
    else:
        return tail_factorial(n - 1, accumulator * n)


print(tail_factorial(5))

print('-' * 30)

print('Perform some timing tests')
# timeit runs code number times an returns time taken in
# seconds to run all repetitions
res1 = timeit.timeit(lambda: factorial(5), number=1000000)
print(res1)

res2 = timeit.timeit(lambda: tail_factorial(5), number=1000000)
print(res2)

