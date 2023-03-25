#printing numbers--->square
def sq(x,y):
    for i in range(x,y):
                    sqrt=int(pow(i,0.5))
                    if(i>1 and i==(sqrt*sqrt)):
                        print(i)
x=int(input("enter the numbers:"))
y=int(input("enter the numbers:"))
sq(x,y)

