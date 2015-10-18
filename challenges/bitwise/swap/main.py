def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


tests = [
    (1, 2),
    (10, 0),
    (-1, 1)
]

for a, b in tests:
    assert swap(a, b) == (b, a)
