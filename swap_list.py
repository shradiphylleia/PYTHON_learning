#swapping first and last
#swapping index
l=list()
n=int(input("enter the number of terms in the list:"))
for i in range(0,n):
      l.append(int(input("enter number:")))
#swap:apprach temporary variable
x=l[-1]
l[-1]=l[0]
l[0]=x
print(l)
#swap:approach 2
l[0],l[-1]=l[-1],l[0]
print(l)
#swapping index
x=int(input("enter the indices which you want to swap:"))
y=int(input("enter the indices which you want to swap:"))
l[x],l[y]=l[y],l[x]
print(l)
