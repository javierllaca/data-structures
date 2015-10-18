"""
Given a string s, compute the longest substring of s containing at most n
unique characters.
"""

from random import randrange
from time import time


def longest_n_char_substring_brute(s, n):
    x, y = 0, 0
    for i in range(len(s)):
        c = set()
        for j in range(i, len(s)):
            if len(c) == n and j - i > y - x:
                x, y = i, j
            c.add(s[j])
    return s[x:y]


def longest_n_char_substring(s, n):
    """Returns the longest substring of s with at most n unique characters."""
    x, y = 0, 0
    j = 0
    while j < len(s):
        i = j
        c = set()
        while i > 0:  # look back
            if len(c) == n and s[i] not in c:
                break
            c.add(s[i])
            i -= 1
        i += 1  # i is inclusive, j is not
        while j < len(s):  # look ahead
            if len(c) == n and s[j] not in c:
                break
            c.add(s[j])
            j += 1
        if j - i > y - x:
            x, y = i, j
    return s[x:y]


def benchmark(f, args):
    start = time()
    res = f(*args)
    return res, time() - start


s = 'abbbbbbbaccccccccdccdaaeaa'
assert longest_n_char_substring(s, 2) == longest_n_char_substring_brute(s, 2)


for i in range(1, 5):
    s = ''.join([chr(randrange(26) + ord('a')) for _ in range(int(10 ** i))])

    r1, t1 = benchmark(longest_n_char_substring, (s, 4))
    r2, t2 = benchmark(longest_n_char_substring_brute, (s, 4))

    # Compare the lengths, since the actual substrings might be different --
    # the order in which substrings are considered is different.
    assert len(r1) == len(r2)
    assert t2 > t1
