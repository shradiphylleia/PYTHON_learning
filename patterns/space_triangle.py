##          1 
##        1 2 
##      1 2 3 
##    1 2 3 4 
##  1 2 3 4 5 
for i in range(1,6):
    num=1
    for j in range(6,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print(num,end=' ')
            num+=1
    print("")
