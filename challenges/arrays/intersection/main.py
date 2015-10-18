def intersection(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return c


print intersection(range(10), range(5, 15))
