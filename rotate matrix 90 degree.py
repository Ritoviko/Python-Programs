import numpy as np

a = np.array([[10, 11, 12],[20, 21, 22],[30, 31, 32]])

print(a)

b=a

for i in range(3):
    b[:,3-1-i] = a[i, :]
    

print(b)
