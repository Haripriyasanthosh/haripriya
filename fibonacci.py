a=int(input("Enter the limit"))
t1=0
t2=1
count=0
while(count<a):
    print(t1)
    t=t1+t2
    t1=t2
    t2=t
    count=count+1