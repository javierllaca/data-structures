def frequency(s):
    """Returns a dictionary with the frequency of each character in s"""
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq


def is_permutation(s1, s2):
    """Determines whether s2 is a permutation of s1"""
    if len(s1) != len(s2):
        return False
    f1 = frequency(s1)
    f2 = frequency(s2)
    if len(f1) != len(f2):
        return False
    for key in f1:
        if key not in f2 or f1[key] != f2[key]:
            return False
    return True


assert is_permutation('cat', 'tac')
assert is_permutation('abba', 'baab')
assert is_permutation('abcd', 'abcc')
