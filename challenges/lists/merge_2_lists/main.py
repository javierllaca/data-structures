from data_structures.list import List


def merge(l1, l2):
    res = List()
    m, n = l1.head, l2.head
    while m and n:
        if m.val <= n.val:
            res.push_back(m.val)
            m = m.next
        else:
            res.push_back(n.val)
            n = n.next
    p = m or n  # remaining list
    while p:
        res.push_back(p.val)
        p = p.next
    return res


l1 = List(range(10))
l2 = List(range(10, 20))

assert merge(l1, l2) == List(range(20))
