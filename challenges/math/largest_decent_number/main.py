def largest_decent_number(n):
    """Returns the largest decent number having n digits"""
    if n % 3 == 0:
        return int('5' * n)
    i = n
    while i % 3 != 0:
        i -= 5
        if i < 0:
            return -1
    return int('5' * i + '3' * (n - i))


t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    print largest_decent_number(n)
