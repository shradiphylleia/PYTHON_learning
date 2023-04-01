#tens didgit twice that of units digit
#21 63 84 etc
for i in range(10,1000):
    d=u=t=0
    u=i%10
    t=i//10
    if t==2*u:
        print(i)
        
