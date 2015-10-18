dp = {}
dp[1] = 1


def collatz_length(n):
    if n not in dp:
        dp[n] = 1 + (
            collatz_length(n / 2) if n % 2 == 0 else collatz_length(3 * n + 1)
        )
    return dp[n]


max_length = 1, 1

for i in range(2, 1000000):
    max_length = max(max_length, (collatz_length(i), i))

print max_length[1]
