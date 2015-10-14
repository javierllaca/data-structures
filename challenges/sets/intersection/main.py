def intersect_a(a, b):
    a.sort()
    b.sort()
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        while a[i] < b[j]:
            i += 1
        while b[j] < a[i]:
            j += 1
        res.append(a[i])
        i += 1
        j += 1
    return res


def intersect_b(a, b):
    elems = {}
    res = []
    for elem in a:
        elems[elem] = 1
    for elem in b:
        if elem in elems and elems[elem] == 1:
            elems[elem] += 1
            res.append(elem)
    return res


print intersect_a(range(10), range(5, 10))
print intersect_b(range(10), range(5, 10))
