class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ''
        n = self
        while n:
            s += str(n.val)
            s += ' -> '
            n = n.next
        return s


class List:

    def __init__(self, vals=None):
        self.head = None
        self.end = None
        if vals:
            for val in vals:
                self.push_back(val)

    def __str__(self):
        return str(self.head)

    def push_front(self, val):
        self.head = Node(val, self.head)
        if not self.end:
            self.end = self.head

    def push_back(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.end = n
        else:
            self.end.next = n
            self.end = n

    def reverse(self):
        a = None
        b = self.head
        self.end = b
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        self.head = a

    def __eq__(self, other):
        m, n = self.head, other.head
        while n and m:
            if m.val != n.val:
                return False
            m = m.next
            n = n.next
        if n or m:
            return False
        return True

    def __iter__(self):
        n = self.head
        while n:
            yield n.val
            n = n.next


a, b = List(), List()
for i in range(10):
    a.push_back(i)
    b.push_front(i)

a.reverse()
assert a == b
