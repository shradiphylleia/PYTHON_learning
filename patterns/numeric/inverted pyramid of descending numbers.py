##5 5 5 5 5 
##4 4 4 4 
##3 3 3 
##2 2 
##1
## inverted pyramid of descending numbers
b=5
for i in range(5,0,-1):
    for j in range(0,i):
        print(b,end=" ")
    b=b-1
    print("")
