class BankAccount:

    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        amount = float(input("Enter deposit ammount: "))
        self.account_balance +=  amount

    def withdraw(self, amount):
        amount = float(input("Enter withdraw amount: "))
        if self.account_balance < amount:
            print("Insufficient funds")
        else:
            self.account_balance -= amount

    def display_balance(self):
        print(f"Current Balance:{self.account_balance}")