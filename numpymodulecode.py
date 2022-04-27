import numpy as np
a = np.array([1, 2, 3, 5, 4])
arr = np.array([[1,2,3,4],[5,6,7,8], [9, 10, 11, 12]])
print(a)
print()
print(a.shape)
print()
print(arr)
print()
print(arr.shape)
print()

m = int(input("Enter the value: "))
r = int(input("Enter the row value: "))
c = int(input("Enter the column value: "))
n = np.full([r,c], m)
print(n)


