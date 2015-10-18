class Polynomial:

    def __init__(self, val=None):
        self.val = val or {}

    def evaluate(self, x):
        sum = 0
        for power in self.val:
            sum += self[power] * (x ** power)
        return sum

    def __neg__(self):
        res = Polynomial()
        for power in self.val:
            res[power] = -self[power]
        return res

    def __add__(self, other):
        res = Polynomial()
        powers = set(self.val.keys()).union(set(other.val.keys()))
        for power in powers:
            res[power] = 0
            if power in self.val:
                res[power] += self[power]
            if power in other.val:
                res[power] += other[power]
        return res

    def __mul__(self, other):
        res = Polynomial()
        for k1 in self.val:
            temp = Polynomial()
            for k2 in other.val:
                temp[k1 + k2] = self[k1] * other[k2]
            res += temp
        return res

    def __pow__(self, i):
        if i == 0:
            return Polynomial({0: 1})
        return self * (self ** (i - 1))

    def __getitem__(self, i):
        return self.val[i]

    def __setitem__(self, i, val):
        self.val[i] = val

    def __str__(self):
        s, powers = '', sorted(self.val.keys(), reverse=True)
        for power in powers:
            if self[power] == -1 and power != 0:
                s += '-'
            if abs(self[power]) != 1 or power == 0:
                s += str(self[power])
            if power > 0:
                s += 'x'
            if power > 1:
                s += '^' + str(power)
            if power != powers[-1]:
                s += ' + '
        return s

if __name__ == '__main__':
    p = Polynomial({2: 1, 1: 1, 0: 1})
    r = Polynomial({2: 1, 1: 1, 0: 1})
    q = Polynomial({3: 56, 2: -1, 1: 2, 0: 1})
    a = Polynomial({1: 1, 0: 1})
    print (p + q + r).evaluate(3)
    print str(p * r)
    for i in range(10):
        print '(', a, ')^', i, '=', str(a ** i)
    print str(-p)
