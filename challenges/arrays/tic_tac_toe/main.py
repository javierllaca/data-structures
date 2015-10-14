def won(a):
    for i in range(3):
        if (a[i][0] == a[i][1] == a[i][2] or
                a[i][0] == a[i][1] == a[i][2]):
            return True
    if (a[0][0] == a[1][1] == a[2][2] or
            a[0][2] == a[1][1] == a[2][0]):
        return True
    return False


a = [
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 0]
]


print won(a)
