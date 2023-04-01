l=[]
try:
    while True:
        l.append(int(input("enter the value:")))
except:
    #approach--equate
    l2=l;
print("cloned list:",l2)
#approach--function
l3=l.copy()
print("cloned list:",l3)
