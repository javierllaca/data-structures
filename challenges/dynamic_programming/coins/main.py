def min_coins(target, coins):
    dp = [float('inf')] * (target + 1)
    for coin in coins:
        if coin <= target:
            dp[coin] = 1
    for i in range(len(dp)):
        for coin in coins:
            if coin <= target:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[target]


def permutations(target, coins):
    dp = [0] * (target + 1)
    for coin in coins:
        if coin <= target:
            dp[coin] = 1
    for i in range(len(dp)):
        for coin in coins:
            if coin <= i:
                dp[i] += dp[i - coin]
    return dp[target]


def combinations(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(len(dp)):
            if coin <= i:
                dp[i] += dp[i - coin]
    return dp[target]


def combinations_unique(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(len(dp) - 1, coin - 1, -1):
            if coin <= i:
                dp[i] += dp[i - coin]
    return dp[target]


target = 3
coins = [1, 2]

print min_coins(target, coins)
print permutations(target, coins)
print combinations(target, coins)
print combinations_unique(target, coins)
