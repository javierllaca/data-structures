def all_unique(s):
    """Determine whether a string has all unique characters"""
    chars = set()
    for c in s:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True


assert all_unique('abcd')
assert not all_unique('abad')
