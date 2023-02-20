count=100
x=int(input("Enter the starting year:"))
for i in range(x,100):
    if((i%400==0) or (i%100!=0) and (i%4==0)):
        if(i%2==0):
            print("The following are the even leap years")
    print(i)