class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew:", amount)
        else:
            print("Not enough balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)

print("Balance:", account.get_balance())
