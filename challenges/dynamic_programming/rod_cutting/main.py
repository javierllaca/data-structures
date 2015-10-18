def cut_rod(p, n):
    r = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_cut_rod(p, n):
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = extended_cut_rod(p, n)
    while n > 0:
        print s[n]
        n -= s[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print extended_cut_rod(p, 10)
print_cut_rod_solution(p, 10)

print extended_cut_rod(p, 7)
print_cut_rod_solution(p, 7)
