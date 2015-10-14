def computeFibs(n):
    """Returns the fibonacci numbers less than or equal to n"""
    fibs = [1]
    next = 2
    while next <= n:
        fibs.append(next)
        next = fibs[-1] + fibs[-2]
    return fibs


def encodeFibonacci(n):
    """Returns the binary fibonacci encoding for n"""
    s = ''
    fibs = computeFibs(n)
    for i in range(len(fibs) - 1, -1, -1):
        if n >= fibs[i]:
            n -= fibs[i]
            s += '1'
        else:
            s += '0'
        i -= 1
    return s


n = int(raw_input())
print encodeFibonacci(n)
