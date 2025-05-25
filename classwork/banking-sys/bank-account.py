#  Practical Coding Task: 
# ➢ Scenario: 
# You’re creating a BankAccount class where: 
# • The balance should not be directly accessible or changeable. 
# • Only controlled functions should be able to set or get the balance. 
# ❖ Task Requirements: 
# 1. Create a class called BankAccount. 
# 2. Use _ _init_ _() to take: 
# o account_holder 
# o initial_balance (set this as a private variable using __balance) 
# 3. Add the following methods: 
# i: deposit(amount) —> only adds if amount is positive 
# ii: withdraw(amount) —> checks if balance is enough before deducting 
# iii: get_balance() —> returns current balance (getter) 
# iv:  set_balance(amount) —> sets balance only if amount is valid (setter with validation) 
# 4. Create an object with sample data. 
# 5. Try to access __balance directly (and see it fails). 
# 6. Use the methods to: 
# i. Deposit money   ii. Withdraw money   iii:Print balance using getter

# Solution:

class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.__balance = balance # private variable
        print(f"Account Holder: {self.account_holder}, Initial Balance: {self.__balance}")
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount: float):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount: float):
        if amount >= 0:
            self.__balance = amount
            print(f"New Balance: {self.__balance}")
        else:
            print("Invalid balance amount.")
# Creating an object with sample data
account = BankAccount("Ali", 1000.0)
# Trying to access __balance directly (will fail)
try:
    print(account.__balance)
except AttributeError as e:
    print(f"AttributeError: {e}")
# Using the methods to deposit, withdraw, and print balance
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: {account.get_balance()}")
# Setting a new balance
account.set_balance(1500)
# Trying to set an invalid balance
account.set_balance(-100)
# Trying to withdraw more than the balance
account.withdraw(2000)
# Trying to withdraw a valid amount
account.withdraw(1000)
# Trying to deposit a negative amount   
account.deposit(-200)
# Trying to deposit a valid amount
account.deposit(300)