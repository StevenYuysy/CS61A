class Account ():
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient Funds'
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


a = Account('someone')
a.holder  # someone
a.balance  # 0
a.deposit(10)  # 10
a.withdraw(10)  # 0
a.withdraw(20)  # Insufficient Funds
a.holder = 'b'
