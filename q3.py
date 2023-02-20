x=int(input("Enter the limit:"))
print("Enter the number of elements:")
for i in range(0,x):
    a=int(input())
    if(a>100):
       p="over"
       print(p)
    else:
        print(a)