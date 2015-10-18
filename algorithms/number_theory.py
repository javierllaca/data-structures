from math import sqrt


def gcd(a, b):
    """Euclidean algorithm"""
    return a if b == 0 else gcd(b, a % b)


def egcd(a, b):
    """Extended Euclidean algorithm
    Returns (g, x, y) such that g = gcd(a, b) and ax + by = gcd(a, b)
    """
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b / a) * y, y)


def is_prime(n):
    """Determines whether n is prime"""
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def are_coprime(a, b):
    """Determines whether a and b are coprime"""
    return gcd(a, b) == 1


def modinv(a, m):
    """Computes the modular multiplicative inverse of a mod n"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m


def modexp(a, b, n):
    """Computes a^b % n in O(lg(n))"""
    if b == 0:
        return 1
    t = modexp(a, b / 2, n)
    c = (t * t) % n
    if b % 2 == 1:
        c = (c * a) % n
    return c
