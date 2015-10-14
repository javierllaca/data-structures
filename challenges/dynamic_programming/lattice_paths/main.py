dp = [
    [0 for _ in range(50)]
    for _ in range(50)
]

dp[0][0] = 0
dp[0][1] = 1
dp[1][0] = 1


def paths(x, y):
    """Returns the number of possible paths from (0, 0) to (x, y) by moving
    down and right.
    """
    if dp[x][y] == 0:
        count = 0
        if x > 0:
            count += paths(x - 1, y)
        if y > 0:
            count += paths(x, y - 1)
        dp[x][y] = count
    return dp[x][y]


# pre-compute all inner square grids
for i in range(20):
    paths(i, i)

print paths(20, 20)
