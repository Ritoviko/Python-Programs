import array as a

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

arr = a.array('i')

for i in range(0, n*m):
    arr.append(int(input()))

for i in range(0, len(arr)):
    if i%n==0:
        print()
    print(arr[i], end=" ")
