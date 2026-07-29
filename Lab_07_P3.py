class BankAccount:
    def __init__(self,acc_num,name,balance):
        self.acc_num=acc_num
        self.name=name
        self.balance=balance
    def Deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited to account. ")
    def Withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"{amount} is withdraw from account.")
        else:
            print("Insufficient Balance!")
    def BankFees(self):
        self.balance-=self.balance*0.05
    def Display(self):
        print(f"Account No:{self.acc_num}")
        print(f"Name of the Owner:{self.name}")
        print(f"Current Balance :{self.balance}")

obj=BankAccount(205032456789,"Mehedi",20000)
obj.Display()
obj.Deposit(5000)
obj.Display()
obj.Withdraw(3000)
obj.Display()
obj.BankFees()
obj.Display()