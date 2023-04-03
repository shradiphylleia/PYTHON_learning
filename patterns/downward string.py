##P Y T H O N
##  P Y T H O
##    P Y T H
##      P Y T
##        P Y
##          P
s="PYTHON"
space=0
for i in range(6,0,-1):
    print("  "*space,end="")
    for j in range(0,i):
        print(s[j],end=" ")
    space+=1
    print("")
