"""
Cracking the Coding Interview, 4.7

You have two very large binary trees: T1, with millions of nodes, and T2, with
hun- dreds of nodes Create an algorithm to decide if T2 is a subtree of T1
"""

from data_structures.tree.avl import AvlTree
from data_structures.tree.bst import BST
from itertools import izip
import random


def find_node(a, b):
    if not a:
        return None
    if a.key == b.key:
        return a
    if b.key < a.key:
        return find_node(a.left, b)
    return find_node(a.right, b)


def dfs(n):
    if n:
        yield n.key
        for i in dfs(n.left):
            yield i
        for i in dfs(n.right):
            yield i


def is_subtree(a, b):
    """Determines whether a is a subtree of b"""
    n = find_node(a, b)
    # simultaneously traverse both trees and compare the keys
    for x, y in izip(dfs(n), dfs(b)):
        if x != y:
            return False
    return True


def copy_tree(n):
    t = BST()
    for k in n:
        t.insert(k)
    return t


# We initially use an AVL tree for balance purposes
t = AvlTree()
for i in range(100):
    t.insert(i)

# Now that we have a balanced tree, we convert it to a regular BST to preserve
# the structure upon deletion
t1 = copy_tree(t.root)

# case 1: t2 is a subtree of t1
t2 = copy_tree(t.find(23))
assert is_subtree(t1.root, t2.root)

# cases 2 and 3: Choose a random key in t2
r = random.choice([key for key in t2])

t1.delete(r)
assert not is_subtree(t1.root, t2.root)

t2.delete(r)
assert is_subtree(t1.root, t2.root)
