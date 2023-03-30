#prime in range entered by user
#skills set demonstrated
#making a function---passing parameters
#outoput as a list
def prime_range(x,y):
    l=[]
    for i in range(x,y):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            l.append(i)
    return l
x=int(input("enter the lower bound:"))
y=int(input("enter the upper bound:"))
print(prime_range(x,y))
