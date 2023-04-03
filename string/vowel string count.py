#counting number of vowels
s=input("enter word:")
vowel=0
for c in s:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
        vowel+=1
    else:
        pass
print("the number of vowels in the string are",vowel)    
