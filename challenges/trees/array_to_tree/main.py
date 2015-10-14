"""
Cracking the Coding Interview, 4.3

Given a sorted (increasing order) array, write an algorithm to create a binary
tree with minimal height
"""

from data_structures.tree.bst import BST, BinaryNode


def array_to_tree(a, low, high):
    if high < low:
        return None
    mid = (low + high) / 2
    return BinaryNode(
        a[mid],
        array_to_tree(a, low, mid - 1),
        array_to_tree(a, mid + 1, high)
    )


a = range(100)

t = BST(array_to_tree(a, 0, len(a) - 1))

print str(t)
