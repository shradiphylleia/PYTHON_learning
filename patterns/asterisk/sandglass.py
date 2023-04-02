##sandglass pattern
##* * * * * 
## * * * * 
##  * * * 
##   * * 
##    * 
##    * 
##   * * 
##  * * * 
## * * * * 
##* * * * *
s=0
for i in range(5,0,-1):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end=" ")
    s=s+1
    if(i!=1):
        print("")
    else:
        continue
s=5
for i in range(0,6):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end=" ")
    s=s-1
    print("")
