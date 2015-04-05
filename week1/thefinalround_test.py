import unittest
from thefinalround import *


class TheFinalRoundTest(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]),{'apple': 2, 'pie': 1, 'banana': 1})

    def test_unique_words_count(self):
        self.assertEqual(unique_words_count(["apple", "banana", "apple", "pie"]), 3)

    def test_nan_expand(self):
        self.assertEqual(nan_expand(0), '')

    def test_nan_expand_2(self):
        self.assertEqual(nan_expand(2), "Not a Not a NaN")

    def test_iterations_of_nan_expand(self):
        self.assertEqual(iterations_of_nan_expand(''), 0)

    def test_iterations_of_nan_expand_2(self):
        self.assertEqual(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'), 10)

    def test_iterations_of_nan_expand_3(self):
        self.assertFalse(iterations_of_nan_expand("Show these people!"))

    def test_prime_factoriazation(self):
        self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])

    def test_group(self):
        self.assertEqual(group([1, 1, 1, 2, 3, 1, 1]), [[1, 1, 1], [2], [3], [1, 1]])

    def test_max_consecutive(self):
        self.assertEqual(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)

    def test_groupby(self):
        self.assertEqual(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]), {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})

    def test_spam_eggs(self):
        self.assertEqual(prepare_meal(5), "eggs")

    def test_spam_eggs_meal(self):
        self.assertEqual(prepare_meal(3), 'spam')

    def test_spam_and_eggs(self):
        self.assertEqual(prepare_meal(27), "spam spam spam")

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path('/'), '/')

    def test_reduce_file_path_2(self):
        self.assertEqual(reduce_file_path('/srv/www/htdocs/wtf/'), '/srv/www/htdocs/wtf')

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn(""))

    def test_is_an_bn_2(self):
        self.assertFalse(is_an_bn("rado"))

    def test_credit_card_validation(self):
        self.assertTrue(is_credit_card_valid(79927398713))

    def test_credit_card_validation_2(self):
        self.assertFalse(is_credit_card_valid(79927398715))

    def test_goldbach(self):
        self.assertEqual(goldbach(4), [(2, 2)])

    def test_magic_square(self):
        self.assertTrue(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))

    def test_magic_square_2(self):
        self.assertFalse(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

    def test_friday_years(self):
        self.assertEqual(friday_years(1000, 2000), 178)

if __name__ == '__main__':
    unittest.main()
