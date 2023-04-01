#twisted prime
def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return 1
    else:
        return 0
n=int(input("enter number:"))
x=isprime(n)
if x==1:
    #reverse
    d=0
    r=0
    temp=n
    while temp!=0:
        d=temp%10
        r=r*10+d
        temp=temp//10
    y=isprime(r)
    if y==1:
        print("twisted prime")
    else:
        print("not twisted prime")
else:
    print("entered number is not prime")
