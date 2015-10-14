def print_matrix(a):
    for row in a:
        for cell in row:
            print cell,
        print


def rotate(a):
    n = len(a)
    f = n / 2
    c = (n + 1) / 2
    for i in range(f):
        for j in range(c):
            temp = a[i][j]
            a[i][j] = a[n-1-j][i]
            a[n-1-j][i] = a[n-1-i][n-1-j]
            a[n-1-i][n-1-j] = a[j][n-1-i]
            a[j][n-1-i] = temp

a = [
    range(5 * i, 5 * i + 5)
    for i in range(5)
]

print_matrix(a)
print
rotate(a)
print_matrix(a)
