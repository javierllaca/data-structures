from random import randrange
from time import time
# from math import ceil


def median(a):
    return sorted(a)[len(a) / 2]


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
    else:
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
    else:
        return quick_select_f(s2, k - len(s1) - 1)


def select(a, left, right, n):
    if left == right:
        return left
    for i in range(left, right):
        pivotIndex = pivot(a, left, right)
        pivotIndex = partition(a, left, right, pivotIndex)
        if n == pivotIndex:
            return n
        elif n < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1


def pivot(a, left, right):
    for i in range(left, right, 5):
        j = i + 4
        if j > right:
            j = right
        median5 = partition5(a, i, j)
        swap(a, median5, i / 5)

    top = left + (right - left) / 5 - 1
    return select(a, left, top, (right - left) / 10)


def partition5(a, left, right):
    temp = a[left:right + 1]
    m = median(temp)
    return temp.index(m) + left


def _main():
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


"""
a = [randrange(10) for i in range(10)]
k = 8

for i in range(1, 10):
    b = list(a)
    q = quick_select(b, i)
    print 'quick_select({}, {}) == {}'.format(sorted(a), i, q)
"""


if __name__ == '__main__':
    a = 3

for i in range(10):
    print 'i -> {}'.format(select(range(10), 0, 9, i))
