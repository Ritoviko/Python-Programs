import numpy as np

r = int(input("Row value: "))
c = int(input("Column value: "))
a = np.full([r,c], 1)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        n = int(input())
        a[i][j] = n

print(a)
print(a.reshape(c, r))

