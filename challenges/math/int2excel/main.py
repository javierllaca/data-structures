"""
Input: n > 0
Output: excel column string

e.g.:
1   'A'
.
.
.
26  'Z'
27  'AA'
.
.
.
52  'AZ'
53  'BA'
.
.
.
"""


def int2excel(n):
    s = ''
    while n != 0:
        s += chr(((n - 1) % 26) + ord('A'))
        n = (n - 1) / 26
    return s[::-1]


tests = [
    (1, 'A'),
    (26, 'Z'),
    (27, 'AA'),
    (52, 'AZ'),
    (53, 'BA')
]

for n, s in tests:
    assert int2excel(n) == s
