class bank_account():
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, amountdp):
        self.balance = self.balance+amountdp
        print("Transaction accepted")
        print("Current funds " + str(self.balance))
    def withdraw(self, amountwt):
        if(self.balance-amountwt >0):
             self.balance = self.balance-amountwt
             print("Transaction accepted")
             print("Current funds " + str(self.balance))
        else:
            print("Transaction not accepted")
            print("Current funds " + str(self.balance))

print("Enter your name")
owner = str(input())

print("Enter initial balance")
balance = int(input())
acc1 = bank_account(owner, balance)

print("How much do you want to deposit?")
amountdp = int(input())
acc1.deposit(amountdp)
print("How much do you want to deposit?")
amountdp = int(input())
acc1.deposit(amountdp)

print("How much do you want to withdraw?")
amountwt = int(input())
acc1.withdraw(amountwt)
print("How much do you want to withdraw?")
amountwt = int(input())
acc1.withdraw(amountwt)