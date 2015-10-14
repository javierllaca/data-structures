def powerset(s):
    if not s:
        return [[]]
    p = []
    for subset in powerset(s[:-1]):
        p.append(subset)
        p.append(subset + [s[-1]])
    return p


a = [1, 2, 3, 4]
print powerset(a)
