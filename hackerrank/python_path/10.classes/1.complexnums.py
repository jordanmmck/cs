import math


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def mod(self):
        return math.sqrt(self.re**2 + self.im**2)

    def __add__(self, c2):
        return Complex(self.re + c2.re, self.im + c2.im)

    def __sub__(self, c2):
        return Complex(self.re - c2.re, self.im - c2.im)

    def __mul__(self, c2):
        return Complex(
            self.re *
            c2.re -
            self.im *
            c2.im,
            self.im *
            c2.re +
            self.re *
            c2.im)

    def __div__(self, c2):
        con = Complex(c2.re, c2.im).conjugate()
        return Complex((self * con) / (c2.mod()**2))

    def conjugate(self):
        return Complex(self.re, -self.im)

    def __str__(self):
        if self.im >= 0:
            return '%.2f+%.2fi' % (self.re, self.im)
        else:
            return '%.2f-%.2fi' % (self.re, -self.im)


c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(mod(c1))
print(mod(c2))
