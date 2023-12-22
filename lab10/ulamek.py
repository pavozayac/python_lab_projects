import sys
import random
from math import gcd
import json

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

        assert denominator != 0

        self.__normalize()

    def __normalize(self):
        self.numerator = self.numerator * abs(self.denominator) // self.denominator
        self.denominator = abs(self.denominator)

        mygcd = gcd(self.numerator, self.denominator)

        self.numerator //= mygcd
        self.denominator //= mygcd

    def from_str(frac: str):
        f = frac.strip()
        if f == '0':
            return Fraction(0, 1)

        if '/' not in f:
            raise ValueError('Invalid format: separator \'/\' not found.')
        
        tokens =  f.split('/')

        if len(tokens) < 2:
            raise ValueError('Invalid format.')
        
        try:
            return Fraction(int(tokens[0].strip()), int(tokens[1].strip()))
        except ValueError:
            raise ValueError('Non-integer found in fraction field.')


    def save_to_file(self, fname: str):
        with open(fname, 'w') as myfile:
            myfile.write(str(self))

    def from_file(fname: str):
        with open(fname, 'r') as myfile:
            return Fraction.from_str(myfile.read())
    
            
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
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator*other.denominator - other.numerator*self.denominator, self.denominator * other.denominator)
    
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