def read_map(s):
    a = []
    for line in s.strip().split('\n'):
        a.append(map(int, list(line)))
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


def visit_land(a, i, j, visited):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        for x, y in neighbors(a, i, j):
            if a[x][y] == 1 and (x, y) not in visited:
                visited.add((x, y))
                stack.append((x, y))


def count_islands(a):
    islands = 0
    visited = set()
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1 and (i, j) not in visited:
                visit_land(a, i, j, visited)
                islands += 1
    return islands


input_string = """
000000011111
011100010001
001100010101
000000010001
110001011111
111001000000
000011011100
000000011100
001100011000
011110000000
"""

a = read_map(input_string)
print count_islands(a)
