class bank:
    def __init__(self,name,accno,acctype):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=0
    def showaccount(self):
        print("name of account holder",self.name)
        print("account number",self.accno)
        print("account type",self.acctype)
        print("The balance",self.balance)
    def deposit(self,d1):
        self.bal=self.bal+deposit
        return self.bal
    def withdrawl(self,w1):
        self.bal=self.bal-withdrawl
        return self.bal
n=input("enter your name")
a=int(input("enter your account number"))
b=input("enter your account type")
o=bank(n,a,b)
o.showaccount()
while[True]:
    print("\nmenu")
    print("\n 1.deposit")
    print("\n 2.withdrawl")
    c=int(input("enter your choice"))
    d=o
    if(c==1):
     d=int(input("enter the amount to be deposit"))
     print("your total balance amount is:",o.deposit(d))
    elif(c==2):
        n=int(input("enter the amount to be withdrawn"))
        if(w>d):
            print("insufficient balance")
        else:
            print("your total balance amount is",o.withdrawl(w))
    else:
        print("invalid choice")





