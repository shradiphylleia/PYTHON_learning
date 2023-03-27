#sum of elements in a list
l=[]
def sum_list(l):
    s=0
    for i in range(0,len(l)):
        s=s+l[i]
    return s
def pro_list(l):
    p=1
    for i in range(0,len(l)):
        p=p*l[i]
    return p
n=int(input("enter the number of terms in list:"))
for i in range(0,n):
    l.append(int(input("enter the number:")))
print(sum_list(l))
print(pro_list(l))
