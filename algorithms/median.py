from math import floor


def select(a, left, right, n):
    if left == right:
        return a[left]
    for i in range(left, right):
        pivotIndex = pivot(a, left, right)
        pivotIndex = partition(a, left, right, pivotIndex)
        if n == pivotIndex:
            return a[n]
        elif n < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1


def pivot(a, left, right):
    # move the medians of five-element subgroups to the first n/5 positions
    for i in range(left, right, 5):
        # get the median of the i'th five-element subgroup
        subRight = i + 4
        if subRight > right:
            subRight = right

        median5 = partition5(a, i, subRight)
        swap(a, median5, floor(i/5))

    # compute the median of the n/5 medians-of-five
    return select(a, left, left + ceil((right - left) / 5) - 1, (right - left)/10)


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition5(a, left, right):
    part_size = (right - left) / 5
    return [a[left + i * part_size : left + (i + 1) * part_size ] for i in range(5)]


print partition5(range(100), 0, 100)
print select(range(100), 0, 100, 50)
