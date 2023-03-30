#swapping with and without third variable
#this program also demonstrates how to take input

#implicitly taken as string type conversion required
a=int(input("enter first number:"))
b=int(input("enter second number:"))
#temp variable used
c=a
a=b
b=c
print("swapped value\n value of first variable:",a,"value of second variable:",b)

#without third variable
#apporach addition and subtarction operation used
x=int(input("enter first number:"))
y=int(input("enter second number:"))
x=x+y
y=x-y
x=x-y
print("swapped value\n value of first variable:",x,"value of second variable:",y)
