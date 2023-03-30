#prime number
#a number is said to be prime if it is only divisible by 1 and itself
c=0
x=int(input("enter the number:"))
for i in range(1,x+1):
    if x%i==0:
        c=c+1
if(c==2):
    print("the en
          tered number is prime")
