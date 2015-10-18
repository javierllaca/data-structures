from random import randrange
from time import time


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition(a, left, right, pivot_index):
    pivot = a[pivot_index]
    swap(a, pivot_index, right)
    pivot_index = left
    for i in range(left, right):
        if a[i] <= pivot:
            swap(a, i, pivot_index)
            pivot_index += 1
    swap(a, right, pivot_index)
    return pivot_index


def quick_select_aux(a, left, right, k):
    if left == right:
        return a[left]
    pivot_index = randrange(left, right + 1)
    pivot_index = partition(a, left, right, pivot_index)
    if k == pivot_index:
        return a[k]
    if k < pivot_index:
        return quick_select_aux(a, left, pivot_index - 1, k)
    return quick_select_aux(a, pivot_index + 1, right, k)


def quick_select(a, k):
    return quick_select_aux(a, 0, len(a) - 1, k)


def quick_select_f(a, k):
    if len(a) == 1:
        return a[0]
    pivot_index = randrange(len(a))
    pivot = a[pivot_index]
    s1 = [a[i] for i in range(len(a)) if a[i] <= pivot and i != pivot_index]
    s2 = [a[i] for i in range(len(a)) if a[i] > pivot and i != pivot_index]
    if k == len(s1):
        return pivot
    if k < len(s1):
        return quick_select_f(s1, k)
    return quick_select_f(s2, k - len(s1) - 1)


def median_of_medians(a, lo, hi):
    medians = []
    for i in range(lo, hi, 5):
        b = sorted(a[i:i + 5])
        medians.append(b[(len(b) - 1) / 2])
    if len(medians) == 1:
        return medians[0]
    return median_of_medians(medians, 0, len(medians))


def select(a, left, right, n):
    if left == right:
        return left
    for i in range(left, right):
        pivot = median_of_medians(a, left, right)
        pivotIndex = a[left:right].index(pivot)
        pivotIndex = partition(a, left, right, pivotIndex)
        if n == pivotIndex:
            return n
        elif n < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1


n = 10000000
m = 10000

b = [randrange(m) for i in range(n)]
c = list(b)
d = sorted(b)

k = randrange(m)

start = time()
q = quick_select_f(b, k)
end = time()
assert q == d[k]
print end - start

start = time()
q = quick_select(c, k)
end = time()
assert q == d[k]
print end - start
