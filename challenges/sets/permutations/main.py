def permutations(s):
    if not s:
        return [[]]
    perms = []
    for i in range(len(s)):
        for perm in permutations(s[:i] + s[i + 1:]):
            perms.append(perm + [s[i]])
    return perms


a = [1, 2, 3, 4]
print permutations(a)
