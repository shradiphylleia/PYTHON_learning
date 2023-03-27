#clear list
l=list()
try:
    while True:
        l.append(int(input("enter value in list:")))
except:
    print(l)
#method 1
l.clear()
print("method 1",l)
#method 2
l=[1,2,3,4]
print(l)
l=[]
print("method 2",l)
#method 3
l=[1,2,3,4]
del l[:]
print("method 3",l)
