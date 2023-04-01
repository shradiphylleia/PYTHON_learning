#fibonacci--given number of terms
#0,1,1,2,3,5,...
#the next element is the sum of the previous and the previous two elements
#print 0 and 1---then c the sum of the pevious two---b vlaue now in a and c value now in b for further iteration
a=0
b=1
c=0
n=int(input("enter the number of terms you wish to print:"))
print(a,b,end=" ")
for i in range(0,n):
     c=a+b
     print(c,end=" ")
     a=b
     b=c
