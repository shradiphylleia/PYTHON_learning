x=input()
c=d=0
for i in range(0,len(x)):
    if x[i].isalpha()==True:
        c=c+1
    if x[i].isdigit()==True:
        d=d+1
print(c,d)
