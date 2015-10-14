"""
Given an array of integers and an integer k denoting the maximum distance from
every integer to its sorted position, sort the array in linear time
"""

from data_structures.priority import PriorityQueue


def sort(a, k):
    q = PriorityQueue()
    for elem in a:
        if len(q) == k + 1:
            yield q.pop()
        q.push(elem)
    while not q.is_empty():
        yield q.pop()


a = [1, 0, 2, 4, 3]
for elem in sort(a, 1):
    print elem
