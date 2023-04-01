#max and min element in list
l=list()
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    l.append(int(input("enter number in the list:")))
print("The maximum element is:",max(l),"the minimum element is:",min(l))
#without function
g=l[0]
s=l[0]
for i in range(0,n):
    if l[i]>g:
        g=l[i]
    else:
        s=l[i]
print("largest",g,"smallest",s)
