"""
Cracking the Coding Interview, 4.5

Write an algorithm to find the ‘next’ node (i e , in-order successor) of a
given node in a binary search tree where each node has a link to its parent
"""


def node_successor(n):
    if n.right:
        p = n.right
        while p.left:
            p = p.left
    else:
        p = n.parent
        while p.left != n:
            n = p
            p = p.parent
    return p
