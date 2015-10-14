from data_structures.tree.avl import AvlTree


def height(t):
    return 1 + max(height(t.left), height(t.right)) if t else 0


t = AvlTree()

# Test insertion
for elem in range(1000):
    t.insert(elem)
    root = t.root
    assert abs(height(root.left) - height(root.right)) <= 1
    assert t.find(elem) is not None

# Test deletion
for elem in range(1000):
    t.delete(elem)
    assert abs(height(root.left) - height(root.right)) <= 1
    assert t.find(elem) is None
