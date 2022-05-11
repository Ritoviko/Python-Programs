def find(a, x, i):
    if x == a[i]:
        return i
    elif i<len(a)-1:
        return find(a, x, i+1)
    else:
        print("Element not found")
        return -1

n = int(input("Enter the size of array: "))

arr = []
print("Enter the elements for the array: ")
for i in range(n):
    print("Element", i+1, ": ")
    arr.append(int(input()))

x = int(input("Enter the element whose index to be found: "))
count = 0
Ans = find(arr, x, count)

print("Last Index: ", len(arr)-1)
print(Ans)
