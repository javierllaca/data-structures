from data_structures.queue import LIFO

"""
Assume an infinite binary tree such that:
- The value of the root is 1/1
- Any node with value a/b has
    - a/(a + b) as a left child
    - (a + b)/b as a right child

i.e.:
            1/1
          /     \
      1/2         2/1
     /   \       /   \
   1/3   3/2   2/3   3/1
   / \   / \   / \   / \
           ...

Let the index of a node in the tree be given by a breadth-first ordering:

index   value
0       1/1
1       1/2
2       2/1
3       1/3
4       3/2
5       2/3
6       3/1
...

Given integers x and y, find the index of the node with value x/y

Note: The tree contains all positive rational numbers
"""


def find_index(x, y):
    delta_x, delta_y = 0, 0
    path = LIFO()

    # Move upwards to determine vertical displacement
    # Use a stack to keep track of path (0: left, 1: right)
    while x != y:
        if x > y:
            x = x - y
            path.push(1)
        else:
            y = y - x
            path.push(0)
        delta_y += 1

    # Use path to compute horizontal displacement
    i = delta_y
    while not path.is_empty():
        delta_x += 2 ** (i - 1) * path.pop()
        i -= 1

    # Number of leaves in previous level + horizontal displacement
    return int(2 ** delta_y - 1 + delta_x)


tests = [
    (5, 2, 10),
    (1, 3, 3),
    (2, 3, 5),
    (3, 8, 19),
]

for x, y, index in tests:
    assert find_index(x, y) == index
