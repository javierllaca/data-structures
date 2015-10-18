def search_unsorted(a, x, lo, hi):
    """Linear search"""
    for i in range(lo, hi + 1):
        if x == a[i]:
            return i
    return -1


def search_sorted(a, x, lo, hi):
    """Binary search"""
    mid = lo + (hi - lo) / 2
    if x == a[mid]:
        return mid
    if x < a[mid]:
        return binary_search(a, x, lo, mid - 1)
    return binary_search(a, x, mid + 1, hi)
