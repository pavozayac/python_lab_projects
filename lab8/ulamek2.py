import sys
import random
from math import gcd

class Fraction:
    __slots__ = ('numerator', 'denominator')
    
    
    def __init__(self, numerator: int, denominator: int):
        assert denominator != 0

        self.numerator = numerator
        self.denominator = denominator

        self.__normalize()

    def __normalize(self):
        self.numerator = self.numerator * abs(self.denominator) // self.denominator
        self.denominator = abs(self.denominator)

        mygcd = gcd(self.numerator, self.denominator)

        self.numerator //= mygcd
        self.denominator //= mygcd

    def __str__(self) -> str:
        if self.numerator == 0:
            return '0'
        else:
            return f'{self.numerator} / {self.denominator}'

    def __repr__(self) -> str:
        if self.numerator == 0:
            return '0'
        else:
            return f'{self.numerator} / {self.denominator}'
    
    def __add__(self, other):
        return Fraction(self.numerator*other.denominator + other.numerator*self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator*other.denominator - other.numerator*self.numerator, self.denominator * other.denominator)
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        return (self.numerator, self.denominator) == (other.numerator, other.denominator)

    def __ne__(self, other):
        return (self.numerator, self.denominator) != (other.numerator, other.denominator)
    
    def __lt__(self, other):
        return self.numerator*other.denominator < other.numerator*self.denominator

    def __le__(self, other):
        return self.numerator*other.denominator <= other.numerator*self.denominator

    def __gt__(self, other):
        return self.numerator*other.denominator > other.numerator*self.denominator

    def __ge__(self, other):
        return self.numerator*other.denominator >= other.numerator*self.denominator


if __name__ == '__main__':
    assert len(sys.argv) == 3

    n = int(sys.argv[1])
    k = int(sys.argv[2])

    assert k < n

    tab = []

    for i in range(n):
        tab.append(Fraction(random.randint(-100, 100), random.randint(1, 200)))

    for i in range(k):
        tab[i] += tab[i+1]

    