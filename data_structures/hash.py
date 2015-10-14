from math import sqrt
from random import randrange


class HashTable:

    def __init__(self, n=1000):
        self.n = next_prime(n)
        self.items = [[] for i in range(self.n)]

    def put(self, key, value):
        i = hash(key) % self.n
        self.items[i].append((key, value))

    def get(self, key):
        bucket = self.items[hash(key) % self.n]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def __str__(self):
        s = ''
        for i in range(len(self.items)):
            s += '{} : {}\n'.format(i, self.items[i])
        return s


def is_prime(n):
    sqrt_n = int(sqrt(n) + 1)
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


def rand_alpha_string(n):
    s = []
    span = ord('z') - ord('a')
    for i in range(n):
        c = chr(ord('a') + randrange(span))
        s.append(c)
    return ''.join(s)


h = HashTable(100)

k_v_pairs = [(rand_alpha_string(5), i) for i in range(100)]

for k, v in k_v_pairs:
    h.put(k, v)

for k, v in k_v_pairs:
    assert h.get(k) == v
