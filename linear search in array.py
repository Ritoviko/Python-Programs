import array as a

def linearsearch(arr, d):

    for i in range(len(arr)):
        if d == arr[i]:
            print(i)
            return
    print(-1)


n = int(input("Enter the size of the array: "))

arr = a.array('i')
print("Enter the elements of the array: ")
for i in range(n):
    m = int(input())
    arr.append(m)

d = int(input("Enter the element to be found: "))
linearsearch(arr, d)
