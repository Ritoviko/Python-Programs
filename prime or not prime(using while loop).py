n = int(input("Enter the number: "))
m = 0
if n==0 or n == 1:
    print("Not a Prime number")
else:
    i = 2
    while(i<n):
        if n%i==0:
            m = m+1
        i = i+1

if m==0:
    print("Prime")
else:
    print("Not Prime")
