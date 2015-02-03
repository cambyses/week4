class BankAccount:
    def __init__(self):
        self.balance = 0.0
    #deposit
    def deposit(self,amount):
        self.balance = self.balance + amount

    #withdraw
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount

    #transfer
    def transfer(self,amount,account):
        if amount <= self.balance:
            self.balance = self.balance - amount
            account.balance = account.balance + amount
