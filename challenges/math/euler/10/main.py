from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes_below(n):
    i = 2
    while i < n:
        if is_prime(i):
            yield i
        i += 1


print sum(primes_below(2000000))
