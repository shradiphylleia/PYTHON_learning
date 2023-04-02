##Right down mirror star Pattern
##*****
## ****
##  ***
##   **
##    *
s=0
for i in range(5,0,-1):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end="")
    s=s+1
    print("")
