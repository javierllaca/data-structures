def kmp_search(s, w):
    """Knuth-Morris-Pratt algorithm"""
    m = 0
    i = 0
    t = kmp_table(w)
    while m + i < len(s):
        if w[i] == s[m + i]:
            if i == len(w) - 1:
                return m
            i += 1
        else:
            if t[i] > -1:
                m += i - t[i]
                i = t[i]
            else:
                i = 0
                m += 1
    return len(s)


def kmp_table(w):
    """Knuth-Morris-Pratt algorithm table"""
    t = [0 for _ in range(len(w))]
    t[0] = -1
    pos = 2
    cnd = 0
    while pos < len(w):
        if w[pos - 1] == w[cnd]:
            cnd += 1
            t[pos] = cnd
            pos += 1
        elif cnd > 0:
            cnd = t[cnd]
        else:
            t[pos] = 0
            pos += 1
    return t


def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)
    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(
                    d[i -1][j] + 1,
                    d[i][j - 1] + 1,
                    d[i - 1][j - 1] + 1
                )
    return d[m][n]


assert kmp_search('abcdef', 'def') == 3
assert kmp_search('abcdef', 'cd') == 2
assert kmp_search('abcdef', 'gh') == 6

assert levenshtein_distance('drift', 'shift') == 2
assert levenshtein_distance('cat', 'concatenate') == 8
