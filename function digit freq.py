def freq(n, d):
    flag = 0
    while n>0:
        temp = n%10
        n = n//10
        if temp == d:
            flag+=1
    return flag


n = int(input("Enter any integer: "))
m = int(input("Enter the value to be found: "))
print(freq(n, m))
