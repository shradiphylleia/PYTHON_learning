#special number--->sum of its digit added to the product of its digit gives the number itself
#example:59
#sum of digit:5+9=14
#product of digit:5*9=45
#14+45=number itself=59
s=0
p=1
d=0
n=int(input("enter the number to check special or not:"))
temp=n
while n!=0:
    d=n%10
    s=s+d
    p=p*d
    n=n//10
if temp==(s+p):
    print("special number")
else:
    print("not a special number")
