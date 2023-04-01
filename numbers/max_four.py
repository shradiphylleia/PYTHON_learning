num=int(input("enter four digit number:"))
m=0
while num!=0:
    d=int(num%10)
    if(d>m):
        m=d
    num=num/10
print("maximum number",m)
