##Print two pyramids of stars
##*  
##* *  
##* * *  
##* * * *  
##* * * * *  
##* * * * * *  
## 
##* * * * * *  
##* * * * *  
##* * * *  
##* * *  
##* *  
##*  
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
print(" ")
for i in range(6,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ") 
