from time import time


def score_combinations(s, w):
    if not w or s < 0:
        return 0
    if s == 0:
        return 1
    return score_combinations(s, w[1:]) + score_combinations(s - w[0], w)


dp = {}


def score_combinations_dp(s, w):
    if not w or s < 0:
        return 0
    if s == 0:
        return 1
    if s not in dp:
        dp[s] = {}
    if w[0] not in dp[s]:
        dp[s][w[0]] = (
            score_combinations_dp(s, w[1:]) +
            score_combinations_dp(s - w[0], w)
        )
    return dp[s][w[0]]


s = 100

for i in range(2, 8):
    w = range(1, i)
    dp = {}

    start = time()
    a1 = score_combinations_dp(s, w)
    t1 = time() - start

    start = time()
    a2 = score_combinations(s, w)
    t2 = time() - start

    assert a1 == a2

    print t2 - t1, t2 / t1
