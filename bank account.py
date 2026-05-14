class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount()

account.deposit(5000)
account.withdraw(2000)
account.check_balance()