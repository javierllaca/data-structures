def intersection(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        a1, b1 = l1[i]
        a2, b2 = l2[j]
        if b1 < a2:
            i += 1
        elif b2 < a1:
            j += 1
        else:
            res.append((max(a1, a2), min(b1, b2)))
            i += 1
            j += 1
    return res


l1 = [(0, 4), (5, 9)]
l2 = [(2, 3), (4, 6), (8, 9)]

print intersection(l1, l2)
