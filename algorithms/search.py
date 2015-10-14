def linear_search(a, x, lo, hi):
    for i in range(lo, hi + 1):
        if x == a[i]:
            return i
    return -1


def binary_search(a, x, lo, hi):
    mid = lo + (hi - lo) / 2
    if x < a[mid]:
        return binary_search(a, x, lo, mid - 1)
    elif x > a[mid]:
        return binary_search(a, x, mid + 1, hi)
    else:
        return mid
