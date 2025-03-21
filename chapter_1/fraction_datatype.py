import math

class Fraction:
    """Represents the fraction datatype"""
    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numerator and denominator must be integers.")  # Better error message
        
        if den == 0:
            raise ValueError("Denominator cannot be zero.")  # Keep this check
        if den < 0:
            num *= -1
            den *= -1
        
        reduce = math.gcd(num, den)  # Reduce fraction
        self.numerator = num // reduce
        self.denominator = den // reduce
    
    def __repr__(self):
        if self.numerator == 0:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)
    
    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __ne__(self, other):
        return self.numerator != other.numerator or self.denominator != other.denominator
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iadd__(self, other):
        ans = self.__add__(other)
        self.numerator = ans.numerator
        self.denominator = ans.denominator
        return self

f = Fraction(3, 4)
print(f)  # 3/4

f += Fraction(1, 4)  # In-place addition
print(f)  # 1/1 (simplified from 4/4)
