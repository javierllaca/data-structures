dp = [[0 for _ in range(21)] for _ in range(21)]

# fill in edges
for i in range(21):
    dp[i][0] = 1
    dp[0][i] = 1


def lattice_paths(i, j):
    if dp[i][j] == 0:
        dp[i][j] = lattice_paths(i - 1, j) + lattice_paths(i, j - 1)
    return dp[i][j]


for i in range(20):
    lattice_paths(i, i)

print lattice_paths(20, 20)
