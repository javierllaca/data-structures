def traverse(g, a, visited):
    queue = [a]
    nodes = 0
    while queue:
        n = queue.pop(0)
        visited.add(n)
        nodes += 1
        for neighbor in g[n]:
            if neighbor not in visited:
                queue.append(neighbor)
    return nodes


g = {}

n, l = map(int, raw_input().split())

for i in range(n):
    g[i] = set()

for i in range(l):
    a, b = map(int, raw_input().split())
    g[a].add(b)
    g[b].add(a)

visited = set()
component_sizes = []

for k in g:
    if k not in visited:
        component_sizes.append(traverse(g, k, visited))

result = 0

for component_size in component_sizes:
    n -= component_size
    result += component_size * n

print result
