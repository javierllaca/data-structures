class PriorityQueue:

    def __init__(self, capacity=128, a=None):
        self.a = [float('-inf') for _ in range(capacity)]
        if a:
            build_max_heap(a)
            for i in range(len(a)):
                self.a[i] = a[i]
        self.i = len(a) if a else 0

    def insert(self, key):
        self.i += 1
        self.a[self.i] = float('-inf')
        self.increase_key(self.i, key)

    def maximum(self):
        return self.a[0]

    def extract_max(self):
        x = self.a[0]
        self.a[0] = self.a[self.i]
        self.i -= 1
        max_heapify(self.a, 0)
        return x

    def increase_key(self, i, key):
        if key < self.a[i]:
            raise Exception
        self.a[i] = key
        while i > 0 and self.a[parent(i)] < self.a[i]:
            self.a[i], self.a[parent(i)] = self.a[parent(i)], self.a[i]
            i = parent(i)


def parent(i):
    return (i - 1) / 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(a, i):
    l = left(i)
    r = right(i)
    if l < len(a) and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < len(a) and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    for i in range(len(a) / 2, -1, -1):
        max_heapify(a, i)


def print_heap(a):
    n = 1
    i = 0
    while True:
        for j in range(n):
            print a[i],
            i += 1
            if i == len(a):
                print
                return
        print
        n *= 2


# Method 1
q1 = PriorityQueue(14, range(10))
q1.insert(10)

# Method 2
q2 = PriorityQueue(14)
for i in range(11):
    q2.insert(i)

print_heap(q1.a)
print_heap(q2.a)
