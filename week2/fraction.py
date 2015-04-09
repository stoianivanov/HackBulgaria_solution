class Fraction:

    def __init__(self, numerator, denominator):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise TypeError

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.numerator/self.denominator == other.numerator/other.denominator

    def __add__(self, other):
        numerator = self.denominator*other.numerator + self.numerator*other.denominator
        denominator = self.denominator * other.denominator
        if denominator % numerator == 0:
            return Fraction(1, denominator // numerator)
        else:
            return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.denominator*other.numerator - self.numerator*other.denominator
        denominator = self.denominator * other.denominator
        if numerator == 0:
            return 0
        elif denominator % numerator == 0:
            return Fraction(1, denominator // numerator)
        else:
            return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator*other.numerator
        denominator = self.denominator * other.denominator
        if denominator % numerator == 0:
            return Fraction(1, denominator // numerator)
        else:
            return Fraction(numerator, denominator)
