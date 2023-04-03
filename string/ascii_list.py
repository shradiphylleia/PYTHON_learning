#ascii code of entered word in list
str=input("enter word:")
l=list()
for c in str:
    l.append(ord(c))
print(l)
