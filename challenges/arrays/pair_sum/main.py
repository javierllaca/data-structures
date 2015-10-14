from random import randrange


def pair_sum(a, s):
    """Returns all pairs of integers in a that sum to s. O(n)"""
    a = set(a)
    pairs = []
    for i in a:
        if s - i in a:
            pairs.append((i, s - i))
    return pairs


a = [randrange(100) for i in range(100)]

print pair_sum(a, 100)
