from account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, account_number=None, overdraft_limit=0):
        super().__init__(owner, balance, account_number)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.__overdraft_limit:
            super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds available balance and overdraft limit.")

    def __str__(self):
        return super().__str__() + f"\nOverdraft Limit: ${self.__overdraft_limit:.2f}"
