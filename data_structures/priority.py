from heapq import heapify, heappush, heappop
from random import randrange


class PriorityQueue:

    def __init__(self, queue=None):
        self.queue = queue or []
        heapify(self.queue)

    def is_empty(self):
        return not self.queue

    def push(self, value):
        heappush(self.queue, value)

    def pop(self):
        if len(self) > 0:
            return heappop(self.queue)
        return None

    def __len__(self):
        return len(self.queue)


def heap_sort(a):
    q = PriorityQueue(a)
    return [q.pop() for i in range(len(a))]


if __name__ == '__main__':
    a = [randrange(10000) for i in range(1000000)]
    a = heap_sort(a)
