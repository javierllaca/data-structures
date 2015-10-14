def prime_factors(n):
    factors = []
    if n > 1:
        i = 2
        while n % i != 0:
            i += 1
        factors.append(i)
        factors.extend(prime_factors(n / i))
    return factors

print max(prime_factors(600851475143l))
