import numpy as np

r = int(input("Row value: "))
c = int(input("Column value: "))
a = np.full([r,c], 1)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        n = int(input())
        a[i][j] = n

print(a)

for i in range(c):
    print(a[i][0], end="->")

for i in range(c-1, 0, -1):
    print(a[i][1], end="->")

for i in range(c):
    if i<c-1:
        print(a[i][2], end="->")
    elif i==c-1:
        print(a[i][2], end="")
