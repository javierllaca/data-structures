from queue import FIFO, LIFO


class Graph:

    def __init__(self, nodes=[]):
        self.edges = {}
        for node in nodes:
            self.make_node(node)

    def make_node(self, x):
        if x not in self.edges:
            self.edges[x] = set()

    def add_edge(self, x, y, cost=1):
        self.make_node(x)
        self.make_node(y)
        self.edges[x].add((y, cost))
        self.edges[y].add((x, cost))

    def traverse(self, start, queue, end=None):
        queue.push(start)
        visited = set([start])
        while not queue.is_empty():
            node = queue.pop()
            if node == end:
                return True
            for neighbor, cost in self.edges[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.push(neighbor)
        return not end

    def bfs(self, start, end):
        return self.traverse(start, FIFO(), end)

    def dfs(self, start, end):
        return self.traverse(start, LIFO(), end)

    def dijkstra(self, source):
        dist = {}
        prev = {}
        queue = FIFO()

        dist[source] = 0
        prev[source] = None

        for v in self.edges.keys():
            if v != source:
                dist[v] = float('inf')
                prev[v] = None
            queue.push(v)

        while not queue.is_empty():
            distances = [(dist[queue[i]], i) for i in range(len(queue))]
            _, index = min(distances)
            u = queue.remove(index)

            for v, cost in self.edges[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

        return dist, prev

    def __iter__(self):
        return iter(self.edges)
