from random import randrange


def shuffle(a):
    for i in range(0, len(a) - 1):
        j = randrange(i, len(a))
        a[i], a[j] = a[j], a[i]


a = range(52)
shuffle(a)
print a
