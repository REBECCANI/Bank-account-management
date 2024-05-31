import json
from account import BankAccount
from savings import SavingsAccount
from checking import CheckingAccount
from credit import CreditCardAccount

def serializeToJson(account_obj, filename):
    filename = "account.json"
    try:
        if isinstance(account_obj, (BankAccount, SavingsAccount, CheckingAccount, CreditCardAccount)):
            account_data = vars(account_obj)
            account_data['__class__'] = account_obj.__class__.__name__
            with open(filename, 'w') as json_file:
                json.dump(account_data, json_file, indent=4)
            print(f"Account details serialized to {filename}.")
        else:
            print("Invalid account object.")
    except Exception as e:
        print(f"Error occurred during serialization: {e}")

def deserializeFromJson(filename):
    filename = "account.json"
    try:
        with open(filename, 'r') as json_file:
            account_data = json.load(json_file)
            account_class_name = account_data.get('__class__')
            if account_class_name == 'BankAccount':
                return BankAccount(**account_data)
            elif account_class_name == 'SavingsAccount':
                return SavingsAccount(**account_data)
            elif account_class_name == 'CheckingAccount':
                return CheckingAccount(**account_data)
            elif account_class_name == 'CreditCardAccount':
                return CreditCardAccount(**account_data)
            else:
                print("Invalid account type in JSON data.")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
    return None

# Example usage within serializer.py:

# Creating a BankAccount object
account = BankAccount("John Doe", 1000, "12345")

# Serializing the BankAccount object to JSON
serializeToJson(account, "account.json")

# Deserializing the BankAccount object from JSON
deserialized_account = deserializeFromJson("account.json")
if deserialized_account:
    print("Deserialized Account:")
    print(deserialized_account)
