"""
Cracking the Coding Interview, 4.4

Given a binary search tree, design an algorithm which creates a linked list of
all the nodes at each depth (i.e., if you have a tree with depth D, you'll have
D linked lists)
"""

from data_structures.tree.avl import AvlTree
from random import randrange


def tree_levels(t):
    depth = 0
    queue = [(t, 0)]
    level = []
    while queue:
        n, d = queue.pop(0)
        if depth != d:
            yield level
            level = []
            depth = d
        level.append(n.key)
        if n.left:
            queue.append((n.left, d + 1))
        if n.right:
            queue.append((n.right, d + 1))


t = AvlTree()

keys = [randrange(100) for _ in range(100)]

for key in keys:
    t.insert(key)

print str(t)

for level in tree_levels(t.root):
    print level
