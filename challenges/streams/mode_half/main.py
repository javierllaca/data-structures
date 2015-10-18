"""
You are given a finite stream of integers and know that an integer k will make
up at least half of those integers. Using constant space, find k.
"""


def mode_half(stream):
    curr, count = None, 0
    for item in stream:
        if count == 0:
            curr = item
        if item == curr:
            count += 1
        elif item != curr:
            count -= 1
    return curr


a = [0, 1, 2, 2, 2, 2, 3, 4]
print mode_half(a)
