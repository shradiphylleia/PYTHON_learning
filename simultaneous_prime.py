#fifty simultaneous prime numbers
n=int(input("enter the number:"))
s=int(input("enter the number of simultaneous prime number you want:"))
k=0
while k<s:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print(n," ")
        k=k+1
    n=n+1
    
    
