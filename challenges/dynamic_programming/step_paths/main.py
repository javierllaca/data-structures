"""
A child is running up a staircase with n steps, and can hop
either 1 step, 2 steps, or 3 steps at a time. Implement a
method to count how many possible ways the child can run up
the stairs.
"""

dp = [-1 for _ in range(100)]
dp[0] = 0
dp[1] = 1


def step_paths(n):
    if dp[n] == -1:
        dp[n] = 1 + step_paths(n - 1) + step_paths(n - 2) + step_paths(n - 3)
    return dp[n]

print step_paths(10)
