#perfect number-->if the sum of the factors of the number(including 1 excluding itself) is equal to the number itself
#example 6
#factors 1,2,3
#sum of factors =number itself
s=0
n=int(input("enter the number:"))
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print("perfect number")
else:
    print("not a perfect number")
