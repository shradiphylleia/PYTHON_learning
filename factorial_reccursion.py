def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
s=fact(int(input("enter the number for factorial:")))
print(s)
