import unittest
from warmups import *


class WarmupsTest(unittest.TestCase):
    def test_factorial_with_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_with_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_with_five(self):
        self.assertEqual(factorial(5), 120)

    def test_fibanocci_with_one(self):
        self.assertEqual(fibonacci(1), [1])

    def test_fibanocci_with_two(self):
        self.assertEqual(fibonacci(2), [1, 1])

    def test_fibanocci_with_three(self):
        self.assertEqual(fibonacci(3), [1, 1, 2])

    def test_fibanocci_with_ten(self):
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_sum_of_digits_with_negative(self):
        self.assertEqual(sum_of_digits(-10), 1)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)

    def test_sum_of_digits_with_six(self):
        self.assertEqual(sum_of_digits(6), 6)

    def test_fact_digits_1(self):
        self.assertEqual(fact_digits(111), 3)

    def test_fact_digits_2(self):
        self.assertEqual(fact_digits(145), 145)

    def test_fact_digits_3(self):
        self.assertEqual(fact_digits(999), 1088640)

    def test_palindrome_with_numbers(self):
        self.assertTrue(palindrome(121))

    def test_palindrome_with_string(self):
        self.assertTrue(palindrome("kapak"))

    def test_palindrome_with_string_false(self):
        self.assertFalse(palindrome("baba"))

    def test_to_digits_1(self):
        self.assertEqual(to_digits(123), [1, 2, 3])

    def test_to_digits_2(self):
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])

    def test_to_digits_3(self):
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_number(self):
        self.assertEqual(to_number([1, 2, 3]), 123)

    def test_to_number_(self):
        self.assertEqual(to_number([9, 9, 9, 9, 9]), 99999)

    def test_to_number_3(self):
        self.assertEqual(to_number([1, 2, 3, 0, 2, 3]), 123023)

    def test_fib_number(self):
        self.assertEqual(fib_number(3), 112)

    def test_fib_number_(self):
        self.assertEqual(fib_number(10), 11235813213455)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)

    def test_count_vowels_2(self):
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)

    def test_count_vowels_3(self):
        self.assertEqual(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"), 22)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("grrrrgh!"), 7)

    def test_count_consonants_2(self):
        self.assertEqual(count_consonants("A nice day to code!"), 6)

    def test_char_histogram(self):
        self.assertEqual(char_histogram("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})

    def test_char_histogra2(self):
        self.assertEqual(char_histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3})

    def test_p_score(self):
        self.assertEqual(p_score(121), 1)

    def test_p_score_2(self):
        self.assertEqual(p_score(198), 6)

    def test_is_increasing(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))

    def test_is_increasing_2(self):
        self.assertFalse(is_increasing([1, 1, 1]))

    def test_is_decreasing(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))

    def test_is_decreasing_2(self):
        self.assertFalse(is_decreasing([1, 1, 2, 1]))

    def test_next_hack(self):
        self.assertEqual(next_hack(0), 1)

    def test_next_hack_2(self):
        self.assertEqual(next_hack(10), 21)

    def test_next_hack_3(self):
        self.assertEqual(next_hack(8031), 8191)
if __name__ == '__main__':
    unittest.main()
