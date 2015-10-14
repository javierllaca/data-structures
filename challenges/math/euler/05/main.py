def smallest_evenly_divisible(n):
    top = n
    factors = [i for i in range(1, n + 1) if n % i != 0]
    while True:
        if all([n % i == 0 for i in factors]):
            return n
        n += top
    return i

print smallest_evenly_divisible(20)
