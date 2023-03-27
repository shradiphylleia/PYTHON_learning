#factors of a number
#list--nested list--even prime---odd prime
le=[]
lo=[]
l=[]
def factors(x):
    for i in range(1,x+1):
        if x%i==0:
            if i%2==0:
                le.append(i)
            else:
                lo.append(i)
    l=[le,lo]   
    return l
x=int(input("enter the number:"))
print(factors(x))
