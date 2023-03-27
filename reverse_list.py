#reverse a list
l=list()
try:
    while True:
        l.append(int(input("enter value:")))
except:
    print(l)
#method 1--reverse function
l.reverse()
print("reversed:",l)
#method 2--slicing
l=[1,2,3,4]
print("reverse:",l[::-1])
