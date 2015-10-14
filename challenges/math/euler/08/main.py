from sys import stdin


def max_inner_product(s, n):
    max_product = float('-inf')
    for i in range(len(s) - n):
        product = 1
        for j in range(i, i + n):
            product *= int(s[j])
        max_product = max(max_product, product)
    return max_product


s = ''
for line in stdin:
    s += line.strip()

print max_inner_product(s, 13)
