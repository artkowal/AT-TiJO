import unittest
from lab04_pokrycieKoduTestami.src.atm import ATM, InvalidPinException, InsufficientFundsException


class ATMTest(unittest.TestCase):
    def setUp(self):
        # arrange
        self.atm = ATM(initial_balance=1000, correct_pin=1234)


    def test_raise_error_when_pin_is_invalid_on_check_balance(self):
        # act & assert
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(1111)

    def test_return_balance_when_pin_is_correct(self):
        # act
        balance = self.atm.check_balance(1234)

        # assert
        self.assertEqual(balance, 1000)

    def test_increase_balance_when_deposit_is_successful(self):
        # act
        new_balance = self.atm.deposit(1234, 500)

        # assert
        self.assertEqual(new_balance, 1500)

    def test_raise_error_when_pin_is_invalid_on_deposit(self):
        # act & assert
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(1111, 500)

    def test_raise_error_when_deposit_amount_is_negative(self):
        # act & assert
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, -500)

    def test_decrease_balance_when_withdraw_is_successful(self):
        # act
        new_balance = self.atm.withdraw(1234, 500)

        # assert
        self.assertEqual(new_balance, 500)

    def test_raise_error_when_withdraw_amount_exceeds_balance(self):
        # act & assert
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(1234, 2000)

    def test_raise_error_when_pin_is_invalid_on_withdraw(self):
        # act & assert
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(1111, 500)

    def test_raise_error_when_withdraw_amount_is_negative(self):
        # act & assert
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, -500)