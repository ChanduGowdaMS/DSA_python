class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self, amount):
        if amount<=self.balance:
            self.balance+=amount
            print("Your balance :", self.balance)
        else:
            print("insufficient")
        
    def withdraw(self, amount):
        self.balance-=amount
        print("Your balance :", self.balance)
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

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

obj01=SavingsAccount("chandu", 4000, 2)
obj01.add_interest()
obj01.display_balance()
obj01.withdraw(1000)
obj01.deposit(2000)