#second largest_list
l=list()
length=int(input("enter the number of terms:."))
for i in range(0,length):
    l.append(int(input("enter value:")))
g=max(l)
g2=l[0]
for i in range(0,len(l)+1):
    if g2<g and g2>l[i]:
        g2=l[i]
    else:
        continue
print("second greatest element is:",g2)
