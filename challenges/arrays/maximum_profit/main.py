def maximum_profit(a):
    min_value, max_profit = float('inf'), 0
    for i in range(len(a)):
        min_value = min(min_value, a[i])
        max_profit = max(max_profit, a[i] - min_value)
    return max_profit


assert maximum_profit([5, 9, 8, 10, 15, 4, 13]) == 10  # 5, 15
assert maximum_profit([5, 9, 8, 10, 15, 4, 16]) == 12  # 4, 16
