import unittest
from cash_desk import *


class BillTest(unittest.TestCase):
    def test_create_new_bill_class(self):
        bill = Bill(10)
        self.assertTrue(isinstance(bill, Bill))

    def test_create_int_value_from_bill(self):
        bill = Bill(10)
        self.assertEqual(int(bill), 10)

    def test_amount_in_bill(self):
        bill = Bill(10)

        with self.assertRaises(AttributeError):
            bill.f

    def test_str_dunder_for_bill(self):
        bill = Bill(10)

        self.assertEqual(str(bill), "A 10$ bill")

    def test_repr_dunder_for_bill(self):
        bill = Bill(10)

        self.assertEqual(repr(bill), "A 10$ bill")

    def test_eq_between_bills_when_not_same(self):
        bill1 = Bill(10)
        bill2 = Bill(11)

        self.assertTrue(bill1 != bill2)

    def test_eq_between_bills_when_same(self):
        bill1 = Bill(10)
        bill2 = Bill(10)

        self.assertTrue(bill1 == bill2)

    def test_can_hash_bill(self):
        bill = Bill(10)

        self.assertIsNotNone(hash(bill))

    def test_can_put_bill_in_dictionary(self):
        money_holder = {}
        bill = Bill(10)

        money_holder[bill] = 1

        self.assertTrue(bill in money_holder)

    def test_value_error_raises_from_negative_amount(self):
        with self.assertRaises(ValueError):
            bill = Bill(-10)

    def test_value_error_raises_from_zero_amount(self):
        with self.assertRaises(ValueError):
            bill = Bill(0)

    def test_type_error_raises_from_float_amount(self):
        with self.assertRaises(TypeError):
            bill = Bill(0.5)

    def test_dect_cash_desk(self):
        money_holder = {}
        a = Bill(10)
        money_holder[a] = 1
        c = Bill(10)
        if c in money_holder:
            money_holder[c] += 1
        self.assertEqual(money_holder, {Bill(10): 2})


class BillBatchTest(unittest.TestCase):
    def setUp(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        self.bills = BillBatch(bills)

    def test_creat_bill_batch(self):

        self.assertTrue(isinstance(self.bills, BillBatch))

    def test_dunder_len(self):
        self.assertEqual(len(self.bills), 4)

    def test_iteration_with_dunder_int(self):
        self.assertEqual(int(self.bills[1]), 20)

    def test_iteration_with_dunder_str(self):
        self.assertEqual(str(self.bills[2]), str(Bill(50)))

    def test_iteration_type_error(self):
        with self.assertRaises(TypeError):
            self.bills[10]

    def test_total(self):
        self.assertEqual(self.bills.total(), 180)


class CashDeskTest(unittest.TestCase):
    def setUp(self):
        self.desk = CashDesk()

    def test_create_cash_desk(self):
        self.assertTrue(isinstance(self.desk, CashDesk))

    def test_type_error_with_non_dict(self):
        with self.assertRaises(TypeError):
            cdesk = CashDesk(desk=[10])

    def test_type_error_with_non_int(self):
        with self.assertRaises(TypeError):
            cdesk = CashDesk(total=0.5)

    def test_value_error_with_negative(self):
        with self.assertRaises(ValueError):
            cdesk = CashDesk(total=-10)

    def test_total(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BillBatch(bills)
        self.desk.take_money(batch)
        self.desk.take_money(Bill(10))
        self.assertEqual(self.desk.total, 390)

if __name__ == '__main__':
    unittest.main()
