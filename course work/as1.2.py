x=9
y=7
add=x+y
sub=x-y
pro=x*y
div=x/y
print("Addition of",x,"and",y,":",add)
print("Subtraction of",y,"from",x,":",sub)
print("Product of",x,"and",y,":",pro)
print("Division of ",x,"and",y,"yields:",div)
#2
radius=float(input("Enter the radius of circle:"))
area=(22/7)*radius*radius
print("Area of circle is:",area)
#3
x=int(input("Enter value of variable x:"))
y=int(input("Enter value of variable y:"))
print((x+y)*(x+y))
#4
p=float(input("enter the dimensions of prependicular:"))
b=float(input("enter the dimensions of base:"))
c=(p*p)-(b*b)
print("Hypotenuse of the triangle is=",c)
#5
p=float(input("Enter principal amount:"))
r=float(input("Enter the rate:"))
t=int(input("Enter the time duration in years:"))
si=(p*r*t)/100
print("The simple interest incurred on",p,"is=",si)
#6
x=5
y=6
z=7
s=(x+y+z)/2
area=pow((s*(s-x)*(s-y)*(s-z)),0.5)
print("Area of the traingle with sides",x,y,z,"is=",area)
#7
#8
x=15
y=17
print("Value of variable x and y before swapping:",x,y)
x=x+y
y=x-y
x=x-y
print("Value of variable x and y after swapping:",x,y)
#9
s=0
n=int(input("enter the number of natural numbers you wish to add:"))
for i in range(1,n+1):
    s=s+n
print("The sum of first",n,"natural numbers is=",s)
#10
#11
x=int(input("Enter the number to find its left shift and right shift values:"))
nl=int(input("Enter the number of left shift:"))
nr=int(input("Enter the number of right shift:"))
l=x<<nl
r=x>>nr
print("Left shift of the number is:",l)
print("Right shift of the number is:",r) 
#12
t=(10,20,56,78,89)
num=int(input("enter number:"))
if num in t:
    print("Entered number is present in sequence")
else:
    print("Entered number is not present in sequence")
#13
s="shraddha"
c=str(input("enter the character to check whether the character is in the string:"))
if c in s:
    print("Character is present in string")
else:
    print("Character is not present in string")
