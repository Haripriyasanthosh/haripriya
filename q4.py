a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if(a>b) and (a>c):
    print("a is larger")
elif(b>a) and (b>c):
    print("b is larger")
else:
    larger=c
print("The larger number is",larger)