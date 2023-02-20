n=int(input("Enter a value"))
fact=1
if(n<0):
    print("Fact does not exist")
elif(n==0):
 print("The fact of o is 1")
else:
    for i in range(1,n + 1):
        fact=fact*n
        print("The fact of",n,"is",fact)