n = int(input())
row = 1
current = 1
while(n>=(row*(row+1)/2)):
    for i in range(current,1+((row*(row+1)//2))):
        print(i, end=" ")
        current+=1
    print()
    row+=1


