from random import random


def pick(stream, k=1):
    res = []
    i = 1
    for elem in stream:
        if len(res) < k:
            res.append(elem)
        else:
            rand = random()
            if rand < float(k) / i:
                rand = int(random() * k)
                res[rand] = elem
        i += 1
    return res


f = {}

for i in range(10000):
    res = pick(range(10), 5)
    for elem in res:
        if elem in f:
            f[elem] += 1
        else:
            f[elem] = 1

for k, v in f.items():
    print k, v
