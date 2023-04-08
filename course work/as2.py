#1
#divisible by 3 and 5 both
n=int(input("Enter number:"))
if n%3==0 and n%5==0:
    print(n,"is divisible by both 3 and 5")
else:
    print(n,"is not divisible by 3 and 5")
#2
#multiple of five or not
n=int(input("Enter number:"))
if n%5==0:
    print(n,"is multiple of 5")
else:
    print(n,"is not multiple of 5")
#3
#greatest between the two
x=int(input("Enter number:"))
y=int(input("Enter number:"))
if x!=y:
    print("The greatest between the entered number is:",max(x,y))
else:
    print("The numbers are equal")
#4
#greatest among three
x=int(input("Enter number:"))
y=int(input("Enter number:"))
z=int(input("Enter number:"))
print("The greatest among the three entered numbers is:",max(x,y,z))
#5
#real roots or imaginary
a=int(input("Enter coefficient of x^2:"))
b=int(input("Enter coefficient of x:"))
c=int(input("Enter constant:"))
d=b*b-4*a*c
if d>=0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")
#6
#leap year or not
y=int(input("Enter the year to check leap or not"))
if ((y%4==0 and y%100!=0) or  (y%400==0)):
    print(" Entered year is Leap year")
else:
    print("Entered year is not Leap year")
#7
#input date print next date
#8
#grade year
name=input("Enter name of student:")
rnum=input("Enter roll number of student:")
sid=input("Enter sap id of student")
course=input("Enter name of the course:")
sem=int(input("Enter  the semester:"))
pds=float(input("Enter marks of PDS"))
python=float(input("Enter marks of Python"))
chem=float(input("Enter marks of Chemistry"))
eng=float(input("Enter marks of English"))
phy=float(input("Enter marks of Physics"))
per=((pds+python+chem+eng+phy)/300)*100
cgpa=per/10
grade=""
if cgpa>=0 and cgpa<=3.4:
    grade="F"
elif cgpa>=3.5 and cgpa<=5.0:
    grade="C+"
elif cgpa>=5.1 and cgpa<=6.0:
    grade="B"
elif cgpa>=6.1 and cgpa<=7:
    grade="B+"
elif cgpa>=7.1 and cgpa<=8:
    grade="A"
elif cgpa>=8.1 and cgpa<=9:
    grade='A+'
else:
    grade='A'
print("--------GRADESHEET-------")
print("NAME:",name,end="\t"*2)
print("SAPID:",sid,end="\n")
print("ROLL NUMBER",rnum,end="\t"*2)
print("COURSE",course,end="\n")
print("SEM:",sem)
print("SUBJECT NAME:\t MARKS")
print("PDS:\t",pds)
print("PYTHON:\t",python)
print("CHEMISTRY:\t",chem)
print("ENGLISH:\t",eng)
print("PHYSICS:\t",phy)
print("PERCENTAGE:\t",per)
print("CGPA:\t",cgpz)
print("GRADE:\t",grade)
#4
#1
#factorial of a number
f=1
x=int(input("enter the number for which you want to find factorial:"))
for i in range(x,0,-1):
    f=f*i
print("the factorial of",x,"is",f)
#2
#armstrong
n=int(input("enter the number:"))
d=0
s=0
temp=n
while n!=0:
    d=n%10
    s=s+(pow(d,3))
    n=n//10
if s==temp:
    print("armstrong number")
else:
    print("not an armstrong number")
#3
#fibonacci--given number of terms
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
#4
#prime number
c=0
x=int(input("enter the number:"))
for i in range(1,x+1):
    if x%i==0:
        c=c+1
if(c==2):
    print("the entered number is prime")
#5
#palindrome number--->reverse of number==original number
n=int(input("enter the number:"))
d=r=0
temp=n
while n!=0:
    d=n%10
    r=r*10+d
    n=n//10
if r==temp:
    print("palindrome number")
else:
    print("mot a palindrome number")
#6
n=int(input("Enter number"))
s=0
d=0
while n!=0:
    d=n%10
    s=s+d
    n=n//10
print("The sum of the digits of the entered number is:",s)
#7
print("The numbers between range 1 to 100 divisble by 5 and 7 are:",end="")
for i in range(1,101):
    if i%5==0 and i%7==0:
        print(i,end=" ")
#8
s=input("Enter string")
print(s.upper())
#9
#prime in range entered by user
for i in range(1,101):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
        if c==2:
            print(j)
        else:
            pass
#10
#table
n=int(input("Enter the number to:"))
for i in range(1,11):
    print(n,'*',i'=',(n*i))

