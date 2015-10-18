from algorithms.number_theory import is_prime, are_coprime, modexp, modinv
from random import choice, randrange


def random_prime(i, j):
    """Returns a random prime number between i and j"""
    primes = [n for n in range(i, j) if is_prime(n)]
    return choice(primes)


def random_coprime(n, k):
    """Returns a random integer less than k that is coprime with n"""
    coprimes = [m for m in range(2, k) if are_coprime(n, m)]
    return choice(coprimes)


def encode(m, e, n):
    """Encode m with public key (e, n)"""
    return modexp(m, e, n)


def decode(c, d, n):
    """Decode c with private key (d, n)"""
    return modexp(c, d, n)


def generate_keys(i, j):
    """Returns (n, e, d), where (e, n), (d, n) are public and private keys"""
    p, q = random_prime(i, j), random_prime(i, j)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random_coprime(phi, phi)
    d = modinv(e, phi)
    return n, e, d


n, e, d = generate_keys(256, 512)

# test
m = randrange(n)
c = encode(m, e, n)
assert m == decode(c, d, n)
