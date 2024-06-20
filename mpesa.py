class Account:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance= balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f'{amount } deposited successfully. New balance is {self.balance}')
        else:
            print('Amount should be greater than zero')
    def withdraw(self,amount):
        if amount<=0:
            print('Invalid inputs')
        elif amount>self.balance:
            print('Insufficient funds')
        else:
            self.balance-=amount
            print(f'{amount} withdrawn successfully. New balance is {self.balance}')
    def __str__(self):
        return f"Account holder: {self.account_holder}\nBalance:{self.balance}"
class SavingsAccount(Account):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        print(f'Interest added successfully. New balance is {self.balance} ')
    def __str__(self):
        return (f'Savings account holder: {self.account_holder}\nBalance: {self.balance},'
                f'interest rate:{self.interest_rate}')
acc=Account('Jack Siso', 10000)
acc.deposit(2000)
acc.withdraw(7000)
acc.withdraw(-500)
print(acc)
save=SavingsAccount('Jack Siso', 1000, 14)
save.deposit(500)
save.withdraw(300)
save.add_interest()
print(save)