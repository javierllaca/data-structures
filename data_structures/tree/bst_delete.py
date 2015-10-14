from data_structures.tree.bst import BST

t = BST()

for i in [5, 3, 7, 2, 4, 6, 8]:
    t.insert(i)

for k in t:
    print k

print str(t)
t.delete(2)
print str(t)
t.delete(4)
print str(t)
