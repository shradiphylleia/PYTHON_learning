#capitalize first and last character of the words of the string
s=input("Enter the string:")
s=s.split(" ")
for word in s:
    word=word[0].upper()+word[1:-1]+word[-1].upper()
    print(word)
