#equilateral triangle
##            * 
##           * * 
##          * * * 
##         * * * * 
##        * * * * * 
##       * * * * * * 
##      * * * * * * * 
s=12
for i in range(1,8):
    print(" "*s,end="")
    for j in range(1,i+1):
        print("*",end=" ")
    s=s-1
    print("")
