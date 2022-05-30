def binary(arr, x, n):
    m = (n//2)-1
    mid = arr[m]
    if mid>x:
        for i in range(m,-1,-1):
            if arr[i]==x:
                return i
    elif mid<x:
        for i in range(m, len(arr)):
            if arr[i]==x:
                return i
    elif mid == x:
        return m
    else:
        return -1

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
x = int(input())
y = binary(arr, x, n)
print(y)
