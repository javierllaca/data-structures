class BinaryNode(object):

    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        return not self.left and not self.right

    def find(self, k):
        x = self
        while x and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self):
        x = self
        while x.left:
            x = x.left
        return x

    def maximum(self):
        x = self
        while x.right:
            x = x.right
        return x

    def successor(self):
        x = self
        if x.right:
            return x.right.minimum()
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def __str__(self):
        s = '({}'.format(self.key)
        if self.left:
            s += ' {}'.format(self.left)
        if self.right:
            s += ' {}'.format(self.right)
        return s + ')'

    def __iter__(self):
        yield self.key
        if self.left:
            for k in self.left:
                yield k
        if self.right:
            for k in self.right:
                yield k


class BST:

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return not self.root

    def find(self, k):
        if self.root:
            return self.root.find(k)
        return None

    def insert(self, k):
        z = BinaryNode(k)
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, k):
        z = self.find(k)
        if not z:
            return
        if not z.left:
            self.transplant(z, z.right)
        elif not z.right:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        for k in self.root:
            yield k
