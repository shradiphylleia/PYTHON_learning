print("i\ti**2\ti**4\ti**8\ti**16")
for i in range(1,6):
    print(i,end="\t")
    for j in range(1,5):
    #2^1 2^2 2^3
        p=2**j
    #i**2^1...
        print((i**p),end="\t")
    print("")
