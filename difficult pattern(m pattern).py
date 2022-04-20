n = int(input())
space = (2*n)-2
nst = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="   ")

    for k in range(1, space):
        print(end="     ")


    if i<n:
        for k in range(j, 0, -1):
            print(k, end="  ")
        space-=2
        nst+=1
        print()
    else:
        for k in range(j-1, 0, -1):
            print(k, end="  ")
        print()
    
