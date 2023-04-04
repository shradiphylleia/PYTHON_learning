#A string is said to be symmetrical if both the halves of the string are the same
# A string is said to be a palindrome string if it is same when read forward or backward.
s=input("Enter string:")
l=len(s)
m=l//2
if s[0:m]==s[m:]:
    print("symmetrical")
else:
    print("not symmetrical")
#palindrome
srev=s[-1::-1]
if srev==s:
    print("palindrome")
else:
    print("not palindrome")
