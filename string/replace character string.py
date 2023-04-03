#replace character with another character
#sample input:computer science
#sample character you wish to replace:r
#sample character you want to replace it with:*
s=input("enter string:")
c=input("enter the character in the string you wish to replace:")
r=input("enter the character you want to replace it with:")
st=""
for ch in s:
    if ch==c:
        st=st+r
    else:
        st=st+ch
print("the new string",st)
