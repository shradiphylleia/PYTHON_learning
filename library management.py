#identical library books are placed one over the other forming a layer of books
#students sequentially take thr topmost book whereas the student done with the the book put it back on the layer
book=10
def deposit():
    book=book+1;
    return book
def borrow():
    book=book-1
    return book:
def display():
    print("the number of books on the shelf",book)
c=int(input("enter 1 to deposit book and 2 to borrow book 3 to display the number of books"))
if c==1:
    deposit()
elif c==2:
    if book==0:
    print("no book on shelf to issue")
    else:
    borrow()
elif c==3:
    display()
else:
    print("enter valid choice")
