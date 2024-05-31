from account import BankAccount

class CreditCardAccount(BankAccount):
    def __init__(self, owner, balance=0, account_number=None, credit_limit=0):
        super().__init__(owner, balance, account_number)
        self.__credit_limit = credit_limit

    def make_purchase(self, amount):
        if amount <= self.__credit_limit - self.get_balance():
            self.set_balance(self.get_balance() + amount)
        else:
            print("Purchase amount exceeds available credit limit.")

    def __str__(self):
        return super().__str__() + f"\nCredit Limit: ${self.__credit_limit:.2f}"
