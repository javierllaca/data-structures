def search(a, x):
    i, j = len(a) - 1, 0
    while i >= 0 and j < len(a[0]):
        if x == a[i][j]:
            return i, j
        if x > a[i][j]:
            j += 1
        else:
            i -= 1
    return None


def test_matrix_search(a, x, exists=True):
    if not exists:
        assert search(a, x) is None
    else:
        i, j = search(a, x)
        assert a[i][j] == x


a = [
    range(i, i + 4)
    for i in range(4)
]

test_matrix_search(a, 4)

a = [
    range(4 * i, 4 * i + 4)
    for i in range(4)
]

test_matrix_search(a, 8)
test_matrix_search(a, 15)
test_matrix_search(a, 16, exists=False)
