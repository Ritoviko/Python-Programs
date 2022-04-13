t = int(input("Enter the test cases: "))
a= []

for i in range (0, t):
    n = int(input())
    a.append(n)

for i in a:
    flag = 0

    if i==0 or i==1:
        flag = flag+1
    else:
        for j in range(2, i):
            if i%j==0:
                flag = flag+1

    if flag>0:
        print("Not Prime")
    else:
        print("Prime")
