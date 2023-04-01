#duck number-->a number is siad to be duck number if zero is present in the number
n=int(input("enter a number:"))
c=d=0
while n!=0:
    d=n%10
    if(d==0):
        c=c+1
    n=n//10
if c!=0:
    print("duck number")
else:
    print("not a duck number")
