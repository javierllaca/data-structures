from sys import stdin


def children(a, i, j):
    if i < len(a) - 1:
        if j < len(a[i + 1]):
            yield i + 1, j
        if j < len(a[i + 1]) + 1:
            yield i + 1, j + 1


def maximum_path_sum(a, i=0, j=0):
    if i < len(a):
        max_sum = 0
        for x, y in children(a, i, j):
            max_sum = max(max_sum, maximum_path_sum(a, x, y))
        return a[i][j] + max_sum
    return 0


a = []
for line in stdin:
    a.append(map(int, line.split()))

print maximum_path_sum(a)
