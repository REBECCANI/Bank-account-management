from account import BankAccount
from savings import SavingsAccount
from checking import CheckingAccount
from credit import CreditCardAccount

# Create instances of each account type
account1 = BankAccount("John Doe", 1000, "12345")
savings1 = SavingsAccount("Alice Smith", 5000, "54321", 2.5)
checking1 = CheckingAccount("Bob Johnson", 2000, "67890", -1000)
credit1 = CreditCardAccount("Eve Brown", 0, "98765", 5000)

# Perform actions on the accounts
account1.deposit(500)
account1.withdraw(200)
savings1.deposit(1000)
savings1.calculate_interest()
checking1.withdraw(2500)
credit1.make_purchase(1000)

# Create a list of accounts and print their details
accounts = [account1, savings1, checking1, credit1]

for account in accounts:
    print(account)
    print("=" * 30)
