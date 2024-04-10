class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deporit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficeint funds!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


class InterestBearingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        Account.__init__(self, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest_rate(self):
        return self.balance * self.interest_rate


class Transactions:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, transaction):
        self.transactions.append(transaction)

    def transaction_history(self):
        for tr in self.transactions:
            print(tr)


class SavingsAccount(InterestBearingAccount, Transactions):
    def __init__(self, account_number, balance, interest_rate):
        InterestBearingAccount.__init__(self, account_number, balance, interest_rate)
        Transactions.__init__(self)


savings = SavingsAccount("SA001", 5000, 0.08)
savings.deporit(2500)
# 7500
savings.withdraw(650)
interest = savings.calculate_interest_rate()
balance = savings.get_balance()

print("Balance: {}, Interest:{}".format(balance, interest))
