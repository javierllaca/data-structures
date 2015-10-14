from bst import BinaryNode, BST


class AvlNode(BinaryNode):

    def __init__(self, key, left=None, right=None, height=0):
        super(AvlNode, self).__init__(key, left, right)
        self.height = height

    def successor(self):
        raise Exception("successor not implemented")


class AvlTree(BST):

    def __init__(self, root=None):
        self.root = root

    def insert(self, k):
        self.root = insert(k, self.root)

    def delete(self, k):
        self.root = delete(k, self.root)


def height(t):
    return t.height if t else -1


def insert(k, t):
    if not t:
        return AvlNode(k)
    if k < t.key:
        t.left = insert(k, t.left)
    elif k > t.key:
        t.right = insert(k, t.right)
    return balance(t)


def delete(k, t):
    if not t:
        return t
    if k < t.key:
        t.left = delete(k, t.left)
    elif k > t.key:
        t.right = delete(k, t.right)
    elif t.left and t.right:
        t.key = t.right.minimum().key
        t.right = delete(t.key, t.right)
    else:
        t = t.left if t.left else t.right
    return balance(t)


def balance(t):
    if not t:
        return t
    if height(t.left) - height(t.right) > 1:
        if height(t.left.left) >= height(t.left.right):
            t = rotate_with_left_child(t)
        else:
            t = double_rotate_with_left_child(t)
    else:
        if height(t.right) - height(t.left) > 1:
            if height(t.right.right) >= height(t.right.left):
                t = rotate_with_right_child(t)
            else:
                t = double_rotate_with_right_child(t)
    t.height = max(height(t.left), height(t.right)) + 1
    return t


def rotate_with_left_child(a):
    """Update heights and return new root"""
    b = a.left
    a.left = b.right
    b.right = a
    a.height = max(height(a.left), height(a.right)) + 1
    b.height = max(height(b.left), a.height) + 1
    return b


def rotate_with_right_child(a):
    """Update heights and return new root"""
    b = a.right
    a.right = b.left
    b.left = a
    a.height = max(height(a.left), height(a.right)) + 1
    b.height = max(height(b.right), a.height) + 1
    return b


def double_rotate_with_left_child(a):
    """Rotate left child with its right child and a with new left child"""
    a.left = rotate_with_right_child(a.left)
    return rotate_with_left_child(a)


def double_rotate_with_right_child(a):
    """Rotate right child with its left child and a with new right child"""
    a.right = rotate_with_left_child(a.right)
    return rotate_with_right_child(a)
