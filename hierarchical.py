class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self, amount):
        if amount<=self.balance:
            self.balance+=amount
            self.display_balance()
        else:
            print("insufficient")
        
    def withdraw(self, amount):
        self.balance-=amount
        self.display_balance()
    def display_balance(self):       
        print("Your balance :", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("interest added:", interest)
        self.display_balance()

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.display_balance()
        else:
            print("Withdrawal exceeds overdraft limit")
obj01=SavingsAccount("chandu", 4000, 2)
obj01.add_interest()
obj01.display_balance()
obj01.withdraw(1000)
obj01.deposit(2000)
obj02=CurrentAccount("addd",200, 3000)
obj02.withdraw_with_overdraft(1000)