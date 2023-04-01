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
c=input("character to count:")
print(str.count(c))

#capitalize first letter of string
str=input("enter the string:")
print(str.capitalize())
#capitalize ech letter of a string
print(str.title())

#f-string string interpolation
direction="east"
fact="sun rises in"
f'{fact} {direction}.'
#interpolating using format() appended at the end
day="jan 1st"
event="new year"
"we are celebrating {} {}".format(day,event)

#check if all number string
str=input("enter string:")
print(str.isnumeric())
#check if all alpha
print(str.isalpha())
#check all lower case
str=input("enter string")
print(str.islower())
#check if first character is lower case
print(str[0].islower())
#check all upper case
print(str.isupper())
#check if first character upper case
print(str[0].isupper())
#check alphanumeric
print(str.isaplnumeri())
#all whitespace string
print(str.isspace())
#check starts with ends with
print(str.startswith('s'))
print(str.endswith('a'))

#upper or lower case
print(str.upper())
print(str.lower())

#upper a paritcular index
print(str[0].upper())
#upper first and last
new=str[0].upper()+str[1:-1]+str[-1].upper()

#strip whitespaces
print(str.lstrip())
print(str.rstrip())
print(str.strip())

#replacing all instances
s="sun moon planets"
s.replace("planets","stars")
 
