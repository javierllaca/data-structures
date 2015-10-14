import time
from random import randrange


def sort(a, fn):
    if fn == merge_sort:
        aux = [0 for i in range(len(a))]
        fn(a, aux, 0, len(a) - 1)
    else:
        fn(a, 0, len(a) - 1)


def merge_sort(a, aux, lo, hi):
    if lo < hi:
        mid = (lo + hi) / 2
        merge_sort(a, aux, lo, mid)
        merge_sort(a, aux, mid + 1, hi)
        merge(a, aux, lo, mid, hi)


def merge(a, aux, lo, mid, hi):
    for i in range(lo, hi + 1):
        aux[i] = a[i]

    aux_a = lo
    aux_b = mid + 1
    current = lo

    while aux_a <= mid and aux_b <= hi:
        if aux[aux_a] <= aux[aux_b]:
            a[current] = aux[aux_a]
            aux_a += 1
        else:
            a[current] = aux[aux_b]
            aux_b += 1
        current += 1

    remaining = mid - aux_a
    for i in range(remaining + 1):
        a[current + i] = aux[aux_a + i]


def quick_sort(a, lo, hi):
    if lo < hi:
        index = partition(a, lo, hi)
        quick_sort(a, lo, index - 1)
        quick_sort(a, index + 1, hi)


def partition(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] < pivot:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, hi)
    return i + 1


def insertion_sort(a, lo, hi):
    for j in range(lo + 1, hi + 1):
        i = j - 1
        key = a[j]
        while i >= lo and key < a[i]:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def selection_sort(a, lo, hi):
    for i in range(lo, hi + 1):
        min_index = i
        for j in range(i, hi + 1):
            if a[j] < a[min_index]:
                min_index = j
        swap(a, i, min_index)


def bubble_sort(a, lo, hi):
    for i in range(hi, lo, -1):
        for j in range(lo, i):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)


def counting_sort(a, k):
    b = [0 for _ in range(len(a))]
    c = [0 for _ in range(k + 1)]
    for j in range(len(a)):
        c[a[j]] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1


def get_digit(n, d):
    return n / 10 ** d % 10


def radix_sort(a, d):
    for i in range(d):
        pass


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def is_sorted(a):
    return all(a[i] <= a[i+1] for i in range(len(a) - 1))


def rand_arr(n, hi):
    return [randrange(hi) for i in range(n)]


def main():
    a = rand_arr(10000, 1000)
    fns = [bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort]
    for fn in fns:
        copy = list(a)
        start = time.time()
        sort(copy, fn)
        elapsed = time.time() - start
        assert is_sorted(copy)
        print elapsed


if __name__ == '__main__':
    main()
