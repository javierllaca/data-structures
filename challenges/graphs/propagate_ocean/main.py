def read_map(s):
    a = []
    for line in s.strip().split('\n'):
        a.append(list(line))
    return a


def neighbors(a, i, j):
    if i > 0:
        yield((i - 1, j))
    if j > 0:
        yield((i, j - 1))
    if i < len(a) - 1:
        yield((i + 1, j))
    if j < len(a[0]) - 1:
        yield((i, j + 1))


def propagate_ocean(a, i, j):
    a[i][j] = 'O'
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        for x, y in neighbors(a, i, j):
            if a[x][y] == 'W':
                a[x][y] = 'O'
                stack.append((x, y))


def print_map(a):
    for row in a:
        for cell in row:
            print cell,
        print


input_string = """
LLLLLLL
WWWLWWW
WLLLLLW
WWWWWLL
LLLLWLL
WWWLLLL
"""

a = read_map(input_string)
print_map(a)
print
propagate_ocean(a, 1, 0)
print_map(a)
