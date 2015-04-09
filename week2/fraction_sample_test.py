import unittest
from fraction import *


class FractionTest(unittest.TestCase):
    def setUp(self):
        self.fraction = Fraction(1, 2)

    def test_create_fraction(self):
        self.assertTrue(isinstance(self.fraction, Fraction))

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            f = Fraction("dsa", 2)

    def test_dunder_str(self):
        self.assertEqual(str(self.fraction), '1 / 2')

    def test_dunder_repr(self):
        self.assertEqual(repr(self.fraction), '1 / 2')

    def test_dunder_eq(self):
        fraction2 = Fraction(1, 2)
        self.assertTrue(self.fraction, fraction2)

    def test_add(self):
        fraction2 = Fraction(1, 2)
        self.assertEqual(str(self.fraction + fraction2), '1 / 1')

    def test_sub(self):
        fraction2 = Fraction(1, 2)
        self.assertEqual(str(self.fraction - fraction2), '0')

    def test_mul(self):
        fraction2 = Fraction(1, 2)
        self.assertEqual(str(self.fraction * fraction2), '1 / 4')
if __name__ == '__main__':
    unittest.main()
