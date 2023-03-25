l=[]
i=0
def apperance():
    last=int(input("enter the number of terms:"))
    for i in range(0,last):
        val=int(input("enter the value to be entered in the list:"))
        l.append(val)
    for i in range(0,last):
        print(l[i],l.count(l[i]),sep=":")
    
apperance()
