def knapsack(total_w, items):
    dp = [0 for _ in range(total_w + 1)]
    for i in range(len(items)):
        v, w = items[i]
        for j in range(total_w, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[total_w]


print knapsack(5, [(3, 2), (4, 1), (1, 6)])
