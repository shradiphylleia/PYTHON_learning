##1  2  3  4  5
##6  7  8  9
##10 11 12
##13 14
##15
n=1
for i in range(5,0,-1):
    for j in range(1,i+1):
        if i>=4:
            print(n,end="  ")
        else:
            print(n,end=" ")
        n+=1
    print("")
