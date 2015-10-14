def permutations(xs):
    if len(xs) == 1:
        return [xs]
    ps = []
    for i in range(len(xs)):
        slice = xs[:i] + xs[i + 1:]
        for p in permutations(slice):
            ps.append([xs[i]] + p)
    return ps


for permutation in permutations(range(7)):
    print permutation
