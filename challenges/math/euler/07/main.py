from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    i, j = 2, 1
    while j < n:
        i += 1
        if is_prime(i):
            j += 1
    return i


print nth_prime(10001)
