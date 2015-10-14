from random import randrange


def two_random():
    x = randrange(1000, 10000)
    return x / 200, x % 100 / 2

print two_random()
