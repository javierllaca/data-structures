from data_structures.queue import LIFO


class StackQueue:

    def __init__(self):
        self.stack1 = LIFO()
        self.stack2 = LIFO()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


q = StackQueue()

for i in range(10):
    q.push(i)

res = []
while not q.is_empty():
    res.append(q.pop())

assert res == range(10)
