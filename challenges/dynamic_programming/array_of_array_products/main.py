def array_of_array_products(a):
    res = []
    p1, p2 = 1, 1
    l, r = [], []
    for i in range(len(a)):
        l.append(p1)
        r.append(p2)
        p1 *= a[i]
        p2 *= a[-i - 1]
    for i in range(len(a)):
        res.append(l[i] * r[len(a) - i - 1])
    return res


assert array_of_array_products([2, 7, 3, 4]) == [7*3*4, 2*3*4, 2*7*4, 2*7*3]
