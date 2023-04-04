#to print even length words of the string
s=input("Enter the string:")
s=s.split(" ")
for word in s:
    if len(word)%2==0:
        print(word)
    else:
        continue
