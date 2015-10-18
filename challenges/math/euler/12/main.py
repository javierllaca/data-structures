def divisors(n):
    d = 1
    for e in prime_factors(n).values():
        d *= e + 1
    return d


def increment_key(d, k, i=1):
    if k in d:
        d[k] += i
    else:
        d[k] = i


def prime_factors(n):
    factors = {}
    if n > 1:
        i = 2
        while n % i != 0:
            i += 1
        increment_key(factors, i)
        for k, v in prime_factors(n / i).items():
            increment_key(factors, k, v)
    return factors


t, d, i = 1, 1, 2

while d < 500:
    t += i
    d = divisors(t)
    i += 1

print t
