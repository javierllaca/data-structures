from data_structures.queue import FIFO, LIFO
from random import randrange


def max_queue(a, queue):
    for elem in a:
        if queue.is_empty():
            queue.push(elem)
        elif elem > queue.peek():
            queue.pop()
            queue.push(elem)
    return queue.pop()


a = [randrange(100) for i in range(1000)]

assert max(a) == max_queue(a, FIFO())
assert max(a) == max_queue(a, LIFO())
