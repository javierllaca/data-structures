from sys import stdin


def interleave_words_and_spaces(words, spaces):
    s = ''
    if len(words) - 1 != len(spaces):
        return None
    for i in range(len(spaces)):
        s += words[i] + ' ' * spaces[i]
    return s + words[-1]


def justify(s, n):
    tokens = s.split()
    if len(tokens) == 0:
        return ''
    if len(tokens) == 1:
        return tokens[0]
    if len(tokens[0]) > n:
        tokens[0] = tokens[0][n:]
        words, spaces = [tokens[0]], []
    else:
        i = 0
        word_length, space_length = len(tokens[0]), 0
        words, spaces = [tokens[0]], []
        while i < len(tokens):
            a, b = word_length + len(tokens[i]), space_length + 1
            if a + b > n:
                break
            else:
                word_length, space_length = a, b
                words.append(tokens[i])
                spaces.append(1)
                i += 1
        j = 0
        while word_length + space_length - 1 < n:
            spaces[j] += 1
            space_length += 1
            j = (j + 1) % len(spaces)
    return '{}\n{}'.format(
        interleave_words_and_spaces(words, spaces),
        justify(' '.join(tokens[i:]), n)
    )


for line in stdin:
    print justify(line, 80)
