import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.acc = BankAccount("Rado", 0, "$")

    def test_creat_new_bank_account(self):
        self.assertTrue(isinstance(self.acc, BankAccount))

    def test_validation_bank_account(self):
        with self.assertRaises(ValueError):
            account = BankAccount("", -10, "$")

    def test_initial_zero_balance_bank_account(self):
        self.assertEqual(self.acc.balance(), 0)

    def test_str_dunder_bank_account(self):
        self.assertEqual(str(self.acc), "Bank account for Rado with balance of 0$")

    def test_repr_dunder_bank_account(self):
        self.assertEqual(repr(self.acc), "Rado : 0$")

    def test_int_dunder_bank_account(self):
        self.assertEqual(int(self.acc), 0)

    def test_deposit_bank_account(self):
        self.acc.deposit(1000)
        self.assertEqual(int(self.acc), 1000)

    def test_balance_bank_account(self):
        self.acc.deposit(1000)
        self.assertEqual(self.acc.balance(), 1000)

    def test_deposit_raise_error(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-1111)

    def test_withdraw_bank_account(self):
        self.acc.deposit(1000)
        self.assertTrue(self.acc.withdraw(500))

    def test_withdraw_answer_false_bank_account(self):
        self.acc.deposit(1000)
        self.assertFalse(self.acc.withdraw(1509))

    def test_history_bank_account(self):
        self.acc.deposit(1000)
        self.assertEqual(self.acc.history(), ['Account was created', 'Deposited 1000$'])

    def test_transfer_to_bank_account(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        self.assertTrue(rado.transfer_to(ivo, 500))

    def test_raise_type_error_bank_account(self):
        rado = BankAccount("Rado", 1000, "BGN")
        ivo = BankAccount("Ivo", 0, "BGN")
        self.assertRaises(not(rado.transfer_to(ivo, 500), TypeError))

if __name__ == '__main__':
    unittest.main()
