"""
You are given a Double Link List with one pointer of each node pointing to the
next node just like in a single link list. The second pointer however CAN point
to any node in the list and not just the previous node. Now write a program in
O(n) time to duplicate this list. That is, write a program which will create a
copy of this list.
"""

from random import randrange


class Node:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = None

    def __iter__(self):
        n = self
        while n:
            yield n
            n = n.next

    def __str__(self):
        return '{} {}'.format(self.data, self.next)


def make_random_list(n):
    nodes = [Node(i) for i in range(n)]
    root = nodes[0]

    structure = [
        (i, i + 1, randrange(n))
        for i in range(len(nodes) - 1)
    ]

    for node, next, random in structure:
        if next:
            nodes[node].next = nodes[next]
        nodes[node].random = nodes[random]

    return root


def copy_list(l):
    if not l:
        return None
    new_head = Node(l.data)
    i, j = new_head, l
    while j.next:
        i.next = Node(j.next.data)
        i = i.next
        j = j.next
    return new_head


def copy_random_list(l):
    root = Node[0]
    nodes = [n for n in l]
    structure = [
        (i, i + 1, randrange(n))
        for i in range(len(nodes) - 1)
    ]
    for node, next, random in structure:
        if next:
            nodes[node].next = nodes[next]
        nodes[node].random = nodes[random]
    return root


l = make_random_list(10)

for n in l:
    if n.random:
        print n.data, n.random.data

print str(copy_list(l))
