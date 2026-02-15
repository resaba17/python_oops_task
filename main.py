#PROBLEM 1- BANK ACCOUNT
#Create base class BankAccount
#Add attributes account_number and balance
#Add deposit() and withdraw()methods
#Create SavingsAccount and CurrentAccount using inheritance
#Use encapsulation(_balance)
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance #encapsulated variable

    def deposit(self, amount):
        self._balance += amount
        print("Deposit done")

    def withdraw(self, amount):
        if amount <=self._balance:
            self._balance -= amount
            print("Withdraw successful")
        else:
            print("Not enough balance")
    def show_balance(self):
        print("Balnce:", self._balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculation_interest(self):
        interest = self._balance * self. interest_rate/100
        print("Interest:", interest)

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().___init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self._balance -amount >= self.minimum_balance:
            self._balance -= amount 
            print("Withdraw successful")
        else:
            print("Minimum balance required")

#PROBLEM 2- EMPLOYEE MANAGEMENT 
#Base class employee
#Method calculated_salary()
#Create subclasses
#Use polymorphism
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculated_salary(self):
        return self.salary
    
class RegularEmployee(Employee):
    def calculated_salary(self):
        return self.salary + 1000
    
class ContractEmployee (Employee):
    def calculated_salary(self):
        return self.salary
    
class Manager(Employee):
    def calculated_salary(self):
        return self.salary + 5000 
    
#PROBLEM 3 -VEHICLE RENTAL:
#Base class vehicle
#Attributes model and rental_rate
#Method calculate_rental
#Subclasses Car, Bike, Truck
class vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate
    
    def calculate_rental(self, days):
        return self.rental_rate * days
    
class Car(vehicle):
    pass

class Bike(vehicle):
    pass

class Truck(vehicle):
    def calculated_rental(self, days):
        return self.rental_rate + days + 200
    