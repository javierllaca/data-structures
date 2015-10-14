from data_structures.graph import Graph

"""
Given an array a with weight, and indexes i and j, determine whether index j is
reachable from i by moving forward or backward n positions, where n is the
weight of the array at a given position.
"""


def reachable_a(a, i, j):
    """Using an auxiliary graph data structure"""
    g = Graph(range(len(a)))
    for i in range(len(a)):
        g.add_edge(i, (i + a[i]) % len(a))
        g.add_edge(i, (i - a[i]) % len(a))
    return g.bfs(i, j)


def reachable_b(a, i, j):
    queue = [i]
    visited = [False for _ in range(len(a))]
    while queue:
        n = queue.pop(0)
        print n, a[n]
        if n == j:
            return True
        elif not visited[n]:
            visited[n] = True
            queue.append((n + a[n]) % len(a))
            queue.append((n - a[n]) % len(a))
    return False


assert reachable_a([1, 2, 3, 1, 4], 0, 3)
assert reachable_b([1, 2, 3, 1, 4], 0, 3)
