#sample input:PYTHON
#sample output:
#P
#P Y
#P Y T
#P Y T H
#P Y T H O
#P Y T H O N
s=input("enter word:")
for i in range(1,len(s)+1):
    for j in range(0,i):
        print(s[j],end=" ")
    print("")
    
