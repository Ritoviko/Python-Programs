n = int(input("Enter any number: "))

out = 0
i = 1

while True:
    flag = 0
    flag2 = 0
    nxt = n+i
    prev = n-1
    for j in range(1, nxt):
        if nxt%j==0:
            flag+=1

    for k in range(1, prev):
        if prev%k==0:
            flag2+=1

    if flag <=1:
        print(nxt)
        out = 1
    if flag2 <=1:
        print(prev)
        out = 1

    if out ==1:
        break
    else:
        i+=1


