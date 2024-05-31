""" NAMES: NISHIMWE REBECCA
ANDREW ID: nrebecca@andrew.cmu.edu"""
class BankAccount:
    def __init__(self, owner, balance=0, account_number=None):
        self.__owner = owner
        self.__balance = balance
        self.__account_number = account_number

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Withdrawal amount must be greater than zero and less than or equal to the balance.")

    def __str__(self):
        return f"Account Owner: {self.__owner}\nAccount Number: {self.__account_number}\nBalance: ${self.__balance:.2f}"
