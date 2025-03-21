class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")

    def get_balance(self):
        return self._balance

    def can_withdraw(self, amount):
        return amount <= self._balance


class SavingsAccount(BankAccount):
    def can_withdraw(self, amount):
        return self._balance - amount >= 100


def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")


# Testowanie
regular_account = BankAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)  # Works
#perform_transaction(savings_account, 500, 450)  # Exception !
