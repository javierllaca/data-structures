decimals = [
    1000,
    900,
    500,
    400,
    100,
    90,
    50,
    40,
    10,
    9,
    5,
    4,
    1,
]

romans = [
    'M',
    'CM',
    'D',
    'CD',
    'C',
    'XC',
    'L',
    'XL',
    'X',
    'IX',
    'V',
    'IV',
    'I',
]

r_d = dict(zip(romans, decimals))

d_r = dict(zip(decimals, romans))


def floor(n):
    for elem in decimals:
        if n >= elem:
            return elem
    return None


def decimal_to_roman(n):
    if n == 0:
        return ''
    if n in d_r:
        return d_r[n]
    f = floor(n)
    return d_r[f] * (n / f) + decimal_to_roman(n % f)


def roman_to_decimal(s):
    n = 0
    i = 0
    while i < len(s):
        if len(s) - i > 1:
            k = s[i:i + 2]
            if k in r_d:
                n += r_d[k]
                i += 2
                continue
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            j += 1
        n += r_d[s[i]] * (j - i)
        i = j
    return n


assert decimal_to_roman(1993) == 'MCMXCIII'
assert roman_to_decimal('LXXXIX') == 89
