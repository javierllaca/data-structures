from data_structures.list import List


class FancyList(List):

    def __add__(self, other):
        return list_sum(self, other)


def list_sum(a, b):
    l = FancyList()
    carry = 0
    p, q = a.head, b.head
    while p and q:
        sum = p.val + q.val + carry
        carry = sum / 10
        l.push_back(sum % 10)
        p = p.next
        q = q.next
    r = p if p else q
    while r:
        sum = r.val + carry
        carry = sum / 10
        l.push_back(sum % 10)
        r = r.next
    while carry != 0:
        l.push_back(carry % 10)
        carry = carry / 10
    return l


def int_to_list(n):
    return FancyList(map(int, list(str(n))[::-1]))


def test(a, b):
    l1 = int_to_list(a)
    l2 = int_to_list(b)
    l3 = int_to_list(a + b)
    assert l1 + l2 == l3


tests = [
    (10, 13),
    (0, 0),
    (1, 1)
]

for a, b in tests:
    test(a, b)
