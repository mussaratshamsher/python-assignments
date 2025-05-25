

# Online banking System

from abc import ABC, abstractmethod

# ABSTRACTION: Abstract base class
class BankAccount(ABC):
    def __init__(self, name, balance):
        self._owner =name #encapsulation
        self.__balance = balance #encapsulation

    def deposit(self, amount):
        self.__balance +=amount #internal access to private modifier

    def account_type(self):
        print("No specific type") 

    # Abstraction: Abstract method to be implemented by subclass
    @abstractmethod
    def get_report(self):
        pass
    # Internal method to access private balance within child classes
    def _get_balance(self):
        return self.__balance
# Inheritance: BusinessAccount subclass
class BusinessAccount(BankAccount):
        def __init__(self, name, balance, company_name):
             super().__init__(name, balance)
             self.company_name = company_name

        def account_type(self):
             print("Business Account")     
        #Ploymorohism:  different implementation of get_report()
        def get_report(self):
             return f"{self.company_name} balance is {self._get_balance()}"
# Inheritance: IndividualAccount subclass
class IndividualAccount(BankAccount):
        def __init__(self, name, balance, cnic):
             super().__init__(name, balance)
             self.cnic = cnic
        def account_type(self):
             print("Individual Account")
# Polymorphism:  different implementation fo get_report()    
        def get_report(self):
             return f"CNIC {self.cnic} balance is {self._get_balance()}"
# Objects
b1 = BusinessAccount("Ali", 1000, "Upwork")
b2 = BusinessAccount("Sana", 2000, "Amazon")
i1 = IndividualAccount("Ahmed", 1500, "32304-123987-2")

class BankAccount():
     def __init__(self, name:str):
          self.name = name 
          self.balance = 1000

     def deposit(self, amount:int):
          self.balance += amount 
     def withdraw(self, amount:int):
          if amount <= self.balance:
               self.balance -= amount
                   
class BusinessAccount(BankAccount):
     def __init__(self, name:str, company_name:str):
          super().__init__(name)
          self.company_name = company_name
b1 = BusinessAccount("Ali", "Upwork")
b2 = BusinessAccount("Sana", "Amazon")
b1.deposit(500)
print(b1.balance)
b1.withdraw(300)
print(b1.balance)


        