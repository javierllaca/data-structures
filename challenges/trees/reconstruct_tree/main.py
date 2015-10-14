"""
Reconstruct a binary tree
Input: inorder, preorder
Output: root of constructed tree
class Node: data (ints), leftChild, rightChild
"""


class Node:
    pass


inorder = [2, 3, 5, 6, 7, 9]
preorder = [5, 3, 2, 7, 6, 9]


def binary_search(a, x, lo, hi):
    if lo == hi:
        return lo
    mid = lo + (hi - lo) / 2
    if x == a[mid]:
        return mid
    if x < a[mid]:
        return binary_search(a, x, lo, mid)
    else:
        return binary_search(a, x, mid + 1, hi)


def reconstruct_tree(inorder, preorder):
    if not inorder:
        return None
    root = preorder.pop(0)
    root_index = binary_search(inorder, root, 0, len(inorder))
    left_child = reconstruct_tree(inorder[:root_index], preorder)
    right_child = reconstruct_tree(inorder[root_index + 1:], preorder)
    return Node(root, left_child, right_child)
