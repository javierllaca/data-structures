"""
1. Implement the following OCaml type in the language of your choice:

type t =
    | A of int
    | B of (t * t)

2. Write code to check if two values of type T are equal.
"""


class T:

    def __init__(self, x, y=None):
        if not y:
            if isinstance(x, int):
                self.x = x
            else:
                raise Exception
        else:
            if isinstance(x, T) and isinstance(y, T):
                self.x = x
                self.y = y
            else:
                raise Exception

    def is_leaf(self):
        return isinstance(self.x, int)

    def __eq__(self, other):
        if self.is_leaf():
            return other.is_leaf() and self.x == other.x
        if not other.is_leaf():
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        if self.is_leaf():
            return str(self.x)
        return '({}) ({})'.format(self.x, self.y)


a = T(T(T(3), T(5)), T(4))

b = T(T(T(3), T(5)), T(4))
assert a == b

c = T(T(3), T(4))
assert not a == c
