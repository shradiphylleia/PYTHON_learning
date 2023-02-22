#string manipulations

#to check if the string begins with capital letter or not
#example The Man
#istitle function:gives True or False accordingly print*
print("to check if the first character of the entered string is captial")
str=input("enter the string:")
print(str.istitle())

#string has a particular string
print("string has a particular substring")
str=input("enter the string:")
substr=input("enter sub string:")
print(substr in str)

#index of first occurence of substring
print("index of particular substring")
str=input("enter the string:")
substr=input("enter sub string:")
print(str.find(substr))
print(str.index(substr))
#searching specific part of substring
#index("sub",beg,end) excluded
print(str.index(substr,1,4))

#count the total number of characters in a string
print("count character")
str=input("enter the string:")
c=input("character to count")
print(str.count(c))

#capitalix=z first letter of string
str=input("enter the string:")
print(str.capitalize())

#f-string string interpolation
direction="east"
fact="sun rises in"
f'{fact} {direction}.'

