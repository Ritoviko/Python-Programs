n = int(input("Enter the number: "))
flag = False
if n==0 or n == 1:
    flag = True
else:
    i = 2
    while(i<n):
        if n%i==0:
            flag = True
        i = i+1

if flag==False:
    print("Prime")
else:
    print("Not Prime")
