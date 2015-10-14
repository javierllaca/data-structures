class Graph:

    def __init__(self):
        self.edges = {}

    def make_node(self, x):
        if x not in self.edges:
            self.edges[x] = {}

    def add_edge(self, x, y, cost=1):
        self.edges[x][y] = cost
        self.edges[y][x] = cost

    def bfs(self, start):
        queue = [(start, 0)]
        path = {}

        while queue:
            node, cost = queue.pop(0)
            for neighbor in self.edges[node]:
                if neighbor not in path:
                    path[neighbor] = cost + self.edges[node][neighbor]
                    queue.append((neighbor, cost + self.edges[node][neighbor]))

        return path


t = int(raw_input())

for i in range(t):

    n, m = map(int, raw_input().split())

    g = Graph()

    for j in range(1, n + 1):
        g.make_node(j)

    for j in range(m):
        a, b = map(int, raw_input().split())
        g.add_edge(a, b, 6)

    s = int(raw_input())

    bfs = g.bfs(s)

    for j in range(1, n + 1):
        if j != s:
            if j in bfs:
                print bfs[j],
            else:
                print -1,
    print
