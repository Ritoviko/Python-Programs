import array as a

nr = int(input("enter row of array 1: "))
nc = int(input("enter column of array 1: "))


arr = a.array('i')
arr1 = a.array('i')
sum = a.array('i')

for i in range(nr*nc):
    arr.append(int(input()))

mr = int(input("enter row of array 2: "))
mc = int(input("enter column of array 2: "))

for i in range(mr*mc):
    arr1.append(int(input()))

for i in range(nr*nc):
    sum.append(arr[i]+arr1[i])

for i in range(len(sum)):
    if i%nr == 0:
        print()
    print(sum[i], end=" ")
