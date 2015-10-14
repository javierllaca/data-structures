def compute_fibs(hi):
    fibs = [1]
    next = 1
    while next < hi:
        fibs.append(next)
        next = fibs[-1] + fibs[-2]
    return fibs

print sum([fib for fib in compute_fibs(4000000) if fib % 2 == 0])
