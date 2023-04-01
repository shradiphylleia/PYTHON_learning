##mirrored right triangle
##Right triangle pyramid of Stars
##        * 
##      * * 
##    * * * 
##  * * * * 
##* * * * * 
for i in range(1,6):
    for j in range(5,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print('*',end=" ")
    print(" ")
