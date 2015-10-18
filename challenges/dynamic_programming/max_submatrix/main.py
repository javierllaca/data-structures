def max_submatrix(a):
    n = len(a)
    dp = [[[[
        0 for _ in range(n)
        ] for _ in range(n)
        ] for _ in range(n)
        ] for _ in range(n)
    ]
    max_sum = (float('-inf'), (0, 0, 0, 0))
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    dp[i][j][x][y] += a[x][y]
                    if x > i and y > j:
                        dp[i][j][x][y] += (
                            dp[i][j][x - 1][y]
                            + dp[i][j][x][y - 1]
                            - dp[i][j][x - 1][y - 1]
                        )
                    elif x > i:
                        dp[i][j][x][y] += dp[i][j][x - 1][y]
                    elif y > j:
                        dp[i][j][x][y] += dp[i][j][x][y - 1]
                    max_sum = max(max_sum, (dp[i][j][x][y], (i, j, x, y)))
    return max_sum


def submatrix(a, i, j, x, y):
    return [row[j:y + 1] for row in a[i:x + 1]]


def print_matrix(a):
    for row in a:
        for cell in row:
            print '{: <20}'.format(cell),
        print


def test(a):
    print_matrix(a)
    s, coords = max_submatrix(a)
    print '\n({})\n'.format(s)
    print_matrix(submatrix(a, *coords))
    print '\n{}\n'.format('-' * 50)


test([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

test([
    [1, -1, 2],
    [-2, 3, 4],
    [-3, 4, 4]
])
