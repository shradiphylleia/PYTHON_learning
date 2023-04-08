r=int(input("rows:"))
c=int(input("column:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        print(i*j,end=" ")
    print("")
