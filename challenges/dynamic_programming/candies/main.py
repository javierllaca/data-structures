def min_candies(a):
    indexed_ordering = sorted([(a[i], i) for i in range(len(a))])
    c = [1 for _ in range(len(a))]
    for _, i in indexed_ordering:
        prev, next = c[i] - 1, c[i] - 1
        if i > 0 and a[i] > a[i - 1]:
            prev = c[i - 1]
        if i < len(a) - 1 and a[i] > a[i + 1]:
            next = c[i + 1]
        c[i] = max(prev, next) + 1
    return c


n = int(raw_input())

a = []
for i in range(n):
    a.append(int(raw_input()))

print sum(min_candies(a))
