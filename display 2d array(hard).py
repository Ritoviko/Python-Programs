import array as a

n=int(input())
arr = a.array('i')
for i in range(n):
    m = int(input())
    arr.append(m)
n_row = 3
for i in range(0, len(arr)):
    if i%((len(arr))/n_row)==0:
        print()
    print(arr[i], end=" ")
