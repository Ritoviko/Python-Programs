low = int(input("Enter the starting range: "))
high = int(input("Enter the ending range: "))

for i in range(low, high+1):
    flag = 0
    if i == 0 or i == 1:
        flag +=1
    else:
        for j in range(2, i):
            if i%j==0:
                flag +=1

    if flag==0:
        print(i)
