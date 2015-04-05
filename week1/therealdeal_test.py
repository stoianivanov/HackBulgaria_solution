import unittest
from therealdeal import *


class TheRealDealTest(unittest.TestCase):
    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(8), 15)

    def test_sum_of_divisors_3(self):
        self.assertEqual(sum_of_divisors(1000), 2340)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_2(self):
        self.assertTrue(is_prime(11))

    def test_is_prime_3(self):
        self.assertFalse(is_prime(1))

    def test_number_of_divisors(self):
        self.assertTrue(prime_number_of_divisors(7))

    def test_number_of_divisors_2(self):
        self.assertFalse(prime_number_of_divisors(8))

if __name__ == '__main__':
    unittest.main()
