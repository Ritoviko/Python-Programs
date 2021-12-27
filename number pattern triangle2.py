n = int(input("Enter the range of the pattern: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("\r")
