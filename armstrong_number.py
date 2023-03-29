#armstrong--->sum of the cube of the digits of the number is equal to the original number
#example-->153--->1+125+27=153
n=int(input("enter the number:"))
d=0
s=0
temp=n
while n!=0:
    d=n%10
    s=s+(pow(d,3))
    n=n//10
if s==temp:
    print("armstrong number")
else:
    print("not an armstrong number")
