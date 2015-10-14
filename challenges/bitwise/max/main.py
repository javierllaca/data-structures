def max(a, b):
    c = a - b
    k = (c >> 31) & 0x1
    return a - k * c


print max(5, 10)
print max(7, -1)
print max(0, 0)
