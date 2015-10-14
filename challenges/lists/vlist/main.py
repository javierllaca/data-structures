# VList
#
# add 0,1,2,3,4,5,2:
# tail
# [0] <- tail
# [0] <-> [1] <- tail
# [0] <-> [1,2] <- tail
# [0] <-> [1,2] <-> [3] <- tail
# [0] <-> [1,2] <-> [3,4] <- tail
# [0] <-> [1,2] <-> [3,4,5] <- tail
# [0] <-> [1,2] <-> [3,4,5,2] <- tail

from math import log


class VNode:

    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class VList:

    def __init__(self):
        self.tail = None
        self.nodes = 0
        self.size = 0

    def add_to_end(self, x):
        if not self.tail:
            self.tail = VNode([x])
            self.nodes += 1
        else:
            n = self.tail
            if len(n.key) == 2 ** (self.nodes - 1):
                new_node = VNode([x], None, n)
                n.prev = new_node
                self.tail = new_node
                self.nodes += 1
            else:
                n.key.append(x)
        self.size += 1

    def value_at(self, i):
        if i > self.size - 1:
            raise Exception("out of bounds")
        x = int(log(i, 2))
        j = self.nodes - x - 1
        n = self.tail
        while n and j > 0:
            n = n.next
            j -= 1
        return n.key[i - 2 ** x]

    def __str__(self):
        s = '-> '
        n = self.tail
        while n:
            s += str(n.key) + ' -> '
            n = n.next
        return s


l = VList()

# node 1
l.add_to_end(0)
print str(l)

# node 2
for e in [1, 2]:
    l.add_to_end(e)
print str(l)

# node 3
for e in [3, 4, 5, 2]:
    l.add_to_end(e)
print str(l)

assert l.value_at(4) == 3
assert l.value_at(6) == 5
assert l.value_at(3) == 2
