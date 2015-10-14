"""
Cracking the Coding Interview, 4.1

Implement a function to check if a tree is balanced For the purposes of this
question, a balanced tree is defined to be a tree such that no two leaf nodes
differ in distance from the root by more than one
"""

from data_structures.tree.bst import BST
from data_structures.tree.avl import AvlTree
from random import randrange


def leaf_distance(t, d=0):
    if not t:
        return
    if t.is_leaf():
        yield d
    else:
        for _d in leaf_distance(t.left, d + 1):
            yield _d
        for _d in leaf_distance(t.right, d + 1):
            yield _d


def is_balanced(t):
    dist = None
    for d in leaf_distance(t):
        if not dist:
            dist = d
        if abs(dist - d) > 1:
            return False
    return True


keys = [randrange(100) for _ in range(10)]

a, b = BST(), AvlTree()

for key in keys:
    a.insert(key)
    b.insert(key)

print is_balanced(a.root)
print is_balanced(b.root)
