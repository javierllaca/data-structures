class Queue:

    def __init__(self):
        self._queue = []

    def is_empty(self):
        return not self._queue

    def push(self, x):
        self._queue.append(x)

    def pop(self):
        raise Exception('Not implemented')

    def peek(self):
        raise Exception('Not implemented')

    def __getitem__(self, i):
        return self._queue[i]

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)


class FIFO(Queue):

    def pop(self):
        return self._queue.pop(0)

    def peek(self):
        return self._queue[0]


class LIFO(Queue):

    def pop(self):
        return self._queue.pop()

    def peek(self):
        return self._queue[-1]
