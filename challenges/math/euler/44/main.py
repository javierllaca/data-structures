from math import sqrt


def is_pentagonal(n):
    p = (sqrt(1 + 24 * n) + 1) / 6
    return p == int(p)


def find():
    i = 1
    while True:
        i += 1
        n = i * (3 * i - 1) / 2
        for j in range(i - 1, 0, -1):
            m = j * (3 * j - 1) / 2
            if is_pentagonal(n - m) and is_pentagonal(n + m):
                return n - m


print find()
