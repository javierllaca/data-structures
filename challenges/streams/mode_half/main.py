"""
You are given a finite stream of integers and know that an integer k will make
up at least half of those integers. Using constant space, find k.
"""

a = [0, 1, 2, 2, 2, 2, 3, 4]

curr, count = None, 0

for i in range(len(a)):
    if count == 0:
        curr = a[i]
    if a[i] == curr:
        count += 1
    elif a[i] != curr:
        count -= 1

print curr
