def factorial_trailing_zeroes(n):
    """Returns the number of trailing zeroes in n factorial"""
    zeroes = 0
    for i in range(5, n + 1, 5):
        while i % 5 == 0:
            zeroes += 1
            i /= 5
    return zeroes


def trailing_zeroes(n):
    """Returns the number of trialing zeroes in n"""
    str_n = str(n)
    i = len(str_n) - 1
    while str_n[i] == '0':
        i -= 1
    return len(str_n) - 1 - i


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def test_trailing_zeroes():
    for i in range(10):
        print 10 ** i, trailing_zeroes(10 ** i)


def test_factorial_trailing_zeroes():
    for i in range(1000):
        assert trailing_zeroes(factorial(i)) == factorial_trailing_zeroes(i)
