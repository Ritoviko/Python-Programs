n = int(input())
num1 = 0
num2 = 1

for i in range(1, n+1):
    for j in range(0, i):
        temp = num1+num2
        if i==1:
            print(num1, end=" ")
        elif i==2:
            if j ==0:
                print(num2, end=" ")
            else:
                print(temp, end=" ")
                num1 = num2
                num2 = temp
                
        else:
            print(temp, end=" ")
            num1 = num2
            num2 = temp
    print()
