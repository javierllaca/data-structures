from data_structures.list import List
from data_structures.priority import PriorityQueue as PQ
from time import time


def build_lists(k, n):
    """k lists of n nodes each"""
    l = []
    for i in range(k):
        l.append(List([
            j * k + i for j in range(n)
        ]))
    return l


def merge(l):
    p = [i.head for i in l]
    q = PQ()
    for i in range(len(p)):
        q.push((p[i].val, i))
    res = List()
    while not q.is_empty():
        val, i = q.pop()
        res.push_back(val)
        p[i] = p[i].next
        if p[i]:
            q.push((p[i].val, i))
    return res


def merge_brute(l):
    res = []
    for i in l:
        for j in i:
            res.append(j)
    return List(sorted(res))


l = build_lists(100, 1000)

start = time()
l1 = merge_brute(l)
print time() - start

start = time()
l2 = merge(l)
print time() - start

assert l1 == l2
