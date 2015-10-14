from math import sqrt


def special_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(1, n):
            if a ** 2 + b ** 2 == (n - a - b) ** 2:
                c = int(sqrt(a ** 2 + b ** 2))
                return a * b * c
    return None


print special_pythagorean_triplet(1000)
