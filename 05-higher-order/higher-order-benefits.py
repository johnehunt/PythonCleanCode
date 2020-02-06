data = [1, 3, 4, 6, 7, 9, 11, 12]
print('data:', data)

# Filter for even numbers using a lambda function
d1 = list(filter(lambda i: i % 2 == 0, data))
print('d1:', d1)

d2 = []
for i in data:
    if i % 2 == 0:
        d2.append(i)

print('d2:', d2)
