"""
Cracking the Coding Interview, 4.6

Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree Avoid storing additional nodes in a data structure

NOTE: This is not necessarily a binary search tree
"""


def node_height(n):
    h = 0
    while n.parent:
        h += 1
        n = n.parent
    return h


def first_common_ancestor(a, b):
    if not a.parent or b.parent:
        return None
    p1, p2 = a.parent, b.parent
    h1, h2 = node_height(p1), node_height(p2)
    while h1 > h2:
        p1 = p1.parent
        h1 -= 1
    while h2 > h1:
        p2 = p2.parent
        h2 -= 1
    while p1 and p2:
        if p1 == p2:
            return p1
        p1 = p1.parent
        p2 = p2.parent
    return None


def lca(t, a, b):
    if not t:
        return None
    if t == a or t == b:
        return t
    l, r = lca(t.left, a, b), lca(t.right, a, b)
    if l == r:
        return t
    return l if l else r
