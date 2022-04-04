class user:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self.accountBalance

    def displayUserBalance(self):
        print(f'User: {self.firstName} {self.lastName} - Balance {self.accountBalance}.')

    def transfer(self, amount, targetAcc):
        self.accountBalance -= amount
        targetAcc.accountBalance += amount
        print(self.accountBalance)
        print(targetAcc.accountBalance)


bob = user('Bob', 'Smith')
tommy = user('Tommy', 'Timber')
jimmy = user('Jimmy', 'Johnson')

bob.makeDeposit(100)
bob.makeDeposit(100)
bob.makeDeposit(100)
bob.makeWithdrawal(25)
bob.displayUserBalance()

tommy.makeDeposit(100)
tommy.makeDeposit(100)
tommy.makeWithdrawal(25)
tommy.makeWithdrawal(25)
tommy.displayUserBalance()

jimmy.makeDeposit(100)
jimmy.makeWithdrawal(25)
jimmy.makeWithdrawal(25)
jimmy.makeWithdrawal(25)
jimmy.displayUserBalance()

bob.transfer(100, jimmy)