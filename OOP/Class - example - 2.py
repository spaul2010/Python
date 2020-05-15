# ------------------------------------------------------------------------------
#    Class Example - 2
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#    Class Definition
# ------------------------------------------------------------------------------
class Account:
    """Simple account class with balance"""
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is = {}".format(self.balance))


if __name__ == '__main__':
    paul = Account('Paul', 0)
    paul.show_balance()

    paul.deposit(1000)
    paul.show_balance()
    paul.withdraw(500)
    paul.show_balance()

    paul.withdraw(1500)



