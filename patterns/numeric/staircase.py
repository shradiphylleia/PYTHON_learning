##1
##2 2 2
##3 3 3
##4 4 4 4 4
##5 5 5 5 5
##6 6 6 6 6 6 6
#odd numbers are printed the same time
#even numbers are printed +1 time
for i in range(1,7):
    if i%2!=0:
        for j in range(1,i+1):
            print(i,end=" ")
    else:
        for j in range(1,i+2):
            print(i,end=" ")
    print("")
