# Byoung Hartzel L. Kim             9 - Beryllium
# 2nd quarter first task

# bankaccount class
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def set_account_number(self, account_number):
        # sets account number
        self._account_number = account_number

    def set_balance(self, balance):
        # checks if inputted balance is negative / positive
        if balance >= 0:
            self._balance = balance
            return self._balance
        else:
            print("The balance must be not be a negative number.")
            return None

    def get_account_number(self):
        # gives account number
        return self._account_number

    def get_balance(self):
        # gives balance
        return self._balance

# to check if the account is first second or third added
allaccounts = []
a1 = BankAccount(12345, 1000)
allaccounts.append(a1)

print(f"Account {len(allaccounts)}")
print(f"Account Number: {allaccounts[0].get_account_number()}")
print(f"Balance: {allaccounts[0].get_balance()}")

# sets balance to negative, it should say that its not possible and it will warn the user
a1.set_balance(-100)
print(f"Account Number: {allaccounts[0].get_account_number()}")
print(f"Balance: {allaccounts[0].get_balance()}")
