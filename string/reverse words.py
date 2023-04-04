#reverse words in a given string
#sample input:sun rises in the east
#sample output:east in the rises sun
s=input("Enter the string:")
rev=""
w=" "
s=s+" "
for i in range(0,len(s)):
    if s[i]==" ":
        rev=w+rev
        w=" "
    else:
        w=w+s[i]
print(rev)
