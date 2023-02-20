string1=input("enter the first string")
string2=input("enter the second string")
a=string1[0]
b=string2[0]
new_string1=b+string1[1:]
new_string2=a+string2[1:]
print(new_string1+' '+new_string2)