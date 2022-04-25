import array as a

n=int(input())
arr = a.array('i')
for i in range(n):
    m = int(input())
    arr.append(m)
    
for i in range(1, len(arr)+1):
    print(arr[i-1], end=" ")
    if i%3==0:
        print()
