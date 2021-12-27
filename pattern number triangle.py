n = int(input("Enter the range for the pattern: "))

for i in range(n+1, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
