#neon number--->sum of the digits of the square of the number is equal to number itself
#example-->9 9*9=81
#8+1=9
n=int(input("enter the number:"))
d=0
s=0
sq=n*n
while sq!=0:
    d=sq%10
    s=s+d
    sq=sq//10
if s==n:
    print("neon number")
else:
    print("not a neon number")
