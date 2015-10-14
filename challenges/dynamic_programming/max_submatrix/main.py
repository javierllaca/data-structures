def max_submatrix(a):
    n = len(a)
    dp = [[[[
        0 for _ in range(n)
        ] for _ in range(n)
        ] for _ in range(n)
        ] for _ in range(n)
    ]
    max_sum = float('-inf')
    m_i, m_j, m_x, m_y = 0, 0, 0, 0
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
                    if dp[i][j][x][y] > max_sum:
                        max_sum = dp[i][j][x][y]
                        m_i, m_j, m_x, m_y = i, j, x, y
    m = [row[m_j:m_y + 1] for row in a[m_i:m_x + 1]]
    return m_i, m_j, m_x, m_y, m


def print_matrix(a):
    for row in a:
        for cell in row:
            print '{: <20}'.format(cell),
        print


def test(a):
    i, j, x, y, m = max_submatrix(a)
    print_matrix(a)
    print '-' * 50
    print_matrix(m)


test([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])
print
test([
    [1, -1, 2],
    [-2, 3, 4],
    [-3, 4, 4]
])
