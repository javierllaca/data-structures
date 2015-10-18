dp = [0 for i in range(101)]
dp[0] = 1


def factorial(n):
    if dp[n] == 0:
        dp[n] = n * factorial(n - 1)
    return dp[n]


print sum([int(c) for c in str(factorial(100))])
