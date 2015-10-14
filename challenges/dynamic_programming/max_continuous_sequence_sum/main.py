from random import randrange
from time import time


"""
You are given an array of integers (both positive and negative) Find the
continuous sequence with the largest sum Return the sum

Example:

Input: [2, -8, 3, -2, 4, -10]
Output: 5 (i.e., [3, -2, 4])
"""


def max_crossing_subarray(a, low, mid, high):
    max_left, max_right = -1, -1
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, high):
        sum += a[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


def max_subarray(a, low, high):
    """O(n * log(n)) solution"""
    if high == low:
        return low, high, a[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = max_subarray(a, low, mid)
        right_low, right_high, right_sum = max_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum =\
            max_crossing_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        if right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def max_sequence_sum(a):
    """O(n^2) solution (brute force)"""
    max_sum = float('-inf')
    for i in range(len(a)):
        prev = 0
        for j in range(i, len(a)):
            if prev + a[j] > max_sum:
                max_sum = prev + a[j]
            prev += a[j]
    return max_sum


# a = [2, -8, 3, -2, 4, -10]
# assert max_sequence_sum(a) == 5

a = [randrange(-1000, 1000) for i in range(5000)]

start = time()
sum = max_sequence_sum(a)
print sum, time() - start

start = time()
low, high, sum = max_subarray(a, 0, len(a) - 1)
print sum, time() - start
