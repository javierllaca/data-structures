def union(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        a1, b1 = l1[i]
        a2, b2 = l2[j]
        if b1 < a2:
            a, b = a1, b1
            i += 1
        elif b2 < a1:
            a, b = a2, b2
            j += 1
        else:
            a, b = min(a1, a2), max(b1, b2)
            if b == b1:
                j += 1
            if b == b2:
                i += 1
        merge(a, b, res)
    while i < len(l1):
        a, b = l1[i]
        merge(a, b, res)
        i += 1
    while j < len(l2):
        a, b = l2[j]
        merge(a, b, res)
        j += 1
    return res


def merge(a, b, stack):
    if stack and a < stack[-1][1]:
        stack[-1] = stack[-1][0], b
    else:
        stack.append((a, b))


l1 = [(0, 4), (6, 10)]
l2 = [(1, 2), (5, 7), (11, 13)]

assert union(l1, l2) == [(0, 4), (5, 10), (11, 13)]


l1 = [(0, 3), (4, 10)]
l2 = [(2, 5), (6, 8), (9, 10)]

assert union(l1, l2) == [(0, 10)]
