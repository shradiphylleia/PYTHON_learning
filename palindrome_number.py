#palindrome number
#a palindrome number is a number which when reversed is eqaul to the original number
#example 525
#floor division----//
rev=0
n=int(input(":to check for palindrome:\n enter the number:"))
num=n
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
if(rev==num):
    print("entered number is palindrome")
else:
    print("entered number is not palindrome")
