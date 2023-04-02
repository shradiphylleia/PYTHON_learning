##Downward full Pyramid Pattern of star
## * * * * * * 
##  * * * * * 
##   * * * * 
##    * * * 
##     * * 
##      *
s=10
for i in range(6,0,-1):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end=" ")
    s=s+1
    print("")
