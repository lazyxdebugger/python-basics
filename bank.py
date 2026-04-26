class InsufficientBalanceError(Exception):
    pass

class bank_acc:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("deposited:",amount)
        print("total balance:",self.balance)

    def withdraw(self,amount):
        try:
            if amount>self.balance:
                raise InsufficientBalanceError("amount to be withdrawed is greater than the actual balance.")
            else:
                self.balance-=amount
                print("withdrawed:",amount)
                print("total balance:",self.balance)
        except InsufficientBalanceError as e:
            print(e)

balance=float(input("enter the balance:"))            
obj=bank_acc(balance)

depo=float(input("enter the amount to deposit:"))
obj.deposit(depo)

withd=float(input("enter the amount to withdraw:"))
obj.withdraw(withd)
