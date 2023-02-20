for i in range(1,5):
    for j in range(0,i):
        print(i,end="")
    print("")
c=5
x=3
for i in range(1,4):
    print(" "*i,end="")
    for j in range(x,0,-1):
        print(c,end="")
    print("")
    c=c+1
    x=x-1
