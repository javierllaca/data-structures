from data_structures.disjoint_sets import DisjointSets


n, l = map(int, raw_input().split())

s = DisjointSets()

for i in range(n):
    s.make_set(i)

for i in range(l):
    a, b = map(int, raw_input().split())
    s.union(a, b)

result = 0

for s in s.sets():
    n -= len(s)
    result += len(s) * n

print result
