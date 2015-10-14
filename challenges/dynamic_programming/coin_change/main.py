n, m = map(int, raw_input().split())
c = map(int, raw_input().split())

dp = [[-1 for _ in range(m)] for _ in range(n + 1)]


def coin_change(n, c):
    if n == 0:
        return 1
    if not c or n < 0:
        return 0
    i, j = n, len(c) - 1
    if dp[i][j] == -1:
        dp[i][j] = coin_change(n, c[1:]) + coin_change(n - c[0], c)
    return dp[i][j]


print coin_change(n, c)
