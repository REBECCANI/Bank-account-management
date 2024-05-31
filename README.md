Overview
--------
This task involves creating a bank account management system using advanced object-oriented programming concepts such as encapsulation, inheritance, method overriding, and polymorphism. The solution consists of multiple Python classes and methods to manage different types of bank accounts, as well as serialization and deserialization of account data.

Structure
---------
1. Files:
    - account.py: Contains the BankAccount class.
    - savings.py: Contains the SavingsAccount class that inherits from BankAccount.
    - checking.py: Contains the CheckingAccount class that inherits from BankAccount.
    - credit.py: Contains the CreditCardAccount class that inherits from BankAccount.
    - tester.py: Contains code to test the functionality of the classes and demonstrate polymorphism.
    - serializer.py: Contains functions to serialize and deserialize account objects to and from JSON files.
    - account.json: JSON file for storing serialized account data.

2. Classes and Methods:
    - BankAccount (account.py)
        - Attributes: __account_owner, __balance, __account_number
        - Methods: deposit(amount), withdraw(amount), get_account_owner(), get_account_number(), get_balance(), set_balance(balance), __str__()
    - SavingsAccount (savings.py)
        - Attributes: __interest_rate
        - Methods: calculate_interest(), __str__()
    - CheckingAccount (checking.py)
        - Attributes: __overdraft_limit
        - Methods: withdraw(amount), __str__()
    - CreditCardAccount (credit.py)
        - Attributes: __credit_limit
        - Methods: make_purchase(amount), __str__()
    - Serializer Functions (serializer.py)
        - Methods: serializeToJson(account, file_path), deserializeFromJson(file_path)

3. Testing (tester.py)
    - Creation and manipulation of different account types.
    - Demonstration of polymorphism by adding different account objects to a list and iterating over them.

How to Run
----------
1. Set Up:
    - Ensure you have Python installed on your system.
    - Place all the .py files in the same directory.

2. Execution:
    - Open a terminal/command prompt and navigate to the directory containing the files.
    - Run the tester script to test the functionality:
      python tester.py
    - To test serialization and deserialization, modify the tester.py or create a new script to call serializeToJson() and deserializeFromJson() functions from serializer.py.



Error Handling
--------------
The serialization functions in serializer.py include basic error handling to ensure that file read/write operations degrade gracefully in case of exceptions.

Internal Documentation
