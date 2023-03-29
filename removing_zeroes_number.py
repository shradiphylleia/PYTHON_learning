#removing zeroe from the number
n=int(input("enter the number:"))
d=newn=temp=0
while n!=0:
    d=n%10
    if d!=0:
        temp=temp*10+d
    else:
        pass
    n=n//10
print(temp)
d=0
while temp!=0:
    d=temp%10
    newn=newn*10+d
    temp=temp//10
print(newn)
#recursively?
#try improving the code
