from data_structures.tree.bst import BST


def k_smallest(n, k):
    if k == 0 or not n:
        return []
    left = k_smallest(n.left, k)
    if len(left) == k:
        return left
    mid = [n.key]
    if len(left) + 1 == k:
        return left + mid
    right = k_smallest(n.right, k - len(left) - 1)
    return left + mid + right


t = BST()
for e in [5, 3, 7, 2, 4, 6, 8]:
    t.insert(e)

print str(t)

for i in range(8):
    print k_smallest(t.root, i)
