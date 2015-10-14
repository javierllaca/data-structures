from random import randrange
from time import time


def add(a, b):
    result = a ^ b
    carry = (a & b) << 1
    if carry != 0:
        return add(result, carry)
    return result


numbers = [
    int(''.join([
        str(randrange(10))
        for i in range(10000)
    ]))
    for i in range(10000)
]


def benchmark(f, *args):
    start = time()
    res = f(*args)
    end = time()
    return res, end - start


s1, t1 = benchmark(lambda x: reduce(add, x), numbers)
s2, t2 = benchmark(sum, numbers)

assert s1 == s2

print t1, t2
