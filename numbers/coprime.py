#co-prime-->common
#exapmle 14 15
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        c=c+1
if c==1:
    print(a,b,"are co-prime numbers")
else:
    print(a,b,"are not co-prime numbers")
