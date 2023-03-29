#present in fibonacci series or not
import math
n=int(input("enter number to check if it is present in fibonacci series or not:"))
if(n!=0):
    a1=5*n*n+4
    a2=5*n*n-4
    b1=int(math.sqrt(a1))
    b2=int(math.sqrt(a2))
    if ((b1*b1==a1)or(b2*b2==a2)):
        print("the number is present")
    else:
        print("the number is not present")
else:
    print("the number is present")
