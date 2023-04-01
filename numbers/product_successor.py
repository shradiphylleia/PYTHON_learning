#to find the product of successours of ven digits present in the number
n=int(input("enter a  number:"))
d=0
p=1
while n!=0:
    d=n%10
    if d%2==0:
        p=p*(d+1)
    else:
        pass
    n=n//10
print(p)
