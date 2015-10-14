from data_structures.priority import PriorityQueue as PQ
from time import time


def build_arrays(k, n):
    """k lists of n nodes each"""
    l = []
    for i in range(k):
        l.append([
            j * k + i for j in range(n)
        ])
    return l


def merge(l):
    p = [0 for _ in range(len(l))]
    q = PQ()
    for i in range(len(p)):
        q.push((l[i][p[i]], i))
    res = []
    while not q.is_empty():
        val, i = q.pop()
        res.append(val)
        p[i] += 1
        if p[i] < len(l[i]):
            q.push((l[i][p[i]], i))
    return res


def merge_brute(l):
    res = []
    for i in l:
        for j in i:
            res.append(j)
    return sorted(res)


l = build_arrays(1000, 1000)

start = time()
l1 = merge_brute(l)
print time() - start

start = time()
l2 = merge(l)
print time() - start

assert l1 == l2
