class DisjointSets:

    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def make_set(self, x):
        self.parents[x] = x
        self.ranks[x] = 0

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.link(self.find(x), self.find(y))

    def link(self, x, y):
        if self.ranks[x] > self.ranks[x]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            if self.ranks[x] == self.ranks[y]:
                self.ranks[y] += 1

    def sets(self):
        sets = {}
        for val in self:
            parent = self.find(val)
            if parent in sets:
                sets[parent].add(val)
            else:
                sets[parent] = set([val])
        return sets.values()

    def __iter__(self):
        return iter(self.parents)


s = DisjointSets()

for i in range(10):
    s.make_set(i)

vals = [
    (0, 2),
    (2, 2),
    (1, 3),
    (0, 4),
    (6, 4),
    (3, 7),
    (5, 9)
]

for x, y in vals:
    s.union(x, y)

print s.sets()
