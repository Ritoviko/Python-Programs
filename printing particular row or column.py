import numpy as np

r = int(input("Row value: "))
c = int(input("Column value: "))
a = np.full([r,c], 1)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        n = int(input())
        a[i][j] = n
print(a)
print()

nr = int(input("Enter the row to be accessed: "))
nc = int(input("Enter the column to be accessed: "))

for i in range(c):
    if i<c-1:
        print(a[nr-1][i], end=",")
    elif i==c-1:
        print(a[nr-1][i], end="")
        
print()

for i in range(r):
    if i<r-1:
        print(a[i][nc-1], end=",")
    elif i==r-1:
        print(a[i][nc-1], end="")
print()

