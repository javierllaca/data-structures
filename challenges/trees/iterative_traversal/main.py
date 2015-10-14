from data_structures.queue import LIFO
from data_structures.tree.bst import BST


def pre_order(n):
    stack = LIFO()
    stack.push(n)
    while not stack.is_empty():
        n = stack.pop()
        print n.key
        if n.right:
            stack.push(n.right)
        if n.left:
            stack.push(n.left)


def in_order(n):
    stack = LIFO()
    while not stack.is_empty() or n:
        if n:
            stack.push(n)
            n = n.left
        else:
            n = stack.pop()
            print n.key
            n = n.right


def post_order(n):
    stack = LIFO()
    prev = None
    while not stack.is_empty() or n:
        if n:
            stack.push(n)
            n = n.left
        else:
            p = stack.peek()
            if p.right and prev != p.right:
                n = p.right
            else:
                print p.key
                prev = stack.pop()


t = BST()
for elem in [5, 3, 7, 2, 4, 6, 8]:
    t.insert(elem)

in_order(t.root)
print
pre_order(t.root)
print
post_order(t.root)
