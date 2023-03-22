#factorial of a number
#factorial of 5
#denoted by 5!=5*4*3*2*1=120
#take input----loop to go from number to 5----multiply
f=1
x=int(input("enter the number for which you want to find factorial:"))#default taken in as string therefore typecasting
for i in range(x,0,-1):# range function(start,stop,step) in membership operator
    f=f*i
print("the factorial of",x,"is",f)
    
