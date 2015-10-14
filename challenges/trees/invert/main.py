from data_structures.tree.bst import BST


def invert(t):
    if t:
        temp = t.left
        t.left = t.right
        t.right = temp
        invert(t.left)
        invert(t.right)


t = BST()
for elem in [5, 3, 7, 2, 4, 6, 8]:
    t.add(elem)

print str(t)
invert(t.root)
print str(t)
