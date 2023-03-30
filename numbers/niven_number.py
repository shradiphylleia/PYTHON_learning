#niven number-->divisible by sum of its digit
#example 126
#sum of digits 1+2+6=9 and the number is divisble by 9
n=int(input("enter the number:"))
temp=n
d=0
s=0
while n!=0:
    d=n%10
    s=s+d
    n=n//10
if temp%s==0:
    print("niven number")
else:
    print("not a niven number")
