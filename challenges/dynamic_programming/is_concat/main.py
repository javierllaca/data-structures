def valid_substring(dp, i, s):
    if i == len(dp):
        return True
    for k in range(i, len(dp)):
        if dp[i][k] and valid_substring(dp, k + 1, s):
            return True
    return False


def is_concat(s, d):
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] in d:
                dp[i][j] = True
    return valid_substring(dp, 0, s)


assert is_concat(
    'catworld',
    set(['hello', 'world', 'cat'])
)

assert is_concat(
    'caterdog',
    set(['cat', 'dog', 'cater'])
)

assert not is_concat(
    'caterdo',
    set(['cat', 'dog', 'cater'])
)
