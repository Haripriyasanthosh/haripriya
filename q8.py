n=int(input("enter the number:"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print("number is not prime")
        else:
            print("number is prime")