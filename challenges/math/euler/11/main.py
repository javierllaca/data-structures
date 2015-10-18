from sys import stdin


def horizontal_products(a, n):
    for i in range(len(a)):
        for j in range(len(a[i]) - n + 1):
            product = 1
            for k in range(n):
                product *= a[i][j + k]
            yield product


def vertical_products(a, n):
    for j in range(len(a[0])):
        for i in range(len(a) - n + 1):
            product = 1
            for k in range(n):
                product *= a[i + k][j]
            yield product


def right_diagonal_products(a, n):
    for i in range(len(a) - n + 1):
        for j in range(len(a[i]) - n + 1):
            product = 1
            for k in range(n):
                product *= a[i + k][j + k]
            yield product


def left_diagonal_products(a, n):
    for i in range(len(a) - n + 1):
        for j in range(n - 1, len(a[i])):
            product = 1
            for k in range(n):
                product *= a[i + k][j - k]
            yield product


a = []
for line in stdin:
    a.append(map(int, line.split()))

max_product = max([p for p in horizontal_products(a, 4)])
max_product = max(max_product, max([p for p in vertical_products(a, 4)]))
max_product = max(max_product, max([p for p in right_diagonal_products(a, 4)]))
max_product = max(max_product, max([p for p in left_diagonal_products(a, 4)]))

print max_product
