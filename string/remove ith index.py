#Remove the ith character from the string
s=input("Enter the string:")
n=int(input("Enter the index of character which you wish to remove:"))
new_s=""
for i in range(0,len(s)):
    if i==n:
        continue
    else:
        new_s=new_s+s[i]
print("The new string after removal of the character at ith index is:",new_s)
