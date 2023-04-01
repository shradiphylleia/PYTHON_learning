#search--->list
l=[]
n=int(input("enter the number of terms in the list:"))
for i in range(0,n):
    l.append(int(input("enter the number:")))
def search(l,num):
    if num in l:
        print("the number is present in the list")
    else:
        print("the number is not present in the list")
search(l,int(input("enter number to be search:")))
    
