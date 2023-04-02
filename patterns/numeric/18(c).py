##15 14 13 12 11
##10 9  8  7
##6  5  4
##3  2
##1
n=15
for i in range(5,0,-1):
    for j in range(1,i+1):
        if n>=10:
            print(n,end=" ")
        else:
            print(n,end="  ")
        n-=1
    print("")
