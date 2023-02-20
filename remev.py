n=int(input("Enter the number of elements:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
   ele=int(input())
   if(ele%2==1):
      list.append(ele)
print(list)