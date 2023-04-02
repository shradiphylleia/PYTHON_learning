##Left triangle pascal’s pattern
##    *
##   **
##  ***
## ****
##*****
## ****
##  ***
##   **
##    *
s=4
for i in range(1,6):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end="")
    s=s-1
    print("")
s=1
for i in range(4,0,-1):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end="")
    s=s+1
    print("")    
