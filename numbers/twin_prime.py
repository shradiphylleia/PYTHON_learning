#twin prime--->the difference between the two prime numbers is 2
#[3,5] [5,7] [11,13] [17,19]
for i in range(3,50):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        #prime therefore look for +2 prime
        s=i+2
        c2=0
        for j in range(1,s+1):
            if s%j==0:
                c2=c2+1
        if c2==2:
            print(i,s)
#can be done using function that can be called twice
#try to optimize---ask 6n+1 6n-1
# 3 5 7 11 17 19
