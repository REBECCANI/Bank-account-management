from account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, account_number=None, interest_rate=0.0):
        super().__init__(owner, balance, account_number)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.__interest_rate / 100

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.__interest_rate}%"
