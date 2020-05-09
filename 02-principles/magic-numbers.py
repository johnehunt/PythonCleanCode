from random import randint

a = []
cards = []


def swap_entries(array, x, y):
    pass


# What does this mean?
for i in range(1, 52):
    j = (i + randint(1, 52) - 1) - 1
    swap_entries(a, i, j)

# More meangful?
DECK_SIZE = 52
for i in range(1, DECK_SIZE):
    j = (i + randint(1, DECK_SIZE) - 1) - 1
    swap_entries(cards, i, j)
