from math import sqrt


class Rational:

    def __init__(self, num=0, denom=1):
        self.num = num
        self.denom = denom
        self.simplify()

    def __abs__(self):
        return Rational(abs(self.num), abs(self.denom))

    def __neg__(self):
        return Rational(-self.num, self.denom)

    def __invert__(self):
        return Rational(self.denom, self.num)

    def __add__(self, other):
        return Rational(
            self.num * other.denom + other.num * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Rational(self.num * other.num, self.denom * other.denom)

    def __div__(self, other):
        return self * ~other

    def __pow__(self, n):
        return Rational(self.num ** n, self.denom ** n)

    def sqrt(self):
        return Rational(sqrt(self.num), sqrt(self.denom))

    def simplify(self):
        g = gcd(abs(self.num), abs(self.denom))
        self.num = self.num / g
        self.denom = self.denom / g

    def double(self):
        return float(self.num) / float(self.denom)

    def __eq__(self, other):
        return self.num == other.num and self.denom == other.denom

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.denom)


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def parse_rational(s):
    if '/' in s:
        toks = map(int, s.split('/'))
        return Rational(toks[0], toks[1])
    if '.' in s:
        toks = s.split('.')
        return Rational(int(toks[0])) + Rational(
            int(toks[1]),
            10 ** (len(toks[1]) + 1)
        )
    return Rational(int(s))


if __name__ == '__main__':
    a = Rational(3)
    b = parse_rational('3/4')
    c = ~b
    d = parse_rational('3.15')
    print str(a)
    print str(b)
    print str(c)
    print str(b * c)
    print str(d)
