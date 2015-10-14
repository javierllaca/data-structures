from data_structures.tree.bst import BST


def get_interval(n, i, j):
    if not n:
        return []
    if n.key < i:
        return get_interval(n.right, i, j)
    if n.key > j:
        return get_interval(n.left, i, j)
    left = get_interval(n.left, i, j)
    mid = [n.key]
    right = get_interval(n.right, i, j)
    return left + mid + right


t = BST()
for e in [5, 3, 7, 2, 4, 6, 8]:
    t.insert(e)

print str(t)

print get_interval(t.root, 4, 6)
