#index==value
l=[]
last=int(input("enter the number of terms you wish to enter:"))
for i in range(0,last):
    val=int(input("enter the value to be entered in the list:"))
    l.append(val)
print("the values at indices equal to the index are:")
for i in range(0,last):
                 if i==l[i]:
                     print(i)
