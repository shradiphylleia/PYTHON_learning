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
