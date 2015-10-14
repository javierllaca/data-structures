from data_structures.tree.bst import BST


def inorder_heights(node, height=0):
    if node:
        return (
            inorder_heights(node.left, height + 1) +
            [height] +
            inorder_heights(node.right, height + 1)
        )
    return []


def is_palindrome(ls):
    mid = len(ls) / 2
    for i in range(mid):
        if ls[i] != ls[-i - 1]:
            return False
    return True


def is_symmetric(tree):
    return is_palindrome(inorder_heights(tree.root))


t = BST()
for i in [5, 3, 2, 4, 7, 6, 8]:
    t.add(i)
print is_symmetric(t)
